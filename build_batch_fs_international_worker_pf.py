# -*- coding: utf-8 -*-
"""Batch FS (23 Nov 2026): PF for foreign employees in India ('international workers') - who is covered, how it is
calculated (12% + 12% on full wages, no ceiling), certificate of coverage, the court split, and what employers should do.
Call-first page for foreign companies and expats.
Demand: sweep 23 Nov 2026 (ac46, foreign), all 7 markets: "how is pf calculated for international workers in india".
Site mentioned international workers on several pages but had no page explaining the calculation.
Facts (checked 23 Nov 2026):
- EPF Scheme, 2026 (in force from 1 July 2026 per LKS; notified 29 June 2026 per site page) carries forward the
  international worker framework of paragraph 83 of the 1952 Scheme and paragraph 43A of EPS 1995; UK now expressly
  within the framework after the Double Contributions Convention (LKS Attorneys, 18 Sept 2026).
- International worker: a foreign national working for an EPF-covered establishment in India, unless from a country with
  a social security agreement and holding a certificate of coverage; also Indian employees working in SSA countries
  (Beacon Filing; LKS).
- Contributions on full wages with no ceiling; employee 12%, employer 12% (all to EPF for a worker joining above the
  ceiling; an existing EPS member has 8.33% of wages up to INR 25,000 to EPS); EDLI 0.5% (Beacon Filing table).
- Wage ceiling for Indian employees INR 25,000 from 17 Sept 2026 (PIB; Gazette S.O. 5109(E)).
- Courts: Karnataka HC, Stone Hill Education Foundation v. Union of India (2024) struck down the IW provisions; Delhi HC,
  SpiceJet / LG Electronics v. Union of India (4 Nov 2025) upheld them; Supreme Court issued notice in March 2026 and
  directed no final orders in section 7A proceedings against the petitioners while pending (Bar & Bench, Cyril
  Amarchand client alert). Practitioner advice: keep contributing on full wages and preserve refund claims.
- ESI: covers employees earning up to INR 21,000 a month, so most international workers fall outside it."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "pf-for-foreign-employees-india-international-worker-epf-calculation-full-salary-certificate-of-coverage-2026"

C = contact("the employee's nationality, monthly salary and its components, assignment length, whether they hold a certificate of coverage from their home country, and the state where the Indian entity is registered")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="PF for Foreign Employees in India (2026): How International Worker EPF Is Calculated - 12% Plus 12% on Full Salary, Certificates of Coverage and the Court Challenge",
    em="no wage ceiling, unless a social security agreement applies.",
    kicker="/ Foreign companies &middot; Payroll &middot; Provident fund &middot; Updated 2026-11-23",
    lead=("<strong>A foreign national employed by an Indian company is an &lsquo;international worker&rsquo; for provident fund, and contributes on the full salary, with no wage ceiling.</strong> "
          "The employee pays <strong>12%</strong> of PF wages and the employer another <strong>12%</strong>, plus insurance and administration charges. Indian employees, by contrast, are covered compulsorily only up to wages of INR 25,000 a month. "
          "The exemption is a <strong>certificate of coverage</strong>: a worker from a country with a social security agreement with India, who keeps contributing at home, does not pay Indian PF. "
          "Courts are split on whether full-salary PF for foreigners is constitutional, and the Supreme Court is hearing the question, but the rule is <strong>in force under the EPF Scheme, 2026</strong>, so most advisers say keep contributing. "
          "Get the certificate <strong>before</strong> the assignment starts."),
    sections=[
        ("/ How it is calculated", "International worker vs Indian employee.",
         table(["", "International worker", "Indian employee"], [
             ["Wages for PF", "Full PF wages, no ceiling", "Compulsory up to INR 25,000 a month (from 17 September 2026); above that by choice"],
             ["Employee contribution", "12% of full PF wages", "12% of wages up to the ceiling"],
             ["Employer contribution", "12% of full PF wages; all to the provident fund for a worker who joins above the ceiling (an existing pension-scheme member has part diverted to the pension scheme)", "12%, of which 8.33% of wages up to INR 25,000 goes to the pension scheme"],
             ["Insurance (EDLI) and admin", "Paid by the employer", "Paid by the employer"],
             ["Exemption", "Certificate of coverage from a social security agreement country", "Not applicable"]])
         + '<p><strong>Illustration:</strong> a foreign national with PF wages of INR 3,00,000 a month contributes INR 36,000 a month; the employer adds INR 36,000 plus insurance and administration charges. An Indian employee on the same wages would be compulsorily covered only on INR 25,000.</p>'
         + call_box("Foreign nationals on an Indian payroll", ["Whether each employee is an international worker",
                                                               "Certificates of coverage and detachment periods",
                                                               "PF wages, calculation and monthly returns",
                                                               "Past periods under-contributed: exposure and fixes",
                                                               "Tax on the employee&rsquo;s salary and residence status"],
                    "nationality, salary breakdown, assignment length, certificate of coverage status and the state of registration.")),
        ("/ Certificates of coverage", "The way out, if your country has an agreement.",
         ul("<strong>Who qualifies:</strong> nationals of countries with a social security agreement with India, sent to India and still covered at home. India has agreements in force with countries including Germany, France, Japan, the Netherlands, Switzerland and, since 15 July 2026, the United Kingdom. There is no agreement with the United States. See the " + L("india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage.html", "list of agreements") + ".",
            "<strong>Timing:</strong> obtain it from the home authority before or at the start of the assignment and keep it on file; renew it if the assignment is extended.",
            "<strong>Without it:</strong> even a national of an agreement country is treated as an international worker and contributes on full wages.",
            "<strong>Gulf and US nationals:</strong> no agreement, so international worker rules apply in full.")),
        ("/ The court challenge", "What employers should do while it is pending.",
         ul("<strong>Karnataka High Court (2024):</strong> struck down the international worker provisions as unequal, because Indian employees have a ceiling and foreigners do not.",
            "<strong>Delhi High Court (4 November 2025):</strong> upheld the same provisions as a permissible policy choice.",
            "<strong>Supreme Court (March 2026):</strong> issued notice on the challenge and told the authorities not to pass final orders against the petitioners while it is pending. No final judgment yet.",
            "<strong>EPF Scheme, 2026:</strong> carries the same framework forward, so the obligation continues.",
            "<strong>Practical course:</strong> keep contributing on full wages and keep records, so that a refund can be claimed if the provisions are struck down. Cutting contributions now risks arrears, interest and damages if they are upheld.",
            "<strong>Other benefits:</strong> state insurance (ESI) covers only wages up to INR 21,000 a month, so most international workers are outside it. Gratuity applies to foreign employees as to Indian ones; see the " + L("gratuity-calculator-new-labour-codes-2026.html", "gratuity calculator") + ".")
         + '<p>Related: ' + L("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "tax for foreign employees in India") + ' &middot; ' + L("epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition.html", "EPF Scheme 2026") + ' &middot; ' + L("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "payroll benefits for a foreign-owned subsidiary") + ' &middot; ' + L("employer-of-record-india-hire-from-abroad.html", "employer of record") + ' &middot; ' + L("doing-business-in-india-2026-guide-for-foreign-companies-entity-tax-fdi-compliance-repatriation.html", "doing business in India") + '.</p>'
         + sources("Employees&rsquo; Provident Funds Scheme, 2026 (international worker framework carried forward from paragraph 83 of the 1952 Scheme and paragraph 43A of EPS 1995), as analysed by LKS Attorneys (18 September 2026); EPFO wage ceiling of INR 25,000 from 17 September 2026 (PIB; Gazette S.O. 5109(E)); Stone Hill Education Foundation v. Union of India (Karnataka High Court, 2024); SpiceJet Ltd and LG Electronics India Pvt Ltd v. Union of India (Delhi High Court, 4 November 2025); Supreme Court notice of March 2026 (Bar &amp; Bench; Cyril Amarchand Mangaldas client alert); Beacon Filing guide to international worker contributions. Checked 23 November 2026.")),
    ],
    faqs=[("Do foreign employees in India have to contribute to PF?", "Yes. A foreign national working for an Indian establishment covered by the EPF law is an international worker and contributes, unless they come from a country with a social security agreement with India and hold a certificate of coverage."),
          ("How is PF calculated for international workers in India?", "On the full PF wages with no ceiling: 12% from the employee and 12% from the employer, plus employer-paid insurance and administration charges. Indian employees are compulsorily covered only up to wages of INR 25,000 a month."),
          ("How can a foreign employee avoid Indian PF?", "By holding a certificate of coverage from a country that has a social security agreement with India, showing they remain covered by their home system during the Indian assignment."),
          ("Does India have a social security agreement with the US or UAE?", "No. US and Gulf nationals working in India are international workers without an exemption. The UK has been covered since 15 July 2026."),
          ("Is full-salary PF for foreign workers still valid after the Karnataka High Court ruling?", "The Karnataka High Court struck the provisions down in 2024, the Delhi High Court upheld them in November 2025, and the Supreme Court is hearing the question. The EPF Scheme, 2026 keeps the rule, so most advisers recommend continuing to contribute and preserving a refund claim."),
          ("Can BQP run PF for our foreign employees in India?", "Yes. " + C)],
    related=[("india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage.html", "Social security agreements"),
             ("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "Tax for foreign employees in India"),
             ("epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition.html", "EPF Scheme 2026")],
    cta_h="Foreign nationals on your Indian payroll?", cta_b=C,
    keywords="PF for foreign employees India, international worker PF India, how is PF calculated for international workers, EPF foreign nationals full salary no ceiling, certificate of coverage India PF, social security agreement India PF exemption, Stone Hill Karnataka High Court PF, EPF Scheme 2026 international workers",
    desc="PF for foreign employees in India (2026): international workers contribute 12% + 12% on full salary with no ceiling (Indian employees: INR 25,000), unless they hold a certificate of coverage from a social security agreement country. Court split and Supreme Court status, and what employers should do.",
    howto={"name": "How an Indian employer handles PF for a foreign national", "description": "International worker steps.", "steps": [
        {"name": "Check nationality and agreement", "text": "Is there a social security agreement with the home country?"},
        {"name": "Get the certificate of coverage", "text": "Before or at the start of the assignment, if the country has an agreement."},
        {"name": "Register as an international worker", "text": "If no certificate applies."},
        {"name": "Contribute on full wages", "text": "12% employee and 12% employer, plus insurance and admin charges."},
        {"name": "Keep records", "text": "To support a refund claim if the Supreme Court strikes the rule down."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FS complete")
