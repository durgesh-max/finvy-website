# -*- coding: utf-8 -*-
"""Batch JT (27 Nov 2026): Professional tax and Shops and Establishments registration in Gujarat / Ahmedabad.
Demand: sweep ac137 (27 Nov 2026): 'professional tax registration' (7 markets) with 'gujarat', 'ahmedabad', 'online gujarat',
'certificate gujarat', 'vadodara', 'surat', 'rajkot' variants, and 'shop and establishment registration' with 'gujarat',
'ahmedabad', 'surat', 'gandhinagar', 'documents required', 'certificate download'; no page covered either (the firm is
Ahmedabad-based).
Facts (verified 27 Nov 2026): Gujarat State Tax on Professions, Trades, Callings and Employments Act, 1976 - employers deduct
professional tax from salaries above the exempt limit and deposit it; employers take a registration certificate as
deductor and an enrolment certificate for their own tax (naming varies across sources - described generically); each place
of business may need its own registration; in Ahmedabad, professional tax is administered and paid through the Ahmedabad
Municipal Corporation (AMC FAQ, online quick pay). Gujarat Shops and Establishments (Regulation of Employment and Conditions
of Service) Act, 2019 - originally registration for establishments with ten or more workers and intimation for smaller ones
(section 7, within 60 days of commencement); the Amendment Act, 2026 (retrospective from 16 December 2025) moved
establishments with fewer than 20 workers to online intimation instead of registration. No slab rates, fees or penalty
amounts stated. No office claims beyond the firm's existing Ahmedabad base."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "professional-tax-and-shop-establishment-registration-gujarat-ahmedabad-2026"

C = contact("your business name and constitution (proprietorship, partnership, LLP or company), PAN, the address of each place of business in Gujarat, the date you started, the number of employees and their monthly salaries, and any registration or notice you already have")
PAGES = [dict(
    slug=SLUG,
    title="Professional Tax and Shop and Establishment Registration in Gujarat and Ahmedabad (2026): Who Must Register, Employer Deduction, AMC, the 20-Worker Intimation Rule and Documents",
    em="register once, deduct every month.",
    kicker="/ Businesses, startups and foreign-owned subsidiaries in Gujarat &middot; State and municipal registrations &middot; Updated 2026-11-27",
    lead=("<strong>Two local registrations catch most new businesses in Gujarat: professional tax, which employers must deduct from salaries and deposit, and the Shops and Establishments law, which now asks smaller establishments for an online intimation and larger ones for registration.</strong> "
          "In Ahmedabad, professional tax is administered through the Ahmedabad Municipal Corporation. "
          "Both apply to Indian subsidiaries of foreign companies and to startups as much as to local shops, and both are easy to miss until a notice arrives."),
    sections=[
        ("/ The two registrations", "What each covers.",
         table(["Law", "Who it applies to", "What you do"], [
             ["Gujarat State Tax on Professions, Trades, Callings and Employments Act, 1976", "Employers paying salaries above the exempt limit, and businesses and professionals liable for their own professional tax", "Register as an employer (deductor) and enrol for your own tax; deduct from salaries and deposit on time; each place of business may need its own registration"],
             ["Gujarat Shops and Establishments (Regulation of Employment and Conditions of Service) Act, 2019", "Shops and commercial establishments in Gujarat", "Smaller establishments give an online intimation of commencement; establishments above the worker threshold register"]])),
        ("/ What changed in 2026", "The Shops and Establishments threshold.",
         ul("<strong>Before:</strong> the 2019 Act required registration for establishments with ten or more workers, and an intimation within 60 days of commencement for smaller ones.",
            "<strong>Now:</strong> the Gujarat Shops and Establishments (Amendment) Act, 2026, effective retrospectively from 16 December 2025, moved establishments with fewer than 20 workers to the online intimation route instead of registration.",
            "<strong>Check older guides:</strong> many compliance guides written before December 2025 still show the ten-worker threshold.")),
        ("/ Professional tax in practice", "For employers in Ahmedabad and Gujarat.",
         ul("<strong>Register before the first payroll</strong> that crosses the exempt salary limit, then deduct from each eligible employee's salary every month.",
            "<strong>Ahmedabad:</strong> registration, payment and queries go through the Ahmedabad Municipal Corporation, which also offers online payment.",
            "<strong>Other cities:</strong> the local authority or the state commercial tax department handles professional tax, depending on where the business is.",
            "<strong>Show it on payslips</strong> and in Form 130 (old Form 16); professional tax paid is deductible from salary income under the old tax regime.")
         + call_box("Gujarat registrations", ["Professional tax employer registration and enrolment",
                                              "Shops and Establishments intimation or registration",
                                              "GST, Udyam and payroll set-up for new businesses",
                                              "Registrations for foreign-owned subsidiaries in Gujarat",
                                              "Catch-up for missed deductions or notices"],
                    "Business details, addresses and headcount.")
         + sources("Gujarat State Tax on Professions, Trades, Callings and Employments Act, 1976 and Rules; Ahmedabad Municipal Corporation professional tax FAQ; Gujarat Shops and Establishments (Regulation of Employment and Conditions of Service) Act, 2019, Rules, 2020 and Amendment Act, 2026. Checked 27 November 2026.")),
    ],
    faqs=[("Who must register for professional tax in Gujarat?", "Employers who pay salaries above the exempt limit must register as deductors, deduct professional tax from those salaries and deposit it; businesses and professionals also enrol for their own professional tax. Each place of business in Gujarat may need its own registration."),
          ("Where do I register and pay professional tax in Ahmedabad?", "In Ahmedabad, professional tax is administered by the Ahmedabad Municipal Corporation, which handles registration and offers online payment; outside Ahmedabad the local authority or the state commercial tax department is responsible."),
          ("Is Shop and Establishment registration mandatory in Gujarat?", "Under the Gujarat Shops and Establishments Act, 2019 as amended in 2026, establishments with fewer than 20 workers give an online intimation of commencement instead of registering, and larger establishments register. Before the amendment the registration threshold was ten workers, so older guides may be out of date."),
          ("When did the Gujarat shop act threshold change to 20 workers?", "The Gujarat Shops and Establishments (Amendment) Act, 2026 applies retrospectively from 16 December 2025 and moved establishments with fewer than 20 workers to the intimation route."),
          ("Does a foreign company's Indian subsidiary in Ahmedabad need these registrations?", "Yes. Professional tax applies to its payroll in Gujarat and the Shops and Establishments law applies to its office, in the same way as for any Indian employer, alongside GST and other registrations."),
          ("What should I send to get professional tax and shop act registration done in Gujarat?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your business name and constitution, PAN, the address of each place of business in Gujarat, the start date, the number of employees and their monthly salaries, and any registration or notice you already have. We check which registrations and intimations apply and file them. You keep your own portal logins."),
          ("Can BQP handle Gujarat registrations for my business?", "Yes. CA Durgesh Chavda is based in Ahmedabad and works with startups, local businesses and foreign-owned subsidiaries in Gujarat. " + C)],
    related=[("ca-firm-ahmedabad.html", "CA firm in Ahmedabad"),
             ("best-ca-gujarat-state-registration-ahmedabad-rajkot-dholera.html", "Gujarat state registrations"),
             ("sole-proprietorship-registration-india-documents-gst-udyam-shop-licence-online-2026.html", "Sole proprietorship registration"),
             ("udyam-msme-registration-benefits-india-2026.html", "Udyam (MSME) registration"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary and Form 130")],
    cta_h="Starting or running a business in Gujarat?", cta_b=C,
    keywords="professional tax registration gujarat, professional tax registration ahmedabad, professional tax gujarat online, shop and establishment registration gujarat, shop and establishment registration ahmedabad, gujarat shops and establishments act 2019 amendment 2026, amc professional tax",
    desc="Professional tax and Shops and Establishments registration in Gujarat and Ahmedabad: who must register, employer deduction, the Ahmedabad Municipal Corporation, the 2026 change to online intimation for establishments with fewer than 20 workers, and what to send.",
    howto={"name": "How to set up professional tax and shop act compliance in Gujarat", "description": "From first office to first payroll.", "steps": [
        {"name": "List your places of business", "text": "Note each address in Gujarat, the start date and the headcount."},
        {"name": "Shops and Establishments", "text": "File the online intimation (fewer than 20 workers) or register (larger establishments)."},
        {"name": "Professional tax", "text": "Register as an employer and enrol for your own tax with the right authority (AMC in Ahmedabad)."},
        {"name": "Deduct and deposit", "text": "Deduct from eligible salaries each month and deposit on time."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JT complete")
