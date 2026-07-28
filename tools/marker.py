#!/usr/bin/env python3
"""Auto-marker for the Business 9609 revision papers.

Scans the `submissions/` folder for answer files, marks each one against the
mark scheme that is built into the content modules, and writes a Markdown
feedback report next to it (`<name>.feedback.md`).

Marking approach (transparent and deliberately conservative):
  * Knowledge / short-answer parts  -> keyword matching against the indicative
    content, one mark per distinct point covered (capped at the max marks).
  * Calculation parts               -> checks whether the expected numerical
    answer(s) appear in your response.
  * Essay / "evaluate" parts        -> an INDICATIVE level & mark based on
    whether you show knowledge, two sides of an argument, application and a
    justified judgement, plus the full level descriptors so you can self-check.

Objective (knowledge + calculation) marks are reliable. Essay marks are an
estimate to guide revision, not a substitute for a teacher's judgement.

Submission file format (Markdown-ish, forgiving) -- see submissions/TEMPLATE.md:

    set: A            # A (exam papers) or B (knowledge check)
    paper: 3          # Set A: 1-16   |   Set B: B1-B10

    ## Q1
    (a) your answer to part a ...
    (b) your answer to part b ...

    ## Q2
    your answer (for a single-part question) ...
"""
import os
import re
import sys
import math
import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SUBS = os.path.join(ROOT, 'submissions')

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
        import build  # noqa: builds MIXED_PAPERS with the fixed seed
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
# Text helpers
# --------------------------------------------------------------------------
def keywords(text):
    words = re.findall(r"[a-zA-Z][a-zA-Z\-']{2,}", text.lower())
    return [w for w in words if len(w) > 3 and w not in STOPWORDS]


def stem(w):
    return w[:6]


def clean_point(s):
    s = re.sub(r'\([^()]*\)', ' ', s)                       # (1), (1 each), (2)
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
    """Award ~1 mark per distinct indicative point the answer covers."""
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
    credited, missed = [], []
    hits = 0
    used = set()
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
    # de-duplicate preserving order
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
    # decide target level (1..4)
    if is_evaluate:
        # "Evaluate/discuss": reward two sides + a justified judgement
        if wc < 20:
            lvl = 1
        elif wc < 60 or not two:
            lvl = 2
        elif two and not judge:
            lvl = 3
        else:
            lvl = 4 if wc >= 90 else 3
    else:
        # "Analyse": reward developed, applied points (two sides NOT required)
        if wc < 15:
            lvl = 1
        elif wc < 45:
            lvl = 2
        else:
            lvl = 3
    # map to available levels
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
        # conservative: don't hand out the very top mark automatically
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
# Submission parsing
# --------------------------------------------------------------------------
def parse_submission(text):
    header = {}
    answers = {}
    cur_q = None
    cur_label = None
    body_started = False
    qhead = re.compile(r'^\s*#{0,3}\s*Q\s*[.:]?\s*(\d+)\b', re.I)
    part = re.compile(r'^\s*\(?([a-hA-H])\)\s*(.*)$')
    kv = re.compile(r'^\s*(set|paper|name)\s*[:=]\s*(.+?)\s*$', re.I)
    for raw in text.splitlines():
        line = raw.rstrip()
        mh = qhead.match(line)
        if mh:
            cur_q = int(mh.group(1))
            cur_label = None
            answers.setdefault(cur_q, {})
            body_started = True
            continue
        if not body_started:
            mk = kv.match(line)
            if mk:
                header[mk.group(1).lower()] = mk.group(2).strip()
                continue
        if cur_q is None:
            continue
        mp = part.match(line)
        if mp and len(mp.group(1)) == 1:
            cur_label = mp.group(1).lower()
            answers[cur_q].setdefault(cur_label, '')
            answers[cur_q][cur_label] += mp.group(2) + '\n'
        else:
            key = cur_label if cur_label else '_'
            answers[cur_q].setdefault(key, '')
            answers[cur_q][key] += line + '\n'
    return header, answers


def get_part_answer(ans_for_q, part, only_part, whole_text):
    """Return the student's text for a given part.

    If the student labelled their parts with (a)/(b)/... we use the matching
    label. If they wrote one unlabelled block for a multi-part question (a
    common case), we fall back to the whole block so their points can still be
    credited against each part."""
    lbl = (part['label'] or '').lower()
    if lbl and lbl in ans_for_q and ans_for_q[lbl].strip():
        return ans_for_q[lbl].strip()
    labelled = any(k in 'abcdefgh' and ans_for_q[k].strip() for k in ans_for_q)
    if only_part or not labelled:
        return whole_text.strip()
    return ''


