# -*- coding: utf-8 -*-
"""Batch AN: Round 25 - SEBI SME IPO consultation paper (14 October 2026)."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


ROWS = [
    ("Eligibility basis", "Post-issue paid-up capital", "Post-issue market cap: up to ₹1,000 crore must use the SME platform; ₹1,000-4,000 crore may opt in; above ₹4,000 crore must use the main board"),
    ("Profit test", "Operating profit of ₹1 crore in at least 2 of the preceding 3 years", "Average operating profit of ₹3 crore a year over the preceding 3 years (restated consolidated)"),
    ("If the profit test is not met", "Not eligible", "Book-built route with at least 75% allotted to QIBs; full refund if not met"),
    ("Minimum application", "₹2 lakh", "₹1 lakh: four lots of at least ₹25,000"),
    ("Minimum allottees", "200", "500"),
    ("Trading lot", "Linked to price band", "One share"),
    ("Market making", "Compulsory", "Removed"),
    ("General corporate purposes", "15% of issue, capped at ₹10 crore", "15% of issue; ₹10 crore cap removed"),
    ("Offer for sale", "Up to 20% of issue; each seller up to 50% of pre-issue holding", "Retained"),
    ("Price band", "Cap up to 120% of floor", "Cap at least 105% and up to 120% of floor"),
    ("After converting from a firm or LLP", "One full financial year before filing", "Four completed quarters plus one audited annual statement filed"),
]

table = "<table><thead><tr><th>Item</th><th>Current rule (ICDR, March 2025)</th><th>Proposed</th></tr></thead><tbody>" + \
        "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in ROWS) + "</tbody></table>"

p = dict(
    slug="sebi-sme-ipo-consultation-paper-october-2026-proposed-rules",
    title="SEBI's SME IPO Overhaul: What the October 2026 Consultation Paper Proposes",
    em="₹3 crore average profit, ₹1,000 crore market cap, 500 allottees.",
    kicker="/ News &middot; SME IPO &middot; Updated 2026-10-30",
    lead="On 14 October 2026 SEBI published a consultation paper proposing a major overhaul of SME IPO rules: a higher profit test (average operating profit of ₹3 crore over three years), eligibility based on market capitalisation, a lower ₹1 lakh minimum application, 500 minimum allottees and no compulsory market making. Comments are due by 4 November 2026. Until SEBI notifies final amendments, the March 2025 rules continue to apply.",
    sections=[
        ("/ Current rule vs proposal", "Side by side.", table),
        ("/ What it means if you are planning an SME IPO", "Practical points.",
         ul("Companies that meet today's test (₹1 crore operating profit in 2 of 3 years) but not a ₹3 crore three-year average should consider filing before any amendment takes effect, or plan for the QIB route.",
            "Companies converted from a partnership, proprietorship or LLP may find the proposed four-quarter rule shorter than today's full-year wait.",
            "Larger companies (market cap above ₹1,000 crore) would need Ind AS restated consolidated financials if they choose the SME platform, and must go to the main board above ₹4,000 crore.",
            "Restated, audited financials, clean GST and TDS records, and tidy share-capital history (demat under Rule 9B, FEMA filings for foreign holders) matter under either set of rules.",
            "You can send comments to SEBI by 4 November 2026.") +
         '<p><strong>Sources:</strong> <a href="https://upstox.com/news/market-news/ipo/sme-ipo-rules-set-for-major-overhaul-here-s-what-sebi-proposes/article-201897/" rel="nofollow noopener" target="_blank">Upstox</a>; '
         '<a href="https://www.caclubindia.com/news/sebi-proposes-sme-ipo-rules-2026-rs-3-crore-average-profit-and-500-allottees-proposed-26876.asp" rel="nofollow noopener" target="_blank">CAclubindia</a>.</p>'
         '<p>Check your current eligibility with the <a href="sme-ipo-eligibility-checker.html">SME IPO eligibility checker</a>.</p>'
         "<p><em>Last updated: 30 October 2026. These are proposals; confirm against the consultation paper on sebi.gov.in and any final notification.</em></p>"),
    ],
    faqs=[
        ("What did SEBI propose for SME IPOs in October 2026?", "A consultation paper dated 14 October 2026 proposes an average operating profit of ₹3 crore over three years, market-cap-based eligibility (SME platform up to ₹1,000 crore), a ₹1 lakh minimum application, 500 minimum allottees, removal of compulsory market making, and a QIB route for issuers that miss the profit test."),
        ("Are the new SME IPO rules in force?", "No. They are proposals; comments are due by 4 November 2026. The SEBI ICDR rules as amended in March 2025 apply until SEBI notifies amendments."),
        ("What is the current SME IPO profit requirement?", "Operating profit (EBITDA) of at least ₹1 crore in at least two of the preceding three financial years."),
        ("What happens to the minimum application size?", "It is proposed to fall from ₹2 lakh to ₹1 lakh, made up of four lots of at least ₹25,000 each."),
        ("Can BQP help prepare for an SME IPO?", "Yes: eligibility review, restated financials, tax and FEMA clean-up, and coordination with the merchant banker. " + CONTACT),
    ],
    related=[("sme-ipo.html", "SME IPO advisory"), ("sme-ipo-eligibility-checker.html", "SME IPO eligibility checker")],
    keywords="SEBI SME IPO consultation paper October 2026, SME IPO new rules 2026, SME IPO 3 crore operating profit, SME IPO minimum application 1 lakh, SME IPO 500 allottees, SEBI SME IPO proposals",
    desc="SEBI's 14 October 2026 consultation paper on SME IPOs: ₹3 crore average operating profit, market-cap eligibility (₹1,000 crore / ₹4,000 crore), ₹1 lakh minimum application, 500 allottees, no compulsory market making. Current rules vs proposals; comments due 4 November 2026.",
)

html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
            hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
            hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
            related=[(h, "Related", t) for h, t in p["related"]],
            cta_headline="Planning an SME IPO?", cta_body=CONTACT)
write_page(p["slug"], html)
print("Batch AN complete")
