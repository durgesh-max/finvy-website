# -*- coding: utf-8 -*-
"""Batch JK (26 Nov 2026): ROC compliance for private limited companies and LLPs, FY 2026-27 calendar.
Demand: sweep ac121 (26 Nov 2026), all 7 markets: "roc compliance", "roc compliance for private limited company",
"roc compliance for pvt ltd company", "roc compliance for llp", "roc compliance calendar 2026-27", "roc compliance due date",
"roc compliance meaning", "roc compliance fees". No dedicated page existed.
Facts (checked 26 Nov 2026): Companies Act 2013 ss. 92, 96, 137, 139, 164(2), 173; LLP Act 2008 / LLP Rules (Form 11 by
30 May, Form 8 by 30 October); MSME-1 half-yearly (31 October / 30 April); DPT-3 30 June (site DPT-3 page, StudyCafe /
LegalWiz calendars); DIR-3 KYC every three financial years by 30 June (G.S.R. 943(E), site DIR-3 KYC page); AOC-4 /
MGT-7 / Circular 05/2026 (site company annual filing page); PAS-3, DIR-12, MGT-14, INC-20A, ADT-1 (site form pages).
No firm fees are quoted."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 26 November 2026."
SLUG = "roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees"

C = contact("whether you run a private limited company, OPC or LLP, its CIN or LLPIN, the last AGM or Form 11 / Form 8 filed, and which forms or years are pending")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="ROC Compliance and ROC Late Filing Fees (2026-27): Calendar, Due Dates, Forms, the Rs 100 a Day Additional Fee and the Circular 05/2026 Waiver for Private Limited Companies and LLPs",
    em="what to file with the Registrar, and when.",
    kicker="/ Private limited companies, OPCs, LLPs and foreign subsidiaries &middot; Companies Act 2013 &middot; Updated 2026-11-26",
    lead=("<strong>ROC compliance means the filings a company or LLP must make with the Registrar of Companies on the MCA portal, plus the meetings and records the law requires.</strong> "
          "A private limited company files AOC-4 within 30 days and MGT-7 / MGT-7A within 60 days of its AGM, DPT-3 by 30 June, MSME-1 half-yearly and event-based forms such as DIR-12 and PAS-3. "
          "An LLP files Form 11 by 30 May and Form 8 by 30 October. Late forms cost an additional fee of &#8377;100 a day with no cap."),
    sections=[
        ("/ What ROC compliance means", "Three kinds of obligation.",
         ul("<strong>Annual forms:</strong> financial statements, annual return and other yearly returns filed with the Registrar of Companies (ROC) through the MCA V3 portal.",
            "<strong>Event-based forms:</strong> filed when something changes, such as a new director, a share allotment, a special resolution or a change of auditor.",
            "<strong>Meetings and records:</strong> board meetings, the annual general meeting (AGM), statutory registers and minutes that must be kept even though they are not filed.",
            "<strong>Who it applies to:</strong> every company registered in India, including foreign-owned subsidiaries, and every LLP, whether or not it has done any business in the year.")),
        ("/ Private limited company: FY 2026-27 calendar", "Annual and recurring items.",
         table(["Item", "What it is", "When"], [
             ["Board meetings", "At least four a year, with no more than 120 days between two meetings", "Through the year; small companies and OPCs need at least one in each half of the calendar year, at least 90 days apart"],
             ["Statutory audit", "Every company's accounts are audited, whatever its size", "Before the AGM"],
             ["AGM", "Shareholders adopt the accounts (OPCs do not hold an AGM)", "Within six months of the year end, so by 30 September; the first AGM within nine months of the first year end"],
             ["AOC-4", "Financial statements and board report", "Within 30 days of the AGM"],
             ["MGT-7 / MGT-7A", "Annual return (MGT-7A for small companies and OPCs)", "Within 60 days of the AGM"],
             ["ADT-1", "Auditor appointment", "Within 15 days of the meeting that appoints the auditor"],
             ["DPT-3", "Return of deposits and outstanding loans as at 31 March", "30 June"],
             ["MSME-1", "Dues to micro and small suppliers unpaid beyond 45 days", "31 October (April-September) and 30 April (October-March)"],
             ["DIR-3 KYC", "KYC of every director with a DIN", "Once every three financial years, by 30 June"],
             ["ITR-6", "Company income tax return (filed with the Income Tax Department, not the ROC)", "31 October normally; 21 November 2026 for AY 2026-27"]])
         + '<p>For FY 2025-26 accounts, General Circular 05/2026 waives the additional fee on AOC-4 filed by 31 December 2026 and MGT-7 / MGT-7A filed by 31 January 2027; see ' + L("company-annual-filing-india-2026-aoc-4-mgt-7-due-date-fee-waiver-circular-05-2026-ccfs-status-check.html", "company annual filing and the 2026 waiver") + '. Form guides: ' + L("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4") + ', ' + L("mgt-7-mgt-7a-annual-return-29-november-2026-india.html", "MGT-7") + ', ' + L("form-dpt-3-return-of-deposits-india-2026.html", "DPT-3") + ', ' + L("form-adt-1-auditor-appointment-15-days-first-auditor-rotation-adt-3-india-2026.html", "ADT-1") + ' and ' + L("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC") + '.</p>'),
        ("/ Event-based ROC forms", "Filed when something changes.",
         table(["Form", "Event", "Time limit"], [
             ["INC-20A", "Declaration of commencement of business (new companies with share capital)", "Within 180 days of incorporation"],
             ["DIR-12", "Appointment, resignation or change of a director", "Within 30 days"],
             ["PAS-3", "Return of allotment of shares", "Within 15 days for a private placement; 30 days for other allotments"],
             ["MGT-14", "Filing of special and certain board resolutions", "Within 30 days"],
             ["SH-7 / INC-22 and others", "Change in capital, registered office and similar events", "Within the period set for each form"]])
         + '<p>Guides: ' + L("form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026.html", "INC-20A") + ', ' + L("form-dir-12-director-appointment-resignation-30-days-late-fees-dir-11-india-2026.html", "DIR-12") + ' and ' + L("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "MGT-14") + '.</p>'),
        ("/ LLP ROC compliance", "Two annual forms plus KYC.",
         table(["Item", "What it is", "When"], [
             ["Form 11", "Annual return of the LLP", "By 30 May"],
             ["Form 8", "Statement of account and solvency", "By 30 October"],
             ["Audit", "Required if turnover exceeds &#8377;40 lakh or contribution exceeds &#8377;25 lakh", "Before Form 8"],
             ["DIR-3 KYC", "KYC of designated partners with a DIN / DPIN", "Once every three financial years, by 30 June"],
             ["Form 3 / Form 4", "Changes in the LLP agreement or partners", "Within 30 days of the change"]])
         + '<p>More: ' + L("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing") + ' and ' + L("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "Form 8 for 2026") + '.</p>'),
        ("/ Late fees, penalties and fees", "What missing a date costs.",
         ul("<strong>Additional fee:</strong> &#8377;100 a day of delay on top of the normal filing fee, with no cap, for both companies and LLPs, unless a waiver applies.",
            "<strong>Penalties:</strong> separate penalties can apply to the company and its officers for failing to hold meetings or file returns.",
            "<strong>Director disqualification:</strong> directors of a company that has not filed financial statements or annual returns for three continuous financial years can be disqualified under section 164(2).",
            "<strong>Strike-off:</strong> the Registrar can strike off companies that stop filing; a company with no business can instead apply to become " + L("dormant-company-india-section-455-msc-1-msc-3-foreign-subsidiary-vs-strike-off-2026.html", "dormant") + " or " + L("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "close through STK-2") + ".",
            "<strong>Government filing fees:</strong> the normal MCA fee for most forms depends on the company's authorised share capital (or the LLP's contribution), so it differs from company to company.")),
        ("/ Foreign-owned subsidiaries", "Extra reporting beyond the ROC.",
         ul("<strong>RBI reporting:</strong> FC-GPR within 30 days of allotting shares to a foreign investor, and the annual FLA return.",
            "<strong>Resident director:</strong> at least one director must stay in India for 182 days or more in the financial year.",
            "<strong>Calendar:</strong> see the " + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "annual compliance calendar for foreign-owned subsidiaries") + ".")
         + call_box("ROC compliance", ["AOC-4, MGT-7 / MGT-7A and ADT-1",
                                       "DPT-3, MSME-1 and DIR-3 KYC",
                                       "Board meeting and AGM documentation",
                                       "LLP Form 11 and Form 8",
                                       "Catch-up filings and foreign subsidiary compliance"],
                    "your CIN or LLPIN and pending forms.")
         + sources("Companies Act, 2013 (sections 92, 96, 137, 139, 164 and 173) and the Companies (Registration Offices and Fees) Rules; Limited Liability Partnership Act, 2008 and LLP Rules; MSME-1 and DPT-3 requirements; G.S.R. 943(E) on DIR-3 KYC; MCA General Circular 05/2026; ROC calendars from StudyCafe and LegalWiz; site form guides. Checked 26 November 2026.")),
    ],
    faqs=[("What is ROC compliance?", "ROC compliance is the set of filings a company or LLP makes with the Registrar of Companies on the MCA portal, such as the annual financial statements and annual return, plus event-based forms and the meetings and registers the law requires."),
          ("What are the ROC compliances for a private limited company?", "At least four board meetings, a statutory audit, an AGM by 30 September, AOC-4 within 30 days and MGT-7 / MGT-7A within 60 days of the AGM, ADT-1 within 15 days of appointing the auditor, DPT-3 by 30 June, MSME-1 half-yearly if dues to micro and small suppliers are outstanding, DIR-3 KYC every three years, and event-based forms such as DIR-12 and PAS-3."),
          ("What is the ROC compliance calendar for 2026-27?", "DIR-3 KYC and DPT-3 by 30 June, AGM by 30 September, AOC-4 within 30 days and MGT-7 / MGT-7A within 60 days of the AGM, MSME-1 by 31 October and 30 April, and for LLPs Form 11 by 30 May and Form 8 by 30 October."),
          ("What are the ROC compliances for an LLP?", "Form 11 (annual return) by 30 May, Form 8 (statement of account and solvency) by 30 October, an audit if turnover exceeds Rs 40 lakh or contribution exceeds Rs 25 lakh, DIR-3 KYC of designated partners every three years, and Form 3 / Form 4 within 30 days of changes."),
          ("How many board meetings must a private limited company hold?", "At least four a year with no more than 120 days between two meetings. A small company or OPC needs at least one meeting in each half of the calendar year, at least 90 days apart."),
          ("Is ROC compliance needed if the company has no business?", "Yes. Annual filings are due even with no transactions. A company with no business can apply for dormant status or close through strike-off instead of filing indefinitely."),
          ("What is the penalty for late ROC filing?", "An additional fee of Rs 100 a day of delay with no cap, plus possible penalties on the company and officers; directors can be disqualified if financial statements or annual returns are not filed for three continuous years."),
        ("What is the ROC late filing fee for AOC-4 and MGT-7, and is there a waiver in 2026?", "The additional fee is Rs 100 for every day of delay for each form, on top of the normal filing fee, with no upper cap; LLP Form 8 and Form 11 carry the same Rs 100 a day. Under MCA General Circular 05/2026, the additional fee for AOC-4 is waived for filings made by 31 December 2026 and for MGT-7 / MGT-7A by 31 January 2027, so companies with overdue FY 2025-26 accounts or annual returns should file inside those windows. LLP Form 8 is not covered. Separately, the Registrar can levy penalties on the company and its officers for continuing default."),
        ("What should I send to clear overdue ROC filings?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with: the company CIN or LLP LLPIN, the MCA master data showing which forms are pending, audited financial statements and the auditor's report for each year missed, AGM and board meeting dates, current director and shareholder details, and the DSC position of each director. We list every overdue form, work out the additional fee (and any waiver that still applies), and file AOC-4, MGT-7 / MGT-7A, ADT-1 or LLP Forms 8 and 11 in the right order."),
          ("What are the ROC compliance fees?", "The government filing fee for most MCA forms depends on the company's authorised share capital or the LLP's contribution, and late filing adds Rs 100 a day. Professional fees depend on the scope of work and are agreed upfront."),
          ("Can BQP handle our ROC compliance?", "Yes. CA Durgesh Chavda handles annual and event-based ROC filings for private limited companies, OPCs, LLPs and foreign-owned subsidiaries, including catch-up of missed years. " + C)],
    related=[("company-annual-filing-india-2026-aoc-4-mgt-7-due-date-fee-waiver-circular-05-2026-ccfs-status-check.html", "Company annual filing 2026"),
             ("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing"),
             ("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC every three years"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Foreign subsidiary compliance calendar"),
             ("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "Closing a company (STK-2)")],
    cta_h="ROC filings pending?", cta_b=C,
    keywords="roc compliance, roc compliance for private limited company, roc compliance for pvt ltd company, roc compliance for llp, roc compliance calendar 2026-27, roc compliance due date, roc compliance meaning, roc compliance fees, annual compliance private limited company, mca compliance calendar",
    desc="ROC compliance for private limited companies and LLPs in 2026-27: meaning, board meetings, AGM, AOC-4, MGT-7, ADT-1, DPT-3, MSME-1, DIR-3 KYC, LLP Form 11 and Form 8 due dates, event-based forms and the Rs 100 a day late fee.",
    howto={"name": "How to stay ROC compliant in a year", "description": "For private limited companies.", "steps": [
        {"name": "Hold board meetings", "text": "At least four, no more than 120 days apart."},
        {"name": "File DPT-3 and DIR-3 KYC", "text": "By 30 June (DIR-3 KYC once every three years)."},
        {"name": "Audit and hold the AGM", "text": "Adopt the audited accounts by 30 September."},
        {"name": "File AOC-4 and MGT-7", "text": "Within 30 and 60 days of the AGM."},
        {"name": "File MSME-1 and event forms", "text": "MSME-1 by 31 October and 30 April; DIR-12, PAS-3 and MGT-14 as events happen."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JK complete")
