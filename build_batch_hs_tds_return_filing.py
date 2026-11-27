# -*- coding: utf-8 -*-
"""Batch HS (25 Nov 2026): TDS return filing for FY 2026-27 under the Income-tax Act, 2025 - new forms (138 salary,
140 other resident payments, 144 non-residents, 143 TCS replacing 24Q, 26Q, 27Q, 27EQ), quarterly due dates (31 July,
31 October, 31 January, 31 May; TCS Q4 reported as 15 May), payment dates (7th; March by 30 April), process (challan
allocation, return preparation and validation utilities, upload), late fee (Rs 200 a day), certificates (Form 130 / 131),
corrections, transition (Jan-Mar 2026 quarter in old forms).
Demand: sweep ac101 (25 Nov 2026), all 7 markets: "tds return filing date", "tds return filing due date for fy 2026-27",
"tds return filing utility", "tds return filing online", "tds return filing process step by step", "tds return filing fees".
Facts (checked 25 Nov 2026): Business Today (18 July 2026) on new forms, section codes and challan allocation; Taxguru
(Q1 tax year 2026-27 forms and due dates; 1961 Act for Q4 FY 2025-26); KoinX, GimBooks, Studycafe due-date calendars
(Q4 TCS 15 May per Studycafe); BankBazaar / TaxHeal on the Rs 200 a day late fee (section 427 per TaxHeal); site pages
(form numbers page; Form 16 -> 130, 16A -> 131)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee"

C = contact("whether you deduct tax on salary, contractor, professional, rent or non-resident payments, your TAN, which quarters are pending, and whether any return needs correction")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="TDS Return Filing FY 2026-27: Due Dates, New Forms 138, 140, 144 and 143, Step-by-Step Process, Late Fee (Maximum Cap) and Penalty",
    em="new form numbers, same quarterly rhythm.",
    kicker="/ Employers, businesses and deductors &middot; TDS &middot; Updated 2026-11-25",
    lead=("<strong>From tax year 2026-27, TDS returns are filed under the Income-tax Act, 2025 in new forms: Form 138 for salary (was 24Q), Form 140 for other payments to residents (was 26Q), Form 144 for payments to non-residents (was 27Q) and Form 143 for TCS (was 27EQ).</strong> "
          "Quarterly returns are due on 31 July, 31 October, 31 January and 31 May; the October-December 2026 return is due on 31 January 2027. "
          "Tax deducted must be paid by the 7th of the next month (March deductions by 30 April). A late return attracts a fee of &#8377;200 a day, so file on time even if the details need correcting later."),
    sections=[
        ("/ Quick answers", "What deductors search for.",
         ul("<strong>What is the TDS return due date for FY 2026-27?</strong> 31 July 2026 (April-June), 31 October 2026 (July-September), 31 January 2027 (October-December) and 31 May 2027 (January-March). TCS returns for January-March are reported as due on 15 May; check the notified date.",
            "<strong>Which form do I use?</strong> Form 138 for salary, Form 140 for other resident payments such as contractors, professionals, rent and interest, Form 144 for non-residents and Form 143 for TCS.",
            "<strong>What about the January-March 2026 quarter?</strong> It was the last filed in the old 24Q, 26Q and 27Q under the 1961 Act.",
            "<strong>Is there a fee to file?</strong> Filing online yourself has no government fee; the late fee is &#8377;200 for every day of delay.",
            "<strong>How do I file online?</strong> Prepare the return in the return preparation utility, validate it with the file validation utility, and upload it on the income tax e-filing portal with your TAN login (or through a facilitation centre).",
            "<strong>What certificates follow?</strong> Form 130 (was Form 16) for salary and Form 131 (was Form 16A) for other deductions, downloaded after the return is processed.")),
        ("/ Old vs new TDS return forms", "Tax year 2026-27 onwards.",
         table(["Payment", "Old form (1961 Act)", "New form (2025 Act)", "Certificate"], [
             ["Salary", "24Q", "Form 138", "Form 130 (was 16)"],
             ["Other payments to residents", "26Q", "Form 140", "Form 131 (was 16A)"],
             ["Payments to non-residents", "27Q", "Form 144", "Form 131 equivalent for non-residents"],
             ["Tax collected at source", "27EQ", "Form 143", "TCS certificate"]])
         + '<p>Full list: ' + L("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "old vs new income tax form numbers") + '.</p>'),
        ("/ Step by step", "Each quarter.",
         ul("<strong>1. Deduct and pay:</strong> deposit TDS by the 7th of the next month (30 April for March), and allocate each challan to the right form and section code so the return can match it.",
            "<strong>2. Collect deductee details:</strong> PAN, amounts, dates and section codes; for non-residents, treaty documents such as the TRC and Form 41.",
            "<strong>3. Prepare and validate:</strong> use the return preparation utility and the file validation utility to create the upload file.",
            "<strong>4. Upload:</strong> on the e-filing portal with the TAN login, verified electronically, before the due date.",
            "<strong>5. Issue certificates:</strong> Form 130 for salary after the year ends, Form 131 quarterly for other payments.",
            "<strong>6. Correct if needed:</strong> file a correction statement for wrong PANs, amounts or challan mismatches flagged after processing.")
         + '<p>Related: ' + L("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent under section 393") + ', ' + L("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "Form 144 for rent paid to NRIs") + ' and ' + L("india-tax-compliance-calendar-fy-2026-27-complete.html", "the FY 2026-27 compliance calendar") + '.</p>'
         + call_box("TDS return filing", ["Quarterly Forms 138, 140, 144 and 143",
                                         "Challan allocation and section codes",
                                         "Correction statements and defaults",
                                         "Form 130 / 131 certificates",
                                         "Non-resident TDS and treaty rates"],
                    "your TAN, payment types and pending quarters.")
         + sources("Income-tax Act, 2025 and Income-tax Rules, 2026 (TDS statements); Business Today, 18 July 2026; Taxguru on Q1 tax year 2026-27 forms and due dates; KoinX, GimBooks and Studycafe TDS / TCS calendars; BankBazaar and TaxHeal on the late fee. Confirm the notified dates and current utility versions before filing. Checked 25 November 2026.")),
    ],
    faqs=[("What are the TDS return due dates for FY 2026-27?", "31 July 2026 for April-June, 31 October 2026 for July-September, 31 January 2027 for October-December and 31 May 2027 for January-March. TCS returns for January-March are reported as due on 15 May."),
          ("Which forms replaced 24Q, 26Q and 27Q?", "From tax year 2026-27: Form 138 replaced 24Q (salary), Form 140 replaced 26Q (other resident payments), Form 144 replaced 27Q (non-residents), and Form 143 replaced 27EQ (TCS)."),
          ("What is the late fee for filing a TDS return late?", "Rs 200 for every day of delay until the return is filed, capped at the TDS amount reported in that return. Interest on late payment of TDS and penalties for not filing are separate."),
        ("What is the maximum late fee and penalty for a late TDS return?", "The late fee is Rs 200 for every day of delay, but the total fee for a return cannot exceed the TDS amount reported in it - so the cap is the tax deducted for that quarter, and the fee must be paid before the late return is accepted. Separately, the Assessing Officer can levy a penalty of Rs 10,000 to Rs 1 lakh for not filing the return or for filing wrong details (section 271H of the 1961 Act; section 461 of the Income-tax Act, 2025). For returns due from 1 April 2025, the penalty is generally not levied only if the TDS, late fee and interest are paid and the return is filed within one month of the due date - the earlier one-year window was cut to one month. Interest on TDS deducted or paid late runs on top. WhatsApp +91 78018 87130 with your TAN, the quarters pending and any default notice, and we work out the fee and interest and file the returns."),
          ("How do I file a TDS return online step by step?", "Pay TDS by the 7th of the next month and allocate challans, collect deductee PANs and section codes, prepare the return in the return preparation utility, validate it with the file validation utility, and upload it on the e-filing portal with your TAN login before the due date."),
        ("How do I check TDS return status online?", "Keep the token number (provisional receipt number) you get when the return is uploaded. Log in to TRACES (tdscpc.gov.in) as a deductor with your TAN, open the statement status option under Statements / Payments and search by financial year, quarter and form type, or by token number. A new return shows as Uploaded, then Accepted or Rejected, usually within a day or two, and later as Processed with or without defaults. Click the token number to see the rejection reasons or the acknowledgement."),
        ("What if my TDS return is rejected or processed with defaults?", "A rejected return is treated as not filed, so fix the error and upload it again as a regular return; the Rs 200 a day late fee keeps running until an accepted return is in. If it is processed with defaults (short deduction, short payment, late payment interest or late fee, PAN errors), download the justification report from TRACES, pay any amount due with a challan and file a correction return using the consolidated file and the original token number. CA Durgesh Chavda can review the default notice and file the correction."),
          ("When was the last TDS return filed in the old forms?", "The January-March 2026 quarter, filed by 31 May 2026, was the last in 24Q, 26Q and 27Q under the 1961 Act."),
          ("Can BQP file our TDS returns?", "Yes. CA Durgesh Chavda can file Forms 138, 140, 144 and 143, fix defaults and corrections, and issue Form 130 and 131 certificates. " + C)],
    related=[("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old vs new form numbers"),
             ("india-tax-compliance-calendar-fy-2026-27-complete.html", "FY 2026-27 compliance calendar"),
             ("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent FY 2026-27"),
             ("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "Form 144 for NRI rent"),
             ("section-194t-tds-partnership-firm-partners-india.html", "TDS on partner payments")],
    cta_h="TDS returns due or in default?", cta_b=C,
    keywords="TDS return filing, TDS return due date FY 2026-27, TDS return filing date, Form 138, Form 140, Form 144, Form 143, TDS return filing process, TDS return utility, TDS return late fee, 24Q 26Q replaced",
    desc="TDS return filing FY 2026-27: Forms 138 (salary), 140 (residents), 144 (non-residents), 143 (TCS) replace 24Q/26Q/27Q/27EQ; due 31 Jul, 31 Oct, 31 Jan, 31 May; payment by the 7th; Rs 200/day late fee; step-by-step.",
    howto={"name": "How to file a TDS return in 2026-27", "description": "Each quarter.", "steps": [
        {"name": "Deposit TDS", "text": "By the 7th of the next month (30 April for March), allocating challans by form and section."},
        {"name": "Collect deductee data", "text": "PAN, amounts, dates and section codes."},
        {"name": "Prepare and validate", "text": "Return preparation utility, then file validation utility."},
        {"name": "Upload before the due date", "text": "On the e-filing portal with the TAN login."},
        {"name": "Issue certificates", "text": "Form 130 for salary, Form 131 for other payments."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HS complete")
