# -*- coding: utf-8 -*-
"""Batch CF (14 Nov 2026): demand-led pages (Google autocomplete seen in all seven target markets):
inherited property in India (rules, rights, sale, tax) and the India-Germany and India-Netherlands tax treaties.
Facts: no inheritance or estate tax in India; inheritance is not taxable income. Hindu Succession Act, 1956 (Class I
heirs share equally); daughters are coparceners by birth with equal rights (2005 amendment; Supreme Court, Vineeta
Sharma v Rakesh Sharma, 11 August 2020); Indian Succession Act, 1925 for Christians and Parsis; Muslim personal law.
Inherited property: holding period includes the previous owner's; cost is the previous owner's cost (fair market value
on 1 April 2001 may be used for assets acquired earlier); long-term gains at 12.5% without indexation; resident
individuals/HUFs may opt for 20% with indexation for land or buildings acquired before 23 July 2024; NRIs only 12.5%;
reinvestment reliefs (sections 54, 54EC, 54F, carried into the 2025 Act). NRIs may inherit any immovable property and
repatriate sale proceeds up to USD 1 million per financial year.
India-Germany DTAA: dividends, interest, royalties and fees for technical services each capped at 10%.
India-Netherlands DTAA: dividends, interest, royalties and FTS 10%; MFN protocol cannot lower rates without a
notification under the Act (Supreme Court, Nestle SA, 19 October 2023).
Sources: Income Tax Department withholding-rate chart; indialawoffices, calcguru, Taxmann, Trilegal, Business Today,
Outlook (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."
DATE = "2026-11-14"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, body, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">{body} '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')


def src(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not legal or tax advice for your situation.</p>'


C_INH = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with who passed away and when, whether there is a will, the heirs and where they live, and the property details. "
         "We reply the same working day with the steps, the tax on a sale and a fixed-scope quote; legal documents are prepared with your lawyer.")
C_NRI = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your country of residence, the Indian income and the years involved. "
         "We reply the same working day with the treaty position and a fixed-scope quote.")

INH = dict(
    slug="inherited-property-india-rules-rights-sale-tax-nri-resident-2026",
    title="Inherited Property in India (2026): Who Inherits, Documents, Selling It, Capital Gains Tax for Residents and NRIs",
    em="no inheritance tax, but the sale is taxed.",
    kicker=f"/ Inheritance &middot; Property &middot; Residents and NRIs &middot; Updated {DATE}",
    lead=("India has <strong>no inheritance or estate tax</strong>: receiving property from a parent or relative is not taxed. Tax arises only when the heir <strong>sells</strong>. "
          "The heir takes over the <strong>previous owner's purchase date and cost</strong> (fair market value on 1 April 2001 can be used for older property), so most inherited property is already long-term on day one. "
          "Long-term gains are taxed at <strong>12.5% without indexation</strong>; a resident individual or HUF may instead choose <strong>20% with indexation</strong> for land or buildings acquired before 23 July 2024, while NRIs pay 12.5%. "
          "Who inherits depends on the will, or without one, on personal law: under the Hindu Succession Act, daughters have the same rights as sons."),
    sections=[
        ("/ Who inherits", "Will first, then personal law.",
         table(["Situation", "Who inherits"], [
             ["There is a valid will", "The beneficiaries named in it; probate is compulsory for certain wills in Mumbai, Kolkata and Chennai and useful elsewhere when property is disputed"],
             ["No will: Hindu, Sikh, Jain or Buddhist", "Hindu Succession Act, 1956: Class I heirs (widow, sons, daughters, mother and others) share equally; daughters are coparceners by birth with equal rights (2005 amendment, confirmed by the Supreme Court in Vineeta Sharma, 11 August 2020)"],
             ["No will: Christian or Parsi", "Indian Succession Act, 1925"],
             ["No will: Muslim", "Muslim personal law"],
             ["Heir lives abroad (NRI or OCI)", "Can inherit any property in India, including agricultural land; see <a href=\"nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html\">NRIs and agricultural land</a>"]])),
        ("/ Documents to put the property in your name", "Before you can sell.",
         ul("Death certificate, and the will with probate where required, or a legal heir certificate (a succession certificate is used for bank balances, shares and other movable assets).",
            "Mutation of the land or municipal records and the housing society transfer into the heirs' names.",
            "If one heir is to keep the property, the others sign a registered <strong>release (relinquishment) deed</strong>; stamp duty depends on the state and is often concessional between family members.",
            "If the heirs split several properties, a registered <strong>partition deed</strong>.",
            "Heirs living abroad can sign through a power of attorney; see <a href=\"nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html\">selling Indian property from abroad</a>.")),
        ("/ Tax when you sell", "Previous owner's date and cost carry over.",
         table(["Point", "Rule"], [
             ["Holding period", "Includes the previous owner's holding; over 24 months is long-term"],
             ["Cost", "The previous owner's cost; for property acquired before 1 April 2001, fair market value on that date (a registered valuer's report helps)"],
             ["Rate: residents", "12.5% without indexation, or 20% with indexation for land or buildings acquired before 23 July 2024, whichever is lower; confirm how the date applies to your inheritance"],
             ["Rate: NRIs", "12.5% without indexation; the buyer deducts TDS, which a lower deduction certificate can reduce"],
             ["Saving the tax", "Reinvest in a residential house (section 54), capital gain bonds within six months (section 54EC) or, for other assets, section 54F, within the time limits"]])
         + box("Selling a parent's flat bought decades ago?", "The 1 April 2001 valuation and the indexation option for residents can cut the taxable gain sharply, so get the numbers before agreeing a price.",
               "Hi Durgesh, I want to sell a property I inherited in India. Can you work out the capital gains tax?")
         + '<p>Related: <a href="nri-inheritance-indian-property-tax-fema-2026.html">NRI inheritance of Indian property</a> &middot; <a href="inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html">inheriting while living abroad</a> &middot; <a href="nri-property-tds-ldc-calculator.html">NRI property TDS calculator</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating up to USD 1 million</a>.</p>'
         + src("Hindu Succession Act, 1956 and Hindu Succession (Amendment) Act, 2005; Vineeta Sharma v Rakesh Sharma (Supreme Court, 11 August 2020); Indian Succession Act, 1925; Income-tax Act, 1961 sections 49, 55, 112, 54, 54EC and 54F (carried into the Income-tax Act, 2025); Finance (No. 2) Act, 2024 (rates from 23 July 2024); FEMA Non-debt Instruments Rules, 2019. Secondary summaries checked 14 November 2026: Business Today, Outlook, Angel One.")),
    ],
    faqs=[("Is there inheritance tax in India?", "No. India has no inheritance or estate tax, and property received by inheritance is not taxed as income. Tax arises only when the heir sells."),
          ("How is capital gains tax worked out on inherited property?", "The heir uses the previous owner's purchase cost and holding period (fair market value on 1 April 2001 for older property). Long-term gains are taxed at 12.5% without indexation; residents may choose 20% with indexation for land or buildings acquired before 23 July 2024."),
          ("Do daughters have equal rights in inherited property?", "Yes, for Hindus, Sikhs, Jains and Buddhists. Since the 2005 amendment to the Hindu Succession Act, daughters are coparceners by birth with the same rights as sons, as confirmed by the Supreme Court in 2020."),
          ("Can an NRI inherit and sell property in India?", "Yes. An NRI or OCI can inherit any property in India, sell it (agricultural land only to a resident Indian citizen) and repatriate up to USD 1 million per financial year."),
          ("What documents do I need to sell inherited property?", "Death certificate, will and probate or legal heir certificate, mutation in the records, and release or partition deeds if the heirs are dividing the property."),
          ("Can I avoid tax on selling inherited property?", "You can reduce or defer it by reinvesting the gain in a residential house, in capital gain bonds within six months, or under section 54F, within the time limits."),
          ("Can BQP help?", "Yes. " + C_INH)],
    related=[("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of Indian property"), ("nri-property-tds-ldc-calculator.html", "NRI property TDS calculator"),
             ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "NRIs and agricultural land")],
    cta_h="Inherited property in India?", cta_b=C_INH,
    keywords="inherited property India, inherited property rules India, inherited property sale laws India, inherited property rights India daughters, capital gains on inherited property India, inheritance tax India, NRI inherited property sale, legal heir certificate property sale",
    desc="Inherited property in India in 2026: no inheritance tax; who inherits (will, Hindu Succession Act with equal rights for daughters, other personal laws); documents (probate, legal heir certificate, mutation, release deed); capital gains with previous owner's cost and date, 12.5% or 20% with indexation, NRIs, reinvestment reliefs.",
    howto={"name": "How to sell inherited property in India", "description": "Steps for resident and NRI heirs.", "steps": [
        {"name": "Establish who inherits", "text": "Check for a will and probate; otherwise apply the heirs' personal law and obtain a legal heir certificate."},
        {"name": "Transfer the title", "text": "Get the records mutated and sign release or partition deeds among heirs if needed."},
        {"name": "Work out the tax", "text": "Use the previous owner's cost (or 1 April 2001 value) and date; compare 12.5% with 20% with indexation if resident."},
        {"name": "Sell and reinvest", "text": "Obtain a lower TDS certificate if NRI, then reinvest under section 54 or 54EC within the time limits."}]})


def treaty(country, slug, rows, notes, extra_faqs, credit, related_send, special=""):
    return dict(
        slug=slug,
        title=f"India-{country} Tax Treaty (DTAA) for NRIs and Companies in {country} (2026): 10% Caps on Dividends, Interest, Royalties and Technical Fees",
        em=f"a flat 10% cap, with the right paperwork.",
        kicker=f"/ NRI &middot; {country} &middot; DTAA &middot; Updated {DATE}",
        lead=(f"Under the India-{country} tax treaty, India's tax on <strong>dividends, interest, royalties and fees for technical services</strong> paid to a resident of {country} is capped at <strong>10%</strong>, well below the Indian rates for non-residents (20% on dividends, royalties and technical fees, 30% on NRO interest). "
              f"The cap applies only if the payer receives a <strong>tax residency certificate from {country}</strong> and <strong>Form 10F (now Form 41)</strong>; rent and gains on Indian property stay taxable in India, and {country} gives relief for the Indian tax." + special),
        sections=[
            ("/ Treaty caps vs Indian rates", "The lower one applies.",
             table(["Income from India", f"India-{country} treaty cap", "Indian rate for non-residents (before surcharge and cess)"], rows)
             + box(f"Indian company paying a {country} parent or vendor?", f"Collect the {country} TRC and Form 41 before the payment, deduct at 10% and certify the remittance on Forms 145/146; without them the full Indian rate applies.",
                   f"Hi Durgesh, we need to pay a company in {country} from India. Can you confirm the treaty withholding rate and documents?")),
            ("/ How to claim and avoid double tax", "Step by step.",
             ul(f"Obtain a tax residency certificate from the {country} tax authority for the year.",
                "File Form 10F (Form 41 under the Income-tax Rules, 2026) on the Indian e-filing portal; a PAN is needed.",
                "Give both to the Indian payer before payment, or claim the treaty rate and refund in an Indian return.",
                f"Declare the income in {country} and claim {credit} for the Indian tax, within the treaty cap.",
                *notes)
             + f'<p>Related: <a href="what-is-dtaa.html">what a DTAA is</a> &middot; <a href="nri-dtaa-claim-practical-trc-form-10f.html">claiming DTAA with TRC and Form 10F</a> &middot; <a href="{related_send}">sending money between Europe and India</a> &middot; <a href="india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html">India-Canada DTAA</a>.</p>'
             + src(f"India-{country} Double Taxation Avoidance Agreement and protocol; Income Tax Department chart of withholding rates under the Act and tax treaties; Income-tax Act, 2025 and Income-tax Rules, 2026 (Forms 41, 145, 146). Secondary summaries checked 14 November 2026.")),
        ],
        faqs=[(f"What is the India-{country} DTAA rate on dividends?", "10%, compared with 20% under Indian law for non-residents, provided the TRC and Form 10F (Form 41) are given."),
              (f"What is the India-{country} DTAA rate on royalties and technical fees?", "10% each, compared with 20% under Indian law."),
              (f"What TDS applies on NRO interest for an NRI in {country}?", "30% plus surcharge and cess by default; 10% under the treaty once the bank has your TRC, Form 10F (Form 41) and PAN."),
              *extra_faqs,
              ("Can BQP handle the Indian side?", "Yes. " + C_NRI)],
        related=[("nri-dtaa-claim-practical-trc-form-10f.html", "Claim DTAA: TRC and Form 10F"), (related_send, "Money between Europe and India"),
                 ("what-is-dtaa.html", "What is a DTAA")],
        cta_h=f"Income from India while resident in {country}?", cta_b=C_NRI,
        keywords=f"DTAA India and {country}, India {country} tax treaty, India {country} DTAA rates, India {country} DTAA dividend interest royalty 10%, NRI {country} India tax, {country} company India withholding tax, India {country} double taxation",
        desc=f"India-{country} DTAA in 2026: 10% caps on dividends, interest, royalties and fees for technical services vs Indian rates, TRC and Form 10F (Form 41), withholding by Indian payers, and relief in {country}.",
        howto={"name": f"How to claim the India-{country} treaty rate", "description": "Steps for individuals and companies.", "steps": [
            {"name": "Get a TRC", "text": f"Obtain a tax residency certificate from {country}."},
            {"name": "File Form 41", "text": "Submit Form 10F (Form 41) on the Indian e-filing portal with a PAN."},
            {"name": "Give documents to the payer", "text": "The Indian payer deducts at 10% and certifies the remittance on Forms 145/146."},
            {"name": "Claim relief at home", "text": f"Declare the income in {country} and claim relief for the Indian tax."}]})


ROWS = [["Dividends", "10%", "20%"], ["Interest (NRO deposits, loans)", "10%", "30% on NRO interest; 20% on some foreign-currency loans"],
        ["Royalties", "10%", "20%"], ["Fees for technical services", "10%", "20%"], ["Rent and gains on Indian property", "Taxable in India", "Slab rates for rent; 12.5% on long-term property gains"]]

GERMANY = treaty("Germany", "india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026", ROWS,
                 ["German residents declare foreign income in the German return (Anlage AUS) and claim credit for Indian tax."],
                 [("Does the India-Germany treaty cover technical fees?", "Yes. Fees for technical services are capped at 10%, which matters for Indian companies paying German engineering and software firms.")],
                 "a foreign tax credit", "send-money-europe-to-india-germany-netherlands-ireland-nri-2026.html")
NETHERLANDS = treaty("Netherlands", "india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026", ROWS,
                     ["The Netherlands taxes residents' savings and investments, including Indian deposits and shares, under Box 3, separately from Indian tax.",
                      "Dutch holding structures face the treaty's anti-abuse rules and the principal purpose test; see <a href=\"netherlands-bv-indian-stepdown-treaty-shopping-ca.html\">Netherlands BV holding an Indian company</a>."],
                     [("Can the MFN clause reduce India-Netherlands rates below 10%?", "Not automatically. In Nestle SA (19 October 2023) the Supreme Court held that a lower rate under the MFN clause needs a notification under the Indian tax law; without it, 10% applies.")],
                     "relief", "send-money-europe-to-india-germany-netherlands-ireland-nri-2026.html",
                     special=" The protocol's most-favoured-nation clause does not lower these rates automatically: the Supreme Court held in <strong>Nestle SA (19 October 2023)</strong> that a notification is needed first.")

for p in [INH, GERMANY, NETHERLANDS]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CF complete")
