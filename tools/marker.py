#!/usr/bin/env python3
"""Auto-marker for the Business 9609 revision papers.

Scans the `submissions/` folder, marks each answer file against the mark scheme
built into the content modules, and writes a Markdown feedback report next to it
(`<name>.feedback.md`).

Features
--------
* Multiple papers per file  - repeat the `paper:` header to start a new paper
  section within the same file.
* Multiple files            - every `*.md` file in submissions/ is marked and
  gets its own feedback report.
* Handwriting / images (OCR) - an answer can be a photo/scan. Either
    - reference it from your file:   `img: my-photo.jpg`  (or `![](my-photo.jpg)`)
    - or just commit image files named like `B2-Q1.jpg`, `A3-Q11b.png`,
      `7-Q5.jpg` and they are grouped and marked automatically.
  Images are read with an OCR engine (installed in the GitHub Action). A `.txt`
  reference is read directly as a typed transcription.

Marking
-------
* Knowledge / short answers -> keyword matching against the indicative content.
* Calculations              -> checks the expected numeric answer(s) appear.
* Essays / "evaluate"       -> an INDICATIVE level & mark plus a checklist and
  the full level descriptors. Objective marks are reliable; essay marks guide
  revision and are not a substitute for a teacher's judgement.
"""
import os
import re
import sys
import math
import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SUBS = os.path.join(ROOT, 'submissions')

OCR_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff', '.heic', '.heif'}
TEXT_EXTS = {'.txt'}

STOPWORDS = set((
    "the a an of to and or in on for with as is are be by that this it its from at into "
    "can may might will would could should not no any two three four five each other more "
    "most than then use used using their they them we you your our his her also such not "
    "over under about which who whom whose what when where why how if but so because due "
    "there here these those one both all some many much very just only per via e.g eg ie "
    "etc between within without across after before during above below out up down off "
    "means meaning give given gives state define explain identify outline distinguish "
    "business businesses firm firms company companies product products customer customers"
).split())


# --------------------------------------------------------------------------
# Load the mark scheme (same ordering the learner sees in the PDFs)
# --------------------------------------------------------------------------
def load_sets():
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    sys.path.insert(0, ROOT)
    set_a, set_b = {}, {}
    try:
        import build  # builds MIXED_PAPERS with the fixed seed
        for p in build.MIXED_PAPERS:
            set_a[str(p['number'])] = p
    except Exception as e:  # pragma: no cover
        print("WARNING: could not load Set A:", e)
    try:
        from setb import PAPERS_B
        for p in PAPERS_B:
            set_b[p['code'].upper()] = p
    except Exception as e:  # pragma: no cover
        print("WARNING: could not load Set B:", e)
    return set_a, set_b


def questions_of(paper):
    if 'questions' in paper:
        return list(paper['questions'])
    return list(paper['sectionA']) + list(paper['sectionB']) + list(paper['case']['questions'])


# --------------------------------------------------------------------------
# OCR / image handling
# --------------------------------------------------------------------------
try:  # optional HEIC support
    import pillow_heif  # type: ignore
    pillow_heif.register_heif_opener()
except Exception:
    pass

_EASY_READER = None
_OCR_STATE = {'engine': None}


def _easy_reader():
    global _EASY_READER
    if _EASY_READER is None:
        import easyocr  # type: ignore
        _EASY_READER = easyocr.Reader(['en'], gpu=False, verbose=False)
    return _EASY_READER


def _preprocess(path):
    from PIL import Image, ImageOps  # type: ignore
    img = Image.open(path)
    try:
        img = ImageOps.exif_transpose(img)
    except Exception:
        pass
    img = img.convert('L')
    img = ImageOps.autocontrast(img)
    w, h = img.size
    if max(w, h) < 1800:
        f = 1800.0 / max(w, h)
        img = img.resize((int(w * f), int(h * f)))
    return img


