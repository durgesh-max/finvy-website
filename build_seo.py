# -*- coding: utf-8 -*-
"""BQP SEO page builder — compact, self-contained, cream/orange/Martian Mono."""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://bharatquantumprospera.com"
AUTHOR = "CA Durgesh Chavda, Bharat Quantum Prospera"
WA = "https://wa.me/917801887130"

STYLE = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--orange:#CC4A1A;--orange-dark:#A93D13;--orange-accent:#FF5F00;--cream:#F4F1DB;--cream-2:#E8E1C4;--ink:#463325;--ink-2:#7A6150;--ink-3:#A89481;--border:rgba(70,51,37,.18);--border-strong:rgba(70,51,37,.3);--ff-mono:'Martian Mono','JetBrains Mono','Geist Mono','Space Mono',ui-monospace,SFMono-Regular,Menlo,monospace}
html{scroll-behavior:smooth;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;background:var(--cream)}
body{background:var(--cream);color:var(--ink);font-family:var(--ff-mono);font-size:15px;line-height:1.6;overflow-x:hidden}
::selection{background:var(--orange);color:var(--cream)}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.site-header{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:18px 26px;pointer-events:none;background:linear-gradient(to bottom,rgba(244,241,219,.95),rgba(244,241,219,0));backdrop-filter:blur(6px)}
.site-header > *{pointer-events:auto}
.logo-mark{color:var(--ink);display:flex;align-items:center;transition:transform .2s}
.logo-mark:hover{transform:scale(1.03)}
.nav-pills{display:flex;gap:8px}
.nav-pill{padding:7px 18px;border:1px solid rgba(70,51,37,.3);border-radius:999px;font-family:var(--ff-mono);font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:-.02em;color:var(--ink);background:transparent;transition:all .2s}
.nav-pill:hover{background:var(--ink);color:var(--cream);border-color:var(--ink)}
.nav-cta{padding:7px 18px;border:1px solid var(--ink);border-radius:999px;background:var(--ink);color:var(--cream);font-family:var(--ff-mono);font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:-.02em;transition:all .2s}
.nav-cta:hover{background:var(--orange);border-color:var(--orange)}
@media(max-width:860px){.nav-pills{display:none}}
main{padding-top:0}
.svc-hero{position:relative;background:var(--orange);color:var(--cream);padding:140px 5vw 80px;min-height:60vh;display:flex;flex-direction:column;justify-content:flex-end}
.svc-hero::before{content:"";position:absolute;inset:0;background-image:repeating-linear-gradient(to right,transparent 0,transparent 38px,rgba(0,0,0,.06) 38px,rgba(0,0,0,.06) 39px);pointer-events:none}
.svc-hero-inner{position:relative;z-index:1;max-width:1400px}
.svc-back{display:inline-block;margin-bottom:32px;padding:7px 16px;border:1px solid rgba(244,241,219,.4);border-radius:999px;font-size:11px;text-transform:uppercase;letter-spacing:-.01em;color:var(--cream);opacity:.85;transition:all .2s}
.svc-back:hover{background:var(--cream);color:var(--ink);opacity:1}
.svc-hero-kicker{font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:.06em;margin-bottom:20px;opacity:.9}
.svc-hero-title{font-family:var(--ff-mono);font-weight:400;text-transform:uppercase;line-height:1.02;letter-spacing:-.025em;font-size:clamp(32px,5.5vw,84px);max-width:1300px}
.svc-hero-title em{font-style:italic;font-weight:400;text-decoration:underline;text-decoration-color:var(--cream);text-decoration-thickness:4px;text-underline-offset:6px}
.svc-hero-lead{margin-top:28px;font-size:clamp(13px,1vw,15px);text-transform:uppercase;letter-spacing:-.01em;line-height:1.55;max-width:820px;opacity:.95}
.section{padding:0 5vw;margin-top:24px}
.section:first-of-type{margin-top:40px}
.card{background:var(--cream);border:1px solid var(--border);border-radius:32px;padding:clamp(28px,4vw,64px);margin-bottom:24px;max-width:1600px;margin-left:auto;margin-right:auto}
.card-label{font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:-.01em;color:var(--ink-2);margin-bottom:28px;opacity:.85}
.card-label::before{content:"/ "}
.card-h2{font-family:var(--ff-mono);font-weight:400;text-transform:uppercase;line-height:1.08;letter-spacing:-.02em;font-size:clamp(22px,3vw,40px);color:var(--ink);margin-bottom:24px;max-width:1100px}
.card-h2 em{font-style:italic;color:var(--orange)}
.card-body{font-size:clamp(14px,1.02vw,16px);line-height:1.7;color:var(--ink);max-width:900px}
.card-body p{margin-bottom:1.2em}
.card-body p:last-child{margin-bottom:0}
.card-body strong{font-weight:600;color:var(--ink)}
.card-body a{color:var(--orange);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.card-body a:hover{color:var(--orange-dark)}
.card-body table{border-collapse:collapse;width:100%;margin:1.5em 0;font-size:13px}
.card-body th{background:var(--cream-2);text-align:left;padding:12px 16px;border:1px solid var(--border);font-weight:500;text-transform:uppercase;letter-spacing:.02em;color:var(--ink-2)}
.card-body td{padding:12px 16px;border:1px solid var(--border);vertical-align:top}
.card-body ol,.card-body ul{margin:1em 0 1.2em 1.4em}
.card-body li{margin-bottom:.5em}
.faq-item{padding:22px 0;border-bottom:1px solid var(--border)}
.faq-item:last-child{border-bottom:0}
.faq-q{font-weight:600;color:var(--ink);margin-bottom:10px;font-size:15px}
.faq-a{color:var(--ink-2);line-height:1.65}
.related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:16px}
.related-item{display:block;padding:24px;border:1px solid var(--border);border-radius:20px;background:var(--cream);color:var(--ink);transition:all .2s}
.related-item:hover{border-color:var(--orange);background:var(--cream-2);transform:translateY(-2px)}
.related-label{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-2);margin-bottom:8px;opacity:.8}
.related-title{font-size:16px;font-weight:500;color:var(--ink);margin-bottom:12px}
.related-arrow{font-size:12px;color:var(--orange);text-transform:uppercase;letter-spacing:.04em}
.cta-box{background:var(--ink);color:var(--cream);border-radius:32px;padding:clamp(28px,4vw,56px);margin-top:40px;max-width:900px}
.cta-box .card-label{color:rgba(244,241,219,.7)}
.cta-box .card-h2{color:var(--cream)}
.cta-box .card-body{color:rgba(244,241,219,.9)}
.cta-btn{display:inline-block;margin-top:20px;padding:14px 28px;background:var(--orange-accent);color:var(--cream);border-radius:999px;font-size:12px;text-transform:uppercase;letter-spacing:.04em;font-weight:600;transition:all .2s}
.cta-btn:hover{background:var(--cream);color:var(--ink)}
.footer{background:var(--ink);color:var(--cream);padding:60px 5vw 40px;margin-top:80px}
.footer-inner{max-width:1600px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:40px;margin-bottom:40px}
.footer h3{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--orange-accent);margin-bottom:16px;font-weight:500}
.footer ul{list-style:none}
.footer li{margin-bottom:8px;font-size:13px;opacity:.85}
.footer a:hover{color:var(--orange-accent);opacity:1}
.footer-bottom{border-top:1px solid rgba(244,241,219,.15);padding-top:24px;font-size:11px;opacity:.7;text-transform:uppercase;letter-spacing:.02em}
"""

HEADER = """<header class="site-header">
  <a href="index.html" class="logo-mark" aria-label="Bharat Quantum Prospera"><svg width="54" height="36" viewBox="0 0 110 64" aria-hidden="true"><text x="5" y="50" font-family="'Plus Jakarta Sans','Inter',system-ui,sans-serif" font-size="50" font-weight="800" letter-spacing="-3" fill="currentColor">bqp<tspan fill="#FF5F00" dx="-2">.</tspan></text></svg></a>
  <nav class="nav-pills">
    <a href="index.html#about" class="nav-pill">About</a>
    <a href="index.html#services" class="nav-pill">Services</a>
    <a href="index.html#founder" class="nav-pill">Founder</a>
    <a href="index.html#global" class="nav-pill">Global</a>
  </nav>
  <a href="index.html#contact" class="nav-cta">Contact</a>
