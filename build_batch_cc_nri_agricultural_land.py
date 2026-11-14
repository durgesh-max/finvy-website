# -*- coding: utf-8 -*-
"""Batch CC (14 Nov 2026): NRIs and OCI cardholders and agricultural land, farmhouses and plantations in India.
FEMA (Non-debt Instruments) Rules, 2019, rule 24 and RBI Master Direction / FAQ on immovable property:
- NRI/OCI may purchase immovable property other than agricultural land, farm house or plantation property (24(a));
  cannot acquire such property by purchase or by gift.
- May acquire any immovable property, including agricultural land, by inheritance from a person resident in India, or
  from a person resident outside India who acquired it under the foreign exchange law in force at the time.
- May transfer any immovable property to a person resident in India (24(d)); transfer to an NRI/OCI only of property
  other than agricultural land, plantation property or farmhouse.
- State land laws can add conditions on who may own agricultural land.
Income tax: agricultural land outside municipal limits and beyond 2 km (population 10,000-1 lakh), 6 km (1-10 lakh) or
8 km (over 10 lakh), measured aerially from the municipality or cantonment, is not a capital asset (1961 Act s.2(14)(iii),
carried into the Income-tax Act, 2025); urban agricultural land is a capital asset: long-term (over 24 months) at 12.5%
without indexation for NRIs; section 54B reinvestment relief where used for agriculture for 2 years; buyer deducts TDS
on payments to an NRI unless a lower/nil certificate is obtained. Agricultural income is exempt from income tax.
Repatriation of sale proceeds of inherited property: up to USD 1 million per financial year from the NRO account with
CA certificate. Sources: RBI FAQ on purchase of immovable property; RBI Master Direction; Upstox, 1acre.in (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the village and taluka, the nearest town, how you got the land (inheritance or otherwise) and whether you want to keep, lease or sell it. "
           "We reply the same working day with the FEMA and tax position and a fixed-scope quote.")
SLUG = "nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Rural or urban decides the tax.</p>'
       f'<p style="margin:0">If the land is outside municipal limits and beyond the 2, 6 or 8 km band, it is not a capital asset and the gain is not taxed at all. Get this checked before the buyer deducts TDS on the full price. '
       f'<a href="{wa("Hi Durgesh, I am an NRI and I inherited agricultural land in India. Can you check whether the sale is taxable and how to repatriate the money?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="NRIs, OCI Cardholders and Agricultural Land in India (2026): Buying, Inheriting, Selling, Tax and Repatriation",
    em="inherit yes, buy no, sell only to a resident Indian.",
    kicker="/ NRI &middot; OCI &middot; FEMA &middot; Property tax &middot; Updated 2026-11-14",
    lead=("An NRI or OCI cardholder <strong>cannot buy or receive as a gift</strong> agricultural land, a farmhouse or plantation property in India, but <strong>can inherit it</strong>. "
          "Inherited farmland can be sold or gifted <strong>only to a person resident in India who is an Indian citizen</strong>, not to another NRI or OCI (FEMA Non-debt Instruments Rules, 2019, rule 24). "
          "For tax, <strong>rural</strong> agricultural land (outside municipal limits and beyond 2, 6 or 8 km depending on the town's population) is not a capital asset, so its sale is not taxed; <strong>urban</strong> agricultural land is taxed like other land, at 12.5% on long-term gains for NRIs. "
          "Sale proceeds of inherited property can be repatriated up to USD 1 million a financial year from the NRO account."),
    sections=[
        ("/ What NRIs and OCIs can and cannot do", "The FEMA rules in one table.",
         table(["Transaction", "NRI / OCI allowed?", "Rule"], [
             ["Buy agricultural land, farmhouse or plantation", "No", "Rule 24(a) permits purchase of immovable property other than these"],
             ["Receive it as a gift", "No", "Gifts to NRIs/OCIs exclude agricultural land, farmhouses and plantations"],
             ["Inherit it", "Yes", "From a person resident in India, or from a non-resident who acquired it lawfully"],
             ["Sell or gift it to a resident Indian citizen", "Yes", "Rule 24(d): transfer to a person resident in India"],
             ["Sell or gift it to another NRI or OCI", "No", "Transfers to NRIs/OCIs exclude these properties"],
             ["Buy a flat, house, office or plot (non-agricultural)", "Yes", "Rule 24(a); no limit on number"]])
         + "<p>State land laws can add their own conditions on who may hold agricultural land, so check the state where the land is before any transfer.</p>"),
        ("/ Tax when you sell", "Rural is outside the capital gains net.",
         table(["Land", "How it is taxed"], [
             ["Rural agricultural land: outside municipal or cantonment limits and beyond 2 km (town population 10,000 to 1 lakh), 6 km (1 lakh to 10 lakh) or 8 km (over 10 lakh), measured aerially", "Not a capital asset: no capital gains tax"],
             ["Urban agricultural land (inside those limits)", "Capital asset: long-term after 24 months, taxed at 12.5% without indexation for NRIs; short-term gains at slab rates"],
             ["Urban land used for agriculture by you or your parents for 2 years before sale", "Section 54B relief if the gain is reinvested in other agricultural land within the time allowed"]])
         + BOX
         + ul("Population is taken from the last published census, and every nearby municipality counts, including newly notified ones.",
              "A buyer paying an NRI must deduct tax unless a lower or nil deduction certificate is obtained; for rural land with no taxable gain, apply before the sale. Try the <a href=\"nri-property-tds-ldc-calculator.html\">NRI property TDS calculator</a>.",
              "Income from farming or leasing the land (agricultural income) is exempt from income tax.")),
        ("/ Inherited the land? The order of steps", "From succession to repatriation.",
         ul("<strong>Establish title:</strong> will and probate where required, or legal heir or succession documents, then mutation of the land records in your name.",
            "<strong>Decide:</strong> keep (and lease through a local arrangement), or sell or gift to a resident Indian citizen.",
            "<strong>Before selling:</strong> confirm rural or urban status and get a lower or nil TDS certificate if needed.",
            "<strong>Repatriate:</strong> sale proceeds go to your NRO account; up to USD 1 million per financial year can be sent abroad with a CA certificate and bank forms (Forms 145/146, formerly 15CA/15CB), with proof of inheritance.",
            "<strong>Report abroad:</strong> declare the sale in your country of residence as its rules require.")
         + '<p>Related: <a href="nri-inheritance-indian-property-tax-fema-2026.html">NRI inheritance of Indian property</a> &middot; <a href="inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html">inheriting from India while living abroad</a> &middot; <a href="nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html">selling from abroad with a power of attorney</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating USD 1 million</a>.</p>'
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Non-debt Instruments) Rules, 2019, rule 24; RBI FAQ on purchase of immovable property by NRIs and OCIs; RBI Master Direction on acquisition and transfer of immovable property; Income-tax Act, 1961, section 2(14)(iii) and section 54B, carried into the Income-tax Act, 2025. Secondary summaries checked 14 November 2026: Upstox, 1acre.in. <em>{UPDATED}</em> General information, not advice for your situation; state land laws also apply.</p>'),
    ],
    faqs=[("Can an NRI buy agricultural land in India?", "No. Under rule 24 of the FEMA Non-debt Instruments Rules, 2019, NRIs and OCI cardholders can buy any immovable property except agricultural land, farmhouses and plantation property."),
          ("Can an NRI or OCI inherit agricultural land?", "Yes. They can inherit any immovable property, including agricultural land, from a person resident in India, or from a non-resident who acquired it lawfully."),
          ("Who can an NRI sell inherited agricultural land to?", "Only to a person resident in India who is an Indian citizen. Agricultural land, farmhouses and plantations cannot be sold or gifted to another NRI or OCI."),
          ("Can my parents gift me agricultural land if I am an NRI?", "No. Agricultural land, farmhouses and plantation property cannot be acquired by an NRI or OCI by gift; inheritance is the only route."),
          ("Is the sale of agricultural land taxable for an NRI?", "Rural agricultural land is not a capital asset, so there is no capital gains tax. Urban agricultural land (within municipal limits or the 2, 6 or 8 km band) is taxed at 12.5% on long-term gains for NRIs, with section 54B relief possible on reinvestment in agricultural land."),
          ("How much of the sale money can I take abroad?", "Up to USD 1 million per financial year from the NRO account, with a CA certificate and bank forms, and proof of inheritance."),
          ("Can BQP handle the sale and repatriation?", "Yes. " + CONTACT)],
    related=[("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of Indian property"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate up to USD 1 million"),
             ("nri-property-tds-ldc-calculator.html", "NRI property TDS calculator")],
    cta_h="Inherited farmland in India?", cta_b=CONTACT,
    keywords="can NRI buy agricultural land in India, OCI agricultural land, NRI inherited agricultural land sell, NRI farmhouse plantation FEMA, agricultural land capital gains NRI, rural agricultural land not capital asset 2 km 6 km 8 km, NRI sell agricultural land to whom, repatriate agricultural land sale proceeds",
    desc="NRIs and OCI cardholders and agricultural land in India in 2026: cannot buy or receive by gift, can inherit, can sell only to a resident Indian citizen (FEMA NDI Rules rule 24); rural land not taxed, urban land at 12.5%; TDS, section 54B and USD 1 million repatriation.",
    howto={"name": "How an NRI sells inherited agricultural land in India", "description": "Steps from inheritance to repatriation.", "steps": [
        {"name": "Establish title", "text": "Obtain probate or legal heir documents and get the land records mutated in your name."},
        {"name": "Check rural or urban status", "text": "Measure the aerial distance from the nearest municipality and check its census population against the 2, 6 and 8 km bands."},
        {"name": "Sell to an eligible buyer", "text": "Sell only to a person resident in India who is an Indian citizen; obtain a lower or nil TDS certificate if the gain is low or not taxable."},
        {"name": "Repatriate", "text": "Receive the proceeds in your NRO account and remit up to USD 1 million per financial year with a CA certificate and bank forms."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CC complete")
