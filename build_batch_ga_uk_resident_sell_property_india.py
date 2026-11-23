# -*- coding: utf-8 -*-
"""Batch GA (24 Nov 2026): British citizen or UK resident selling property in India - who can buy, Indian TDS and tax,
repatriation, and UK capital gains tax (18%/24%, GBP 3,000 exemption, foreign tax credit relief, Self Assessment, FIG
regime for new arrivals). Call-first page.
Demand: autocomplete check 24 Nov 2026: "can a british citizen sell property in india", "uk resident selling property in
india", "uk citizen selling property in india".
Facts (checked 24 Nov 2026):
- FEMA and Indian tax as on the US/Canada pages (12.5% long-term plus surcharge and cess; Form 128; Form 141; USD 1 million
  NRO repatriation with Forms 145/146).
- UK: CGT rates 18% (basic rate band) and 24% (higher) for individuals, including residential property; annual exempt
  amount GBP 3,000 for 2026-27 (gov.uk; Taxfix; Brown Butler). UK residents are taxed on worldwide gains; overseas
  property gains are reported through Self Assessment (the 60-day UK property return is for UK residential property);
  foreign tax credit relief for Indian tax under the India-UK treaty. From 6 April 2025 the remittance basis was replaced
  by the 4-year foreign income and gains (FIG) regime for new arrivals after 10 years of non-residence; claiming FIG
  relief means losing the annual exempt amount for that year (Experts for Expats)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "uk-resident-british-citizen-selling-property-in-india-tds-tax-repatriation-uk-cgt-2026"

C = contact("the property's city and type, when and how you acquired it, the expected sale price, whether you are a British citizen or an Indian citizen living in the UK, when you moved to the UK, and your timeline")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="British Citizen or UK Resident Selling Property in India (2026): Who Can Buy, TDS, Repatriation and UK Capital Gains Tax",
    em="India taxes first; HMRC gives credit.",
    kicker="/ NRIs &middot; United Kingdom &middot; Property sale &middot; Updated 2026-11-24",
    lead=("<strong>A British citizen of Indian origin, or an Indian living in the UK, can sell a house, flat or commercial property in India to a resident Indian, an NRI or an OCI holder; agricultural land only to a resident Indian citizen.</strong> "
          "India taxes the gain first: the buyer deducts TDS, <strong>12.5% plus surcharge and cess</strong> on long-term gains, unless you get a <strong>lower deduction certificate (Form 128)</strong>, and up to <strong>USD 1 million a year</strong> can be sent to the UK from your NRO account. "
          "If you are UK resident, HMRC taxes the gain in pounds at <strong>18% or 24%</strong> after the <strong>GBP 3,000</strong> annual exemption, through Self Assessment, with <strong>foreign tax credit relief</strong> for the Indian tax. "
          "Newer arrivals (in the first four tax years after ten years abroad) may be able to claim the <strong>foreign income and gains regime</strong> instead."),
    sections=[
        ("/ Quick answers", "What UK-based sellers ask.",
         ul("<strong>Can a British citizen sell property in India?</strong> Yes. As a person of Indian origin (with or without OCI) you can sell residential or commercial property to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India.",
            "<strong>How much TDS will the buyer deduct?</strong> 12.5% plus surcharge and cess on long-term gains (held over 24 months); 30% plus surcharge and cess on short-term gains. A Form 128 certificate brings it down to the real tax.",
            "<strong>Do I pay UK tax as well?</strong> If you are UK resident, yes: capital gains tax at 18% or 24% on the gain in pounds above GBP 3,000, with credit for the Indian tax paid on the same gain.",
            "<strong>Do I need to file the 60-day UK property return?</strong> That return is for UK residential property. A gain on Indian property goes on your Self Assessment return for the tax year.",
            "<strong>Can I sell without flying to India?</strong> Yes, through a power of attorney signed in the UK, notarised and apostilled (or attested at the Indian High Commission), and adjudicated for stamp duty in India.")),
        ("/ India vs UK", "Two tax calculations on one sale.",
         table(["", "India", "United Kingdom (UK resident)"], [
             ["Gain measured in", "Rupees: sale price minus cost (no indexation for non-residents)", "Pounds, at exchange rates on purchase and sale"],
             ["Rate", "Long-term 12.5% plus surcharge and cess; short-term at slab rates", "18% within the basic rate band, 24% above it, after the GBP 3,000 annual exemption"],
             ["Relief", "Section 54 or 54F if you buy another house in India; 54EC bonds for land or building gains", "Foreign tax credit relief for the Indian tax under the India-UK treaty (limited to the UK tax on that gain)"],
             ["Filing", "TDS, Form 128 certificate, Indian return, Forms 145/146", "Self Assessment return for the tax year (6 April to 5 April)"],
             ["New arrivals", "Same", "Foreign income and gains regime may exempt the gain in the first four tax years after ten years of non-residence; claiming it loses the annual exemption that year"]])
         + '<p>Inherited property: for UK tax your cost is usually the market value at the date of death; for Indian tax it is the previous owner&rsquo;s cost. See ' + L("returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html", "moving between the UK and India") + ' for split-year points.</p>'),
        ("/ Steps", "Selling from the UK.",
         ul("<strong>1. Documents:</strong> title deed or inheritance papers, mutation, tax receipts, PAN (Form 95 for foreign citizens).",
            "<strong>2. Work out both gains</strong> and estimate Indian and UK tax.",
            "<strong>3. Apply for Form 128</strong> before the sale; see " + L("nri-property-tds-ldc-calculator.html", "the TDS and LDC calculator") + ".",
            "<strong>4. Sign in person or by power of attorney;</strong> the buyer deducts TDS.",
            "<strong>5. Receive proceeds in your NRO account</strong> and remit with Forms 145 and 146, up to USD 1 million a year.",
            "<strong>6. File the Indian return</strong> to recover excess TDS, then report the gain in your UK Self Assessment and claim foreign tax credit relief.")
         + call_box("selling property in India from the UK", ["Indian capital gain, TDS and Form 128",
                                                               "Power of attorney from the UK",
                                                               "Repatriation to the UK",
                                                               "UK capital gains tax and credit, with your UK adviser",
                                                               "Whether the FIG regime applies to you"],
                    "the property details, how you acquired it, the expected sale price and when you moved to the UK.")
         + sources("FEMA (Non-debt Instruments) Rules, 2019; Income-tax Act provisions on long-term capital gains for non-residents (12.5% without indexation from 23 July 2024) and TDS; Form 128; CBDT Notification 121/2026 (Form 141); RBI rules on remittances of up to USD 1 million per financial year from NRO accounts; HMRC, Capital Gains Tax rates and allowances (18% and 24%; GBP 3,000 annual exempt amount for 2026-27); HMRC foreign tax credit relief; Finance Act 2025 foreign income and gains regime from 6 April 2025; India-UK Double Taxation Avoidance Agreement. Checked 24 November 2026.")),
    ],
    faqs=[("Can a British citizen sell property in India?", "Yes. A British citizen of Indian origin, with or without an OCI card, can sell residential or commercial property in India to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India."),
          ("Do UK residents pay tax on selling property in India?", "Yes, in both countries. India taxes the gain first (12.5% plus surcharge and cess for long-term gains, through TDS). HMRC then charges capital gains tax at 18% or 24% on the gain in pounds above GBP 3,000, with foreign tax credit relief for the Indian tax."),
          ("Do I report the sale of Indian property in the 60-day UK return?", "No. The 60-day return is for UK residential property. A gain on Indian property is reported on your Self Assessment return for the tax year."),
          ("Can I avoid UK tax on an Indian property sale as a new arrival?", "Possibly. Under the foreign income and gains regime from April 2025, people in their first four tax years of UK residence after ten years of non-residence can claim relief on foreign gains, but they lose the annual exemption for that year. Check your dates with a UK adviser."),
          ("How much can I transfer from India to the UK after the sale?", "Up to USD 1 million per financial year from your NRO account, with Form 145 and a chartered accountant's certificate in Form 146."),
          ("Can BQP handle the sale from the UK?", "Yes. " + C)],
    related=[("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("us-citizen-selling-property-in-india-inherited-tds-tax-power-of-attorney-us-capital-gains-2026.html", "US citizen selling property in India"),
             ("canadian-citizen-selling-property-in-india-tds-tax-repatriation-canada-capital-gains-2026.html", "Canadian citizen selling property in India"),
             ("nri-property-tds-ldc-calculator.html", "NRI property TDS and LDC calculator"),
             ("returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html", "Moving between the UK and India")],
    cta_h="Selling property in India from the UK?", cta_b=C,
    keywords="British citizen selling property in India, UK resident selling property in India, can a British citizen sell property in India, UK capital gains tax on Indian property, India UK DTAA property sale, repatriate property sale proceeds UK, FIG regime foreign gains",
    desc="British citizen or UK resident selling property in India (2026): who can buy, TDS 12.5% plus surcharge and cess on long-term gains, Form 128, power of attorney from the UK, USD 1 million repatriation, and UK CGT at 18% or 24% after GBP 3,000 with foreign tax credit relief; FIG regime for new arrivals.",
    howto={"name": "How a UK resident sells property in India", "description": "Indian and UK steps.", "steps": [
        {"name": "Get documents in order", "text": "Title, mutation, tax receipts, PAN."},
        {"name": "Estimate both taxes", "text": "Indian gain in rupees; UK gain in pounds."},
        {"name": "Get a lower deduction certificate", "text": "Form 128 before the sale."},
        {"name": "Complete the sale", "text": "In person or by power of attorney; buyer deducts TDS."},
        {"name": "Repatriate and report", "text": "Forms 145/146 from NRO; Indian return; UK Self Assessment with foreign tax credit relief."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GA complete")
