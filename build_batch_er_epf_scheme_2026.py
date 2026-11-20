# -*- coding: utf-8 -*-
"""Batch ER (21 Nov 2026): EPF Scheme 2026 (with EPS 2026 and EDLI 2026) - what changed for employers, foreign-owned
Indian subsidiaries, international workers and NRIs withdrawing PF. Call-first page.
Facts (checked 21 Nov 2026; Nexdigm 'New EPF, EPS and EDLI Schemes 2026'; TaxGuru 'EPF Scheme 2026: Ten Major Changes',
18 July 2026; Lexplosion; site payroll page for the wage ceiling):
- Notified 29 June 2026 by the Ministry of Labour and Employment under the Code on Social Security, 2020: EPF Scheme, 2026
  (G.S.R. 525(E), section 15(1)(a)), EPS, 2026 and EDLI Scheme, 2026, replacing the 1952, 1995 and 1976 schemes; existing
  members, balances and service continue; special provisions EEC 2026, VISHWAS 2026, AMNESTY 2026.
- Contributions 12% on 'wages' as defined in the Code (replacing 'basic wages'); mandatory membership up to the notified
  wage ceiling (INR 15,000 at notification; INR 25,000 from 17 September 2026, S.O. 5109(E) - site payroll page); higher
  earners are excluded employees who can join by option; voluntary contributions above the ceiling need not be matched.
- Aadhaar, PAN and seeded bank account mandatory; UAN for every employee; e-nomination, nomination made before marriage
  invalid; monthly electronic return (ECR) within 15 days after month end; late fee INR 500 a day for delayed returns.
- Withdrawals: partial after 12 months of membership, keeping 25% of contributions; full withdrawal on retirement after
  55, permanent incapacity, migration from India for permanent settlement abroad; otherwise 12 months after leaving
  employment. EPS withdrawal benefit only after 36 months from the last contribution or at superannuation; pension can be
  deferred from 58 to 60 with 4% increase a year; minimum pension INR 1,000.
- EDLI: minimum INR 2.5 lakh and maximum INR 7 lakh for members with 12 months' continuous employment.
- International worker provisions are now in the main scheme text (TaxGuru); certificate of coverage under social
  security agreements continues (site SSA page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "epf-scheme-2026-changes-employers-foreign-subsidiaries-nri-withdrawal-12-months-wages-definition"

C = contact("whether you are an employer or an employee, your payroll structure (basic pay and allowances), headcount, any foreign nationals on payroll, or your PF withdrawal situation")
PAGES = [dict(
    slug=SLUG,
    title="EPF Scheme 2026: What Changed for Employers, Foreign-Owned Subsidiaries and NRIs - New Wage Definition, INR 25,000 Ceiling, 12-Month Withdrawal Rule",
    em="the new provident fund rules that replaced the 1952 scheme.",
    kicker="/ Payroll &middot; Provident fund &middot; Labour codes &middot; Updated 2026-11-21",
    lead=("On <strong>29 June 2026</strong> the government notified the <strong>Employees&rsquo; Provident Fund Scheme, 2026</strong>, with new pension (EPS 2026) and insurance (EDLI 2026) schemes, under the Code on Social Security. They <strong>replace the 1952, 1995 and 1976 schemes</strong>. Existing members, balances and service carry over. "
          "For employers, the main changes are that the 12% contribution is now worked out on <strong>&ldquo;wages&rdquo; as defined in the Code</strong>, not just basic pay; the mandatory wage ceiling is <strong>INR 25,000 a month from 17 September 2026</strong>; and Aadhaar, PAN, e-nomination and monthly electronic returns are compulsory, with a late fee of INR 500 a day. "
          "For employees, <strong>full withdrawal after leaving a job now needs 12 months</strong> without employment, where it used to be two. Partial withdrawals are simpler but 25% must stay in the account, and the pension withdrawal benefit is paid only after <strong>36 months</strong>. "
          "People who <strong>migrate abroad for permanent settlement</strong> can still withdraw in full. Foreign nationals remain covered as international workers unless they hold a certificate of coverage."),
    sections=[
        ("/ What changed", "1952 scheme vs 2026 scheme.",
         table(["Point", "Before", "EPF Scheme 2026"], [
             ["Legal basis", "EPF Act, 1952 and EPF Scheme, 1952", "Code on Social Security, 2020 and EPF Scheme, 2026 (G.S.R. 525(E), 29 June 2026)"],
             ["Contribution base", "Basic wages, dearness allowance and retaining allowance", "&ldquo;Wages&rdquo; as defined in the Code; 12% each from employer and employee"],
             ["Mandatory wage ceiling", "INR 15,000 a month", "INR 25,000 a month from 17 September 2026; higher earners can join by option"],
             ["Member records", "Paper forms still common", "UAN, Aadhaar, PAN and a seeded bank account mandatory; e-nomination; a nomination made before marriage is invalid"],
             ["Employer returns", "Monthly ECR", "Electronic return within 15 days after month end; late fee INR 500 a day"],
             ["Full withdrawal after leaving a job", "After two months without employment", "After 12 months; immediately on retirement after 55, permanent incapacity or migration abroad for permanent settlement"],
             ["Partial withdrawal", "Many separate purposes and service conditions", "Specified purposes after 12 months of membership; 25% of contributions must remain"],
             ["Pension withdrawal benefit (short service)", "After two months", "After 36 months from the last contribution, or at superannuation"],
             ["Death cover (EDLI)", "Up to INR 7 lakh", "INR 2.5 lakh minimum and INR 7 lakh maximum with 12 months&rsquo; continuous employment"],
             ["Past defaults", "-", "VISHWAS 2026 (reduced damages for late payments) open until 28 December 2026; the enrolment campaign for left-out employees closed on 31 October 2026"]])
         + call_box("The new provident fund rules and our payroll", ["Whether your salary structure meets the new definition of wages",
                                                                   "Cost of the INR 25,000 ceiling and options for higher earners",
                                                                   "Foreign nationals on payroll: international worker rules and certificates of coverage",
                                                                   "Past late payments and the VISHWAS 2026 window that closes on 28 December 2026",
                                                                   "For individuals: withdrawing PF after moving abroad, and the tax on it"],
                    "your payroll summary or salary structure, headcount, any foreign nationals employed, or your PF and service details.")),
        ("/ What to do now", "Employers, foreign-owned subsidiaries and individuals.",
         ul("<strong>Employers:</strong> test each salary component against the Code&rsquo;s definition of wages; allowances that were kept out of PF may now count.",
            "<strong>Budget:</strong> employees earning up to INR 25,000 a month must now be covered; review cost-to-company and offer letters.",
            "<strong>Records:</strong> complete UAN, Aadhaar, PAN, bank seeding and e-nominations for every employee; file the monthly return within 15 days.",
            "<strong>Foreign-owned subsidiaries:</strong> align group payroll and benefits with the new scheme; see <a href=\"foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html\">payroll and benefits for an Indian subsidiary</a>.",
            "<strong>Foreign nationals:</strong> international workers contribute unless they hold a certificate of coverage; see <a href=\"india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage.html\">India&rsquo;s social security agreements</a>.",
            "<strong>NRIs and people moving abroad:</strong> full withdrawal remains possible on permanent settlement abroad; see <a href=\"nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html\">EPF withdrawal for NRIs</a> for forms and tax.",
            "<strong>Past late payments:</strong> settle damages at reduced rates under <a href=\"epfo-vishwas-2026-pf-damages-settlement-reduced-rates-last-date-28-december-2026.html\">VISHWAS 2026</a> by 28 December 2026.",
            "<strong>Gratuity and other codes:</strong> see the <a href=\"gratuity-calculator-new-labour-codes-2026.html\">gratuity calculator under the labour codes</a>.")
         + '<p>Related: <a href="employer-of-record-india-hire-from-abroad.html">employer of record in India</a> &middot; <a href="foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html">compliance calendar for foreign-owned subsidiaries</a> &middot; <a href="expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html">expat tax in India</a>.</p>'
         + sources("Employees' Provident Fund Scheme, 2026 (G.S.R. 525(E), 29 June 2026), Employees' Pension Scheme, 2026 and Employees' Deposit-Linked Insurance Scheme, 2026 under the Code on Social Security, 2020, as summarised by Nexdigm ('New EPF, EPS and EDLI Schemes 2026') and TaxGuru ('EPF Scheme, 2026: Ten Major Changes', 18 July 2026); Notification S.O. 5109(E) of 17 September 2026 on the wage ceiling. Check the notifications and EPFO circulars for effective dates of individual provisions.")),
    ],
    faqs=[("What is the EPF Scheme 2026?", "The Employees' Provident Fund Scheme, 2026 was notified on 29 June 2026 under the Code on Social Security, 2020 and replaces the EPF Scheme, 1952. New pension (EPS 2026) and insurance (EDLI 2026) schemes were notified with it. Existing members, balances and service continue."),
          ("What is the EPF wage ceiling in 2026?", "INR 25,000 a month from 17 September 2026, up from INR 15,000. Employees earning up to the ceiling must be covered; higher earners can join by option."),
          ("When can I withdraw my full PF after leaving a job?", "Under the 2026 scheme, 12 months after leaving employment (it was two months earlier). Full withdrawal is immediate on retirement after 55, permanent incapacity or migration abroad for permanent settlement."),
          ("Is PF now calculated on full salary?", "Contributions are 12% of 'wages' as defined in the Code on Social Security, which is wider than basic pay, so some allowances may now count. Mandatory contributions apply up to the wage ceiling."),
          ("Do foreign employees in India still pay PF?", "Yes. International workers remain covered under the 2026 scheme unless they hold a certificate of coverage under a social security agreement."),
          ("Can BQP review our payroll for the new scheme?", "Yes. " + C)],
    related=[("foreign-company-india-subsidiary-employee-benefits-payroll-epf-esic-gratuity-2026.html", "Payroll and benefits for an Indian subsidiary"),
             ("nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html", "EPF withdrawal for NRIs"),
             ("india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage.html", "India's social security agreements")],
    cta_h="Payroll in India under the new provident fund scheme?", cta_b=C,
    keywords="EPF Scheme 2026, new EPF rules 2026, EPF wage ceiling 25000, PF withdrawal 12 months rule, EPS 2026 36 months, wages definition Code on Social Security PF, international worker PF 2026, EPF scheme 1952 replaced",
    desc="EPF Scheme 2026 (notified 29 June 2026) replaces the 1952 scheme: PF on 'wages' under the Code, INR 25,000 ceiling from 17 Sept 2026, mandatory Aadhaar/PAN and e-returns, full withdrawal 12 months after leaving a job, pension withdrawal after 36 months. Employer and NRI steps.",
    howto={"name": "How an employer prepares for the EPF Scheme 2026", "description": "Payroll and compliance steps.", "steps": [
        {"name": "Review the wage definition", "text": "Test salary components against 'wages' under the Code on Social Security."},
        {"name": "Apply the INR 25,000 ceiling", "text": "Cover employees up to the ceiling; decide the policy for higher earners."},
        {"name": "Clean member records", "text": "UAN, Aadhaar, PAN, bank seeding and e-nominations."},
        {"name": "File returns on time", "text": "Monthly electronic return within 15 days after month end."},
        {"name": "Check foreign nationals and past gaps", "text": "Certificates of coverage; VISHWAS 2026 for past late payments, open until 28 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ER complete")
