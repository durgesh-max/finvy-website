# -*- coding: utf-8 -*-
"""Batch IE (25 Nov 2026): TDS on salary for tax year 2026-27 - section 392 of the Income-tax Act, 2025 (section 192 of
the 1961 Act): deducted when salary is paid, at the average rate on estimated taxable salary for the year; no fixed
rate; new regime default (slabs 0-4 lakh nil, 4-8 5%, 8-12 10%, 12-16 15%, 16-20 20%, 20-24 25%, above 24 lakh 30%);
section 87A (section 156 of the 2025 Act) rebate up to Rs 60,000 makes tax nil up to Rs 12 lakh taxable income (Rs 12.75
lakh salary after Rs 75,000 standard deduction) with marginal relief; old regime standard deduction Rs 50,000.
Certificate Form 130 (replacing Form 16), first issue by 15 June 2027 for tax year 2026-27; quarterly TDS return Form
138 (replacing 24Q).
Demand: sweep ac108 (25 Nov 2026), all 7 markets: "tds on salary", "tds on salary limit", "tds on salary rate", "tds on
salary section", "tds on salary new section", "tds on salary calculator fy 2026-27", "tds on salary for fy 2026-27".
Facts (checked 25 Nov 2026): Income Tax Department Form 130 FAQs and section 392 pages; Taxmann and Cleartax on section
392; India Briefing and Business Today on Form 130; site pages on 2026-27 slabs and 87A (tax-rates-in-india-2026-27,
itr-filing-ay-2026-27) and section 392 mapping (section-195-now-393 page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27"

C = contact("whether you are the employer or employee, the salary structure, the regime chosen, and any other income or deductions to be declared")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="TDS on Salary 2026-27: Section 392 (Old Section 192), Limit, Rates, Calculation, Form 130 and Form 16 Not Received",
    em="spread the year's tax evenly across the months.",
    kicker="/ Employees and employers &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>TDS on salary is deducted by the employer each time salary is paid, at the average rate of income tax on the employee&rsquo;s estimated taxable salary for the year; there is no fixed TDS rate on salary.</strong> "
          "From tax year 2026-27 the provision is section 392 of the Income-tax Act, 2025 (section 192 of the 1961 Act). "
          "Under the default new regime, no tax is payable, and so no TDS is due, on salary up to about &#8377;12.75 lakh (&#8377;12 lakh of taxable income after the &#8377;75,000 standard deduction, using the section 87A rebate). "
          "The annual TDS certificate is now Form 130, replacing Form 16, and the employer&rsquo;s quarterly return is Form 138, replacing Form 24Q."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is the new section for TDS on salary?</strong> Section 392 of the Income-tax Act, 2025, in force from 1 April 2026, replacing section 192.",
            "<strong>What is the TDS on salary rate?</strong> There is no flat rate. The employer works out the tax on the year&rsquo;s estimated salary under the regime the employee chooses and deducts it evenly across the remaining months.",
            "<strong>What is the TDS on salary limit?</strong> TDS applies only if estimated taxable income exceeds the level at which tax becomes payable: in the new regime, taxable income above &#8377;12 lakh (salary above about &#8377;12.75 lakh), with marginal relief just above; in the old regime, above the basic exemption after deductions.",
            "<strong>Which regime does the employer use?</strong> The new regime by default, unless the employee tells the employer they want the old regime for TDS.",
            "<strong>What certificate do employees get?</strong> Form 130 (the successor to Form 16), first issued by 15 June 2027 for tax year 2026-27.",
            "<strong>Can other income be taken into account?</strong> Yes. Employees can declare other income and losses under house property so the employer adjusts TDS; TDS from a previous employer in the same year must also be reported to the new employer.")),
        ("/ New regime slabs used for TDS (tax year 2026-27)", "Before the 87A rebate and 4% cess.",
         table(["Taxable income", "Rate"], [
             ["Up to &#8377;4 lakh", "Nil"], ["&#8377;4-8 lakh", "5%"], ["&#8377;8-12 lakh", "10%"], ["&#8377;12-16 lakh", "15%"],
             ["&#8377;16-20 lakh", "20%"], ["&#8377;20-24 lakh", "25%"], ["Above &#8377;24 lakh", "30%"]])
         + '<p>Section 87A (section 156 of the 2025 Act) gives a rebate of up to &#8377;60,000, so tax is nil up to &#8377;12 lakh of taxable income. Full rates and surcharge: ' + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates in India 2026-27") + '; compare regimes with the ' + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + '.</p>'),
        ("/ How the monthly TDS is worked out", "The employer's steps.",
         ul("<strong>Estimate annual salary:</strong> basic, allowances, perquisites and bonus expected for the year.",
            "<strong>Apply the regime:</strong> new regime with &#8377;75,000 standard deduction, or old regime with &#8377;50,000 standard deduction plus exemptions such as " + L("hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html", "HRA") + " and declared deductions.",
            "<strong>Compute tax:</strong> slab tax, less rebate, plus cess; divide by the number of salary payments left in the year and deduct monthly, adjusting as actual figures change.",
            "<strong>Collect proofs:</strong> employees on the old regime submit evidence of rent, investments and loans so the employer can allow them.",
            "<strong>Deposit and report:</strong> the employer deposits TDS and files the quarterly return in Form 138; see " + L("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing") + ".",
            "<strong>Issue Form 130:</strong> by 15 June after the tax year; employees then file their return, see " + L("itr-filing-ay-2026-27-deadlines-changes-india.html", "ITR filing") + ".")
         + call_box("Salary TDS", ["Payroll TDS computation",
                                    "Regime choice for employees",
                                    "Form 138 quarterly returns",
                                    "Form 130 certificates",
                                    "TDS mismatches and refunds"],
                    "the salary structure and the regime.")
         + sources("Income-tax Act, 2025, section 392 (section 192 of the Income-tax Act, 1961) and section 156 (rebate); Income Tax Department FAQs on Form 130; Taxmann and Cleartax commentary on section 392; India Briefing and Business Today on Form 130. Checked 25 November 2026.")),
    ],
    faqs=[("What is the new section for TDS on salary?", "Section 392 of the Income-tax Act, 2025, which applies from 1 April 2026 and replaces section 192 of the Income-tax Act, 1961."),
          ("What is the rate of TDS on salary?", "There is no fixed rate. The employer deducts tax at the average rate applicable to the employee's estimated taxable salary for the year, under the new regime by default or the old regime if the employee opts for it."),
          ("What is the TDS on salary limit for 2026-27?", "Under the new regime, no TDS is due if taxable income is up to Rs 12 lakh, which with the Rs 75,000 standard deduction means salary up to about Rs 12.75 lakh, because the section 87A rebate makes the tax nil. Above that, TDS applies, with marginal relief just above the threshold."),
          ("What replaces Form 16?", "Form 130 is the salary TDS certificate under the Income-tax Act, 2025. For tax year 2026-27 it is due by 15 June 2027."),
        ("I have not received Form 16 (now Form 130) from my employer or previous employer. Can I still file my return?", "Yes. Form 16 is a certificate, not a condition for filing. The employer must issue it by 15 June after the year for any tax deducted, and can be penalised for not doing so, so ask HR or the payroll team first - a past employer can still issue it from the tax department's TDS system. Meanwhile, file using your payslips and the TDS credited to your PAN in Form 168 (old 26AS) and AIS: the salary paid and tax deducted by each employer appear there once the employer has filed its quarterly salary TDS return. If you changed jobs, add both employers' salary and claim the standard deduction only once, and check whether the second employer knew your earlier salary - if not, too little tax may have been deducted and you may need to pay the balance as self-assessment tax before filing. If tax was deducted but does not show in Form 168, the employer has not filed or has filed the TDS return wrongly, so ask for a correction before claiming it. WhatsApp +91 78018 87130 with your payslips, Form 168 / AIS and the details of each employer, or book a call."),
        ("I received salary arrears this year. How does relief under section 89 work?", "Section 89(1) (section 157 of the Income-tax Act, 2025 from tax year 2026-27, according to published commentary) stops arrears or advance salary from being taxed at a higher slab just because they are paid in one year. The tax is worked out twice for the year of receipt (with and without the arrears) and again for each earlier year the arrears relate to (with and without its share); the relief is the extra tax in the year of receipt minus the extra tax the arrears would have caused if paid on time. It also covers family pension arrears and some lump-sum payments such as gratuity or compensation on termination in specified cases. To claim it, file Form 10E online on the e-filing portal before filing the return (reported to be replaced by Form 39 from tax year 2026-27) - a return claiming the relief without it is processed without the relief. Relief can be nil if the earlier years were taxed at a higher rate, so compute it before claiming. WhatsApp +91 78018 87130 with the arrears breakup by year and your past returns, or book a call."),
          ("Which return does the employer file for salary TDS?", "The quarterly TDS return for salary is Form 138, which replaces Form 24Q from tax year 2026-27."),
          ("Can BQP handle salary TDS for our company?", "Yes. CA Durgesh Chavda can set up payroll TDS computation, file Form 138 returns and issue Form 130, including for foreign-owned Indian subsidiaries. " + C)],
    related=[("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing"),
             ("hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html", "HRA exemption"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Subsidiary payroll and benefits")],
    cta_h="Need salary TDS set up correctly?", cta_b=C,
    keywords="TDS on salary, TDS on salary section 392, TDS on salary new section, TDS on salary limit 2026-27, TDS on salary rate, section 192 TDS, Form 130, Form 138, TDS on salary calculation",
    desc="TDS on salary 2026-27: section 392 of the Income-tax Act, 2025 (old section 192), average-rate deduction, new regime slabs, nil TDS up to about Rs 12.75 lakh salary, old regime, Form 130 (replacing Form 16) and Form 138 returns.",
    howto={"name": "How TDS on salary is calculated", "description": "For tax year 2026-27.", "steps": [
        {"name": "Estimate annual salary", "text": "Including allowances, perquisites and bonus."},
        {"name": "Apply the regime", "text": "New regime by default, or old regime if chosen."},
        {"name": "Compute annual tax", "text": "Slab tax less rebate, plus 4% cess."},
        {"name": "Spread over the months", "text": "Divide by remaining salary payments and adjust as figures change."},
        {"name": "Deposit, report and certify", "text": "Deposit monthly, file Form 138 quarterly, issue Form 130."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IE complete")