</header>"""

FOOTER = """<footer class="footer">
  <div class="footer-inner">
    <div>
      <h3>Bharat Quantum Prospera</h3>
      <ul>
        <li>CA-led advisory for founders building beyond borders.</li>
        <li>Operating under DRSPV &amp; Associates Chartered Accountants.</li>
        <li>Ahmedabad · Mumbai · Bengaluru · Rajkot · Dubai</li>
      </ul>
    </div>
    <div>
      <h3>Services</h3>
      <ul>
        <li><a href="/us-incorporation.html">US Incorporation</a></li>
        <li><a href="/sme-ipo.html">SME IPO Advisory</a></li>
        <li><a href="/gift-city.html">GIFT City IFSC</a></li>
        <li><a href="/ma-transactions.html">M&amp;A and Transactions</a></li>
        <li><a href="/global-taxation.html">Global Taxation</a></li>
        <li><a href="/esop-compensation.html">ESOP &amp; 409A</a></li>
        <li><a href="/fund-raising.html">Fund Raising</a></li>
      </ul>
    </div>
    <div>
      <h3>Contact</h3>
      <ul>
        <li><a href="https://wa.me/917801887130" target="_blank" rel="noopener">WhatsApp Durgesh</a></li>
        <li><a href="mailto:durgesh@bharatquantumprospera.com">durgesh@bharatquantumprospera.com</a></li>
        <li><a href="tel:+917801887130">+91 78018 87130</a></li>
        <li><a href="/founder.html">Meet the Founder</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    &copy; 2026 Bharat Quantum Prospera &middot; Operating under DRSPV &amp; Associates Chartered Accountants &middot; ICAI registered
  </div>
