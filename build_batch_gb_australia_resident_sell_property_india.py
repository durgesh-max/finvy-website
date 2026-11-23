# -*- coding: utf-8 -*-
"""Batch GB (24 Nov 2026): Australian citizen or Australian resident selling property in India - who can buy, Indian TDS and
tax, repatriation, and Australian CGT (worldwide gains for residents, 50% discount after 12 months, cost base at market value
on becoming resident, temporary residents generally outside CGT on foreign assets, foreign income tax offset). Call-first page.
Demand: autocomplete check 24 Nov 2026: "australian citizen selling property in india".
Facts (checked 24 Nov 2026): Indian side as on the US/UK/Canada pages. ATO: a person who becomes an Australian resident
(other than a temporary resident) is treated as acquiring CGT assets at market value on that day; 50% CGT discount for
individuals on assets held at least 12 months while resident (apportioned for foreign-residency periods after 8 May 2012);
temporary residents are generally taxed only on taxable Australian property; foreign tax paid is credited through the
foreign income tax offset under the India-Australia treaty."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "australian-citizen-resident-selling-property-in-india-tds-tax-repatriation-australia-cgt-2026"

C = contact("the property's city and type, when and how you acquired it, the expected sale price, whether you are an Australian citizen, permanent resident or on a temporary visa, when you became an Australian resident, and your timeline")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Australian Citizen or Resident Selling Property in India (2026): Who Can Buy, TDS, Repatriation and Australian Capital Gains Tax",
    em="India taxes first; the ATO gives an offset.",
    kicker="/ NRIs &middot; Australia &middot; Property sale &middot; Updated 2026-11-24",
    lead=("<strong>An Australian citizen of Indian origin, or an Indian living in Australia, can sell a house, flat or commercial property in India to a resident Indian, an NRI or an OCI holder; agricultural land only to a resident Indian citizen.</strong> "
          "India taxes the gain first: the buyer deducts TDS, <strong>12.5% plus surcharge and cess</strong> on long-term gains, unless you get a <strong>lower deduction certificate (Form 128)</strong>, and up to <strong>USD 1 million a year</strong> can be sent to Australia from your NRO account. "
          "If you are an Australian tax resident, the ATO taxes the gain in dollars: <strong>half the gain is taxable</strong> if you held the property for at least 12 months, and if you bought it before moving to Australia your cost is its <strong>market value on the day you became resident</strong>. "
          "The Indian tax comes off through the <strong>foreign income tax offset</strong>. People on <strong>temporary visas</strong> are generally not taxed in Australia on gains on Indian property."),
    sections=[
        ("/ Quick answers", "What Australia-based sellers ask.",
         ul("<strong>Can an Australian citizen sell property in India?</strong> Yes. As a person of Indian origin (with or without OCI) you can sell residential or commercial property to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India.",
            "<strong>How much TDS will the buyer deduct?</strong> 12.5% plus surcharge and cess on long-term gains (held over 24 months); 30% plus surcharge and cess on short-term gains. A Form 128 certificate brings it down to the real tax.",
            "<strong>Do I pay tax in Australia?</strong> If you are an Australian resident for tax (and not a temporary resident), yes: the gain goes in your return, halved if you held the property for at least 12 months, and the Indian tax is offset.",
            "<strong>I bought the flat before moving to Australia. What is my cost?</strong> For Australian tax, generally its market value on the day you became an Australian resident, so only the growth since then is taxed. Get a valuation for that date.",
            "<strong>I am on a temporary visa. Am I taxed?</strong> Temporary residents are generally taxed in Australia only on taxable Australian property, so a gain on Indian property is usually outside Australian tax; India still taxes it.")),
        ("/ India vs Australia", "Two tax calculations on one sale.",
         table(["", "India", "Australia (resident)"], [
             ["Gain measured in", "Rupees: sale price minus cost (no indexation for non-residents)", "Australian dollars, at exchange rates on acquisition (or on becoming resident) and sale"],
             ["Cost", "Your purchase cost (previous owner's cost if inherited)", "Purchase cost, or market value on the day you became an Australian resident if bought earlier"],
             ["Rate", "Long-term 12.5% plus surcharge and cess; short-term at slab rates", "Net gain added to income at marginal rates; 50% discount if held at least 12 months while resident"],
             ["Relief", "Section 54 or 54F if you buy another house in India; 54EC bonds for land or building gains", "Foreign income tax offset for the Indian tax under the India-Australia treaty"],
             ["Temporary visa holders", "Same Indian tax", "Generally not taxed on gains on Indian property"]])
         + '<p>The discount is reduced for any period after 8 May 2012 when you were a foreign resident. See the ' + L("india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html", "India-Australia tax treaty") + '.</p>'),
        ("/ Steps", "Selling from Australia.",
         ul("<strong>1. Documents:</strong> title deed or inheritance papers, mutation, tax receipts, PAN (Form 95 for foreign citizens).",
            "<strong>2. Value the property</strong> at the date you became an Australian resident, if bought before then.",
            "<strong>3. Apply for Form 128</strong> before the sale; see " + L("nri-property-tds-ldc-calculator.html", "the TDS and LDC calculator") + ".",
            "<strong>4. Sign in person or by power of attorney</strong> (notarised and apostilled in Australia, adjudicated in India); the buyer deducts TDS.",
            "<strong>5. Receive proceeds in your NRO account</strong> and remit with Forms 145 and 146, up to USD 1 million a year.",
            "<strong>6. File the Indian return</strong> to recover excess TDS, then report the gain in your Australian return and claim the foreign income tax offset.")
         + call_box("selling property in India from Australia", ["Indian capital gain, TDS and Form 128",
                                                                  "Power of attorney from Australia",
                                                                  "Repatriation to Australia",
                                                                  "Australian CGT, cost base and offset, with your Australian adviser",
                                                                  "Temporary resident position"],
                    "the property details, how and when you acquired it, when you became an Australian resident and the expected sale price.")
         + sources("FEMA (Non-debt Instruments) Rules, 2019; Income-tax Act provisions on long-term capital gains for non-residents (12.5% without indexation from 23 July 2024) and TDS; Form 128; RBI rules on remittances of up to USD 1 million per financial year from NRO accounts; Australian Taxation Office guidance on how changing residency affects CGT (market value on becoming resident), the CGT discount for foreign residents (periods after 8 May 2012), temporary residents and the foreign income tax offset; India-Australia Double Taxation Avoidance Agreement. Checked 24 November 2026.")),
    ],
    faqs=[("Can an Australian citizen sell property in India?", "Yes. An Australian citizen of Indian origin, with or without an OCI card, can sell residential or commercial property in India to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India."),
          ("Do Australian residents pay tax on selling property in India?", "Yes. India taxes the gain first (12.5% plus surcharge and cess for long-term gains, through TDS). Australia then taxes the gain in Australian dollars, halved if held at least 12 months, with a foreign income tax offset for the Indian tax."),
          ("What is my cost base if I bought the property before moving to Australia?", "Generally the market value of the property on the day you became an Australian resident for tax, so only the increase after that date is taxed in Australia."),
          ("Are temporary visa holders in Australia taxed on Indian property gains?", "Generally no. Temporary residents are taxed in Australia only on taxable Australian property, so a gain on Indian property usually falls outside Australian tax. India still taxes it."),
          ("How much can I transfer from India to Australia after the sale?", "Up to USD 1 million per financial year from your NRO account, with Form 145 and a chartered accountant's certificate in Form 146."),
          ("Can BQP handle the sale from Australia?", "Yes. " + C)],
    related=[("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html", "India-Australia tax treaty"),
             ("uk-resident-british-citizen-selling-property-in-india-tds-tax-repatriation-uk-cgt-2026.html", "UK resident selling property in India"),
             ("us-citizen-selling-property-in-india-inherited-tds-tax-power-of-attorney-us-capital-gains-2026.html", "US citizen selling property in India"),
             ("nri-property-tds-ldc-calculator.html", "NRI property TDS and LDC calculator")],
    cta_h="Selling property in India from Australia?", cta_b=C,
    keywords="Australian citizen selling property in India, Australian resident selling property in India, sell property in India from Australia tax, Australia CGT foreign property India, cost base market value becoming resident, temporary resident foreign capital gains Australia, India Australia DTAA property",
    desc="Australian citizen or resident selling property in India (2026): who can buy, TDS 12.5% plus surcharge and cess, Form 128, USD 1 million repatriation, and Australian CGT: 50% discount after 12 months, cost at market value on becoming resident, foreign income tax offset; temporary visa holders generally exempt.",
    howto={"name": "How an Australian resident sells property in India", "description": "Indian and Australian steps.", "steps": [
        {"name": "Get documents and a valuation", "text": "Title, mutation, PAN; market value on the date you became resident if bought earlier."},
        {"name": "Estimate both taxes", "text": "Indian gain in rupees; Australian gain in dollars with the 50% discount."},
        {"name": "Get a lower deduction certificate", "text": "Form 128 before the sale."},
        {"name": "Complete the sale", "text": "In person or by power of attorney; buyer deducts TDS."},
        {"name": "Repatriate and report", "text": "Forms 145/146 from NRO; Indian return; Australian return with the foreign income tax offset."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GB complete")
