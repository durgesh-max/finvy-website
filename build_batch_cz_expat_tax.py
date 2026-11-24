# -*- coding: utf-8 -*-
"""Batch CZ (18 Nov 2026): expatriate (foreign national) tax in India. Demand: autocomplete 18 Nov 2026 - "expat tax
india", "expat in india" in all 7 markets; no page on the site.
Facts: residence tests for a foreign national - 182 days in the tax year, or 60 days plus 365 days in the previous
four years (the 120/182-day relaxations apply only to Indian citizens/PIOs); newcomers are usually non-resident or
RNOR for the first two to three years (non-resident in 9 of 10 previous years, or 729 days or less in the previous 7
years), taxed only on Indian-source income; salary for services rendered in India is earned in India wherever paid;
short-stay exemption for a foreign citizen employed by a foreign enterprise not carrying on business in India, stay
of 90 days or less (1961 Act s.10(6)(vi), narrow) and the treaty dependent-personal-services 183-day rule with
conditions; Indian employer deducts salary TDS; foreign-paid salary needs advance tax/self-assessment; Indian EPF
applies to 'international workers' on full salary unless a certificate of coverage under a social security agreement
applies (India has agreements with about 19-20 countries, e.g. Germany, France, Japan, Netherlands, Switzerland,
South Korea, Australia, Canada); FRRO registration for long-stay visas; Schedule FA foreign asset reporting only for
resident and ordinarily resident individuals. Sources: PwC Worldwide Tax Summaries, Alliott Global, TaxGuru (checked
18 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the employee's nationality, arrival date, expected stay, who pays the salary and any home-country social security cover. "
           "We reply within one working day with the residency position, tax and PF treatment, and a fixed-scope quote.")
SLUG = "expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Sending an employee to India, or hiring a foreigner here?</p>'
       f'<p style="margin:0">Residency, who pays the salary, provident fund and the treaty decide the cost. Getting it right before arrival avoids back-tax for the employee and permanent establishment questions for the employer. '
       f'<a href="{wa("Hi Durgesh, we are sending a foreign employee to India. Can you advise on tax and PF?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Expat Tax in India (2026): How Foreign Employees Are Taxed, Residency and RNOR, Salary Paid Abroad, Provident Fund and Treaty Relief",
    em="for expatriates and the companies that send them.",
    kicker="/ Foreign companies &middot; Expatriates &middot; Payroll &middot; Updated 2026-11-18",
    lead=("A foreign national working in India is taxed on <strong>salary for work done in India</strong>, wherever and in whatever currency it is paid. How much else is taxed depends on <strong>residency</strong>: a foreigner becomes resident after <strong>182 days</strong> in India in a tax year (or 60 days plus 365 days in the previous four years), but is usually <strong>RNOR (resident but not ordinarily resident)</strong> for the first two or three years, so <strong>foreign income stays outside Indian tax</strong> during that time. "
          "Short visits can be exempt: a <strong>90-day exemption</strong> applies to employees of a foreign employer with no business in India, and most <strong>tax treaties exempt stays under 183 days</strong> when a foreign employer pays and bears the salary. "
          "Expatriates are also <strong>'international workers' for Indian provident fund</strong>, contributing on full salary unless their home country has a <strong>social security agreement</strong> with India and they hold a certificate of coverage."),
    sections=[
        ("/ Residency and what is taxed", "The first question.",
         table(["Status", "Test for a foreign national", "Taxed in India on"], [
             ["Non-resident", "Below 182 days, and not 60 + 365 days", "Indian-source income only (including salary for work in India)"],
             ["Resident but not ordinarily resident (RNOR)", "Resident, and non-resident in 9 of the previous 10 years or in India 729 days or less in the previous 7 years", "Indian income, plus foreign income from a business controlled or profession set up in India; foreign salary for work abroad and foreign investment income stay out"],
             ["Resident and ordinarily resident", "Resident and does not meet the RNOR tests (usually from year three or four)", "Worldwide income; foreign assets reported in Schedule FA; foreign tax credit under treaties"]])
         + BOX),
        ("/ Salary, short stays and payroll", "How it works in practice.",
         ul("<strong>Salary for work in India is taxable in India</strong> even if a foreign parent pays it into a foreign account; if the Indian entity bears or recharges the cost, the Indian entity normally runs payroll and deducts TDS.",
            "<strong>Salary paid abroad</strong> and not routed through Indian payroll: the employee pays advance tax and files an Indian return.",
            "<strong>90-day exemption</strong> (section 10(6)(vi) of the 1961 Act, carried forward): a foreign citizen employed by a foreign enterprise that carries on no business in India, staying 90 days or less in the year, with pay not deducted by an Indian business. Narrow in practice.",
            "<strong>Treaty 183-day rule</strong>: most treaties exempt salary if the stay is under 183 days (in the year or a 12-month period, depending on the treaty), the employer is not resident in India and the cost is not borne by an Indian entity or permanent establishment. Needs a tax residency certificate and Form 41.",
            "<strong>Perquisites</strong> such as rent-free accommodation, school fees and tax paid by the employer (tax equalisation) are taxable salary.",
            "<strong>Permanent establishment</strong>: an employee working in India for a foreign company can create a PE for the employer; see <a href=\"permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html\">PE risk</a>.")),
        ("/ Provident fund, registration and exit", "Often missed.",
         ul("<strong>Provident fund</strong>: foreign nationals employed by an Indian establishment are 'international workers' and contribute on full salary, unless covered by a social security agreement (India has 21 in force, including Germany, France, Japan, the Netherlands, Switzerland, South Korea, Australia, Canada and, from 15 July 2026, the United Kingdom; there is none with the United States; see the <a href=\"india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage.html\">full list</a>) and a certificate of coverage is issued. Check the current EPF scheme text, which was revised in 2026.",
            "<strong>Registration</strong>: foreigners on long-stay visas register with the Foreigners Regional Registration Office (FRRO) after arrival.",
            "<strong>Indian return</strong>: file every year in which there is taxable Indian income; claim treaty relief and foreign tax credit (Form 67) where relevant.",
            "<strong>Leaving India</strong>: settle final tax, claim refunds of excess TDS, and plan provident fund withdrawal under the scheme or the social security agreement.")
         + '<p>Related: <a href="foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html">employee benefits and payroll for foreign-owned subsidiaries</a> &middot; <a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a> &middot; <a href="foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html">remote employees and EOR</a> &middot; <a href="form-67-foreign-tax-credit-india-2026.html">Form 67 foreign tax credit</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961, sections 5, 6, 9(1)(ii) and 10(6)(vi), carried into the Income-tax Act, 2025; India&rsquo;s tax treaties (dependent personal services articles); Employees&rsquo; Provident Fund Scheme (international workers) and India&rsquo;s social security agreements. Secondary summaries checked 18 November 2026: PwC Worldwide Tax Summaries, Alliott Global, TaxGuru. <em>{UPDATED}</em> General information, not advice for a specific assignment.</p>'),
    ],
    faqs=[("How are expats taxed in India?", "On salary for work done in India, wherever paid. Residency decides the rest: non-residents and RNORs (usually the first two or three years) are taxed only on Indian income; resident and ordinarily resident expats are taxed on worldwide income."),
        ("How is a US citizen working in India taxed?", "Twice in principle, relieved in practice. India taxes salary for work done in India, and once resident (182 days or more, or the 60-day rule) taxes wider income, with relief for the first years as RNOR. The US taxes its citizens on worldwide income wherever they live, so the US return usually claims the foreign earned income exclusion or a foreign tax credit for Indian tax, using the India-US treaty where needed. US citizens in India also file FBAR and FATCA reports for Indian accounts."),
        ("Does a US citizen working in India pay Indian provident fund or US Social Security?", "India and the US have no social security agreement, so a US citizen on an Indian payroll is usually an international worker who contributes to Indian provident fund on full salary, while someone kept on a US payroll may also owe US Social Security. Which applies depends on who employs and pays the person, so plan the employment structure before the move."),
          ("When does a foreign national become tax resident in India?", "After 182 days in India in a tax year, or 60 days in the year plus 365 days in the previous four years. The relaxed 120-day and 182-day variants apply only to Indian citizens and persons of Indian origin."),
          ("Is there a short-stay exemption for foreign employees?", "Yes, two: a 90-day exemption for employees of a foreign enterprise with no business in India, and the treaty rule exempting stays under 183 days where a non-resident employer pays and bears the salary. Both have conditions."),
          ("Do expats contribute to Indian provident fund?", "Usually yes, as 'international workers', on full salary, unless their home country has a social security agreement with India and they hold a certificate of coverage."),
          ("Do expats report foreign assets in India?", "Only once they are resident and ordinarily resident; RNORs and non-residents do not file Schedule FA."),
          ("Can BQP handle expat tax and payroll?", "Yes. " + CONTACT)],
    related=[("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Employee benefits for foreign-owned subsidiaries"), ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             ("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment risk")],
    cta_h="Expatriates working in India?", cta_b=CONTACT,
    keywords="expat tax India, expatriate taxation India 2026, foreign employee tax India, RNOR expat India, 90 day exemption foreign employee India, 183 day rule DTAA India, international worker provident fund India, social security agreement India certificate of coverage",
    desc="Expat tax in India (2026): salary for work in India taxed wherever paid; 182-day and 60/365-day residency tests; RNOR for the first years; 90-day and treaty 183-day exemptions; perquisites; international worker provident fund and social security agreements; FRRO and exit steps.",
    howto={"name": "How a company plans an expatriate's tax in India", "description": "Steps before and during an India assignment.", "steps": [
        {"name": "Project the days", "text": "Estimate days in India per tax year to see residency and RNOR status."},
        {"name": "Decide who pays", "text": "Indian payroll with TDS, or foreign payroll with advance tax; check treaty short-stay conditions."},
        {"name": "Check provident fund", "text": "Apply international worker rules or obtain a certificate of coverage under a social security agreement."},
        {"name": "Review PE risk", "text": "Check whether the employee's work creates a permanent establishment for a foreign employer."},
        {"name": "File and exit cleanly", "text": "Annual returns, foreign tax credit claims, and final tax and PF settlement on departure."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CZ complete")
