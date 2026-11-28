# -*- coding: utf-8 -*-
"""Batch KJ (27 Nov 2026): Payroll outsourcing services in India - what is handled each month and year, who needs it
(Indian companies and foreign-owned subsidiaries), how it differs from an Employer of Record, and how to start.
Demand: sweep ac167 (27 Nov 2026), all 7 markets: "payroll outsourcing services india", "hr payroll outsourcing services
india", "payroll outsourcing india", "payroll services india", "payroll outsourcing cost in india", "payroll outsourcing
agreement format india", "hr outsourcing india"; the site had subsidiary payroll / EPF / EOR pages but no payroll
outsourcing service page.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - payroll compliance for foreign-owned subsidiaries needs a CA.
Facts (site pages): TDS on salary deposited by the 7th of the next month, quarterly TDS return in Form 138 (old 24Q),
annual salary certificate Form 130 (old Form 16) by 15 June; EPF for establishments with 20 or more employees, wage ceiling
INR 25,000 a month from 17 September 2026 (up from INR 15,000); ESI for employees earning up to INR 21,000 a month in
establishments with 10 or more employees, 3.25% employer + 0.75% employee; professional tax and labour welfare fund are
state-specific; gratuity, statutory bonus and the new Labour Codes. No fees (the 'cost' query is answered by pointing to a
call), no office claims, no statistics, no portal menu paths, never ask for portal passwords."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "payroll-outsourcing-services-india-tds-salary-form-138-pf-esi-professional-tax-payslips-foreign-subsidiary-2026"

C = contact("the company name or CIN, the states where employees work, the headcount, the current salary structure (CTC breakup), the PF, ESI and professional tax registrations you already have, and whether the company is a foreign-owned subsidiary")
PAGES = [dict(
    slug=SLUG,
    title="Payroll Outsourcing Services in India (2026): Monthly Payroll, TDS on Salary and Form 138, PF, ESI, Professional Tax, Payslips and Form 130 - for Indian Companies and Foreign-Owned Subsidiaries",
    em="paid right, deducted right, filed on time.",
    kicker="/ Indian companies, startups and foreign-owned subsidiaries &middot; Payroll processing, statutory deductions and filings &middot; Updated 2026-11-27",
    lead=("<strong>Payroll outsourcing means a CA firm runs your monthly payroll: calculates salaries, deducts and deposits TDS, PF, ESI and professional tax, issues payslips, and files the returns that go with them.</strong> "
          "For a foreign company with an Indian subsidiary, it also means one person who understands both the Indian deductions and how the cost is reported back to the parent. "
          "It is done on data and online, so the company's location does not matter."),
    sections=[
        ("/ What a payroll outsourcing service handles", "Every month and every year.",
         table(["When", "What is done"], [
             ["Every month", "Salary calculation from attendance and CTC, TDS on salary, PF and ESI contributions, professional tax, payslips, bank payment file"],
             ["By the 7th / 15th", "TDS on salary deposited by the 7th of the next month; PF and ESI contributions by the 15th"],
             ["Every quarter", "TDS return on salary in Form 138 (old 24Q); state professional tax returns where required"],
             ["Every year", "Form 130 (old Form 16) salary certificates by 15 June, investment declarations and proofs, statutory bonus, leave encashment and gratuity provisions"],
             ["On joining and exit", "PF / ESI enrolment, full and final settlement, gratuity where due, relieving and tax computation"],
             ["Registrations", "PF, ESI, professional tax and labour welfare fund registrations in each state where people work"]])
         + ul("<strong>PF:</strong> establishments with 20 or more employees; the mandatory wage ceiling rose to INR 25,000 a month from 17 September 2026.",
              "<strong>ESI:</strong> employees earning up to INR 21,000 a month in establishments with 10 or more employees - 3.25% employer and 0.75% employee.",
              "<strong>State rules:</strong> professional tax and labour welfare fund differ by state, so a team spread across states needs each state handled.",
              "<strong>Labour Codes:</strong> the new Labour Codes change the wage definition, gratuity for fixed-term staff and other benefits - salary structures should be reviewed.")),
        ("/ Payroll outsourcing, EOR or your own entity?", "Pick the right model first.",
         ul("<strong>Your own Indian company or subsidiary:</strong> you are the employer; payroll outsourcing runs the payroll and filings in your name.",
            "<strong>Employer of Record (EOR):</strong> a third party is the legal employer for you - useful before you set up an entity, but the contracts and IP sit with the EOR.",
            "<strong>Contractors:</strong> simpler, but misclassification and permanent establishment risk grow as the team grows.",
            "<strong>Cost:</strong> depends on headcount, number of states and how much of the HR work is included - book a call and we scope it for your team.")
         + call_box("Payroll outsourcing", ["Monthly payroll processing and payslips",
                                            "TDS on salary, Form 138 returns and Form 130",
                                            "PF, ESI, professional tax and labour welfare fund",
                                            "Registrations, joining and full-and-final settlements",
                                            "Payroll for foreign-owned subsidiaries"],
                    "CIN, states, headcount, CTC structure and existing registrations.")
         + sources("Income-tax Act, 2025 and Income-tax Rules, 2026 (TDS on salary, Forms 138 and 130); Employees' Provident Funds and Miscellaneous Provisions Act and the September 2026 wage-ceiling notification; ESI Act; state professional tax laws; the Labour Codes; site EPF / ESI, subsidiary payroll, EOR and TDS return guides. Checked 27 November 2026.")),
    ],
    faqs=[("What does a payroll outsourcing service in India include?", "Monthly salary processing from attendance and CTC, deduction and deposit of TDS on salary, PF, ESI and professional tax, payslips and the bank payment file, quarterly TDS returns in Form 138 (old 24Q), annual Form 130 (old Form 16) certificates, investment declarations, full and final settlements, and the PF, ESI and professional tax registrations in each state where employees work."),
          ("Can a foreign company outsource payroll for its Indian subsidiary?", "Yes. The subsidiary stays the employer and the payroll provider runs payroll, deductions and filings in its name, with reports the parent can use for group accounting. Before an entity exists, an Employer of Record is the usual alternative; once the subsidiary is set up, payroll can move in-house to it."),
          ("What are the payroll compliance deadlines in India?", "TDS on salary is deposited by the 7th of the following month and PF and ESI contributions by the 15th. The TDS return on salary (Form 138) is filed quarterly, and Form 130 salary certificates are issued by 15 June after the year ends. Professional tax dates depend on the state."),
        ("What is the time limit for full and final settlement when an employee leaves?", "Under section 17(2) of the Code on Wages, 2019, in force since 21 November 2025, wages due to an employee who resigns, is removed, dismissed or retrenched, or whose establishment closes must be paid within two working days. That deadline covers wages as the Code defines them (basic pay, dearness allowance and retaining allowance); gratuity is due within 30 days of becoming payable under the Code on Social Security, and leave encashment, bonus and reimbursements follow the law and the company's policy. Practitioners still debate whether the two days run from the resignation or the last working day, so many employers now pay salary dues within two working days of the last day and settle the rest promptly after exit formalities. Notice periods and notice-pay buyouts are set by the employment contract and standing orders, not a single statutory number. Book a call to align the exit process and payroll."),
          ("How much does payroll outsourcing cost in India?", "It depends on headcount, the number of states, and whether HR work such as onboarding documents and leave tracking is included. We do not quote a standard rate - book a call or WhatsApp the details and we scope it for your team."),
          ("Is there a standard payroll outsourcing agreement format?", "There is no prescribed format. The agreement should set out the scope (payroll, statutory filings, registrations), data the company provides and by when, confidentiality and data protection, who signs and pays statutory dues, responsibility for errors, and exit and handover. We share our engagement terms once the scope is agreed."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company name or CIN, the states where employees work, the headcount, the CTC structure, the PF, ESI and professional tax registrations you already have, and whether the company is foreign-owned. We tell you what is needed and set up the payroll calendar, or book a call.")],
    related=[("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Subsidiary payroll: EPF, ESI, gratuity"),
             ("employer-of-record-india-hire-from-abroad.html", "Employer of Record in India"),
             ("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "Remote employees: EOR vs contractor vs subsidiary"),
             ("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing (Form 138)"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar")],
    cta_h="Want your India payroll handled?", cta_b=C,
    keywords="payroll outsourcing services india, payroll outsourcing india, hr payroll outsourcing services india, payroll services india, payroll outsourcing cost in india, payroll outsourcing agreement format india, payroll compliance india, payroll for foreign subsidiary india, tds on salary form 138, pf esi professional tax",
    desc="Payroll outsourcing services in India: monthly payroll, TDS on salary by the 7th, PF and ESI by the 15th, Form 138 (old 24Q) returns, Form 130 (old Form 16) by 15 June, professional tax, registrations and full-and-final settlements - for Indian companies and foreign-owned subsidiaries.",
    howto={"name": "How to outsource payroll in India", "description": "From scoping to the first payroll run.", "steps": [
        {"name": "Share the basics", "text": "CIN, states, headcount, CTC structure and existing registrations."},
        {"name": "Fix registrations", "text": "PF, ESI, professional tax and labour welfare fund where required."},
        {"name": "Set the payroll calendar", "text": "Attendance cut-off, salary date, TDS by the 7th, PF and ESI by the 15th."},
        {"name": "Run and file", "text": "Monthly payroll and payslips, quarterly Form 138, annual Form 130."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KJ complete")
