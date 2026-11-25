# -*- coding: utf-8 -*-
"""Batch JC (25 Nov 2026): Company annual filing in India 2026 (ROC / MCA) - AOC-4 within 30 days of the AGM (30 October
2026 for a 30 September AGM), MGT-7 / MGT-7A within 60 days (29 November 2026); additional fee Rs 100 a day of delay
(no cap) on top of the normal fee; General Circular 05/2026 (24 October 2026) waives the additional fee for FY 2025-26
AOC-4 variants filed by 31 December 2026 and MGT-7 / MGT-7A by 31 January 2027 (fee relaxation, not an AGM extension);
Companies Compliance Facilitation Scheme 2026 (CCFS-2026, General Circular 01/2026, extended by 04/2026) waived 90% of
additional fees on older delayed filings and closed on 15 September 2026. Other annual items: ADT-1, DIR-3 KYC, DPT-3
by 30 June, MSME-1 half-yearly, income tax return (ITR-6). Status check: MCA master data / view public documents.
Demand: sweep ac116 (25 Nov 2026), all 7 markets: "company annual filing", "company annual filing due date / date",
"company annual filing status / status check", "company annual filing fee", "company annual filing scheme",
"corporate annual filing".
Facts (checked 25 Nov 2026): Taxmann, AZB Partners, Mondaq (CCFS-2026); CareerIndia, TaxGuru, Fox Mandal (Circular
05/2026); site AOC-4, MGT-7, LLP annual filing, DPT-3 and ADT-1 pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "company-annual-filing-india-2026-aoc-4-mgt-7-due-date-fee-waiver-circular-05-2026-ccfs-status-check"

C = contact("your company's CIN, the date of the last AGM, which of AOC-4, MGT-7 and other forms are pending, and the years involved")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="MCA Filing Due Date 2026 (Company Annual Filing): AOC-4 and MGT-7 Last Dates, Fee Waiver Till 31 December / 31 January (Circular 05/2026), Extension, CCFS-2026 and Status Check",
    em="file FY 2025-26 forms inside the waiver window.",
    kicker="/ Private limited companies, OPCs and foreign subsidiaries &middot; ROC compliance &middot; Updated 2026-11-25",
    lead=("<strong>Every company files its financial statements in AOC-4 within 30 days of the AGM and its annual return in MGT-7 (MGT-7A for small companies and OPCs) within 60 days, which for a 30 September AGM means 30 October and 29 November 2026.</strong> "
          "Late filing normally costs an additional fee of &#8377;100 a day with no cap, but General Circular 05/2026 waives it for FY 2025-26 AOC-4 filed by 31 December 2026 and MGT-7 / MGT-7A by 31 January 2027. "
          "The separate CCFS-2026 amnesty for older delayed filings closed on 15 September 2026."),
    sections=[
        ("/ Annual filings and due dates", "What a company files each year.",
         table(["Filing", "What it is", "Due date (FY 2025-26)"], [
             ["AOC-4 (or AOC-4 XBRL / CFS)", "Financial statements and board report", "Within 30 days of the AGM (30 October 2026); fee-free till 31 December 2026"],
             ["MGT-7 / MGT-7A", "Annual return (MGT-7A for small companies and OPCs)", "Within 60 days of the AGM (29 November 2026); fee-free till 31 January 2027"],
             ["ADT-1", "Auditor appointment", "Within 15 days of the meeting"],
             ["DPT-3", "Return of deposits and outstanding loans", "30 June"],
             ["MSME-1", "Dues to micro and small suppliers over 45 days", "Half-yearly"],
             ["DIR-3 KYC", "Director KYC", "30 June (now every three years)"],
             ["ITR-6", "Company income tax return", "31 October normally; 21 November 2026 for AY 2026-27"]])
         + '<p>Form details: ' + L("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 and the waiver") + ', ' + L("mgt-7-mgt-7a-annual-return-29-november-2026-india.html", "MGT-7 and MGT-7A") + ', ' + L("form-dpt-3-return-of-deposits-india-2026.html", "DPT-3") + ' and ' + L("form-adt-1-auditor-appointment-15-days-first-auditor-rotation-adt-3-india-2026.html", "ADT-1") + '. For LLPs: ' + L("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing") + '.</p>'),
        ("/ Fees, waivers and the CCFS-2026 scheme", "What late filing costs now.",
         ul("<strong>Additional fee:</strong> &#8377;100 a day of delay on top of the normal filing fee, with no upper limit.",
            "<strong>Circular 05/2026:</strong> waives the additional fee for FY 2025-26 AOC-4 variants filed by 31 December 2026 and MGT-7 / MGT-7A by 31 January 2027; it does not extend the AGM deadline, and after these dates the fee runs from the original due date.",
            "<strong>CCFS-2026:</strong> a one-time scheme that waived 90% of additional fees on older delayed filings (MGT-7, AOC-4, ADT-1 and others); it closed on 15 September 2026 after one extension.",
            "<strong>Penalties:</strong> beyond fees, continued non-filing can lead to penalties on the company and officers, director disqualification and strike-off.",
            "<strong>Normal fees:</strong> the base filing fee depends on the company's share capital and still applies.")),
        ("/ How to check filing status", "Confirm what is filed and what is pending.",
         ul("<strong>MCA master data:</strong> search the company name or CIN to see status (active, strike-off), last AGM and balance sheet dates.",
            "<strong>View public documents:</strong> download filed forms and financial statements from the MCA portal.",
            "<strong>Company or foreign buyer checks:</strong> see " + L("how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html", "how to verify an Indian company") + ".",
            "<strong>Foreign-owned subsidiaries:</strong> see the " + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "annual compliance calendar") + ".")
         + call_box("ROC annual filing", ["AOC-4 and MGT-7 / MGT-7A filing",
                                           "Catch-up of missed years",
                                           "ADT-1, DPT-3, MSME-1 and DIR-3 KYC",
                                           "Board report and AGM documentation",
                                           "Foreign subsidiary compliance"],
                    "your CIN and pending forms.")
         + sources("Companies Act, 2013 (sections 92, 137, 403) and Companies (Registration Offices and Fees) Rules; MCA General Circulars 01/2026, 04/2026 and 05/2026 as reported by Taxmann, AZB Partners, Mondaq, TaxGuru, Fox Mandal and CareerIndia; site AOC-4, MGT-7, LLP, DPT-3 and ADT-1 guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the due date for company annual filing in India?", "AOC-4 within 30 days of the AGM and MGT-7 / MGT-7A within 60 days; with the AGM on 30 September, that is 30 October and 29 November 2026 for FY 2025-26."),
          ("Is there a fee waiver for late AOC-4 and MGT-7 in 2026?", "Yes. General Circular 05/2026 waives the additional fee for FY 2025-26 AOC-4 filed by 31 December 2026 and MGT-7 / MGT-7A by 31 January 2027. It does not extend the AGM date."),
        ("Has the MCA extended the filing due date in 2026?", "No. The due dates (AOC-4 within 30 days and MGT-7 / MGT-7A within 60 days of the AGM) and the AGM deadline have not been extended. General Circular 05/2026 only waives the additional fee for FY 2025-26 AOC-4 filed by 31 December 2026 and MGT-7 / MGT-7A filed by 31 January 2027; after those dates the additional fee runs from the original due date."),
          ("What is the late fee for company annual filing?", "An additional fee of Rs 100 a day of delay on top of the normal filing fee, with no cap, unless a waiver applies."),
          ("What is the company annual filing scheme (CCFS-2026)?", "The Companies Compliance Facilitation Scheme 2026 waived 90% of additional fees on older delayed filings such as MGT-7, AOC-4 and ADT-1. It closed on 15 September 2026."),
          ("How do I check a company's annual filing status?", "Search the company on the MCA master data page with its name or CIN to see its status and last AGM and balance sheet dates, and view filed documents on the MCA portal."),
          ("What happens if a company does not file annual returns?", "Additional fees keep running, and continued default can lead to penalties on the company and officers, disqualification of directors and strike-off by the Registrar."),
          ("Can BQP file our annual returns?", "Yes. CA Durgesh Chavda handles AOC-4, MGT-7, ADT-1, DPT-3 and catch-up filings for companies and foreign-owned subsidiaries. " + C)],
    related=[("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 and the waiver"),
             ("mgt-7-mgt-7a-annual-return-29-november-2026-india.html", "MGT-7 and MGT-7A"),
             ("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing"),
             ("form-dpt-3-return-of-deposits-india-2026.html", "DPT-3"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Foreign subsidiary compliance calendar")],
    cta_h="Annual returns pending?", cta_b=C,
    keywords="company annual filing, company annual filing due date, company annual filing status check, company annual filing fee, company annual filing scheme, aoc-4 due date 2026, mgt-7 due date 2026, circular 05/2026, ccfs 2026, roc annual filing",
    desc="Company annual filing in India 2026: AOC-4 within 30 days and MGT-7 within 60 days of the AGM, Rs 100 a day additional fee, FY 2025-26 waiver till 31 December / 31 January (Circular 05/2026), CCFS-2026 closed 15 September, and how to check filing status.",
    howto={"name": "How to complete company annual filing", "description": "For private limited companies.", "steps": [
        {"name": "Hold the AGM", "text": "Approve the financial statements by 30 September."},
        {"name": "File AOC-4", "text": "Within 30 days; fee-free till 31 December 2026 for FY 2025-26."},
        {"name": "File MGT-7 / MGT-7A", "text": "Within 60 days; fee-free till 31 January 2027 for FY 2025-26."},
        {"name": "File other forms", "text": "ADT-1, DPT-3, MSME-1 and DIR-3 KYC as due."},
        {"name": "Check status", "text": "Confirm on the MCA master data page."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JC complete")
