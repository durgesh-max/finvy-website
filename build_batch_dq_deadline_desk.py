# -*- coding: utf-8 -*-
"""Batch DQ (19 Nov 2026): deadline desk 20 November 2026 - 31 January 2027 (call-first) and GST input tax credit cut-off
for FY 2025-26 (30 November 2026). Built to drive call bookings in the last-mile window.
Facts (checked 19 Nov 2026): CBDT Circular No. 07/2026 - tax audit report extended to 21 October 2026 and ITR for audit
(non-transfer-pricing) cases to 21 November 2026; transfer pricing cases unchanged - Form 3CEB 31 October 2026, ITR 30
November 2026 (Angel One, Taxscan, CAclubindia); MCA General Circular 05/2026 (24 October 2026) - no additional fee for
AOC-4 family filed by 31 December 2026 and MGT-7/7A by 31 January 2027 for FY 2025-26, otherwise fee from the original
due date (Studycafe, Corpseed); GSTR-9/9C for FY 2025-26 due 31 December 2026, portal opened 8 October 2026, no
extension reported (Taxscan, CAclubindia); section 16(4) CGST Act - ITC for FY 2025-26 cannot be taken after 30
November 2026 or the date of filing the annual return, whichever is earlier; GSTR-9 mandatory above INR 2 crore,
GSTR-9C above INR 5 crore; GSTR-3B for October due 20 November (monthly filers); belated and revised ITR for AY 2026-27
by 31 December 2026; FAST-DS 2026 declarations by 31 December 2026; ODI annual performance report by 31 December;
advance tax third instalment 15 December; TDS deposit 7th; Q3 TDS statements 31 January 2027."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."

DESK = "deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies"
ITC = "gst-itc-last-date-30-november-2026-fy-2025-26-section-16-4-claim-before-cutoff"

PAGES = []

C_DESK = contact("which deadline you are facing, your entity type (individual, NRI, company, LLP, foreign subsidiary) and what is pending")
PAGES.append(dict(
    slug=DESK,
    title="Deadline Desk: Every Income Tax, GST and ROC Due Date from 20 November 2026 to 31 January 2027 - For Indian Businesses, NRIs and Foreign-Owned Companies",
    em="what is due, what was extended, and what happens if you miss it.",
    kicker="/ Deadlines &middot; Income tax &middot; GST &middot; ROC &middot; Updated 2026-11-19",
    lead=("The next ten weeks hold the biggest cluster of Indian deadlines in the year. <strong>20 November</strong>: GSTR-3B for October. <strong>21 November</strong>: income-tax returns for tax-audit cases, extended from 31 October by CBDT Circular 07/2026. <strong>30 November</strong>: returns for transfer-pricing cases (not extended) and the <strong>last date to claim GST input tax credit for FY 2025-26</strong>. <strong>15 December</strong>: advance tax. <strong>31 December</strong>: belated and revised returns for AY 2026-27, GSTR-9 and GSTR-9C, the end of the AOC-4 fee waiver, FAST-DS 2026 foreign-asset declarations and the ODI annual performance report. <strong>31 January 2027</strong>: the end of the MGT-7 fee waiver and Q3 TDS statements. "
          "Missing these means late fees, interest, lost input tax credit or refunds, and in some cases penalties or prosecution exposure. If any of them is yours, <strong>book a call</strong> and we will tell you what can still be filed, in what order, and what it will cost to fix."),
    sections=[
        ("/ The calendar", "20 November 2026 to 31 January 2027.",
         table(["Date", "What", "Who", "If missed"], [
             ["20 November 2026 (passed)", "GSTR-3B for October (monthly filers)", "GST-registered businesses", "Late fee and 18% interest; last regular return in which FY 2025-26 ITC can be claimed"],
             ["21 November 2026", "ITR for tax-audit cases (not transfer pricing), extended by CBDT Circular 07/2026", "Companies, firms and individuals with tax audit", "Belated return by 31 December with fee and interest; some deductions and loss carry-forward lost"],
             ["30 November 2026", "ITR for transfer-pricing cases (no extension); master file where applicable", "Companies with international or specified domestic transactions, including foreign-owned subsidiaries", "Same as above, plus transfer pricing penalty exposure"],
             ["30 November 2026", "Last date to claim GST input tax credit for FY 2025-26 (section 16(4))", "Every GST-registered business", "Credit lost permanently"],
             ["30 November 2026", "Liaison office annual statement (Form 49C) for FY 2025-26, per current guidance", "Foreign companies' liaison offices", "Penalty exposure"],
             ["30 November 2026", "Pensioners' annual life certificate (<a href=\"nri-pensioner-life-certificate-from-abroad-30-november-2026-indian-pension-tax-dtaa.html\">from abroad too</a>)", "Pensioners, including those living outside India", "December pension held until it is submitted"],
             ["7 December 2026", "TDS and TCS deposit for November", "All deductors", "Interest and disallowance"],
             ["15 December 2026", "Advance tax, third instalment (75% cumulative)", "Businesses, NRIs with Indian income above the threshold", "Interest under the advance-tax provisions"],
             ["28 December 2026", "EPFO VISHWAS 2026: apply to settle damages on provident fund paid late before 14 June 2024 (<a href=\"epfo-vishwas-2026-pf-damages-settlement-reduced-rates-last-date-28-december-2026.html\">guide</a>)", "Employers with past late PF payments", "Regular damages of up to 37% a year; no extension expected"],
             ["31 December 2026", "Belated and revised ITR for AY 2026-27", "Anyone who missed or needs to correct a return, including NRIs claiming refunds", "Only an updated return afterwards, with additional tax and no refund"],
             ["31 December 2026", "GSTR-9 and GSTR-9C for FY 2025-26 (<a href=\"gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html\">mandatory vs optional tables</a>)", "Turnover above INR 2 crore (9C above INR 5 crore)", "Late fee of INR 50 to 200 a day by turnover; notices on mismatches"],
             ["31 December 2026", "AOC-4 without additional fee (General Circular 05/2026)", "Companies that missed 30 October", "Additional fee from the original due date"],
             ["31 December 2026", "FAST-DS 2026 foreign-asset declarations", "Residents with undisclosed foreign assets or income", "Black Money Act exposure"],
             ["31 December 2026", "ODI annual performance report", "Indian entities and residents with overseas direct investment", "Late submission fee; restrictions on new ODI"],
             ["31 January 2027", "MGT-7 / MGT-7A without additional fee; Q3 TDS statements", "Companies; deductors", "Additional fee from the original due date; TDS late fee"]])
         + call_box("an upcoming deadline", ["Which of these deadlines apply to you and which are already missed",
                                              "What can still be filed, and the cheapest order to fix things",
                                              "Late fee, interest and penalty exposure in rupees",
                                              "Documents we need and how quickly we can file",
                                              "For NRIs and foreign-owned companies: refunds, treaty claims and FEMA filings"],
                    "your PAN or company name, the deadline you are worried about, and what has been filed so far.")),
        ("/ NRIs and foreign-owned companies", "What is most often missed.",
         ul("<strong>NRIs:</strong> a belated return by 31 December 2026 is the last chance to claim refunds of TDS on NRO interest, rent and property sales for FY 2025-26; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR for NRIs</a> and <a href=\"nri-missed-itr-deadline-what-to-do-india.html\">NRI missed the deadline</a>.",
            "<strong>Returning NRIs:</strong> foreign assets missed in Schedule FA can be declared under FAST-DS 2026 by 31 December; see <a href=\"fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html\">FAST-DS 2026</a>.",
            "<strong>Foreign-owned subsidiaries:</strong> transfer-pricing returns by 30 November, AOC-4 by 31 December and MGT-7 by 31 January within the fee waiver; see <a href=\"foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html\">subsidiary compliance calendar</a>.",
            "<strong>Indian groups with overseas investment:</strong> ODI annual performance report by 31 December.")),
        ("/ Detailed guides", "One page per deadline.",
         ul("<a href=\"itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html\">ITR for audit cases: 21 November 2026</a>",
            "<a href=\"form-3ceb-tp-audit-india-2026-30-november-checklist.html\">Transfer pricing: Form 3CEB and the 30 November return</a>",
            "<a href=\"" + ITC + ".html\">GST input tax credit cut-off: 30 November 2026</a>",
            "<a href=\"gstr-9-fy-2024-25-december-2026-last-mile-checklist.html\">GSTR-9 for FY 2025-26: 31 December 2026</a>",
            "<a href=\"belated-itr-31-december-2026-section-139-4-india.html\">Belated return: 31 December 2026</a> &middot; <a href=\"revised-itr-section-139-5-deadline-31-december-2026-india.html\">revised return</a>",
            "<a href=\"aoc-4-filing-deadline-30-october-2026-late-fee-india.html\">AOC-4 fee waiver to 31 December</a> &middot; <a href=\"mgt-7-mgt-7a-annual-return-29-november-2026-india.html\">MGT-7 fee waiver to 31 January 2027</a>",
            "<a href=\"november-2026-compliance-calendar-india-tax-gst-mca.html\">November 2026 compliance calendar</a>")
         + sources("CBDT Circular No. 07/2026 (AY 2026-27 due dates); MCA General Circular 05/2026 dated 24 October 2026; CGST Act, 2017, section 16(4) and GSTR-9/9C notifications; Black Money (Undisclosed Foreign Income and Assets) and FAST-DS 2026 scheme notifications; RBI overseas investment directions. Reports checked 19 November 2026: Angel One, Taxscan, CAclubindia, Studycafe, Corpseed. Check the portals for any further extension before relying on a date.")),
    ],
    faqs=[("What is the ITR due date for audit cases for AY 2026-27?", "21 November 2026, extended from 31 October by CBDT Circular 07/2026. Transfer-pricing cases were not extended and remain due on 30 November 2026."),
          ("What is the last date to claim GST input tax credit for FY 2025-26?", "30 November 2026, or the date you file the FY 2025-26 annual return if earlier (section 16(4) of the CGST Act)."),
          ("Has the AOC-4 or MGT-7 due date been extended?", "MCA General Circular 05/2026 waives the additional fee if AOC-4 is filed by 31 December 2026 and MGT-7/7A by 31 January 2027 for FY 2025-26; filed later, the fee runs from the original due date."),
          ("What is the last date for a belated or revised ITR for AY 2026-27?", "31 December 2026. After that only an updated return is possible, with additional tax and no refund."),
          ("What is due on 31 December 2026?", "Belated and revised ITRs, GSTR-9 and GSTR-9C for FY 2025-26, AOC-4 within the fee waiver, FAST-DS 2026 declarations and the ODI annual performance report."),
          ("Can BQP handle a last-minute filing?", "Yes. " + C_DESK)],
    related=[("itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html", "ITR for audit cases: 21 November"), ("belated-itr-31-december-2026-section-139-4-india.html", "Belated return by 31 December"),
             ("november-2026-compliance-calendar-india-tax-gst-mca.html", "November 2026 compliance calendar")],
    cta_h="Facing one of these deadlines?", cta_b=C_DESK,
    keywords="due dates November December 2026 India, ITR due date 21 November 2026, transfer pricing ITR 30 November 2026, GST ITC last date 30 November 2026, GSTR-9 31 December 2026, AOC-4 MGT-7 fee waiver 2026, belated ITR 31 December 2026, NRI deadlines December 2026",
    desc="Deadline desk 20 Nov 2026 - 31 Jan 2027: GSTR-3B 20 Nov; audit ITR 21 Nov (Circular 07/2026); TP ITR and GST ITC cut-off 30 Nov; advance tax 15 Dec; belated/revised ITR, GSTR-9/9C, AOC-4 fee waiver, FAST-DS and ODI APR 31 Dec; MGT-7 fee waiver 31 Jan 2027; NRI and foreign-company points.",
    howto={"name": "How to clear year-end Indian deadlines", "description": "From 20 November 2026 to 31 January 2027.", "steps": [
        {"name": "List what applies", "text": "Income tax, GST, ROC and FEMA deadlines for your entity."},
        {"name": "Do the money-losing items first", "text": "GST ITC by 30 November and refund-bearing returns before 31 December."},
        {"name": "File within waivers", "text": "AOC-4 by 31 December and MGT-7 by 31 January to avoid additional fees."},
        {"name": "Fix missed items", "text": "Belated or revised returns, FAST-DS declarations, late FEMA filings."},
        {"name": "Plan the next quarter", "text": "Advance tax, TDS and the FY 2026-27 calendar under the new Act."}]}))

C_ITC = contact("your GSTIN, filing frequency (monthly or quarterly), and whether GSTR-2B and your books are reconciled for FY 2025-26")
PAGES.append(dict(
    slug=ITC,
    title="GST Input Tax Credit Last Date for FY 2025-26: 30 November 2026 Under Section 16(4) - What to Claim, Reconcile and Fix Before the Cut-Off",
    em="credit not claimed by then is lost.",
    kicker="/ GST &middot; Input tax credit &middot; Deadline &middot; Updated 2026-11-19",
    lead=("Input tax credit on purchases relating to <strong>FY 2025-26</strong> must be claimed by <strong>30 November 2026</strong>, or by the date you file the FY 2025-26 annual return (GSTR-9) if that is earlier. This is the rule in <strong>section 16(4) of the CGST Act</strong>, and credit not claimed by then is <strong>lost permanently</strong>. "
          "For monthly filers, the practical vehicle is the <strong>October 2026 GSTR-3B</strong>, due on 20 November and acceptable for this purpose if filed by 30 November. Before filing, reconcile your purchase register with <strong>GSTR-2B</strong>, chase suppliers who have not filed GSTR-1, and claim missed credits and credit notes. Reverse credit on invoices unpaid beyond 180 days. "
          "Filing GSTR-9 early closes the window early, so finish the credit review first."),
    sections=[
        ("/ The cut-off in practice", "What to do in the next ten days.",
         table(["Step", "What to check", "Why it matters"], [
             ["Reconcile with GSTR-2B", "Purchase register vs GSTR-2B for April 2025 to March 2026", "Only credits reflected in GSTR-2B can generally be claimed"],
             ["Chase suppliers", "Invoices missing from GSTR-2B because suppliers did not file GSTR-1", "If they file before your return, the credit can still flow"],
             ["Claim missed credits", "Invoices received late, debit notes, import IGST (ICEGATE)", "Last chance for FY 2025-26"],
             ["Reverse where required", "Unpaid invoices beyond 180 days, blocked credits, exempt use", "Avoid interest and notices"],
             ["File the right return", "October GSTR-3B (monthly) by 30 November; quarterly filers check which return carries the credit", "Credit claimed after 30 November is invalid"],
             ["Then GSTR-9", "Annual return for FY 2025-26 by 31 December 2026", "Filing it earlier ends the credit window earlier"]])
         + call_box("GST input tax credit before 30 November", ["A quick reconciliation of your FY 2025-26 credit against GSTR-2B",
                                                                 "Which missed credits can still be claimed and in which return",
                                                                 "Reversals that avoid notices later",
                                                                 "GSTR-9 and GSTR-9C preparation for 31 December",
                                                                 "Exporters: refunds of unutilised credit"],
                    "your GSTIN, purchase register and GSTR-2B downloads for FY 2025-26.")),
        ("/ Questions businesses ask", "Common edge cases.",
         ul("<strong>Credit notes and debit notes:</strong> the 30 November limit also applies to debit notes relating to FY 2025-26; check the date on the debit note under current rules.",
            "<strong>Import IGST:</strong> claim credit on bills of entry for FY 2025-26 before the cut-off; reconcile with ICEGATE data.",
            "<strong>Quarterly (QRMP) filers:</strong> the return that can carry FY 2025-26 credit must be filed by 30 November 2026; confirm the filing route before the date.",
            "<strong>Suppliers who never filed:</strong> credit generally cannot be claimed; pursue the supplier for tax and keep evidence of payment.",
            "<strong>After the cut-off:</strong> credit cannot be claimed in GSTR-9 itself; the annual return only reports what was claimed.")
         + '<p>Related: <a href="' + DESK + '.html">deadline desk to 31 January 2027</a> &middot; <a href="gstr-9-fy-2024-25-december-2026-last-mile-checklist.html">GSTR-9 for FY 2025-26</a> &middot; <a href="gstr-9-pre-filing-audit-checklist-december-2026.html">GSTR-9 pre-filing checklist</a> &middot; <a href="gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html">GST changes from 1 November 2026</a>.</p>'
         + sources("CGST Act, 2017, section 16(2) and 16(4) (as amended by the Finance Act, 2022) and rule 36(4)/37 of the CGST Rules; GSTN advisories on GSTR-9/9C for FY 2025-26 (portal opened 8 October 2026). Reports checked 19 November 2026: Taxscan, CAclubindia. General information; confirm your filing route before the date.")),
    ],
    faqs=[("What is the last date to claim ITC for FY 2025-26?", "30 November 2026, or the date of filing the FY 2025-26 annual return if earlier, under section 16(4) of the CGST Act."),
          ("In which return should FY 2025-26 ITC be claimed?", "For monthly filers, usually the October 2026 GSTR-3B, due 20 November and accepted for this purpose if filed by 30 November 2026."),
          ("Can missed ITC be claimed in GSTR-9?", "No. GSTR-9 only reports credit already claimed in returns; credit not claimed by the cut-off is lost."),
          ("Does filing GSTR-9 early affect the ITC deadline?", "Yes. The window closes on the earlier of 30 November and the date the annual return is filed, so finish the credit review before filing GSTR-9."),
          ("What if my supplier has not filed GSTR-1?", "The credit generally will not appear in GSTR-2B and cannot be claimed; follow up with the supplier before the cut-off."),
          ("Can BQP review our ITC before 30 November?", "Yes. " + C_ITC)],
    related=[(DESK + ".html", "Deadline desk to 31 January 2027"), ("gstr-9-fy-2024-25-december-2026-last-mile-checklist.html", "GSTR-9 for FY 2025-26"),
             ("gstr-9-pre-filing-audit-checklist-december-2026.html", "GSTR-9 pre-filing checklist")],
    cta_h="Worried about losing GST credit?", cta_b=C_ITC,
    keywords="GST ITC last date FY 2025-26, ITC claim deadline 30 November 2026, section 16(4) time limit, last date to claim input tax credit 2026, GSTR-2B reconciliation November 2026, October GSTR-3B ITC FY 2025-26",
    desc="GST input tax credit for FY 2025-26 must be claimed by 30 November 2026 (or GSTR-9 filing if earlier) under section 16(4): reconcile with GSTR-2B, chase suppliers, claim missed credits in the October GSTR-3B, reverse where needed, then file GSTR-9 by 31 December.",
    howto={"name": "How to secure FY 2025-26 input tax credit before 30 November 2026", "description": "Last-mile steps.", "steps": [
        {"name": "Reconcile", "text": "Purchase register vs GSTR-2B for FY 2025-26."},
        {"name": "Chase suppliers", "text": "Get missing GSTR-1 filings before your return."},
        {"name": "Claim and reverse", "text": "Claim missed credits; reverse unpaid or blocked credits."},
        {"name": "File by 30 November", "text": "October GSTR-3B (monthly) or the applicable return."},
        {"name": "File GSTR-9 after", "text": "Annual return by 31 December 2026."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DQ complete:", len(PAGES))