def ocr_image(path):
    """Return recognised text, '' if nothing readable, or None if no OCR engine
    is available in this environment."""
    # 1) EasyOCR (best for handwriting)
    try:
        reader = _easy_reader()
        lines = reader.readtext(path, detail=0, paragraph=True)
        _OCR_STATE['engine'] = 'EasyOCR'
        return "\n".join(lines).strip()
    except Exception:
        pass
    # 2) Tesseract fallback
    try:
        import pytesseract  # type: ignore
        img = _preprocess(path)
        txt = pytesseract.image_to_string(img, config='--psm 6').strip()
        _OCR_STATE['engine'] = 'Tesseract'
        return txt
    except Exception:
        return None


def _download(url):
    import urllib.request
    import tempfile
    req = urllib.request.Request(url, headers={'User-Agent': 'exam-marker'})
    data = urllib.request.urlopen(req, timeout=30).read()  # nosec - CI only
    ext = os.path.splitext(url.split('?')[0])[1] or '.png'
    tf = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
    tf.write(data)
    tf.close()
    return tf.name


def read_reference(ref):
    """Resolve an image/text reference to text.
    Returns (text_or_None, status) where status is one of
    'text' | 'ocr' | 'empty' | 'ocr-unavailable' | 'not-found' | 'unsupported'."""
    ref = ref.strip().strip('`"\'')
    is_url = ref.lower().startswith(('http://', 'https://'))
    if is_url:
        try:
            path = _download(ref)
        except Exception:
            return None, 'not-found'
    else:
        path = os.path.join(SUBS, os.path.basename(ref))
    ext = os.path.splitext(path)[1].lower()
    if not is_url and not os.path.exists(path):
        return None, 'not-found'
    if ext in TEXT_EXTS:
        try:
            with open(path, encoding='utf-8', errors='replace') as f:
                return f.read().strip(), 'text'
        except Exception:
            return None, 'not-found'
    if ext in OCR_EXTS:
        t = ocr_image(path)
        if t is None:
            return None, 'ocr-unavailable'
        return (t, 'ocr') if t.strip() else ('', 'empty')
    return None, 'unsupported'


DIRECTIVE = re.compile(
    r'!\[[^\]]*\]\(\s*([^)\s]+)[^)]*\)'                                    # ![alt](path)
    r'|\[\[\s*(?:img|image|photo|scan|file)\s*[:=]\s*([^\]]+?)\s*\]\]'      # [[img: path]]
    r'|^[ \t]*(?:img|image|photo|scan|file)[ \t]*[:=][ \t]*(\S.*?)[ \t]*$',  # img: path
    re.I | re.M)


def resolve_media(text, referenced):
    """Replace image/text references in `text` with their (OCR'd) content.
    Records referenced basenames in `referenced`. Returns (new_text, used_ocr)."""
    used = {'ocr': False}

    def repl(m):
        ref = m.group(1) or m.group(2) or m.group(3)
        if not ref:
            return m.group(0)
        base = os.path.basename(ref.strip().strip('`"\''))
        referenced.add(base.lower())
        content, status = read_reference(ref)
        if status == 'text':
            return content
        if status == 'ocr':
            used['ocr'] = True
            return content
        notes = {
            'empty': "[image '%s': no readable text - please write more clearly or type this answer]" % base,
            'ocr-unavailable': "[image '%s' submitted - OCR engine not available in this run]" % base,
            'not-found': "[image '%s' not found in submissions/]" % base,
            'unsupported': "[reference '%s': unsupported file type]" % base,
        }
        return notes.get(status, "[image '%s']" % base)

    return DIRECTIVE.sub(repl, text), used['ocr']


IMG_NAME = re.compile(
    r'^(?:set[-_ ]?)?([abAB]?\d{1,2})[-_ ]*q[-_ ]?(\d{1,2})[-_ ]?([a-hA-H])?', re.I)


