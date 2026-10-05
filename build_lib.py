# -*- coding: utf-8 -*-
"""Shared helpers for BQP SEO page builders.

Provides: DOMAIN, HEADER, FOOTER, PAGE_STYLE, page(), write_page(), schema helpers."""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://bharatquantumprospera.com"

HEADER = """<header class="site-header" id="siteHeader">
  <a href="index.html" class="logo-mark" aria-label="Bharat Quantum Prospera"><svg class="bqp-mark" width="52" height="34" viewBox="0 0 110 64" aria-hidden="true"><text x="2" y="48" font-family="Inter,system-ui,sans-serif" font-size="46" font-weight="700" letter-spacing="-3" fill="currentColor">bqp<tspan fill="#C2312A" dx="-1">.</tspan></text></svg></a>
  <nav class="nav-pills" id="navPills">
    <a href="services.html" class="nav-pill">Services</a>
    <a href="industries.html" class="nav-pill">Industries</a>
    <a href="about.html" class="nav-pill">About</a>
    <a href="insights.html" class="nav-pill">Insights</a>
  </nav>
  <div class="nav-right">
    <a href="get-a-quote.html" class="nav-cta">Get a quote</a>
  </div>
  <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navPills" aria-label="Menu">Menu</button>
</header>"""

FOOTER = """<footer class="footer">
  <div class="footer-card">
    <div class="footer-inner">
      <div class="footer-top">
        <div class="footer-brand">
          <h3>Bharat Quantum<br/>Prospera</h3>
          <p>A chartered advisory built for founders who think beyond borders.</p>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="services.html">All Services</a></li>
            <li><a href="us-incorporation.html">US Incorporation</a></li>
            <li><a href="capital-advisory.html">Capital Advisory</a></li>
            <li><a href="fund-raising.html">Fund Raising</a></li>
            <li><a href="corporate-strategy.html">M&amp;A &amp; Corporate Strategy</a></li>
            <li><a href="sme-ipo.html">IPO Services</a></li>
            <li><a href="startup-registration.html">Startup Registration</a></li>
            <li><a href="transfer-pricing.html">Transfer Pricing</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Firm</h5>
          <ul>
            <li><a href="industries.html">Industries</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="insights.html">Insights</a></li>
            <li><a href="careers.html">Careers</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="founder.html">Founder</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Reach</h5>
          <ul>
            <li><a href="tel:+917801887130">+91 78018 87130</a></li>
            <li><a href="mailto:durgesh@bharatquantumprospera.com">durgesh@bharatquantumprospera.com</a></li>
            <li>Ahmedabad &middot; Mumbai</li>
            <li>Bengaluru &middot; Rajkot</li>
            <li>Dubai, UAE</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Bharat Quantum Prospera. All rights reserved.</span>
        <span>Ahmedabad &middot; Est. in Practice</span>
      </div>
    </div>
  </div>
</footer>"""

PAGE_STYLE = """<style>
  .svc-hero{padding:140px 5vw 72px;max-width:1400px;margin:0 auto}
  .svc-hero .back{display:inline-block;margin-bottom:22px;padding:6px 14px;border:1px solid var(--line-strong);border-radius:4px;font-size:12px;font-weight:500;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-2);text-decoration:none}
  .svc-hero .kicker{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--red);margin-bottom:12px}
  .svc-hero h1{font-weight:400;text-transform:uppercase;line-height:1.05;letter-spacing:-.02em;font-size:clamp(32px,4.4vw,58px);color:var(--ink);margin-bottom:22px;max-width:1100px}
  .svc-hero h1 em{font-style:normal;color:var(--red)}
  .svc-hero .lead{font-size:17px;line-height:1.6;color:var(--ink-2);max-width:860px;margin-bottom:28px}
  .svc-hero .cta-row{display:flex;flex-wrap:wrap;gap:12px}
  .svc-hero .cta-row a{display:inline-flex;align-items:center;padding:12px 24px;font-size:14px;font-weight:600;letter-spacing:-.01em;text-decoration:none;border-radius:4px}
  .svc-hero .cta-row .primary{background:var(--red);color:#fff}
  .svc-hero .cta-row .ghost{background:transparent;color:var(--ink);border:1px solid var(--line-strong)}

  .section{padding:0 5vw 20px;max-width:1400px;margin:0 auto}
  .section:first-of-type{padding-top:0}
  .card{background:#fff;border:1px solid var(--border);border-radius:8px;padding:clamp(28px,4vw,48px);margin-bottom:20px}
  .card-label{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:var(--red);margin-bottom:14px}
  .card-h2{font-size:clamp(22px,2.8vw,36px);font-weight:400;text-transform:uppercase;letter-spacing:-.02em;line-height:1.1;color:var(--ink);margin-bottom:22px;max-width:1000px}
  .card-h2 em{font-style:normal;color:var(--red)}
  .card-body{font-size:15px;line-height:1.7;color:var(--ink);max-width:900px}
  .card-body p{margin-bottom:1em}
  .card-body strong{font-weight:600}
  .card-body code{background:var(--cream);padding:2px 8px;border-radius:3px;font-size:13px;font-family:'SF Mono',Menlo,monospace}
  .card-body ol,.card-body ul{margin:1em 0 1em 1.4em}
  .card-body li{margin-bottom:.55em}
  .card-body a{color:var(--red);text-decoration:underline;text-underline-offset:3px}

  .faq-item{padding:20px 0;border-bottom:1px solid var(--border)}
  .faq-item:last-child{border-bottom:0}
  .faq-q{font-size:15px;font-weight:600;color:var(--ink);margin-bottom:10px;letter-spacing:-.01em}
  .faq-a{font-size:14px;line-height:1.65;color:var(--ink-2)}

  .cta-card{background:var(--red);color:#fff;padding:clamp(32px,4vw,56px);border-radius:8px;margin-bottom:20px}
  .cta-card .card-label{color:rgba(255,255,255,.78)}
  .cta-card .card-h2{color:#fff}
  .cta-card .card-body{color:rgba(255,255,255,.92)}
  .cta-card .btn-row{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px}
  .cta-card .btn-row a{display:inline-flex;align-items:center;padding:12px 22px;font-size:13px;font-weight:600;letter-spacing:-.01em;text-decoration:none;border-radius:4px}
  .cta-card .btn-row .solid{background:#fff;color:var(--ink)}
  .cta-card .btn-row .outline{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.6)}

  .related-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:14px}
  .related-item{display:block;padding:22px 20px;background:var(--cream);border:1px solid var(--border);border-radius:6px;text-decoration:none;color:var(--ink)}
  .related-item:hover{border-color:var(--red)}
  .related-item .rl{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--red);margin-bottom:6px;font-weight:600}
  .related-item .rt{font-size:15px;font-weight:600;color:var(--ink);line-height:1.3}
</style>"""


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, separators=(',', ':'), ensure_ascii=False) + '</script>'


