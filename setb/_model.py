"""Content helpers for Set B (same shape as content/_model.py)."""


def P(label, text, marks, ans=None, levels=None):
    return {'label': label, 'text': text, 'marks': marks,
            'ans': ans or [], 'levels': levels}


def Q(parts, stem=None, diagram=None):
    return {'parts': parts, 'stem': stem, 'diagram': diagram}
