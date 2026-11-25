# -*- coding: utf-8 -*-
"""Batch FZ (24 Nov 2026): US citizen selling property in India (bought or inherited) - who can buy, Indian TDS and tax,
repatriation, power of attorney, and US tax (Schedule D, 0/15/20% plus 3.8% NIIT, stepped-up basis on inheritance,
foreign tax credit on Form 1116, Form 3520 for large inheritances, FBAR). Call-first page.
Demand: autocomplete check 24 Nov 2026: "can us citizen sell property in india", "us citizen selling inherited property in
india", "us citizen selling property in india tax", "... power of attorney", "can us citizen with oci sell property in
india". The site's US citizen property page covers buying and holding; no sale-focused page.
Facts (checked 24 Nov 2026):
- FEMA: a person of Indian origin / OCI can sell residential or commercial property to a resident Indian, NRI or OCI;
  agricultural land, plantation or farmhouse only to an Indian citizen resident in India; inherited property can be sold
  (site pages).
- Indian tax: long-term (over 24 months, counting the previous owner's holding for inherited property) 12.5% without
  indexation plus surcharge and cess; short-term at slab rates; buyer deducts TDS; Form 128 lower deduction certificate;
  Form 141 without TAN for resident buyers from 1 October 2026; NRO repatriation up to USD 1 million per financial year
  with Forms 145/146 (site pages).
- US: citizens taxed on worldwide income; long-term capital gain rates 0/15/20% plus 3.8% net investment income tax above
  thresholds; gain in US dollars; basis of inherited property is fair market value at date of death (IRC 1014);
  foreign tax credit (Form 1116) for Indian tax under the India-US treaty (Article 13 lets India tax gains on Indian
  immovable property); Form 3520 for gifts or bequests from a foreign person over USD 100,000; NRO account on FBAR if
  aggregate foreign accounts exceed USD 10,000 (site FBAR and gift pages)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "us-citizen-selling-property-in-india-inherited-tds-tax-power-of-attorney-us-capital-gains-2026"

C = contact("the property's city and type, whether you bought or inherited it (and the date of death if inherited), the expected sale price, whether you hold an OCI card, and your timeline")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="US Citizen or NRI in the US Selling Property in India (2026): Tax Implications in India and the US, Inherited Property, TDS, Power of Attorney and Repatriation",
    em="India taxes first; the US credits it.",
    kicker="/ NRIs &middot; USA &middot; Property sale &middot; Updated 2026-11-24",
    lead=("<strong>Yes, a US citizen can sell property in India, including inherited property: as a person of Indian origin (with or without an OCI card) you can sell a house, flat or commercial property to a resident Indian, an NRI or an OCI holder; agricultural land only to a resident Indian citizen.</strong> "
          "India taxes the gain first: the buyer deducts TDS, <strong>12.5% plus surcharge and cess</strong> on long-term gains, unless you get a <strong>lower deduction certificate (Form 128)</strong>. "
          "You can send up to <strong>USD 1 million a year</strong> to the US from your NRO account. "
          "The US taxes the gain in dollars at <strong>0%, 15% or 20%</strong> (plus 3.8% net investment income tax for higher incomes), with a <strong>foreign tax credit</strong> for the Indian tax; for <strong>inherited</strong> property, your US cost is the value on the date of death, which often makes the US gain small."),
    sections=[
        ("/ Quick answers", "What US citizens selling in India ask.",
         ul("<strong>Can a US citizen sell property in India?</strong> Yes, residential or commercial property, to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India.",
            "<strong>Can I sell property I inherited in India?</strong> Yes. For Indian tax, your cost and holding period include the previous owner&rsquo;s; for US tax, your cost is the fair market value at the date of death.",
            "<strong>Can I sell without travelling to India?</strong> Yes, through a power of attorney signed in the US, notarised and apostilled (or attested at an Indian consulate), then adjudicated for stamp duty in India within the time allowed.",
            "<strong>How much TDS?</strong> 12.5% plus surcharge and cess on long-term gains (held over 24 months); 30% plus surcharge and cess on short-term gains. Apply for Form 128 before the sale so TDS matches the real tax.",
            "<strong>What do I report in the US?</strong> The sale on Schedule D and Form 8949, the Indian tax on Form 1116 for credit, the NRO account on the FBAR and Form 8938 where thresholds are met, and Form 3520 if you inherited over USD 100,000 from a non-US person.")),
        ("/ India vs US", "Two tax calculations on one sale.",
         table(["", "India", "United States"], [
             ["Gain measured in", "Rupees: sale price minus cost (no indexation for non-residents)", "US dollars, at exchange rates on purchase (or date of death) and sale"],
             ["Cost of inherited property", "Previous owner&rsquo;s cost (or value on 1 April 2001 for older property)", "Fair market value at the date of death (stepped-up basis)"],
             ["Rate", "Long-term 12.5% plus surcharge and cess; short-term at slab rates", "Long-term 0%, 15% or 20%, plus 3.8% NIIT above income thresholds; short-term at ordinary rates"],
             ["Relief", "Section 54 or 54F if you buy another house in India; 54EC bonds for land or building gains", "Foreign tax credit on Form 1116 for the Indian tax, under the India-US treaty"],
             ["Paperwork", "TDS, Form 128 certificate, Indian return, Forms 145/146", "Form 1040 with Schedule D, Form 8949, Form 1116; FBAR, Form 8938; Form 3520 for large inheritances"]])
         + '<p>Because the US uses the stepped-up value for inherited property and measures in dollars, the Indian tax is often larger than the US tax on the same sale; unused foreign tax credit can be carried back one year and forward ten. See the ' + L("india-us-dtaa-withholding-rates.html", "India-US treaty rates") + '.</p>'),
        ("/ Steps", "Selling from the US without surprises.",
         ul("<strong>1. Documents:</strong> title deed or will, probate or succession certificate where needed, mutation in your name, tax receipts, PAN (Form 95 for foreign citizens).",
            "<strong>2. Work out both gains</strong> and the expected Indian and US tax.",
            "<strong>3. Apply for the lower deduction certificate</strong> (Form 128); see " + L("nri-property-tds-ldc-calculator.html", "the TDS and LDC calculator") + ".",
            "<strong>4. Sign in person or by power of attorney;</strong> the buyer deducts TDS (a resident buyer can deposit it under their own PAN in Form 141 from 1 October 2026).",
            "<strong>5. Receive the money in your NRO account</strong> and remit with Forms 145 and 146, up to USD 1 million a year.",
            "<strong>6. File the Indian return</strong> to claim back excess TDS, then report in the US and claim the foreign tax credit.")
         + call_box("selling property in India as a US citizen", ["Indian capital gain, TDS and Form 128",
                                                                   "Inherited property: title, succession, mutation",
                                                                   "Power of attorney from the US",
                                                                   "Repatriation to the US",
                                                                   "US reporting and foreign tax credit, with your US CPA"],
                    "the property details, how you acquired it and the expected sale price.")
         + sources("FEMA (Non-debt Instruments) Rules, 2019 on transfer of immovable property by NRIs and OCIs; Income-tax Act provisions on long-term capital gains (12.5% without indexation for non-residents from 23 July 2024), inherited property cost and holding period, and TDS on payments to non-residents; Form 128 lower deduction certificate; CBDT Notification 121/2026 (Form 141 without TAN from 1 October 2026); RBI rules on remittances of up to USD 1 million per financial year from NRO accounts; US Internal Revenue Code sections 1(h), 1014, 1411 and 901; IRS Forms 8949, 1116, 3520 and 8938 instructions; FinCEN FBAR rules; India-US Double Taxation Avoidance Agreement, Article 13. Checked 24 November 2026.")),
    ],
    faqs=[("Can a US citizen sell property in India?", "Yes. A US citizen of Indian origin, with or without an OCI card, can sell residential or commercial property in India to a resident Indian, an NRI or an OCI. Agricultural land, plantations and farmhouses can be sold only to an Indian citizen resident in India."),
          ("Can a US citizen sell inherited property in India?", "Yes. Indian tax uses the previous owner's cost and holding period; US tax uses the fair market value at the date of death as your cost, which often leaves little US gain. Title must first be in your name through mutation, and a succession certificate or probate may be needed."),
          ("How is the sale of Indian property taxed for a US citizen?", "India taxes the gain first (12.5% plus surcharge and cess for long-term gains). The US taxes the gain in dollars at 0%, 15% or 20%, plus 3.8% NIIT for higher incomes, and allows a foreign tax credit for the Indian tax under the India-US treaty."),
          ("Can a US citizen sell property in India with a power of attorney?", "Yes. Sign a power of attorney in the US, have it notarised and apostilled or attested at an Indian consulate, and have it adjudicated for stamp duty in India within the time allowed; your attorney can then sign the sale deed."),
          ("How do I transfer the sale proceeds to the US?", "Through your NRO account, up to USD 1 million per financial year, with Form 145 and a chartered accountant's certificate in Form 146."),
          ("Can BQP handle a US citizen's property sale in India?", "Yes. " + C)],
    related=[("us-citizen-buy-own-property-india-oci-fema-tax-fbar-2026.html", "US citizen owning property in India"),
             ("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html", "Inheriting from India while living abroad"),
             ("nri-property-tds-ldc-calculator.html", "NRI property TDS and LDC calculator"),
             ("india-us-dtaa-withholding-rates.html", "India-US treaty rates")],
    cta_h="Selling property in India from the US?", cta_b=C,
    keywords="US citizen selling property in India, can US citizen sell property in India, US citizen selling inherited property in India, US citizen selling property in India tax, power of attorney sell property India from USA, OCI sell property India, stepped up basis inherited property India",
    desc="US citizen selling property in India (2026), including inherited property: who can buy, TDS 12.5% plus surcharge and cess, Form 128, power of attorney from the US, USD 1 million repatriation, and US tax (0/15/20% plus NIIT, stepped-up basis, Form 1116 credit, Form 3520, FBAR).",
    howto={"name": "How a US citizen sells property in India", "description": "Indian and US steps.", "steps": [
        {"name": "Get documents in order", "text": "Title or will, succession papers, mutation, PAN."},
        {"name": "Estimate both taxes", "text": "Indian gain in rupees; US gain in dollars with stepped-up basis if inherited."},
        {"name": "Get a lower deduction certificate", "text": "Form 128 before the sale."},
        {"name": "Complete the sale", "text": "In person or by power of attorney; buyer deducts TDS."},
        {"name": "Repatriate and report", "text": "Forms 145/146 from NRO; Indian return; US return with Form 1116."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FZ complete")
