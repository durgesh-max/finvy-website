# -*- coding: utf-8 -*-
"""Batch DT (20 Nov 2026): NRI visiting India in December 2026 - customs (Baggage Rules 2026), gold, cash, gifts to
family, property and banking tasks, residency day count, tax deadlines. Call-first page.
Facts (checked 20 Nov 2026): Baggage Rules, 2026 in force from 2 February 2026 - general duty-free allowance INR 75,000
(was INR 50,000) for residents and Indian-origin tourists arriving by air or sea; gold jewellery by weight - 40 g for
women, 20 g for others, for passengers resident abroad for over a year, ornaments only (coins and bars excluded),
excess declared with duty (Angel One, Khaleej Times, Taxscan, Gulf News); currency - declare foreign currency notes
above USD 5,000 or total foreign exchange above USD 10,000 (Currency Declaration Form); no cap on bringing foreign
exchange; Indian rupee rule worded differently across sources (INR 25,000) - hedged; ATITHI app for advance
declaration. Tax: gifts from relatives tax-free, gifts from non-relatives above INR 50,000 taxable to the recipient;
residency 182 days / 120 days with Indian income above INR 15 lakh; belated ITR 31 Dec 2026; advance tax 15 Dec."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
TRIP = "nri-visiting-india-december-2026-baggage-rules-gold-cash-gifts-property-tax-checklist"
NYE = "nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency"

C_TRIP = contact("your country, travel dates, and what you want to get done in India (property sale, bank or PAN work, gifts, investments)")
PAGES = [dict(
    slug=TRIP,
    title="Visiting India in December 2026 as an NRI: Baggage Rules 2026 (Gold and Duty-Free Limits), Cash Declaration, Gifts to Family, Property Work and Tax Checklist",
    em="what to carry, what to declare, and what to get done while you are in India.",
    kicker="/ NRIs &middot; Travel &middot; Customs &middot; Tax &middot; Updated 2026-11-20",
    lead=("NRIs flying to India for the holidays or a family wedding have new rules this year. Under the <strong>Baggage Rules, 2026</strong> (in force from 2 February 2026) the general duty-free allowance is <strong>INR 75,000</strong>. If you have lived abroad for over a year, you can bring <strong>gold jewellery duty-free by weight: 40 grams for women and 20 grams for others</strong>. Coins and bars are not covered, and anything above the limit must be declared and taxed. "
          "Declare <strong>foreign currency notes above USD 5,000</strong>, or total foreign exchange above <strong>USD 10,000</strong>, on the Currency Declaration Form; you can file in advance on the ATITHI app. "
          "Gifts to <strong>relatives</strong> are tax-free in their hands; gifts from non-relatives above INR 50,000 are taxable. "
          "Use the trip to finish paperwork that needs you in person: a property sale or power of attorney, bank and PAN updates, and NRO-to-abroad remittances. Count your days, because a long stay can change your <strong>residential status</strong>."),
    sections=[
        ("/ Customs and cash", "Before you board.",
         table(["Item", "Rule (Baggage Rules, 2026 / FEMA)", "Tip"], [
             ["General duty-free allowance", "INR 75,000 for residents and Indian-origin tourists arriving by air or sea", "Electronics and gifts above the allowance attract duty"],
             ["Gold jewellery", "40 g (women), 20 g (others) for passengers resident abroad over a year; ornaments only", "Keep purchase bills; declare and pay duty on any excess"],
             ["Gold coins and bars", "Not within the jewellery allowance", "Declare; duty applies"],
             ["Foreign currency", "No limit on bringing it in; declare notes above USD 5,000 or total above USD 10,000", "File the declaration on arrival or via the ATITHI app"],
             ["Indian rupees", "A INR 25,000 threshold applies; sources word it differently", "Check the current customs notice before carrying rupee cash"]])
         + call_box("my India visit (tax, property and banking)", ["What paperwork to finish while you are in India",
                                                                    "Property sale: lower deduction certificate, power of attorney and repatriation",
                                                                    "Gifts to family and their tax treatment",
                                                                    "Your residency status given the length of your stay",
                                                                    "Year-end filings: refunds, advance tax and FAST-DS"],
                    "your travel dates, Indian assets (property, bank accounts, investments) and what you want to complete in India.")),
        ("/ Gifts, property and banking", "Make the trip count.",
         ul("<strong>Gifts to family:</strong> cash, jewellery or transfers to relatives (parents, siblings, spouse, children and their spouses, and others defined in the law) are not taxed in their hands; gifts from non-relatives above INR 50,000 in a year are; see <a href=\"nri-gift-indian-relatives-section-56-fema-2026.html\">NRI gifts to relatives</a>.",
            "<strong>Selling property:</strong> apply for a lower deduction certificate before signing, or the buyer deducts TDS on the full price; see <a href=\"nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html\">selling property from abroad</a> and <a href=\"nri-property-tds-ldc-calculator.html\">TDS and LDC calculator</a>.",
            "<strong>Buying property:</strong> pay from NRE or by remittance to keep the price repatriable; see <a href=\"can-nri-buy-property-in-india-residential-commercial-fema-payment-home-loan-tds-2026.html\">can an NRI buy property</a>.",
            "<strong>Power of attorney:</strong> signing in India avoids apostille delays later.",
            "<strong>Banking:</strong> update KYC, convert savings accounts to NRO if not done, and arrange NRO repatriation with Forms 15CA/15CB; see <a href=\"repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html\">repatriating money</a>.")),
        ("/ Tax deadlines around your trip", "December is busy.",
         ul("<strong>15 December 2026:</strong> advance tax if your Indian tax after TDS exceeds INR 10,000.",
            "<strong>31 December 2026:</strong> belated or revised return for FY 2025-26 to claim TDS refunds; FAST-DS 2026 for returning NRIs with unreported foreign assets.",
            "<strong>Residency:</strong> 182 days in India in the financial year (or 120 days if Indian income exceeds INR 15 lakh and the 365-day test is met) makes you resident; see <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.")
         + f'<p>Related: <a href="{NYE}.html">NRI year-end tax checklist</a> &middot; <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">deadline desk</a> &middot; <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR</a>.</p>'
         + sources("Baggage Rules, 2026 (in force 2 February 2026); Foreign Exchange Management (Export and Import of Currency) Regulations as amended; Income-tax Act provisions on gifts (section 56(2)(x) of the 1961 Act, carried into the 2025 Act) and residency. Reports checked 20 November 2026: Angel One, Khaleej Times, Taxscan, Gulf News, Wego, Bangalore Customs traveller guide. Customs rules are summarised for convenience; check the CBIC notice before travel.")),
    ],
    faqs=[("How much gold jewellery can an NRI bring to India duty-free in 2026?", "Under the Baggage Rules, 2026, passengers resident abroad for over a year can bring gold jewellery up to 40 grams (women) or 20 grams (others) duty-free; coins and bars are not covered and excess must be declared with duty."),
          ("What is the duty-free allowance for NRIs flying to India?", "INR 75,000 for residents and Indian-origin tourists arriving by air or sea, raised from INR 50,000 by the Baggage Rules, 2026."),
          ("How much foreign currency can I bring into India?", "There is no limit, but foreign currency notes above USD 5,000 or total foreign exchange above USD 10,000 must be declared on the Currency Declaration Form."),
          ("Are gifts from an NRI to family in India taxable?", "No, gifts to relatives are not taxed in their hands; gifts from non-relatives above INR 50,000 in a year are taxable to the recipient."),
          ("Can a December visit make me resident in India?", "Only if your total days in India in the financial year reach 182, or 120 for Indian citizens and PIOs with Indian income above INR 15 lakh who meet the 365-day test."),
          ("Can BQP help with property, banking and tax while I am in India?", "Yes. " + C_TRIP)],
    related=[(NYE + ".html", "NRI year-end tax checklist"), ("nri-gift-indian-relatives-section-56-fema-2026.html", "NRI gifts to relatives"),
             ("nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html", "Selling property from abroad")],
    cta_h="Coming to India this December?", cta_b=C_TRIP,
    keywords="NRI baggage rules 2026, how much gold NRI can bring to India 2026, duty free allowance India 75000, gold jewellery 40 grams women 20 grams men, currency declaration India USD 5000 10000, NRI visiting India December tax checklist, NRI gift to parents tax",
    desc="NRIs visiting India in December 2026: Baggage Rules 2026 (INR 75,000 duty-free; gold jewellery 40 g women / 20 g others; coins and bars excluded), currency declaration above USD 5,000 / 10,000, gifts to relatives, property and banking tasks, residency day count, 15 and 31 December deadlines.",
    howto={"name": "How an NRI prepares for an India visit in December 2026", "description": "Customs, tax and paperwork.", "steps": [
        {"name": "Check customs limits", "text": "INR 75,000 general allowance; gold jewellery 40 g / 20 g; declare currency above the thresholds."},
        {"name": "List in-person tasks", "text": "Property sale or POA, bank KYC, NRO repatriation, PAN updates."},
        {"name": "Plan gifts", "text": "Gifts to relatives are tax-free; document larger gifts."},
        {"name": "Count your days", "text": "Keep the stay within residency limits unless you plan to become resident."},
        {"name": "Meet tax deadlines", "text": "Advance tax by 15 December; belated return and FAST-DS by 31 December."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DT complete:", len(PAGES))
