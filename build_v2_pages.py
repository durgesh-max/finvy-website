# -*- coding: utf-8 -*-
"""Build long-tail SEO pages matching current main design system (Inter, bqp.css)."""
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
    print("wrote", slug + ".html")


# ============================================================
# PAGES
# ============================================================

# 1. how-to-get-ein-without-ssn
write_page("how-to-get-ein-without-ssn", page(
    slug="how-to-get-ein-without-ssn",
    title="How to Get an EIN Without an SSN (2026) | Foreign Founder Guide - BQP",
    description="Step-by-step guide to getting an IRS Employer Identification Number for your US company when you have no SSN or ITIN. Form SS-4, the IRS International EIN line, Line 7b trick, typical timelines.",
    keywords="EIN without SSN, EIN no SSN, EIN foreign founder, Form SS-4 foreign applicant, IRS International EIN, how to get EIN India, EIN Brazil, EIN LLC no SSN, EIN C-Corp without social",
    hero_kicker="/ How-to &middot; US setup",
    hero_title_html="Getting an EIN, <em>without an SSN.</em>",
    hero_lead="Every foreign founder forming a US LLC or C-Corp needs an Employer Identification Number from the IRS. You don't need an SSN or ITIN to get one. The process has specific wording the IRS expects on Line 7b of Form SS-4 and specific channels &mdash; here's exactly how it works.",
    sections=[
        ("/ Overview", "What an EIN is &mdash; and why nothing works without it.",
         "<p>The EIN (Employer Identification Number) is a 9-digit tax ID the IRS assigns to every US business entity. It is the corporate equivalent of an individual's SSN. Mercury, Brex, Relay, Stripe, every US bank, every state tax authority, every US business counterparty will ask for it. You cannot open a US business bank account, process payments, sign enterprise contracts, or file US tax returns without one.</p>"
         "<p>For foreign founders &mdash; Indian, Brazilian, Mexican, UK, UAE, SG, anywhere &mdash; the EIN is accessible without an SSN or ITIN. The IRS has an International EIN unit specifically for this. Most founders don't know this exists and either (a) delay their formation while trying to get an ITIN first (unnecessary; adds 8-14 weeks), or (b) hire expensive agents to do it when they could have done it themselves in a week.</p>"),
        ("/ The four application channels", "Fax wins for foreign founders.",
         "<p><strong>1. Online.</strong> At <code>irs.gov/ein</code>. Instant EIN &mdash; but requires an SSN or ITIN of the Responsible Party. Not available to foreign founders.</p>"
         "<p><strong>2. Fax.</strong> Form SS-4 faxed to the IRS International EIN unit at <code>+1-855-215-1627</code>. Response by fax within 4-11 business days typically. <strong>This is the standard channel for foreign founders.</strong></p>"
         "<p><strong>3. Phone.</strong> Call <code>+1-267-941-1099</code> (not toll-free from India). Monday-Friday, 06:00-23:00 ET (that's 15:30-08:30 IST). IRS agent asks the SS-4 questions on the call and issues the EIN before you hang up. Expect a 20-40 min wait to get through. Faster than fax when you can get through.</p>"
         "<p><strong>4. Mail.</strong> Last resort &mdash; 6-8 weeks. Only use if fax and phone both fail.</p>"),
        ("/ Form SS-4 &mdash; Line 7b is the trap", "What to write when you have no SSN.",
         "<p>Most foreign founders get Form SS-4 right except Line 7b. The field asks for \"SSN, ITIN, or EIN\" of the Responsible Party (that's you, the founder). You have none of those.</p>"
         "<p><strong>Do NOT leave Line 7b blank.</strong> The IRS will reject the application.</p>"
         "<p><strong>Do NOT invent a number.</strong> That's fraud and the application will come back rejected or worse.</p>"
         "<p><strong>Write exactly:</strong> <code>Foreign / Non-US Applicant</code></p>"
         "<p>This specific wording is recognised by the IRS International EIN unit and processed cleanly. Every bank that later asks to see your CP 575 EIN letter also recognises this.</p>"),
        ("/ Timeline", "What actually happens, when.",
         "<p><strong>Day 0:</strong> Form your entity (Delaware C-Corp, Wyoming LLC, etc.). You need the Certificate of Incorporation or Articles of Organization first &mdash; the IRS asks for the entity to exist before issuing the EIN.</p>"
         "<p><strong>Day 1:</strong> Prepare Form SS-4 with Line 7b correctly worded, sign it, fax to +1-855-215-1627. Save the fax confirmation.</p>"
         "<p><strong>Day 4-11:</strong> IRS faxes back the EIN assignment. Save this &mdash; it's your proof until the CP 575 letter arrives.</p>"
         "<p><strong>Day 14-28:</strong> IRS mails the CP 575 letter (physical) to the address on your SS-4. For foreign founders using a Delaware/Wyoming registered agent, this arrives at the agent's address and gets forwarded to you. Verify arrival with your agent.</p>"
         "<p><strong>Day 15+:</strong> With the EIN in hand, open your US business bank account (Mercury, Brex, Relay). Start Stripe setup. The EIN unlocks everything.</p>"),
    ],
    faqs=[
        ("Can I use my passport number instead of SSN?",
         "No. The IRS does not accept passport numbers in Line 7b. The accepted wording for foreign founders without SSN or ITIN is exactly: Foreign / Non-US Applicant. This has been the standard since the IRS International EIN unit started processing SS-4s for non-US applicants."),
        ("How long does the fax method take?",
         "4 to 11 business days is typical. Some foreign founders have received the EIN by fax in 2-3 days. Factors that slow it down: fax queue load at IRS, errors on Form SS-4, missing supporting documents, Responsible Party identification concerns."),
        ("Do I need an ITIN before applying for the EIN?",
         "No. Do not waste 8-14 weeks applying for an ITIN just to use it on Form SS-4. The EIN is issued independently to foreign founders without an SSN or ITIN. The ITIN is only needed later if you personally receive certain types of US-source income that require a US tax return."),
        ("Can a third-party agent get the EIN for me?",
         "Yes, but it is not required. US-based agents (law firms, incorporation services) can submit the SS-4 on your behalf using Form 8821 (Tax Information Authorization) or Form 2848 (Power of Attorney). Expect to pay $150-$500 for this. If you do the fax yourself with correct wording, the result is identical."),
        ("What if the IRS fax number doesn't work from my country?",
         "Use an online fax service (eFax, HelloFax, etc.) or route through a US-based colleague. Any sending fax number works &mdash; the IRS replies to the fax number listed on your SS-4, so make sure the number you give is one you can receive at."),
        ("What is CP 575 and do I need the physical letter?",
         "CP 575 is the official IRS letter confirming your EIN assignment. The fax response is sufficient proof for most purposes but some US banks and payment processors insist on seeing CP 575. If lost or delayed, request a replacement 147C letter by calling +1-267-941-1099 and asking for an EIN verification letter."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (overview)"),
        ("delaware-franchise-tax-calculator.html", "Tool", "Delaware Franchise Tax Calculator"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Need the EIN handled end-to-end?",
    cta_body="Our standard US incorporation mandate includes the EIN application via the IRS International channel with the Line 7b wording done right. Average turnaround from engagement to EIN in hand: 7-10 business days. Then your bank account, Stripe, FEMA / ODI, and ongoing compliance.",
    howto={
        "name": "How to get an EIN without an SSN for a US LLC or C-Corp",
        "description": "Step-by-step process for foreign founders to obtain an IRS Employer Identification Number without a US Social Security Number or ITIN.",
        "steps": [
            {"name": "Form your US entity first", "text": "File Certificate of Incorporation (C-Corp) or Articles of Organization (LLC) with the state. The EIN cannot be issued before the entity legally exists."},
            {"name": "Prepare Form SS-4", "text": "Download Form SS-4 from irs.gov. Fill it in with your entity name, address, Responsible Party details, and nature of business. On Line 7b, write exactly: Foreign / Non-US Applicant."},
            {"name": "Fax SS-4 to IRS International", "text": "Fax the signed Form SS-4 to +1-855-215-1627. Include a cover sheet with your return fax number. Save the sender confirmation page."},
            {"name": "Wait 4-11 business days", "text": "The IRS International EIN unit will fax back the EIN assignment. If no response in 10 business days, call +1-267-941-1099 to follow up."},
            {"name": "Receive CP 575 by mail", "text": "The IRS mails the official CP 575 letter to the address on your SS-4 within 2-4 weeks. Keep this document permanently as your proof of EIN."},
            {"name": "Open US bank account", "text": "With the EIN confirmation in hand, apply at Mercury, Brex, or Relay. Approval typically 1-3 weeks after application with EIN and formation documents."},
        ]
    }
))

# 2. stripe-atlas-alternative-india
write_page("stripe-atlas-alternative-india", page(
    slug="stripe-atlas-alternative-india",
    title="Stripe Atlas Alternative for Indian Founders (2026) | CA-Led - BQP",
    description="Comparing Stripe Atlas against CA-led US incorporation for Indian founders. What Atlas doesn't do (FEMA ODI, 83(b), 5472, flip support), what you actually need, and when the cost difference pays for itself in 90 days.",
    keywords="stripe atlas alternative, stripe atlas india, stripe atlas vs CA firm, stripe atlas FEMA, stripe atlas ODI, doola alternative, firstbase alternative, best US incorporation service for Indian founders",
    hero_kicker="/ Comparison &middot; US incorporation",
    hero_title_html="A Stripe Atlas alternative <em>that handles the Indian side.</em>",
    hero_lead="Stripe Atlas, Doola, and Firstbase form your Delaware or Wyoming entity for $500-$1,000 and stop there. For Indian founders that leaves FEMA ODI, 83(b), transfer pricing, Form 5472, and the fundraise diligence pack hanging. Here's what a CA-led mandate covers &mdash; and when it pays for itself.",
    sections=[
        ("/ What Atlas does", "The US-side paperwork, and well.",
         "<p>Stripe Atlas, Doola and Firstbase are legitimate services. They file your Delaware or Wyoming entity, get the EIN, draft basic bylaws or operating agreement, and introduce you to Mercury for banking. For roughly USD 500 total, they handle the US-side mechanics in 2-4 weeks.</p>"
         "<p>If you are a solo bootstrapped founder with no Indian corporate entity putting capital in, no planned fundraise, and no intent to flip anything &mdash; Atlas is defensible. The service does what it says.</p>"),
        ("/ What Atlas does not do", "The Indian side &mdash; and that's where founders get stuck.",
         "<p>Atlas has no visibility into the Indian side of your structure. It does not handle:</p>"
         "<ul>"
         "<li><strong>FEMA ODI filing</strong> &mdash; required within 30 days of your Indian company sending capital to the US entity. Non-filing is a FEMA violation that compounds at every fundraise diligence.</li>"
         "<li><strong>Annual Performance Report</strong> to RBI (every year the US entity is held by an Indian company).</li>"
         "<li><strong>Transfer pricing documentation</strong> and Form 3CEB &mdash; required if your Indian co. and US co. have any intercompany transactions.</li>"
         "<li><strong>83(b) election filing</strong> for founder stock. Atlas often forgets. Missing the 30-day window costs founders five- and six-figure tax bills at exit.</li>"
         "<li><strong>Form 5472</strong> &mdash; US LLC owned by a foreign person must file this annually with a pro-forma Form 1120. USD 25,000 penalty for missed filings.</li>"
         "<li><strong>Delaware franchise tax election</strong> &mdash; Atlas doesn't advise on Authorized Shares vs Assumed Par Value Method, so most startups default to the Authorized Shares method and get hit with ~$85,000 bills.</li>"
         "<li><strong>Flip structuring</strong> &mdash; if you have an existing Indian company and need to flip it to a Delaware parent for US VC, Atlas does not touch this.</li>"
         "<li><strong>Fundraise diligence pack</strong> &mdash; what investors ask for during due diligence on your Indian/US combined structure.</li>"
         "</ul>"),
        ("/ The 90-day pay-back", "When CA-led saves money, not costs it.",
         "<p>Atlas: USD 500 upfront. Clean on day 1. Gap grows every month after.</p>"
         "<p>CA-led mandate: INR 65,000-140,000 (USD 800-1,700) upfront depending on package. Covers both sides end-to-end.</p>"
         "<p>Realistic 12-month cost comparison for a seed-stage Indian founder going US:</p>"
         "<ul>"
         "<li><strong>Atlas path:</strong> $500 formation + eventual $800 to fix FEMA ODI retroactively + $500 to file missed 83(b) if it's even possible + $2,000-$5,000 to prepare the fundraise diligence pack from scratch + $84,000 overcharge on Delaware franchise if you file the wrong method one year. Realistic 12-month total if things go wrong: USD 3,000-10,000+. Best case if nothing goes wrong: USD 500.</li>"
         "<li><strong>CA-led path:</strong> INR 1.4L (~USD 1,700) all-in Year 1. Everything handled. Diligence-ready from day 1.</li>"
         "</ul>"
         "<p>The break-even is pretty obvious once FEMA ODI is on the table. If your Indian company is funding the US entity, CA-led wins. If not, Atlas is fine.</p>"),
        ("/ Decision matrix", "Use this.",
         "<p><strong>Use Stripe Atlas / Doola / Firstbase if:</strong> you are a solo founder, no Indian corporate entity putting capital in, no fundraise planned in next 18 months, happy to self-manage ongoing US compliance (franchise tax, Form 1120 or Form 5472, BOI reporting). Budget: USD 500 upfront + USD 1,000-2,000/year ongoing compliance you handle yourself.</p>"
         "<p><strong>Use a CA-led mandate if:</strong> you have an Indian company putting capital into the US entity, OR you plan to raise from US VCs in the next 12 months, OR you want to flip an existing Indian startup to Delaware, OR you want someone who takes responsibility for both sides of the cross-border structure. Budget: INR 65,000-350,000 upfront depending on scope, INR 50,000-150,000/year ongoing.</p>"
         "<p><strong>Use nothing (yet):</strong> if you don't yet know whether you need a US entity. We'll do a 20-minute call for free and tell you honestly.</p>"),
    ],
    faqs=[
        ("Is BQP cheaper than Stripe Atlas?",
         "No &mdash; and that's not the comparison. Atlas is USD 500. Our Wyoming LLC package starts at INR 65k (~USD 800). We cost more because we do more: FEMA ODI, 83(b), Form 5472, transfer pricing, Delaware franchise tax strategy, flip support if needed. For a pure solo US-only setup where none of that applies, Atlas is cheaper. For an Indian founder with any India-US intercompany structure, we are the cheaper total over 12-24 months because we prevent the retroactive clean-up costs."),
        ("Can I start with Atlas and switch to BQP later?",
         "Yes, this is common. Many founders start with Atlas for the formation then engage us when they realise FEMA ODI, Form 5472, or 83(b) need handling. We take over the compliance side and leave the Atlas-formed entity in place. Expect a USD 300-500 one-time take-over fee to audit the existing setup and plug gaps."),
        ("Does Atlas help with Mercury banking?",
         "Yes, Atlas has a direct Mercury integration. Mercury treats Atlas-formed entities as pre-vetted, which speeds up account opening by about 1 week. BQP also works directly with Mercury for client introductions &mdash; approval timeline is similar. Mercury has approved both Atlas-formed and BQP-formed entities consistently since 2022."),
        ("What about Firstbase and Doola?",
         "Similar product category to Atlas. Firstbase skews slightly US-based founder focused; Doola is explicitly international. All three handle US-side formation well, all three stop at the US border. Same analysis applies: fine for solo US-only setups, insufficient for cross-border structures involving an Indian company."),
        ("Does Atlas handle 83(b) filings?",
         "Atlas provides a template 83(b) and reminds you to file within 30 days. The founder has to actually print, sign, mail by certified mail, and keep proof of mailing. Atlas does not do the physical filing. Many founders miss this. Our mandate includes handling the physical filing and keeping the proof-of-mailing permanently in your records."),
        ("What is the Delaware franchise tax trap?",
         "Delaware mails a first-year franchise tax bill calculated using the Authorized Shares Method, which charges ~$85,000 for the standard 10M-share VC template. You can elect the Assumed Par Value Method on the annual report and reduce this to ~$450 for a pre-revenue startup. Atlas does not explain this; many Atlas customers pay the $85k. We cover this in our ongoing compliance package. See our full Delaware franchise tax calculator at bharatquantumprospera.com/delaware-franchise-tax-calculator.html."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (overview)"),
        ("delaware-franchise-tax-calculator.html", "Tool", "Delaware Franchise Tax Calculator"),
        ("how-to-get-ein-without-ssn.html", "Guide", "EIN without SSN"),
    ],
    cta_headline="Comparing Atlas and considering CA-led?",
    cta_body="A 20-minute scoping call confirms whether Atlas is enough for your case or whether you'll end up paying us retroactively anyway. If Atlas fits, we'll tell you. If CA-led wins the 12-month math for your structure, we'll quote firm.",
))

# 3. india-us-dtaa-withholding-rates
write_page("india-us-dtaa-withholding-rates", page(
    slug="india-us-dtaa-withholding-rates",
    title="India-US DTAA Withholding Rates (2026) | Dividends, Royalties, FTS - BQP",
    description="Complete India-US Double Taxation Avoidance Agreement withholding rates for 2026. Dividends 15% / 25%, royalties & FTS 15% / 10%, interest 10% / 15%. Form 10F, TRC, when the lower rate applies, Section 90(2) override.",
    keywords="India US DTAA, India US tax treaty, DTAA withholding rate, Form 10F, TRC India US, DTAA dividend rate, royalty withholding India US, FTS withholding India US, double taxation India US",
    hero_kicker="/ Cross-border tax &middot; India-US DTAA",
    hero_title_html="India-US DTAA, <em>withholding rates &amp; mechanics.</em>",
    hero_lead="Every Indian company receiving US-source payments, and every US company paying Indian residents, needs to understand which article of the India-US tax treaty applies to the flow and at what rate. This page lists every withholding category, the treaty article, and the mechanical steps to claim the treaty rate.",
    sections=[
        ("/ The headline rates", "What the India-US DTAA caps.",
         "<p>The India-US Double Taxation Avoidance Agreement (signed 1989, in force 1990, protocols 1991 and 1999) sets maximum withholding tax rates that override higher domestic rates. Current treaty-capped rates:</p>"
         "<ul>"
         "<li><strong>Dividends (Article 10):</strong> 15% (default); 25% applies in older cases but 15% is the general cap. For dividends from a US corporation to a 10%+ Indian corporate shareholder, 15% is the floor.</li>"
         "<li><strong>Interest (Article 11):</strong> 10% for financial institutions; 15% for other interest.</li>"
         "<li><strong>Royalties and Fees for Included Services (Article 12):</strong> 10% for industrial equipment royalties; 15% for other royalties and most Fees for Included Services (FIS). Note India and US use different terminology &mdash; India calls it FTS (Fees for Technical Services), the treaty calls it FIS.</li>"
         "<li><strong>Business profits (Article 7):</strong> taxable only in the residence country unless there is a Permanent Establishment in the source country. If US customer pays Indian company for services with no US PE, no US withholding at all.</li>"
         "<li><strong>Capital gains on shares (Article 13):</strong> taxable in the country of residence of the seller, with specific carve-outs.</li>"
         "</ul>"),
        ("/ Who gets which rate", "Reading the article is the whole game.",
         "<p>Characterisation determines rate. The same money flow can be royalty (Article 12, 15% cap) or business profits (Article 7, no US withholding if no US PE). Which one applies depends on the facts and the contract.</p>"
         "<p>Common misclassification: SaaS subscription payments from US customer to Indian company. If the Indian company provides pure SaaS (customer uses the service, no transfer of software or IP), it is business profits under Article 7 &mdash; no US withholding. If the contract transfers software source code, that is a royalty under Article 12 &mdash; 15% US withholding applies.</p>"
         "<p>Another common one: cloud hosting fees from US customer to Indian company. US position has swung. Current conservative read: business profits (Article 7) if the Indian company has no US PE. Aggressive IRS positions have argued royalty treatment on specific facts.</p>"),
        ("/ Mechanics &mdash; how to actually claim the lower rate", "Form 10F, TRC, Form W-8BEN-E.",
         "<p>To get the US payer to withhold at the treaty rate (instead of the default 30% US domestic rate on most cross-border payments), the Indian recipient must give the US payer:</p>"
         "<ol>"
         "<li><strong>Form W-8BEN-E</strong> (for entities; W-8BEN for individuals). This is a US IRS form the Indian recipient signs certifying their foreign status and treaty eligibility. Must be renewed every 3 years or when circumstances change.</li>"
         "<li><strong>Indian Tax Residency Certificate (TRC)</strong> from the Indian tax authority (CBDT), issued per Section 90(4) of the Indian Income-tax Act. Request through your jurisdictional Assessing Officer. Validity 1 year.</li>"
         "<li><strong>Form 10F</strong> &mdash; an Indian prescribed form self-certifying additional information required to claim treaty benefits. From April 2023, must be filed electronically on the Indian income tax portal. Mandatory for non-resident claims.</li>"
         "</ol>"
         "<p>Without all three documents, the US payer must withhold at the full 30% default. Many Indian service providers lose 15 percentage points of their US revenue by not providing the documents to the US customer at onboarding.</p>"),
        ("/ Section 90(2) override", "The India-side protection.",
         "<p>Section 90(2) of the Indian Income-tax Act 1961 says: where there is a DTAA, the taxpayer is entitled to the more beneficial of the DTAA rate or the Indian domestic rate. The treaty cannot be used to increase tax; only to reduce.</p>"
         "<p>Example: a Mauritius-India DTAA situation where domestic Indian law would tax at 20% but the DTAA caps at 10%, the taxpayer gets 10%. Conversely, if domestic Indian law allows a 5% rate and the DTAA says 10%, the taxpayer gets 5%.</p>"
         "<p>For India-US flows, Section 90(2) matters when claiming foreign tax credit on US tax paid against Indian tax liability. The credit is capped at the lower of (a) US tax actually paid and (b) Indian tax that would have been payable on the same income.</p>"),
    ],
    faqs=[
        ("What is the dividend withholding rate under the India-US DTAA?",
         "15% is the general cap. The treaty's older 25% rate applies only in limited circumstances. For a US C-Corp paying dividends to its Indian parent company, the rate is 15% provided all treaty-claim documents (Form W-8BEN-E, TRC, Form 10F) are in place with the US payer."),
        ("What is Form 10F and when is it required?",
         "Form 10F is a self-certification prescribed under Indian Rule 21AB used by non-residents to claim DTAA treaty benefits in India. From April 2023, it must be filed electronically on the Indian income tax portal (incometax.gov.in) by any non-resident claiming DTAA relief. Without it, treaty benefits are typically denied on an audit."),
        ("Do I need Form 10F for US-source income received by an Indian company?",
         "Form 10F is required when the Indian company is claiming DTAA benefits on income taxable in India. For US-source income taxed in the US at a treaty rate, the Indian company gives the US payer Form W-8BEN-E (not Form 10F) with a Tax Residency Certificate from India. Form 10F applies on the Indian side &mdash; e.g., for an Indian payer paying a US entity treaty-rate royalty."),
        ("Can an Indian startup selling SaaS to US customers avoid US withholding entirely?",
         "If the Indian company provides pure SaaS from India with no US Permanent Establishment and the SaaS is characterised as business profits under Article 7, no US withholding applies. The US customer should be given a Form W-8BEN-E claiming Article 7 and a TRC. The key is the contract wording &mdash; it must not transfer software or IP ownership (which would make it a royalty under Article 12 at 15%)."),
        ("What is a Permanent Establishment and does my Indian company have one in the US?",
         "A Permanent Establishment (PE) under Article 5 of the India-US DTAA is a fixed place of business in the US &mdash; a leased office, a warehouse, employees physically working there. A US customer, a US bank account, or occasional business travel does not create a PE. If you have US employees or a US office, you likely have a PE and the Article 7 business-profits exemption is lost on activity attributable to that PE."),
        ("How do I get an Indian Tax Residency Certificate?",
         "Apply through your jurisdictional Assessing Officer with Form 10FA and supporting documents (PAN card, proof of Indian residence, bank statements). Issued per Section 90(4) and Rule 21AB. Typical processing is 15-30 days. Valid for 1 financial year. Must be renewed annually to maintain DTAA eligibility for cross-border payments."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (overview)"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
        ("stripe-atlas-alternative-india.html", "Compare", "Stripe Atlas vs CA-led"),
    ],
    cta_headline="India-US cross-border flows that need a treaty claim?",
    cta_body="If you are an Indian company receiving US royalties, FIS, dividends or interest &mdash; or paying any of these to a US party &mdash; getting the treaty rate requires specific documents filed before the first payment. We handle the full Form W-8BEN-E, TRC and Form 10F process and defend the treaty position if challenged.",
))

# 4. fema-odi-us-entity-indian-founder
write_page("fema-odi-us-entity-indian-founder", page(
    slug="fema-odi-us-entity-indian-founder",
    title="FEMA ODI for US Entity (2026) | Indian Founder Compliance Guide - BQP",
    description="Complete guide to FEMA Overseas Direct Investment compliance for Indian founders funding US LLCs or C-Corps. Form ODI, 30-day deadline, Annual Performance Report, LRS vs ODI route, penalty for non-compliance.",
    keywords="FEMA ODI US, Form ODI India, Overseas Direct Investment US entity, LRS vs ODI, Indian founder US LLC FEMA, Annual Performance Report APR, FEMA violation penalty, OPI vs ODI",
    hero_kicker="/ FEMA &middot; India-side compliance",
    hero_title_html="FEMA ODI for your US entity. <em>The one filing Atlas can't do.</em>",
    hero_lead="If you are an Indian resident sending capital to a US LLC or C-Corp you own, FEMA kicks in. The Overseas Direct Investment (ODI) framework governs how, how much, and under what reporting. Here is what you file, when, and what happens if you don't.",
    sections=[
        ("/ What triggers ODI", "When FEMA cares about your US entity.",
         "<p>FEMA Overseas Direct Investment rules apply when:</p>"
         "<ul>"
         "<li>An <strong>Indian individual resident</strong> or <strong>Indian company (Indian Party)</strong> invests capital into a foreign entity, AND</li>"
         "<li>The investment gives the Indian party a stake in the foreign entity's capital (equity, convertible instruments, loans with equity-like characteristics).</li>"
         "</ul>"
         "<p>So if you (Indian resident) wire USD from your Indian bank account to your Wyoming LLC's Mercury account as a founder capital contribution &mdash; ODI applies. If your Indian Pvt Ltd invests in a Delaware C-Corp subsidiary &mdash; ODI applies.</p>"
         "<p>If you fund the US entity entirely from USD you earned outside India (held in a US bank account you own as a non-resident, or held abroad under LRS limits already used) &mdash; FEMA may not apply directly. Facts-specific; needs a review.</p>"),
        ("/ Form ODI &mdash; the 30-day deadline", "File through your AD bank, not with RBI directly.",
         "<p>Within 30 days of the first remittance to the US entity, you must file Form ODI through your Authorised Dealer (AD) Category-I bank &mdash; your Indian bank handling the outbound forex. The AD bank forwards the submission to RBI.</p>"
         "<p>Form ODI collects: Indian Party details (your Indian company or your personal residency status), foreign entity details (US entity name, address, EIN, nature of business), investment amount, structure (equity, loan, convertible), source of funds (Indian company retained earnings, LRS, external commercial borrowings), and intended use.</p>"
         "<p>Standard automatic route applies for most structures:</p>"
         "<ul>"
         "<li>Indian company investments up to 400% of net worth (sum of paid-up capital and free reserves) under automatic route.</li>"
         "<li>Indian individuals using LRS: USD 250,000/year/person combined for all current and capital account transactions including ODI.</li>"
         "<li>Investments above these limits need prior RBI approval through the approval route.</li>"
         "</ul>"),
        ("/ Annual Performance Report (APR)", "Every year, forever (or until you divest).",
         "<p>After the initial Form ODI filing, you must submit the APR to RBI through your AD bank by June 30 each year, covering the previous Indian financial year (April to March).</p>"
         "<p>APR reports: foreign entity's audited financial statements, business update, investment valuation, any changes in capital structure, any additional investments made during the year. The APR is NOT optional and NOT dependent on whether the foreign entity made any transactions &mdash; even a dormant US entity needs an APR each year.</p>"
         "<p>Common failure: founders file Form ODI at inception, launch the US entity, then forget about APR. First APR deadline passes. Second APR deadline passes. By the third year the back-reporting plus late-filing penalties start adding up materially.</p>"),
        ("/ Penalties and clean-up", "What the FEMA regulator actually does.",
         "<p>Non-filing of Form ODI: compoundable offence under FEMA. Compounding fee typically ranges from 1% of the investment per year of non-filing to significantly higher for repeat defaults, with caps.</p>"
         "<p>Non-filing of APR: separately compoundable, around INR 5,000 to INR 50,000 per missed APR depending on duration and amount.</p>"
         "<p>More painful than the regulator: fundraise diligence. Every VC and every acquirer in India will have their lawyers audit your FEMA compliance. Discovering back-missed Form ODI or APRs during diligence delays the round by 2-4 months while you compound and clean up. Costs: INR 1-3 lakh for a mid-sized back-clean-up plus the time cost of a stalled fundraise.</p>"),
    ],
    faqs=[
        ("Can I use LRS to fund my US LLC?",
         "Yes, as an Indian individual resident. LRS allows USD 250,000 per person per financial year for permitted current and capital account transactions, including investment in overseas entities. The LRS remittance is reported through your AD bank; a Form A2 is filed. If you also need Form ODI depends on whether your stake in the US entity constitutes a reportable overseas direct investment &mdash; typically yes for founder equity."),
        ("What is the difference between ODI and OPI?",
         "ODI (Overseas Direct Investment) applies to stakes giving control, participation in management, or substantial equity holding in a foreign operating entity. OPI (Overseas Portfolio Investment) applies to minority holdings in listed foreign securities (shares, bonds, ETFs). For a founder forming their own US LLC or C-Corp, ODI is the applicable regime because the founder controls the entity."),
        ("Can I bypass FEMA ODI by funding the US LLC from US revenue?",
         "If the US LLC generates US-source revenue in its own US bank account and uses that revenue to fund operations, FEMA ODI does not apply to that specific flow (no Indian funds crossed the border). FEMA ODI applies at the moment of outbound remittance from India. If no outbound Indian remittance happens, there is no ODI event. However, the initial capital to open the US bank and get operational typically needs some Indian funding &mdash; and that triggers ODI."),
        ("What is the Annual Performance Report deadline?",
         "APR for the previous Indian financial year (ending March 31) is due to RBI through your AD bank by June 30 each year. Example: for FY2025-26 (ending 31 March 2026), the APR is due by 30 June 2026. Delays are compoundable per missed year."),
        ("Does FEMA apply if I'm an NRI founder?",
         "FEMA ODI applies to Indian residents under the Foreign Exchange Management Act. If you are a Non-Resident Indian (NRI) under FEMA, you are not an Indian resident for FEMA purposes and ODI does not apply to your outbound investment into a US entity (because the capital is not crossing India's border from an Indian resident's hands). However, Indian income tax residency can still apply even for NRIs on certain income &mdash; separate analysis."),
        ("Can BQP file the Form ODI and APR for me?",
         "Yes &mdash; it is a standard inclusion in our US incorporation mandate for Indian clients. We handle the initial Form ODI filing within the 30-day window, prepare the APR each year, and liaise with your AD bank. If you did your US formation elsewhere (Stripe Atlas, Doola) and need just the FEMA side handled, we take on compliance-only engagements starting at INR 25,000 per year."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation (overview)"),
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("stripe-atlas-alternative-india.html", "Compare", "Stripe Atlas vs CA-led"),
    ],
    cta_headline="Funded a US entity from India &mdash; and skipped Form ODI?",
    cta_body="If your initial Form ODI was missed or your APRs are overdue, the clean-up is straightforward but time-sensitive before your next fundraise. We assess the back-exposure, prepare the compounding application, file the overdue APRs, and get you to clean FEMA status within 60-90 days.",
))

print("v2 pages built")