# --------------------------------------------------------------------------
# Mark one question
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
# Render feedback markdown
# --------------------------------------------------------------------------
def render_feedback(fname, header, paper, results, missing):
    L = []
    title = paper_title(paper)
    L.append("# Marked feedback")
    L.append("")
    who = header.get('name', '')
    L.append("**Submission:** `%s`%s  " % (os.path.basename(fname),
             ("  ·  **Name:** " + who) if who else ""))
    L.append("**Paper:** Set %s · %s  " % (header.get('set', '?').upper(), title))
    L.append("**Marked:** %s (UTC)  " % datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M'))
    L.append("")
    obj_a = sum(r['obj_awarded'] for r in results)
    obj_m = sum(r['obj_max'] for r in results)
    ess_a = sum(r['essay_awarded'] for r in results)
    ess_m = sum(r['essay_max'] for r in results)
    tot_a, tot_m = obj_a + ess_a, obj_m + ess_m
    pct = (100.0 * tot_a / tot_m) if tot_m else 0.0
    L.append("## Score summary")
    L.append("")
    L.append("| Category | Marks | Notes |")
    L.append("|---|---|---|")
    L.append("| Knowledge & calculation (auto-marked) | **%d / %d** | keyword & numeric matching |" % (obj_a, obj_m))
    if ess_m:
        L.append("| Essays / evaluation (indicative) | *%d / %d* | estimate only \u2013 check descriptors |" % (ess_a, ess_m))
    L.append("| **TOTAL (answered questions)** | **%d / %d** | **%.0f%%** |" % (tot_a, tot_m, pct))
    L.append("")
    L.append("> Knowledge and calculation marks are reliable. Essay marks are an "
             "automated estimate to guide revision, not a final grade.")
    if missing:
        L.append("")
        L.append("> Note: you referenced question(s) %s which are not in this paper - they were skipped."
                 % ", ".join(str(m) for m in missing))
    L.append("")
    L.append("---")
    for r in results:
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
                if len(stu) > 600:
                    stu = stu[:600] + ' ...'
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
                for name, ok in p['checklist']:
                    L.append("- [%s] %s" % ("x" if ok else " ", name))
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
    L.append("")
    L.append("*Auto-generated by tools/marker.py. Re-commit your submission any time to be re-marked.*")
    return "\n".join(L) + "\n"


def paper_title(paper):
    if 'title' in paper and 'code' in paper:
        return "%s \u2013 %s" % (paper['code'], paper['title'])
    return "Paper %s \u2013 %s" % (paper.get('number', '?'), paper.get('title', ''))


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------
def resolve_paper(header, set_a, set_b):
    s = (header.get('set', '') or '').strip().upper()
    pref = (header.get('paper', '') or '').strip().upper()
    if not pref:
        return None, "No 'paper:' specified in the header."
    if s == 'B' or pref.startswith('B'):
        code = pref if pref.startswith('B') else ('B' + pref)
        if code in set_b:
            return set_b[code], None
        return None, "Set B paper '%s' not found (expected B1-B10)." % code
    # default Set A
    num = re.sub(r'\D', '', pref)
    if num in set_a:
        return set_a[num], None
    return None, "Set A paper '%s' not found (expected 1-%d)." % (pref, len(set_a))


def mark_file(path, set_a, set_b):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    header, answers = parse_submission(text)
    paper, err = resolve_paper(header, set_a, set_b)
    fb_path = re.sub(r'\.md$', '', path) + '.feedback.md'
    if err:
        msg = ("# Marked feedback\n\n**Could not mark this submission.**\n\n> %s\n\n"
               "Please set a valid header, e.g.\n\n```\nset: B\npaper: B1\n```\n"
               "then re-commit. See submissions/README.md.\n" % err)
        with open(fb_path, 'w', encoding='utf-8') as f:
            f.write(msg)
        return fb_path, None
    qs = questions_of(paper)
    results, missing = [], []
    for qnum in sorted(answers.keys()):
        if 1 <= qnum <= len(qs):
            results.append(mark_question(qnum, qs[qnum - 1], answers[qnum]))
        else:
            missing.append(qnum)
    fb = render_feedback(path, header, paper, results, missing)
    with open(fb_path, 'w', encoding='utf-8') as f:
        f.write(fb)
    total_a = sum(r['awarded'] for r in results)
    total_m = sum(r['max'] for r in results)
    return fb_path, (total_a, total_m, len(results))


def main():
    if not os.path.isdir(SUBS):
        print("No submissions/ folder found - nothing to mark.")
        return 0
    set_a, set_b = load_sets()
    targets = []
    for name in sorted(os.listdir(SUBS)):
        if not name.endswith('.md'):
            continue
        low = name.lower()
        if low.endswith('.feedback.md') or low in ('readme.md', 'template.md'):
            continue
        targets.append(os.path.join(SUBS, name))
    summary = []
    for path in targets:
        fb_path, score = mark_file(path, set_a, set_b)
        rel = os.path.relpath(fb_path, ROOT)
        if score:
            a, m, n = score
            line = "Marked %s -> %s  (%d/%d over %d question(s))" % (
                os.path.basename(path), os.path.basename(fb_path), a, m, n)
        else:
            line = "Could not mark %s (see %s)" % (os.path.basename(path), os.path.basename(fb_path))
        print(line)
        summary.append(line)
    step = os.environ.get('GITHUB_STEP_SUMMARY')
    if step:
        with open(step, 'a', encoding='utf-8') as f:
            f.write("## Exam marker\n\n")
            for line in summary or ["No submission files found."]:
                f.write("- " + line + "\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
