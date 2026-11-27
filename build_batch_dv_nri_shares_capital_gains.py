# -*- coding: utf-8 -*-
"""Batch DV (20 Nov 2026): NRI capital gains tax on Indian shares (LTCG/STCG, TDS by broker, accounts, treaty, refunds).
Call-first page. Demand: sweep 20 Nov 2026 (ac18), all 7 markets: "nri long term capital gains tax on shares", "nri
short term capital gains tax on shares", "do you pay capital gains tax on foreign shares"; site had NRI mutual fund and
property pages but no NRI shares page.
Facts: listed equity shares (STT paid) - long-term after 12 months at 12.5% above INR 1.25 lakh a year (section 112A),
short-term at 20% (section 111A), rates from 23 July 2024; for NRIs the broker/payer deducts TDS on the gain (plus
surcharge and cess); NRIs cannot set the basic exemption limit against these special-rate gains; dividends - TDS 20%
plus surcharge and cess or treaty rate with TRC and Form 10F; buybacks taxed as capital gains from 1 April 2026;
repatriable trading through NRE-linked accounts designated for portfolio investment (PIS) and non-repatriable through
NRO; most treaties let India tax gains on Indian shares (Singapore/Mauritius grandfathering only for shares acquired
before 1 April 2017); losses carried forward only if the return is filed on time; residence-country tax and foreign
tax credit; SEBI digital KYC from abroad from 3 December 2026 (site page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
NS = "nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026"
NYE = "nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency"

C_NS = contact("your country of residence, broker and account type (NRE/PIS or NRO), the gains and TDS for the year, and any losses")
PAGES = [dict(
    slug=NS,
    title="NRI Capital Gains Tax on Indian Shares (2026): LTCG 12.5% Above INR 1.25 Lakh, STCG 20%, TDS by the Broker, Treaty Relief and Getting Refunds",
    em="for NRIs trading or investing in Indian stocks from abroad.",
    kicker="/ NRIs &middot; Shares &middot; Capital gains &middot; Updated 2026-11-20",
    lead=("NRIs pay the same capital gains rates on <strong>listed Indian shares</strong> as residents. Gains on shares held <strong>over 12 months</strong> are long-term and taxed at <strong>12.5% above INR 1.25 lakh</strong> a year; shorter holdings are taxed at <strong>20%</strong>, plus surcharge and cess in both cases. The big difference is <strong>TDS</strong>: for NRIs the broker deducts tax on the gain at the time of sale, often more than the final tax. NRIs also <strong>cannot use the basic exemption limit</strong> against these gains, which residents can. "
          "Most tax treaties let India tax gains on Indian shares, so treaty relief is limited. Older shares bought by Singapore and Mauritius residents before 1 April 2017 are the main exception. Your country of residence may also tax the gain and give credit for Indian tax. "
          "To recover excess TDS and carry forward losses, file an Indian return. For FY 2025-26 that means a belated or revised return by <strong>31 December 2026</strong>."),
    sections=[
        ("/ Rates and TDS at a glance", "Listed equity shares (STT paid).",
         table(["Item", "Rate / rule", "NRI-specific point"], [
             ["Long-term gains (held over 12 months)", "12.5% on gains above INR 1.25 lakh in the year", "TDS deducted by the broker; basic exemption cannot be used"],
             ["Short-term gains (12 months or less)", "20%", "TDS deducted by the broker"],
             ["Surcharge and cess", "Added to the above", "Raises the effective TDS rate"],
             ["Dividends", "Taxable; TDS 20% plus surcharge and cess, or treaty rate", "Give TRC and Form 10F to the company or registrar"],
             ["Buybacks (from 1 April 2026)", "Taxed as capital gains for shareholders", "Promoters face an additional levy"],
             ["Losses", "Short-term losses set off against any gains; long-term against long-term", "Carry forward only if the return is filed on time"]])
         + call_box("tax on my Indian shares", ["Whether TDS deducted this year exceeds your actual tax",
                                                "Filing a belated or revised return by 31 December 2026 to recover it",
                                                "Treaty position for your country and credit in your home return",
                                                "Account set-up (NRE/PIS vs NRO) and repatriation",
                                                "Carrying forward losses and planning future sales"],
                    "your broker's capital gains statement, Form 26AS / AIS, country of residence and account type.")),
        ("/ Accounts, treaty and home-country tax", "What else changes for NRIs.",
         ul("<strong>Accounts:</strong> repatriable investing is done through NRE-linked accounts designated for portfolio investment; non-repatriable investing through NRO accounts; proceeds follow the source account's repatriation rules; see <a href=\"nre-nro-fcnr-account-tax-rules.html\">NRE, NRO and FCNR</a>.",
            "<strong>KYC from abroad:</strong> from 3 December 2026 intermediaries can complete KYC digitally for NRIs and OCIs in FATF-compliant countries; see <a href=\"nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html\">digital KYC from abroad</a>.",
            "<strong>Treaties:</strong> India generally keeps the right to tax gains on Indian shares; grandfathering for Singapore and Mauritius residents covers only shares bought before 1 April 2017; mutual fund units can be treated differently under some treaties; see <a href=\"nri-mutual-funds-india-tax.html\">NRI mutual funds</a> and <a href=\"india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html\">India-UAE treaty</a>.",
            "<strong>Home country:</strong> US, UK, Canadian and Australian residents report the gain at home and claim credit for Indian tax; Gulf residents pay no tax at home; see <a href=\"is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026.html\">how home countries tax Indian income</a>.",
            "<strong>Trading derivatives:</strong> futures and options profits are business income, taxed at slab rates, with audit thresholds to watch.")),
        ("/ Getting excess TDS back", "Before 31 December 2026.",
         ul("Download Form 26AS and AIS and match TDS with the broker's statement.",
            "File ITR-2 (ITR-3 if you trade derivatives) for FY 2025-26 as a belated or revised return by 31 December 2026, claiming treaty or slab benefits and set-offs.",
            "After 31 December only an updated return is possible, which cannot claim a refund.",
            "Keep a lower deduction certificate in mind for large planned sales.")
         + f'<p>Related: <a href="{NYE}.html">NRI year-end checklist</a> &middot; <a href="which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html">which ITR for NRIs</a> &middot; <a href="ltcg-12-5-percent-new-capital-gains-india-2026.html">capital gains rates 2026</a>.</p>'
         + sources("Income-tax Act, 1961 for FY 2025-26 (sections 111A, 112A, 115AD/195 withholding on non-residents, 70-74) as amended by the Finance (No. 2) Act, 2024 and the Finance Act, 2026 (buybacks); Income-tax Act, 2025 from FY 2026-27; India-Singapore and India-Mauritius protocols (2016-17 grandfathering); RBI rules on NRI portfolio investment; SEBI circular on digital KYC (4 November 2026).")),
    ],
    faqs=[("What is the capital gains tax for NRIs on Indian shares?", "Listed shares held over 12 months: 12.5% on gains above INR 1.25 lakh a year; held 12 months or less: 20%; plus surcharge and cess, the same rates as residents."),
          ("Is TDS deducted on an NRI's share sales?", "Yes. The broker deducts TDS on the capital gain for NRIs at the time of sale, which can exceed the final tax; file a return to claim the excess back."),
          ("Can NRIs use the basic exemption limit against share gains?", "No. Only residents can adjust the unused basic exemption against short-term and long-term gains taxed at special rates."),
          ("Do tax treaties exempt NRI share gains from Indian tax?", "Generally not; most treaties let India tax gains on Indian shares. Singapore and Mauritius grandfathering covers only shares bought before 1 April 2017."),
          ("How can an NRI get back excess TDS on share sales?", "File ITR-2 (or ITR-3 for derivatives) for the year; for FY 2025-26 a belated return is possible until 31 December 2026 and a revised return until 31 March 2027."),
        ("How are unlisted shares taxed for an NRI?", "Unlisted shares held for more than 24 months are long-term: 12.5% plus surcharge and cess, without indexation. Held for 24 months or less, the gain is short-term and taxed at slab rates. The buyer must deduct TDS under section 393 (old 195) on the gain, so the price, cost and holding period need to be documented before the sale - see our guide to TDS on buying shares from a non-resident."),
        ("How can an NRI reduce capital gains tax on shares legally?", "Set off short-term and long-term capital losses against gains in the same year, and carry forward unused losses for eight years - which needs the return filed by the due date. Long-term gains can qualify for section 54F if the net sale proceeds are invested in a residential house in India within the time limits. Check whether your country's treaty gives any relief (most let India tax gains on Indian shares), and file a return to recover TDS deducted above the final tax."),
          ("Can BQP file my return and recover TDS?", "Yes. " + C_NS)],
    related=[("nri-mutual-funds-india-tax.html", "NRI mutual funds tax"), (NYE + ".html", "NRI year-end checklist"),
             ("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "Which ITR for NRIs")],
    cta_h="Excess TDS on your Indian share sales?", cta_b=C_NS,
    keywords="NRI capital gains tax on shares, NRI long term capital gains tax on shares, NRI short term capital gains tax shares, NRI TDS on share sale refund, NRI LTCG 12.5 percent 1.25 lakh, NRI STCG 20 percent, NRI PIS account tax, NRI share trading tax India 2026",
    desc="NRI capital gains tax on Indian shares (2026): LTCG 12.5% above INR 1.25 lakh, STCG 20%, TDS by the broker, no basic exemption for NRIs, dividends and buybacks, treaty limits (Singapore/Mauritius pre-2017 grandfathering), home-country tax, refunds via belated/revised ITR by 31 December 2026.",
    howto={"name": "How an NRI handles tax on Indian share sales", "description": "From sale to refund.", "steps": [
        {"name": "Get statements", "text": "Broker capital gains statement, Form 26AS and AIS."},
        {"name": "Compute actual tax", "text": "12.5% above INR 1.25 lakh for long-term, 20% short-term, with set-offs."},
        {"name": "Check treaty and home country", "text": "Treaty relief rarely applies; claim credit at home."},
        {"name": "File the return", "text": "ITR-2 or ITR-3; belated or revised by 31 December 2026 for FY 2025-26."},
        {"name": "Repatriate correctly", "text": "Follow NRE/PIS or NRO rules for the proceeds."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DV complete:", len(PAGES))
