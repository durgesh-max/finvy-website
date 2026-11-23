# -*- coding: utf-8 -*-
"""Batch CM (15 Nov 2026): NRI salary (sweep-3 demand: "nri salary exempt under which section", "nri salary tds rate",
"nri salary in india", seen in all 7 markets).
Facts: salary is earned in India if the services are rendered in India (1961 Act s.9(1)(ii), carried into the Income-tax
Act, 2025), wherever and in whatever currency it is paid; a non-resident is taxed only on income received or deemed
received in India or accruing or arising in India; tribunals have held salary for services rendered wholly outside India
by an NRI is not taxable in India even if credited to an Indian account; CBDT Circular 13/2017 clarified salary of
non-resident seafarers for services outside India credited to an NRE account is not taxable; work done while physically
in India (including remote work during visits) is taxable and the employer deducts TDS on salary; residence tests:
182 days, or 60 days plus 365 in four years (120 days for Indian citizens/PIO visiting with Indian income above INR 15
lakh), deemed residence for Indian citizens with Indian income above INR 15 lakh not taxed elsewhere; treaties
(dependent personal services article) can give relief. Sources: ITAT (Vishal Gulati and others), itatonline, Taxscan,
ClearTax (checked 15 Nov 2026)."""
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


CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your days in India this year and the last four, who pays you and where you work from. "
           "We reply the same working day with your residential status and whether your salary is taxable in India.")
