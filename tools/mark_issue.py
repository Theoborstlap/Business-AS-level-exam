#!/usr/bin/env python3
"""Mark a GitHub issue body and write a comment-ready feedback file.

Reads the issue body from the ISSUE_BODY environment variable (passed by the
workflow, never interpolated into a shell command), marks it with the shared
marker engine, and writes `issue-feedback.md` for the workflow to post as a
comment. Images dragged into the issue appear as `![](https://...)` links and
are downloaded + OCR'd by the marker.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import marker  # noqa: E402


def main():
    body = os.environ.get('ISSUE_BODY', '') or ''
    number = os.environ.get('ISSUE_NUMBER', '').strip()
    label = ("GitHub issue #%s" % number) if number else "your issue submission"
    set_a, set_b = marker.load_sets()
    md, sections, totals = marker.mark_text(body, set_a, set_b, source_label=label)
    a, m, nq = totals
    ok = [s for s in sections if s.get('kind') == 'ok']
    if not ok:
        md += ("\n\n---\n*Tip: put each answer under a `## Q1`, `## Q2` heading, and start "
               "the submission with `paper: B1` (or `paper: 3`). You can drag photos of "
               "handwriting straight into the issue box.*\n")
    with open('issue-feedback.md', 'w', encoding='utf-8') as f:
        f.write(md)
    print("Wrote issue-feedback.md  (%d/%d over %d question(s), %d paper section(s))"
          % (a, m, nq, len(ok)))


if __name__ == '__main__':
    main()
