# -*- coding: utf-8 -*-
"""Batch DR (20 Nov 2026): NRI year-end tax checklist before 31 December 2026 - refunds, belated/revised returns,
FAST-DS for returnees, advance tax, residency day count for holiday visits, TRC and lower deduction certificates.
Call-first page for the deadline window.
Facts (checked 19-20 Nov 2026): belated and revised ITR for AY 2026-27 by 31 December 2026; late fee up to INR 5,000
(INR 1,000 if total income does not exceed INR 5 lakh) plus interest; after that only an updated return (section
139(8A)) - 48 months from the end of the assessment year since the Finance Act, 2025, additional tax 25%/50%/60%/70%,
no refund through ITR-U (Taxmann, Business Today); advance tax only if tax after TDS exceeds INR 10,000, third
instalment 15 December, interest under 234B/234C (Income Tax Department); FAST-DS 2026 declarations by 31 December
2026 (site pages); residency: 182 days, or 60 days plus 365 in four prior years (120 days for Indian citizens/PIOs with
Indian income above INR 15 lakh; visiting citizens otherwise use 182), deemed residence for citizens with Indian
income above INR 15 lakh not taxed abroad; TRC and Form 10F (Form 41) for treaty rates; lower deduction certificate
before a property sale."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
NYE = "nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency"
DESK = "deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies"

C_NYE = contact("your country of residence, days in India this year, Indian income and TDS (Form 26AS / AIS), and any property sale or foreign assets")
PAGES = [dict(
    slug=NYE,
    title="NRI Year-End Tax Checklist Before 31 December 2026: Claim Refunds, File Belated or Revised ITR, FAST-DS, Advance Tax and Your India Day Count",
    em="six things to do before the year closes.",
    kicker="/ NRIs &middot; Year-end &middot; Deadlines &middot; Updated 2026-11-20",
    lead=("Six things NRIs should check before <strong>31 December 2026</strong>. First, <strong>file a belated or revised return for FY 2025-26 (AY 2026-27)</strong> to claim back excess TDS on NRO interest, rent or a property sale; after 31 December only an <strong>updated return</strong> is possible, which carries additional tax of 25% to 70% and <strong>cannot claim a refund</strong>. Second, pay <strong>advance tax by 15 December</strong> if your FY 2026-27 Indian tax after TDS will exceed INR 10,000, for example on capital gains. Third, <strong>returning NRIs</strong> who held unreported foreign assets while resident should consider <strong>FAST-DS 2026</strong>, open until 31 December. "
          "Fourth, <strong>count your India days</strong> if you are visiting for the holidays: 182 days, or 120 days for Indian citizens with Indian income above INR 15 lakh, can make you resident. Fifth, get your <strong>tax residency certificate and Form 10F</strong> ready for treaty rates. Sixth, apply for a <strong>lower deduction certificate</strong> before any property sale."),
    sections=[
        ("/ The checklist", "Do these in order.",
         table(["#", "Action", "Deadline", "Why it matters"], [
             ["1", "Belated or revised ITR for FY 2025-26 (AY 2026-27)", "31 December 2026", "Last chance to claim refunds of excess TDS; late fee up to INR 5,000 (INR 1,000 for small incomes) plus interest"],
             ["2", "Advance tax for FY 2026-27 if tax after TDS exceeds INR 10,000", "15 December 2026 (75% cumulative)", "Avoids interest for short payment"],
             ["3", "FAST-DS 2026 for unreported foreign assets from resident years", "31 December 2026", "Closes Black Money Act exposure for returning NRIs"],
             ["4", "Count days in India for FY 2026-27", "Before you travel", "182 days, or 120 days with Indian income above INR 15 lakh, can make you resident and taxable on worldwide income"],
             ["5", "TRC and Form 10F (Form 41) for treaty rates", "Before the next payment", "Lower TDS on interest, dividends and royalties"],
             ["6", "Lower deduction certificate before a property sale", "Before the sale agreement", "Avoids TDS on the full sale price"]])
         + call_box("my NRI year-end tax position", ["Whether you have a refund to claim for FY 2025-26 and how to file it before 31 December",
                                                      "Your residency for FY 2026-27 given your travel plans",
                                                      "Advance tax for 15 December, if any",
                                                      "FAST-DS for foreign assets if you have returned to India",
                                                      "Treaty documents and lower TDS certificates for the coming year"],
                    "Form 26AS / AIS, your days in India this year, and details of any property sale, rent or foreign assets.")),
        ("/ Refunds: why 31 December matters", "Updated returns cannot get you money back.",
         ul("<strong>Common refund sources:</strong> TDS on property sale (deducted on the full price unless a lower deduction certificate was used), TDS on rent (31.2% or more), TDS on NRO interest (30% plus surcharge and cess) where treaty or slab tax is lower.",
            "<strong>Belated return:</strong> section 139(4), by 31 December 2026, with late fee and interest; see <a href=\"belated-itr-31-december-2026-section-139-4-india.html\">belated return</a>.",
            "<strong>Revised return:</strong> to correct a filed return, also by 31 December 2026; see <a href=\"revised-itr-section-139-5-deadline-31-december-2026-india.html\">revised return</a>.",
            "<strong>Updated return afterwards:</strong> allowed for up to 48 months after the assessment year since the Finance Act, 2025, but only to pay more tax, not to claim a refund; see <a href=\"itr-u-updated-return-48-months-section-139-8a-india.html\">ITR-U</a>.",
            "<strong>Which form:</strong> ITR-2, or ITR-3 with business income; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR for NRIs</a>.")),
        ("/ Holiday visits and residency", "Count before you fly.",
         ul("<strong>Basic tests:</strong> resident if in India 182 days or more in the financial year, or 60 days in the year plus 365 days in the previous four years; for Indian citizens and persons of Indian origin visiting India, the 60-day limb becomes 120 days only if Indian income exceeds INR 15 lakh, otherwise 182 days applies.",
            "<strong>Deemed residence:</strong> an Indian citizen with Indian income above INR 15 lakh who is not liable to tax in any country is treated as resident (not ordinarily resident); relevant for NRIs in the UAE and other no-tax countries; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence</a>.",
            "<strong>Check your status:</strong> use the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.")
         + f'<p>Related: <a href="{DESK}.html">deadline desk to 31 January 2027</a> &middot; <a href="fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html">FAST-DS 2026</a> &middot; <a href="advance-tax-q3-december-15-2026-india.html">advance tax 15 December</a> &middot; <a href="nri-property-tds-ldc-calculator.html">NRI property TDS and lower deduction certificate</a> &middot; <a href="nri-missed-itr-deadline-what-to-do-india.html">NRI missed the deadline</a>.</p>'
         + sources("Income-tax Act, 1961 for AY 2026-27 (sections 6, 139(4), 139(5), 139(8A), 140B, 208, 234A-234C, 234F) as amended by the Finance Act, 2025; Income-tax Act, 2025 from tax year 2026-27; FAST-DS 2026 scheme. Checked 19-20 November 2026: Income Tax Department advance tax guidance, Taxmann and Business Today on the 48-month ITR-U window.")),
    ],
    faqs=[("What is the last date for NRIs to file a belated ITR for FY 2025-26?", "31 December 2026 for AY 2026-27, with a late fee of up to INR 5,000 (INR 1,000 if total income does not exceed INR 5 lakh) plus interest."),
          ("Can an NRI claim a TDS refund after 31 December 2026?", "Not through the regular route. After 31 December only an updated return (ITR-U) is possible, which can be used to pay additional tax but not to claim a refund."),
          ("Do NRIs need to pay advance tax?", "Only if the Indian tax for the year, after TDS, exceeds INR 10,000; the third instalment (75% cumulative) is due on 15 December."),
          ("Can a holiday visit to India make an NRI resident?", "Yes, if total days in India reach 182 in the financial year, or 120 days for Indian citizens and PIOs whose Indian income exceeds INR 15 lakh and who meet the 365-day test; count before you travel."),
          ("What is FAST-DS 2026 and does it apply to NRIs?", "A one-time window to declare undisclosed foreign assets and income from resident years; it mainly matters for returning NRIs and is open until 31 December 2026."),
          ("Can BQP handle my year-end filings from abroad?", "Yes. " + C_NYE)],
    related=[("belated-itr-31-december-2026-section-139-4-india.html", "Belated return by 31 December"), ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             (DESK + ".html", "Deadline desk")],
    cta_h="NRI with Indian income or a refund pending?", cta_b=C_NYE,
    keywords="NRI tax checklist December 2026, NRI belated ITR 31 December 2026, NRI TDS refund last date, NRI advance tax 15 December, NRI residency 182 days holiday visit, NRI FAST-DS 2026, NRI updated return refund",
    desc="NRI year-end checklist before 31 Dec 2026: belated/revised ITR for refunds (ITR-U later cannot refund), advance tax by 15 Dec if tax after TDS exceeds INR 10,000, FAST-DS for returnees, India day count for holiday visits (182/120 days), TRC and Form 10F, lower deduction certificate before property sales.",
    howto={"name": "How an NRI closes the tax year before 31 December 2026", "description": "Six steps.", "steps": [
        {"name": "Check refunds", "text": "Compare TDS in Form 26AS / AIS with actual tax; file a belated or revised return by 31 December."},
        {"name": "Pay advance tax", "text": "If FY 2026-27 tax after TDS exceeds INR 10,000, pay by 15 December."},
        {"name": "Review foreign assets", "text": "Returning NRIs consider FAST-DS 2026 by 31 December."},
        {"name": "Count India days", "text": "Plan holiday visits around the 182-day and 120-day tests."},
        {"name": "Prepare treaty and TDS documents", "text": "TRC, Form 10F and a lower deduction certificate before property sales."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DR complete:", len(PAGES))
