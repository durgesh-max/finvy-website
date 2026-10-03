# -*- coding: utf-8 -*-
"""Submit all URLs (existing + 20 new) to IndexNow.
   Run AFTER PR #1 is merged and GitHub Pages has deployed (~60-90s after merge)."""
import json, urllib.request, urllib.error

DOMAIN = "https://bharatquantumprospera.com"
KEY = "a4c7f9e2b1d5c8a3f6e9b2d47a1c5e8f"

URLS = [
    f"{DOMAIN}/",
    f"{DOMAIN}/sitemap.xml",
    f"{DOMAIN}/llms.txt",
    f"{DOMAIN}/robots.txt",
    # Existing service pages (lastmod refreshed)
    f"{DOMAIN}/us-incorporation.html",
    f"{DOMAIN}/sme-ipo.html",
    f"{DOMAIN}/capital-advisory.html",
    f"{DOMAIN}/fund-raising.html",
    f"{DOMAIN}/ma-transactions.html",
    f"{DOMAIN}/gift-city.html",
    f"{DOMAIN}/global-taxation.html",
    f"{DOMAIN}/esop-compensation.html",
    f"{DOMAIN}/fund-structuring.html",
    f"{DOMAIN}/corporate-legal.html",
    f"{DOMAIN}/international-expansion.html",
    f"{DOMAIN}/founder.html",
    # 20 new insights pages
    f"{DOMAIN}/india-us-tax-treaty-dtaa.html",
    f"{DOMAIN}/india-uae-tax-treaty-dtaa.html",
    f"{DOMAIN}/india-singapore-tax-treaty-dtaa.html",
    f"{DOMAIN}/india-uk-tax-treaty-dtaa.html",
    f"{DOMAIN}/india-mauritius-tax-treaty-dtaa.html",
    f"{DOMAIN}/stripe-atlas-vs-firstbase.html",
    f"{DOMAIN}/stripe-atlas-vs-doola.html",
    f"{DOMAIN}/c-corp-vs-s-corp.html",
    f"{DOMAIN}/mercury-vs-brex.html",
    f"{DOMAIN}/safe-vs-convertible-note.html",
    f"{DOMAIN}/esop-vs-rsu-vs-phantom-stock.html",
    f"{DOMAIN}/delaware-c-corp-vs-llc.html",
    f"{DOMAIN}/how-to-get-ein-as-foreign-founder.html",
    f"{DOMAIN}/how-to-file-fbar-from-india.html",
    f"{DOMAIN}/how-to-flip-indian-company-to-us.html",
    f"{DOMAIN}/how-to-file-form-5472.html",
    f"{DOMAIN}/how-to-file-boir-cta.html",
    f"{DOMAIN}/what-is-fatca.html",
    f"{DOMAIN}/what-is-pfic.html",
    f"{DOMAIN}/what-is-form-w-8ben.html",
]

payload = {
    "host": "bharatquantumprospera.com",
    "key": KEY,
    "keyLocation": f"{DOMAIN}/{KEY}.txt",
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
except urllib.error.HTTPError as e:
    print(f"IndexNow HTTPError: {e.code} - {e.read().decode()[:400]}")
except Exception as e:
    print(f"IndexNow error: {type(e).__name__} - {e}")
