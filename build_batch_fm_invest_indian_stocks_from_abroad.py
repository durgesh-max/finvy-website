# -*- coding: utf-8 -*-
"""Batch FM (22 Nov 2026): How to invest in the Indian stock market from the USA, UK, UAE and elsewhere - NRIs, OCI
cardholders and foreign nationals. Step-by-step hub. Call-first.
Demand: sweep 22 Nov 2026 (ac44), all 7 markets: "how nri can invest in indian stock market", "nri can invest in indian
stock market", "invest in india stock market from usa", "invest in india stocks from usa", "how to invest in india
stocks from uk", "how to invest in sip in india from uk", "investing in india from usa reddit".
Facts, each already sourced on a site page checked this month:
- SEBI circular of 4 Nov 2026: from 3 Dec 2026 NRIs, OCIs and foreign nationals in FATF-compliant countries can do KYC
  digitally from abroad (video verification) (site page).
- FEMA: repatriable investment in listed shares through the bank's designated route (Portfolio Investment Scheme with an
  NRE account; since June 2026 also a designated repatriable rupee account); non-repatriable through NRO. Since 13 June
  2026 an individual may hold below 10% of a listed company, 24% aggregate (site pages).
- 2026 amendments opened the repatriable Schedule III route to any individual resident outside India, not only NRIs and
  OCIs; reported by the bank on Form LEC (IFI); land-border-country approval rule unchanged (site page).
- India tax on listed shares: 12.5% long-term (over 12 months) above INR 1.25 lakh, 20% short-term, plus surcharge and
  cess; broker deducts TDS for NRIs; refunds via return (site NRI shares page).
- Home country: US PFIC rules on Indian mutual funds; UK non-reporting offshore fund rules (income tax on gains);
  Canada T1135 above CAD 100,000; Singapore and UAE generally no tax on the gains (site mutual funds abroad page).
- Many Indian fund houses restrict investments by residents of the US and Canada because of FATCA reporting; check each
  fund house (stated as a check, not a rule)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 22 November 2026."
SLUG = "how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026"

C = contact("the country you live in, whether you are an NRI, OCI cardholder or foreign national, what you want to buy (shares, mutual funds, SIP), and whether you already have NRE, NRO or demat accounts")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="How to Invest in the Indian Stock Market From the USA, UK, UAE or Anywhere Abroad (2026): NRIs, OCIs and Foreign Nationals - Accounts, KYC, Limits and Tax",
    em="the accounts, the paperwork, and the tax on both sides.",
    kicker="/ NRIs &middot; Foreign investors &middot; Shares &middot; Updated 2026-11-22",
    lead=("<strong>You can buy listed Indian shares from abroad through an Indian broker, a demat account and an Indian bank account that the rules allow for this.</strong> "
          "<strong>NRIs and OCI cardholders</strong> use an NRE account with the bank&rsquo;s portfolio investment route if they want to send the money back abroad freely, or an NRO account if they do not. "
          "Since 2026, <strong>any foreign individual</strong> can also buy listed Indian shares on a repatriable basis. Each person can hold <strong>less than 10%</strong> of a company. "
          "From <strong>3 December 2026</strong>, KYC can be completed by video from most countries, without visiting India. "
          "India taxes the gains at <strong>12.5%</strong> (held over 12 months, above INR 1.25 lakh a year) or <strong>20%</strong> (shorter), and the broker deducts tax at sale. "
          "Your home country may also tax them. <strong>Indian mutual funds are the trap</strong>: US investors face PFIC rules, and UK investors usually pay income tax on the gains."),
    sections=[
        ("/ Which route is yours", "By who you are.",
         table(["You are", "Bank account", "Can the money go back abroad freely?", "Notes"], [
             ["NRI", "NRE account with the bank&rsquo;s portfolio investment route", "Yes", "Fund from abroad or from NRE balances"],
             ["NRI", "NRO account", "Only within USD 1 million a year, with Forms 145 and 146", "Use for Indian income such as rent or dividends"],
             ["OCI cardholder", "Same as an NRI", "Same as an NRI", "OCI cardholders invest on the same footing as NRIs for listed shares"],
             ["Foreign national (not of Indian origin)", "Designated repatriable rupee account at an Indian bank", "Yes", "Opened up in 2026; bank reports each purchase on Form LEC"],
             ["Citizen or entity of a country sharing a land border with India", "Approval rules apply", "-", "Government approval is still needed where ownership or control would pass"]])
         + '<p>Limits for listed companies: each individual below 10% of a company&rsquo;s paid-up capital, all such investors together up to 24% unless the company raises it.</p>'
         + call_box("Investing in India from abroad", ["Which account route fits you and your country",
                                                       "Opening accounts and KYC from abroad",
                                                       "Tax in India: TDS at sale, refunds and the annual return",
                                                       "Tax at home: US PFIC, UK offshore fund rules, treaty credit",
                                                       "Moving the money back when you sell"],
                    "your country, your status (NRI, OCI or foreign national), what you want to buy and the accounts you already have.")),
        ("/ Step by step", "From no account to your first trade.",
         ul("<strong>1. PAN:</strong> an Indian PAN is needed. NRIs, OCIs and foreigners can apply from abroad; see " + L("nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund.html", "PAN from abroad") + ".",
            "<strong>2. Bank account:</strong> NRE with portfolio investment permission (repatriable) or NRO (non-repatriable). Foreign nationals open the designated rupee account.",
            "<strong>3. Demat and trading account:</strong> with a broker that serves non-residents. From 3 December 2026, KYC can be done by video from FATF-compliant countries. See " + L("nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html", "KYC from abroad") + ".",
            "<strong>4. Fund and trade:</strong> send money through banking channels; buy on the exchange through the linked bank route. NRIs are not allowed to day-trade or short-sell in the cash segment.",
            "<strong>5. Tax at sale:</strong> the broker deducts TDS on the gain. File an Indian return to recover any excess and to carry forward losses.",
            "<strong>6. Report at home:</strong> declare the account and gains where you live, and claim credit for the Indian tax where a treaty allows it.")),
        ("/ Tax on both sides", "India first, then home.",
         table(["", "India", "Where you live"], [
             ["Listed shares", "12.5% long-term above INR 1.25 lakh a year; 20% short-term; plus surcharge and cess; TDS by the broker", "Usually taxable, with credit for Indian tax under a treaty"],
             ["Indian mutual funds", "Same India rates; TDS at redemption", "US: PFIC rules, often punitive. UK: usually non-reporting offshore funds, so gains are taxed as income. Canada: T1135 above CAD 100,000"],
             ["Dividends", "Taxed in India; treaty rate with a tax residency certificate and Form 41", "Taxable at home, with credit"],
             ["UAE or Singapore resident", "India tax as above", "Generally no tax on the gains there"]])
         + ul("<strong>US residents and citizens:</strong> many Indian fund houses do not accept US or Canadian residents because of FATCA reporting; check before investing. Direct shares avoid PFIC.",
              "<strong>UK residents:</strong> check HMRC&rsquo;s reporting fund list before buying any Indian fund. See " + L("indian-mutual-funds-uk-resident-non-reporting-offshore-fund-hmrc-letter-2026-us-pfic-canada-australia.html", "Indian funds while living abroad") + ".",
              "<strong>Returning to India later:</strong> accounts must be redesignated when you become resident; see " + L("change-nri-status-mutual-funds-demat-resident-to-nri-nri-to-resident-kyc-2026.html", "changing status on demat and funds") + ".")
         + '<p>Related: ' + L("nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html", "NRI capital gains on Indian shares") + ' &middot; ' + L("foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html", "foreign individuals and listed shares") + ' &middot; ' + L("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "OCI bank accounts") + ' &middot; ' + L("nro-to-nre-transfer-limit-tax-form-145-146-15ca-15cb-documents-usd-1-million-2026.html", "NRO to NRE transfer") + ' &middot; ' + L("what-is-pfic.html", "what is a PFIC") + '.</p>'
         + sources("SEBI circular of 4 November 2026 on KYC for non-residents (effective 3 December 2026); Foreign Exchange Management (Non-debt Instruments) Rules, 2019, Schedule III, as amended in 2026, and the Mode of Payment and Reporting Regulations (June 2026); Income-tax Act provisions on capital gains of non-residents and withholding; HMRC offshore funds rules; US PFIC rules (Internal Revenue Code sections 1291 to 1298). Each point is sourced in detail on the linked page. Checked 22 November 2026. General information, not investment advice.")),
    ],
    faqs=[("Can an NRI invest in the Indian stock market?", "Yes. An NRI invests in listed Indian shares through a demat and trading account linked to an NRE account with the bank's portfolio investment route (repatriable) or an NRO account (non-repatriable)."),
          ("Can a US citizen or foreigner buy Indian shares?", "Yes. OCI cardholders invest like NRIs, and since 2026 any individual resident outside India can buy listed Indian shares on a repatriable basis through a designated rupee account, below 10% of a company each. Citizens of countries sharing a land border with India face approval rules."),
          ("Can I open an Indian demat account from abroad?", "Yes. From 3 December 2026, NRIs, OCI cardholders and foreign nationals in FATF-compliant countries can complete KYC digitally by video without visiting India."),
        ("What is the full form of PIS account, and do I need one?", "PIS stands for Portfolio Investment Scheme, the RBI route under which an NRI or OCI buys and sells listed Indian shares through one designated bank. A PIS account is generally needed to trade shares on the stock exchange on a repatriable basis through an NRE account; a non-PIS NRO route is used for non-repatriable investing, and mutual funds and IPO applications are handled differently. Only one designated bank can be used, joint PIS accounts are not allowed, and intraday trading and short selling are not permitted. Rules and bank charges change, so confirm with your bank and broker."),
          ("How are Indian shares taxed for someone living abroad?", "India taxes long-term gains on listed shares at 12.5% above INR 1.25 lakh a year and short-term gains at 20%, plus surcharge and cess, with tax deducted by the broker. The country where you live may tax the gain too, usually with credit for the Indian tax."),
          ("Should a US resident buy Indian mutual funds?", "Usually not without advice. Indian mutual funds are generally PFICs for US taxpayers, which can mean heavy tax and reporting, and many Indian fund houses do not accept US residents. Direct shares avoid PFIC."),
        ("Can foreigners invest in Indian mutual funds?", "NRIs and OCI cardholders can, after KYC, paying from an NRE or NRO account; some fund houses do not accept investors living in the US or Canada. The 2026 opening for other foreign individuals covers listed shares through a repatriable rupee account; for mutual fund units, foreign nationals who are not NRIs or OCIs generally use the foreign portfolio investor route, which needs registration through a custodian. Check with the fund house and your bank before investing, and check how your home country taxes foreign funds."),
        ("Can an OCI cardholder start a SIP in Indian mutual funds?", "Yes. OCI cardholders invest like NRIs: complete KYC (video KYC from most countries from 3 December 2026), link an NRE or NRO account, and choose a fund house that accepts residents of your country."),
          ("Can I do a SIP in India from the UK?", "An NRI in the UK can, if the fund house accepts UK residents, but most Indian funds are non-reporting offshore funds for UK tax, so gains are taxed as income at your marginal rate. Check HMRC's reporting fund list first."),
          ("Can BQP help me invest in India from abroad?", "Yes, with accounts, tax and repatriation; we do not recommend specific investments. " + C)],
    related=[("nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html", "Demat KYC from abroad"),
             ("nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html", "NRI capital gains on Indian shares"),
             ("indian-mutual-funds-uk-resident-non-reporting-offshore-fund-hmrc-letter-2026-us-pfic-canada-australia.html", "Indian funds while living abroad")],
    cta_h="Investing in India from abroad?", cta_b=C,
    keywords="how NRI can invest in Indian stock market, invest in Indian stock market from USA, invest in India stocks from UK, NRI demat account from abroad, OCI invest in Indian shares, foreigner buy Indian shares, PIS account NRI, SIP in India from UK, Indian mutual funds PFIC US",
    desc="How to invest in Indian shares from the USA, UK, UAE (2026): NRIs and OCIs via NRE-PIS or NRO, any foreign individual now via a repatriable rupee account (under 10% each), video KYC from 3 December 2026, 12.5% / 20% Indian tax with broker TDS, and the US PFIC and UK fund traps.",
    howto={"name": "How to invest in the Indian stock market from abroad", "description": "Steps for NRIs, OCIs and foreign nationals.", "steps": [
        {"name": "Get a PAN", "text": "Apply from abroad if you do not have one."},
        {"name": "Open the right bank account", "text": "NRE with portfolio investment route, NRO, or a designated rupee account for foreign nationals."},
        {"name": "Open demat and trading accounts", "text": "Video KYC from FATF-compliant countries from 3 December 2026."},
        {"name": "Fund and buy", "text": "Through banking channels and the linked bank route."},
        {"name": "Handle tax", "text": "Broker TDS in India, an Indian return for refunds, and reporting at home."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FM complete")
