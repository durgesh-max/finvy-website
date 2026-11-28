# -*- coding: utf-8 -*-
"""Batch LW (28 Nov 2026): NRI inheriting Indian shares and mutual funds - transmission with or without a nominee, documents,
holding them on a non-repatriation basis, selling, capital gains with the previous owner's cost and holding period, TDS, and
repatriating proceeds from the NRO account.
Demand: 'nri inherited shares india', 'transmission of shares nri', 'inherited mutual funds nri', 'how to claim shares of deceased
parent from abroad', 'tax on sale of inherited shares nri' - only touched on the NRI inheritance property page; no dedicated page.
NRIs abroad dealing with a parent's portfolio need help. User steer 26 Nov / 19 Nov 2026: more call bookings, foreign audience.
Facts: inheritance itself is not taxed in India (receipts by inheritance are excluded from section 56(2)(x)); transmission of demat
shares through the depository participant with the death certificate and the claimant's KYC - simpler where a nominee is registered;
without a nominee, legal heir documents (succession certificate, probate or letter of administration, or the simplified documents
the rules allow); physical shares through the company's registrar; mutual fund units through the AMC or its registrar; an NRI or OCI
heir may acquire Indian securities by inheritance under FEMA and holds them on a non-repatriation basis in an NRO-linked demat; sale
proceeds go to the NRO account; repatriation from NRO balances is allowed up to USD 1 million per financial year with Forms 15CA /
15CB (site page); capital gains on sale use the previous owner's cost and holding period (sections 49 and 2(42A)); listed equity and
equity funds: long-term gains taxed at 12.5% above the annual exemption, short-term at 20% (from 23 July 2024; site NRI capital gains
page); TDS on NRI sales and redemptions is deducted by the payer; DTAA relief and Form 10F / TRC may apply. No fees, no portal menu
paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "nri-inherited-shares-mutual-funds-india-transmission-nominee-legal-heir-tax-on-sale-repatriation-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the holding statements (demat and mutual funds), "
     "whether you are the nominee, the death certificate, your country of residence and citizenship, your Indian bank and demat "
     "status (NRO / NRE), and whether you plan to sell. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="NRI Inheriting Indian Shares and Mutual Funds (2026): Transmission With or Without a Nominee, Holding on Non-Repatriation Basis, Tax on Sale and Repatriation",
    em="claim first, then decide whether to sell.",
    kicker="/ NRIs and OCI cardholders abroad &middot; Inherited shares and mutual funds in India &middot; Updated 2026-11-28",
    lead=("<strong>Inheriting a parent&rsquo;s Indian shares or mutual funds is not taxed in India, but the holdings must be transmitted to you before you can do anything with them. "
          "With a registered nominee the process is short; without one, legal heir documents are needed. "
          "As an NRI or OCI heir you hold them on a non-repatriation basis, pay capital gains on sale using your parent&rsquo;s cost and holding period, and repatriate the proceeds from your NRO account within the annual limit.</strong>"),
    sections=[
        ("/ Transmission", "Getting the holdings into your name.",
         table(["Holding", "Where to apply", "Key documents"], [
             ["Demat shares", "The depository participant (DP) of the deceased", "Death certificate, transmission form, claimant KYC (PAN, passport, overseas address), client master of your demat"],
             ["Physical shares", "The company&rsquo;s registrar and transfer agent", "Death certificate, transmission forms, claimant KYC; dematerialisation after transmission"],
             ["Mutual fund units", "The AMC or its registrar", "Death certificate, transmission request, claimant KYC and bank details"],
             ["No nominee registered", "Same channels", "Legal heir documents - succession certificate, probate or letter of administration, or the simplified documents the rules allow, with consent of other heirs"]])
         + ul("<strong>Your own accounts first:</strong> an NRI heir needs an NRO-linked demat (and NRI KYC with the fund houses) to receive the holdings.",
              "<strong>Nominee vs owner:</strong> a nominee receives the holdings, but other legal heirs may still have a claim under succession law - settle that within the family.")),
        ("/ Tax and repatriation", "When you sell.",
         ul("<strong>No tax on inheritance:</strong> receipts by inheritance are outside the gift tax rule.",
            "<strong>Cost and holding period:</strong> on sale, your cost is the previous owner&rsquo;s cost and the holding period includes theirs.",
            "<strong>Rates:</strong> listed equity shares and equity funds - long-term gains at 12.5% above the annual exemption, short-term at 20%; TDS is deducted by the broker or fund house on NRI sales.",
            "<strong>Repatriation:</strong> sale proceeds land in your NRO account; you can repatriate up to USD 1 million per financial year from NRO balances with Forms 15CA / 15CB.",
            "<strong>Your home country:</strong> report the inherited assets and gains where you live, and use the DTAA (with a TRC and Form 10F) to avoid double tax.")
         + call_box("inherited Indian shares and funds", ["Transmission with or without a nominee",
                                                          "NRO demat and NRI KYC",
                                                          "Capital gains computation with inherited cost",
                                                          "TDS, ITR and refunds",
                                                          "Repatriation with 15CA / 15CB"],
                    "Holding statements, nominee status, death certificate, residency, bank and demat status.")
         + sources("Income-tax Act, 1961 (sections 2(42A), 49, 56(2)(x), 112A, 111A and 195) and the corresponding provisions of the Income-tax Act, 2025; FEMA (Non-debt Instruments) Rules, 2019 and FEMA (Remittance of Assets) Regulations; SEBI and depository transmission procedures; site NRI inheritance, NRI capital gains, NRO to NRE and 15CA / 15CB pages.")),
    ],
    faqs=[("Is inheritance of shares or mutual funds taxed in India for an NRI?", "No. India has no inheritance tax, and assets received by inheritance are excluded from the gift tax rule. Tax arises only when you sell, as capital gains."),
          ("How does an NRI claim a deceased parent's demat shares?", "Apply to the parent's depository participant with the death certificate, the transmission form and your KYC, with an NRO-linked demat account to receive the shares. If no nominee was registered, legal heir documents are also needed."),
          ("What if no nominee was registered on the shares or mutual funds?", "The claimant must produce legal heir documents - a succession certificate, probate or letter of administration, or the simplified documents allowed by the rules, usually with consent of the other legal heirs."),
          ("How are capital gains calculated on inherited shares?", "Your cost is the previous owner's cost and the holding period includes their holding. Listed equity and equity funds held long term are taxed at 12.5% above the annual exemption; short-term gains at 20%."),
          ("Can an NRI repatriate money from selling inherited shares?", "Yes. Sale proceeds are credited to the NRO account, and up to USD 1 million per financial year can be repatriated from NRO balances with Forms 15CA and 15CB."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the holding statements, nominee status, death certificate, your residency and citizenship, your bank and demat status and your plans to sell. Or book a call directly.")],
    related=[("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of Indian property"),
             ("nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html", "NRI capital gains on Indian shares"),
             ("nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026.html", "NRO to NRE transfer and the USD 1 million limit"),
             ("change-nri-status-mutual-funds-demat-resident-to-nri-nri-to-resident-kyc-2026.html", "Change NRI status in mutual funds and demat")],
    cta_h="Inherited a parent&rsquo;s Indian portfolio?", cta_b=C,
    keywords="nri inherited shares india, transmission of shares nri, inherited mutual funds nri, claim shares of deceased parent from abroad, tax on sale of inherited shares nri, inherited shares cost holding period, repatriate inherited shares proceeds",
    desc="NRI inheriting Indian shares and mutual funds: no inheritance tax, transmission through the DP, registrar or AMC (nominee vs legal heir documents), holding on non-repatriation basis in NRO demat, capital gains with the previous owner's cost and holding period, TDS, and repatriation up to USD 1 million a year.",
    howto={"name": "How an NRI claims inherited Indian shares and funds", "description": "Claim, hold, sell, repatriate.", "steps": [
        {"name": "Open NRO demat and KYC", "text": "Set up accounts to receive the holdings."},
        {"name": "Apply for transmission", "text": "DP, registrar or AMC with death certificate and KYC; legal heir documents if no nominee."},
        {"name": "Plan the sale", "text": "Use the inherited cost and holding period; account for TDS."},
        {"name": "Repatriate", "text": "From NRO with 15CA / 15CB within USD 1 million a year; report abroad."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LW complete")
