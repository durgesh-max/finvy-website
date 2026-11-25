# -*- coding: utf-8 -*-
"""Batch IV (25 Nov 2026): ESIC registration for employers 2026 - Employees' State Insurance (now under the Code on
Social Security, 2020) applies to factories and establishments with 10 or more employees in notified areas (20 for some
establishments in some states); employees earning up to Rs 21,000 a month gross (Rs 25,000 for persons with
disabilities) are covered; contributions 3.25% employer + 0.75% employee (employees earning up to Rs 176 a day pay
nothing, employer still pays); employer registers online on the ESIC portal (or through SPICe+ at incorporation) and
gets a 17-digit employer code; employees get an insurance number (IP number); contributions paid monthly by the 15th of
the following month; benefits: medical care for employee and family, sickness, maternity, disablement, dependants.
Demand: sweep ac114 (25 Nov 2026), all 7 markets: "esic registration", "esic registration for employer", "esic
registration process", "esic registration online", "esic registration number", "esic registration means", "esic
registration certificate download".
Facts (checked 25 Nov 2026): ESIC coverage page; Treelife, greytHR, Cleartax, Onsurity, Bajaj Finserv, Taxguru notes;
site payroll page (labour codes in force, ESIC ceiling unchanged at Rs 21,000)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "esic-registration-employer-2026-applicability-10-employees-21000-wage-limit-contribution-3-25-0-75-process"

C = contact("your state and city, number of employees, their monthly gross wages, the date you crossed 10 employees, and whether you already have EPF registration")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="ESIC Registration for Employers 2026: Who Must Register (10+ Employees), Rs 21,000 Wage Limit, 3.25% + 0.75% Contribution and Online Process",
    em="once you hit 10 employees, registration is not optional.",
    kicker="/ Employers, startups and foreign-owned subsidiaries &middot; Payroll compliance &middot; Updated 2026-11-25",
    lead=("<strong>Any factory or establishment with 10 or more employees in an ESIC-notified area must register with the Employees&rsquo; State Insurance Corporation and cover employees earning up to &#8377;21,000 a month.</strong> "
          "The employer contributes 3.25% and the employee 0.75% of wages, paid monthly by the 15th of the following month. "
          "Registration is online on the ESIC portal (or through SPICe+ when a company is incorporated) and gives the employer a 17-digit code number."),
    sections=[
        ("/ ESIC at a glance", "Applicability, rates and dates.",
         table(["Point", "Rule"], [
             ["Who must register", "Factories and establishments with 10 or more employees in notified areas (20 for some establishments in some states)"],
             ["Which employees are covered", "Gross wages up to &#8377;21,000 a month (&#8377;25,000 for persons with disabilities)"],
             ["Employer contribution", "3.25% of wages"],
             ["Employee contribution", "0.75% of wages (nil if daily wage is up to &#8377;176; employer still pays)"],
             ["Payment due date", "15th of the following month"],
             ["Employer code", "17-digit number allotted on registration"],
             ["Employee number", "Insurance (IP) number and e-Pehchan card"]])
         + '<p>The scheme continues under the Code on Social Security, 2020; see the ' + L("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "payroll and benefits guide") + ' for EPF, gratuity and bonus alongside ESI.</p>'),
        ("/ How to register (online)", "Step by step.",
         ul("<strong>Check applicability:</strong> count all employees, including contract and casual staff, against the 10-employee threshold in your area.",
            "<strong>Sign up on the ESIC portal:</strong> employer registration with PAN, business registration (incorporation certificate, partnership deed or shop licence), address proof, bank details and employee list.",
            "<strong>New companies:</strong> ESIC registration can be obtained through SPICe+ at incorporation.",
            "<strong>Get the code:</strong> the 17-digit employer code and registration certificate are issued online and can be downloaded from the portal.",
            "<strong>Register employees:</strong> add each covered employee to get an IP number; they and their families can then use ESIC dispensaries and hospitals.",
            "<strong>Pay monthly:</strong> deduct 0.75%, add 3.25% and pay by the 15th; keep wage registers for inspection.")),
        ("/ Benefits and penalties", "Why it matters.",
         ul("<strong>Benefits for employees:</strong> medical care for the employee and family, cash benefit during sickness, maternity benefit, disablement and dependants&rsquo; benefits.",
            "<strong>Late payment:</strong> attracts interest and damages, and non-registration can lead to assessment of contributions for past periods.",
            "<strong>Above the wage limit:</strong> employees earning more than &#8377;21,000 a month are outside ESIC; many employers give them group health insurance instead.",
            "<strong>Other payroll items:</strong> TDS on salary and PF; see " + L("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary") + ", " + L("pf-withdrawal-tax-rules-2026-epf-taxable-or-not-5-years-tds-10-percent-which-head.html", "PF withdrawal rules") + " and the " + L("gratuity-calculator-new-labour-codes-2026.html", "gratuity calculator") + ".")
         + call_box("Payroll compliance", ["ESIC and EPF registration",
                                            "Monthly ESI, PF and TDS payroll",
                                            "Labour code compliance",
                                            "Foreign-owned subsidiary payroll",
                                            "Inspections and notices"],
                    "your headcount and wages.")
         + sources("Employees' State Insurance Act, 1948 and Code on Social Security, 2020; ESIC coverage page (esic.gov.in); Treelife, greytHR, Cleartax, Onsurity, Bajaj Finserv and Taxguru guides; site payroll and benefits guide. Checked 25 November 2026.")),
    ],
    faqs=[("Who needs ESIC registration?", "Factories and establishments with 10 or more employees in ESIC-notified areas (20 for some establishments in some states) must register and cover employees earning up to Rs 21,000 a month (Rs 25,000 for persons with disabilities)."),
          ("What is the ESIC contribution rate in 2026?", "3.25% of wages from the employer and 0.75% from the employee, 4% in total. Employees earning up to Rs 176 a day do not pay their share, but the employer still pays 3.25%."),
          ("How do I register for ESIC as an employer?", "Register online on the ESIC portal with PAN, business registration documents, address proof, bank details and the employee list; new companies can get ESIC through SPICe+ at incorporation. A 17-digit employer code is issued online."),
          ("What is the ESIC registration number?", "The 17-digit employer code number allotted on registration; each covered employee gets a separate insurance (IP) number."),
          ("What is the due date for ESIC payment?", "Contributions for a month are due by the 15th of the following month; late payment attracts interest and damages."),
          ("Can BQP handle ESIC and payroll compliance?", "Yes. CA Durgesh Chavda can register your business for ESIC and EPF and run monthly payroll compliance, including for foreign-owned subsidiaries. " + C)],
    related=[("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Payroll and benefits guide"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary"),
             ("pf-withdrawal-tax-rules-2026-epf-taxable-or-not-5-years-tds-10-percent-which-head.html", "PF withdrawal rules"),
             ("gratuity-calculator-new-labour-codes-2026.html", "Gratuity calculator"),
             ("tds-rate-chart-fy-2026-27-section-393-income-tax-act-2025-old-sections-194c-194j-194i-thresholds.html", "TDS rate chart 2026-27")],
    cta_h="Hiring your tenth employee?", cta_b=C,
    keywords="esic registration, esic registration for employer, esic registration process, esic registration online, esic registration number, esic contribution rate 2026, esic wage limit 21000, esic applicability 10 employees",
    desc="ESIC registration for employers 2026: mandatory at 10+ employees in notified areas, covers employees earning up to Rs 21,000 a month, 3.25% employer + 0.75% employee contribution by the 15th, online registration and 17-digit code, benefits and penalties.",
    howto={"name": "How to register for ESIC", "description": "For employers.", "steps": [
        {"name": "Check applicability", "text": "10 or more employees in a notified area."},
        {"name": "Register online", "text": "ESIC portal (or SPICe+ for new companies) with PAN and business documents."},
        {"name": "Get the employer code", "text": "17-digit code and certificate online."},
        {"name": "Register employees", "text": "IP numbers for employees earning up to Rs 21,000 a month."},
        {"name": "Pay monthly", "text": "3.25% + 0.75% by the 15th of the next month."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IV complete")
