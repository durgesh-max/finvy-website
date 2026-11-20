# -*- coding: utf-8 -*-
"""Batch EP (21 Nov 2026): India's social security agreements (totalization) - full list, the India-UK Double Contributions
Convention in force from 15 July 2026, no agreement with the US, certificate of coverage, international worker PF.
Call-first page for foreign companies posting staff to India and Indian companies posting staff abroad.
Demand: sweep 21 Nov 2026 (ac31), all 7 markets: "does india and us have totalization agreement", "india us
totalization agreement", "india us social security agreement", "us india social security totalization agreement".
Facts (checked 21 Nov 2026):
- MEA 'Social Security Agreements' page: Active - Belgium, France, Switzerland, Luxembourg, Netherlands, Hungary, Denmark,
  Czech Republic, South Korea, Norway, Germany, Finland, Canada, Japan, Sweden, Austria, Portugal, Canada (Quebec),
  Australia, Brazil, United Kingdom (contributions only). Signed, not yet in force - Argentina, Poland. No US entry.
- KPMG GMS Flash Alert 2026-154: India-UK Double Contributions Convention takes effect 15 July 2026; certificate of
  coverage for assignments starting on or after that date, up to 60 months (36 months initially announced); employee
  must have been under home legislation at least 30 days before, or contributions paid for the prior calendar month;
  people already on assignment on that date are not covered; six-month cooling-off between assignments; no rule for
  people working in both countries (contributions can be due in both).
- International workers: foreign nationals employed by a covered Indian establishment contribute to provident fund on
  full salary unless excluded by a certificate of coverage under an agreement (site expat page; EPF Scheme 2026 replaced
  the 1952 scheme on 29 June 2026 - readers told to check the current text).
- No India-US totalization agreement (site US pages; SSA list)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage"

C = contact("the two countries involved, who employs the person, the assignment dates and whether a certificate of coverage has been applied for")
PAGES = [dict(
    slug=SLUG,
    title="India's Social Security Agreements (2026): Full List, the New UK Convention from 15 July 2026, No US Totalization Agreement, and the Certificate of Coverage",
    em="for companies sending employees to or from India.",
    kicker="/ Foreign companies &middot; Expats &middot; Provident fund &middot; Updated 2026-11-21",
    lead=("<strong>India has no social security (totalization) agreement with the United States.</strong> A US employee posted to India, or an Indian employee posted to the US, can end up paying into both systems. "
          "India has <strong>21 agreements in force</strong>: Belgium, France, Switzerland, Luxembourg, the Netherlands, Hungary, Denmark, the Czech Republic, South Korea, Norway, Germany, Finland, Canada, Quebec, Japan, Sweden, Austria, Portugal, Australia, Brazil and, newest, the <strong>United Kingdom</strong>. Agreements with Argentina and Poland are signed but not yet in force. "
          "The <strong>India-UK Double Contributions Convention</strong> took effect on <strong>15 July 2026</strong>. An employee sent from one country to the other on or after that date can stay in the home country&rsquo;s system for up to <strong>60 months</strong> with a <strong>certificate of coverage</strong>. People who were already on assignment on that date are not covered. "
          "Without a certificate, a foreign national employed in India is an <strong>international worker</strong> and provident fund is due on full salary."),
    sections=[
        ("/ The list", "Where a certificate of coverage is available.",
         table(["Status", "Countries", "What it means"], [
             ["In force", "Belgium, France, Switzerland, Luxembourg, Netherlands, Hungary, Denmark, Czech Republic, South Korea, Norway, Germany, Finland, Canada, Quebec, Japan, Sweden, Austria, Portugal, Australia, Brazil", "Posted employees with a certificate of coverage contribute only in the home country; most agreements also allow periods to be added together for pensions and benefits to be paid abroad"],
             ["In force from 15 July 2026", "United Kingdom (Double Contributions Convention)", "Contributions only: home-country cover for up to 60 months with a certificate; it does not combine pension periods"],
             ["Signed, not yet in force", "Argentina, Poland", "No relief yet"],
             ["No agreement", "United States, UAE and other Gulf countries, Singapore, and others", "Contributions can be due in both countries; check each country&rsquo;s domestic rules"]])
         + call_box("Social security for employees moving to or from India", ["Whether an agreement applies and for how long",
                                                                           "Getting the certificate of coverage in time",
                                                                           "Provident fund for international workers without a certificate",
                                                                           "Income tax, residency and treaty relief for the assignee",
                                                                           "Permanent establishment risk for the employer"],
                    "the countries, employer, role, assignment start and end dates and current payroll arrangements.")),
        ("/ India and the UK from 15 July 2026", "The Double Contributions Convention.",
         ul("<strong>Who:</strong> employees sent by their employer from India to the UK, or from the UK to India, on or after 15 July 2026.",
            "<strong>Relief:</strong> with a certificate of coverage, contributions continue only in the home country for up to 60 months (36 months was the figure first announced).",
            "<strong>Condition:</strong> the employee was under the home country&rsquo;s social security law for at least 30 days before the assignment, or contributions were paid for the calendar month before it starts.",
            "<strong>Already on assignment on 15 July 2026:</strong> not covered; the host country&rsquo;s rules apply.",
            "<strong>Repeat assignments:</strong> a six-month gap is needed before a new certificate (or a gap equal to the last assignment if that was shorter).",
            "<strong>Working in both countries:</strong> the convention has no rule for this, so contributions can be due in both.",
            "See also <a href=\"indian-ca-for-clients-in-uk.html\">Indian CA for UK clients</a> and the <a href=\"india-uk-tax-treaty-dtaa.html\">India-UK tax treaty</a>.")),
        ("/ Certificate of coverage and international workers", "How it works in India.",
         ul("<strong>Coming to India:</strong> get the certificate from the home country&rsquo;s social security authority before the assignment starts and give it to the Indian employer; the employee is then excluded from Indian provident fund for the certified period.",
            "<strong>Going abroad from India:</strong> the Indian employer applies to EPFO for the certificate so the employee is exempt from the host country&rsquo;s contributions.",
            "<strong>No certificate:</strong> a foreign national employed by a covered Indian establishment is an international worker and contributes on full salary; withdrawal is restricted. Check the current EPF scheme text (the EPF Scheme, 2026 replaced the 1952 scheme on 29 June 2026).",
            "<strong>United States:</strong> no agreement, so work years in one country do not count in the other and double contributions are possible; see <a href=\"us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html\">US Social Security and India</a>.",
            "<strong>Tax is separate:</strong> income-tax residency and treaty relief follow different rules; see <a href=\"expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html\">expat tax in India</a> and <a href=\"foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html\">payroll and benefits for an Indian subsidiary</a>.")
         + '<p>Related: <a href="permanent-establishment-risk-checker-india-foreign-company-2026.html">PE risk checker</a> &middot; <a href="employer-of-record-india-hire-from-abroad.html">employer of record in India</a> &middot; <a href="india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html">India entry structure chooser</a>.</p>'
         + sources("Ministry of External Affairs, 'Social Security Agreements' (status list, viewed 21 November 2026); KPMG GMS Flash Alert 2026-154, 'United Kingdom - Social Security Agreement with Republic of India' (entry into force 15 July 2026, 60 months, eligibility and transitional rules), citing the GOV.UK explainer of 17 June 2026; EPFO rules on international workers and certificates of coverage. Each agreement has its own maximum period and conditions; check the agreement text before an assignment.")),
    ],
    faqs=[("Does India have a totalization agreement with the US?", "No. India and the United States have no social security agreement in force, so contributions can be due in both countries and work periods are not combined."),
          ("Which countries have a social security agreement with India?", "In force: Belgium, France, Switzerland, Luxembourg, the Netherlands, Hungary, Denmark, the Czech Republic, South Korea, Norway, Germany, Finland, Canada, Quebec, Japan, Sweden, Austria, Portugal, Australia, Brazil and the United Kingdom. Argentina and Poland are signed but not yet in force."),
          ("When did the India-UK social security agreement start?", "The India-UK Double Contributions Convention took effect on 15 July 2026. Employees posted on or after that date can stay in the home system for up to 60 months with a certificate of coverage."),
          ("What is a certificate of coverage?", "A document from the home country's social security authority confirming the employee remains covered there, which exempts them from the host country's contributions for the certified period."),
          ("Do foreign employees pay provident fund in India?", "Yes, as international workers on full salary, unless they hold a certificate of coverage under a social security agreement."),
          ("Can BQP help with an assignment to or from India?", "Yes. " + C)],
    related=[("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "Expat tax in India"),
             ("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Payroll and benefits for an Indian subsidiary"),
             ("us-social-security-taxable-in-india-dtaa-article-20-returning-nri.html", "US Social Security and India")],
    cta_h="Sending an employee to or from India?", cta_b=C,
    keywords="India US totalization agreement, India social security agreement countries list 2026, India UK Double Contributions Convention 15 July 2026, certificate of coverage India EPFO, international worker provident fund India, India UK social security agreement",
    desc="India's social security agreements (2026): 21 in force including the UK Double Contributions Convention from 15 July 2026 (60 months with a certificate of coverage); no US totalization agreement; Argentina and Poland pending; international worker PF without a certificate.",
    howto={"name": "How to avoid double social security contributions on an India assignment", "description": "Steps for the employer.", "steps": [
        {"name": "Check for an agreement", "text": "See whether the two countries have a social security agreement in force."},
        {"name": "Check the conditions", "text": "Maximum period, prior coverage and start date rules."},
        {"name": "Apply for the certificate of coverage", "text": "From the home country's authority (EPFO for employees leaving India), before the assignment starts."},
        {"name": "Set up payroll", "text": "Exclude the employee from host-country contributions for the certified period."},
        {"name": "Review tax separately", "text": "Residency, treaty relief and permanent establishment."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EP complete")