</footer>"""


def json_ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, separators=(',', ':'), ensure_ascii=False) + '</script>'


def breadcrumb(slug, title, parent="Insights"):
    return json_ld({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN},
            {"@type": "ListItem", "position": 2, "name": parent, "item": f"{DOMAIN}/#insights"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"{DOMAIN}/{slug}.html"},
        ],
    })


def faq_schema(faqs):
    return json_ld({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
        ],
    })


def article_schema(slug, title, description):
    return json_ld({
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": description,
        "url": f"{DOMAIN}/{slug}.html",
        "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/founder.html"},
        "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN},
        "inLanguage": "en-IN",
    })


def howto_schema(name, description, steps):
    return json_ld({
        "@context": "https://schema.org", "@type": "HowTo",
        "name": name, "description": description,
        "step": [{"@type": "HowToStep", "position": i + 1, "name": s["name"], "text": s["text"]}
                 for i, s in enumerate(steps)],
    })


def related_grid(items):
    parts = ['<div class="related-grid">']
    for href, label, title in items:
        parts.append(
            f'<a href="{href}" class="related-item">'
            f'<div class="related-label">{label}</div>'
            f'<div class="related-title">{title}</div>'
            f'<div class="related-arrow">Read more &rarr;</div>'
            f'</a>'
        )
    parts.append('</div>')
    return "\n".join(parts)


def cta_box(headline, body):
    return f"""<div class="cta-box">
  <p class="card-label">Ready when you are</p>
  <h2 class="card-h2">{headline}</h2>
  <div class="card-body"><p>{body}</p>
    <a href="{WA}?text=Hi%20Durgesh%2C%20I%20have%20a%20question." class="cta-btn" target="_blank" rel="noopener">WhatsApp Durgesh &rarr;</a>
  </div>
