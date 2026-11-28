# -*- coding: utf-8 -*-
"""Batch ME (28 Nov 2026): Capital gains tax on overseas property for an Indian resident - worldwide taxation for residents, the
24-month holding period, long-term rates (12.5%, or 20% with indexation for land or buildings acquired before 23 July 2024 for
resident individuals and HUFs), section 54 / 54F reinvestment only in India, foreign tax credit, Schedule FA / CG reporting, and
the RNOR and NRI position.
Demand: sweep ac251 (28 Nov 2026), all 7 markets: 'do you have to pay capital gains tax on overseas property' (coverage 0.50) - the
site covers selling Indian property from abroad but not a resident selling a foreign flat. Returning NRIs and Indian residents
with property abroad need computation and credit help. User steer 26 Nov / 19 Nov 2026: more call bookings.
Facts: a resident and ordinarily resident is taxed on worldwide income, so gains on selling foreign property are taxable in India;
RNORs and NRIs are generally not taxed in India on foreign capital gains; immovable property held for more than 24 months is a
long-term capital asset; long-term gains taxed at 12.5% without indexation, with resident individuals and HUFs able to choose 20%
with indexation for land or buildings acquired before 23 July 2024 (matched to the site property capital gains calculator page);
section 54 and 54F exemptions require the new residential house to be in India; tax paid abroad on the same gain can be claimed as
foreign tax credit (Form 67) under the DTAA or section 91; the property must have been reported in Schedule FA while held and the sale
in Schedule CG; foreign currency cost and sale price are converted at the rates the rules prescribe. No fees, no portal menu paths,
no FEMA repatriation specifics (depend on how the property was acquired). advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "capital-gains-tax-on-overseas-property-indian-resident-sell-foreign-house-flat-section-54-foreign-tax-credit-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the country of the property, purchase and sale dates "
     "and amounts, how it was acquired (bought while abroad, under LRS, inherited), tax paid abroad on the sale, your residential "
     "status in India for the year of sale, and whether it was reported in Schedule FA. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Capital Gains Tax on Overseas Property for Indian Residents (2026): Selling a Foreign House or Flat, Rates, Section 54, Foreign Tax Credit and Schedule FA",
    em="taxed in India too, with credit for tax paid abroad.",
    kicker="/ Indian residents and returning NRIs with property abroad &middot; Capital gains on foreign real estate &middot; Updated 2026-11-28",
    lead=("<strong>If you are resident and ordinarily resident in India, a gain on selling a house or flat abroad is taxable in India, even if the other country also taxes it. "
          "Held more than 24 months, it is a long-term gain - taxed at 12.5%, or at 20% with indexation for property bought before 23 July 2024 if you are an individual or HUF - with credit for tax paid abroad. "
          "The section 54 and 54F reinvestment exemptions work only if the new house is in India.</strong>"),
    sections=[
        ("/ How India taxes the sale", "Status first, then the rules.",
         table(["Point", "Position"], [
             ["Resident and ordinarily resident (ROR)", "Gain taxable in India (worldwide income)"],
             ["RNOR or NRI in the year of sale", "Generally not taxable in India"],
             ["Long-term", "Held more than 24 months"],
             ["Long-term rate", "12.5% without indexation; resident individuals and HUFs may choose 20% with indexation for land or buildings bought before 23 July 2024"],
             ["Short-term", "Added to income and taxed at slab rates"],
             ["Section 54 / 54F", "Only if the new residential house is in India"],
             ["Tax paid abroad", "Foreign tax credit under the DTAA or section 91, claimed with Form 67"]])
         + ul("<strong>Currency conversion:</strong> cost and sale price in foreign currency are converted at the rates the rules prescribe - the rupee movement can increase the Indian gain.",
              "<strong>Returning NRIs:</strong> selling while still RNOR can keep the gain outside Indian tax - timing matters.")),
        ("/ Reporting and planning", "Before and after the sale.",
         ul("<strong>Schedule FA:</strong> the property should have been reported as a foreign asset each year you held it as a resident; missing years can draw Black Money Act penalties.",
            "<strong>Schedule CG and FSI:</strong> report the gain in capital gains and foreign source income, with the foreign tax credit claim.",
            "<strong>Credit limits:</strong> the credit is limited to the Indian tax on that income; timing differences between the two countries&rsquo; tax years need care.",
            "<strong>Bringing money to India:</strong> through banking channels; FEMA treatment depends on how the property was acquired - check before the sale.",
            "<strong>Inherited property abroad:</strong> the previous owner&rsquo;s cost and holding period apply.")
         + call_box("selling property abroad", ["Residential status check for the year of sale",
                                                "Capital gains computation and rate choice",
                                                "Foreign tax credit and Form 67",
                                                "Schedule FA, CG and FSI reporting",
                                                "Section 54 / 54F planning in India"],
                    "Country, dates and amounts, how acquired, tax paid abroad, residential status, Schedule FA history.")
         + sources("Income-tax Act, 1961 (sections 5, 2(42A), 48, 49, 54, 54F, 90, 91 and 112) and the corresponding provisions of the Income-tax Act, 2025; Income-tax Rules on foreign tax credit (Form 67) and currency conversion; Black Money Act, 2015; site property capital gains calculator, section 54, Form 67 and Schedule FA pages.")),
    ],
    faqs=[("Do I have to pay capital gains tax in India on property sold abroad?", "Yes, if you are resident and ordinarily resident in India in the year of sale, because residents are taxed on worldwide income. If you are RNOR or non-resident that year, foreign capital gains are generally not taxed in India."),
          ("What is the tax rate on long-term capital gains from overseas property?", "12.5% without indexation for property held more than 24 months. Resident individuals and HUFs may instead choose 20% with indexation for land or buildings acquired before 23 July 2024. Short-term gains are taxed at slab rates."),
          ("Can I claim section 54 exemption if I buy a house abroad?", "No. Section 54 and section 54F require the new residential house to be in India. Reinvesting the gain in a house in India can qualify, subject to the usual conditions."),
          ("What if I already paid capital gains tax in the other country?", "You can claim foreign tax credit under the tax treaty or section 91, by filing Form 67, up to the Indian tax on that gain."),
          ("Do I need to report overseas property in my ITR?", "Yes. A resident and ordinarily resident must report foreign property in Schedule FA every year it is held, and the sale in Schedule CG and Schedule FSI in the year of sale."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the country, purchase and sale details, how it was acquired, tax paid abroad, your residential status and Schedule FA history. Or book a call directly.")],
    related=[("property-capital-gains-tax-calculator-india-indexation-12-5-vs-20-inherited-nri-2026.html", "Property capital gains tax calculator"),
             ("form-67-foreign-tax-credit-india-2026.html", "DTAA relief and foreign tax credit (Form 67)"),
             ("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "Section 54 exemption"),
             ("house-flat-property-abroad-not-in-schedule-fa-fast-ds-returning-nri.html", "Property abroad not shown in Schedule FA")],
    cta_h="Selling a house or flat abroad?", cta_b=C,
    keywords="capital gains tax on overseas property, do you have to pay capital gains tax on overseas property, sell foreign property indian resident tax, foreign property capital gains india, section 54 foreign house, foreign tax credit capital gains property",
    desc="Capital gains tax on overseas property for Indian residents: taxable for RORs (not usually for RNORs / NRIs), long-term after 24 months at 12.5% or 20% with indexation for pre-23 July 2024 land or buildings, section 54 / 54F only for a new house in India, foreign tax credit via Form 67, Schedule FA and CG.",
    howto={"name": "How to handle the sale of property abroad", "description": "Status, compute, credit, report.", "steps": [
        {"name": "Check your status", "text": "ROR, RNOR or NRI in the year of sale."},
        {"name": "Compute the gain", "text": "Holding period, currency conversion, rate choice."},
        {"name": "Claim credit", "text": "Foreign tax paid on the gain via Form 67."},
        {"name": "Report", "text": "Schedule FA history, Schedule CG and FSI; plan section 54 in India if relevant."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch ME complete")
