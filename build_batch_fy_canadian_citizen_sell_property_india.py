# -*- coding: utf-8 -*-
"""Batch FY (24 Nov 2026): Canadian citizen (or Canadian resident NRI) selling property in India - who can buy from you,
Indian TDS and tax, repatriation, and Canadian tax (50% inclusion, foreign tax credit, T1135). Call-first page.
Demand: sweep ac51 (24 Nov 2026), all 7 markets: "canadian citizen selling property in india". The site had the
India-Canada treaty page and general NRI sale pages, not a Canada-specific sale page.
Facts (checked 24 Nov 2026):
- FEMA: a person of Indian origin (foreign citizen, including OCI) can sell residential or commercial property to a
  resident Indian, NRI or OCI; agricultural land, plantation or farmhouse only to an Indian citizen resident in India
  (site pages on NRI/OCI property and agricultural land).
- Indian tax: long-term (over 24 months) 12.5% without indexation plus surcharge and cess; short-term at slab rates
  (TDS at 30% plus surcharge and cess); buyer deducts TDS; lower deduction certificate Form 128 (formerly Form 13); from
  1 October 2026 resident buyers can deposit TDS via Form 141 without TAN (site pages).
- Repatriation: sale proceeds from NRO up to USD 1 million per financial year with Forms 145 and 146 (formerly 15CA/15CB)
  (site pages).
- Canada: residents taxed on worldwide income; capital gains inclusion rate remains one-half after the proposed increase
  was cancelled on 21 March 2025 (Prime Minister's announcement; CRA); India-Canada treaty lets India tax gains on Indian
  immovable property and Canada gives a foreign tax credit (site treaty page). Form T1135 for specified foreign property
  costing over CAD 100,000; personal-use property is not specified foreign property."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "canadian-citizen-selling-property-in-india-tds-tax-repatriation-canada-capital-gains-2026"

C = contact("the property's city and type, when and how it was bought or inherited, the expected sale price, whether you are a Canadian citizen or an Indian citizen living in Canada, and your timeline")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Canadian Citizen Selling Property in India (2026): Who Can Buy, TDS, Indian Tax, Repatriation and Canadian Capital Gains",
    em="taxed in India first, then in Canada with a credit.",
    kicker="/ NRIs &middot; Canada &middot; Property sale &middot; Updated 2026-11-24",
    lead=("<strong>A Canadian citizen of Indian origin can sell a house, flat or commercial property in India to a resident Indian, an NRI or an OCI holder; agricultural land can be sold only to a resident Indian citizen.</strong> "
          "India taxes the gain first: the buyer deducts TDS, at <strong>12.5% plus surcharge and cess</strong> on long-term gains (property held over 24 months) unless you obtain a <strong>lower deduction certificate (Form 128)</strong>, and you file an Indian return. "
          "You can send up to <strong>USD 1 million a year</strong> of the proceeds to Canada from your NRO account with Forms 145 and 146. "
          "Canada then taxes <strong>50% of the gain</strong> (the inclusion rate stayed at one-half after the planned increase was cancelled in March 2025), with a <strong>foreign tax credit</strong> for the Indian tax under the India-Canada treaty."),
    sections=[
        ("/ Quick answers", "What Canadians selling in India ask.",
         ul("<strong>Can a Canadian citizen sell property in India?</strong> Yes. As a person of Indian origin you can sell residential or commercial property to a resident Indian, an NRI or an OCI. Agricultural land, a plantation or a farmhouse can be sold only to an Indian citizen resident in India.",
            "<strong>How much TDS will the buyer deduct?</strong> On a long-term gain, 12.5% plus surcharge and cess; on a short-term gain, 30% plus surcharge and cess. Without a lower deduction certificate, buyers often deduct on the whole sale price, so apply for Form 128 before the sale.",
            "<strong>Do I pay tax in Canada too?</strong> Yes, if you are a Canadian tax resident: half the gain is taxable, and the Indian tax paid is credited against the Canadian tax on that gain.",
            "<strong>How do I get the money to Canada?</strong> Through your NRO account, up to USD 1 million per financial year, with Form 145 and a CA&rsquo;s certificate in Form 146.",
            "<strong>Do I need to visit India?</strong> Not necessarily: a registered power of attorney executed in Canada (attested and adjudicated in India) lets a relative sign the sale deed.")),
        ("/ India vs Canada", "Two tax calculations on one sale.",
         table(["", "India", "Canada"], [
             ["Who is taxed", "Non-resident seller on Indian property", "Canadian residents on worldwide income"],
             ["Gain measured in", "Rupees: sale price minus cost (no indexation for non-residents)", "Canadian dollars at the exchange rates on purchase and sale"],
             ["Rate", "Long-term 12.5% plus surcharge and cess; short-term at slab rates", "50% of the gain added to income at your marginal rate"],
             ["Relief", "Section 54 or 54F if you buy another house in India; 54EC bonds for land or building gains", "Foreign tax credit for the Indian tax under the India-Canada treaty"],
             ["Paperwork", "TDS by the buyer, Form 128 certificate, Indian return, Forms 145/146", "Report on your Canadian return; Form T1135 if the property was held as an investment costing over CAD 100,000"]])
         + '<p>Because the gain is measured in different currencies, the Indian and Canadian gains can differ a lot; rupee depreciation can make the Canadian gain smaller than the Indian one. See the ' + L("india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html", "India-Canada tax treaty") + '.</p>'),
        ("/ Steps", "Selling from Canada without surprises.",
         ul("<strong>1. Check title and documents:</strong> sale deed or inheritance papers, mutation, tax receipts, PAN.",
            "<strong>2. Work out the gain</strong> in India and estimate the Canadian tax.",
            "<strong>3. Apply for the lower deduction certificate</strong> (Form 128) so TDS matches the real tax; see " + L("nri-property-tds-ldc-calculator.html", "the TDS and LDC calculator") + ".",
            "<strong>4. Sign or give power of attorney;</strong> the buyer deducts TDS (from 1 October 2026 a resident buyer can deposit it under their own PAN in Form 141).",
            "<strong>5. Receive proceeds in your NRO account</strong> and remit to Canada with Forms 145 and 146.",
            "<strong>6. File the Indian return</strong> to claim any excess TDS back, then report the gain in Canada and claim the foreign tax credit.")
         + call_box("selling property in India from Canada", ["Indian capital gain and TDS",
                                                               "Lower deduction certificate (Form 128)",
                                                               "Repatriation to Canada",
                                                               "Canadian tax and foreign tax credit",
                                                               "Reinvestment options in India"],
                    "the property details, purchase or inheritance documents and the expected sale price.")
         + sources("FEMA (Non-debt Instruments) Rules, 2019 on acquisition and transfer of immovable property by NRIs and OCIs; Income-tax Act provisions on long-term capital gains (12.5% without indexation for non-residents from 23 July 2024) and TDS on payments to non-residents; Form 128 lower deduction certificate; CBDT Notification 121/2026 (Form 141 without TAN from 1 October 2026); RBI rules on remittance of up to USD 1 million per financial year from NRO accounts; Prime Minister of Canada announcement of 21 March 2025 cancelling the capital gains inclusion rate increase and CRA guidance; India-Canada Double Taxation Avoidance Agreement; CRA Form T1135. Checked 24 November 2026.")),
    ],
    faqs=[("Can a Canadian citizen sell property in India?", "Yes. A Canadian citizen of Indian origin can sell residential or commercial property to a resident Indian, an NRI or an OCI holder. Agricultural land, a plantation or a farmhouse can be sold only to an Indian citizen resident in India."),
          ("What is the TDS when a Canadian citizen sells property in India?", "On a long-term gain (property held over 24 months), 12.5% plus surcharge and cess; on a short-term gain, 30% plus surcharge and cess. A lower deduction certificate in Form 128 can reduce TDS to the tax actually due."),
          ("Is the sale of Indian property taxable in Canada?", "Yes, for Canadian tax residents. Half of the gain, measured in Canadian dollars, is added to income, and the Indian tax paid is credited against the Canadian tax under the India-Canada treaty."),
          ("How much money can I transfer from India to Canada after selling property?", "Up to USD 1 million per financial year from your NRO account, with Form 145 and a chartered accountant's certificate in Form 146."),
          ("Can I sell my property in India without travelling from Canada?", "Yes, through a registered power of attorney executed in Canada, attested there and adjudicated in India within the time allowed, which lets a relative sign the sale deed."),
          ("Can BQP handle the sale from Canada?", "Yes. " + C)],
    related=[("india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html", "India-Canada tax treaty"),
             ("nri-selling-indian-property-capital-gains.html", "NRI selling Indian property"),
             ("nri-property-tds-ldc-calculator.html", "NRI property TDS and LDC calculator"),
             ("buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", "Buying from an NRI: no TAN from 1 October 2026"),
             ("indian-ca-for-clients-in-canada.html", "Indian CA for clients in Canada")],
    cta_h="Selling property in India from Canada?", cta_b=C,
    keywords="Canadian citizen selling property in India, sell property in India from Canada, NRI Canada property sale tax, TDS NRI property sale Canada, India Canada DTAA capital gains, repatriate property sale proceeds to Canada, Canada capital gains foreign property",
    desc="Canadian citizen selling property in India (2026): who can buy (resident, NRI, OCI; farmland only to resident citizens), TDS 12.5% plus surcharge and cess on long-term gains, Form 128 certificate, USD 1 million a year repatriation, and Canadian tax at 50% inclusion with a foreign tax credit.",
    howto={"name": "How a Canadian citizen sells property in India", "description": "Indian and Canadian steps.", "steps": [
        {"name": "Check documents", "text": "Title, mutation, tax receipts, PAN."},
        {"name": "Estimate both taxes", "text": "Indian gain in rupees, Canadian gain in dollars."},
        {"name": "Get a lower deduction certificate", "text": "Form 128 before the sale."},
        {"name": "Complete the sale", "text": "In person or by registered power of attorney; buyer deducts TDS."},
        {"name": "Repatriate and file", "text": "Forms 145/146 from NRO; Indian return; Canadian return with foreign tax credit."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FY complete")
