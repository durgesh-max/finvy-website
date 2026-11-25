# -*- coding: utf-8 -*-
"""Batch IU (25 Nov 2026): TDS rate chart FY 2026-27 - resident payees; from 1 April 2026 TDS sits in section 393 of the
Income-tax Act, 2025 (salary in section 392) with rates and thresholds carried over from the 1961 Act as revised by the
Finance Act, 2025: 192A 10% / Rs 50,000; 193 10% / Rs 10,000; 194 10% / Rs 10,000; 194A banks 10% / Rs 50,000 (seniors
Rs 1 lakh), others Rs 10,000; 194B 30% / Rs 10,000; 194C 1% individual-HUF, 2% others / Rs 30,000 single or Rs 1 lakh
aggregate; 194D 2% / Rs 20,000; 194H 2% / Rs 20,000; 194I 2% P&M, 10% land-building / Rs 50,000 per month; 194-IA 1% /
Rs 50 lakh; 194-IB 2% / Rs 50,000 per month; 194J 2% technical, 10% professional / Rs 50,000 (director fees no limit);
194K 10% / Rs 10,000; 194N 2% above Rs 1 crore (co-ops Rs 3 crore); 194O 0.1% (Rs 5 lakh for individual / HUF
sellers); 194Q 0.1% above Rs 50 lakh; 194R 10% / Rs 20,000; 194S 1% / Rs 10,000 (Rs 50,000 specified persons); 194T
10% / Rs 20,000; higher rate (generally 20%) without PAN.
Demand: sweep ac114 (25 Nov 2026), all 7 markets: "tds rates", "tds rates fy 2026-27", "tds rates for fy 26-27",
"tds rates and sections", "tds rates for ay 2026-27", "tds rates for fy 2025-26 pdf download".
Facts (checked 25 Nov 2026): Taxguru TDS rates TY 2026-27 under the Income-tax Act, 2025 (4 April 2026); Income Tax
Department TDS pages (section 393 listing); BCAS comparison (dividend threshold Rs 10,000, rate 10%); site pages on TDS on
salary, rent, partners, Form 15G / 15H and lower deduction certificates."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tds-rate-chart-fy-2026-27-section-393-income-tax-act-2025-old-sections-194c-194j-194i-thresholds"

C = contact("the payments you make (contractors, professionals, rent, commission, purchases), whether you are an individual, firm or company, and your turnover")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="TDS Rate Chart FY 2026-27: Rates and Thresholds by Section (Old 194C, 194J, 194I, 194H and More, Now Section 393)",
    em="same rates, new section numbers from 1 April 2026.",
    kicker="/ Businesses, employers and landlords &middot; TDS &middot; Updated 2026-11-25",
    lead=("<strong>From 1 April 2026, TDS on payments to residents is governed by section 393 of the Income-tax Act, 2025 (salary by section 392), but the rates and thresholds largely carry over from the old sections as revised in 2025.</strong> "
          "Key figures: contractors 1% or 2% above &#8377;30,000 a bill or &#8377;1 lakh a year, professional fees 10% and technical fees 2% above &#8377;50,000, rent 10% (land or building) or 2% (machinery) above &#8377;50,000 a month, and commission 2% above &#8377;20,000. "
          "Without a PAN, TDS is generally deducted at 20% or the higher applicable rate."),
    sections=[
        ("/ TDS rate chart (residents)", "Old section, nature of payment, rate and yearly threshold.",
         table(["Old section", "Payment", "Rate", "Threshold"], [
             ["192 (now 392)", "Salary", "Slab rates", "Basic exemption"],
             ["192A", "Premature EPF withdrawal", "10%", "&#8377;50,000"],
             ["193", "Interest on securities", "10%", "&#8377;10,000"],
             ["194", "Dividends", "10%", "&#8377;10,000"],
             ["194A", "Interest from banks / post office", "10%", "&#8377;50,000 (&#8377;1 lakh senior citizens)"],
             ["194A", "Other interest", "10%", "&#8377;10,000"],
             ["194B", "Lottery, game show winnings", "30%", "&#8377;10,000 per winning"],
             ["194C", "Contractors", "1% individual / HUF, 2% others", "&#8377;30,000 a bill or &#8377;1 lakh a year"],
             ["194D", "Insurance commission", "2% (10% if paid to a domestic company)", "&#8377;20,000"],
             ["194H", "Commission or brokerage", "2%", "&#8377;20,000"],
             ["194I", "Rent: plant and machinery", "2%", "&#8377;50,000 a month"],
             ["194I", "Rent: land, building, furniture", "10%", "&#8377;50,000 a month"],
             ["194-IA", "Purchase of immovable property", "1%", "&#8377;50 lakh"],
             ["194-IB", "Rent paid by individuals / HUFs not under audit", "2%", "&#8377;50,000 a month"],
             ["194J", "Technical services, certain royalties", "2%", "&#8377;50,000"],
             ["194J", "Professional fees", "10%", "&#8377;50,000 (director fees: no limit)"],
             ["194K", "Mutual fund income", "10%", "&#8377;10,000"],
             ["194N", "Cash withdrawals", "2%", "Above &#8377;1 crore (&#8377;3 crore for co-operatives)"],
             ["194O", "E-commerce operators", "0.1%", "&#8377;5 lakh for individual / HUF sellers"],
             ["194Q", "Purchase of goods (buyer turnover above &#8377;10 crore)", "0.1%", "Above &#8377;50 lakh"],
             ["194R", "Business perquisites", "10%", "&#8377;20,000"],
             ["194S", "Virtual digital assets", "1%", "&#8377;10,000 (&#8377;50,000 specified persons)"],
             ["194T", "Partner salary, interest, commission", "10%", "&#8377;20,000"]])
         + '<p>Thresholds apply per payer per payee in a year unless stated. Payments to NRIs are covered separately (old section 195) at rates in force or treaty rates. Individuals and HUFs below the audit limit generally need not deduct under the contractor, professional, commission and rent sections, except 194-IB.</p>'),
        ("/ How the 2026 change works", "Old law vs new law.",
         ul("<strong>Payments up to 31 March 2026:</strong> the Income-tax Act, 1961 sections (194C, 194J and so on) apply, including returns and certificates for that period.",
            "<strong>Payments from 1 April 2026:</strong> section 393 tables of the Income-tax Act, 2025 apply; most rates and thresholds are unchanged.",
            "<strong>New forms:</strong> TDS returns move to Forms 138, 140, 144 and 143; Form 16 becomes Form 130 and Form 16A becomes Form 131; see " + L("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing") + ".",
            "<strong>Salary and rent:</strong> see " + L("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary") + " and " + L("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent") + ".",
            "<strong>Lower or nil deduction:</strong> payees can apply for a lower deduction certificate (Form 128, formerly Form 13) or give " + L("form-15g-15h-no-tds-declaration-india-2026.html", "Form 15G / 15H") + " on interest and dividends.")
         + call_box("TDS compliance", ["TDS rate and threshold checks",
                                        "Monthly deposits and quarterly returns",
                                        "Lower deduction certificates",
                                        "TDS on NRI payments",
                                        "Notices and defaults"],
                    "the payments you make.")
         + sources("Income-tax Act, 1961 sections 192 to 194T and 206AA as amended by the Finance Act, 2025; Income-tax Act, 2025 sections 392 and 393; Income Tax Department TDS pages; Taxguru TDS rates chart for tax year 2026-27 (4 April 2026); BCAS comparison of TDS provisions. Checked 25 November 2026.")),
    ],
    faqs=[("What are the TDS rates for FY 2026-27?", "Key rates: contractors 1% (individual / HUF) or 2% (others), professional fees 10%, technical fees 2%, rent 10% on land or buildings and 2% on machinery, commission 2%, property purchase 1%, dividends and bank interest 10%, partner payments 10%. Without PAN, generally 20%."),
          ("What is the TDS threshold for contractors and professionals?", "Contractors (old 194C): Rs 30,000 for a single payment or Rs 1 lakh in the year. Professional and technical fees (old 194J): Rs 50,000 in the year; director fees have no threshold."),
        ("What is the TDS rate on commission in 2026-27?", "Commission or brokerage (old section 194H, now in the section 393 table) attracts 2% TDS once payments to a person exceed Rs 20,000 in the year. Insurance commission (old 194D) is 2% for individuals and other non-company payees and 10% when paid to a domestic company, also above Rs 20,000. Without a PAN, TDS is 20%."),
          ("What is the TDS limit on rent from 1 April 2025?", "Rs 50,000 a month (or part of a month) for rent under the old 194I and 194-IB; TDS is 10% on land or buildings and 2% on plant and machinery, and 2% where individuals not under audit pay rent."),
          ("Which section covers TDS under the new Income-tax Act, 2025?", "Section 393 covers TDS on payments other than salary, through tables that replace sections 193 to 194T; salary TDS is in section 392. Rates and thresholds were largely carried over."),
          ("What happens if the payee has no PAN?", "TDS is generally deducted at 20% or the applicable rate, whichever is higher, so payees should share their PAN with the payer."),
          ("Can BQP manage TDS compliance for my business?", "Yes. CA Durgesh Chavda can check rates and thresholds, handle deposits and returns, obtain lower deduction certificates and respond to TDS notices. " + C)],
    related=[("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary"),
             ("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent"),
             ("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing"),
             ("section-194t-tds-partnership-firm-partners-india.html", "TDS on partners (194T)"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower TDS certificate")],
    cta_h="Deducting TDS?", cta_b=C,
    keywords="tds rate chart fy 2026-27, tds rates and sections, tds rates fy 2026-27, tds rates ay 2026-27, section 393 tds, 194c tds rate threshold, 194j tds rate 2026, 194i rent tds limit, tds rate chart pdf",
    desc="TDS rate chart FY 2026-27: rates and thresholds by section (old 192A to 194T, now section 393 of the Income-tax Act, 2025) - contractors 1% / 2%, professionals 10%, technical 2%, rent 10% / 2% above Rs 50,000 a month, commission 2%, dividends 10%, no-PAN 20%.",
    howto={"name": "How to apply the right TDS rate", "description": "For payments to residents.", "steps": [
        {"name": "Identify the payment", "text": "Contractor, professional, rent, commission, interest, purchase."},
        {"name": "Check the threshold", "text": "Per payee per year (or per month for rent)."},
        {"name": "Apply the rate", "text": "From the chart; 20% if the payee has no PAN."},
        {"name": "Deposit and file", "text": "Deposit monthly and file quarterly TDS returns."},
        {"name": "Issue certificates", "text": "Form 130 (salary) or Form 131 (other payments)."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IU complete")
