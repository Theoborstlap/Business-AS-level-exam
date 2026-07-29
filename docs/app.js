/* UI for the Business 9609 auto-marker website. Loads markscheme.json, renders
 * a paper, marks answers client-side with marker.js, and (optionally) reads
 * handwriting photos with Tesseract.js loaded on demand from a CDN. */
(function () {
  'use strict';
  var DATA = null, CUR = null;
  var $ = function (id) { return document.getElementById(id); };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  fetch('markscheme.json').then(function (r) { return r.json(); })
    .then(function (d) { DATA = d; initPapers(); })
    .catch(function () {
      $('paperArea').innerHTML = '<div class="note">Could not load the question bank ' +
        '(markscheme.json). If you are viewing this file locally, use the GitHub Pages URL instead.</div>';
    });

  function initPapers() {
    $('setSel').addEventListener('change', fillPapers);
    $('loadBtn').addEventListener('click', loadPaper);
    $('markBtn').addEventListener('click', markAll);
    $('clearBtn').addEventListener('click', function () { if (CUR) loadPaper(); });
    fillPapers();
  }

  function fillPapers() {
    var setKey = $('setSel').value;
    var list = setKey === 'A' ? DATA.papersA : DATA.papersB;
    var sel = $('paperSel');
    sel.innerHTML = '';
    list.forEach(function (p) {
      var o = document.createElement('option');
      o.value = p.id;
      o.textContent = (setKey === 'A' ? 'Paper ' + p.id : p.id) + ' - ' + p.title;
      sel.appendChild(o);
    });
  }

  function loadPaper() {
    var setKey = $('setSel').value, pid = $('paperSel').value;
    var paper = DATA[setKey][pid];
    if (!paper) return;
    CUR = { setKey: setKey, pid: pid, paper: paper };
    $('startNote').classList.add('hidden');
    $('summaryBar').classList.remove('hidden');
    $('totalScore').textContent = '-';
    $('totalBreakdown').textContent = '';
    var area = $('paperArea');
    area.innerHTML = '';
    var h = document.createElement('div');
    h.innerHTML = '<h2 style="margin:6px 0">' + (setKey === 'A' ? 'Paper ' + pid : pid) +
      ' - ' + esc(paper.title) + '</h2>' +
      (paper.theme ? '<p class="paper-title">' + esc(paper.theme) + '</p>' : '');
    area.appendChild(h);

    paper.questions.forEach(function (q) {
      var card = document.createElement('div');
      card.className = 'qcard';
      card.id = 'q-' + q.num;
      var html = '<div><span class="qnum">Q' + q.num + '</span>' +
        (q.stem ? '<span class="qstem">' + esc(q.stem) + '</span>' : '') + '</div>';
      q.parts.forEach(function (p, i) {
        var pid2 = q.num + '-' + (p.label || 'x' + i);
        var lbl = p.label ? '(' + esc(p.label) + ') ' : '';
        html += '<div class="part">' +
          '<div class="ptext">' + lbl + esc(p.text) +
          '<span class="marks">[' + p.marks + ']</span>' +
          '<span class="kind">' + Marker.kindOfPart(p) + '</span></div>' +
          '<textarea id="ta-' + pid2 + '" placeholder="Type your answer..."></textarea>' +
          '<div class="photo-row">' +
          '<button class="btn-mini" data-ta="ta-' + pid2 + '" data-status="st-' + pid2 + '">&#128247; Photo (handwriting)</button>' +
          '<span class="ocr-status" id="st-' + pid2 + '"></span>' +
          '</div>' +
          '<div class="result-slot" id="res-' + pid2 + '"></div>' +
          '</div>';
      });
      card.innerHTML = html;
      area.appendChild(card);
    });

    // wire photo buttons
    Array.prototype.forEach.call(area.querySelectorAll('button[data-ta]'), function (b) {
      b.addEventListener('click', function () { pickPhoto(b.getAttribute('data-ta'), b.getAttribute('data-status')); });
    });
    window.scrollTo(0, 0);
  }

  function modelHtml(model) {
    var out = '<div class="model">';
    model.forEach(function (m) {
      if (m.t === 'head') out += '<div><strong>' + esc(m.s) + '</strong></div>';
      else if (m.t === 'level') out += '<div class="lvl">' + esc(m.s) + '</div>';
      else if (m.t === 'calc') out += '<div class="calc">' + esc(m.s) + '</div>';
      else out += '<div>&bull; ' + esc(m.s) + '</div>';
    });
    return out + '</div>';
  }

  function renderPartResult(slot, res) {
    var cls = res.awarded >= res.max ? 'good' : (res.awarded > 0 ? 'part' : 'bad');
    var star = res.indicative ? '~' : '';
    var html = '<div class="result ' + cls + '">' +
      '<span class="score">' + star + res.awarded + ' / ' + res.max + star + '</span> ' +
      '<span class="small">(' + res.kind + (res.indicative ? ', indicative' : '') + ')</span>';
    if (res.kind === 'essay') {
      if (res.band) html += '<div class="small">Indicative band: <strong>' + esc(res.band) + '</strong>. ' + esc(res.desc || '') + '</div>';
      html += '<ul class="checklist">';
      res.checklist.forEach(function (c) {
        html += '<li>' + (c[1] ? '&#9989;' : '&#11036;') + ' ' + esc(c[0]) + '</li>';
      });
      html += '</ul>';
    } else if (res.kind === 'calc') {
      html += '<div class="small">Expected: ' + esc((res.expected || []).join(', ') || '-') +
        ' &nbsp;|&nbsp; matched: ' + esc((res.matched || []).join(', ') || 'none') + '</div>';
    } else {
      if (res.credited && res.credited.length)
        html += '<div class="small credit">Credited: ' + esc(res.credited.join('; ')) + '</div>';
      if (res.awarded < res.max && res.missed && res.missed.length)
        html += '<div class="small miss">Not detected: ' + esc(res.missed.join('; ')) + '</div>';
    }
    html += '<details><summary>Model answer / mark scheme</summary>' + modelHtml(res.model) + '</details>';
    html += '</div>';
    slot.innerHTML = html;
  }

  function markAll() {
    if (!CUR) return;
    var objA = 0, objM = 0, essA = 0, essM = 0, answered = 0;
    CUR.paper.questions.forEach(function (q) {
      q.parts.forEach(function (p, i) {
        var pid2 = q.num + '-' + (p.label || 'x' + i);
        var ta = $('ta-' + pid2);
        var slot = $('res-' + pid2);
        if (!ta || !slot) return;
        var val = ta.value.trim();
        if (val) answered++;
        var res = Marker.markPart(p, val);
        renderPartResult(slot, res);
        if (res.indicative) { essA += res.awarded; essM += res.max; }
        else { objA += res.awarded; objM += res.max; }
      });
    });
    var totA = objA + essA, totM = objM + essM;
    var pct = totM ? Math.round(100 * totA / totM) : 0;
    $('totalScore').textContent = totA + ' / ' + totM + '  (' + pct + '%)';
    var bd = 'Knowledge & calculation: ' + objA + '/' + objM;
    if (essM) bd += '  \u00b7  essays (indicative): ' + essA + '/' + essM;
    if (!answered) bd = 'No answers typed yet - fill some boxes then Mark.';
    $('totalBreakdown').textContent = bd;
    var first = document.querySelector('.result');
    if (first) first.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  // ---- Handwriting OCR (Tesseract.js, loaded on demand) ----
  function loadTesseract() {
    if (window.Tesseract) return Promise.resolve();
    return new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/npm/tesseract.js@5/dist/tesseract.min.js';
      s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  function pickPhoto(taId, statusId) {
    var inp = document.createElement('input');
    inp.type = 'file'; inp.accept = 'image/*';
    inp.addEventListener('change', function () {
      if (inp.files && inp.files[0]) ocrInto(taId, statusId, inp.files[0]);
    });
    inp.click();
  }

  function ocrInto(taId, statusId, file) {
    var ta = $(taId), st = $(statusId);
    st.textContent = 'Loading OCR engine (first time only)...';
    loadTesseract().then(function () {
      st.textContent = 'Reading photo... 0%';
      return Tesseract.recognize(file, 'eng', {
        logger: function (m) {
          if (m.status === 'recognizing text') st.textContent = 'Reading photo... ' + Math.round(m.progress * 100) + '%';
        }
      });
    }).then(function (out) {
      var text = (out && out.data && out.data.text ? out.data.text : '').trim();
      if (text) {
        ta.value = (ta.value ? ta.value + '\n' : '') + text;
        st.textContent = 'Transcribed - please CHECK it is correct, then Mark.';
      } else {
        st.textContent = 'No text could be read - try a clearer, straight-on photo, or type it.';
      }
    }).catch(function () {
      st.textContent = 'OCR unavailable (offline?). Please type this answer instead.';
    });
  }
})();
