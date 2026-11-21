# -*- coding: utf-8 -*-
"""Batch FE (21 Nov 2026): TDS when you buy shares of an Indian company from a non-resident (NRI or foreign company).
Call-first page for buyers, sellers and deal teams.
Demand: sweep 21 Nov 2026 (ac39), all 7 markets: "tds on purchase of shares from non resident", "tds on purchase of
unlisted shares from non resident", "tds on sale of unlisted shares by non resident", "tds on sale of shares by non
resident", "tds on capital gains on sale of shares by non resident". The site had the NRI listed-share page (broker TDS)
but nothing for off-market or unlisted share purchases.
Facts (checked 21 Nov 2026):
- Section 195 of the 1961 Act is section 393(2) of the Income-tax Act, 2025: any person (resident or non-resident)
  paying a non-resident a sum chargeable to tax deducts tax at the rates in force (site page; TDSMAN, Lexverge 2026 guides).
  Quarterly statement Form 144 (formerly 27Q).
- Rates carried over: long-term capital gains 12.5% (unlisted shares held over 24 months; listed over 12 months, above
  INR 1.25 lakh via section 112A); short-term on listed shares with STT 20%; short-term on unlisted shares at normal
  rates - 30% top slab for individuals, 35% for a foreign company (site NRI shares page, branch-vs-subsidiary page);
  plus surcharge and 4% cess.
- Lower or nil deduction certificate: Form 128 (formerly Form 13), section 395 (site page).
- Treaties: Mauritius, Singapore and Cyprus - shares acquired before 1 April 2017 grandfathered, later acquisitions
  taxable in India, subject to limitation-of-benefits and principal purpose tests (site treaty pages). US and UK
  treaties leave share gains to domestic law. Netherlands treaty exempts some share sales (site Netherlands page).
- Fair value: Rule 11UA value is the floor for the seller's consideration and the buyer's deemed income on unlisted
  shares (sections 50CA and 56(2)(x) of the 1961 Act); FEMA pricing and Form FC-TRS within 60 days (site FC-TRS page).
- No-TAN route from 1 October 2026 (Form 141 Schedule E) covers only immovable property bought by resident individuals
  and HUFs (site page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026"

C = contact("who is selling (NRI or foreign company) and their country, the Indian company, the price, when the shares were acquired and the planned closing date")
PAGES = [dict(
    slug=SLUG,
    title="TDS on Purchase of Shares From a Non-Resident (2026): Rates for Unlisted and Listed Shares, Who Deducts, Treaty Relief and the Lower Deduction Certificate",
    em="what the buyer must withhold before paying an NRI or foreign seller.",
    kicker="/ Share transfers &middot; Non-residents &middot; Withholding tax &middot; Updated 2026-11-21",
    lead=("<strong>If you buy shares of an Indian company from a non-resident, you must deduct Indian tax from the price before you pay.</strong> "
          "This applies whether the seller is an NRI or a foreign company, and whether the buyer is in India or abroad. "
          "The tax is on the seller&rsquo;s capital gain: <strong>12.5%</strong> if unlisted shares were held for more than 24 months, and the normal rate if held for less (<strong>up to 30% for an individual, 35% for a foreign company</strong>), plus surcharge and 4% cess. "
          "If the gain is not worked out and certified, the tax office can expect deduction on the <strong>whole price</strong>. "
          "The fixes are a Chartered Accountant&rsquo;s computation of the gain, a <strong>lower or nil deduction certificate (Form 128)</strong>, or a <strong>tax treaty</strong> claim with a tax residency certificate. "
          "A buyer who does not deduct can be made to pay the tax, interest and a penalty. On-market sales of listed shares are different: the NRI&rsquo;s bank or broker deducts the tax."),
    sections=[
        ("/ Rates at a glance", "What to withhold on the seller&rsquo;s gain.",
         table(["Shares sold by a non-resident", "Holding period", "Tax rate on the gain", "Who deducts"], [
             ["Unlisted shares (private company, start-up)", "More than 24 months", "12.5%", "The buyer"],
             ["Unlisted shares", "24 months or less", "Normal rates: up to 30% for an individual, 35% for a foreign company", "The buyer"],
             ["Listed shares sold off-market", "More than 12 months", "12.5%", "The buyer"],
             ["Listed shares sold on the exchange by an NRI", "More than 12 months", "12.5% above INR 1.25 lakh a year", "The NRI&rsquo;s bank or broker"],
             ["Listed shares sold on the exchange by an NRI", "12 months or less", "20%", "The NRI&rsquo;s bank or broker"]])
         + '<p>Surcharge and 4% cess are added. For example, 12.5% becomes 13% with cess alone, and up to about 13.65% for a foreign company at the highest surcharge. A treaty rate, where one applies, is used without surcharge or cess.</p>'
         + call_box("Buying or selling Indian company shares with a non-resident on one side", ["How much the buyer must withhold on this deal",
                                                                                               "Computing and certifying the seller&rsquo;s gain",
                                                                                               "A lower or nil deduction certificate before closing",
                                                                                               "Treaty position for the seller&rsquo;s country",
                                                                                               "Fair value, FEMA pricing, Form FC-TRS and the bank remittance forms"],
                    "the seller&rsquo;s country and status, the Indian company, price, original cost and purchase date of the shares, and the closing date.")),
        ("/ Step by step", "What the buyer does.",
         ul("<strong>1. Confirm the seller is non-resident</strong> for tax, and get PAN, tax residency certificate and Form 41 (formerly Form 10F) if a treaty is claimed.",
            "<strong>2. Work out the gain:</strong> sale price less cost, with the holding period. For a non-resident who bought unlisted shares in foreign currency, the computation rules differ from a resident&rsquo;s; have a CA certify it.",
            "<strong>3. Decide the amount to deduct:</strong> tax on the certified gain, or on the figure in a lower or nil deduction certificate. See <a href=\"nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html\">Form 128, formerly Form 13</a>.",
            "<strong>4. Get a TAN</strong> if you do not have one. A foreign buyer needs one too. The no-TAN route that began on 1 October 2026 covers only property bought by individuals and HUFs.",
            "<strong>5. Deduct, deposit and report:</strong> deduct at payment, deposit the tax by the 7th of the next month, file the quarterly statement in Form 144 (formerly 27Q) and give the seller the TDS certificate.",
            "<strong>6. FEMA side:</strong> price within the fair-value rule, Form FC-TRS within 60 days, and Form 145 and 146 for the bank if money is remitted abroad. See <a href=\"how-to-transfer-shares-between-resident-nri-foreign-step-by-step.html\">transferring shares between residents and non-residents</a>.")),
        ("/ Practical points", "Where deals go wrong.",
         ul("<strong>Non-resident buyer, non-resident seller:</strong> the duty to deduct still applies when the shares are of an Indian company. A foreign buyer needs a PAN and TAN in India for this.",
            "<strong>Treaty relief:</strong> sellers in Mauritius, Singapore or Cyprus keep exemption only for shares acquired before 1 April 2017, and must pass the treaty&rsquo;s anti-abuse tests. The US and UK treaties let India tax the gain. A few treaties, such as the Netherlands, still exempt some share sales. Get this checked before agreeing to deduct nothing.",
            "<strong>Fair value matters twice:</strong> if unlisted shares are sold below fair value under the tax rules, the seller is taxed as if the fair value was received and the buyer can be taxed on the discount. FEMA sets its own price limits. See <a href=\"fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html\">FEMA valuation reports</a>.",
            "<strong>Escrow, earn-outs and deferred payments:</strong> tax is deducted when each amount is paid or credited, so the share purchase agreement should say how.",
            "<strong>Indemnity is not a substitute:</strong> the tax office recovers from the buyer first. A tax indemnity from a seller who has left India is hard to enforce.",
            "<strong>Seller&rsquo;s refund:</strong> if too much is deducted, the seller recovers it by filing an Indian return. That takes months, which is why a lower deduction certificate before closing is worth the effort.",
            "<strong>Selling the foreign holding company instead:</strong> a sale of an overseas company can also be taxed in India if most of its value comes from Indian assets. Ask before assuming an offshore deal is outside India.")
         + '<p>Related: <a href="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html">section 195 is now section 393</a> &middot; <a href="nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html">NRI capital gains on listed shares</a> &middot; <a href="due-diligence-indian-company-foreign-buyer.html">due diligence on an Indian company</a> &middot; <a href="india-mauritius-tax-treaty-dtaa.html">India-Mauritius treaty</a> &middot; <a href="india-singapore-tax-treaty-dtaa.html">India-Singapore treaty</a> &middot; <a href="tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html">TDS on other payments to foreign companies</a>.</p>'
         + sources("Income-tax Act, 2025, section 393(2) (formerly section 195 of the Income-tax Act, 1961) and the capital gains rate provisions carried over from the Finance (No. 2) Act, 2024; lower deduction certificate provisions (section 395, Form 128); fair-value rules for unlisted shares (Rule 11UA); India&rsquo;s tax treaties with Mauritius, Singapore, Cyprus, the Netherlands, the United States and the United Kingdom; FEMA (Non-debt Instruments) Rules, 2019 and Form FC-TRS; 2026 practitioner guides on section 393 (TDSMAN, Lexverge). Checked 21 November 2026. General information; the rate for a deal depends on its facts.")),
    ],
    faqs=[("Is TDS applicable on purchase of shares from a non-resident?", "Yes. A buyer of shares of an Indian company from a non-resident must deduct Indian tax on the seller's capital gain before paying, under section 393 of the Income-tax Act, 2025 (formerly section 195). On-market sales of listed shares by NRIs are handled by the NRI's bank or broker."),
          ("What is the TDS rate on sale of unlisted shares by a non-resident?", "12.5% on long-term gains (shares held more than 24 months) and normal rates on short-term gains, up to 30% for an individual and 35% for a foreign company, plus surcharge and 4% cess. A treaty may reduce this."),
          ("Is TDS deducted on the full sale price or only on the gain?", "Tax is due on the capital gain. To deduct on the gain only, the buyer needs a reliable computation, normally certified by a Chartered Accountant, or a lower or nil deduction certificate in Form 128. Without either, the tax office can expect deduction on the whole payment."),
          ("Does a foreign buyer have to deduct TDS when buying Indian shares from another foreign seller?", "Yes. The duty applies to any person paying a non-resident a sum taxable in India, including a non-resident buyer. The buyer needs an Indian PAN and TAN to deposit the tax."),
          ("Can a tax treaty remove the TDS?", "Sometimes. Sellers in Mauritius, Singapore and Cyprus are exempt only for shares acquired before 1 April 2017 and must meet anti-abuse tests; the US and UK treaties allow India to tax the gain. The seller must give a tax residency certificate and Form 41."),
          ("What happens if the buyer does not deduct TDS?", "The buyer can be treated as in default and asked to pay the tax, with interest and a penalty, even though the gain was the seller's."),
          ("Can BQP handle the withholding on our share purchase?", "Yes. " + C)],
    related=[("how-to-transfer-shares-between-resident-nri-foreign-step-by-step.html", "Transferring shares between residents and non-residents"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Lower or nil TDS certificate (Form 128)"),
             ("due-diligence-indian-company-foreign-buyer.html", "Due diligence on an Indian company")],
    cta_h="Share purchase with a non-resident seller?", cta_b=C,
    keywords="TDS on purchase of shares from non resident, TDS on sale of unlisted shares by non resident, TDS on sale of shares by non resident, section 195 shares non resident, section 393 TDS capital gains, lower deduction certificate share sale, buying shares from NRI TDS, foreign company selling Indian shares tax",
    desc="Buying shares of an Indian company from an NRI or foreign company (2026): the buyer deducts tax on the seller's gain - 12.5% long-term on unlisted shares, up to 30% or 35% short-term, plus surcharge and cess. CA computation, Form 128 certificate, treaty relief, TAN and Form 144.",
    howto={"name": "How to deduct TDS when buying shares from a non-resident", "description": "Buyer's steps.", "steps": [
        {"name": "Confirm the seller's status", "text": "Non-resident; collect PAN, tax residency certificate and Form 41."},
        {"name": "Compute the gain", "text": "Price less cost, with holding period, certified by a CA."},
        {"name": "Fix the rate", "text": "12.5% long-term, normal rates short-term, or the treaty or certificate rate."},
        {"name": "Deduct and deposit", "text": "At payment; deposit by the 7th of the next month using a TAN."},
        {"name": "Report", "text": "Quarterly Form 144, TDS certificate to the seller, and Form FC-TRS within 60 days."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FE complete")
