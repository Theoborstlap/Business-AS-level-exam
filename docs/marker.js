/* Browser/Node marking engine for the Business 9609 auto-marker website.
 * Mirrors tools/marker.py: knowledge = keyword matching, calculations =
 * numeric check, essays = indicative level + checklist. Objective marks are
 * reliable; essay marks are an estimate. Works client-side (no server). */
(function (root) {
  'use strict';

  var STOP = new Set((
    "the a an of to and or in on for with as is are be by that this it its from at into " +
    "can may might will would could should not no any two three four five each other more " +
    "most than then use used using their they them we you your our his her also such not " +
    "over under about which who whom whose what when where why how if but so because due " +
    "there here these those one both all some many much very just only per via e.g eg ie " +
    "etc between within without across after before during above below out up down off " +
    "means meaning give given gives state define explain identify outline distinguish " +
    "business businesses firm firms company companies product products customer customers"
  ).split(/\s+/));

  var TWO_SIDED = ['however', 'on the other hand', 'whereas', 'although', 'conversely',
    'downside', 'drawback', 'disadvantage', 'argument against', 'but ',
    'in contrast', 'nevertheless', 'yet '];
  var JUDGE = ['depends', 'overall', 'in conclusion', 'on balance', 'therefore',
    'recommend', 'most important', 'in my view', 'i believe', 'judgement',
    'judgment', 'the best option', 'ultimately', 'to conclude', 'this suggests'];
  var APPLY = ['for example', 'for instance', 'e.g', 'because', 'in this case',
    'the case', 'such as', '$', '%'];

  function keywords(text) {
    var m = (text || '').toLowerCase().match(/[a-z][a-z\-']{2,}/g) || [];
    return m.filter(function (w) { return w.length > 3 && !STOP.has(w); });
  }
  function stem(w) { return w.slice(0, 6); }

  function cleanPoint(s) {
    s = s.replace(/\([^()]*\)/g, ' ');
    s = s.replace(/\bany\s+(two|three|four|other)\b\s*:?/ig, ' ');
    s = s.replace(/\b\d+\s*marks?\b/ig, ' ');
    s = s.replace(/\bmax\b/ig, ' ');
    s = s.split('e.g.').join(' ').split('i.e.').join(' ');
    return s.replace(/^[\s.;:]+|[\s.;:]+$/g, '');
  }

  function numTokens(seg) {
    return (seg || '').match(/-?\$?\u00a3?\u20ac?\d[\d,]*(?:\.\d+)?%?/g) || [];
  }
  function normNum(t) {
    return t.replace(/,/g, '').replace(/\$/g, '').replace(/\u00a3/g, '')
      .replace(/\u20ac/g, '').replace(/\s/g, '');
  }

  function uniq(arr) {
    var seen = {}, out = [];
    arr.forEach(function (x) { if (!seen[x]) { seen[x] = 1; out.push(x); } });
    return out;
  }

  function kindOfPart(part) {
    var ans = part.ans || [];
    if (ans.some(function (a) { return a.indexOf('L|') === 0; })) return 'essay';
    if (ans.some(function (a) { return a.indexOf('=') === 0; })) return 'calc';
    return 'knowledge';
  }
  function pointsOf(part) {
    return (part.ans || []).filter(function (a) {
      return !(a.indexOf('L|') === 0 || a.indexOf('#') === 0 ||
               a.indexOf('=') === 0 || a.indexOf('DIAG|') === 0);
    });
  }
  function calcLinesOf(part) {
    return (part.ans || []).filter(function (a) { return a.indexOf('=') === 0; })
      .map(function (a) { return a.slice(1).trim(); });
  }

  function markKnowledge(student, points, maxm) {
    if (!student || !student.trim()) return { marks: 0, credited: [], missed: [] };
    var skw = {};
    keywords(student).forEach(function (w) { skw[stem(w)] = 1; });
    var phrases = [];
    points.forEach(function (pt) {
      cleanPoint(pt).split(/[;,/]| or /).forEach(function (frag) {
        var kw = keywords(frag);
        if (kw.length) phrases.push([frag.trim(), kw]);
      });
    });
    var credited = [], missed = [], hits = 0, used = {};
    phrases.forEach(function (pr) {
      var frag = pr[0], kw = pr[1];
      var need = Math.max(1, Math.ceil(kw.length * 0.5));
      var covered = 0;
      kw.forEach(function (w) { if (skw[stem(w)]) covered++; });
      var key = kw.map(stem).sort().join('|');
      if (covered >= need && !used[key]) { hits++; used[key] = 1; credited.push(frag); }
      else if (covered < need) { missed.push(frag); }
    });
    return { marks: Math.min(maxm, hits), credited: uniq(credited), missed: uniq(missed) };
  }

  function markCalc(student, calcLines, points, maxm) {
    var expected = [];
    calcLines.forEach(function (line) {
      var body = line.replace(/^=+/, '').trim();
      body.split(';').forEach(function (seg) {
        var ns = numTokens(seg);
        if (ns.length) expected.push(normNum(ns[ns.length - 1]));
      });
    });
    expected = uniq(expected);
    if (!expected.length) return markKnowledge(student, points, maxm);
    var studSet = {};
    numTokens(student).forEach(function (t) { studSet[normNum(t)] = 1; });
    var matched = expected.filter(function (e) { return studSet[e]; });
    var final = expected[expected.length - 1];
    var gotFinal = matched.indexOf(final) !== -1;
    var marks;
    if (expected.length <= 2) {
      marks = gotFinal ? maxm : (matched.length && maxm > 1 ? 1 : 0);
    } else {
      marks = Math.min(maxm, Math.round(maxm * matched.length / expected.length));
      if (gotFinal) marks = Math.max(marks, Math.ceil(maxm * 0.6));
    }
    return { marks: marks, expected: expected, matched: matched, isCalc: true };
  }

  function parseLevels(levels) {
    var out = [];
    levels.forEach(function (a) {
      var m = a.match(/Level\s*(\d+)\s*\((\d+)\s*[-\u2013]\s*(\d+)\)/);
      var parts = a.split('|');
      var desc = parts.length >= 3 ? parts.slice(2).join('|').trim() : '';
      if (m) out.push({ ln: +m[1], lo: +m[2], hi: +m[3], desc: desc });
    });
    out.sort(function (a, b) { return a.lo - b.lo; });
    return out;
  }

  function markEssay(student, part) {
    var maxm = part.marks;
    var levels = parseLevels((part.ans || []).filter(function (a) { return a.indexOf('L|') === 0; }));
    var text = (student || '').toLowerCase();
    var wc = ((student || '').match(/[a-zA-Z']+/g) || []).length;
    var two = TWO_SIDED.some(function (k) { return text.indexOf(k) !== -1; });
    var judge = JUDGE.some(function (k) { return text.indexOf(k) !== -1; });
    var apply = APPLY.some(function (k) { return text.indexOf(k) !== -1; });
    var topAvail = levels.length ? Math.max.apply(null, levels.map(function (l) { return l.ln; })) : (maxm >= 10 ? 4 : 3);
    var isEval = topAvail >= 4 || maxm >= 10;
    var lvl;
    if (isEval) {
      if (wc < 20) lvl = 1;
      else if (wc < 60 || !two) lvl = 2;
      else if (two && !judge) lvl = 3;
      else lvl = wc >= 90 ? 4 : 3;
    } else {
      if (wc < 15) lvl = 1; else if (wc < 45) lvl = 2; else lvl = 3;
    }
    var est = 0, band = '', desc = '';
    if (levels.length) {
      var top = Math.max.apply(null, levels.map(function (l) { return l.ln; }));
      var target = Math.min(lvl, top);
      var pick = null;
      levels.forEach(function (l) { if (l.ln === target) pick = l; });
      if (!pick) pick = levels[Math.min(levels.length - 1, target - 1)];
      est = Math.round((pick.lo + pick.hi) / 2);
      if (pick.ln === top && est === pick.hi && pick.hi > pick.lo) est = pick.hi - 1;
      band = 'Level ' + pick.ln + ' (' + pick.lo + '-' + pick.hi + ')';
      desc = pick.desc;
    } else {
      est = Math.round(maxm * (0.3 + 0.15 * lvl));
    }
    if (!student || !student.trim()) est = 0;
    var checklist = [
      ['Knowledge / relevant points', wc >= 40],
      ['Two sides of the argument', two],
      ['Application (example/context/figures)', apply],
      ['A justified judgement / conclusion', judge],
      ['Sufficient length/development', wc >= 90]
    ];
    return { marks: est, band: band, desc: desc, checklist: checklist, wc: wc, indicative: true };
  }

  function modelAnswer(part) {
    var out = [];
    (part.ans || []).forEach(function (a) {
      if (a.indexOf('L|') === 0) {
        var p = a.split('|'); out.push({ t: 'level', s: p[1] + ': ' + p.slice(2).join('|') });
      } else if (a.indexOf('DIAG|') === 0) { /* skip diagrams on the web */ }
      else if (a.indexOf('#') === 0) out.push({ t: 'head', s: a.slice(1).trim() });
      else if (a.indexOf('=') === 0) out.push({ t: 'calc', s: a.slice(1).trim() });
      else out.push({ t: 'point', s: a });
    });
    return out;
  }

  function markPart(part, student) {
    var kind = kindOfPart(part);
    var res = { kind: kind, max: part.marks, label: part.label, text: part.text,
                student: student || '', model: modelAnswer(part) };
    if (kind === 'essay') {
      var e = markEssay(student, part);
      res.awarded = e.marks; res.band = e.band; res.desc = e.desc;
      res.checklist = e.checklist; res.wc = e.wc; res.indicative = true;
    } else if (kind === 'calc') {
      var c = markCalc(student, calcLinesOf(part), pointsOf(part), part.marks);
      res.awarded = c.marks; res.expected = c.expected || []; res.matched = c.matched || [];
      res.credited = c.credited || []; res.missed = c.missed || [];
    } else {
      var k = markKnowledge(student, pointsOf(part), part.marks);
      res.awarded = k.marks; res.credited = k.credited; res.missed = k.missed;
    }
    return res;
  }

  var Marker = {
    keywords: keywords, kindOfPart: kindOfPart, pointsOf: pointsOf,
    calcLinesOf: calcLinesOf, markKnowledge: markKnowledge, markCalc: markCalc,
    markEssay: markEssay, modelAnswer: modelAnswer, markPart: markPart
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = Marker;
  else root.Marker = Marker;

  // ---- Node self-test ----
  if (typeof require !== 'undefined' && require.main === module) {
    var assert = require('assert');
    var k = markPart({ label: 'a', text: 'Define business activity', marks: 2,
      ans: ["Using resources/factors of production (1) to produce goods and services to satisfy customers' needs and wants (1)."] },
      'A business uses resources such as land and labour to produce goods and services that satisfy customers needs and wants');
    console.log('knowledge:', k.awarded + '/' + k.max, 'credited', k.credited.length);
    assert(k.awarded === 2, 'knowledge should be 2');

    var c = markPart({ label: '', text: 'Break-even', marks: 4,
      ans: ["=Contribution = 25 - 10 = 15", "=Break-even = 60,000 / 15 = 4,000 units", "2 + 2."] },
      'Contribution is 15, so break-even = 60,000/15 = 4,000 units');
    console.log('calc:', c.awarded + '/' + c.max, 'matched', JSON.stringify(c.matched));
    assert(c.awarded === 4, 'calc should be full');

    var wrong = markPart({ label: '', text: 'Break-even', marks: 3,
      ans: ["=Break-even = 60,000 / 15 = 4,000 units", "answer 4,000."] }, 'about 5000 units');
    console.log('calc wrong:', wrong.awarded + '/' + wrong.max);
    assert(wrong.awarded === 0, 'wrong calc should be 0');

    var e = markPart({ label: 'b', text: 'Evaluate', marks: 12,
      ans: ["L|Level 4 (10-12)|Balanced, supported judgement.", "L|Level 3 (7-9)|Balanced.",
             "L|Level 2 (4-6)|Limited.", "L|Level 1 (1-3)|One-sided."] },
      'On one hand, the decision lowers costs and raises profit, which benefits shareholders and ' +
      'improves competitiveness because unit costs fall. However, it can harm employee morale and ' +
      'product quality, and it may damage the firm reputation with customers in the long run. ' +
      'On the other hand, the savings could be reinvested to protect jobs elsewhere. It depends on ' +
      'the situation and the firm objectives; overall I would recommend going ahead only if staff ' +
      'are consulted and retrained, because that keeps motivation high while still cutting costs, ' +
      'so ultimately the benefits outweigh the drawbacks for this business in the long term.');
    console.log('essay:', e.awarded + '/' + e.max, e.band, '(wc=' + e.wc + ')');
    assert(e.awarded >= 7, 'developed two-sided essay should reach L3+');
    console.log('ALL MARKER.JS TESTS PASSED');
  }
})(typeof window !== 'undefined' ? window : globalThis);
