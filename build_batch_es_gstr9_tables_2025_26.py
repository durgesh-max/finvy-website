# -*- coding: utf-8 -*-
"""Batch ES (21 Nov 2026): GSTR-9 and GSTR-9C for FY 2025-26 - which tables are mandatory and which are optional after
Notification No. 05/2026-Central Tax (26 October 2026), due 31 December 2026, late fee by turnover. Call-first page.
Facts (checked 21 Nov 2026; TaxGuru 'GSTR-9 and GSTR-9C for FY 2025-26: Table-Wise Reporting and Relaxations', 18 Nov
2026; CAclubindia 'GSTR-9 for FY 2025-26: What Changes Before the 31 December Due Date?', 18 Nov 2026; notification text
via TaxGuru copy):
- Notification 05/2026-Central Tax dated 26 October 2026, effective 1 November 2026, amends the GSTR-9 / GSTR-9C
  instructions so the existing optional reporting continues for '2025-26 onwards'; no new tables.
- Relaxations withdrawn from FY 2024-25 stay withdrawn: Table 6E (ITC on imports, inputs and capital goods separately),
  Table 7 (reversals row by row; no dumping into 7H), Tables 12 and 13 (ITC reversed / availed in the next year).
- Optional / consolidated: 5D and 5E together in 5D; 5H-5K (report 5A-5F net); 6B-6D inputs and input services together,
  capital goods separate; Tables 15, 16, 18. Mandatory: 4, 5A-5C, 5F, 5G, 6A, 6A1, 6E, 6H if applicable, 7, 8, 9, 10-11
  if applicable, 12-13 if applicable, 17 (HSN: 6-digit above INR 5 crore AATO, 4-digit B2B otherwise; rate change of
  22 September 2025 means the same HSN can appear at two rates).
- GSTR-9C: mandatory except Tables 5B-5N (report total in 5O) and Table 14. Self-certified. Above INR 5 crore.
- GSTR-9 required above INR 2 crore aggregate turnover (exempt up to INR 2 crore); due 31 December 2026 unless extended;
  cannot be revised.
- Late fee (Notification 07/2023-Central Tax): INR 50 a day up to INR 5 crore and INR 100 a day for INR 5-20 crore,
  each capped at 0.04% of turnover in the State; INR 200 a day above INR 20 crore, capped at 0.5%.
- Section 16(4) ITC cut-off 30 November 2026 or the date of filing GSTR-9 if earlier (site ITC page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026"

C = contact("your GSTINs, FY 2025-26 turnover, whether GSTR-9C applies, and any known differences between GSTR-1, GSTR-3B, GSTR-2B and your books")
PAGES = [dict(
    slug=SLUG,
    title="GSTR-9 and GSTR-9C for FY 2025-26: Mandatory vs Optional Tables After Notification 05/2026, Due 31 December 2026, Late Fee by Turnover",
    em="what you must fill this year and what you can still skip.",
    kicker="/ GST &middot; Annual return &middot; Due 31 December 2026 &middot; Updated 2026-11-21",
    lead=("The GST annual return <strong>GSTR-9</strong> and the reconciliation statement <strong>GSTR-9C</strong> for FY 2025-26 are due on <strong>31 December 2026</strong>. No extension has been announced. "
          "<strong>Notification No. 05/2026-Central Tax</strong> of 26 October 2026 keeps last year&rsquo;s optional tables optional for FY 2025-26 onwards and adds no new tables. "
          "The relaxations withdrawn from FY 2024-25 <strong>stay withdrawn</strong>: <strong>Table 6E</strong> (credit on imports), <strong>Table 7</strong> (reversals, row by row) and <strong>Tables 12 and 13</strong> (credit reversed or claimed in the next year) must be filled. "
          "GSTR-9 is required above <strong>INR 2 crore</strong> turnover and GSTR-9C above <strong>INR 5 crore</strong>. The late fee is <strong>INR 50, 100 or 200 a day</strong> depending on turnover. "
          "The return cannot be revised, and filing it early closes the window to claim FY 2025-26 input tax credit, which otherwise runs to 30 November 2026."),
    sections=[
        ("/ GSTR-9 tables", "Mandatory and optional for FY 2025-26.",
         table(["Table", "What it covers", "FY 2025-26"], [
             ["4", "Outward supplies, reverse-charge inward supplies, advances", "Mandatory"],
             ["5A-5C, 5F, 5G", "Zero-rated, SEZ, reverse-charge outward, non-GST, total", "Mandatory"],
             ["5D, 5E", "Exempt and nil-rated supplies", "Can be combined in 5D"],
             ["5H-5K", "Credit notes, debit notes, amendments", "Optional; report 5A-5F net of these"],
             ["6A, 6A1", "Credit as per GSTR-3B; last year&rsquo;s credit claimed this year", "Mandatory"],
             ["6B-6D", "Credit on inputs, input services, capital goods", "Inputs and input services can be combined; capital goods separate"],
             ["6E", "Credit on import of goods", "Mandatory; inputs and capital goods separately"],
             ["6H", "Credit reclaimed after an earlier reversal", "Mandatory if applicable"],
             ["7", "Credit reversed (Rules 37, 37A, 38, 39, 42, 43, section 17(5))", "Mandatory, row by row"],
             ["8, 9", "GSTR-2B credit vs credit availed; tax paid", "Mandatory"],
             ["10, 11", "FY 2025-26 supplies declared or amended up to November 2026", "Mandatory if applicable"],
             ["12, 13", "FY 2025-26 credit reversed or availed in FY 2026-27", "Mandatory if applicable"],
             ["15, 16, 18", "Demands and refunds; composition and deemed supplies; inward HSN", "Optional"],
             ["17", "HSN summary of outward supplies", "Mandatory; the 22 September 2025 rate change can put one HSN on two lines"]])
         + call_box("Our GSTR-9 and GSTR-9C for FY 2025-26", ["Reconciling GSTR-1, GSTR-3B, GSTR-2B and books before filing",
                                                              "Tables 6E, 7, 12 and 13, which can no longer be skipped",
                                                              "Unclaimed input tax credit before the 30 November cut-off",
                                                              "Shortfalls found now: paying through DRC-03 before a notice",
                                                              "GSTR-9C reconciliation and the rate-wise tax table"],
                    "GSTINs, turnover, GSTR-1 / 3B / 2B data or portal access, and your trial balance.")),
        ("/ GSTR-9C, late fee and what to do", "Before 31 December.",
         table(["Turnover", "Late fee a day (CGST plus SGST)", "Cap"], [
             ["Up to INR 5 crore", "INR 50", "0.04% of turnover in the State"],
             ["Above INR 5 crore up to INR 20 crore", "INR 100", "0.04% of turnover in the State"],
             ["Above INR 20 crore", "INR 200", "0.5% of turnover in the State"]])
         + ul("<strong>GSTR-9C:</strong> self-certified, above INR 5 crore. Everything is mandatory except the line-wise turnover adjustments in Tables 5B to 5N (put the total in 5O) and the expense-wise credit table (Table 14).",
              "<strong>Order of work:</strong> claim missed credit and make GSTR-1 amendments in the October returns filed by 30 November, before you file GSTR-9; see the <a href=\"gst-itc-last-date-30-november-2026-fy-2025-26-section-16-4-claim-before-cutoff.html\">30 November credit cut-off</a>.",
              "<strong>Reconcile first:</strong> use the <a href=\"gstr-9-pre-filing-audit-checklist-december-2026.html\">pre-filing checklist</a>; large differences in Table 8 are where notices usually start.",
              "<strong>Shortfall found:</strong> see <a href=\"discovered-gstr-9-shortfall-voluntary-disclosure-urgent-india.html\">voluntary payment before a notice</a>.",
              "<strong>Full guide:</strong> <a href=\"gstr-9-gstr-9c-annual-return-india-2026.html\">GSTR-9 and GSTR-9C explained</a>.")
         + '<p>Related: <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">deadline desk to 31 January 2027</a> &middot; <a href="gstr-9-fy-2024-25-december-2026-last-mile-checklist.html">GSTR-9 last-mile checklist</a>.</p>'
         + sources("Notification No. 05/2026-Central Tax dated 26 October 2026 (GSTR-9 and GSTR-9C instructions, FY 2025-26 onwards); Notification No. 07/2023-Central Tax (late fee); CGST Act sections 44 and 47 and rule 80; table-wise position as set out by TaxGuru (18 November 2026) and CAclubindia (18 November 2026). Check the GST portal for any extension of the due date before relying on 31 December.")),
    ],
    faqs=[("What is the due date for GSTR-9 for FY 2025-26?", "31 December 2026 for both GSTR-9 and GSTR-9C, unless the government extends it. No extension had been announced as of 21 November 2026."),
          ("Which GSTR-9 tables are optional for FY 2025-26?", "Under Notification 05/2026-Central Tax the earlier relaxations continue: exempt and nil-rated supplies can be combined in Table 5D, Tables 5H to 5K are optional, inputs and input services can be combined in Table 6, and Tables 15, 16 and 18 are optional."),
          ("Are Tables 12 and 13 of GSTR-9 mandatory?", "Yes, where applicable. The option to skip Tables 12 and 13, and the shortcuts in Tables 6E and 7, were withdrawn from FY 2024-25 and have not been restored for FY 2025-26."),
          ("What is the late fee for GSTR-9?", "INR 50 a day for turnover up to INR 5 crore and INR 100 a day for INR 5 to 20 crore, each capped at 0.04% of turnover in the State; INR 200 a day above INR 20 crore, capped at 0.5%."),
          ("Who must file GSTR-9C?", "Taxpayers with aggregate turnover above INR 5 crore. It is self-certified; Tables 5B to 5N and Table 14 remain optional."),
          ("Can BQP prepare our GSTR-9 and GSTR-9C?", "Yes. " + C)],
    related=[("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9 and GSTR-9C explained"), ("gstr-9-pre-filing-audit-checklist-december-2026.html", "GSTR-9 pre-filing checklist"),
             ("gst-itc-last-date-30-november-2026-fy-2025-26-section-16-4-claim-before-cutoff.html", "GST credit cut-off 30 November")],
    cta_h="GSTR-9 due on 31 December?", cta_b=C,
    keywords="GSTR-9 FY 2025-26 optional tables, Notification 05/2026 Central Tax GSTR-9, GSTR-9 due date 31 December 2026, GSTR-9 Table 12 13 mandatory, GSTR-9 Table 6E Table 7, GSTR-9C optional tables 5B 5N Table 14, GSTR-9 late fee 50 100 200",
    desc="GSTR-9 and GSTR-9C for FY 2025-26, due 31 December 2026: Notification 05/2026 keeps the optional tables (5D/5E, 5H-5K, 15, 16, 18); Tables 6E, 7, 12 and 13 stay mandatory; GSTR-9C optional 5B-5N and 14; late fee INR 50, 100 or 200 a day by turnover.",
    howto={"name": "How to prepare GSTR-9 for FY 2025-26", "description": "Before the 31 December 2026 due date.", "steps": [
        {"name": "Meet the 30 November cut-off", "text": "Claim missed credit and make GSTR-1 amendments in the October returns filed by 30 November."},
        {"name": "Reconcile", "text": "GSTR-1, GSTR-3B, GSTR-2B and books; explain differences."},
        {"name": "Fill the mandatory tables", "text": "Including 6E, 7 row by row, and 12 and 13 where applicable."},
        {"name": "Use the optional reporting", "text": "Combine 5D and 5E, net off 5H to 5K, skip 15, 16 and 18 if you wish."},
        {"name": "Pay shortfalls and file", "text": "Pay through DRC-03, then file GSTR-9 and GSTR-9C by 31 December."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ES complete")