def breadcrumb(slug, title):
    return ld({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN},
            {"@type": "ListItem", "position": 2, "name": "Insights", "item": f"{DOMAIN}/insights.html"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"{DOMAIN}/{slug}.html"},
        ]
    })


def faq_schema(faqs):
    return ld({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    })


def article_schema(slug, title, desc):
    return ld({
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "description": desc, "url": f"{DOMAIN}/{slug}.html",
        "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/founder.html"},
        "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN},
        "inLanguage": "en"
    })


def page(slug, title, description, keywords, hero_kicker, hero_title_html, hero_lead,
         sections, faqs, related, cta_headline, cta_body, howto=None):
    schemas = [breadcrumb(slug, title.split(' | ')[0]), faq_schema(faqs), article_schema(slug, title, description)]
    if howto:
        schemas.append(ld({
            "@context": "https://schema.org", "@type": "HowTo",
            "name": howto["name"], "description": howto["description"],
            "step": [{"@type": "HowToStep", "position": i + 1, "name": s["name"], "text": s["text"]} for i, s in enumerate(howto["steps"])]
        }))

    sect_html = "\n".join(
        f'<section class="section"><div class="card"><p class="card-label">{lbl}</p><h2 class="card-h2">{h2}</h2><div class="card-body">{body}</div></div></section>'
        for lbl, h2, body in sections
    )

    faq_items = "\n".join(f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q, a in faqs)
    faq_html = f'<section class="section"><div class="card"><p class="card-label">FAQ</p><h2 class="card-h2">Common questions, <em>answered.</em></h2><div class="card-body">{faq_items}</div></div></section>'

    related_items = "\n".join(f'<a href="{h}" class="related-item"><div class="rl">{lbl}</div><div class="rt">{t}</div></a>' for h, lbl, t in related)
    related_html = f'<section class="section"><div class="card"><p class="card-label">Related reading</p><h2 class="card-h2">Keep <em>going.</em></h2><div class="card-body"><div class="related-grid">{related_items}</div></div></div></section>'

    cta_html = f'''<section class="section"><div class="cta-card">
      <p class="card-label">/ Ready when you are</p>
      <h2 class="card-h2">{cta_headline}</h2>
      <div class="card-body"><p>{cta_body}</p></div>
      <div class="btn-row">
        <a href="get-a-quote.html" class="solid">Get a firm quote &rarr;</a>
        <a href="https://wa.me/917801887130" target="_blank" rel="noopener" class="outline">WhatsApp Durgesh</a>
      </div>
    </div></section>'''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/svg+xml" href="favicon.svg"/>
<title>{title}</title>
<meta name="description" content="{description}"/>
<meta name="keywords" content="{keywords}"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta name="author" content="CA Durgesh Chavda, Bharat Quantum Prospera"/>
<link rel="canonical" href="{DOMAIN}/{slug}.html"/>
<link rel="alternate" hreflang="en" href="{DOMAIN}/{slug}.html"/>
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{slug}.html"/>
<meta property="og:type" content="article"/>
<meta property="og:site_name" content="Bharat Quantum Prospera"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{description}"/>
<meta property="og:url" content="{DOMAIN}/{slug}.html"/>
<meta property="og:image" content="{DOMAIN}/og-cover.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{description}"/>
<meta name="twitter:image" content="{DOMAIN}/og-cover.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="bqp.css"/>
{PAGE_STYLE}
{chr(10).join(schemas)}
</head>
<body>
{HEADER}
<main>
<section class="svc-hero">
  <a href="us-incorporation.html" class="back">&larr; US Incorporation</a>
  <p class="kicker">{hero_kicker}</p>
  <h1>{hero_title_html}</h1>
  <p class="lead">{hero_lead}</p>
  <div class="cta-row">
    <a href="get-a-quote.html" class="primary">Get a firm quote &rarr;</a>
    <a href="https://wa.me/917801887130" target="_blank" rel="noopener" class="ghost">WhatsApp instead</a>
  </div>
</section>
{sect_html}
{cta_html}
{faq_html}
{related_html}
</main>
{FOOTER}
</body>
</html>
"""


def write_page(slug, html):
    with open(os.path.join(ROOT, slug + ".html"), "w", encoding="utf-8", newline="\r\n") as f:
        f.write(html)
