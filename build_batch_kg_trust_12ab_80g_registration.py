# -*- coding: utf-8 -*-
"""Batch KG (27 Nov 2026): Trust / NGO registration under section 12AB (now section 332 of the Income-tax Act, 2025) and
80G approval (now section 354) - provisional and regular registration, renewal, forms, compliance and what happens if a
deadline is missed.
Demand: sweep ac162 (27 Nov 2026), all 7 markets: "trust registration under 12ab", "trust registered under 12ab",
"trust registration 12ab", "trust registration us 12ab", "what is trust registration"; the site covered 12A / 80G only inside
the section 8 company page.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - registration, renewal and the annual audit of a trust are
handled by a CA.
Facts (verified 27 Nov 2026 by web search, including the Income Tax Department's Form 105 FAQs): from 1 April 2026 sections
332 and 354 of the Income-tax Act, 2025 replace sections 12AB and 80G; existing valid registrations / approvals continue
without fresh registration; new entities get provisional registration (three years) and then apply for regular registration
(generally five years); regular registration / renewal applications are due at least six months before expiry (or within six
months of starting activities for a provisionally registered entity, whichever is earlier); forms renumbered under the
Income-tax Rules, 2026 (Form 104 for provisional, Form 105 for regular registration / renewal, replacing Forms 10A / 10AB -
some sources still use the old numbers); donation statements (old Form 10BD) due by 31 May with a late fee for delay; donors'
cash donations above Rs 2,000 are not deductible; audit report before the return; missing registration can expose the trust
to tax on accreted income. No fees, no office claims, no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "trust-registration-12ab-section-332-80g-ngo-provisional-regular-renewal-form-104-105-2026"

C = contact("the trust deed, society registration or section 8 licence, the PAN, any existing 12A / 12AB / 80G orders with their expiry dates, the last three years' accounts and audit reports, and a short note on the activities")
PAGES = [dict(
    slug=SLUG,
    title="Trust Registration Under 12AB (Now Section 332) and 80G Approval (2026): Provisional and Regular Registration, Renewal, Form 104 / 105 and Compliance",
    em="no registration, no exemption.",
    kicker="/ Charitable and religious trusts, societies and section 8 companies &middot; Registration, renewal and 80G &middot; Updated 2026-11-27",
    lead=("<strong>A trust, society or section 8 company is taxed like any other entity unless it is registered under section 12AB (from 1 April 2026, section 332 of the Income-tax Act, 2025); donors get a deduction only if it also holds 80G approval (now section 354).</strong> "
          "A new entity first gets provisional registration for three years and must then apply for regular registration in time; registered entities renew every five years. "
          "Existing valid registrations continue under the new Act, but missing a renewal date can cost the exemption."),
    sections=[
        ("/ How registration works", "Provisional, regular, renewal.",
         table(["Stage", "What happens"], [
             ["Provisional registration", "For a new entity, granted for three years; apply before or soon after starting activities"],
             ["Regular registration", "Apply at least six months before provisional registration expires, or within six months of starting activities if earlier; generally granted for five years"],
             ["Renewal", "Apply at least six months before the current registration expires"],
             ["80G approval", "Follows the same provisional / regular / renewal path; lets donors claim a deduction"],
             ["Forms (2025 Act)", "Form 104 for provisional and Form 105 for regular registration or renewal, replacing Forms 10A and 10AB"]])
         + ul("<strong>Existing registrations</strong> under 12A / 12AB / 80G remain valid under the 2025 Act until their expiry - no fresh registration just because the Act changed.",
              "<strong>Documents:</strong> trust deed, society registration or section 8 licence, PAN, activity details, accounts and the existing orders.",
              "<strong>Objects matter:</strong> the officer checks that activities are genuine and match the objects, and may ask questions before granting regular registration.")),
        ("/ After registration", "The yearly compliance that keeps it.",
         ul("<strong>Books and audit:</strong> accounts audited and the audit report filed before the return when income before exemption exceeds the basic exemption limit.",
            "<strong>Return:</strong> the trust files its own return every year, showing income applied to its objects and any accumulation.",
            "<strong>Donation statements:</strong> an 80G-approved entity files the annual statement of donations (old Form 10BD) by 31 May and issues donor certificates - late filing attracts a fee and donors lose their deduction.",
            "<strong>Cash donations:</strong> donors cannot claim a deduction for cash donations above Rs 2,000.",
            "<strong>Missed renewal or cancellation:</strong> the exemption is lost and the trust can be taxed on its accreted income, so diary the expiry dates.")
         + call_box("Trust and NGO registration", ["12AB / section 332 provisional and regular registration",
                                                   "80G / section 354 approval and renewal",
                                                   "Replies to officer queries",
                                                   "Audit, return and donation statements",
                                                   "Catch-up for missed renewals"],
                    "Trust deed, PAN, existing orders and accounts.")
         + sources("Income-tax Act, 1961 (sections 12A, 12AB, 80G, 115TD) and the Income-tax Act, 2025 (sections 332 and 354); Income-tax Rules, 2026 (Forms 104 and 105) and the Income Tax Department's FAQs; CBDT condonation for delayed Form 10AB renewals (2026); site section 8 company and audit applicability guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is trust registration under 12AB?", "It is the income tax registration that lets a charitable or religious trust, society or section 8 company claim exemption on income applied to its objects. From 1 April 2026 it sits in section 332 of the Income-tax Act, 2025, but registrations granted under 12A / 12AB stay valid until they expire. Without it, the entity is taxed like any other."),
          ("How does a new trust get 12AB registration?", "It first applies for provisional registration, which is granted for three years. It must then apply for regular registration at least six months before the provisional registration expires, or within six months of starting its activities if that is earlier. Under the 2025 Act the forms are Form 104 (provisional) and Form 105 (regular), replacing Forms 10A and 10AB."),
          ("How long is 12AB registration valid, and when must it be renewed?", "Regular registration is generally granted for five years. The renewal application is due at least six months before it expires. Missing the date can cost the exemption, so diary the expiry date shown in the order."),
          ("Is 80G approval the same as 12AB registration?", "No. 12AB (now section 332) gives the trust its own exemption; 80G (now section 354) lets donors deduct their donations. Both follow a provisional / regular / renewal path and are usually applied for together. An 80G-approved trust must file the annual statement of donations by 31 May and issue donor certificates."),
          ("Does a trust registered under 12AB need fresh registration under the new Income-tax Act?", "No. A valid registration or approval under 12AB or 80G continues under the Income-tax Act, 2025 until its expiry; renewal then follows the new sections and forms."),
        ("What is the difference between audit report Form 10B and Form 10BB for a trust?", "Both are the tax audit reports a registered trust, society or section 8 company must file, signed by a chartered accountant, when its total income before claiming the exemption exceeds the basic exemption limit. Since assessment year 2023-24, Form 10B (old numbering) applies where that total income exceeds INR 5 crore, where the trust received any foreign contribution, or where it applied any income outside India; every other trust files the shorter Form 10BB, which is also used by institutions approved under section 10(23C). Both forms ask for detailed disclosures - application of income, accumulation, corpus donations, anonymous donations, payments to related persons and investments - so the books must be ready well before the deadline, which is one month before the return due date (normally 30 September for a trust whose ITR-7 is due by 31 October). A missing or late audit report can cost the trust its exemption for that year. WhatsApp +91 78018 87130 with the trust deed, registration orders, the year's accounts and any foreign contribution details, or book a call."),
        ("How does an NGO get FCRA registration to receive foreign donations?", "Any trust, society or section 8 company must have FCRA registration or prior permission from the Ministry of Home Affairs before it accepts foreign contribution - including donations from NRIs who are foreign citizens and from foreign companies or foundations. Full registration is generally for organisations that have existed for at least three years and have spent a minimum amount on their objects over that period, shown in audited accounts filed with the application in Form FC-3; a newer organisation applies for prior permission for a specific donor and amount instead. Foreign contributions must first be received in the designated FCRA account at State Bank of India, New Delhi Main Branch, and can then be moved to separate utilisation accounts; no local money can be mixed in. Registration is granted for a fixed period and must be renewed in time, an annual return in Form FC-4 is filed with the accounts, and the 2020 amendment tightened the rules on passing foreign funds to other organisations and on administrative spending. WhatsApp +91 78018 87130 with the registration documents, three years' audited accounts and the planned foreign donors, or book a call."),
          ("What should I send to register or renew a trust?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the trust deed, society registration or section 8 licence, PAN, any existing 12A / 12AB / 80G orders and their expiry dates, the last three years' accounts and a short note on the activities. We tell you which application is due and by when, and prepare it.")],
    related=[("section-8-company-registration-india-non-profit-licence-12a-80g-csr-1-compliance-2026.html", "Section 8 company, 12A and 80G"),
             ("audit-applicability-india-company-llp-partnership-proprietorship-trust-statutory-tax-audit-limits-2026.html", "Audit applicability (incl. trusts)")],
    cta_h="Registering or renewing a trust?", cta_b=C,
    keywords="trust registration under 12ab, 12ab registration, trust registration 12ab, 12a registration, 80g registration, section 332 income tax act 2025, form 10a 10ab, form 104 105, ngo registration income tax, trust renewal 12ab",
    desc="Trust registration under 12AB (now section 332) and 80G approval (now section 354): provisional registration for three years, regular registration and renewal six months before expiry, Forms 104 / 105 (old 10A / 10AB), donation statements by 31 May, audit and what a missed renewal costs.",
    howto={"name": "How to get and keep 12AB registration", "description": "From a new trust to renewal.", "steps": [
        {"name": "Apply for provisional registration", "text": "Form 104 (old 10A) for a new trust, society or section 8 company."},
        {"name": "Apply for regular registration", "text": "Form 105 (old 10AB) at least six months before provisional expiry or within six months of starting activities."},
        {"name": "Keep compliance current", "text": "Audit, annual return and donation statements by 31 May if 80G-approved."},
        {"name": "Renew in time", "text": "Apply at least six months before the five-year registration expires."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KG complete")
