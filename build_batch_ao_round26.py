# -*- coding: utf-8 -*-
"""Batch AO: Round 26 - TCS on sale of goods discontinued (1 Apr 2025); 194Q pages rewritten; 206AB omitted."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SRC = ('<p><strong>Sources:</strong> <a href="https://vjmglobal.com/blog/key-amendments-in-income-tax-provisions-1st-april-2025" rel="nofollow noopener" target="_blank">VJM Global: amendments from 1 April 2025</a>; '
       '<a href="https://calcguru.in/?p=8271" rel="nofollow noopener" target="_blank">CalcGuru: 194Q vs 206C(1H) after the change</a>; '
       '<a href="https://www.incometaxindia.gov.in/w/section-206ab-6" rel="nofollow noopener" target="_blank">Income Tax Department: Section 206AB omitted</a>.</p>'
       '<p><em>Last updated: 30 October 2026. From 1 April 2026, TDS and TCS provisions sit in Sections 393 and 394 of the Income-tax Act, 2025; the rules described here carried over.</em></p>')


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


Q194 = ul("<strong>Who deducts</strong>: a buyer whose turnover exceeded INR 10 crore in the preceding financial year.",
          "<strong>When</strong>: on purchases of goods from a resident seller exceeding INR 50 lakh in the financial year.",
          "<strong>Rate</strong>: 0.1% on the amount above INR 50 lakh, at credit or payment, whichever is earlier.",
          "<strong>Seller without PAN</strong>: 5%.",
          "<strong>Not applicable</strong>: imports from non-resident sellers, and transactions where TDS under another provision or TCS (other than on sale of goods) applies.")

PAGES = [
    dict(slug="section-206c-1h-tcs-sale-goods-india",
         title="TCS on Sale of Goods (Section 206C(1H)) Discontinued From 1 April 2025: What Applies Now",
         em="sellers stop collecting; buyers' TDS under 194Q remains.",
         kicker="/ TDS &amp; TCS &middot; Updated 2026-10-30",
         lead="Finance Act 2025 ended TCS on sale of goods under Section 206C(1H) for sales from 1 April 2025. Sellers with turnover above INR 10 crore no longer collect 0.1% TCS from buyers. For ordinary goods transactions, the only remaining withholding is TDS by large buyers under Section 194Q. Separate TCS on specific items, such as motor vehicles and notified luxury goods above INR 10 lakh, continues.",
         sections=[
             ("/ What changed", "Before and after 1 April 2025.",
              "<table><thead><tr><th></th><th>Up to 31 March 2025</th><th>From 1 April 2025</th></tr></thead><tbody>"
              "<tr><td>Seller (turnover above INR 10 crore)</td><td>Collected 0.1% TCS on receipts above INR 50 lakh per buyer</td><td>No TCS on sale of goods</td></tr>"
              "<tr><td>Buyer (turnover above INR 10 crore)</td><td>Deducted 0.1% TDS under Section 194Q, which took priority</td><td>Still deducts 0.1% TDS under Section 194Q</td></tr>"
              "<tr><td>Non-filer higher rates (Sections 206AB / 206CCA)</td><td>Applied</td><td>Omitted</td></tr></tbody></table>"),
             ("/ What still applies", "Do not switch everything off.", Q194 + ul(
                 "TCS on motor vehicles and notified luxury goods above INR 10 lakh, and on specified items such as scrap and minerals, continues.",
                 "E-commerce operators still deduct 0.1% income-tax TDS under Section 194-O and collect GST TCS under Section 52 of the CGST Act.",
                 "TCS collected for FY 2024-25 and earlier must still be reported correctly; credit mismatches in Form 26AS can still arise for those years.")),
             ("/ What to update", "Housekeeping.", ul(
                 "Remove TCS on sale of goods from invoicing and ERP settings for sales from 1 April 2025.",
                 "Stop issuing declarations to buyers about 194Q vs 206C(1H) overlap; they are no longer needed.",
                 "Reconcile any TCS collected by mistake after 1 April 2025 and correct it with the buyer.") + SRC),
         ],
         faqs=[("Is TCS under Section 206C(1H) still applicable?", "No. Finance Act 2025 discontinued TCS on sale of goods for sales from 1 April 2025."),
               ("What replaces it?", "Nothing on the seller's side. Large buyers (turnover above INR 10 crore) still deduct 0.1% TDS under Section 194Q on purchases above INR 50 lakh from a seller."),
               ("Are Sections 206AB and 206CCA still in force?", "No. Both were omitted from 1 April 2025, so the higher rates for non-filers no longer apply. Higher rates for missing PAN still apply."),
               ("Does TCS still apply to cars and luxury goods?", "Yes. TCS on motor vehicles and notified luxury goods above INR 10 lakh continues."),
               ("Can BQP clean up our TDS/TCS settings?", "Yes, including reconciliation of past years. " + CONTACT)],
         related=[("what-is-section-194q-and-how-to-comply-india.html", "Section 194Q TDS on purchases"), ("form-26as-vs-ais-vs-tis-india-2026.html", "Form 26AS, AIS and TIS")],
         keywords="206C(1H) TCS discontinued, TCS on sale of goods removed 2025, 206C(1H) omitted Finance Act 2025, is TCS on sale of goods applicable, 194Q after 206C(1H) removal",
         desc="TCS on sale of goods under Section 206C(1H) was discontinued for sales from 1 April 2025 (Finance Act 2025). Buyers' 0.1% TDS under Section 194Q remains; Sections 206AB and 206CCA were omitted; TCS on cars and luxury goods continues."),
    dict(slug="what-is-section-194q-and-how-to-comply-india",
         title="What Is Section 194Q and How to Comply (After TCS on Goods Was Scrapped)",
         em="0.1% TDS on purchases above INR 50 lakh.",
         kicker="/ AI Answer &middot; TDS &middot; Updated 2026-10-30",
         lead="Section 194Q requires a buyer with turnover above INR 10 crore in the preceding year to deduct 0.1% TDS on purchases of goods from a resident seller exceeding INR 50 lakh in a financial year. Since TCS on sale of goods under Section 206C(1H) was discontinued from 1 April 2025, Section 194Q is the only withholding on ordinary goods transactions.",
         sections=[
             ("/ The rule", "Section 194Q at a glance.", Q194),
             ("/ How to comply", "Monthly and quarterly steps.",
              "<ol><li>At the start of each year, check whether your turnover in the previous year exceeded INR 10 crore.</li>"
              "<li>Track purchases per seller; deduct only on the amount above INR 50 lakh.</li>"
              "<li>Deduct at credit or payment, whichever is earlier, and deposit by the 7th of the following month.</li>"
              "<li>File the quarterly TDS statement and issue TDS certificates to sellers.</li>"
              "<li>Collect sellers' PAN up front to avoid the 5% rate.</li></ol>"),
             ("/ What changed in 2025", "Simpler than before.", ul(
                 "No more coordination with sellers about 206C(1H) overlap: sellers no longer collect TCS on goods.",
                 "Section 206AB (higher rate for non-filers) was omitted from 1 April 2025.",
                 "From 1 April 2026, the provision sits in Section 393 of the Income-tax Act, 2025.") + SRC),
         ],
         faqs=[("What is Section 194Q?", "TDS of 0.1% by a buyer with turnover above INR 10 crore on purchases of goods from a resident seller above INR 50 lakh in a year, on the amount above INR 50 lakh."),
               ("Does 194Q still interact with 206C(1H)?", "No. TCS on sale of goods under Section 206C(1H) was discontinued from 1 April 2025, so 194Q is the only withholding on ordinary goods sales."),
               ("What if the seller has no PAN?", "TDS is deducted at 5% instead of 0.1%."),
               ("Does 194Q apply to imports?", "No. It applies to purchases from resident sellers."),
               ("Can BQP set up 194Q compliance?", "Yes: tracking, deduction, statements and certificates. " + CONTACT)],
         related=[("section-206c-1h-tcs-sale-goods-india.html", "TCS on sale of goods discontinued"), ("section-194q-tds-purchase-goods-india.html", "Section 194Q detailed guide")],
         keywords="what is section 194Q, section 194Q TDS 0.1%, 194Q after 206C(1H) removed, 194Q applicability 2026, TDS on purchase of goods India",
         desc="Section 194Q: buyers with turnover above INR 10 crore deduct 0.1% TDS on purchases above INR 50 lakh per seller. After TCS on sale of goods (206C(1H)) was discontinued from 1 April 2025, it is the only withholding on goods sales."),
    dict(slug="section-194q-tds-purchase-goods-india",
         title="Section 194Q TDS on Purchase of Goods: Complete Guide for 2026",
         em="thresholds, timing, rates and the end of the 206C(1H) overlap.",
         kicker="/ TDS &middot; Updated 2026-10-30",
         lead="Section 194Q TDS applies when a buyer with turnover above INR 10 crore buys goods worth more than INR 50 lakh in a year from one resident seller: 0.1% on the excess. The old overlap with sellers' TCS under Section 206C(1H) ended when that TCS was discontinued from 1 April 2025.",
         sections=[
             ("/ The rule", "Who, when, how much.", Q194),
             ("/ Worked example", "How the threshold works.",
              "<p>A buyer with last year's turnover of INR 40 crore buys goods worth INR 80 lakh from one supplier during the year. TDS applies on INR 30 lakh (the excess over INR 50 lakh) at 0.1%: INR 3,000. If the supplier has no PAN, the rate is 5%: INR 1.5 lakh.</p>"),
             ("/ Common mistakes", "What to avoid.", ul(
                 "Deducting on the full purchase value instead of only the excess over INR 50 lakh.",
                 "Counting the threshold across all suppliers instead of per supplier.",
                 "Still asking suppliers to confirm they will not collect 206C(1H) TCS; that provision no longer applies.",
                 "Applying the omitted Section 206AB higher rate.") + SRC),
         ],
         faqs=[("When does Section 194Q apply?", "When the buyer's turnover in the preceding year exceeded INR 10 crore and purchases from one resident seller exceed INR 50 lakh in the year."),
               ("What is the rate under 194Q?", "0.1% on the amount above INR 50 lakh; 5% if the seller has no PAN."),
               ("Is there still a 194Q and 206C(1H) overlap?", "No. TCS under Section 206C(1H) was discontinued from 1 April 2025."),
               ("Can BQP help with 194Q?", "Yes. " + CONTACT)],
         related=[("what-is-section-194q-and-how-to-comply-india.html", "Section 194Q quick answer"), ("section-206c-1h-tcs-sale-goods-india.html", "TCS on sale of goods discontinued")],
         keywords="section 194Q TDS purchase of goods, 194Q threshold 50 lakh, 194Q rate 0.1%, 194Q example, 194Q 2026",
         desc="Section 194Q TDS on purchase of goods: 0.1% on purchases above INR 50 lakh per seller by buyers with turnover above INR 10 crore, 5% without PAN, worked example and common mistakes; the 206C(1H) overlap ended from 1 April 2025."),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline="TDS and TCS set-up questions?", cta_body=CONTACT)
    write_page(p["slug"], html)
print(f"Batch AO complete: {len(PAGES)} pages rewritten")
