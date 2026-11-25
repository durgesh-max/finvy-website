# -*- coding: utf-8 -*-
"""Batch IX (25 Nov 2026): FEMA rules for NRIs 2026 - plain-English hub. Bank accounts: a resident savings account must
be redesignated as NRO on becoming an NRI (FEMA Deposit Regulations, 2016); NRE / FCNR repatriable; NRO balances can
move to NRE within the USD 1 million a year limit (RBI amendment FEMA 5(R)(6)/2026-RB, 18 June 2026). Property: NRIs
can buy residential and commercial property but not agricultural land, plantation property or farmhouses (NDI Rules,
2019), except by inheritance; inherited agricultural land can be sold only to a person resident in India who is an
Indian citizen; sale proceeds of up to two residential properties bought with foreign exchange are repatriable.
Remittance: NRO balances, sale proceeds and inheritances up to USD 1 million per financial year (RBI Master Direction
on Remittance of Assets, updated 29 June 2026), with Forms 145 / 146 (old 15CA / 15CB). Investments: listed shares via
the portfolio investment route, mutual funds, existing PPF continues (no new PPF). Penalties: FEMA section 13 - up to
three times the sum involved, Rs 2 lakh where not quantifiable, Rs 5,000 a day for continuing breaches; compounding.
Demand: sweep ac115 (25 Nov 2026), all 7 markets: "fema rules for nri", "fema rules for nri savings account",
"fema rules for nri agricultural land", "fema rules for nri pdf", "fema rules india", "fema rules 2026".
Facts (checked 25 Nov 2026): RBI Master Direction - Remittance of Assets (updated 29 June 2026); RBI notification
FEMA 5(R)(6)/2026-RB; Ujjivan SFB, Kotak, ICICI and Motilal Oswal NRI notes; site NRI pages (accounts, property,
agricultural land, PPF, repatriation, penalties)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "fema-rules-for-nri-2026-savings-account-nro-property-agricultural-land-investment-repatriation-penalty"

C = contact("your country of residence, when you became an NRI, the Indian accounts, property and investments you hold, and what you want to do (buy, sell, invest or move money abroad)")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="FEMA Rules for NRIs (2026): Savings Account to NRO, Property and Agricultural Land, Investments, Repatriation Limits and Penalties",
    em="the rules that change the day you become an NRI.",
    kicker="/ NRIs and OCI cardholders &middot; FEMA &middot; Updated 2026-11-25",
    lead=("<strong>Under FEMA, an NRI cannot keep a resident savings account (it must be redesignated as NRO), can buy residential and commercial property but not agricultural land, plantation property or farmhouses, and can send up to USD 1 million a financial year abroad from NRO balances, sale proceeds and inheritances.</strong> "
          "NRE and FCNR balances are freely repatriable, and since June 2026 NRO balances can also be moved to NRE within the same USD 1 million limit. "
          "Breaches can attract penalties of up to three times the amount involved, so it pays to set things up correctly when your status changes."),
    sections=[
        ("/ FEMA rules for NRIs at a glance", "What you can and cannot do.",
         table(["Area", "Rule for NRIs"], [
             ["Resident savings account", "Not allowed; redesignate it as an NRO account (a resident can be a joint holder on a former-or-survivor basis)"],
             ["NRE / FCNR accounts", "Fund from foreign income; principal and interest freely repatriable"],
             ["NRO account", "For Indian income (rent, dividends, pension, sale proceeds); remittance abroad up to USD 1 million a financial year"],
             ["NRO to NRE transfer", "Allowed since June 2026, within the same USD 1 million limit"],
             ["Residential / commercial property", "Can buy, from foreign remittance or NRE / FCNR / NRO funds"],
             ["Agricultural land, plantation, farmhouse", "Cannot buy; can inherit; can sell only to a resident Indian citizen"],
             ["Shares and mutual funds", "Listed shares through the portfolio investment route; mutual funds subject to the fund house accepting NRIs from your country"],
             ["PPF", "No new account; an existing PPF continues to maturity"],
             ["Penalty for breach", "Up to three times the sum involved (FEMA section 13); compounding available"]])),
        ("/ Accounts and money abroad", "Savings account, NRO, NRE and the USD 1 million limit.",
         ul("<strong>Savings account:</strong> tell your bank when you become an NRI so it is redesignated as NRO; see the " + L("moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026.html", "moving abroad checklist") + ".",
            "<strong>NRE vs NRO vs FCNR:</strong> NRE interest is tax-free in India, NRO interest is taxable with TDS; see " + L("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR rules") + ".",
            "<strong>Sending money abroad:</strong> up to USD 1 million a financial year from NRO, sale proceeds and inheritances, with Forms 145 / 146 (old 15CA / 15CB); see " + L("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "repatriation step by step") + " and " + L("nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026.html", "NRO to NRE transfers") + ".",
            "<strong>Gifts:</strong> resident relatives can gift to NRIs within the rules; see " + L("nri-gift-indian-relatives-section-56-fema-2026.html", "gifts to NRI relatives") + ".")),
        ("/ Property, investments and penalties", "Buying, inheriting, investing and fixing mistakes.",
         ul("<strong>Property:</strong> see " + L("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "can an NRI buy property in India") + " and " + L("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of property") + ".",
            "<strong>Agricultural land:</strong> purchase is barred; inheritance is allowed and sale only to a resident Indian citizen; see " + L("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land") + ".",
            "<strong>Shares and funds:</strong> see " + L("how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026.html", "investing in Indian shares as an NRI") + " and " + L("nri-mutual-funds-india-tax.html", "NRI mutual funds") + ".",
            "<strong>PPF:</strong> see " + L("nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html", "PPF for NRIs") + ".",
            "<strong>Penalties and compounding:</strong> up to three times the sum involved, &#8377;2 lakh where it cannot be quantified, and up to &#8377;5,000 a day for continuing breaches; see " + L("fema-penalty-india-2026-section-13-violation-compounding-late-submission-fee-nri-company.html", "FEMA penalties and compounding") + ".")
         + call_box("NRI FEMA and tax", ["Account redesignation and NRE / NRO set-up",
                                          "Property purchase, sale and repatriation",
                                          "Forms 145 / 146 (15CA / 15CB)",
                                          "Inherited property and agricultural land",
                                          "FEMA compounding"],
                    "your accounts, property and plans.")
         + sources("Foreign Exchange Management Act, 1999; FEMA (Deposit) Regulations, 2016; FEMA (Non-Debt Instruments) Rules, 2019; FEMA (Remittance of Assets) Regulations and RBI Master Direction (updated 29 June 2026); RBI notification FEMA 5(R)(6)/2026-RB (18 June 2026); bank NRI guides (Ujjivan SFB, Kotak, ICICI); site NRI guides. Checked 25 November 2026.")),
    ],
    faqs=[("What are the main FEMA rules for NRIs?", "An NRI must redesignate resident savings accounts as NRO, can hold NRE and FCNR accounts, can buy residential and commercial property but not agricultural land, plantation property or farmhouses, can remit up to USD 1 million a financial year from NRO balances and sale proceeds, and cannot open a new PPF."),
          ("Can an NRI keep a savings account in India?", "No. Under FEMA a resident savings account must be redesignated as an NRO account once you become an NRI. You can also open an NRE account for foreign income."),
          ("Can an NRI buy agricultural land in India?", "No. NRIs and OCI cardholders cannot buy agricultural land, plantation property or farmhouses. They can inherit such land and can sell it only to a person resident in India who is an Indian citizen."),
          ("How much money can an NRI send abroad from India?", "Up to USD 1 million per financial year from NRO balances, property sale proceeds and inheritances, with Forms 145 and 146 (old 15CA and 15CB). NRE and FCNR balances are freely repatriable."),
          ("Can NRO money be moved to an NRE account?", "Yes. Since the RBI's June 2026 amendment, NRO balances can be transferred to NRE within the same USD 1 million annual limit, after tax is paid."),
          ("What is the penalty for breaking FEMA rules?", "Under FEMA section 13, up to three times the sum involved, or Rs 2 lakh where the amount cannot be quantified, plus up to Rs 5,000 a day for continuing breaches. Many breaches can be compounded with the RBI."),
          ("Can BQP help an NRI with FEMA compliance?", "Yes. CA Durgesh Chavda can set up NRE / NRO accounts correctly, handle property purchase, sale and repatriation, Forms 145 / 146 and FEMA compounding. " + C)],
    related=[("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India"),
             ("can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html", "Can an NRI buy property?"),
             ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land"),
             ("moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026.html", "Becoming an NRI checklist"),
             ("fema-penalty-india-2026-section-13-violation-compounding-late-submission-fee-nri-company.html", "FEMA penalties")],
    cta_h="Got Indian accounts or property abroad?", cta_b=C,
    keywords="fema rules for nri, fema rules for nri savings account, fema rules for nri agricultural land, fema rules india 2026, nri savings account to nro, nri repatriation limit usd 1 million, fema penalty nri, can nri buy agricultural land",
    desc="FEMA rules for NRIs (2026): savings account must become NRO, NRE / FCNR repatriable, NRO to NRE within USD 1 million, property yes but agricultural land no, PPF, shares, repatriation and FEMA section 13 penalties, in one plain-English summary.",
    howto={"name": "How to become FEMA-compliant after becoming an NRI", "description": "For new NRIs.", "steps": [
        {"name": "Redesignate accounts", "text": "Convert resident savings accounts to NRO."},
        {"name": "Open NRE / FCNR", "text": "Route foreign income through repatriable accounts."},
        {"name": "Update investments", "text": "Demat, mutual funds, PPF and KYC updated to NRI status."},
        {"name": "Plan property and remittances", "text": "Use the USD 1 million NRO limit with Forms 145 / 146."},
        {"name": "Fix past gaps", "text": "Compound any FEMA breach with the RBI."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IX complete")
