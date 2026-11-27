# -*- coding: utf-8 -*-
"""Batch JP (27 Nov 2026): TDS default notice - TRACES default summary / intimation, the password to open it, and how
to clear short payment, short deduction, interest, late fee and PAN errors.
Demand: sweep ac126 (27 Nov 2026), all 7 markets: "tds default notice", "tds default notice password", "password to open
tds default notice", "tds default summary"; no existing page title targeted it.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - deductors with a default need a correction filed.
Facts (verified 27 Nov 2026): intimation after processing the TDS / TCS statement (section 200A of the 1961 Act), sent
within one year from the end of the FY in which the statement was filed; intimation password = first four characters of
the TAN in capitals + '_' + date of filing of the regular statement (DDMMYYYY); justification report requested on TRACES
(Communications), password starts 'JR_' followed by TAN, form, quarter and year; interest 1% a month for late deduction
and 1.5% a month for late payment (old 201(1A), month or part of a month); late fee Rs 200 a day for a late statement,
now section 427 of the 2025 Act (old 234E), with a cap; correction statement using the consolidated file from TRACES;
site pages: Form 141 (old 26QB) for property buyers, PAN + Form 141 for resident individual / HUF buyers from an NRI from
1 October 2026. No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "tds-default-notice-traces-default-summary-password-how-to-clear-short-payment-interest-late-fee-2026"

C = contact("the default notice or intimation PDF, your TAN (or PAN if you bought property), the form and quarter, the challans paid, the TDS statement you filed and its token number, and the justification report if you have downloaded it")
PAGES = [dict(
    slug=SLUG,
    title="TDS Default Notice (2026): What the TRACES Default Summary Means, the Password to Open It, and How to Clear Short Payment, Interest and Late Fee",
    em="find the default, pay or correct, close it on TRACES.",
    kicker="/ Companies, firms, landlords' tenants and property buyers &middot; TRACES &middot; Updated 2026-11-27",
    lead=("<strong>A TDS default notice is the intimation sent after your TDS statement is processed: it lists the amount the system says is still due - short payment, short deduction, interest on late deduction or payment, the late filing fee or PAN errors.</strong> "
          "Many defaults are not real tax shortfalls but mismatches: a challan tagged to the wrong quarter, a wrong PAN, or a deduction at a lower rate without the certificate being quoted. "
          "The fix is the same each time: download the details from TRACES, pay what is genuinely due, and file a correction statement for the rest."),
    sections=[
        ("/ Opening the notice", "Passwords and where to find the details.",
         ul("<strong>Intimation password:</strong> the first four characters of your TAN in capital letters, an underscore, then the date the regular statement was filed as DDMMYYYY (for TAN ABCD12345E and a statement filed on 15 July 2026: ABCD_15072026).",
            "<strong>Default summary:</strong> log in to TRACES with your TAN and check the statement status and defaults for the form and quarter.",
            "<strong>Justification report:</strong> request it on TRACES under Communications; it shows each default line by line. Its password starts with JR_ followed by the TAN, form, quarter and year.",
            "<strong>Timing:</strong> the intimation is sent within one year from the end of the financial year in which the statement was filed.")),
        ("/ What the default means", "The usual default types.",
         table(["Default", "What it means", "How it is cleared"], [
             ["Short payment", "Tax shown as deducted is more than the challans matched to the statement", "Tag the right challan in a correction statement, or pay the shortfall by a new challan and add it"],
             ["Short deduction", "Deducted at a lower rate than the system expects", "Quote the lower TDS certificate (Form 128, old Form 13) or the PAN / treaty basis in a correction, or pay the difference"],
             ["Interest on late deduction", "Tax deducted after the date it was due", "1% a month or part of a month from the due date of deduction to the date of deduction"],
             ["Interest on late payment", "Tax deposited after the due date", "1.5% a month or part of a month from the date of deduction to the date of payment"],
             ["Late filing fee", "Statement filed after the due date", "Rs 200 a day under section 427 of the 2025 Act (old 234E), with a cap; paid by challan and added in a correction"],
             ["PAN errors", "Invalid or missing PAN for a deductee", "Correct the PAN in a correction statement; without a valid PAN the higher rate applies"]])),
        ("/ Property buyers and tenants", "Defaults are not only for businesses.",
         ul("<strong>Property bought from a resident:</strong> 1% TDS on Rs 50 lakh or more is reported in Form 141 (old 26QB) against the buyer's PAN; late filing or late payment leads to interest and late-fee demands on TRACES.",
            "<strong>Property bought from an NRI:</strong> TDS applies to the whole price; from 1 October 2026 a resident individual or HUF buyer can use a PAN and Form 141 instead of a TAN. Short deduction or missing returns lead to defaults in the buyer's name.",
            "<strong>Rent paid to an NRI landlord:</strong> the tenant deducts on every payment and files quarterly statements; missed quarters show as defaults.")
         + call_box("TDS defaults", ["Reading the default summary and justification report",
                                     "Challan tagging and correction statements",
                                     "Lower-certificate and PAN corrections",
                                     "Interest and late-fee payment",
                                     "Property buyer (Form 141) defaults"],
                    "the notice PDF, TAN or PAN, the quarter and challans.")
         + sources("Income-tax Act, 1961 (sections 200A, 201(1A), 234E) and Income-tax Act, 2025 (sections 393, 427); TRACES user guidance on intimations and justification reports; site TDS return, Form 131 and property TDS guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a TDS default notice?", "It is the intimation issued after your TDS or TCS statement is processed, showing any amount still due: short payment, short deduction, interest on late deduction or payment, the late filing fee or PAN errors. It is sent within one year from the end of the financial year in which the statement was filed."),
          ("What is the password to open a TDS default notice?", "For the intimation, the first four characters of your TAN in capital letters, an underscore, then the filing date of the regular statement as DDMMYYYY - for example ABCD_15072026. The justification report has its own password starting with JR_ followed by the TAN, form, quarter and year."),
          ("What is a TDS default summary on TRACES?", "The summary of defaults for a TAN, form and quarter shown on TRACES after processing. The justification report, requested under Communications, breaks each default down line by line."),
          ("How do I clear a TDS default?", "Download the justification report, check which defaults are real, pay any genuine shortfall, interest or late fee by challan, and file a correction statement using the consolidated file from TRACES - re-tagging challans, correcting PANs or quoting lower deduction certificates for the rest."),
        ("How do I reply to a TDS demand notice I disagree with?", "A demand from processing your TDS statement (the 200A intimation) is answered by correcting the statement, not by a letter: download the justification report, then file a correction statement within the two-year window to fix wrong PANs, re-tag challans, quote a lower deduction certificate or show the treaty rate where the payee gave a TRC and Form 41. Pay only the genuine shortfall, interest and late fee. If an Assessing Officer has instead issued a notice or order treating you as an assessee in default for not deducting, reply to that notice with the payee's details and, where the payee has declared the income and paid tax, the accountant's certificate (old Form 26A) - and appeal the order if needed."),
          ("What is the interest and late fee for TDS defaults?", "Interest is 1% a month (or part of a month) for late deduction and 1.5% a month for late payment. A late statement attracts a fee of Rs 200 a day under section 427 of the 2025 Act (old 234E), subject to a cap."),
          ("What should I send to clear a TDS default?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the default notice or intimation PDF, your TAN (or PAN for a property purchase), the form and quarter, the challans paid, the statement you filed with its token number, and the justification report if downloaded. We check each default, separate real shortfalls from mismatches and file the correction."),
          ("Can BQP clear TDS defaults for my company or property purchase?", "Yes. CA Durgesh Chavda works online with companies, foreign subsidiaries and individual buyers and tenants. " + C)],
    related=[("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing FY 2026-27"),
             ("form-16a-now-form-131-tds-certificate-2026-download-traces-due-dates-form-130-vs-131.html", "Form 131 (old 16A) and TRACES downloads"),
             ("buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", "Buying property from an NRI: Form 141"),
             ("income-tax-notice-for-property-land-purchase-why-you-got-it-how-to-reply-source-of-funds-2026.html", "Income tax notice after a property purchase"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice")],
    cta_h="Got a TDS default notice?", cta_b=C,
    keywords="tds default notice, tds default notice password, password to open tds default notice, tds default summary, traces default, tds intimation 200a, justification report password, tds short payment, tds late fee 234e",
    desc="TDS default notice: what the TRACES default summary and intimation mean, the password to open them (TAN first four characters + filing date), and how to clear short payment, short deduction, interest, the Rs 200 a day late fee and PAN errors with a correction statement.",
    howto={"name": "How to clear a TDS default", "description": "From the notice to a closed default on TRACES.", "steps": [
        {"name": "Open the notice", "text": "Use the TAN-based password and check the default summary on TRACES."},
        {"name": "Get the justification report", "text": "Request it under Communications to see each default."},
        {"name": "Pay what is due", "text": "Pay genuine shortfall, interest or late fee by challan."},
        {"name": "File a correction", "text": "Re-tag challans, fix PANs or quote certificates in a correction statement."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JP complete")
