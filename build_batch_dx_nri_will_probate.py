# -*- coding: utf-8 -*-
"""Batch DX (20 Nov 2026): NRI wills and inheritance documents in India - probate no longer compulsory in Mumbai,
Chennai and Kolkata (Repealing and Amending Act, 2025), will registration optional, India will vs foreign will,
succession certificate vs legal heir certificate, tax and repatriation. Call-first page.
Demand: sweep 20 Nov 2026 (ac18), all 7 markets: "nri will in india", "nri legal heir certificate".
Facts (checked 20 Nov 2026): Repealing and Amending Act, 2025 removed the statutory requirement of probate for wills in
Mumbai, Chennai and Kolkata; probate remains available and is often still requested by registrars, banks and buyers
(Khaitan, Moneylife, Upstox, Global Law Experts); succession certificate (Part X, section 372, Indian Succession Act)
covers debts and securities, not immovable property; legal heir certificate is an administrative document from the
revenue office; foreign wills and foreign probate may need ancillary probate in India; registration of wills is optional
under the Registration Act; India has no inheritance tax; inherited assets carry the previous owner's cost and holding
period for capital gains; NRIs can remit inherited assets from NRO within USD 1 million per financial year with Forms
15CA/15CB."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
WL = "nri-will-india-probate-not-mandatory-mumbai-chennai-kolkata-succession-legal-heir-certificate-2026"

C_WL = contact("your country of residence, the Indian assets (property, bank, shares), where they are, and whether there is an Indian or foreign will")
PAGES = [dict(
    slug=WL,
    title="NRI Will and Inheritance in India (2026): Probate No Longer Compulsory in Mumbai, Chennai and Kolkata, Separate India Will, Succession and Legal Heir Certificates, Tax and Repatriation",
    em="what changed in 2025 and how NRIs should plan Indian assets.",
    kicker="/ NRIs &middot; Wills &middot; Inheritance &middot; Updated 2026-11-20",
    lead=("NRIs can make a will for their Indian assets in India, and <strong>registering it is optional</strong>. Many keep a <strong>separate India will</strong> alongside the will in their country of residence, because a foreign will or foreign probate may need <strong>ancillary probate</strong> before Indian banks and registrars act on it. "
          "The <strong>Repealing and Amending Act, 2025</strong> removed the rule that made <strong>probate compulsory</strong> for wills in <strong>Mumbai, Chennai and Kolkata</strong>. Probate is still available and often still requested by sub-registrars, banks and property buyers. "
          "Without a will, heirs use a <strong>succession certificate</strong> for bank balances, shares and other debts and securities, or a <strong>legal heir certificate</strong> from the revenue office, depending on the asset and the institution. "
          "India has <strong>no inheritance tax</strong>. A later sale is taxed using the previous owner's cost and holding period, and NRI heirs can remit inherited money abroad from an NRO account within <strong>USD 1 million per financial year</strong> after tax."),
    sections=[
        ("/ Which document does what", "For NRI heirs and planners.",
         table(["Document", "Used for", "Issued by", "Notes"], [
             ["Will (India)", "Directs who gets Indian assets", "The person making it", "Registration optional; two witnesses; keep it consistent with any foreign will"],
             ["Probate", "Court confirmation of the will", "High Court or District Court", "No longer compulsory in Mumbai, Chennai and Kolkata after the 2025 Act; still often asked for property"],
             ["Ancillary probate", "Recognising a foreign will or foreign probate in India", "Indian court", "Often needed when only a foreign will exists"],
             ["Succession certificate", "Bank balances, shares, deposits (debts and securities)", "Civil court", "Not for immovable property"],
             ["Legal heir certificate", "Pensions, utility and administrative transfers; some banks", "Revenue office (Tehsildar)", "Administrative, not a court order"],
             ["Mutation", "Updating land and property records", "Local revenue or municipal office", "After title is established"]])
         + call_box("an NRI will or inheritance in India", ["Whether you need an India will alongside your foreign will",
                                                             "Which documents your heirs will need for each asset",
                                                             "Tax on inherited property and later sale",
                                                             "Repatriating inherited money from India",
                                                             "Coordinating with an Indian succession lawyer"],
                    "a list of Indian assets and their location, your country of residence, and copies of any existing wills.")),
        ("/ Tax and repatriation for NRI heirs", "What happens after inheritance.",
         ul("<strong>No inheritance tax:</strong> receiving property or money by inheritance is not taxed in India.",
            "<strong>Income after inheritance:</strong> rent, interest and dividends are taxable to the heir; see <a href=\"nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html\">rent to NRIs</a>.",
            "<strong>Selling inherited property:</strong> cost and holding period of the previous owner carry over; long-term gains at 12.5% for NRIs; buyer deducts TDS unless a lower deduction certificate is obtained; see <a href=\"inherited-property-india-rules-rights-sale-tax-nri-resident-2026.html\">inherited property rules and sale</a>.",
            "<strong>Repatriation:</strong> inherited assets go through the NRO account; remittance up to USD 1 million per financial year with Forms 15CA/15CB; see <a href=\"repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html\">repatriating money</a>.",
            "<strong>Home country:</strong> the US, UK, Canada and Australia have their own estate, inheritance or capital gains rules and reporting for foreign inheritances; plan with both sides.")
         + '<p>Related: <a href="nri-inheritance-indian-property-tax-fema-2026.html">NRI inheritance: tax and FEMA</a> &middot; <a href="inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html">inheriting from India while living abroad</a> &middot; <a href="nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html">agricultural land</a>.</p>'
         + sources("Indian Succession Act, 1925 (section 213 as amended by the Repealing and Amending Act, 2025; Part X succession certificates); Registration Act, 1908 (optional registration of wills); Income-tax Act provisions on gifts, inheritance and capital gains; FEMA rules on remittance of assets. Commentary checked 20 November 2026: Khaitan &amp; Co, Moneylife, Upstox, Global Law Experts. Legal steps should be confirmed with an Indian succession lawyer; we coordinate on tax and FEMA.")),
    ],
    faqs=[("Can an NRI make a will in India?", "Yes. An NRI can make a will for Indian assets; it needs two witnesses, and registration is optional. Many NRIs keep a separate India will consistent with their foreign will."),
          ("Is probate still mandatory in Mumbai, Chennai and Kolkata?", "No. The Repealing and Amending Act, 2025 removed the compulsory probate requirement for wills in those cities, though registrars, banks and buyers may still ask for probate, especially for property."),
          ("What is the difference between a succession certificate and a legal heir certificate?", "A succession certificate is issued by a civil court for debts and securities such as bank balances and shares; a legal heir certificate is an administrative document from the revenue office used for pensions and similar transfers."),
          ("Does a foreign will work in India?", "It can, but Indian banks and registrars often require ancillary probate of a foreign will or foreign probate order, which is why many NRIs keep a separate India will."),
          ("Is inheritance taxed in India for NRIs?", "No inheritance tax applies; income from inherited assets and gains on their later sale are taxable, using the previous owner's cost and holding period."),
          ("Can BQP help NRI heirs?", "Yes, on tax, FEMA and repatriation, working with your Indian lawyer. " + C_WL)],
    related=[("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance: tax and FEMA"), ("inherited-property-india-rules-rights-sale-tax-nri-resident-2026.html", "Inherited property rules and sale"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriating money from India")],
    cta_h="Planning or dealing with an inheritance in India?", cta_b=C_WL,
    keywords="NRI will in India, probate not mandatory Mumbai Chennai Kolkata 2025, Repealing and Amending Act 2025 probate, NRI legal heir certificate, succession certificate vs legal heir certificate, foreign will India ancillary probate, NRI inheritance tax India",
    desc="NRI will and inheritance in India (2026): registration optional, separate India will, probate no longer compulsory in Mumbai, Chennai and Kolkata after the Repealing and Amending Act 2025, ancillary probate for foreign wills, succession vs legal heir certificates, no inheritance tax, sale and repatriation.",
    howto={"name": "How an NRI plans Indian assets for heirs", "description": "Will, documents, tax and repatriation.", "steps": [
        {"name": "List Indian assets", "text": "Property, bank accounts, shares and mutual funds, with locations."},
        {"name": "Make an India will", "text": "Consistent with your foreign will; two witnesses; registration optional."},
        {"name": "Keep nominations updated", "text": "Bank, demat and mutual fund nominations, aligned with the will."},
        {"name": "Brief your heirs", "text": "Which documents each asset will need: probate, succession or legal heir certificate."},
        {"name": "Plan tax and repatriation", "text": "Sale timing, lower deduction certificates and NRO remittance limits."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DX complete:", len(PAGES))
