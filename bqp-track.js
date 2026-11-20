/* Bharat Quantum Prospera: Microsoft Clarity loader + lead attribution.
   1. Loads Microsoft Clarity when CLARITY_ID is set (never on localhost or file://).
   2. Remembers how the visitor arrived (search engine / AI assistant / site / direct, landing page and, where the
      referrer exposes it, the search words) - last non-direct visit, kept 30 days in localStorage.
   3. On a click on a WhatsApp, email, phone, book-a-call or get-a-quote link: sends a Clarity custom event and tags,
      and adds a short "[Ref: page | via source]" line to the pre-filled WhatsApp / email text, so each enquiry shows
      which page and which source produced it. No personal data is stored. */
(function (root) {
  'use strict';
  var CLARITY_ID = 'zgq0b04kz1';
  var KEY = 'bqp_attr', TTL = 30 * 24 * 3600 * 1000;

  var ENGINES = [
    [/(^|\.)gemini\.google\.com$/, 'gemini'], [/(^|\.)google\.[a-z.]+$/, 'google'], [/(^|\.)bing\.com$/, 'bing'],
    [/(^|\.)duckduckgo\.com$/, 'duckduckgo'], [/(^|\.)yahoo\.[a-z.]+$/, 'yahoo'], [/(^|\.)yandex\.[a-z.]+$/, 'yandex'],
    [/(^|\.)baidu\.com$/, 'baidu'], [/(^|\.)ecosia\.org$/, 'ecosia'], [/(^|\.)brave\.com$/, 'brave'],
    [/(^|\.)(chatgpt\.com|chat\.openai\.com|openai\.com)$/, 'chatgpt'], [/(^|\.)perplexity\.ai$/, 'perplexity'],
    [/(^|\.)copilot\.microsoft\.com$/, 'copilot'], [/(^|\.)claude\.ai$/, 'claude'],
    [/(^|\.)linkedin\.com$|(^|\.)lnkd\.in$/, 'linkedin'], [/(^|\.)(facebook\.com|fb\.com)$/, 'facebook'],
    [/(^|\.)instagram\.com$/, 'instagram'], [/(^|\.)(twitter\.com|x\.com|t\.co)$/, 'x'],
    [/(^|\.)youtube\.com$|(^|\.)youtu\.be$/, 'youtube'], [/(^|\.)(whatsapp\.com|wa\.me)$/, 'whatsapp'],
    [/(^|\.)reddit\.com$/, 'reddit'], [/(^|\.)quora\.com$/, 'quora']
  ];

  function clean(s, n) { return String(s || '').replace(/[\r\n\[\]|]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n || 80); }

  function slug(pathname) {
    var p = String(pathname || '').replace(/^\/+/, '').replace(/\.html$/, '').replace(/\/+$/, '');
    return clean(p || 'home', 70);
  }

  /* Returns {src, q} for an external arrival, or null when the referrer is this site or missing with no utm. */
  function classify(referrer, search, host) {
    var utm = '';
    try { utm = new URLSearchParams(search || '').get('utm_source') || ''; } catch (e) {}
    if (utm) return { src: clean(utm, 30).toLowerCase(), q: '' };
    if (!referrer) return null;
    var u; try { u = new URL(referrer); } catch (e) { return null; }
    var h = u.hostname.replace(/^www\./, ''), own = String(host || '').replace(/^www\./, '');
    if (!h || h === own) return null;
    var src = h;
    for (var i = 0; i < ENGINES.length; i++) { if (ENGINES[i][0].test(h)) { src = ENGINES[i][1]; break; } }
    var q = u.searchParams.get('q') || u.searchParams.get('p') || u.searchParams.get('query') || u.searchParams.get('text') || '';
    return { src: src, q: clean(q, 80) };
  }

  function refText(a, page) {
    var parts = ['Ref: ' + page, 'via ' + (a && a.src ? a.src : 'direct')];
    if (a && a.lp && a.lp !== page) parts.push('first page: ' + a.lp);
    if (a && a.q) parts.push('search: ' + a.q);
    return parts.join(' | ');
  }

  function tagWhatsApp(href, ref) {
    var add = encodeURIComponent('\n\n[' + ref + ']');
    if (/[?&]text=/.test(href)) return href.replace(/([?&]text=)([^&#]*)/, function (m, p, v) { return p + v + add; });
    return href + (href.indexOf('?') > -1 ? '&' : '?') + 'text=' + encodeURIComponent('[' + ref + ']');
  }

  function tagMailto(href, ref) {
    var add = encodeURIComponent('\n\n[' + ref + ']');
    if (/[?&]body=/.test(href)) return href.replace(/([?&]body=)([^&#]*)/, function (m, p, v) { return p + v + add; });
    return href + (href.indexOf('?') > -1 ? '&' : '?') + 'body=' + encodeURIComponent('[' + ref + ']');
  }

  function linkKind(href) {
    if (/wa\.me\/|api\.whatsapp\.com/i.test(href)) return 'whatsapp';
    if (/^mailto:/i.test(href)) return 'email';
    if (/^tel:/i.test(href)) return 'phone';
    if (/book-a-call\.html/i.test(href)) return 'book_call_link';
    if (/get-a-quote\.html/i.test(href)) return 'quote_link';
    return '';
  }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { classify: classify, slug: slug, refText: refText, tagWhatsApp: tagWhatsApp, tagMailto: tagMailto, linkKind: linkKind };
    return;
  }

  var w = root, d = w.document, loc = w.location;
  if (!d || !loc) return;

  if (CLARITY_ID && loc.protocol !== 'file:' && !/^(localhost|127\.0\.0\.1|\[::1\])$/.test(loc.hostname)) {
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(w, d, 'clarity', 'script', CLARITY_ID);
  }
  function cl() { if (w.clarity) { try { w.clarity.apply(null, arguments); } catch (e) {} } }

  var page = slug(loc.pathname), attr = null, now = Date.now();
  try { attr = JSON.parse(w.localStorage.getItem(KEY) || 'null'); } catch (e) { attr = null; }
  if (attr && (!attr.t || now - attr.t > TTL)) attr = null;
  var ext = classify(d.referrer, loc.search, loc.hostname);
  if (ext) attr = { src: ext.src, q: ext.q, lp: page, t: now };
  else if (!attr) attr = { src: 'direct', q: '', lp: page, t: now };
  try { w.localStorage.setItem(KEY, JSON.stringify(attr)); } catch (e) {}

  cl('set', 'lead_source', attr.src);
  cl('set', 'landing_page', attr.lp);
  if (attr.q) cl('set', 'search_query', attr.q);
  if (page === 'book-a-call') cl('event', 'view_book_a_call');
  if (page === 'get-a-quote') cl('event', 'view_get_a_quote');

  w.bqpRef = function () { return refText(attr, page); };

  d.addEventListener('click', function (e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '', kind = linkKind(href);
    if (!kind) return;
    cl('set', 'lead_page', page);
    cl('set', 'lead_channel', kind);
    cl('event', 'lead_' + kind);
    if (kind === 'whatsapp' || kind === 'email' || kind === 'phone') cl('upgrade', 'lead_' + kind);
    if ((kind === 'whatsapp' || kind === 'email') && !a.getAttribute('data-bqp-ref')) {
      a.setAttribute('href', kind === 'whatsapp' ? tagWhatsApp(href, w.bqpRef()) : tagMailto(href, w.bqpRef()));
      a.setAttribute('data-bqp-ref', '1');
    }
  }, true);
})(typeof window !== 'undefined' ? window : this);
