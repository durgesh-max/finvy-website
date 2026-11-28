# -*- coding: utf-8 -*-
"""Batch LP (28 Nov 2026): Adding or removing a partner in an LLP - Form 4 within 30 days, supplementary LLP agreement in Form 3
within 30 days, consent, designated partner rules (minimum two, one resident for 120 days), cessation notice, capital changes, and
the tax side on reconstitution (sections 9B and 45(4)).
Demand: 'add partner in llp', 'remove partner from llp', 'llp form 4', 'llp form 3 supplementary agreement', 'change designated
partner llp' - LLP Forms 3 / 4 only mentioned on the registration and annual filing pages; no dedicated page. Founders and foreign
partners need this done correctly. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (LLP Act, 2008 sections 7, 23, 24 and 25 as amended by the LLP (Amendment) Act, 2021; LLP Rules, 2009): at least two partners
and at least two designated partners who are individuals, one of whom is resident in India (in India for at least 120 days in the
financial year - matched to the site LLP registration page); a change in partners or designated partners is notified to the
Registrar in Form 4 within 30 days, with the incoming partner's consent; changes in the LLP agreement (new partner, profit share,
contribution) are filed in Form 3 within 30 days; a partner may cease by giving at least 30 days notice to the other partners unless
the agreement provides otherwise; a designated partner needs a DPIN / DIN; money or capital assets received by a partner on
reconstitution can be taxed in the LLP's hands under sections 9B and 45(4) of the Income-tax Act (from AY 2021-22). No fees, no
late fee amounts, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "add-remove-partner-llp-form-4-form-3-supplementary-agreement-30-days-designated-partner-resident-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current LLP agreement, the incoming or outgoing "
     "partner&rsquo;s details (and whether they will be a designated partner), the date of change, any change in contribution or "
     "profit share, and whether anyone is a foreign national or NRI. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Add or Remove a Partner in an LLP (2026): Form 4 Within 30 Days, Supplementary LLP Agreement in Form 3, Designated Partner Rules and Tax on Exit",
    em="two filings, thirty days.",
    kicker="/ LLP partners, founders and foreign partners &middot; LLP Act sections 23 to 25 &middot; Updated 2026-11-28",
    lead=("<strong>When a partner joins or leaves an LLP, two filings follow: Form 4 to report the change in partners or designated partners, and Form 3 to file the supplementary LLP agreement - each within 30 days. "
          "The LLP must always keep at least two partners and two designated partners, one of them resident in India, and money or assets paid to an exiting partner can be taxed in the LLP&rsquo;s hands.</strong>"),
    sections=[
        ("/ The rules and filings", "LLP Act 2008.",
         table(["Point", "Rule"], [
             ["Minimum partners", "Two partners, and two designated partners who are individuals"],
             ["Resident designated partner", "At least one, in India for at least 120 days in the financial year"],
             ["Form 4", "Notice of a partner or designated partner joining, leaving or changing details - within 30 days, with consent"],
             ["Form 3", "Supplementary LLP agreement for the change (partners, profit share, contribution) - within 30 days"],
             ["Designated partner ID", "DPIN / DIN needed before appointment"],
             ["Leaving partner", "At least 30 days notice to the other partners, unless the agreement says otherwise"]])
         + ul("<strong>Sequence:</strong> sign the supplementary agreement, file Form 4 for the change, then file Form 3 with the agreement.",
              "<strong>Stamp duty:</strong> the supplementary agreement attracts stamp duty that varies by state.")),
        ("/ Foreign partners, exits and tax", "Where it gets complicated.",
         ul("<strong>Foreign or NRI partner:</strong> contribution by a non-resident follows FEMA rules for LLPs (the sector must permit foreign investment under the automatic route) and the related reporting; a foreign designated partner still needs a resident designated partner alongside.",
            "<strong>Exit payouts:</strong> money or capital assets paid to a partner on reconstitution can be taxed in the LLP&rsquo;s hands under sections 9B and 45(4) of the Income-tax Act - value the payout before agreeing it.",
            "<strong>Capital accounts:</strong> settle the outgoing partner&rsquo;s capital and current account in the books, and update bank signatories and GST records.",
            "<strong>Falling below two partners:</strong> if only one partner remains for more than six months, that partner can become personally liable - add a partner promptly.",
            "<strong>Late filings:</strong> Forms 3 and 4 attract additional fees per day of delay and keep the Registrar records out of date.")
         + call_box("LLP partner changes", ["Supplementary LLP agreement",
                                            "Form 4 and Form 3 within 30 days",
                                            "Designated partner and DPIN",
                                            "Foreign partner FEMA steps",
                                            "Tax on exit payouts (9B / 45(4))"],
                    "LLP agreement, partner details, date of change, contribution and profit share, residency.")
         + sources("Limited Liability Partnership Act, 2008 (sections 6, 7, 23, 24 and 25, as amended by the LLP (Amendment) Act, 2021); LLP Rules, 2009 (Forms 3, 4 and 9); Income-tax Act, 1961 (sections 9B and 45(4)) and the corresponding provisions of the Income-tax Act, 2025; site LLP registration, LLP annual filing and LLP vs partnership pages.")),
    ],
    faqs=[("How do I add a new partner to an LLP?", "Sign a supplementary LLP agreement admitting the partner, obtain the partner's consent (and DPIN if they will be a designated partner), file Form 4 with the Registrar within 30 days of the change, and file the supplementary agreement in Form 3 within 30 days."),
          ("How do I remove or replace a partner in an LLP?", "The partner gives notice as the LLP agreement requires (at least 30 days if it is silent), the remaining partners settle the capital account, and the LLP files Form 4 for the cessation and Form 3 for the changed agreement, each within 30 days."),
          ("What is the difference between LLP Form 3 and Form 4?", "Form 3 files the LLP agreement or changes to it. Form 4 notifies the appointment, cessation or change in details of a partner or designated partner."),
          ("Does an LLP need a resident designated partner?", "Yes. At least one of the two or more designated partners must be resident in India, meaning in India for at least 120 days in the financial year."),
          ("Is there tax when a partner leaves an LLP?", "Money or capital assets paid to a partner on reconstitution can be taxed in the LLP's hands under sections 9B and 45(4) of the Income-tax Act, so the payout should be structured and valued with advice."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the LLP agreement, partner details, date of change, any change in contribution or profit share, and residency of the partners. Or book a call directly.")],
    related=[("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration in India"),
             ("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing (Form 11 and Form 8)"),
             ("llp-vs-partnership-firm-india-2026-liability-tax-compliance-registration-fdi-conversion.html", "LLP vs partnership firm"),
             ("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "Convert LLP to private limited company")],
    cta_h="Partner joining or leaving your LLP?", cta_b=C,
    keywords="add partner in llp, remove partner from llp, llp form 4, llp form 3 supplementary agreement, change designated partner llp, llp partner exit tax 9b 45(4), resident designated partner 120 days",
    desc="Add or remove a partner in an LLP: Form 4 within 30 days with consent, supplementary LLP agreement in Form 3 within 30 days, minimum two partners and two designated partners (one resident 120 days), DPIN, 30-day cessation notice, foreign partners, and tax on exit payouts under 9B / 45(4).",
    howto={"name": "How to change partners in an LLP", "description": "Agreement, then two filings.", "steps": [
        {"name": "Sign the supplementary agreement", "text": "Admission or exit, profit share and contribution."},
        {"name": "Get consents and DPIN", "text": "Incoming partner's consent; DPIN for a designated partner."},
        {"name": "File Form 4", "text": "Within 30 days of the change."},
        {"name": "File Form 3", "text": "Supplementary agreement within 30 days; check tax on any exit payout."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LP complete")
