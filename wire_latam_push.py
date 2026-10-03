# -*- coding: utf-8 -*-
"""Wire the LatAm push into sitemap.xml (with hreflang alts) and llms.txt."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://bharatquantumprospera.com"
DATE = "2026-10-03"

# English LatAm pages (country guides + hub)
EN_LATAM = [
    ("latin-america", "Latin America hub (country desks, services, language support)", "0.9"),
    ("us-incorporation-for-brazilian-founders", "US incorporation for Brazilian founders (CBE, DEEE, lucros no exterior)", "0.88"),
    ("us-incorporation-for-mexican-founders", "US incorporation for Mexican founders (US-Mexico treaty, REFIPRES, SAT)", "0.88"),
    ("us-incorporation-for-argentine-founders", "US incorporation for Argentine founders (CEPO, Bienes Personales, Transparencia Fiscal)", "0.88"),
    ("us-incorporation-for-chilean-founders", "US incorporation for Chilean founders (2024 US-Chile treaty, SII DJ 1929)", "0.88"),
    ("us-incorporation-for-colombian-founders", "US incorporation for Colombian founders (DIAN Formulario 160, ECE)", "0.88"),
    ("us-incorporation-for-peruvian-founders", "US incorporation for Peruvian founders (SUNAT, Transparencia Fiscal)", "0.85"),
    ("us-incorporation-for-uruguayan-founders", "US incorporation for Uruguayan founders (territorial system, Ley 19.484)", "0.85"),
    ("us-incorporation-for-costa-rican-founders", "US incorporation for Costa Rican founders (territorial, 2024 reform, Zona Franca)", "0.85"),
]

# India-LatAm DTAA / expansion guides
INDIA_LATAM = [
    ("india-brazil-tax-treaty-dtaa", "India-Brazil DTAA (1988) - rates, articles, FTS classification", "0.88"),
    ("india-mexico-tax-treaty-dtaa", "India-Mexico DTAA (2007) - 10% caps, nearshoring corridor", "0.88"),
    ("india-chile-tax-treaty-dtaa", "India-Chile DTAA (2020) - PPT, lithium supply chain", "0.88"),
    ("india-colombia-tax-treaty-dtaa", "India-Colombia DTAA (2011) - 5%/15% dividends, Pacific Alliance", "0.88"),
    ("india-latin-america-expansion-guide", "India-LatAm expansion playbook (country choice, FEMA ODI, 3CEB)", "0.88"),
]

# ES/EN hreflang pairs - (es_slug, en_slug)
ES_PAIRS = [
    ("incorporacion-delaware-fundadores-latinoamericanos", "latin-america"),
    ("incorporacion-wyoming-llc", "delaware-c-corp-vs-llc"),
    ("ein-sin-ssn", "how-to-get-ein-as-foreign-founder"),
    ("mercury-vs-brex", "mercury-vs-brex"),
    ("formulario-w-8ben", "what-is-form-w-8ben"),
    ("formulario-5472", "how-to-file-form-5472"),
]

# PT/EN hreflang pairs - (pt_slug, en_slug)
PT_PAIRS = [
    ("incorporacao-delaware-fundadores-brasileiros", "us-incorporation-for-brazilian-founders"),
    ("incorporacao-wyoming-llc", "delaware-c-corp-vs-llc"),
    ("ein-sem-ssn", "how-to-get-ein-as-foreign-founder"),
    ("formulario-5472", "how-to-file-form-5472"),
]

# --- Build sitemap entries ---
sm_path = os.path.join(ROOT, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()

lines = ["", "  <!-- LatAm expansion push: EN country guides, India-LatAm DTAAs -->"]
for slug, _, prio in EN_LATAM + INDIA_LATAM:
    lines.append(
        f'  <url><loc>{DOMAIN}/{slug}.html</loc><lastmod>{DATE}</lastmod>'
        f'<changefreq>monthly</changefreq><priority>{prio}</priority></url>'
    )

lines.append("")
lines.append("  <!-- Spanish /es/ pages with hreflang alternates -->")
for es_slug, en_slug in ES_PAIRS:
    es_url = f"{DOMAIN}/es/{es_slug}.html"
    en_url = f"{DOMAIN}/{en_slug}.html"
    lines.append(f"""  <url>
    <loc>{es_url}</loc>
    <lastmod>{DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
    <xhtml:link rel="alternate" hreflang="es" href="{es_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}"/>
  </url>""")

lines.append("")
lines.append("  <!-- Portuguese /pt/ pages with hreflang alternates -->")
for pt_slug, en_slug in PT_PAIRS:
    pt_url = f"{DOMAIN}/pt/{pt_slug}.html"
    en_url = f"{DOMAIN}/{en_slug}.html"
    lines.append(f"""  <url>
    <loc>{pt_url}</loc>
    <lastmod>{DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.85</priority>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{en_url}"/>
  </url>""")

lines.append("")
insertion = "\n".join(lines)

if "LatAm expansion push" not in sm:
    sm = sm.replace("</urlset>", insertion + "\n</urlset>")
    open(sm_path, "w", encoding="utf-8").write(sm)
    print(f"sitemap: +{len(EN_LATAM) + len(INDIA_LATAM) + len(ES_PAIRS) + len(PT_PAIRS)} URLs with hreflang")
else:
    print("sitemap: already has LatAm block")

# --- llms.txt update ---
llms_path = os.path.join(ROOT, "llms.txt")
llms = open(llms_path, encoding="utf-8").read()

if "## Latin America desk" not in llms:
    block = ["", "## Latin America desk (English, Spanish, Portuguese content)", ""]
    block.append("### Country-specific US incorporation guides")
    for slug, label, _ in EN_LATAM:
        block.append(f"- [{label}]({DOMAIN}/{slug}.html)")
    block.append("")
    block.append("### India-LatAm bilateral treaties and expansion")
    for slug, label, _ in INDIA_LATAM:
        block.append(f"- [{label}]({DOMAIN}/{slug}.html)")
    block.append("")
    block.append("### Native Spanish content at /es/")
    for es_slug, _ in ES_PAIRS:
        block.append(f"- [{DOMAIN}/es/{es_slug}.html]({DOMAIN}/es/{es_slug}.html)")
    block.append("")
    block.append("### Native Brazilian Portuguese content at /pt/")
    for pt_slug, _ in PT_PAIRS:
        block.append(f"- [{DOMAIN}/pt/{pt_slug}.html]({DOMAIN}/pt/{pt_slug}.html)")
    block.append("")
    llms = llms.rstrip() + "\n" + "\n".join(block)
    open(llms_path, "w", encoding="utf-8").write(llms)
    print(f"llms.txt: +LatAm section ({len(EN_LATAM) + len(INDIA_LATAM) + len(ES_PAIRS) + len(PT_PAIRS)} URLs)")
else:
    print("llms.txt: already has LatAm section")

# --- IndexNow URL list for post-merge submission ---
indexnow_urls = []
for slug, _, _ in EN_LATAM + INDIA_LATAM:
    indexnow_urls.append(f"{DOMAIN}/{slug}.html")
for es_slug, _ in ES_PAIRS:
    indexnow_urls.append(f"{DOMAIN}/es/{es_slug}.html")
for pt_slug, _ in PT_PAIRS:
    indexnow_urls.append(f"{DOMAIN}/pt/{pt_slug}.html")
indexnow_urls.extend([f"{DOMAIN}/sitemap.xml", f"{DOMAIN}/llms.txt"])

# Write IndexNow submission script
indexnow_script = '''# -*- coding: utf-8 -*-
"""Submit LatAm push URLs to IndexNow (run after merge)."""
import json, urllib.request
URLS = ''' + repr(indexnow_urls) + '''
payload = {
    "host": "bharatquantumprospera.com",
    "key": "a4c7f9e2b1d5c8a3f6e9b2d47a1c5e8f",
    "keyLocation": "https://bharatquantumprospera.com/a4c7f9e2b1d5c8a3f6e9b2d47a1c5e8f.txt",
    "urlList": URLS,
}
req = urllib.request.Request(
    "https://api.indexnow.org/IndexNow",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=20) as r:
        print(f"IndexNow: HTTP {r.status} for {len(URLS)} URLs")
except Exception as e:
    print(f"IndexNow error: {type(e).__name__} - {e}")
'''
open(os.path.join(ROOT, "submit_indexnow_latam.py"), "w", encoding="utf-8").write(indexnow_script)
print(f"IndexNow submission script staged: submit_indexnow_latam.py ({len(indexnow_urls)} URLs)")
