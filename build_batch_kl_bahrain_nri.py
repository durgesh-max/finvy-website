# -*- coding: utf-8 -*-
"""Batch KL (28 Nov 2026): NRIs living in Bahrain - how India taxes their Indian income when there is no India-Bahrain DTAA.
Demand: DTAA coverage check 28 Nov 2026 - the site had treaty pages for Saudi Arabia, Qatar, Kuwait, Oman, Malaysia, Ireland,
Switzerland and Hong Kong but nothing for Bahrain, a large Indian diaspora market. User steer 26 Nov 2026: more call bookings /
WhatsApp enquiries.
Facts (verified 28 Nov 2026): India and Bahrain have a Tax Information Exchange Agreement signed on 31 May 2012 and in force from
11 April 2013 (incometaxindia.gov.in), not a comprehensive double taxation agreement; Bahrain levies no personal income tax;
Indian income of a non-resident is taxed at Indian domestic rates with TDS at the non-resident rate (31.2% on NRO interest in
most cases per the site's NRE/NRO page); deemed residency under section 6(1A) for an Indian citizen with Indian income above
INR 15 lakh who is not liable to tax in any country - deemed residents are RNOR; the CBDT clarified in 2020 that the rule does
not tax income earned outside India by Indian citizens working abroad. No fees, no office claims, no statistics, no portal
menu paths, never ask for passwords."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "nri-in-bahrain-indian-tax-no-dtaa-tiea-nro-tds-deemed-resident-refund-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your residence in Bahrain and how long you have "
     "lived there, your Indian income (NRO interest, rent, shares, mutual funds, property sales) and any TDS already deducted. "
     "Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="NRI in Bahrain: How India Taxes Your Indian Income Without a DTAA (2026) - NRO TDS, Refunds, Deemed Residency and the TIEA",
    em="no treaty, so plan the Indian side.",
    kicker="/ Indians living in Bahrain &middot; NRO interest, rent, shares, mutual funds, property &middot; Updated 2026-11-28",
    lead=("<strong>India and Bahrain have no double taxation agreement - only a Tax Information Exchange Agreement, in force since April 2013. "
          "So an NRI in Bahrain gets no treaty rate on Indian income: TDS is deducted at the full non-resident rate, and the excess comes back only through an Indian income tax return.</strong> "
          "Bahrain does not tax your salary, so there is usually no double tax to relieve - the work is on the Indian side: refunds, residency and reporting."),
    sections=[
        ("/ What the absence of a DTAA means", "Indian rates, no treaty relief.",
         table(["Item", "Position for an NRI living in Bahrain"], [
             ["Agreement", "Tax Information Exchange Agreement only (signed 31 May 2012, in force 11 April 2013); no comprehensive DTAA"],
             ["NRO interest", "TDS at the full non-resident rate (31.2% in most cases), with no treaty cap"],
             ["Rent from Indian property", "Tenant deducts TDS at the non-resident rate; a lower deduction certificate can cut it"],
             ["Shares and mutual funds", "Capital gains taxed in India at Indian rates; no treaty exemption to claim"],
             ["NRE / FCNR interest", "Tax-free in India while you are non-resident, as for every NRI"],
             ["Tax residency certificate", "Has no treaty use for India; proof of residence still helps show NRI status"]])
         + ul("<strong>Refunds:</strong> TDS on NRO interest or rent is often more than the tax actually due once slab rates and deductions apply; the excess is refunded only when you file the Indian return.",
              "<strong>Information exchange:</strong> the TIEA lets the two tax authorities exchange information on request, so income in India should be reported correctly.",
              "<strong>FEMA is unchanged:</strong> NRE, NRO and FCNR accounts, repatriation limits and property rules are the same as for any NRI.")),
        ("/ Deemed residency: the INR 15 lakh rule", "Why Bahrain residents should check it.",
         ul("<strong>The rule:</strong> an Indian citizen whose Indian income (other than foreign-source income) is above INR 15 lakh in a year, and who is not liable to tax in any country, is deemed resident in India.",
            "<strong>Why it matters in Bahrain:</strong> because Bahrain has no personal income tax, NRIs with large Indian income - rent, interest, gains - should check whether this applies.",
            "<strong>What it changes:</strong> a deemed resident is treated as resident but not ordinarily resident (RNOR), so Indian income stays taxable; the CBDT clarified in 2020 that salary earned abroad by Indian citizens working there is not taxed because of this rule.",
            "<strong>Below the threshold, or not an Indian citizen (for example an OCI cardholder):</strong> the rule does not apply.")),
        ("/ How to handle it", "Each year.",
         ul("<strong>Keep your day count:</strong> passport stamps or travel history for the 182-day and 120-day tests.",
            "<strong>Route income correctly:</strong> rent and Indian income to the NRO account; NRE for money brought from Bahrain.",
            "<strong>File the Indian return</strong> (usually ITR-2) when there is Indian income or TDS to recover, by the due date or as a belated return by 31 December.",
            "<strong>Before selling property:</strong> apply for a lower TDS certificate so the buyer deducts on the real gain, not the whole price.")
         + call_box("NRI tax for residents of Bahrain", ["Residential status and the deemed-residency check",
                                                         "NRO interest and rent TDS and refunds",
                                                         "Capital gains on Indian shares, funds and property",
                                                         "Repatriation within FEMA limits",
                                                         "Indian return filing"],
                    "Years in Bahrain, Indian income and TDS (Form 26AS / AIS), bank accounts and any planned property sale.")
         + sources("India-Bahrain Tax Information Exchange Agreement (signed 31 May 2012, in force 11 April 2013), incometaxindia.gov.in; Income-tax Act, 2025 and Income-tax Rules, 2026 on residential status, deemed residency and TDS on payments to non-residents; CBDT clarification of 2020 on deemed residency; FEMA rules for NRE / NRO accounts; site NRE / NRO, deemed-residency and Gulf pages.")),
    ],
    faqs=[("Is there a DTAA between India and Bahrain?", "No. India and Bahrain have only a Tax Information Exchange Agreement, signed on 31 May 2012 and in force from 11 April 2013, under which the tax authorities exchange information on request. There is no comprehensive double taxation agreement, so Indian income of an NRI in Bahrain is taxed at Indian domestic rates."),
          ("How much TDS is deducted on NRO interest for an NRI in Bahrain?", "The full non-resident rate - 31.2% in most cases - because there is no treaty rate to apply. If your actual tax is lower, the excess is refunded when you file an Indian income tax return."),
          ("Is my Bahrain salary taxed in India?", "Not while you are non-resident. Even if the deemed-residency rule applies because your Indian income is above INR 15 lakh, the CBDT has clarified that salary earned abroad by Indian citizens working there is not taxed in India because of that rule."),
          ("Do I need a tax residency certificate from Bahrain?", "Not for treaty relief, because there is no treaty. Proof that you live in Bahrain, together with your day count, still helps show that you are a non-resident for Indian tax."),
          ("Are my Indian mutual fund gains taxable if I live in Bahrain?", "Yes. Without a treaty, capital gains on Indian shares and mutual funds are taxed in India at Indian rates, and the fund house or broker deducts TDS on redemption. Any excess TDS is refunded through the Indian return."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with how long you have lived in Bahrain, your Indian income (NRO interest, rent, shares, mutual funds, property sales), your Form 26AS / AIS and any planned property sale. Or book a call directly.")],
    related=[("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for clients in the UAE and Gulf"),
             ("india-kuwait-dtaa-nri-tax-treaty-rates-10-percent-trc-deemed-resident-nro-2026.html", "India-Kuwait DTAA for NRIs"),
             ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed residency: the INR 15 lakh rule"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules")],
    cta_h="Living in Bahrain with income in India?", cta_b=C,
    keywords="india bahrain dtaa, nri in bahrain tax india, bahrain nri income tax, india bahrain tax treaty, nro tds bahrain, bahrain nri itr, deemed resident bahrain",
    desc="NRI in Bahrain: India and Bahrain have no DTAA, only a TIEA in force since April 2013. NRO interest TDS at the full non-resident rate, refunds through the Indian return, capital gains at Indian rates, and the INR 15 lakh deemed-residency check.",
    howto={"name": "How an NRI in Bahrain handles Indian tax", "description": "Each year.", "steps": [
        {"name": "Check residential status", "text": "Day count and the INR 15 lakh deemed-residency test."},
        {"name": "Route income correctly", "text": "Rent and Indian income to NRO; money from Bahrain to NRE."},
        {"name": "Reconcile TDS", "text": "Match Form 26AS / AIS with interest, rent and gains."},
        {"name": "File the Indian return", "text": "Claim the excess TDS as a refund."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KL complete")
