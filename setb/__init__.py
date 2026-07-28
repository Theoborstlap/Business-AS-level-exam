"""Set B knowledge-recall papers, aggregated into PAPERS_B (ordered)."""
import importlib

PAPERS_B = []
_order = []
for i in range(1, 13):
    name = ".b%02d" % i
    try:
        mod = importlib.import_module(name, __name__)
    except ModuleNotFoundError:
        continue
    if hasattr(mod, 'PAPER'):
        PAPERS_B.append(mod.PAPER)
        _order.append(i)
