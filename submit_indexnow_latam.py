# -*- coding: utf-8 -*-
"""Submit LatAm push URLs to IndexNow (run after merge)."""
import json, urllib.request
URLS = ['https://bharatquantumprospera.com/latin-america.html', 'https://bharatquantumprospera.com/us-incorporation-for-brazilian-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-mexican-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-argentine-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-chilean-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-colombian-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-peruvian-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-uruguayan-founders.html', 'https://bharatquantumprospera.com/us-incorporation-for-costa-rican-founders.html', 'https://bharatquantumprospera.com/india-brazil-tax-treaty-dtaa.html', 'https://bharatquantumprospera.com/india-mexico-tax-treaty-dtaa.html', 'https://bharatquantumprospera.com/india-chile-tax-treaty-dtaa.html', 'https://bharatquantumprospera.com/india-colombia-tax-treaty-dtaa.html', 'https://bharatquantumprospera.com/india-latin-america-expansion-guide.html', 'https://bharatquantumprospera.com/es/incorporacion-delaware-fundadores-latinoamericanos.html', 'https://bharatquantumprospera.com/es/incorporacion-wyoming-llc.html', 'https://bharatquantumprospera.com/es/ein-sin-ssn.html', 'https://bharatquantumprospera.com/es/mercury-vs-brex.html', 'https://bharatquantumprospera.com/es/formulario-w-8ben.html', 'https://bharatquantumprospera.com/es/formulario-5472.html', 'https://bharatquantumprospera.com/pt/incorporacao-delaware-fundadores-brasileiros.html', 'https://bharatquantumprospera.com/pt/incorporacao-wyoming-llc.html', 'https://bharatquantumprospera.com/pt/ein-sem-ssn.html', 'https://bharatquantumprospera.com/pt/formulario-5472.html', 'https://bharatquantumprospera.com/sitemap.xml', 'https://bharatquantumprospera.com/llms.txt']
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
