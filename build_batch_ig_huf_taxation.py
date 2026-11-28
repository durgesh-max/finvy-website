# -*- coding: utf-8 -*-
"""Batch IG (25 Nov 2026): HUF taxation in India 2026 - HUF is a separate taxpayer with its own PAN; new regime is the
default for tax year 2026-27 (section 202 of the Income-tax Act, 2025, earlier section 115BAC) with the same slabs as
individuals (nil up to Rs 4 lakh ... 30% above Rs 24 lakh); the section 87A rebate (section 156 of the 2025 Act) is for
resident individuals only, so an HUF gets no nil-tax-up-to-Rs-12-lakh benefit; old regime basic exemption Rs 2.5 lakh
with deductions such as 80C / 80D for members; HUF without business income can choose the regime each year in the
return. Gifts: from members exempt in the HUF's hands (relative = member for an HUF); member's own property transferred to the HUF
without adequate consideration - income clubbed with the member (section 64(2) of the 1961 Act). Formation by birth /
marriage, declaration deed, PAN, bank account; partition recognised for tax only when recognised under the law.
Demand: sweep ac109 (25 Nov 2026), 6-7 markets: "huf tax", "huf tax slab", "huf tax benefits", "huf tax exemption
limit", "huf tax slab new regime", "huf tax calculator", "huf taxation", "huf tax rate".
Facts (checked 25 Nov 2026): Income Tax Department tax-rate page for HUFs and HUF return help; Taxguru (section 202 /
156 for HUFs); Business Today (8 Sept 2026) and Upstox on HUF tax planning for 2026-27; CAclubindia forum; site NRI karta
page."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "huf-taxation-india-2026-tax-slab-new-regime-benefits-exemption-limit-no-87a-rebate"

C = contact("whether the HUF already exists (PAN, deed), its income sources, the karta and members, and whether any member is abroad")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="HUF Taxation in India 2026: How an HUF Is Taxed vs an Individual, Tax Slab, New vs Old Regime, Exemption Limit, Benefits and Why There Is No Rs 12 Lakh Rebate",
    em="a separate taxpayer, with one important difference from individuals.",
    kicker="/ Hindu Undivided Families &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>A Hindu Undivided Family (HUF) is taxed as a separate person with its own PAN, using the same slab rates as an individual: under the default new regime, income up to &#8377;4 lakh is nil, rising in bands to 30% above &#8377;24 lakh.</strong> "
          "The key difference is that the section 87A rebate (section 156 of the Income-tax Act, 2025), which makes tax nil up to &#8377;12 lakh, applies only to resident individuals, so an HUF pays tax on income above &#8377;4 lakh in the new regime. "
          "Under the old regime the basic exemption is &#8377;2.5 lakh, with deductions such as section 80C and 80D available on payments for members. The main benefit of an HUF is a second slab structure and set of deductions within the family."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is the HUF tax slab for 2026-27?</strong> New regime: nil up to &#8377;4 lakh, 5% to &#8377;8 lakh, 10% to &#8377;12 lakh, 15% to &#8377;16 lakh, 20% to &#8377;20 lakh, 25% to &#8377;24 lakh, 30% above, plus 4% cess.",
            "<strong>Does an HUF get the &#8377;12 lakh rebate?</strong> No. The rebate is for resident individuals only, so an HUF with income of, say, &#8377;10 lakh pays tax under the new regime.",
            "<strong>What is the HUF exemption limit?</strong> &#8377;4 lakh in the new regime and &#8377;2.5 lakh in the old regime; there is no higher senior-citizen limit for an HUF.",
            "<strong>Which regime should an HUF choose?</strong> The new regime applies by default; an HUF without business income can opt for the old regime each year when filing. Compare using the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ".",
            "<strong>What are the HUF tax benefits?</strong> A separate basic exemption and slabs, its own deductions (old regime), and capital gains exemptions such as section 54 on its own property sales.",
            "<strong>Are gifts to an HUF taxable?</strong> Gifts from members are exempt (for an HUF, a relative means a member); gifts from anyone else above &#8377;50,000 in a year are taxable. If a member transfers their own property to the HUF without adequate consideration, income from it is clubbed with that member.")),
        ("/ New vs old regime for an HUF", "Side by side.",
         table(["Point", "New regime (default)", "Old regime"], [
             ["Nil slab", "&#8377;4 lakh", "&#8377;2.5 lakh"],
             ["Section 87A / 156 rebate", "Not available to HUFs", "Not available to HUFs"],
             ["80C, 80D and similar deductions", "Not available", "Available (payments for members)"],
             ["Switching", "Default", "HUF without business income can opt each year in the return"]])),
        ("/ Setting up and running an HUF", "Practical steps.",
         ul("<strong>Formation:</strong> an HUF arises by birth and marriage in a Hindu, Jain, Sikh or Buddhist family; document it with a declaration deed naming the karta and members.",
            "<strong>PAN and bank account:</strong> apply for a PAN in the HUF&rsquo;s name, then open a bank account operated by the karta.",
            "<strong>Funding:</strong> ancestral property, gifts from members or will inheritances; avoid members transferring their own assets without consideration because of clubbing.",
            "<strong>Karta abroad:</strong> residence and tax change when the karta is an NRI; see " + L("nri-karta-huf-residential-status-tax-india-can-nri-be-karta-2026.html", "can an NRI be karta of an HUF") + ".",
            "<strong>Gifts and capital gains:</strong> see " + L("section-56-2-x-gift-tax-india-2026.html", "gift tax under section 56(2)(x)") + " and " + L("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "tax rates 2026-27") + ".")
         + call_box("HUF tax", ["HUF formation and deed",
                                 "PAN and bank account",
                                 "Regime choice and ITR filing",
                                 "Gifts and clubbing checks",
                                 "Partition planning"],
                    "the family structure and income sources.")
         + sources("Income-tax Act, 2025 sections 202 (new regime) and 156 (rebate for resident individuals), and the 1961 Act sections 115BAC, 87A, 56(2)(x) and 64(2); Income Tax Department tax-rate page for HUFs and HUF return help; Taxguru, Business Today (8 September 2026) and Upstox commentary on HUF tax for 2026-27. Checked 25 November 2026.")),
    ],
    faqs=[("What is the HUF tax slab under the new regime for 2026-27?", "The same as individuals: nil up to Rs 4 lakh, 5% from Rs 4 lakh to Rs 8 lakh, 10% to Rs 12 lakh, 15% to Rs 16 lakh, 20% to Rs 20 lakh, 25% to Rs 24 lakh and 30% above Rs 24 lakh, plus 4% cess."),
        ("How is an HUF taxed, and how is it different from an individual?", "An HUF is a separate taxpayer: it has its own PAN, files its own return and pays tax on its own income, apart from the karta and members. It uses the same slab rates as an individual and gets its own basic exemption (Rs 4 lakh in the new regime, Rs 2.5 lakh in the old), so income moved into an HUF legitimately can be taxed at a lower slab. The differences: no section 87A rebate, so the Rs 12 lakh nil-tax benefit of individuals does not apply; no higher exemption for senior citizens; no salary or standard deduction; deductions such as 80C and 80D only in the old regime (for payments made for members); and presumptive taxation under 44AD for business is available, but 44ADA for professionals is limited to resident individuals and partnership firms. Income from property a member transfers to the HUF without adequate consideration stays taxable in the member's hands, and for tax purposes only a total partition is recognised, not a partial one. WhatsApp +91 78018 87130 with the HUF's PAN or deed (if it exists), its income sources and the karta and members, and we tell you whether an HUF return or set-up makes sense."),
          ("Can an HUF claim the section 87A rebate?", "No. The rebate (section 156 of the Income-tax Act, 2025) is available only to resident individuals, so an HUF pays tax on income above the Rs 4 lakh nil slab in the new regime."),
          ("What is the basic exemption limit for an HUF?", "Rs 4 lakh under the new regime and Rs 2.5 lakh under the old regime. There is no higher limit for senior citizens because an HUF is not an individual."),
          ("Can an HUF choose the old tax regime?", "Yes. The new regime is the default, but an HUF without business or professional income can opt for the old regime each year when filing its return; with business income, the choice is made by a separate option."),
          ("Are gifts to an HUF taxable?", "Gifts from members are exempt - for an HUF, a 'relative' means a member of the HUF. Gifts from anyone else are taxable if they exceed Rs 50,000 in a year. If a member transfers their own property to the HUF without adequate consideration, the income from it is taxed in the member's hands."),
          ("How do I create an HUF?", "An HUF arises by law in a Hindu, Jain, Sikh or Buddhist family; in practice it is documented with a declaration or deed naming the karta and members, then a PAN is obtained in the HUF's name and a bank account opened in that name. It needs funds of its own - typically gifts from relatives or ancestral property - because if a member transfers personal property to the HUF without adequate consideration, the income from it is clubbed with that member."),
          ("How is partition of an HUF taxed?", "Only a total partition is recognised for income tax: on a claim, the Assessing Officer holds an inquiry and records a finding, and the HUF is assessed as such only up to the date of partition. A partial partition made after 31 December 1978 is not recognised, so the family continues to be assessed as an undivided HUF. Members are not taxed when they receive their share on partition; when they later sell, the HUF's cost and holding period carry over."),
          ("Can BQP set up and file returns for an HUF?", "Yes. CA Durgesh Chavda can help with the HUF deed, PAN, regime choice, return filing and partition planning, including where the karta lives abroad. " + C)],
    related=[("nri-karta-huf-residential-status-tax-india-can-nri-be-karta-2026.html", "Can an NRI be karta of an HUF?"),
             ("section-56-2-x-gift-tax-india-2026.html", "Gift tax under section 56(2)(x)"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary 2026-27")],
    cta_h="Setting up or filing for an HUF?", cta_b=C,
    keywords="HUF tax, HUF tax slab 2026-27, HUF tax slab new regime, HUF tax benefits, HUF exemption limit, HUF 87A rebate, HUF taxation India, HUF tax rate, HUF tax calculator",
    desc="HUF taxation in India 2026: same slabs as individuals (nil to Rs 4 lakh new regime, Rs 2.5 lakh old), no section 87A / 156 rebate, regime choice, deductions, gifts and clubbing, HUF formation, PAN and karta abroad.",
    howto={"name": "How an HUF is taxed", "description": "For tax year 2026-27.", "steps": [
        {"name": "Confirm the HUF exists", "text": "Deed, PAN and bank account in the HUF's name."},
        {"name": "Total the HUF's income", "text": "Rent, interest, business or capital gains on HUF assets."},
        {"name": "Choose the regime", "text": "New by default; old if deductions make it better."},
        {"name": "Apply slabs without 87A", "text": "No rebate for HUFs; add 4% cess."},
        {"name": "File the return", "text": "In the HUF's name, signed by the karta."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IG complete")
