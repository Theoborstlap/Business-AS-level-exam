import sys, os
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from content import PAPERS
from build import paper_marks

print("No.  A  B  C  Tot  Marks  Title")
tot_q = 0
tot_m = 0
diag = set()
for p in PAPERS:
    a = len(p['sectionA']); b = len(p['sectionB']); c = len(p['case']['questions'])
    n = a + b + c; m = paper_marks(p)
    tot_q += n; tot_m += m
    assert n == 20, (p['number'], n)
    for q in p['sectionA'] + p['sectionB'] + p['case']['questions']:
        if q.get('diagram'):
            diag.add(q['diagram']['type'])
    for ex in p['case'].get('exhibits', []):
        if ex['type'] == 'diagram':
            diag.add(ex['name'])
    print("%3d %2d %2d %2d %4d %6d  %s" % (p['number'], a, b, c, n, m, p['title'][:52]))
print("-" * 72)
print("TOTAL papers: %d   questions: %d   marks: %d" % (len(PAPERS), tot_q, tot_m))
print("Diagram types used:", sorted(diag))
