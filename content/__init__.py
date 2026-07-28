"""Aggregates all paper modules into PAPERS (ordered by paper number)."""
import importlib

PAPERS = []
for i in range(1, 17):
    name = f".paper{i:02d}"
    try:
        mod = importlib.import_module(name, __name__)
    except ModuleNotFoundError:
        continue
    if hasattr(mod, 'PAPER'):
        PAPERS.append(mod.PAPER)

PAPERS.sort(key=lambda p: p['number'])