def parse_image_name(fname):
    """Parse 'B2-Q1.jpg', 'A3_Q11b.png', '7-Q5.jpg' -> (set, paper, qnum, part)."""
    base = os.path.splitext(os.path.basename(fname))[0]
    m = IMG_NAME.match(base)
    if not m:
        return None
    tok, qn, part = m.group(1), int(m.group(2)), (m.group(3) or '').lower()
    tok = tok.upper()
    if tok.startswith('B'):
        return ('B', tok if tok.startswith('B') else 'B' + tok, qn, part)
    if tok.startswith('A'):
        return ('A', tok[1:], qn, part)
    return ('A', tok, qn, part)


# --------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------
def keywords(text):
    words = re.findall(r"[a-zA-Z][a-zA-Z\-']{2,}", text.lower())
    return [w for w in words if len(w) > 3 and w not in STOPWORDS]


def stem(w):
    return w[:6]


def clean_point(s):
    s = re.sub(r'\([^()]*\)', ' ', s)
    s = re.sub(r'(?i)\bany\s+(?:two|three|four|other)\b\s*:?', ' ', s)
    s = re.sub(r'(?i)\b\d+\s*marks?\b', ' ', s)
    s = re.sub(r'(?i)\bmax\b', ' ', s)
    s = s.replace('e.g.', ' ').replace('i.e.', ' ')
    return s.strip(' .;:')


def num_tokens(seg):
    return re.findall(r"-?\$?\u00a3?\u20ac?\d[\d,]*(?:\.\d+)?%?", seg)


def norm_num(tok):
    return (tok.replace(',', '').replace('$', '').replace('\u00a3', '')
            .replace('\u20ac', '').replace(' ', ''))


# --------------------------------------------------------------------------
# Part-level markers
# --------------------------------------------------------------------------
def mark_knowledge(student, points, maxm):
    if not student.strip():
        return 0, ["No answer given."]
    skw = {stem(w) for w in keywords(student)}
    phrases = []
    for pt in points:
        cleaned = clean_point(pt)
        for frag in re.split(r'[;,/]| or ', cleaned):
            kw = keywords(frag)
            if kw:
                phrases.append((frag.strip(), kw))
    credited, missed, hits, used = [], [], 0, set()
    for frag, kw in phrases:
        need = max(1, math.ceil(len(kw) * 0.5))
        covered = sum(1 for w in kw if stem(w) in skw)
        key = frozenset(stem(w) for w in kw)
        if covered >= need and key not in used:
            hits += 1
            used.add(key)
            credited.append(frag)
        elif covered < need:
            missed.append(frag)
    marks = min(maxm, hits)
    notes = []
    if credited:
        notes.append("Credited points: " + "; ".join(dict.fromkeys(credited))[:400])
    if marks < maxm and missed:
        notes.append("Points not detected: " + "; ".join(dict.fromkeys(missed))[:400])
    return marks, notes


def mark_calc(student, calc_lines, points, maxm):
    expected = []
    for line in calc_lines:
        body = line.lstrip('=').strip()
        for seg in body.split(';'):
            ns = num_tokens(seg)
            if ns:
                expected.append(norm_num(ns[-1]))
    seen = set()
    expected = [e for e in expected if not (e in seen or seen.add(e))]
    if not expected:
        return mark_knowledge(student, points, maxm)
    stud_set = {norm_num(t) for t in num_tokens(student)}
    matched = [e for e in expected if e in stud_set]
    final = expected[-1]
    got_final = final in matched
    if len(expected) <= 2:
        marks = maxm if got_final else (1 if matched and maxm > 1 else 0)
    else:
        marks = min(maxm, round(maxm * len(matched) / len(expected)))
        if got_final:
            marks = max(marks, math.ceil(maxm * 0.6))
    notes = ["Expected value(s): " + ", ".join(expected) +
             ("  |  matched: " + ", ".join(matched) if matched else "  |  none matched")]
    return marks, notes


