# -*- coding: utf-8 -*-
"""All guides by topic (HTML sitemap and topic map). Technical audit 23 Nov 2026 found 91 sitemap pages with no internal
link from any other page; this page links every indexable page, grouped by topic, and is linked from every footer.
Rebuild after adding pages: python build_all_guides.py (reads sitemap.xml and page titles)."""
import glob, html, json, os, re
from build_lib import page, write_page, DOMAIN

SLUG = "all-guides"
sm = open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>https://bharatquantumprospera\.com/([^<]*)</loc>", sm)
SKIP = {"", "index.html", SLUG + ".html", "privacy.html", "get-a-quote.html", "book-a-call.html", "contact.html"}

GROUPS = [
    ("tools", "Calculators and tools", r"calculator|checker|chooser|-tool"),
    ("fastds", "FAST-DS 2026 and foreign assets", r"fast-ds|foreign-asset|schedule-fa|black-money|income-tax-email-foreign"),
    ("city", "By city", r"^best-ca-firm-|^ca-in-|^ca-for-[a-z-]*-(mumbai|bangalore|bengaluru|delhi|pune|hyderabad|chennai|ahmedabad|surat|rajkot|jaipur|kolkata)"),
    ("industry", "By industry", r"^best-ca-"),
    ("foreign", "Foreign companies in India: entry, FEMA, tax and compliance", r"foreign|fdi|fema|subsidiary|liaison|branch|wos|press-note|pe-risk|permanent-establishment|equalisation|significant-economic|master-file|transfer-pricing|3ceb|gcc|employer-of-record|india-entry|doing-business|market-entry|fc-gpr|fc-trs|fla-return|odi|ecb|downstream|international-worker|pf-for-foreign|expat|due-diligence|acquire|joint-venture|indirect-transfer|tds-on-purchase-of-shares|no-pe|15ca|15cb|form-145|section-195|dtaa|tax-treaty|withholding"),
    ("nri", "NRIs: tax, money, property and returning to India", r"nri|oci|nre|nro|non-resident|green-card|h1b|returning|inherit|repatriat|send-money|remittance|lrs|tcs|moving-abroad|pensioner|gift|property|residential-status|rnor|uae|dubai"),
    ("startup", "Startups and founders: setup, tax, ESOPs and fundraising", r"startup|founder|esop|sweat-equity|dpiit|80-iac|section-140|angel|seed|fund|vc-|safe|convertible|valuation|llp|private-limited|pvt-ltd|ipo|cap-table|409a|flip|us-incorporation|delaware|c-corp|llc|incorporation"),
    ("gst", "GST", r"gst|gstr|oidar|lut|e-invoice"),
    ("tax", "Income tax, deadlines and returns", r"itr|income-tax|advance-tax|tds|tax-audit|belated|revised|refund|deadline|due-date|calendar|budget|regime|87a|capital-gains|ltcg|form-|section-|notice|tax"),
    ("company", "Company law, ROC and corporate compliance", r"roc|mca|aoc-4|mgt-7|dir-3|din|llp-form|pas-|dpt-3|msme|company-secretarial|strike-off|close-company|companies-act|csr"),
]

def title_of(f):
    try:
        s = open(f, encoding="utf-8", errors="ignore").read()
    except FileNotFoundError:
        return None
    if re.search(r'<meta name="robots" content="[^"]*noindex', s):
        return None
    m = re.search(r"<title>(.*?)</title>", s, re.S)
    t = html.unescape(m.group(1).strip()) if m else f
    t = re.sub(r"\s*[|\-]\s*(BQP|Bharat Quantum Prospera)\s*$", "", t)
    if len(t) > 110:
        cut = t[:110]
        t = cut[:cut.rfind(" ")] + "..."
    return t

buckets = {k: [] for k, _, _ in GROUPS}
buckets["other"] = []
for f in locs:
    if f in SKIP or "/" in f or not f.endswith(".html") or not os.path.exists(f):
        continue
    t = title_of(f)
    if not t:
        continue
    for k, _, rx in GROUPS:
        if re.search(rx, f):
            buckets[k].append((t, f)); break
    else:
        buckets["other"].append((t, f))

names = dict((k, n) for k, n, _ in GROUPS); names["other"] = "Services, industries and the firm"
order = [k for k, _, _ in GROUPS] + ["other"]
total = sum(len(v) for v in buckets.values())
sections = []
nav = " &middot; ".join(f'<a href="#{k}">{names[k]} ({len(buckets[k])})</a>' for k in order if buckets[k])
sections.append(("/ Topics", "Jump to a topic.", f'<p>{nav}</p><p>Not sure where to start? <a href="https://topmate.io/cadurgesh_chavda/741484" target="_blank" rel="noopener">Book a call</a> or <a href="https://wa.me/917801887130" target="_blank" rel="noopener">WhatsApp CA Durgesh Chavda</a>.</p>'))
for k in order:
    items = sorted(buckets[k], key=lambda x: x[0].lower())
    if not items:
        continue
    lis = "".join(f'<li><a href="{f}">{html.escape(t)}</a></li>' for t, f in items)
    sections.append((f"/ {len(items)} pages", f'<span id="{k}"></span>{names[k]}.', f'<ul style="columns:2 320px;column-gap:28px">{lis}</ul>'))

html_out = page(
    slug=SLUG,
    title="All Guides by Topic: NRI Tax, FAST-DS, Foreign Companies in India, Startups, GST and Income Tax | Bharat Quantum Prospera",
    description=f"Every guide on bharatquantumprospera.com by topic: {total} pages on NRI tax and money, FAST-DS 2026, foreign companies in India, startups and founders, GST, income tax deadlines, company law, calculators, industries and cities. By CA Durgesh Chavda.",
    keywords="NRI tax guides, FAST-DS guides, foreign company India guides, startup tax India guides, CA Durgesh Chavda articles, Bharat Quantum Prospera insights",
    hero_kicker="/ Library &middot; All guides",
    hero_title_html="All guides by topic, <em>every page in one place.</em>",
    hero_lead=(f"<strong>{total} practitioner guides and tools by CA Durgesh Chavda and Bharat Quantum Prospera</strong>, grouped by topic: NRI tax and money, FAST-DS 2026, foreign companies doing business in India, startups and founders, GST, income tax and deadlines, company law, calculators, industries and cities. "
               "For a question about your own situation, book a call."),
    sections=sections,
    faqs=[("Who writes these guides?", "CA Durgesh Chavda, a Chartered Accountant (ICAI) in Ahmedabad and founder of Bharat Quantum Prospera, with sources and a last-updated date on each page."),
          ("How do I ask about my own case?", "Book a call at book-a-call.html, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com.")],
    related=[("insights.html", "Library", "Insights library"), ("tools.html", "Tools", "Calculators and tools"), ("book-a-call.html", "Call", "Book a call")],
    cta_headline="Didn't find your exact question?",
    cta_body="Book a call at book-a-call.html, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your country and question.",
)
write_page(SLUG, html_out)
print("all-guides.html:", total, "pages;", {k: len(v) for k, v in buckets.items()})