</div>"""


def build_page(slug, title, description, keywords, hero_kicker, hero_title_html,
               hero_lead, sections, faqs, related, extra_schemas=None,
               article=True, howto=None, cta_headline=None, cta_body=None,
               lang="en", og_locale="en_IN", hreflang_alts=None,
               canonical_path=None, subdir="", back_href="index.html",
               back_label="Back to home", faq_section_title="Frequently asked questions",
               faq_section_h2="Common questions, <em>answered.</em>",
               related_label="Related reading",
               related_h2="Continue where <em>you left off.</em>",
               cta_label="Ready when you are",
               cta_btn_text="WhatsApp Durgesh &rarr;"):
    """
    sections: list of (label, h2_html, body_html)
    faqs: list of (question, answer)
    related: list of (href, label, title)
    """
    schemas = [breadcrumb(slug, title.split(' | ')[0]), faq_schema(faqs)]
    if article:
        schemas.append(article_schema(slug, title, description))
    if howto:
        schemas.append(howto_schema(howto["name"], howto["description"], howto["steps"]))
    if extra_schemas:
        schemas.extend(extra_schemas)
    schema_block = "\n".join(schemas)

    section_html = []
    for label, h2, body in sections:
        section_html.append(f"""<section class="section">
  <div class="card">
    <p class="card-label">{label}</p>
    <h2 class="card-h2">{h2}</h2>
    <div class="card-body">{body}</div>
  </div>
</section>""")

    faq_html_items = "\n".join(
        f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>'
        for q, a in faqs
    )
    faq_section = f"""<section class="section">
  <div class="card">
    <p class="card-label">{faq_section_title}</p>
    <h2 class="card-h2">{faq_section_h2}</h2>
    <div class="card-body">{faq_html_items}</div>
  </div>
</section>"""

    cta_section = ""
    if cta_headline:
        cta_html = f"""<div class="cta-box">
  <p class="card-label">{cta_label}</p>
  <h2 class="card-h2">{cta_headline}</h2>
  <div class="card-body"><p>{cta_body}</p>
    <a href="{WA}?text=Hi%20Durgesh%2C%20I%20have%20a%20question." class="cta-btn" target="_blank" rel="noopener">{cta_btn_text}</a>
  </div>
</div>"""
        cta_section = f'<section class="section"><div style="max-width:1600px;margin:0 auto">{cta_html}</div></section>'

    related_section = f"""<section class="section">
  <div class="card">
    <p class="card-label">{related_label}</p>
    <h2 class="card-h2">{related_h2}</h2>
    <div class="card-body">{related_grid(related)}</div>
  </div>
</section>"""

    canonical_url = f"{DOMAIN}/{canonical_path}" if canonical_path else f"{DOMAIN}/{slug}.html"
    if hreflang_alts:
        hreflang_block = "\n".join(
            f'<link rel="alternate" hreflang="{code}" href="{href}"/>' for code, href in hreflang_alts
        )
    else:
        hreflang_block = (
            f'<link rel="alternate" hreflang="en-IN" href="{canonical_url}"/>\n'
            f'<link rel="alternate" hreflang="x-default" href="{canonical_url}"/>'
        )

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/svg+xml" href="/favicon.svg"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<meta name="keywords" content="{keywords}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta name="author" content="{AUTHOR}"/>
<link rel="canonical" href="{canonical_url}"/>
{hreflang_block}
<meta property="og:type" content="article"/>
<meta property="og:locale" content="{og_locale}"/>
<meta property="og:site_name" content="Bharat Quantum Prospera"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{canonical_url}"/>
<meta property="og:image" content="{DOMAIN}/bqp-logo.svg"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="{DOMAIN}/bqp-logo.svg"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Martian+Mono:wght@100..800&display=swap" rel="stylesheet"/>
<style>{STYLE}</style>
{schema_block}
</head>
<body>
{HEADER}
<main>
<section class="svc-hero">
  <a href="{back_href}" class="svc-back">&larr; {back_label}</a>
  <div class="svc-hero-inner">
    <p class="svc-hero-kicker">{hero_kicker}</p>
    <h1 class="svc-hero-title">{hero_title_html}</h1>
    <p class="svc-hero-lead">{hero_lead}</p>
  </div>
</section>
{chr(10).join(section_html)}
{cta_section}
{faq_section}
{related_section}
</main>
{FOOTER}
</body>
</html>"""


def write_page_subdir(subdir, slug, html):
    """Write page to a subdirectory (e.g. 'es' or 'pt'). Creates dir if needed."""
    full_dir = os.path.join(ROOT, subdir)
    os.makedirs(full_dir, exist_ok=True)
    path = os.path.join(full_dir, slug + ".html")
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(html)
    return path


def write_page(slug, html):
    path = os.path.join(ROOT, slug + ".html")
    with open(path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(html)
    return path
