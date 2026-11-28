# -*- coding: utf-8 -*-
"""Batch MI (29 Nov 2026): Private family trust taxation in India - how a private trust is set up (settlor, trustees,
beneficiaries, trust deed under the Indian Trusts Act, 1882), specific vs discretionary trusts, tax at beneficiaries' rates vs
the maximum marginal rate, revocable transfers, gifts to a trust for relatives, clubbing, and will vs trust.
Demand: sweep ac269 (29 Nov 2026), all 7 markets: 'family trust taxation india' (coverage 0.33), 'is family trust taxable',
'how is a family trust taxed', 'family trust tax rate in india', 'family trust tax benefits in india', 'family trust india
income tax' (0.50), 'will vs trust india', 'living trust vs will india' (0.33-0.50). No page on the site. Families, business
owners and NRIs planning succession need structuring help. User steer 26 Nov 2026: more call bookings.
Facts (Income-tax Act, 1961, sections 61-63, 64, 160-164, 56(2)(x); carried into the Income-tax Act, 2025 under new section
numbers): a private trust is created by a settlor transferring property to trustees for beneficiaries under a trust deed (Indian
Trusts Act, 1882); trustees are representative assessees; where beneficiaries and their shares are known (specific trust), income
is taxed at the rates applicable to the beneficiaries, either in the trustees' hands or directly in the beneficiaries' hands;
where shares are indeterminate (discretionary trust), income is generally taxed at the maximum marginal rate, with limited
exceptions (for example certain trusts created by will and trusts for relatives dependent on the settlor where beneficiaries'
incomes are below the taxable limit); a trust with business income is generally taxed at the maximum marginal rate, with limited
exceptions; income from a revocable transfer is taxed in the settlor's hands; property received by a trust created solely for the
benefit of the settlor's relatives is exempt from tax on gifts under section 56(2)(x); clubbing applies where the trust benefits
the settlor's spouse or son's wife; India has no inheritance or estate tax; a will takes effect only on death and may need probate
depending on where and for whom it is made; a trust works during the settlor's lifetime and assets in the trust pass under the
deed. No stamp duty or fee figures, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "family-trust-taxation-india-private-trust-specific-discretionary-maximum-marginal-rate-will-vs-trust-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with what you want the trust to hold (property, shares, "
     "business, investments), who the beneficiaries are and where they live, whether shares should be fixed or at the trustees' "
     "discretion, and whether a will already exists. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Family Trust Taxation in India (2026): How Private Trusts Are Taxed, Specific vs Discretionary Trusts, the Maximum Marginal Rate, Gifts to a Trust and Will vs Trust",
    em="the deed decides the tax.",
    kicker="/ Families, business owners and NRIs planning succession &middot; Private family trusts &middot; Updated 2026-11-29",
    lead=("<strong>A private family trust is taxed through its trustees, but the rate depends on how the deed is drafted. "
          "If the beneficiaries and their shares are fixed (a specific trust), income is taxed at the beneficiaries&rsquo; own rates; if the trustees decide who gets what (a discretionary trust), income is generally taxed at the maximum marginal rate, with limited exceptions. "
          "Settling property on a trust for relatives is not taxed as a gift, and India has no inheritance tax.</strong>"),
    sections=[
        ("/ How a family trust is taxed", "Sections 160 to 164 of the Income-tax Act, 1961.",
         table(["Type", "How income is taxed"], [
             ["Specific (determinate) trust", "At the beneficiaries' applicable rates - in the trustees' hands as representative assessees or directly in the beneficiaries' hands"],
             ["Discretionary trust", "Generally at the maximum marginal rate, with limited exceptions (some will trusts and trusts for dependent relatives with low incomes)"],
             ["Trust with business income", "Generally at the maximum marginal rate, with limited exceptions"],
             ["Revocable transfer to the trust", "Income taxed in the settlor's hands"],
             ["Trust benefiting the settlor's spouse or son's wife", "Income can be clubbed with the settlor"]])
         + ul("<strong>Setting up:</strong> a settlor transfers property to trustees for named beneficiaries under a trust deed governed by the Indian Trusts Act, 1882; the trust takes a PAN and files returns through its trustees.",
              "<strong>Gifts to the trust:</strong> property received by a trust created solely for the benefit of the settlor&rsquo;s relatives is not taxed as a gift.",
              "<strong>New Act:</strong> the same rules continue in the Income-tax Act, 2025 from tax year 2026-27, under new section numbers.")),
        ("/ Will vs trust", "Which suits the family?",
         ul("<strong>Will:</strong> takes effect only on death; depending on where it is made and for whom, probate may be needed before assets pass.",
            "<strong>Trust:</strong> works during the settlor&rsquo;s lifetime; assets in the trust pass under the deed, giving continuity and control over when beneficiaries receive them.",
            "<strong>Tax neutrality:</strong> India has no inheritance or estate tax, so the choice is mostly about control, continuity, protection and the income-tax rate on trust income.",
            "<strong>Transfer costs:</strong> moving property into a trust can attract state stamp duty and registration - check before transferring real estate.",
            "<strong>NRI beneficiaries or trustees:</strong> FEMA rules on transfers to and distributions for non-residents need checking along with the tax position.")
         + call_box("family trusts and succession", ["Specific vs discretionary structure",
                                                     "Trust deed tax review",
                                                     "Transferring property and shares into the trust",
                                                     "Trust PAN, returns and distributions",
                                                     "Will, trust and NRI beneficiaries"],
                    "Assets, beneficiaries and residence, fixed or discretionary shares, existing will.")
         + sources("Indian Trusts Act, 1882; Income-tax Act, 1961 (sections 56(2)(x), 61 to 64 and 160 to 164) and the corresponding provisions of the Income-tax Act, 2025; site clubbing of income, HUF taxation, gift tax and NRI will pages.")),
    ],
    faqs=[("Is a family trust taxable in India?", "Yes. A private family trust files returns through its trustees. Income of a specific trust, where beneficiaries and shares are fixed, is taxed at the beneficiaries' rates; income of a discretionary trust is generally taxed at the maximum marginal rate, with limited exceptions."),
          ("What is the tax rate for a discretionary family trust?", "Generally the maximum marginal rate. Exceptions include certain trusts created by will and trusts set up for relatives dependent on the settlor where the beneficiaries' incomes are below the taxable limit."),
          ("Is transferring property to a family trust taxed as a gift?", "Not where the trust is created solely for the benefit of the settlor's relatives - such receipts are exempt from tax on gifts. Stamp duty and registration on transferring real estate are separate and depend on the state."),
          ("Will or trust - which is better in India?", "A will takes effect only on death and may need probate depending on where it is made and for whom. A trust works during the settlor's lifetime and lets assets pass under the deed with more control. India has no inheritance tax, so the choice turns mainly on control, continuity and the tax rate on trust income."),
          ("Is income from a family trust clubbed with the settlor?", "It can be. Income from a revocable transfer is taxed in the settlor's hands, and income from assets settled for the benefit of the settlor's spouse or son's wife can be clubbed with the settlor."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the assets, beneficiaries and where they live, whether shares should be fixed or discretionary, and whether a will exists. Or book a call directly.")],
    related=[("clubbing-of-income-india-spouse-minor-child-section-64-gift-to-wife-1500-exemption-huf-2026.html", "Clubbing of income"),
             ("huf-taxation-india-2026-tax-slab-new-regime-benefits-exemption-limit-no-87a-rebate.html", "HUF taxation in India"),
             ("section-56-2-x-gift-tax-india-2026.html", "Gift tax under section 56(2)(x)"),
             ("nri-will-india-probate-not-mandatory-mumbai-chennai-kolkata-succession-legal-heir-certificate-2026.html", "NRI will, probate and succession")],
    cta_h="Planning a family trust or succession structure?", cta_b=C,
    keywords="family trust taxation india, is family trust taxable, how is a family trust taxed, family trust tax rate in india, discretionary trust maximum marginal rate, specific trust tax india, private trust income tax, will vs trust india, living trust vs will india",
    desc="Family trust taxation in India: specific trusts taxed at beneficiaries' rates, discretionary trusts generally at the maximum marginal rate, revocable transfers and clubbing, gifts to a trust for relatives, no inheritance tax, and will vs trust.",
    howto={"name": "How to plan a family trust", "description": "Purpose, structure, deed, transfer.", "steps": [
        {"name": "Define the purpose", "text": "Succession, protection, control or ongoing support."},
        {"name": "Choose the structure", "text": "Specific (fixed shares) or discretionary - it drives the tax rate."},
        {"name": "Draft the deed", "text": "Settlor, trustees, beneficiaries, powers and distribution rules."},
        {"name": "Transfer and comply", "text": "Move assets, take a PAN, file returns and document distributions."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MI complete")
