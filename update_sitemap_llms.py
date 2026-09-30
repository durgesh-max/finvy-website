# -*- coding: utf-8 -*-
"""Wire the 20 new SEO pages into sitemap.xml and llms.txt."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://bharatquantumprospera.com"
DATE = "2026-09-30"

NEW_PAGES = [
    # (slug, label, priority, changefreq)
    ("india-us-tax-treaty-dtaa", "India-US DTAA explained (Article 12, Form 10F, TRC)", "0.9", "monthly"),
    ("india-uae-tax-treaty-dtaa", "India-UAE DTAA after UAE Corporate Tax 2023", "0.88", "monthly"),
    ("india-singapore-tax-treaty-dtaa", "India-Singapore DTAA after the 2017 protocol (LOB, PPT)", "0.88", "monthly"),
    ("india-uk-tax-treaty-dtaa", "India-UK DTAA and the MFN clause (Article 13)", "0.88", "monthly"),
    ("india-mauritius-tax-treaty-dtaa", "India-Mauritius DTAA post-2016 protocol (grandfathering, LOB)", "0.88", "monthly"),
    ("stripe-atlas-vs-firstbase", "Stripe Atlas vs Firstbase compared for Indian founders", "0.85", "monthly"),
    ("stripe-atlas-vs-doola", "Stripe Atlas vs Doola compared for Indian founders", "0.85", "monthly"),
    ("c-corp-vs-s-corp", "C-Corp vs S-Corp (why S-Corp is off the table for Indian founders)", "0.85", "monthly"),
    ("mercury-vs-brex", "Mercury vs Brex for foreign-founder US business banking", "0.85", "monthly"),
    ("safe-vs-convertible-note", "SAFE vs Convertible Note for early-stage rounds", "0.85", "monthly"),
    ("esop-vs-rsu-vs-phantom-stock", "ESOP vs RSU vs Phantom Stock (tax at grant/vest/exercise/sale)", "0.85", "monthly"),
    ("delaware-c-corp-vs-llc", "Delaware C-Corp vs LLC for Indian founders", "0.88", "monthly"),
    ("how-to-get-ein-as-foreign-founder", "How to get an EIN as a foreign founder (no SSN)", "0.9", "monthly"),
    ("how-to-file-fbar-from-india", "How to file FBAR (FinCEN 114) from India", "0.88", "monthly"),
    ("how-to-flip-indian-company-to-us", "How to flip an Indian company to a US parent", "0.9", "monthly"),
    ("how-to-file-form-5472", "How to file Form 5472 for a foreign-owned US LLC", "0.88", "monthly"),
    ("how-to-file-boir-cta", "How to file BOIR (Corporate Transparency Act) with FinCEN", "0.85", "monthly"),
    ("what-is-fatca", "What is FATCA (Foreign Account Tax Compliance Act)", "0.85", "monthly"),
    ("what-is-pfic", "What is a PFIC (Passive Foreign Investment Company)", "0.85", "monthly"),
    ("what-is-form-w-8ben", "What is Form W-8BEN (and W-8BEN-E) for Indian residents", "0.85", "monthly"),
]

# --- sitemap.xml ---
sm_path = os.path.join(ROOT, "sitemap.xml")
sm = open(sm_path, encoding="utf-8").read()

# Insert new URLs before </urlset>
insight_block = ["", "  <!-- Insights / long-tail SEO pages -->"]
for slug, _, prio, freq in NEW_PAGES:
    insight_block.append(
        f'  <url><loc>{DOMAIN}/{slug}.html</loc><lastmod>{DATE}</lastmod><changefreq>{freq}</changefreq><priority>{prio}</priority></url>'
    )
insight_block.append("")
insertion = "\n".join(insight_block)

if "insights / long-tail" not in sm.lower():
    sm = sm.replace("</urlset>", insertion + "\n</urlset>")
    open(sm_path, "w", encoding="utf-8").write(sm)
    print(f"sitemap: +{len(NEW_PAGES)} URLs")
else:
    print("sitemap: already has insights block")

# --- llms.txt ---
llms_path = os.path.join(ROOT, "llms.txt")
llms = open(llms_path, encoding="utf-8").read()

if "## Insights" not in llms:
    block = ["", "## Insights (deep-dive guides for founders and CAs)", ""]
    for slug, label, _, _ in NEW_PAGES:
        block.append(f"- [{label}]({DOMAIN}/{slug}.html)")
    block.append("")
    llms = llms.rstrip() + "\n" + "\n".join(block)
    open(llms_path, "w", encoding="utf-8").write(llms)
    print(f"llms.txt: +{len(NEW_PAGES)} entries")
else:
    print("llms.txt: already has insights block")