LEVEL_RE = re.compile(r'Level\s*(\d+)\s*\((\d+)\s*[-\u2013]\s*(\d+)\)')


def parse_levels(levels):
    out = []
    for a in levels:
        m = LEVEL_RE.search(a)
        desc = a.split('|', 2)[2] if a.count('|') >= 2 else ''
        if m:
            out.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), desc.strip()))
    out.sort(key=lambda x: x[1])
    return out


TWO_SIDED = ['however', 'on the other hand', 'whereas', 'although', 'conversely',
             'downside', 'drawback', 'disadvantage', 'argument against', 'but ',
             'in contrast', 'nevertheless', 'yet ']
JUDGE = ['depends', 'overall', 'in conclusion', 'on balance', 'therefore',
         'recommend', 'most important', 'in my view', 'i believe', 'judgement',
         'judgment', 'the best option', 'ultimately', 'to conclude', 'this suggests']
APPLY = ['for example', 'for instance', 'e.g', 'because', 'in this case', 'the case',
         'such as', '$', '%']


def mark_essay(student, part):
    maxm = part['marks']
    levels = parse_levels(part.get('levels') or [a for a in part['ans'] if a.startswith('L|')])
    text = student.lower()
    wc = len(re.findall(r"[a-zA-Z']+", student))
    two = any(k in text for k in TWO_SIDED)
    judge = any(k in text for k in JUDGE)
    apply = any(k in text for k in APPLY)
    top_avail = max([l[0] for l in levels], default=(4 if maxm >= 10 else 3))
    is_evaluate = top_avail >= 4 or maxm >= 10
    if is_evaluate:
        if wc < 20:
            lvl = 1
        elif wc < 60 or not two:
            lvl = 2
        elif two and not judge:
            lvl = 3
        else:
            lvl = 4 if wc >= 90 else 3
    else:
        if wc < 15:
            lvl = 1
        elif wc < 45:
            lvl = 2
        else:
            lvl = 3
    est_mark, chosen_desc, band = 0, '', ''
    if levels:
        top = max(l[0] for l in levels)
        target = min(lvl, top)
        pick = None
        for (ln, lo, hi, desc) in levels:
            if ln == target:
                pick = (ln, lo, hi, desc)
        if pick is None:
            pick = levels[min(len(levels) - 1, target - 1)]
        ln, lo, hi, desc = pick
        est_mark = int(round((lo + hi) / 2))
        if ln == top and est_mark == hi and hi > lo:
            est_mark = hi - 1
        chosen_desc = desc
        band = "Level %d (%d-%d)" % (ln, lo, hi)
    else:
        est_mark = int(round(maxm * (0.3 + 0.15 * lvl)))
    checklist = [
        ("Knowledge / relevant points", wc >= 40),
        ("Two sides of the argument", two),
        ("Application (example/context/figures)", apply),
        ("A justified judgement / conclusion", judge),
        ("Sufficient length/development", wc >= 90),
    ]
    return est_mark, band, chosen_desc, checklist, wc


# --------------------------------------------------------------------------
# Question helpers
# --------------------------------------------------------------------------
def kind_of_part(part):
    ans = part['ans']
    if any(a.startswith('L|') for a in ans) or part.get('levels'):
        return 'essay'
    if any(a.startswith('=') for a in ans):
        return 'calc'
    return 'knowledge'


def points_of(part):
    return [a for a in part['ans'] if not a.startswith(('L|', '#', '=', 'DIAG|'))]


def calc_lines_of(part):
    return [a[1:].strip() for a in part['ans'] if a.startswith('=')]


def model_answer(part):
    lines = []
    for a in part['ans']:
        if a.startswith('L|'):
            _, lv, desc = a.split('|', 2)
            lines.append("- %s: %s" % (lv, desc))
        elif a.startswith('DIAG|'):
            continue
        elif a.startswith('#'):
            lines.append("**%s**" % a[1:].strip())
        elif a.startswith('='):
            lines.append("- `%s`" % a[1:].strip())
        else:
            lines.append("- %s" % a)
    return "\n".join(lines)


