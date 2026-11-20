# -*- coding: utf-8 -*-
"""Batch EG (20 Nov 2026): Can an NRI buy gold in India - physical gold, gold ETFs, gold mutual funds, sovereign gold
bonds, digital gold - tax on sale, TDS and repatriation. Call-first page.
Demand: sweep 20 Nov 2026 (ac21), all 7 markets: "can nri buy physical gold in india", "can nri buy digital gold in
india"; no site page on NRI gold investment.
Facts (checked 20 Nov 2026): NRIs may buy physical gold and jewellery in India and listed gold ETFs (exchange, through
NRE/NRO/PIS-linked accounts, broker rules vary); NRIs cannot subscribe to sovereign gold bonds, though bonds bought as
a resident may be held to maturity; no new SGB tranche since February 2024; Budget 2026 (Finance Act 2026) limits the
tax-free redemption at maturity to individuals who subscribed at original issue, from 1 April 2026 - secondary-market
buyers taxable (reports: NISM, Business Today, Taxmann, Value Research); SEBI advisory of 8 November 2025: digital
gold / e-gold sold by online platforms is outside SEBI regulation with no investor protection, unlike gold ETFs and
electronic gold receipts; capital gains: physical gold and unlisted gold funds long-term after 24 months, listed gold
ETFs after 12 months, long-term rate 12.5% without indexation (transfers from 23 July 2024), short-term at slab rates;
the INR 1.25 lakh exemption is for listed equity, not gold; sale proceeds generally credited to NRO and repatriated
within USD 1 million per financial year with Forms 145/146 (old 15CA/15CB); foreign tax credit in country of
residence."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "can-nri-buy-gold-in-india-physical-digital-gold-etf-sgb-tax-repatriation-2026"

C = contact("your country of residence, what gold you hold or plan to buy in India (jewellery, coins, ETF, SGB, digital gold), when it was bought, and whether you plan to sell or repatriate")
PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Buy Gold in India? (2026) Physical Gold, Gold ETFs, Sovereign Gold Bonds and Digital Gold - Tax on Sale and Repatriation",
    em="what is allowed, how gains are taxed, and how to move the money abroad.",
    kicker="/ NRI &middot; Gold &middot; Capital gains &middot; Repatriation &middot; Updated 2026-11-20",
    lead=("<strong>Yes.</strong> An NRI can buy <strong>physical gold and jewellery</strong> in India and can invest in <strong>listed gold ETFs</strong> through an NRE or NRO-linked demat account, subject to the broker&rsquo;s rules for the NRI&rsquo;s country. "
          "An NRI <strong>cannot subscribe to sovereign gold bonds</strong>, but bonds bought while resident can be held to maturity. No new SGB tranche has been issued since February 2024, and from 1 April 2026 the tax-free redemption at maturity applies only to the original subscriber. "
          "<strong>Digital gold</strong> sold by apps is outside SEBI regulation, and SEBI warned on 8 November 2025 that it carries no investor protection. "
          "On sale, physical gold and gold mutual funds become long-term after <strong>24 months</strong> and listed gold ETFs after <strong>12 months</strong>. Long-term gains are taxed at <strong>12.5%</strong> without indexation, and short-term gains at slab rates. "
          "Sale proceeds usually go to the <strong>NRO account</strong> and can be repatriated within <strong>USD 1 million</strong> a financial year with Forms 145 and 146 (formerly 15CA and 15CB)."),
    sections=[
        ("/ Gold options for NRIs", "What is allowed and how each is taxed.",
         table(["Option", "Can an NRI buy?", "Long-term after", "Tax on sale", "Points to note"], [
             ["Physical gold, coins, jewellery", "Yes, using NRE or NRO funds", "24 months", "12.5% long-term; slab rate short-term", "Keep invoices; cash purchases are restricted; PAN for large purchases"],
             ["Listed gold ETF", "Yes, through an NRI demat and trading account", "12 months", "12.5% long-term; slab rate short-term", "TDS on NRI gains is usually deducted by the broker or bank"],
             ["Gold mutual fund / fund of funds", "Yes, subject to the fund house&rsquo;s rules for your country", "24 months (check the scheme)", "12.5% long-term; slab rate short-term", "Some fund houses limit US and Canada residents"],
             ["Sovereign gold bonds", "No new subscription; existing holdings can continue", "12 months if listed and sold", "Maturity redemption tax-free only for original subscribers from 1 April 2026", "No new tranche since February 2024"],
             ["Digital gold (apps)", "Platform terms vary", "24 months", "As physical gold", "Not SEBI-regulated; SEBI advisory of 8 November 2025"]])
         + call_box("Selling or holding gold in India as an NRI", ["Which of your gold holdings are long-term and the tax on sale",
                                                                    "TDS deducted and how to claim a refund in the ITR",
                                                                    "Moving the proceeds abroad through NRO, Forms 145 and 146",
                                                                    "Foreign tax credit in the UAE, US, UK, Canada, Australia or Singapore",
                                                                    "SGBs held from your resident years and the 2026 tax change"],
                    "the type of gold, purchase dates and cost, your bank accounts in India and your country of residence.")),
        ("/ Steps before you sell", "Tax, TDS and getting the money out.",
         ul("<strong>Gather cost proof:</strong> purchase invoices, inheritance or gift documents; for inherited gold, the previous owner&rsquo;s cost and holding period carry over.",
            "<strong>Work out the gain:</strong> 24 months for physical gold and gold funds, 12 months for listed ETFs; long-term at 12.5% without indexation, short-term at slab rates. The INR 1.25 lakh exemption is for listed equity, not gold.",
            "<strong>TDS:</strong> buyers and brokers paying a non-resident are generally required to deduct tax; report the sale in your ITR either way and claim any excess TDS as a refund. See <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR an NRI files</a>.",
            "<strong>Repatriate:</strong> proceeds are usually credited to the NRO account; up to USD 1 million a financial year can be sent abroad with Forms 145 and 146. See <a href=\"repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html\">repatriation from NRO</a>.",
            "<strong>Home country:</strong> report the gain where you live and claim credit for Indian tax under the treaty; the UAE has no personal income tax.",
            "<strong>Carrying gold:</strong> check baggage and customs limits on both sides; see <a href=\"nri-visiting-india-december-2026-baggage-rules-gold-cash-gifts-property-tax-checklist.html\">NRI December trip: baggage, gold and cash</a>.")
         + '<p>Related: <a href="nri-mutual-funds-india-tax.html">NRI mutual funds</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR accounts</a> &middot; <a href="nri-taxation-india-complete-guide.html">NRI taxation guide</a>.</p>'
         + sources("Income-tax Act provisions on capital gains (12.5% long-term rate for transfers from 23 July 2024; 12/24-month holding periods); Finance Act 2026 change to the sovereign gold bond redemption exemption (reported by NISM, Business Today, Taxmann and Value Research, February 2026); SEBI press advisory on digital gold, 8 November 2025; RBI sovereign gold bond scheme terms; FEMA rules on NRO repatriation (USD 1 million). Checked 20 November 2026. Confirm a fund house&rsquo;s rules for your country before investing.")),
    ],
    faqs=[("Can an NRI buy gold in India?", "Yes. An NRI can buy physical gold and jewellery and can invest in listed gold ETFs and, subject to fund-house rules, gold mutual funds."),
          ("Can an NRI invest in sovereign gold bonds?", "No new subscription is allowed for NRIs, and no new tranche has been issued since February 2024. Bonds bought while resident can be held to maturity."),
          ("Is digital gold safe for NRIs?", "Digital gold sold by apps is not regulated by SEBI; SEBI's 8 November 2025 advisory said such products carry no securities-market investor protection. Gold ETFs and electronic gold receipts are regulated."),
          ("How is gold sold by an NRI taxed in India?", "Physical gold and gold funds are long-term after 24 months and listed gold ETFs after 12 months; long-term gains are taxed at 12.5% without indexation and short-term gains at slab rates."),
          ("Can an NRI send gold sale proceeds abroad?", "Yes. Proceeds are usually credited to the NRO account and up to USD 1 million a financial year can be repatriated with Forms 145 and 146 (formerly 15CA and 15CB)."),
          ("Can BQP help with tax on selling gold in India?", "Yes. " + C)],
    related=[("nri-visiting-india-december-2026-baggage-rules-gold-cash-gifts-property-tax-checklist.html", "NRI December trip: baggage, gold, cash"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from NRO"), ("nri-mutual-funds-india-tax.html", "NRI mutual funds")],
    cta_h="Holding or selling gold in India from abroad?", cta_b=C,
    keywords="can NRI buy gold in India, can NRI buy digital gold, NRI gold ETF, NRI sovereign gold bond, tax on gold sale NRI, gold capital gains 24 months 12.5%, NRI gold repatriation NRO, SEBI digital gold warning",
    desc="Can an NRI buy gold in India (2026)? Yes: physical gold and listed gold ETFs; no new sovereign gold bonds; digital gold is not SEBI-regulated. Long-term after 24 months (ETFs 12) at 12.5%; proceeds via NRO, up to USD 1 million a year with Forms 145/146.",
    howto={"name": "How an NRI sells gold in India and moves the money abroad", "description": "Tax, TDS and repatriation steps.", "steps": [
        {"name": "Collect cost proof", "text": "Invoices, gift or inheritance papers, purchase dates."},
        {"name": "Compute the gain", "text": "24 months for physical gold and funds, 12 for listed ETFs; 12.5% long-term."},
        {"name": "Handle TDS", "text": "Check TDS deducted and claim any excess in the ITR."},
        {"name": "Credit to NRO and repatriate", "text": "Up to USD 1 million a financial year with Forms 145 and 146."},
        {"name": "Report in your country", "text": "Declare the gain and claim treaty credit for Indian tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EG complete")
