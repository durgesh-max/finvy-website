/* Bharat Quantum Prospera: Microsoft Clarity loader + lead attribution + cookie consent.
   1. Loads Microsoft Clarity when CLARITY_ID is set (never on localhost or file://).
   2. Remembers how the visitor arrived (search engine / AI assistant / site / direct, landing page and, where the
      referrer exposes it, the search words) - last non-direct visit, kept 30 days in localStorage.
   3. On a click on a WhatsApp, email, phone, book-a-call or get-a-quote link: sends a Clarity custom event and tags,
      and adds a short "[Ref: page | via source]" line to the pre-filled WhatsApp / email text, so each enquiry shows
      which page and which source produced it. No personal data is stored.
   4. Consent: visitors in the UK, EEA and Switzerland (detected by time zone) are asked first - Clarity is not loaded
      and nothing is stored until they accept. Elsewhere Clarity runs with a notice and a Decline button. The choice is
      kept in localStorage (bqp_consent); window.bqpConsent.open() re-opens the banner (used on privacy.html). */
(function (root) {
  'use strict';
  var CLARITY_ID = 'zgq0b04kz1';
  var KEY = 'bqp_attr', CONSENT_KEY = 'bqp_consent', TTL = 30 * 24 * 3600 * 1000;

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

  var OPT_IN_ZONES = /^(Europe\/|Atlantic\/(Reykjavik|Canary|Madeira|Azores|Faroe|Jan_Mayen)$|Asia\/(Nicosia|Famagusta)$|Arctic\/Longyearbyen$|America\/(Cayenne|Guadeloupe|Martinique|Marigot|St_Barthelemy)$|Indian\/(Reunion|Mayotte)$|(GB|GB-Eire|Eire|Portugal|Poland|Iceland|CET|EET|WET|MET)$)/;

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
    if (/topmate\.io\//i.test(href)) return 'topmate_call';
    if (/get-a-quote\.html/i.test(href)) return 'quote_link';
    return '';
  }

  /* True when the browser time zone is in the UK, EEA, Switzerland or elsewhere in Europe: ask before any analytics. */
  function optInZone(tz) { return OPT_IN_ZONES.test(String(tz || '')); }

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { classify: classify, slug: slug, refText: refText, tagWhatsApp: tagWhatsApp, tagMailto: tagMailto, linkKind: linkKind, optInZone: optInZone };
    return;
  }

  var w = root, d = w.document, loc = w.location;
  if (!d || !loc) return;

  var live = !!CLARITY_ID && loc.protocol !== 'file:' && !/^(localhost|127\.0\.0\.1|\[::1\])$/.test(loc.hostname);
  function read(k) { try { return w.localStorage.getItem(k); } catch (e) { return null; } }
  function store(k, v) { try { if (v === null) w.localStorage.removeItem(k); else w.localStorage.setItem(k, v); } catch (e) {} }

  var tz = '';
  try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone || ''; } catch (e) {}
  var optIn = optInZone(tz) || /[?&]bqp_optin=1(&|$)/.test(loc.search);
  var choice = null;
  try { var saved = JSON.parse(read(CONSENT_KEY) || 'null'); if (saved && (saved.v === 'granted' || saved.v === 'denied')) choice = saved.v; } catch (e) {}
  function mayTrack() { return choice === 'granted' || (choice === null && !optIn); }

  var loaded = false, tagged = false;
  function loadClarity() {
    if (loaded || !live) return;
    loaded = true;
    (function (c, l, a, r, i, t, y) {
      c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
      t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i;
      y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
    })(w, d, 'clarity', 'script', CLARITY_ID);
  }
  function cl() { if (w.clarity) { try { w.clarity.apply(null, arguments); } catch (e) {} } }

  var page = slug(loc.pathname), attr = null, now = Date.now();
  if (mayTrack()) { try { attr = JSON.parse(read(KEY) || 'null'); } catch (e) { attr = null; } }
  if (attr && (!attr.t || now - attr.t > TTL)) attr = null;
  var ext = classify(d.referrer, loc.search, loc.hostname);
  if (ext) attr = { src: ext.src, q: ext.q, lp: page, t: now };
  else if (!attr) attr = { src: 'direct', q: '', lp: page, t: now };

  function sendTags() {
    if (tagged) return;
    tagged = true;
    cl('set', 'lead_source', attr.src);
    cl('set', 'landing_page', attr.lp);
    if (attr.q) cl('set', 'search_query', attr.q);
    if (page === 'book-a-call') cl('event', 'view_book_a_call');
    if (page === 'get-a-quote') cl('event', 'view_get_a_quote');
  }
  function start() {
    store(KEY, JSON.stringify(attr));
    loadClarity();
    if (choice === 'granted') cl('consentv2', { ad_Storage: 'denied', analytics_Storage: 'granted' });
    sendTags();
  }
  if (mayTrack()) start();

  w.bqpRef = function () { return refText(attr, page); };

  function hideBanner() { var el = d.getElementById('bqp-consent'); if (el && el.parentNode) el.parentNode.removeChild(el); }
  function setChoice(v) {
    choice = v;
    store(CONSENT_KEY, JSON.stringify({ v: v, t: Date.now() }));
    if (v === 'granted') start();
    else {
      store(KEY, null);
      cl('consentv2', { ad_Storage: 'denied', analytics_Storage: 'denied' });
      cl('consent', false);
      cl('stop');
    }
    hideBanner();
  }
  function showBanner() {
    if (!d.body || d.getElementById('bqp-consent')) return;
    if (!d.getElementById('bqp-consent-css')) {
      var st = d.createElement('style'); st.id = 'bqp-consent-css';
      st.textContent = '#bqp-consent{position:fixed;left:14px;bottom:14px;z-index:90;max-width:400px;background:#0E1116;color:#fff;padding:14px 16px;border-radius:10px;box-shadow:0 12px 34px rgba(14,17,22,.28);font:400 13px/1.5 Inter,system-ui,sans-serif}' +
        '#bqp-consent p{margin:0 0 10px;color:#fff}#bqp-consent a{color:#fff;text-decoration:underline}' +
        '#bqp-consent .bqp-consent-row{display:flex;gap:8px}' +
        '#bqp-consent button{flex:1;min-height:38px;padding:8px 14px;border-radius:6px;border:1px solid #fff;background:#fff;color:#0E1116;font:600 13px/1 Inter,system-ui,sans-serif;cursor:pointer}' +
        '#bqp-consent button:focus-visible{outline:2px solid #fff;outline-offset:2px}' +
        '#bqp-consent.bqp-compact{display:flex;align-items:center;gap:10px;padding:10px 12px}' +
        '#bqp-consent.bqp-compact p{margin:0;flex:1;font-size:12.5px;line-height:1.4}' +
        '#bqp-consent.bqp-compact .bqp-consent-row{flex:none;gap:6px}' +
        '#bqp-consent.bqp-compact button{flex:none;min-height:34px;padding:7px 11px}' +
        '@media (max-width:640px){#bqp-consent{left:10px;right:10px;bottom:122px;max-width:none}}' +
        '@media print{#bqp-consent{display:none}}';
      d.head.appendChild(st);
    }
    var el = d.createElement('div');
    el.id = 'bqp-consent'; el.setAttribute('role', 'region'); el.setAttribute('aria-label', 'Cookie choice');
    var lead = optIn
      ? 'With your permission, we use Microsoft Clarity to see how visitors use this site (clicks, scrolling, pages viewed). It sets cookies. No advertising.'
      : 'This site uses Microsoft Clarity analytics cookies. No advertising.';
    // Outside the opt-in zones this is a notice with a decline button, so it is kept to one compact row:
    // on phones the full-size version covered the answer and the call buttons.
    if (!optIn) el.className = 'bqp-compact';
    el.innerHTML = '<p>' + lead + ' <a href="privacy.html">' + (optIn ? 'Privacy and cookies' : 'Privacy') + '</a></p>' +
      '<div class="bqp-consent-row"><button type="button" data-bqp-consent="granted">' + (optIn ? 'Accept' : 'OK') + '</button><button type="button" data-bqp-consent="denied">Decline</button></div>';
    el.addEventListener('click', function (e) {
      var v = e.target && e.target.getAttribute ? e.target.getAttribute('data-bqp-consent') : null;
      if (v) setChoice(v);
    });
    d.body.appendChild(el);
  }
  w.bqpConsent = {
    open: showBanner,
    state: function () { return { choice: choice, optIn: optIn, clarityLoaded: loaded, tracking: mayTrack() }; }
  };
  if (choice === null) showBanner();

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