def get_part_answer(ans_for_q, part, only_part, whole_text):
    lbl = (part['label'] or '').lower()
    if lbl and lbl in ans_for_q and ans_for_q[lbl].strip():
        return ans_for_q[lbl].strip()
    labelled = any(k in 'abcdefgh' and ans_for_q[k].strip() for k in ans_for_q)
    if only_part or not labelled:
        return whole_text.strip()
    return ''


def mark_question(qnum, question, ans_for_q):
    parts = question['parts']
    only_part = len(parts) == 1
    whole_text = "\n".join(v for v in ans_for_q.values())
    out = {'num': qnum, 'parts': [], 'awarded': 0, 'max': 0,
           'obj_awarded': 0, 'obj_max': 0, 'essay_awarded': 0, 'essay_max': 0}
    for part in parts:
        maxm = part['marks']
        out['max'] += maxm
        student = get_part_answer(ans_for_q, part, only_part, whole_text)
        kind = kind_of_part(part)
        rec = {'label': part['label'], 'text': part['text'], 'max': maxm,
               'kind': kind, 'student': student, 'model': model_answer(part)}
        if kind == 'essay':
            est, band, desc, checklist, wc = mark_essay(student, part)
            if not student.strip():
                est = 0
            rec.update({'awarded': est, 'band': band, 'desc': desc,
                        'checklist': checklist, 'wc': wc, 'indicative': True})
            out['essay_awarded'] += est
            out['essay_max'] += maxm
        else:
            if kind == 'calc':
                marks, notes = mark_calc(student, calc_lines_of(part), points_of(part), maxm)
            else:
                marks, notes = mark_knowledge(student, points_of(part), maxm)
            rec.update({'awarded': marks, 'notes': notes, 'indicative': False})
            out['obj_awarded'] += marks
            out['obj_max'] += maxm
        out['awarded'] += rec['awarded']
        out['parts'].append(rec)
    return out


# --------------------------------------------------------------------------
# Submission parsing (multi-paper aware)
# --------------------------------------------------------------------------
QHEAD = re.compile(r'^\s*#{0,3}\s*Q\s*[.:]?\s*(\d+)\b', re.I)
PART = re.compile(r'^\s*\(?([a-hA-H])\)\s*(.*)$')
KV = re.compile(r'^\s*(set|paper|name)\s*[:=]\s*(.*?)\s*$', re.I)


def parse_submission(text):
    name = ''
    blocks = []
    cur = None
    cur_q = None
    cur_label = None
    cur_set = None

    def new_block(paper):
        nonlocal cur, cur_q, cur_label
        cur = {'set': cur_set, 'paper': paper, 'answers': {}}
        blocks.append(cur)
        cur_q = None
        cur_label = None

    for raw in text.splitlines():
        line = raw.rstrip()
        mk = KV.match(line)
        if mk:
            key, val = mk.group(1).lower(), mk.group(2).strip()
            if key == 'name':
                name = val
            elif key == 'set':
                cur_set = val
                if cur is not None and not cur['answers']:
                    cur['set'] = val
            elif key == 'paper':
                new_block(val)
            continue
        mh = QHEAD.match(line)
        if mh:
            if cur is None:
                new_block(None)
            cur_q = int(mh.group(1))
            cur_label = None
            cur['answers'].setdefault(cur_q, {})
            continue
        if cur is None or cur_q is None:
            continue
        mp = PART.match(line)
        if mp and len(mp.group(1)) == 1:
            cur_label = mp.group(1).lower()
            cur['answers'][cur_q].setdefault(cur_label, '')
            cur['answers'][cur_q][cur_label] += mp.group(2) + '\n'
        else:
            key = cur_label if cur_label else '_'
            cur['answers'][cur_q].setdefault(key, '')
            cur['answers'][cur_q][key] += line + '\n'
    return name, blocks


