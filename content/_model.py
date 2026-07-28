"""Content helpers shared by all paper modules.

P(label, text, marks, ans, levels)  -> a sub-part of a question
Q(parts, stem, diagram)             -> one question (may have several parts)

Answer ('ans') list conventions (interpreted by tools/build.py):
  "plain text"          -> a bullet point of indicative content
  "#Heading"            -> a bold sub-heading inside the answer
  "=calc"               -> a highlighted worked-calculation line
  "L|Level 3 (5-6)|..." -> a Cambridge level-of-response descriptor
"""


def P(label, text, marks, ans=None, levels=None):
    return {'label': label, 'text': text, 'marks': marks,
            'ans': ans or [], 'levels': levels}


def Q(parts, stem=None, diagram=None):
    return {'parts': parts, 'stem': stem, 'diagram': diagram}
