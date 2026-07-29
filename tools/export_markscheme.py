#!/usr/bin/env python3
"""Export the full mark scheme to docs/markscheme.json for the browser marker.

The website marks answers entirely client-side, so it needs the question text,
marks, and answer/indicative data. (The mark scheme is already public in the
repo's PDFs, so nothing new is exposed.)
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
import marker  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'docs', 'markscheme.json')


def part_data(p):
    return {'label': p['label'], 'text': p['text'], 'marks': p['marks'],
            'ans': p['ans']}


def paper_entry(paper):
    return {
        'title': paper['title'],
        'theme': paper.get('theme', ''),
        'questions': [{'num': i + 1, 'stem': q.get('stem') or '',
                       'parts': [part_data(p) for p in q['parts']]}
                      for i, q in enumerate(marker.questions_of(paper))],
    }


def main():
    set_a, set_b = marker.load_sets()
    data = {'A': {}, 'B': {}, 'papersA': [], 'papersB': []}
    for num in sorted(set_a, key=lambda x: int(x)):
        data['A'][num] = paper_entry(set_a[num])
        data['papersA'].append({'id': num, 'title': set_a[num]['title']})
    for code in sorted(set_b, key=lambda x: (len(x), x)):
        data['B'][code] = paper_entry(set_b[code])
        data['papersB'].append({'id': code, 'title': set_b[code]['title']})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    na = sum(len(v['questions']) for v in data['A'].values())
    nb = sum(len(v['questions']) for v in data['B'].values())
    size = os.path.getsize(OUT)
    print("Wrote %s  (%.0f KB)  Set A: %d papers/%d Q  Set B: %d papers/%d Q"
          % (os.path.relpath(OUT, ROOT), size / 1024,
             len(data['A']), na, len(data['B']), nb))


if __name__ == '__main__':
    main()
