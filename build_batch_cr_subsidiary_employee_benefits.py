# -*- coding: utf-8 -*-
"""Batch CR (15 Nov 2026): employee benefits and payroll set-up for the Indian subsidiary of a US/UK/foreign company.
Demand: Search Console queries "us company india subsidiary employee benefits setup" (position ~12) and
"uk company india subsidiary benefits" (~22) with no dedicated page.
Facts: four labour codes in force from 21 November 2025 (Code on Wages 2019; Industrial Relations, Social Security and
OSHWC Codes 2020), replacing 29 laws; gratuity for fixed-term employees after one year. EPF wage ceiling for mandatory
coverage raised from INR 15,000 to INR 25,000 a month by Notification S.O. 5109(E) dated 17 September 2026 under section
2(89) of the Code on Social Security (Fox Mandal note; supersedes S.O. 2702(E)); ESIC ceiling unchanged at INR 21,000.
EPF 12% employer + 12% employee; establishments with 20+ employees. ESI employer 3.25% / employee 0.75%,
establishments with 10+ employees. Maternity 26 weeks. Professional tax up to INR 2,500 a year (state). Wages under the
codes: excluded allowances above 50% of remuneration are added back. RSUs/ESOPs of a foreign parent are a perquisite
taxed in India; Indian employer deducts TDS; residents report foreign shares in Schedule FA.
Sources: Labour Ministry PIB release (21 Nov 2025); Fox Mandal on S.O. 5109(E); SCC Online/KPMG summaries (checked 15 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the parent's country, the Indian states where staff will sit, headcount and the salary range. "
           "We reply within one working day with the registrations, a benefits checklist and a payroll calendar, with a fixed-scope quote.")
SLUG = "foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Copying the US benefits plan does not work in India.</p>'
       f'<p style="margin:0">Provident fund, ESI, gratuity, bonus and state registrations are statutory, the salary structure decides what they cost, and the September 2026 PF ceiling change widened coverage. We set up the registrations, salary structure and monthly payroll compliance for foreign-owned subsidiaries. '
       f'<a href="{wa("Hi Durgesh, our foreign company is setting up an Indian subsidiary and hiring. Can you help with payroll and employee benefits?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Employee Benefits and Payroll for the Indian Subsidiary of a US or UK Company (2026): EPF, ESI, Gratuity, Bonus and the New Labour Codes",
    em="what is mandatory, what is market practice, and the 2026 changes.",
    kicker="/ Foreign companies &middot; India subsidiary &middot; Payroll &middot; Updated 2026-11-15",
    lead=("An Indian subsidiary of a US, UK or other foreign company must give its employees the <strong>statutory benefits under India's four labour codes</strong> (in force since <strong>21 November 2025</strong>): <strong>provident fund</strong> (12% employer plus 12% employee, for establishments with 20 or more employees), <strong>ESI health insurance</strong> for employees earning up to INR 21,000 a month (establishments with 10 or more employees), <strong>gratuity</strong> (after five years, or <strong>one year for fixed-term employees</strong>), <strong>statutory bonus</strong>, <strong>26 weeks' paid maternity leave</strong> and state professional tax. "
          "From <strong>17 September 2026</strong> the provident fund wage ceiling for mandatory coverage rose from <strong>INR 15,000 to INR 25,000 a month</strong> (Notification S.O. 5109(E)). Group health insurance and stock awards from the parent are not mandatory but are market practice, and parent RSUs are taxed in India as salary through the subsidiary's payroll."),
    sections=[
        ("/ Mandatory benefits", "Statutory checklist for a foreign-owned subsidiary.",
         table(["Benefit", "Who and when", "Cost / rule"], [
             ["Provident fund (EPF)", "Establishments with 20+ employees; mandatory for employees with wages up to INR 25,000 a month from 17 Sept 2026 (was INR 15,000); others can be covered", "12% employer + 12% employee of wages; monthly deposit and return"],
             ["Employees' State Insurance (ESI)", "Establishments with 10+ employees; employees earning up to INR 21,000 a month", "3.25% employer + 0.75% employee; medical, sickness and maternity cover"],
             ["Gratuity", "On leaving after 5 years' continuous service; fixed-term employees after 1 year (labour codes)", "15 days' wages for each completed year; see the <a href=\"gratuity-calculator-new-labour-codes-2026.html\">gratuity calculator</a>"],
             ["Statutory bonus", "Employees below the wage threshold under the Code on Wages", "8.33% to 20% of wages, paid annually"],
             ["Maternity benefit", "Women employees with the qualifying service", "26 weeks' paid leave; creche facility where the headcount threshold applies"],
             ["Professional tax and labour welfare fund", "Depends on the state (for example Karnataka, Maharashtra, Gujarat, Tamil Nadu)", "Professional tax up to INR 2,500 a year per employee; small welfare-fund contributions"],
             ["Leave, working hours, appointment letters", "All employees (labour codes and state shops and establishments law)", "Written appointment letters, earned leave, overtime at twice the wage rate"]])
         + BOX),
        ("/ Market practice", "Not mandatory, but expected by candidates.",
         ul("<strong>Group health insurance</strong> for employees and family (most foreign-owned employers offer it; ESI-covered employees already have medical cover).",
            "<strong>Parent RSUs or ESOPs:</strong> taxed in India as a perquisite at vesting or exercise; the Indian subsidiary deducts tax through payroll even though the parent grants the shares. If the parent recharges the cost, it needs a recharge agreement and transfer pricing support; see <a href=\"esop-vs-rsu-vs-phantom-stock-india-us.html\">ESOP vs RSU for India-US companies</a>. Employees must report the foreign shares in Schedule FA; see <a href=\"fast-ds-rsu-espp-us-shares-401k-which-category.html\">RSUs and foreign asset reporting</a>.",
            "<strong>National Pension System</strong> employer contribution (tax-efficient for employees), meal cards, internet and phone reimbursements, term life and accident cover.",
            "<strong>Salary structure:</strong> under the labour codes, allowances above 50% of total remuneration are added back to wages, which raises provident fund and gratuity costs; design the structure before the offer letters go out.")),
        ("/ Set-up sequence", "From incorporation to the first payroll.",
         ul("Incorporate the subsidiary (EPFO and ESIC registration numbers are issued through the SPICe+ incorporation form) and get PAN and TAN; see <a href=\"branch-office-vs-liaison-vs-wos-india-foreign.html\">subsidiary vs branch vs liaison office</a>.",
            "Register under the state shops and establishments law and for professional tax in each state where staff sit.",
            "Approve a salary structure, leave policy and appointment letter template compliant with the labour codes.",
            "Run monthly payroll: salary TDS, provident fund and ESI deposits and returns, professional tax; quarterly TDS returns; Form 16 every June (renamed Form 130 from tax year 2026-27).",
            "Agree the parent-subsidiary service arrangement (usually cost plus a markup) and keep transfer pricing documentation; see <a href=\"transfer-pricing-india-foreign-mnc.html\">transfer pricing for foreign MNCs</a>.",
            "Hiring only one or two people first? An employer of record can be faster; see <a href=\"employer-of-record-india-hire-from-abroad.html\">EOR in India</a> and <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">remote employees and PE risk</a>.")
         + '<p>Related: <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies in India</a> &middot; <a href="nominee-resident-director-india-foreign-company.html">resident director for a foreign company</a>.</p>'
         + f'<p><strong>Sources:</strong> Code on Wages, 2019; Code on Social Security, 2020; Industrial Relations Code, 2020; Occupational Safety, Health and Working Conditions Code, 2020 (in force from 21 November 2025, Ministry of Labour and Employment press release); Notification S.O. 5109(E) dated 17 September 2026 (EPF wage ceiling, under section 2(89) of the Code on Social Security), as summarised by Fox Mandal; ESIC wage ceiling unchanged at INR 21,000. Some central and state rules under the codes are still being notified. <em>{UPDATED}</em> General information, not advice for your company.</p>'),
    ],
    faqs=[("What employee benefits are mandatory for an Indian subsidiary of a foreign company?", "Provident fund (12% + 12%, for establishments with 20 or more employees), ESI for employees earning up to INR 21,000 a month (10 or more employees), gratuity, statutory bonus, 26 weeks' paid maternity leave, and state professional tax and labour welfare fund, under the labour codes in force since 21 November 2025."),
          ("What is the EPF wage ceiling in 2026?", "INR 25,000 a month from 17 September 2026 (Notification S.O. 5109(E)), up from INR 15,000. Employees earning up to the ceiling must be covered; employers can cover higher earners voluntarily."),
          ("Is health insurance mandatory for employees in India?", "Private group health insurance is not mandatory, but ESI is mandatory for employees earning up to INR 21,000 a month in establishments with 10 or more employees. Most foreign-owned employers also offer group health cover as market practice."),
          ("When is gratuity payable under the new labour codes?", "After five years of continuous service, and after one year for fixed-term employees. It is 15 days' wages for each completed year of service."),
          ("How are RSUs from a US parent taxed for employees of the Indian subsidiary?", "As a perquisite (salary) in India at vesting, on the fair market value; the Indian subsidiary deducts tax through payroll. Resident employees must also report the foreign shares in Schedule FA of their return."),
          ("Can BQP run payroll compliance for our Indian subsidiary?", "Yes. " + CONTACT)],
    related=[("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "Remote employees, EOR or subsidiary"), ("gratuity-calculator-new-labour-codes-2026.html", "Gratuity calculator"),
             ("india-services-for-foreign-companies-complete-list.html", "Services for foreign companies")],
    cta_h="Hiring in India through a subsidiary?", cta_b=CONTACT,
    keywords="US company India subsidiary employee benefits, UK company India subsidiary benefits, mandatory employee benefits India 2026, EPF wage ceiling 25000, ESIC 21000, gratuity fixed term one year labour codes, payroll setup India subsidiary foreign company, RSU tax India subsidiary employees",
    desc="Employee benefits and payroll for the Indian subsidiary of a US or UK company (2026): mandatory EPF (wage ceiling INR 25,000 from 17 Sept 2026), ESI (INR 21,000), gratuity (1 year for fixed-term staff), bonus, maternity, professional tax under the labour codes, plus market practice and set-up steps.",
    howto={"name": "How a foreign company sets up payroll and benefits for its Indian subsidiary", "description": "Steps from incorporation to first payroll.", "steps": [
        {"name": "Register", "text": "Get EPFO/ESIC numbers via SPICe+, PAN, TAN, shops and establishments and professional tax registrations."},
        {"name": "Design the salary structure", "text": "Keep allowances within the 50% wage rule and decide group health and stock award policies."},
        {"name": "Issue compliant documents", "text": "Appointment letters, leave and working-hour policies under the labour codes."},
        {"name": "Run monthly payroll", "text": "Deduct TDS, deposit PF, ESI and professional tax, and file returns on time."},
        {"name": "Document parent charges", "text": "Put the service and RSU recharge arrangements on paper with transfer pricing support."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CR complete")