def resolve_paper(set_hint, paper_ref, set_a, set_b):
    pref = (paper_ref or '').strip().upper()
    s = (set_hint or '').strip().upper()
    if not pref:
        return None, None, "No 'paper:' specified."
    if s == 'B' or pref.startswith('B'):
        code = pref if pref.startswith('B') else ('B' + pref)
        if code in set_b:
            return set_b[code], 'B', None
        return None, 'B', "Set B paper '%s' not found (expected B1-B10)." % code
    num = re.sub(r'\D', '', pref)
    if num in set_a:
        return set_a[num], 'A', None
    return None, 'A', "Set A paper '%s' not found (expected 1-%d)." % (pref, len(set_a))


# --------------------------------------------------------------------------
# Feedback rendering
# --------------------------------------------------------------------------
def paper_title(paper):
    if 'code' in paper:
        return "%s \u2013 %s" % (paper['code'], paper['title'])
    return "Paper %s \u2013 %s" % (paper.get('number', '?'), paper.get('title', ''))


def _render_question(L, r):
    L.append("")
    L.append("### Q%d  \u2014  %d / %d" % (r['num'], r['awarded'], r['max']))
    for p in r['parts']:
        lbl = ("(%s) " % p['label']) if p['label'] else ""
        tag = {'knowledge': 'knowledge', 'calc': 'calculation', 'essay': 'evaluation'}[p['kind']]
        star = "~" if p.get('indicative') else ""
        L.append("")
        L.append("**%s%s**  \u2014  %s%d / %d%s  _(%s)_" %
                 (lbl, p['text'], star, p['awarded'], p['max'], star, tag))
        if p['student']:
            stu = p['student'].strip().replace('\n', ' ')
            if len(stu) > 700:
                stu = stu[:700] + ' ...'
            L.append("")
            L.append("> Your answer: " + stu)
        else:
            L.append("")
            L.append("> _No answer given for this part._")
        if p['kind'] == 'essay':
            if p.get('band'):
                L.append("")
                L.append("Indicative band: **%s**. %s" % (p['band'], p.get('desc', '')))
            L.append("")
            L.append("Checklist:")
            for nm, ok in p['checklist']:
                L.append("- [%s] %s" % ("x" if ok else " ", nm))
        else:
            for n in p.get('notes', []):
                L.append("")
                L.append("_%s_" % n)
        L.append("")
        L.append("<details><summary>Model answer / mark scheme</summary>")
        L.append("")
        L.append(p['model'])
        L.append("")
        L.append("</details>")
    L.append("")
    L.append("---")