SLUG = "nri-salary-taxable-in-india-remote-work-indian-employer-tds-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Working for an Indian company from Dubai, London or Toronto?</p>'
       f'<p style="margin:0">The contract, your travel log and a residency declaration to the employer decide whether TDS is deducted. Get them aligned before the first payroll, not after the tax notice. '
       f'<a href="{wa("Hi Durgesh, I am an NRI working remotely for an Indian employer. Is my salary taxable in India?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Is an NRI's Salary Taxable in India? (2026): Work Done Abroad vs in India, Remote Work for Indian Employers, TDS and Residence Tests",
    em="where you work decides, not where you are paid.",
    kicker="/ NRI &middot; Salary &middot; Remote work &middot; Updated 2026-11-15",
    lead=("For an NRI, salary is taxable in India <strong>only for work physically done in India</strong>. Indian law treats salary as earned in India when the <strong>services are rendered in India</strong>, wherever it is paid and in whatever currency. "
          "Salary for work done <strong>wholly outside India</strong> is generally not taxed in India even if it is paid into an Indian account; tribunals have held this, and the CBDT clarified it for seafarers' salary credited to NRE accounts (Circular 13/2017). "
          "Days you work from India, including remote work during visits, are taxable and the employer deducts TDS. First check you really are non-resident: the 182-day test, the 60-day and 120-day tests, and deemed residence for Indian citizens with Indian income above INR 15 lakh."),
    sections=[
        ("/ Your situation, and the tax position", "Common cases.",
         table(["Situation", "Taxable in India?"], [
             ["NRI employed and working abroad by a foreign employer, salary paid abroad", "No"],
             ["NRI working abroad for an Indian employer (remote), salary paid into an Indian account", "Generally no, if all services are rendered outside India; keep the contract and travel records"],
             ["NRI working from India during a visit (remote or in office)", "Yes, for the days worked in India; TDS by the employer"],
             ["Seafarer, non-resident, salary for services on foreign voyages credited to NRE", "No (CBDT Circular 13/2017)"],
             ["You become resident (182 days, or 60 + 365 days, or deemed resident)", "Resident: worldwide salary taxable (RNOR relief may apply for a few years after return)"]])
         + BOX),
        ("/ Residence first", "Check this before anything else.",
         table(["Test", "Result"], [
             ["182 days or more in India in the financial year", "Resident"],
             ["60 days in the year and 365 days in the previous four years", "Resident; for Indian citizens leaving for employment abroad, or visiting with Indian income up to INR 15 lakh, the 60 days becomes 182"],
             ["Indian citizen or person of Indian origin visiting with Indian income above INR 15 lakh", "120 days in the year (with 365 in four years) makes you resident (usually RNOR)"],
             ["Indian citizen with Indian income above INR 15 lakh not liable to tax in any other country", "Deemed resident (RNOR); see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for UAE-based Indians</a>"]])),
        ("/ What to do", "Practical steps.",
         ul("Give your Indian employer a written declaration of non-resident status and that services are rendered outside India, with your travel dates, so TDS is not deducted on salary for foreign work.",
            "Keep a day-count log and boarding passes for every year; residence is tested each financial year.",
            "If you work from India for some days, expect TDS on that part; split salary by days if the employer agrees.",
            "If TDS was deducted on salary for foreign work, claim it back in your Indian return.",
            "Your country of residence may tax the salary; India's treaties (dependent personal services article) and foreign tax credits prevent double tax.")
         + '<p>Related: <a href="nri-taxation-india-complete-guide.html">NRI taxation guide</a> &middot; <a href="foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html">foreign employers with staff in India</a> &middot; <a href="best-ca-nri-returning-india-rnor-planning.html">returning to India and RNOR</a> &middot; <a href="nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html">EPF withdrawal for NRIs</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 1961, sections 5, 6 and 9(1)(ii) (carried into the Income-tax Act, 2025); CBDT Circular No. 13/2017 (seafarers); ITAT rulings on salary for services rendered outside India (for example Vishal Gulati). Secondary summaries checked 15 November 2026: itatonline, Taxscan, ClearTax. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is NRI salary taxable in India?", "Only for work physically done in India. Salary for services rendered wholly outside India is generally not taxable in India for a non-resident, even if paid into an Indian account."),
          ("Under which section is NRI salary exempt?", "There is no specific exemption section; salary for services rendered outside India simply does not accrue in India under the source rule (section 9(1)(ii) of the 1961 Act, carried into the 2025 Act), so a non-resident is not taxed on it."),
          ("I work remotely from abroad for an Indian company. Is my salary taxable?", "Generally not, if you are non-resident and do all the work outside India. Give the employer a declaration with travel dates; days worked from India are taxable."),
          ("What TDS applies to NRI salary?", "Salary for work done in India is subject to TDS at slab rates like any salary. Salary for work done outside India should not attract TDS if the employer is satisfied it is not taxable in India."),
          ("Is salary credited to an NRE account taxable?", "Not merely because it is credited there; the CBDT clarified for non-resident seafarers that salary for services outside India credited to an NRE account is not taxable."),
          ("Is salary earned outside India by a resident taxable in India?", "Yes, if you are resident and ordinarily resident: worldwide income, including salary earned abroad, is taxable in India, with credit for foreign tax under the treaty (Form 67, Form 44 from tax year 2026-27). A resident but not ordinarily resident (RNOR) person is not taxed on foreign salary received abroad. Residence depends on your days in India each tax year."),
          ("Do I need to pay income tax in India if I work overseas?", "Not on the overseas salary if you are non-resident for the year. An Indian citizen who leaves India for employment abroad is non-resident if in India for less than 182 days in that tax year; the 60-day test does not apply. Salary for work done in India before you left is still taxable."),
          ("Is Dubai salary tax free in India?", "For a non-resident, yes: salary for work done in the UAE is not taxed in India, and the UAE has no personal income tax. An Indian citizen in the UAE whose Indian income exceeds INR 15 lakh can be a deemed resident, but deemed residents are treated as RNOR, so the UAE salary is still not taxed in India."),
          ("Can BQP confirm my position?", "Yes. " + CONTACT)],
    related=[("nri-taxation-india-complete-guide.html", "NRI taxation guide"), ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed residence for UAE-based Indians"),
             ("best-ca-nri-returning-india-rnor-planning.html", "Returning to India and RNOR")],
    cta_h="Not sure if your salary is taxable in India?", cta_b=CONTACT,
    keywords="NRI salary taxable in India, NRI salary exempt under which section, NRI salary TDS rate, NRI remote work Indian employer tax, salary for services rendered outside India, salary credited to NRE account taxable, NRI salary in India tax 2026",
    desc="Is an NRI's salary taxable in India in 2026? Only for work physically done in India (source rule), not for work done abroad even if paid into an Indian account; remote work for Indian employers, TDS, seafarers (Circular 13/2017), residence tests and deemed residence.",
    howto={"name": "How an NRI checks whether salary is taxable in India", "description": "Steps for NRIs paid by Indian or foreign employers.", "steps": [
        {"name": "Confirm residential status", "text": "Count days in India this year and the previous four; check the INR 15 lakh rules."},
        {"name": "Map where the work is done", "text": "Separate days worked in India from days worked abroad."},
        {"name": "Tell the employer", "text": "Give a written non-resident declaration with travel dates so TDS is applied only to India-sourced salary."},
        {"name": "File and claim relief", "text": "Claim refunds of excess TDS in India and use treaty relief or foreign tax credit abroad."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CM complete")
