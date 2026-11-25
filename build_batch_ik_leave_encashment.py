# -*- coding: utf-8 -*-
"""Batch IK (25 Nov 2026): leave encashment tax 2026 - encashment during service fully taxable as salary; at retirement
or resignation, government employees fully exempt; non-government employees exempt up to the least of (a) amount
received, (b) Rs 25 lakh (raised from Rs 3 lakh by CBDT notification from 1 April 2023; unchanged in later budgets),
(c) 10 months' average salary, (d) cash equivalent of unavailed leave at up to 30 days per completed year of service;
Rs 25 lakh is a lifetime cap across employers; section 10(10AA) of the 1961 Act, section 19 of the 2025 Act; exemption
available under the new regime (10(10AA) is not among the exemptions withdrawn); leave encashment received by legal
heirs on death is not taxable; relief under section 89 for arrears.
Demand: sweep ac111 (25 Nov 2026), all 7 markets: "leave encashment tax", "leave encashment taxability in new regime",
"leave encashment tax exemption", "leave encashment taxable or not", "leave encashment tax free", "leave encashment tax
calculator", "leave encashment tax rules".
Facts (checked 25 Nov 2026): Business Today (3 April 2026), Policybazaar, Zoho Payroll (section 19 of the 2025 Act),
Keka, Motilal Oswal, Goodreturns, Taxscan ITAT reports on the Rs 25 lakh limit."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "leave-encashment-tax-exemption-section-10-10aa-25-lakh-new-regime-retirement-resignation-2026"

C = contact("whether you are a government or private employee, the leave encashment amount, years of service, leave balance, average salary for the last 10 months, and any exemption claimed with earlier employers")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Leave Encashment Tax 2026: Is It Taxable, Rs 25 Lakh Exemption (Section 10(10AA), Now Section 19), New Regime and Calculation",
    em="when you encash decides whether you pay.",
    kicker="/ Employees leaving or retiring &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Leave encashment received while you are still in service is fully taxable as salary, but encashment at retirement or resignation is exempt for government employees and, for private-sector employees, exempt up to &#8377;25 lakh over a lifetime.</strong> "
          "The exemption is in section 10(10AA) of the Income-tax Act, 1961 and section 19 of the Income-tax Act, 2025, and it is available under both the old and new tax regimes. "
          "For non-government employees the exempt amount is the least of four limits, including &#8377;25 lakh and 10 months&rsquo; average salary."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is leave encashment taxable?</strong> During service: yes, fully, as salary. At retirement or resignation: exempt for government employees; for others, exempt up to the least of four limits, with the balance taxable.",
            "<strong>What is the leave encashment exemption limit?</strong> &#8377;25 lakh for non-government employees (from 1 April 2023, earlier &#8377;3 lakh), as a lifetime limit across all employers.",
            "<strong>Is leave encashment exempt in the new tax regime?</strong> Yes. The retirement / resignation exemption is not among those withdrawn in the new regime.",
            "<strong>How is the exempt amount calculated?</strong> Least of: the amount received; &#8377;25 lakh (less any exemption claimed earlier); 10 months&rsquo; average salary; and the cash equivalent of unavailed leave at up to 30 days for each completed year of service.",
            "<strong>Is leave encashment paid to legal heirs taxable?</strong> No, encashment received by legal heirs after an employee&rsquo;s death is not taxable in their hands.",
            "<strong>Is TDS deducted?</strong> The employer deducts TDS on the taxable part along with salary; see " + L("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary 2026-27") + ".")),
        ("/ Calculation (illustrative)", "Private-sector employee resigning.",
         table(["Limit", "Amount"], [
             ["Leave encashment received", "&#8377;12,00,000"],
             ["Notified limit", "&#8377;25,00,000"],
             ["10 months&rsquo; average salary (&#8377;1,00,000 a month)", "&#8377;10,00,000"],
             ["Cash equivalent of unavailed leave (300 days at 30 days a year, on average salary)", "&#8377;10,00,000"],
             ["Exempt (least)", "&#8377;10,00,000"],
             ["Taxable as salary", "&#8377;2,00,000"]])
         + '<p>Figures are illustrative; salary for this purpose generally means basic pay plus dearness allowance forming part of retirement benefits and commission based on turnover, averaged over the 10 months before leaving.</p>'),
        ("/ Planning points", "Before you resign or retire.",
         ul("<strong>Track the lifetime cap:</strong> keep records of exemption claimed at earlier exits; the &#8377;25 lakh is shared across all employers.",
            "<strong>Spread arrears:</strong> where encashment includes arrears, relief under section 89 can reduce the tax.",
            "<strong>Other exit payments:</strong> gratuity and PF have separate rules; see the " + L("gratuity-calculator-new-labour-codes-2026.html", "gratuity calculator") + " and " + L("pf-withdrawal-tax-rules-2026-epf-taxable-or-not-5-years-tds-10-percent-which-head.html", "PF withdrawal tax rules") + ".",
            "<strong>Regime choice:</strong> compare with the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ".",
            "<strong>Employers:</strong> apply the exemption correctly in payroll and report it in Form 130; see " + L("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "subsidiary payroll and benefits") + ".")
         + call_box("Exit payments", ["Leave encashment exemption check",
                                       "Gratuity and PF on exit",
                                       "Section 89 relief",
                                       "Payroll TDS on full and final settlement",
                                       "ITR reporting"],
                    "the exit payment and service details.")
         + sources("Income-tax Act, 1961, section 10(10AA) and the CBDT notification raising the limit to Rs 25 lakh from 1 April 2023; Income-tax Act, 2025, section 19; Business Today (3 April 2026), Policybazaar, Zoho Payroll, Keka, Motilal Oswal and Goodreturns explainers; Taxscan reports on ITAT rulings on the Rs 25 lakh limit. Checked 25 November 2026.")),
    ],
    faqs=[("Is leave encashment taxable?", "Leave encashed during service is fully taxable as salary. At retirement or resignation it is fully exempt for government employees, and exempt for others up to the least of four limits, including Rs 25 lakh over a lifetime."),
          ("What is the leave encashment exemption limit for 2026?", "Rs 25 lakh for non-government employees, a lifetime limit across all employers, in force since 1 April 2023 and unchanged since."),
          ("Is leave encashment exempt under the new tax regime?", "Yes. The exemption for leave encashment at retirement or resignation is available under both the old and the new tax regime."),
          ("How do I calculate taxable leave encashment?", "Take the least of the amount received, Rs 25 lakh (less any exemption claimed earlier), 10 months' average salary and the cash equivalent of unavailed leave at up to 30 days per completed year of service; that amount is exempt and the rest is taxable salary."),
          ("Is leave encashment received by legal heirs taxable?", "No. Leave encashment paid to legal heirs after the employee's death is not taxable in their hands."),
          ("Can BQP check my full and final settlement tax?", "Yes. CA Durgesh Chavda can compute the exempt and taxable parts of leave encashment, gratuity and PF on exit and file your return. " + C)],
    related=[("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary 2026-27"),
             ("gratuity-calculator-new-labour-codes-2026.html", "Gratuity calculator"),
             ("pf-withdrawal-tax-rules-2026-epf-taxable-or-not-5-years-tds-10-percent-which-head.html", "PF withdrawal tax rules"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Subsidiary payroll and benefits")],
    cta_h="Leaving a job or retiring?", cta_b=C,
    keywords="leave encashment tax, leave encashment taxable or not, leave encashment exemption 25 lakh, section 10(10AA), leave encashment new tax regime, leave encashment calculation, leave encashment tax rules 2026, section 19 Income-tax Act 2025",
    desc="Leave encashment tax 2026: taxable during service; at retirement or resignation exempt for government employees and up to Rs 25 lakh (lifetime) for others under section 10(10AA) / section 19 of the 2025 Act, new regime allowed, four-limit calculation.",
    howto={"name": "How to calculate leave encashment exemption", "description": "For non-government employees at exit.", "steps": [
        {"name": "Take the amount received", "text": "Leave encashment paid at retirement or resignation."},
        {"name": "Apply the Rs 25 lakh cap", "text": "Less any exemption claimed with earlier employers."},
        {"name": "Compute 10 months' average salary", "text": "Basic + DA forming part of retirement benefits + turnover commission."},
        {"name": "Compute unavailed leave value", "text": "Up to 30 days per completed year, at average salary."},
        {"name": "Exempt the least", "text": "The balance is taxable salary."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IK complete")