def render_feedback(fname, name, sections, used_ocr):
    L = []
    L.append("# Marked feedback")
    L.append("")
    L.append("**Submission:** `%s`%s  " % (os.path.basename(fname),
             ("  \u00b7  **Name:** " + name) if name else ""))
    L.append("**Marked:** %s (UTC)  " % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))
    ok_sections = [s for s in sections if s['kind'] == 'ok']
    g_obj_a = sum(sum(r['obj_awarded'] for r in s['results']) for s in ok_sections)
    g_obj_m = sum(sum(r['obj_max'] for r in s['results']) for s in ok_sections)
    g_ess_a = sum(sum(r['essay_awarded'] for r in s['results']) for s in ok_sections)
    g_ess_m = sum(sum(r['essay_max'] for r in s['results']) for s in ok_sections)
    tot_a, tot_m = g_obj_a + g_ess_a, g_obj_m + g_ess_m
    pct = (100.0 * tot_a / tot_m) if tot_m else 0.0
    L.append("")
    L.append("## Overall")
    L.append("")
    L.append("| Category | Marks |")
    L.append("|---|---|")
    L.append("| Knowledge & calculation (auto-marked) | **%d / %d** |" % (g_obj_a, g_obj_m))
    if g_ess_m:
        L.append("| Essays / evaluation (indicative) | *%d / %d* |" % (g_ess_a, g_ess_m))
    L.append("| **TOTAL across %d paper(s)** | **%d / %d  (%.0f%%)** |" %
             (len(ok_sections), tot_a, tot_m, pct))
    L.append("")
    L.append("> Knowledge and calculation marks are reliable. Essay marks are an "
             "automated estimate to guide revision, not a final grade.")
    if used_ocr:
        L.append("")
        L.append("> Some answers were read from images using OCR. Check the transcription "
                 "shown under \u201cYour answer\u201d is correct - if the handwriting was "
                 "misread you may score lower than you deserve.")
    L.append("")
    for s in sections:
        L.append("")
        if s['kind'] == 'err':
            L.append("## %s" % (s.get('label') or 'Paper'))
            L.append("")
            L.append("> Could not mark this paper: %s" % s['err'])
            L.append("")
            L.append("Set a valid header, e.g. `paper: B1` or `paper: 3`, then re-commit.")
            continue
        sa = sum(r['obj_awarded'] for r in s['results'])
        sm = sum(r['obj_max'] for r in s['results'])
        ea = sum(r['essay_awarded'] for r in s['results'])
        em = sum(r['essay_max'] for r in s['results'])
        L.append("## Set %s \u00b7 %s" % (s['set_label'], s['title']))
        L.append("")
        head = "**Subtotal:** knowledge/calc %d/%d" % (sa, sm)
        if em:
            head += "  \u00b7  essays (indicative) %d/%d" % (ea, em)
        head += "  \u00b7  **%d/%d**" % (sa + ea, sm + em)
        L.append(head)
        if s['missing']:
            L.append("")
            L.append("> Skipped question(s) not in this paper: %s" %
                     ", ".join(str(m) for m in s['missing']))
        for r in s['results']:
            _render_question(L, r)
    L.append("")
    L.append("*Auto-generated by tools/marker.py. Re-commit any time to be re-marked. "
             "Engine: %s.*" % (_OCR_STATE['engine'] or "text only"))
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------
# Marking a whole file / block
# --------------------------------------------------------------------------
def mark_block(block, set_a, set_b, referenced):
    used_ocr = False
    for q, labels in block['answers'].items():
        for lbl in list(labels.keys()):
            new_text, ocr = resolve_media(labels[lbl], referenced)
            labels[lbl] = new_text
            used_ocr = used_ocr or ocr
    paper, set_label, err = resolve_paper(block.get('set'), block.get('paper'), set_a, set_b)
    if err:
        label = "Paper %s" % (block.get('paper') or '?')
        return {'kind': 'err', 'label': label, 'err': err}, used_ocr
    qs = questions_of(paper)
    results, missing = [], []
    for qnum in sorted(block['answers'].keys()):
        if 1 <= qnum <= len(qs):
            results.append(mark_question(qnum, qs[qnum - 1], block['answers'][qnum]))
        else:
            missing.append(qnum)
    return {'kind': 'ok', 'title': paper_title(paper), 'set_label': set_label,
            'results': results, 'missing': missing}, used_ocr


def mark_text(text, set_a, set_b, referenced=None, source_label='submission'):
    """Mark a raw submission string. Returns (feedback_markdown, sections, totals).
    totals is (awarded, max, num_questions). Reused by files and by issue bodies."""
    if referenced is None:
        referenced = set()
    name, blocks = parse_submission(text)
    sections, used_ocr = [], False
    for block in (blocks or []):
        sec, ocr = mark_block(block, set_a, set_b, referenced)
        used_ocr = used_ocr or ocr
        sections.append(sec)
    if not sections:
        md = ("# Marked feedback\n\n> No `paper:` header or questions found in your "
              "submission. Start with a line like `paper: B1` (or `paper: 3`) then "
              "`## Q1`, `## Q2`, ... See the submission guide for the format.\n")
        return md, sections, (0, 0, 0)
    md = render_feedback(source_label, name, sections, used_ocr)
    a = sum(r['awarded'] for s in sections if s['kind'] == 'ok' for r in s['results'])
    m = sum(r['max'] for s in sections if s['kind'] == 'ok' for r in s['results'])
    nq = sum(len(s['results']) for s in sections if s['kind'] == 'ok')
    return md, sections, (a, m, nq)


