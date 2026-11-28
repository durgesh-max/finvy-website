# -*- coding: utf-8 -*-
"""Batch JE (25 Nov 2026): Form 16A, now Form 131 - the TDS certificate for payments other than salary under the
Income-tax Rules, 2026 (from tax year 2026-27). Issued quarterly by the deductor from TRACES within 15 days after the
due date of the quarterly TDS statement (Q1 by 15 August, Q2 by 15 November, Q3 by 15 February, Q4 by 15 June);
Form 130 (old Form 16) for salary is annual (first due 15 June 2027). Recipients match it with Form 168 (old 26AS) and
AIS; mismatches are fixed by the deductor correcting the TDS statement; late issue attracts a daily penalty (no
amount stated). Quarterly statements: Forms 138 / 140 / 144 / 143.
Demand: sweep ac116 (25 Nov 2026), 5 markets: "form 16a"; plus 'form 16' family searches.
Facts (checked 25 Nov 2026): site TDS return, TDS rate chart, form-number mapping and compliance calendar pages
(Form 131 for July-September 2026 due 15 November 2026)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "form-16a-now-form-131-tds-certificate-2026-download-traces-due-dates-form-130-vs-131"

C = contact("whether you are the deductor or the recipient, your TAN or PAN, the quarter and the payment type, and any mismatch you see in Form 168 (26AS) or AIS")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Form 16A Is Now Form 131 (2026): TDS Certificate for Non-Salary Payments, Quarterly Due Dates, How to Download from TRACES and Form 130 vs 131",
    em="same certificate, new number from tax year 2026-27.",
    kicker="/ Deductors, freelancers, landlords and NRIs &middot; TDS certificates &middot; Updated 2026-11-25",
    lead=("<strong>From tax year 2026-27, Form 16A, the TDS certificate for payments other than salary (rent, professional fees, interest, commission and similar payments), is called Form 131 under the Income-tax Rules, 2026.</strong> "
          "The deductor downloads it from TRACES and must issue it every quarter within 15 days after the TDS return is due, for example by 15 November 2026 for July to September 2026. "
          "Salary TDS gets a separate annual certificate, Form 130 (formerly Form 16)."),
    sections=[
        ("/ Form 131 at a glance", "Who issues it, when and for what.",
         table(["Point", "Form 131 (old Form 16A)", "Form 130 (old Form 16)"], [
             ["Covers", "TDS on payments other than salary", "TDS on salary"],
             ["Issued by", "Any deductor (company, firm, tenant, bank)", "Employer"],
             ["Frequency", "Quarterly", "Annual"],
             ["Due date", "15 days after the quarterly TDS statement is due", "15 June after the tax year (first: 15 June 2027)"],
             ["Source", "Downloaded from TRACES", "Downloaded from TRACES (Part A) plus employer details"]])
         + table(["Quarter (tax year 2026-27)", "Form 131 due by"], [
             ["April to June 2026", "15 August 2026"],
             ["July to September 2026", "15 November 2026"],
             ["October to December 2026", "15 February 2027"],
             ["January to March 2027", "15 June 2027"]])
         + '<p>All renamed forms: ' + L("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "old vs new form numbers") + '. Filing the quarterly statements: ' + L("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing (Forms 138, 140, 144, 143)") + '.</p>'),
        ("/ How to download and check Form 131", "For deductors and recipients.",
         ul("<strong>Deductor:</strong> file the quarterly TDS statement, log in to TRACES with the TAN, request the certificate for the quarter and download it once generated; certificates should be the TRACES-generated ones.",
            "<strong>Recipient:</strong> compare each Form 131 with Form 168 (old 26AS) and the Annual Information Statement before filing your return; see " + L("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "fixing AIS mismatches") + ".",
            "<strong>Mismatch:</strong> if TDS is missing or wrong, the deductor must file a correction statement; until then the credit may not appear.",
            "<strong>Late issue:</strong> deductors face a daily penalty for issuing certificates late, besides late fees for the return itself.",
            "<strong>Rates and thresholds:</strong> see the " + L("tds-rate-chart-fy-2026-27-section-393-income-tax-act-2025-old-sections-194c-194j-194i-thresholds.html", "TDS rate chart for 2026-27") + "; salary TDS: " + L("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary and Form 130") + ".")
         + call_box("TDS compliance", ["Quarterly TDS statements and Form 131",
                                        "Form 130 for employees",
                                        "Correction statements and mismatches",
                                        "Lower or nil TDS certificates",
                                        "TDS refunds for NRIs and freelancers"],
                    "your TAN or PAN and the quarter.")
         + sources("Income-tax Act, 2025 and Income-tax Rules, 2026 (TDS certificates); TRACES; site TDS return, TDS rate chart, form-number mapping and compliance calendar guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is Form 16A called now?", "From tax year 2026-27, Form 16A is Form 131 under the Income-tax Rules, 2026. It is the TDS certificate for payments other than salary."),
          ("When is Form 131 (Form 16A) due?", "Quarterly, within 15 days after the due date of the quarterly TDS statement: by 15 August, 15 November, 15 February and 15 June for the four quarters of tax year 2026-27."),
          ("What is the difference between Form 130 and Form 131?", "Form 130 (formerly Form 16) is the annual salary TDS certificate from the employer; Form 131 (formerly Form 16A) is the quarterly certificate for other payments such as rent, fees, interest and commission."),
          ("How do I download Form 131?", "The deductor downloads it from TRACES with its TAN after filing the quarterly TDS statement and gives it to you. As a recipient you can check the same TDS in Form 168 (old 26AS) and AIS."),
          ("What if TDS in Form 131 does not match Form 26AS / Form 168?", "Ask the deductor to file a correction statement; the credit appears only once the corrected statement is processed."),
        ("Can I file my ITR without Form 16 (now Form 130)?", "Yes. Form 16 (Form 130 from tax year 2026-27) only summarises salary and TDS; it is not required to file the return. Work out salary from your payslips, check the TDS your employer deposited in Form 26AS (now Form 168) and the AIS, claim only exemptions and deductions you can support, and pay any balance tax before filing. If the employer deducted tax but did not deposit it or issue the certificate, ask in writing and keep the payslips as evidence. Book a call to file the return correctly without the certificate."),
          ("Can BQP handle TDS returns and certificates?", "Yes. CA Durgesh Chavda files quarterly TDS statements, issues Forms 130 and 131, fixes mismatches and applies for lower TDS certificates. " + C)],
    related=[("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing"),
             ("tds-rate-chart-fy-2026-27-section-393-income-tax-act-2025-old-sections-194c-194j-194i-thresholds.html", "TDS rate chart 2026-27"),
             ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old vs new form numbers"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary and Form 130"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower TDS certificate")],
    cta_h="TDS certificates to issue or fix?", cta_b=C,
    keywords="form 16a, form 131, form 16a new name, form 16a due date, form 16a download traces, form 130 vs form 131, tds certificate non salary, form 16a 2026",
    desc="Form 16A is now Form 131 (tax year 2026-27): the quarterly TDS certificate for non-salary payments, due 15 days after the quarterly TDS statement (15 August, 15 November, 15 February, 15 June), downloaded from TRACES; Form 130 vs 131 and fixing mismatches.",
    howto={"name": "How a deductor issues Form 131", "description": "Quarterly TDS certificate.", "steps": [
        {"name": "File the TDS statement", "text": "Quarterly statement for the payments."},
        {"name": "Log in to TRACES", "text": "With the deductor's TAN."},
        {"name": "Request the certificate", "text": "Form 131 for the quarter."},
        {"name": "Download and issue", "text": "Within 15 days after the statement due date."},
        {"name": "Fix mismatches", "text": "File correction statements where needed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JE complete")
