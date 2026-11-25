# -*- coding: utf-8 -*-
"""Batch JH (25 Nov 2026): NRI investment options in India (2026) - hub. Permitted routes and how each is taxed and
repatriated: NRE FD (interest tax-free while non-resident, fully repatriable), NRO FD (interest taxable, TDS about 31.2%,
treaty rate with TRC / Form 10F, repatriation within USD 1 million a financial year), FCNR (B) deposits (foreign currency,
1-5 years, interest tax-free while non-resident, no currency risk), mutual funds (NRE = repatriable, NRO = non-repatriable;
TDS on redemption; many AMCs restrict US / Canada residents), listed shares through PIS / demat (equity STCG 20%, LTCG
12.5% above Rs 1.25 lakh), government securities and bonds (RBI Retail Direct), NPS Tier I (18-85, some providers 70;
80CCD in the old regime), GIFT City (dollar FDs, IFSC funds, insurance), property (residential and commercial allowed;
agricultural land, plantation and farmhouse barred except inheritance). Not allowed: new PPF, NSC, SCSS, Sukanya and other
post office small savings accounts (old PPF / NSC continue to maturity). No product recommendations, no return figures.
Demand: sweep ac118 (25 Nov 2026), 6-7 markets: "nri investment in india", "nri investment options in india", "nri
investment schemes in india", "nri investment plans in india", "nri investment in india tax free", "nri investment".
Facts (checked 25 Nov 2026): site NRE / NRO / FCNR, NRI mutual fund, stock market / PIS, bonds, NPS, GIFT City, PPF,
post-office-scheme eligibility, FEMA rules for NRIs and NRI property pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "nri-investment-options-in-india-2026-schemes-nre-fd-fcnr-mutual-funds-shares-nps-bonds-gift-city-tax-repatriation"

C = contact("your country of residence, whether the money is earned abroad (NRE) or in India (NRO), the options you are considering, and whether you plan to bring the money back abroad")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="NRI Investment Options in India (2026): Schemes and Plans Compared - NRE FD, FCNR, Mutual Funds, Shares, NPS, Bonds, GIFT City and Property, With Tax and Repatriation",
    em="the account you invest from decides whether the money can go back.",
    kicker="/ NRIs and OCI cardholders &middot; Investing in India &middot; Updated 2026-11-25",
    lead=("<strong>NRIs can invest in India through NRE, NRO and FCNR deposits, mutual funds, listed shares, government bonds, NPS, GIFT City products and residential or commercial property, but not in new PPF, NSC, Senior Citizens' Savings Scheme or Sukanya Samriddhi accounts.</strong> "
          "Money invested from an NRE account is generally repatriable; money from an NRO account can be sent abroad only within the USD 1 million a year limit. "
          "Interest on NRE and FCNR deposits is tax-free while you are non-resident; most other returns are taxed in India and may also be taxed where you live."),
    sections=[
        ("/ NRI investment options at a glance", "What is allowed, how it is taxed and whether it can go back.",
         table(["Option", "Fund it from", "Tax in India", "Repatriation"], [
             ["NRE fixed deposit", "Foreign income (NRE)", "Interest tax-free while non-resident", "Fully repatriable"],
             ["FCNR (B) deposit", "Foreign currency, 1-5 years", "Interest tax-free while non-resident", "Fully repatriable; no currency risk"],
             ["NRO fixed deposit", "Indian income (NRO)", "Interest taxable; TDS about 31.2% unless a treaty rate applies", "Within USD 1 million a year"],
             ["Mutual funds", "NRE or NRO", "Equity: 20% short term, 12.5% long term above &#8377;1.25 lakh; TDS on redemption", "Repatriable if invested from NRE"],
             ["Listed shares (PIS / demat)", "NRE or NRO", "Same as equity funds", "Repatriable if bought from NRE"],
             ["Government securities and bonds", "NRE or NRO", "Interest taxable unless a bond is tax-free", "Depends on the account"],
             ["NPS Tier I", "NRE or NRO", "Deduction under section 80CCD in the old regime", "As per NPS exit rules"],
             ["GIFT City (IFSC) products", "Foreign currency", "Specific exemptions for IFSC funds and deposits", "Held in foreign currency"],
             ["Residential or commercial property", "NRE, NRO or home loan", "Rent and gains taxed in India", "Rules depend on how it was paid for"],
             ["New PPF, NSC, SCSS, Sukanya", "Not allowed", "-", "-"]])
         + '<p>This page lists the routes NRIs are permitted to use and how they are taxed; it is not advice on which product to buy. Returns, risk and suitability are for you and your financial adviser.</p>'),
        ("/ Deposits and fixed income", "Bank deposits, bonds and pensions.",
         ul("<strong>NRE vs NRO vs FCNR:</strong> NRE and FCNR interest is tax-free while you are non-resident; NRO interest is taxable with TDS; see " + L("nre-nro-fcnr-account-tax-rules.html", "NRI fixed deposits and account tax rules") + ".",
            "<strong>Reclaiming NRO TDS:</strong> TDS on NRO interest is often higher than the final tax or the treaty rate; see the " + L("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest TDS refund calculator") + ".",
            "<strong>Bonds and government securities:</strong> NRIs can buy government securities and T-bills through RBI Retail Direct and listed bonds; see " + L("can-nri-invest-in-bonds-india-government-securities-rbi-retail-direct-ncd-tax-free-bonds-2026.html", "can an NRI invest in bonds") + ".",
            "<strong>NPS:</strong> NRIs and OCI cardholders can open NPS Tier I, funded from NRE or NRO; see " + L("nps-for-nri-oci-account-opening-nre-nro-tax-deduction-80-percent-lump-sum-exit-2026.html", "NPS for NRIs") + ".",
            "<strong>Small savings schemes:</strong> NRIs cannot open new PPF, NSC, SCSS or Sukanya accounts; accounts opened while resident run to maturity; see " + L("nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html", "NRI PPF rules") + " and " + L("is-nri-eligible-87a-rebate-indexation-nps-ppf-scss-sukanya-post-office-schemes-2026.html", "which schemes NRIs can use") + ".")),
        ("/ Markets, GIFT City and property", "Equity, IFSC products and real estate.",
         ul("<strong>Mutual funds:</strong> invest after NRI KYC; many fund houses do not accept investors resident in the US or Canada; TDS is deducted on redemption; see " + L("nri-mutual-funds-india-tax.html", "NRI mutual fund tax") + ".",
            "<strong>Shares:</strong> buy listed shares through a demat account linked to an NRE (repatriable, under the portfolio investment route) or NRO account; see " + L("how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026.html", "investing in Indian shares from abroad") + ".",
            "<strong>GIFT City:</strong> dollar deposits, IFSC funds and insurance held in foreign currency; see " + L("gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html", "GIFT City for NRIs") + ".",
            "<strong>Property:</strong> NRIs can buy residential and commercial property but not agricultural land, plantations or farmhouses (except by inheritance); see " + L("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "can an NRI buy property in India") + " and " + L("fema-rules-for-nri-2026-savings-account-nro-property-agricultural-land-investment-repatriation-penalty.html", "FEMA rules for NRIs") + ".",
            "<strong>Tax where you live:</strong> your country of residence may tax Indian income too; a tax treaty and foreign tax credit usually prevent double tax. Estimate the Indian side with the " + L("nri-income-tax-calculator-india-2026-27-new-old-regime-capital-gains-tds-refund.html", "NRI income tax calculator") + ".")
         + call_box("Investing in India as an NRI", ["Account structure (NRE, NRO, FCNR)",
                                                     "Tax on interest, gains and rent",
                                                     "Treaty rates, TRC and Form 10F",
                                                     "Repatriation and Form 15CA / 15CB",
                                                     "Annual ITR and TDS refunds"],
                    "your country and the options you are considering.")
         + sources("FEMA (Deposit) Regulations, FEMA (Non-Debt Instruments) Rules, 2019 and RBI directions on remittance from NRO accounts; Income-tax Act (NRE / FCNR interest exemption, capital gains rates, TDS on non-residents); PFRDA rules on NPS; small savings scheme rules; site NRE / NRO / FCNR, mutual fund, PIS, bonds, NPS, GIFT City, PPF and property guides. Checked 25 November 2026. Not investment advice.")),
    ],
    faqs=[("What are the investment options for NRIs in India?", "NRE, NRO and FCNR fixed deposits, mutual funds, listed shares, government securities and bonds, NPS Tier I, GIFT City products and residential or commercial property. NRIs cannot open new PPF, NSC, SCSS or Sukanya Samriddhi accounts."),
          ("Which NRI investments in India are tax-free?", "Interest on NRE and FCNR deposits is tax-free in India while you are non-resident. Most other income, such as NRO interest, capital gains and rent, is taxable in India."),
          ("Can an NRI invest in mutual funds and shares in India?", "Yes, after NRI KYC, through NRE (repatriable) or NRO accounts; shares are bought through a demat account under the portfolio investment route. Many fund houses do not accept investors resident in the US or Canada."),
          ("Can an NRI invest in PPF or post office schemes?", "Not in new accounts. PPF and NSC opened while resident continue to maturity, but NRIs cannot open new PPF, NSC, SCSS, Sukanya Samriddhi or other small savings accounts."),
          ("Can NRIs take their investment money back abroad?", "Investments made from an NRE account are generally repatriable with the proceeds; money in an NRO account can be remitted within USD 1 million a financial year after tax, usually with Form 15CA / 15CB."),
          ("Can BQP advise on NRI investments in India?", "CA Durgesh Chavda advises on the tax, FEMA and repatriation side: account structure, tax on interest, gains and rent, treaty relief, TDS refunds and annual returns. He does not recommend specific investment products. " + C)],
    related=[("nre-nro-fcnr-account-tax-rules.html", "NRE vs NRO vs FCNR"),
             ("nri-mutual-funds-india-tax.html", "NRI mutual fund tax"),
             ("how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026.html", "Investing in Indian shares"),
             ("gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html", "GIFT City for NRIs"),
             ("fema-rules-for-nri-2026-savings-account-nro-property-agricultural-land-investment-repatriation-penalty.html", "FEMA rules for NRIs")],
    cta_h="Investing in India from abroad?", cta_b=C,
    keywords="nri investment options in india, nri investment in india, nri investment schemes in india, nri investment plans in india, nri investment in india tax free, best investment for nri in india, nri fd, fcnr, nri mutual funds, nri nps",
    desc="NRI investment options in India 2026: NRE, NRO and FCNR deposits, mutual funds, shares, bonds, NPS, GIFT City and property compared by tax and repatriation; which schemes NRIs cannot use (new PPF, NSC, SCSS, Sukanya).",
    howto={"name": "How an NRI chooses where to invest in India", "description": "The tax and FEMA checks.", "steps": [
        {"name": "Pick the account", "text": "NRE for foreign income (repatriable), NRO for Indian income."},
        {"name": "Check what is allowed", "text": "Deposits, funds, shares, bonds, NPS, GIFT City, property; not new PPF / NSC."},
        {"name": "Check the tax", "text": "NRE / FCNR interest tax-free; others taxed in India and possibly abroad."},
        {"name": "Plan repatriation", "text": "NRO money within USD 1 million a year, with Form 15CA / 15CB."},
        {"name": "File and claim", "text": "ITR-2 or ITR-3 to settle tax and reclaim excess TDS."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JH complete")