def mark_file(path, set_a, set_b, referenced):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    md, sections, totals = mark_text(text, set_a, set_b, referenced, source_label=os.path.basename(path))
    fb_path = re.sub(r'\.md$', '', path) + '.feedback.md'
    with open(fb_path, 'w', encoding='utf-8') as f:
        f.write(md)
    return fb_path, totals


def mark_image_groups(referenced, set_a, set_b):
    """Group standalone image files named like B2-Q1.jpg into virtual papers."""
    written = []
    groups = {}
    for name in sorted(os.listdir(SUBS)):
        ext = os.path.splitext(name)[1].lower()
        if ext not in OCR_EXTS:
            continue
        if name.lower() in referenced:
            continue
        parsed = parse_image_name(name)
        if not parsed:
            continue
        set_hint, paper, qn, part = parsed
        key = (set_hint, paper)
        groups.setdefault(key, {'set': set_hint, 'paper': paper, 'answers': {}})
        text = ocr_image(os.path.join(SUBS, name))
        cell = groups[key]['answers'].setdefault(qn, {})
        lbl = part if part else '_'
        piece = text if text else ("[image '%s': no readable text]" % name if text == '' else
                                    "[image '%s': OCR engine not available]" % name)
        cell[lbl] = (cell.get(lbl, '') + '\n' + piece).strip()
    for (set_hint, paper), block in groups.items():
        sec, used_ocr = mark_block(block, set_a, set_b, referenced)
        fb_path = os.path.join(SUBS, "handwritten-%s.feedback.md" % paper)
        fb = render_feedback("handwritten-%s (images)" % paper, '', [sec], used_ocr)
        with open(fb_path, 'w', encoding='utf-8') as f:
            f.write(fb)
        written.append((paper, fb_path, sec))
    return written


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------
def main():
    if not os.path.isdir(SUBS):
        print("No submissions/ folder found - nothing to mark.")
        return 0
    set_a, set_b = load_sets()
    referenced = set()
    summary = []
    md_files = []
    for name in sorted(os.listdir(SUBS)):
        low = name.lower()
        if not low.endswith('.md'):
            continue
        if low.endswith('.feedback.md') or low in ('readme.md', 'template.md'):
            continue
        md_files.append(os.path.join(SUBS, name))
    for path in md_files:
        fb_path, (a, m, nq) = mark_file(path, set_a, set_b, referenced)
        summary.append("Marked %s -> %s  (%d/%d over %d question(s))" %
                       (os.path.basename(path), os.path.basename(fb_path), a, m, nq))
    for paper, fb_path, sec in mark_image_groups(referenced, set_a, set_b):
        if sec['kind'] == 'ok':
            a = sum(r['awarded'] for r in sec['results'])
            m = sum(r['max'] for r in sec['results'])
            summary.append("Marked images for %s -> %s  (%d/%d over %d question(s))" %
                           (paper, os.path.basename(fb_path), a, m, len(sec['results'])))
        else:
            summary.append("Images for %s: %s" % (paper, sec.get('err', 'error')))
    for line in summary:
        print(line)
    step = os.environ.get('GITHUB_STEP_SUMMARY')
    if step:
        with open(step, 'a', encoding='utf-8') as f:
            f.write("## Exam marker\n\n")
            for line in summary or ["No submission files found."]:
                f.write("- " + line + "\n")
            if _OCR_STATE['engine']:
                f.write("\nOCR engine: **%s**\n" % _OCR_STATE['engine'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
