# -*- coding: utf-8 -*-
"""Batch EM (20 Nov 2026): Can an NRI invest in bonds in India - government securities and T-bills (RBI Retail Direct),
corporate bonds and NCDs, tax-free bonds, RBI Floating Rate Savings Bonds, NSC - tax and TDS. Call-first page.
Demand: sweep 20 Nov 2026 (ac28), all 7 markets: "can nri invest in government bonds", "rbi retail direct for nri",
"can nri invest in rbi floating rate bonds", "can nri invest in treasury bills", "can nri invest in corporate bonds",
"can nri invest in ncd", "can nri invest in nsc", "government tax free nri bonds". No site page.
Facts (checked 20 Nov 2026): RBI Retail Direct - non-resident retail investors eligible to invest in government
securities under FEMA can open a Retail Direct Gilt account (needs an Indian rupee bank account, typically NRO, PAN, KYC);
NRIs can hold G-secs, state development loans and T-bills; RBI Master Direction on non-resident investment in debt
instruments amended 10 April 2026 (circular 06) defines NRI and keeps NRI investments outside investment limits
(Legal500); Floating Rate Savings Bonds 2020 (Taxable) are for resident individuals and HUFs - NRIs not eligible;
sovereign gold bonds closed to NRIs; NSC - no new purchase by NRIs, existing certificates bought while resident
continue to maturity; tax-free bond interest exempt (section 10(15)) and such bonds can be bought on exchanges;
listed corporate bonds/NCDs available to NRIs subject to FEMA and the offer terms; tax: interest taxable in India with
TDS for non-residents, treaty caps with TRC and Form 10F (Form 41); capital gains on listed bonds held over 12 months at
12.5% without indexation, unlisted bonds and debentures taxed at slab rates (from 23 July 2024)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "can-nri-invest-in-bonds-india-government-securities-rbi-retail-direct-ncd-tax-free-bonds-2026"

C = contact("your country of residence, the bonds you hold or plan to buy (G-secs, T-bills, NCDs, tax-free bonds), the account you will fund from (NRE or NRO) and whether you need to repatriate")
PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Invest in Bonds in India? (2026) Government Securities and T-Bills via RBI Retail Direct, Corporate Bonds and NCDs, Tax-Free Bonds - and What Is Not Allowed",
    em="what you can buy, through which account, and how the interest is taxed.",
    kicker="/ NRI &middot; Bonds &middot; RBI Retail Direct &middot; Tax &middot; Updated 2026-11-20",
    lead=("<strong>Yes, mostly.</strong> NRIs can buy <strong>government securities, state development loans and treasury bills</strong>, including directly through <strong>RBI Retail Direct</strong>. That needs a Retail Direct Gilt account linked to an Indian bank account, usually NRO, plus a PAN and KYC. "
          "NRIs can also buy <strong>listed corporate bonds and NCDs</strong>, subject to FEMA and the offer terms, and <strong>tax-free bonds</strong> on the stock exchange. Tax-free bond interest is exempt. "
          "<strong>Not allowed:</strong> RBI Floating Rate Savings Bonds, which are for residents only; new sovereign gold bonds; and new NSCs. Certificates bought while you were resident can continue to maturity. "
          "Interest is taxed in India, TDS is deducted for non-residents, and treaty rates can reduce it if you give a TRC and Form 10F. Listed bonds held for more than 12 months are taxed at <strong>12.5%</strong> on the gain, while gains on <strong>unlisted bonds and debentures</strong> are taxed at slab rates."),
    sections=[
        ("/ What NRIs can and cannot buy", "Instrument by instrument.",
         table(["Instrument", "NRI?", "How", "Tax points"], [
             ["Government securities (G-secs), SDLs", "Yes", "RBI Retail Direct, a bank or a broker; repatriable if funded from NRE", "Interest taxable; TDS; treaty cap with TRC"],
             ["Treasury bills", "Yes", "RBI Retail Direct or a bank", "Discount taxed as income"],
             ["Listed corporate bonds and NCDs", "Yes, subject to FEMA and offer terms", "Broker or public issue that allows NRIs", "Interest taxable; listed gains over 12 months at 12.5%"],
             ["Tax-free bonds (PSU)", "Yes, on the exchange", "Broker (secondary market)", "Interest exempt; gains taxable"],
             ["RBI Floating Rate Savings Bonds", "No", "Residents and HUFs only", "-"],
             ["Sovereign gold bonds", "No new purchase", "Existing ones bought as resident can be held", "See the NRI gold guide"],
             ["NSC", "No new purchase", "Existing certificates continue to maturity", "Interest taxable"],
             ["Unlisted bonds / debentures", "Depends on FEMA route", "Private placement", "Gains at slab rates"]])
         + call_box("Investing in Indian bonds as an NRI", ["Which instruments fit your account (NRE or NRO) and repatriation needs",
                                                            "Opening RBI Retail Direct and linking the right bank account",
                                                            "TDS on interest and claiming the treaty rate",
                                                            "Tax in your country (US, UK, Canada, Australia, Singapore, UAE)",
                                                            "Filing the Indian return to recover excess TDS"],
                    "your PAN, bank accounts, country of residence and the bonds you hold or plan to buy.")),
        ("/ Tax and practical points", "Before you invest.",
         ul("<strong>Repatriation:</strong> investments made from an NRE account are generally repatriable; NRO-funded investments go back to NRO and abroad within the USD 1 million facility.",
            "<strong>TDS on interest:</strong> payers deduct tax on interest paid to non-residents; give a tax residency certificate and <a href=\"nri-form-10f-e-filing-mandatory-india-2026.html\">Form 10F</a> for the treaty rate (for example 12.5% for UAE residents on interest, as summarised in the <a href=\"india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html\">India-UAE guide</a>).",
            "<strong>Capital gains:</strong> listed bonds held over 12 months: 12.5% without indexation; unlisted bonds and debentures: slab rates whatever the holding period.",
            "<strong>Refunds:</strong> excess TDS comes back only through an Indian return; see <a href=\"nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html\">NRO interest refund calculator</a>.",
            "<strong>US persons:</strong> individual bonds are generally not PFICs, unlike Indian mutual funds, but report accounts in FBAR and Form 8938.",
            "<strong>GIFT City:</strong> dollar bonds and deposits in GIFT IFSC are another route; see <a href=\"gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html\">GIFT City for NRIs</a>.")
         + '<p>Related: <a href="can-nri-buy-gold-in-india-physical-digital-gold-etf-sgb-tax-repatriation-2026.html">NRI gold guide</a> &middot; <a href="nri-mutual-funds-india-tax.html">NRI mutual funds</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR accounts</a>.</p>'
         + sources("RBI Retail Direct scheme (eligibility of non-resident retail investors eligible under FEMA); RBI Master Direction on non-resident investment in debt instruments, as amended by circular 06 of 10 April 2026 (Legal500 summary); RBI Floating Rate Savings Bonds 2020 (Taxable) scheme terms; NSC scheme rules; Income-tax provisions on interest, TDS for non-residents, section 10(15) exemptions and capital gains on listed and unlisted bonds (from 23 July 2024). Guides checked 20 November 2026 (Investing.com, Belong, Zee Business). Confirm eligibility with RBI Retail Direct and your bank before investing.")),
    ],
    faqs=[("Can an NRI invest in government bonds in India?", "Yes. NRIs eligible under FEMA can buy government securities, state development loans and treasury bills, including directly through RBI Retail Direct."),
          ("Can an NRI open an RBI Retail Direct account?", "Yes. Non-resident retail investors eligible to invest in government securities under FEMA can open a Retail Direct Gilt account linked to an Indian bank account (usually NRO), with PAN and KYC."),
          ("Can an NRI invest in RBI Floating Rate Savings Bonds?", "No. The Floating Rate Savings Bonds 2020 (Taxable) are open to resident individuals and HUFs only."),
          ("Can an NRI invest in corporate bonds or NCDs?", "Generally yes for listed corporate bonds and NCDs, subject to FEMA and the terms of the issue; check whether a public issue accepts NRI applications."),
          ("Can an NRI buy NSC?", "No new NSC can be bought by an NRI; certificates bought while resident can be held to maturity."),
          ("Can BQP help with NRI bond investments and tax?", "Yes. " + C)],
    related=[("can-nri-buy-gold-in-india-physical-digital-gold-etf-sgb-tax-repatriation-2026.html", "NRI gold guide"), ("nri-mutual-funds-india-tax.html", "NRI mutual funds"),
             ("gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html", "GIFT City for NRIs")],
    cta_h="Thinking of Indian bonds from abroad?", cta_b=C,
    keywords="can NRI invest in bonds in India, can NRI invest in government bonds, RBI Retail Direct for NRI, can NRI invest in RBI floating rate bonds, can NRI invest in treasury bills, can NRI invest in NCD, can NRI invest in NSC, tax free bonds NRI",
    desc="Can an NRI invest in bonds in India (2026)? Yes: G-secs, SDLs and T-bills (RBI Retail Direct with an NRO-linked account), listed corporate bonds/NCDs and tax-free bonds; not RBI Floating Rate Savings Bonds, new SGBs or new NSCs. TDS, treaty rates, 12.5% on listed gains.",
    howto={"name": "How an NRI invests in Indian government bonds", "description": "Through RBI Retail Direct.", "steps": [
        {"name": "Check the funding account", "text": "NRE for repatriable investments, NRO otherwise."},
        {"name": "Open a Retail Direct Gilt account", "text": "With PAN, KYC and the linked Indian bank account."},
        {"name": "Buy G-secs or T-bills", "text": "In auctions or the secondary market."},
        {"name": "Claim the treaty rate", "text": "Give a TRC and Form 10F to reduce TDS on interest."},
        {"name": "File the Indian return", "text": "Report interest and gains; claim excess TDS back."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EM complete")
