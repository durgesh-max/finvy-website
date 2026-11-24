# -*- coding: utf-8 -*-
"""Batch GO (24 Nov 2026): Gift deed to an NRI son or daughter - when a gift deed is needed, registration vs notarisation,
who can receive, FEMA rules for gifting Indian property to NRIs/OCIs, income tax (relatives exempt), stamp duty, signing
from abroad, later sale and capital gains, revocation. Call-first page for parents in India and NRI children.
Demand: sweep ac66 (24 Nov 2026), all 7 markets: "gift deed to nri son", "nri gift deed format", "is gift deed necessary",
"can gift deed be notarized", "gift deed can be given to whom".
Facts (checked 24 Nov 2026): Transfer of Property Act section 123 - a gift of immovable property must be made by a
registered instrument signed by or on behalf of the donor and attested by at least two witnesses; section 122 - acceptance
by the donee during the donor's lifetime; movable property can be gifted by registered deed or by delivery. FEMA (NDI
Rules) - an NRI or OCI may receive residential or commercial property by gift from a relative (Companies Act 2013 section
2(77)); agricultural land, plantation property and farmhouses cannot be received by gift (RBI FAQ, Taxmann, Mondaq).
Income tax: gifts from relatives exempt (site page on section 56(2)(x)); cost and holding period of the previous owner
carry over on later sale. Stamp duty set by each state, often concessional for family gifts."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "gift-deed-to-nri-son-daughter-india-property-registration-fema-tax-stamp-duty-2026"

C = contact("what is being gifted (flat, house, land, money, shares), the state where the property is, who gives and who receives, and where the receiver lives")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Gift Deed to an NRI Son or Daughter (2026): Registration, FEMA Rules, Tax and Stamp Duty for Indian Property",
    em="registered, not just notarised.",
    kicker="/ NRIs &middot; Family property &middot; Updated 2026-11-24",
    lead=("<strong>Parents in India can gift a flat, house or commercial property to an NRI or OCI son or daughter: FEMA allows gifts of residential and commercial property between relatives without RBI approval, and the gift is tax-free for the child as a gift from a relative.</strong> "
          "For immovable property the gift must be made by a <strong>registered gift deed</strong>, signed by the parent and attested by two witnesses; a notarised deed is not enough. The child must accept the gift while the parent is alive, which can be done from abroad. "
          "Agricultural land, plantations and farmhouses cannot be gifted to an NRI or OCI. Stamp duty is set by each state and is often lower for family gifts. When the child later sells, the parent&rsquo;s cost and holding period carry over."),
    sections=[
        ("/ Quick answers", "What families ask.",
         ul("<strong>Is a gift deed necessary?</strong> For immovable property, yes, and it must be registered. For money or shares, a gift deed is not legally required but is good evidence of a gift.",
            "<strong>Can a gift deed be notarised instead of registered?</strong> Not for immovable property: a notarised gift deed does not transfer a flat or land. It can support a gift of money or movable assets.",
            "<strong>Who can a gift deed be given to?</strong> Anyone can receive a gift, but only gifts from relatives (parents, spouse, siblings, children and others in the income tax list) are fully tax-free, and FEMA lets an NRI or OCI receive Indian property by gift only from a relative.",
            "<strong>Can I gift property to my NRI son?</strong> Yes, residential or commercial property, with no RBI approval. Not agricultural land, plantations or farmhouses.",
            "<strong>Does my son need to come to India?</strong> Usually not: he can accept the gift by signing at an Indian consulate or through a registered power of attorney holder, depending on the state&rsquo;s registration practice.")),
        ("/ Gift deed at a glance", "Rules that apply to each type of asset.",
         table(["Asset", "Gift deed", "FEMA for an NRI/OCI receiver", "Tax for the receiver"], [
             ["Flat, house, commercial property", "Registered deed, two witnesses, stamp duty", "Allowed from a relative", "Exempt if from a relative"],
             ["Agricultural land, plantation, farmhouse", "Registered deed", "Not allowed by gift", "Not applicable"],
             ["Money", "Not mandatory; a simple deed or letter helps", "Allowed; outward gifts by residents fall under the LRS", "Exempt if from a relative"],
             ["Shares and mutual funds", "Transfer form; deed optional", "Allowed, with reporting in some cases", "Exempt if from a relative"]])
         + '<p>Money gifts from parents abroad are covered in ' + L("gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026.html", "gift money from parents") + '; the tax rule for gifts from non-relatives is in ' + L("section-56-2-x-gift-tax-india-2026.html", "section 56(2)(x) explained") + '.</p>'),
        ("/ Steps and later sale", "Doing it properly.",
         ul("<strong>Draft the deed:</strong> names, relationship, property description, that the gift is voluntary and without consideration, and acceptance by the child.",
            "<strong>Pay stamp duty and register</strong> at the sub-registrar&rsquo;s office where the property is, with the parent and two witnesses; check the state&rsquo;s concessional rate for family gifts.",
            "<strong>Acceptance from abroad:</strong> the child signs an acceptance at an Indian consulate or appoints a power of attorney holder; see " + L("nri-property-management-india-from-abroad-power-of-attorney-rent-tds-itr-repatriation-2026.html", "power of attorney for NRIs") + ".",
            "<strong>Update records:</strong> mutation in local land and municipal records, society share certificate and utility accounts.",
            "<strong>Later sale:</strong> the parent&rsquo;s purchase cost and holding period count for capital gains, and the buyer deducts tax because the seller is an NRI; see " + L("nri-selling-indian-property-capital-gains.html", "NRI property sale") + ".",
            "<strong>Revocation:</strong> a completed gift generally cannot be revoked, except on conditions written into the deed or, for senior citizens, where a gift made on condition of care is not honoured under the senior citizens&rsquo; maintenance law.")
         + call_box("gifting Indian property to NRI children", ["Gift vs will vs sale: which suits the family",
                                                             "FEMA check for NRI or OCI receivers",
                                                             "Tax position now and on a later sale",
                                                             "Coordinating the deed, registration and consulate signing",
                                                             "Home-country reporting for the child (for example Form 3520 in the US)"],
                    "the asset, the state, the family members and where the child lives.")
         + sources("Transfer of Property Act, 1882, sections 122 and 123; Registration Act, 1908, section 17; Foreign Exchange Management (Non-debt Instruments) Rules, 2019 and RBI FAQs on acquisition of immovable property by NRIs and OCIs (gift from a relative as defined in section 2(77) of the Companies Act, 2013; no agricultural land, plantation or farmhouse); Income-tax Act provisions exempting gifts from relatives; state stamp acts; Maintenance and Welfare of Parents and Senior Citizens Act, 2007, section 23. Legal drafting and registration are done with an advocate; BQP advises on tax and FEMA. Checked 24 November 2026.")),
    ],
    faqs=[("Is a gift deed necessary to gift property to my son?", "Yes for immovable property: a gift of a flat, house or land must be made by a registered gift deed signed by the giver and attested by two witnesses. For money or shares a gift deed is not required, though a simple deed or letter is useful evidence."),
          ("Can a gift deed be notarised instead of registered?", "Not for immovable property. A notarised gift deed does not transfer ownership of a flat or land; it must be registered with the sub-registrar. Notarisation can support a gift of money or movable assets."),
          ("Can parents gift property in India to an NRI son or daughter?", "Yes. Under FEMA, an NRI or OCI can receive residential or commercial property by gift from a relative without RBI approval. Agricultural land, plantations and farmhouses cannot be gifted to them."),
          ("Is a gift from parents to an NRI child taxed in India?", "No. Gifts from relatives, including parents, are exempt from income tax in the receiver's hands. On a later sale, the parent's cost and holding period are used to work out capital gains."),
          ("Does the NRI child need to travel to India for the gift deed?", "Usually not. The child can accept the gift by signing at an Indian consulate or through a registered power of attorney holder, depending on the state's registration practice; the parent and two witnesses attend the registration."),
          ("Can BQP help with gifting property to NRI children?", "Yes. " + C)],
    related=[("nri-gift-indian-relatives-section-56-fema-2026.html", "NRI gifts to relatives in India"),
             ("gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026.html", "Gift money from parents"),
             ("nri-inheritance-indian-property-tax-fema-2026.html", "NRI inheritance of Indian property"),
             ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "Agricultural land for NRIs and OCIs"),
             ("nri-selling-indian-property-capital-gains.html", "NRI property sale and capital gains")],
    cta_h="Gifting a home to a child abroad?", cta_b=C,
    keywords="gift deed to NRI son, NRI gift deed format, is gift deed necessary, can gift deed be notarized, gift deed can be given to whom, gift property to NRI FEMA, gift deed stamp duty family, gift deed acceptance from abroad",
    desc="Gift deed to an NRI son or daughter (2026): immovable property needs a registered deed with two witnesses (notarised is not enough); FEMA allows residential and commercial property gifts from relatives, not agricultural land; tax-free from relatives; state stamp duty; acceptance from abroad; later sale.",
    howto={"name": "How parents gift Indian property to an NRI child", "description": "Steps from deed to records.", "steps": [
        {"name": "Check the property type", "text": "Residential or commercial can be gifted to an NRI or OCI; agricultural land cannot."},
        {"name": "Draft the gift deed", "text": "Voluntary, without consideration, with the child's acceptance."},
        {"name": "Pay stamp duty and register", "text": "At the sub-registrar with the parent and two witnesses."},
        {"name": "Accept from abroad", "text": "Consulate signature or a registered power of attorney."},
        {"name": "Update records", "text": "Mutation, society records and utilities; keep papers for a later sale."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GO complete")
