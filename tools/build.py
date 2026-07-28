"""Builds the two final PDFs from the content package:
   - Business_9609_AS_Exam_Papers_QUESTIONS.pdf
   - Business_9609_AS_Exam_Papers_MARK_SCHEME.pdf
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdfgen import (PDF, F_REG, F_BOLD, F_OBL, F_BI, BLACK, DARK, GREY, LIGHT,
                    LIGHTER, NAVY, BLUE, RED, GREEN, MAROON, BOXBG, BOXBORDER,
                    Color, text_width, PAGE_W, PAGE_H)
import diagrams as dg

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)
from content import PAPERS  # noqa: E402

WHITE = Color(1, 1, 1)


# ---------------- content-model helpers (used by content modules) ----------
def P(label, text, marks, ans=None, levels=None):
    return {'label': label, 'text': text, 'marks': marks,
            'ans': ans or [], 'levels': levels}


def Q(parts, stem=None, diagram=None):
    return {'parts': parts, 'stem': stem, 'diagram': diagram}


def q_marks(q):
    return sum(p['marks'] for p in q['parts'])


def paper_marks(paper):
    tot = 0
    for q in paper['sectionA'] + paper['sectionB'] + paper['case']['questions']:
        tot += q_marks(q)
    return tot


# ---------------- shared rendering ----------------------------------------
def running_header(pdf, left_txt, right_txt):
    y = PAGE_H - 30
    pdf.raw_text(pdf.ml, y, left_txt, 8, F_REG, GREY)
    pdf.raw_text(PAGE_W - pdf.mr - text_width(right_txt, 8), y, right_txt, 8, F_REG, GREY)
    pdf.line(pdf.ml, y - 4, PAGE_W - pdf.mr, y - 4, 0.5, LIGHT)
    pdf.raw_text(PAGE_W / 2 - 12, 26, str(pdf.page_no), 8.5, F_REG, GREY)


def render_part(pdf, label, text, marks, size=10.5, base_indent=0):
    """Render one sub-part with hanging label and right-aligned [marks]."""
    label_indent = 24 if label else 0
    left = pdf.ml + base_indent + label_indent
    width = pdf.content_w - base_indent - label_indent
    mark_str = f"[{marks}]"
    mark_w = text_width(mark_str, size, True) + 6
    lines = pdf._wrap(text, size, False, width)
    if not lines:
        lines = ['']
    leading = size * 1.36
    for i, ln in enumerate(lines):
        pdf.ensure(leading)
        if i == 0 and label:
            pdf.raw_text(pdf.ml + base_indent, pdf.y - size, f"({label})", size, F_BOLD, DARK)
        is_last = (i == len(lines) - 1)
        # if last line, check room for marks inline
        if is_last:
            if text_width(ln, size, False) + mark_w <= width:
                pdf.raw_text(left, pdf.y - size, ln, size, F_REG, DARK)
                pdf.raw_text(PAGE_W - pdf.mr - text_width(mark_str, size, True),
                             pdf.y - size, mark_str, size, F_BOLD, MAROON)
                pdf.y -= leading
            else:
                pdf.raw_text(left, pdf.y - size, ln, size, F_REG, DARK)
                pdf.y -= leading
                pdf.ensure(leading)
                pdf.raw_text(PAGE_W - pdf.mr - text_width(mark_str, size, True),
                             pdf.y - size, mark_str, size, F_BOLD, MAROON)
                pdf.y -= leading
        else:
            pdf.raw_text(left, pdf.y - size, ln, size, F_REG, DARK)
            pdf.y -= leading


def render_question(pdf, num, q):
    pdf.spacer(4)
    pdf.ensure(40)
    # number gutter
    ny = pdf.y
    pdf.raw_text(pdf.ml - 2, ny - 10.5, f"{num}", 11, F_BOLD, NAVY)
    base = 20
    if q.get('stem'):
        # stem beside number
        lines = pdf._wrap(q['stem'], 10.5, False, pdf.content_w - base)
        leading = 10.5 * 1.36
        for i, ln in enumerate(lines):
            pdf.ensure(leading)
            pdf.raw_text(pdf.ml + base, pdf.y - 10.5, ln, 10.5, F_REG, DARK)
            pdf.y -= leading
        pdf.y -= 3
        for p in q['parts']:
            render_part(pdf, p['label'], p['text'], p['marks'], base_indent=base - 6)
    else:
        # first part shares the number line
        parts = q['parts']
        if len(parts) == 1 and not parts[0]['label']:
            render_part(pdf, '', parts[0]['text'], parts[0]['marks'], base_indent=base - 6)
        else:
            for p in parts:
                render_part(pdf, p['label'], p['text'], p['marks'], base_indent=base - 6)
    if q.get('diagram'):
        d = q['diagram']
        dg.draw(pdf, d['type'], **{k: v for k, v in d.items() if k != 'type'})


def section_banner(pdf, letter, title, instruction, marks):
    pdf.spacer(4)
    pdf.ensure(48)
    y = pdf.y
    pdf.fill_rect(pdf.ml, y - 22, pdf.content_w, 22, NAVY)
    pdf.raw_text(pdf.ml + 8, y - 15.5, f"SECTION {letter}  \u2013  {title}", 11.5, F_BOLD, WHITE)
    mtxt = f"[{marks} marks]"
    pdf.raw_text(PAGE_W - pdf.mr - 8 - text_width(mtxt, 10, True), y - 15.5, mtxt, 10, F_BOLD, WHITE)
    pdf.y = y - 22 - 6
    pdf.paragraph(instruction, size=9.3, font=F_OBL, color=GREY, gap_after=6)


def render_exhibit(pdf, ex):
    if ex['type'] == 'table':
        pdf.spacer(2)
        if ex.get('title'):
            pdf.paragraph(ex['title'], size=9.6, font=F_BOLD, color=NAVY, gap_after=3)
        pdf.table(ex['headers'], ex['rows'], col_w=ex.get('col_w'),
                  align=ex.get('align'), size=ex.get('size', 9.2))
    elif ex['type'] == 'diagram':
        dg.draw(pdf, ex['name'], **{k: v for k, v in ex.items()
                                    if k not in ('type', 'name')})
    elif ex['type'] == 'text':
        pdf.paragraph(ex['text'], size=9.8, font=F_OBL, color=DARK, gap_after=5)


# ---------------- QUESTIONS document --------------------------------------
def cover_questions(pdf):
    pdf.add_page()
    pdf.y = PAGE_H - 120
    pdf.fill_rect(pdf.ml, pdf.y - 4, pdf.content_w, 4, NAVY)
    pdf.y -= 26
    pdf.paragraph("Cambridge International AS Level", size=13, font=F_BOLD,
                  color=GREY, align='center', gap_after=4)
    pdf.paragraph("BUSINESS  9609", size=30, font=F_BOLD, color=NAVY,
                  align='center', gap_after=6)
    pdf.paragraph("Advanced Revision Examination Papers", size=15,
                  font=F_OBL, color=DARK, align='center', gap_after=4)
    pdf.paragraph("QUESTION PAPERS", size=13, font=F_BOLD, color=MAROON,
                  align='center', gap_after=18)
    pdf.fill_rect(pdf.ml + 120, pdf.y, pdf.content_w - 240, 0.9, NAVY)
    pdf.spacer(20)
    pdf.paragraph("For examination in October / November 2026", size=12,
                  font=F_BOLD, color=DARK, align='center', gap_after=2)
    pdf.paragraph("Syllabus content for 2026, 2027 and 2028", size=10,
                  font=F_OBL, color=GREY, align='center', gap_after=18)
    pdf.paragraph("15 papers  \u00b7  20 questions per paper  \u00b7  300 questions",
                  size=11, font=F_BOLD, color=NAVY, align='center', gap_after=2)
    pdf.paragraph("Extension / higher-demand standard  \u00b7  AS Level (Papers 1 & 2 style)",
                  size=10, font=F_OBL, color=GREY, align='center', gap_after=24)

    def note(pdf):
        pdf.paragraph("About these papers", size=11, font=F_BOLD, color=NAVY, gap_after=4)
        pdf.bullet("Each paper contains 20 questions arranged in three sections: "
                   "Section A (short-answer), Section B (essay / extended response) and "
                   "Section C (data response / case study), mirroring the structure and "
                   "command words of Cambridge 9609 Papers 1 and 2.", size=9.6)
        pdf.bullet("A multi-part question, e.g. parts (a) and (b), is counted as ONE "
                   "question. Marks for every part are shown in brackets, e.g. [8].", size=9.6)
        pdf.bullet("Diagrams (break-even charts, product life cycles, the Boston Matrix, "
                   "inventory control charts and others) appear where relevant. Some are "
                   "provided as stimulus; others must be drawn by the candidate.", size=9.6)
        pdf.bullet("Full worked answers and Cambridge-style level-of-response mark schemes "
                   "are in the companion document: 'MARK SCHEME'.", size=9.6)
    pdf.box(note)


def render_paper_questions(pdf, paper):
    pdf.add_page()
    total = paper_marks(paper)
    # paper header banner
    y = pdf.y
    pdf.fill_rect(pdf.ml, y - 46, pdf.content_w, 46, NAVY)
    pdf.raw_text(pdf.ml + 10, y - 19, f"PAPER {paper['number']}", 15, F_BOLD, WHITE)
    pdf.raw_text(pdf.ml + 10, y - 36, paper['title'], 11.5, F_BOLD, Color(0.85, 0.9, 1))
    rt = f"Time: {paper['time']}"
    rm = f"Total: {total} marks"
    pdf.raw_text(PAGE_W - pdf.mr - 10 - text_width(rt, 9.5), y - 19, rt, 9.5, F_REG, WHITE)
    pdf.raw_text(PAGE_W - pdf.mr - 10 - text_width(rm, 10, True), y - 36, rm, 10, F_BOLD, WHITE)
    pdf.y = y - 46 - 6
    pdf.paragraph(paper['theme'], size=9.5, font=F_OBL, color=GREY, gap_after=2)
    pdf.paragraph("Answer ALL questions. Show all workings in calculations. "
                  "The number of marks is given in brackets [ ] at the end of each part.",
                  size=9.2, font=F_OBL, color=GREY, gap_after=4)

    n = 1
    sa = sum(q_marks(q) for q in paper['sectionA'])
    section_banner(pdf, 'A', 'Short-answer questions', 'Answer all questions in this section.', sa)
    for q in paper['sectionA']:
        render_question(pdf, n, q); n += 1

    sb = sum(q_marks(q) for q in paper['sectionB'])
    section_banner(pdf, 'B', 'Essay questions', 'Answer all questions. Marks are awarded for analysis and evaluation.', sb)
    for q in paper['sectionB']:
        render_question(pdf, n, q); n += 1

    case = paper['case']
    sc = sum(q_marks(q) for q in case['questions'])
    section_banner(pdf, 'C', 'Data response  \u2013  ' + case['title'], 'Read the case study and use it in your answers.', sc)
    for para in case['context']:
        pdf.paragraph(para, size=9.8, font=F_REG, color=DARK, gap_after=5)
    for ex in case.get('exhibits', []):
        render_exhibit(pdf, ex)
    pdf.spacer(2)
    pdf.line(pdf.ml, pdf.y, PAGE_W - pdf.mr, pdf.y, 0.6, LIGHT)
    pdf.spacer(2)
    for q in case['questions']:
        render_question(pdf, n, q); n += 1


# ---------------- MARK SCHEME document ------------------------------------
def cover_ms(pdf):
    pdf.add_page()
    pdf.y = PAGE_H - 120
    pdf.fill_rect(pdf.ml, pdf.y - 4, pdf.content_w, 4, MAROON)
    pdf.y -= 26
    pdf.paragraph("Cambridge International AS Level", size=13, font=F_BOLD, color=GREY, align='center', gap_after=4)
    pdf.paragraph("BUSINESS  9609", size=30, font=F_BOLD, color=MAROON, align='center', gap_after=6)
    pdf.paragraph("Advanced Revision Examination Papers", size=15, font=F_OBL, color=DARK, align='center', gap_after=4)
    pdf.paragraph("MARK SCHEME  &  MODEL ANSWERS", size=13, font=F_BOLD, color=NAVY, align='center', gap_after=18)
    pdf.fill_rect(pdf.ml + 120, pdf.y, pdf.content_w - 240, 0.9, MAROON)
    pdf.spacer(20)
    pdf.paragraph("For examination in October / November 2026", size=12, font=F_BOLD, color=DARK, align='center', gap_after=2)
    pdf.paragraph("Detailed indicative content, worked calculations and level descriptors", size=10, font=F_OBL, color=GREY, align='center', gap_after=22)

    def note(pdf):
        pdf.paragraph("How to use this mark scheme", size=11, font=F_BOLD, color=NAVY, gap_after=4)
        pdf.bullet("Short-answer parts show the knowledge and application points expected, "
                   "with the marks attached to each point.", size=9.6)
        pdf.bullet("Essay and higher-tariff data-response parts use Cambridge-style "
                   "Levels of Response (AO1 Knowledge, AO2 Application, AO3 Analysis, "
                   "AO4 Evaluation). Award the level that best fits the response.", size=9.6)
        pdf.bullet("Indicative content is not exhaustive; accept any valid, well-argued "
                   "alternative supported by the context.", size=9.6)
        pdf.bullet("All numerical answers are worked in full so method marks can be awarded "
                   "even where a final figure is incorrect (own-figure rule).", size=9.6)
    pdf.box(note)


def render_ans_part(pdf, label, text, marks, ans, levels):
    head = f"({label}) " if label else ""
    pdf.spacer(3)
    pdf.ensure(22)
    # marks tag, top-right, on the restated-question line
    top_y = pdf.y
    mk = f"[{marks}]"
    pdf.raw_text(PAGE_W - pdf.mr - text_width(mk, 9.5, True), top_y - 9, mk, 9.5, F_BOLD, MAROON)
    # question restated (italic, short), leaving room for the marks tag
    qline = head + text
    pdf.paragraph(qline, size=9.4, font=F_OBL, color=NAVY, gap_after=2,
                  max_w=pdf.content_w - 42)
    for a in ans:
        if a.startswith('DIAG|'):  # embed a worked diagram: DIAG|name|caption
            parts = a.split('|', 2)
            name = parts[1]
            cap = parts[2] if len(parts) > 2 else ''
            dg.draw(pdf, name, caption=cap)
        elif a.startswith('#'):  # sub-heading inside answer
            pdf.spacer(1)
            pdf.paragraph(a[1:].strip(), size=9.6, font=F_BOLD, color=MAROON, gap_after=2)
        elif a.startswith('L|'):  # level descriptor "L|Level 3 (5-6)|text"
            _, lv, desc = a.split('|', 2)
            pdf.ensure(16)
            pdf.raw_text(pdf.ml + 6, pdf.y - 9, lv, 9.2, F_BOLD, NAVY)
            pdf.y -= 12
            pdf.paragraph(desc, size=9.2, font=F_REG, color=DARK, indent=14, gap_after=3)
        elif a.startswith('='):  # calculation line (highlighted)
            pdf.paragraph(a[1:].strip(), size=9.4, font=F_BOLD, color=GREEN, indent=8, gap_after=2)
        else:
            pdf.bullet(a, size=9.4, color=DARK)
    pdf.spacer(3)


def render_question_ms(pdf, num, q):
    pdf.spacer(3)
    pdf.ensure(30)
    pdf.raw_text(pdf.ml - 2, pdf.y - 11, f"Q{num}", 11, F_BOLD, MAROON)
    pdf.y -= 16
    if q.get('stem'):
        pdf.paragraph(q['stem'], size=9, font=F_OBL, color=GREY, indent=6, gap_after=3)
    for p in q['parts']:
        render_ans_part(pdf, p['label'], p['text'], p['marks'], p['ans'], p.get('levels'))
    pdf.line(pdf.ml, pdf.y, PAGE_W - pdf.mr, pdf.y, 0.4, LIGHT)


def render_paper_ms(pdf, paper):
    pdf.add_page()
    y = pdf.y
    pdf.fill_rect(pdf.ml, y - 40, pdf.content_w, 40, MAROON)
    pdf.raw_text(pdf.ml + 10, y - 17, f"PAPER {paper['number']}  \u2013  MARK SCHEME", 13.5, F_BOLD, WHITE)
    pdf.raw_text(pdf.ml + 10, y - 32, paper['title'], 10.5, F_BOLD, Color(1, 0.9, 0.9))
    pdf.y = y - 40 - 8
    n = 1
    pdf.heading("Section A  \u2013  Short-answer questions", size=12, color=NAVY, gap_after=3)
    for q in paper['sectionA']:
        render_question_ms(pdf, n, q); n += 1
    pdf.heading("Section B  \u2013  Essay questions", size=12, color=NAVY, gap_after=3)
    for q in paper['sectionB']:
        render_question_ms(pdf, n, q); n += 1
    pdf.heading("Section C  \u2013  Data response: " + paper['case']['title'], size=12, color=NAVY, gap_after=3)
    for q in paper['case']['questions']:
        render_question_ms(pdf, n, q); n += 1


# ---------------- drivers --------------------------------------------------
def build_questions(path):
    pdf = PDF()
    pdf.on_new_page = lambda p: running_header(
        p, "Cambridge AS Level Business 9609", "Question Papers \u00b7 Oct/Nov 2026") if p.page_no > 1 else None
    cover_questions(pdf)
    for paper in PAPERS:
        render_paper_questions(pdf, paper)
    pages = pdf.save(path)
    return pages


def build_markscheme(path):
    pdf = PDF()
    pdf.on_new_page = lambda p: running_header(
        p, "Cambridge AS Level Business 9609", "Mark Scheme \u00b7 Oct/Nov 2026") if p.page_no > 1 else None
    cover_ms(pdf)
    for paper in PAPERS:
        render_paper_ms(pdf, paper)
    pages = pdf.save(path)
    return pages


if __name__ == '__main__':
    qn = build_questions(os.path.join(ROOT, 'Business_9609_AS_Exam_Papers_QUESTIONS.pdf'))
    mn = build_markscheme(os.path.join(ROOT, 'Business_9609_AS_Exam_Papers_MARK_SCHEME.pdf'))
    nq = sum(len(p['sectionA']) + len(p['sectionB']) + len(p['case']['questions']) for p in PAPERS)
    tm = sum(paper_marks(p) for p in PAPERS)
    print(f"Papers: {len(PAPERS)}  Questions: {nq}  Total marks: {tm}")
    print(f"Questions PDF pages: {qn}")
    print(f"Mark scheme PDF pages: {mn}")
