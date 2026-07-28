"""Builds Set B (knowledge-recall short questions) into two PDFs:
   - Business_9609_AS_KnowledgeCheck_SetB_QUESTIONS.pdf
   - Business_9609_AS_KnowledgeCheck_SetB_MARK_SCHEME.pdf

Reuses the PDF engine and the question/answer renderers from build.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pdfgen import (PDF, F_REG, F_BOLD, F_OBL, DARK, GREY, LIGHT, NAVY, MAROON,
                    Color, text_width, PAGE_W, PAGE_H)
from build import (running_header, render_question, render_question_ms,
                   section_banner, q_marks)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)
from setb import PAPERS_B  # noqa: E402

WHITE = Color(1, 1, 1)
TEAL = Color(0.06, 0.42, 0.45)
TEAL_L = Color(0.80, 0.92, 0.93)


def paper_b_marks(paper):
    return sum(q_marks(q) for q in paper['questions'])


def cover(pdf, subtitle, colour):
    pdf.add_page()
    pdf.y = PAGE_H - 120
    pdf.fill_rect(pdf.ml, pdf.y - 4, pdf.content_w, 4, colour)
    pdf.y -= 26
    pdf.paragraph("Cambridge International AS Level", size=13, font=F_BOLD, color=GREY, align='center', gap_after=4)
    pdf.paragraph("BUSINESS  9609", size=30, font=F_BOLD, color=colour, align='center', gap_after=6)
    pdf.paragraph("Knowledge Check  \u2013  SET B", size=16, font=F_BOLD, color=DARK, align='center', gap_after=4)
    pdf.paragraph("Short recall questions for knowledge (AO1) marks", size=12, font=F_OBL, color=DARK, align='center', gap_after=4)
    pdf.paragraph(subtitle, size=13, font=F_BOLD, color=MAROON, align='center', gap_after=18)
    pdf.fill_rect(pdf.ml + 120, pdf.y, pdf.content_w - 240, 0.9, colour)
    pdf.spacer(20)
    pdf.paragraph("For examination in October / November 2026", size=12, font=F_BOLD, color=DARK, align='center', gap_after=2)
    pdf.paragraph("10 knowledge papers  \u00b7  20 questions per paper  \u00b7  200 questions", size=11, font=F_BOLD, color=colour, align='center', gap_after=20)

    def note(pdf):
        pdf.paragraph("How to use Set B", size=11, font=F_BOLD, color=colour, gap_after=4)
        pdf.bullet("Set B is a pure knowledge-recall companion to the Set A exam papers. "
                   "Every question uses knowledge command words \u2013 Define, State, Identify, "
                   "Outline and Distinguish \u2013 so you can check you know the key terms, facts "
                   "and definitions for the whole AS syllabus.", size=9.6)
        pdf.bullet("The 10 papers cover the syllabus section by section (1.1 through 5.5). "
                   "A multi-part question, e.g. (a), (b), (c), counts as ONE question. Marks "
                   "for each part are shown in brackets, e.g. [2].", size=9.6)
        pdf.bullet("Answer every question quickly from memory, then check the companion "
                   "MARK SCHEME. Anything you cannot answer instantly is a topic to revise.", size=9.6)
        pdf.bullet("Target: aim to score at least 90%. Re-test any paper where you drop "
                   "knowledge marks until recall is automatic.", size=9.6)
    pdf.box(note)


def render_paper(pdf, paper):
    pdf.add_page()
    total = paper_b_marks(paper)
    y = pdf.y
    pdf.fill_rect(pdf.ml, y - 46, pdf.content_w, 46, TEAL)
    pdf.raw_text(pdf.ml + 10, y - 19, "KNOWLEDGE PAPER " + paper['code'], 15, F_BOLD, WHITE)
    pdf.raw_text(pdf.ml + 10, y - 36, paper['title'], 11.0, F_BOLD, TEAL_L)
    rt = "Suggested time: " + paper['time']
    rm = "Total: " + str(total) + " marks"
    pdf.raw_text(PAGE_W - pdf.mr - 10 - text_width(rt, 9.5), y - 19, rt, 9.5, F_REG, WHITE)
    pdf.raw_text(PAGE_W - pdf.mr - 10 - text_width(rm, 10, True), y - 36, rm, 10, F_BOLD, WHITE)
    pdf.y = y - 46 - 6
    pdf.paragraph(paper['theme'], size=9.5, font=F_OBL, color=GREY, gap_after=2)
    pdf.paragraph("Answer ALL questions from memory. These questions test knowledge and "
                  "understanding (AO1). The number of marks is given in brackets [ ].",
                  size=9.2, font=F_OBL, color=GREY, gap_after=4)
    section_banner(pdf, 'K', 'Knowledge-recall questions', 'Answer all questions in this section.', total)
    n = 1
    for q in paper['questions']:
        render_question(pdf, n, q)
        n += 1


def render_paper_ms(pdf, paper):
    pdf.add_page()
    y = pdf.y
    pdf.fill_rect(pdf.ml, y - 40, pdf.content_w, 40, MAROON)
    pdf.raw_text(pdf.ml + 10, y - 17, "KNOWLEDGE PAPER " + paper['code'] + "  \u2013  MARK SCHEME", 13.5, F_BOLD, WHITE)
    pdf.raw_text(pdf.ml + 10, y - 32, paper['title'], 10.5, F_BOLD, Color(1, 0.9, 0.9))
    pdf.y = y - 40 - 8
    pdf.heading("Knowledge-recall answers", size=12, color=NAVY, gap_after=3)
    n = 1
    for q in paper['questions']:
        render_question_ms(pdf, n, q)
        n += 1


def build_questions(path):
    pdf = PDF()
    pdf.on_new_page = lambda p: running_header(
        p, "Cambridge AS Level Business 9609", "Knowledge Check Set B \u00b7 Questions") if p.page_no > 1 else None
    cover(pdf, "QUESTION PAPERS", TEAL)
    for paper in PAPERS_B:
        render_paper(pdf, paper)
    return pdf.save(path)


def build_markscheme(path):
    pdf = PDF()
    pdf.on_new_page = lambda p: running_header(
        p, "Cambridge AS Level Business 9609", "Knowledge Check Set B \u00b7 Mark Scheme") if p.page_no > 1 else None
    cover(pdf, "MARK SCHEME & ANSWERS", MAROON)
    for paper in PAPERS_B:
        render_paper_ms(pdf, paper)
    return pdf.save(path)


if __name__ == '__main__':
    qn = build_questions(os.path.join(ROOT, 'Business_9609_AS_KnowledgeCheck_SetB_QUESTIONS.pdf'))
    mn = build_markscheme(os.path.join(ROOT, 'Business_9609_AS_KnowledgeCheck_SetB_MARK_SCHEME.pdf'))
    nq = sum(len(p['questions']) for p in PAPERS_B)
    tm = sum(paper_b_marks(p) for p in PAPERS_B)
    print("Set B papers: %d  questions: %d  marks: %d" % (len(PAPERS_B), nq, tm))
    print("Questions PDF pages: %d" % qn)
    print("Mark scheme PDF pages: %d" % mn)
