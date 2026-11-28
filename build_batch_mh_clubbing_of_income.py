# -*- coding: utf-8 -*-
"""Batch MH (29 Nov 2026): Clubbing of income in India - income of a spouse, minor child, son's wife and HUF conversions taxed
in the hands of the individual: section 64 (and section 27 deemed ownership) of the Income-tax Act, 1961, carried into the
Income-tax Act, 2025; exceptions; the per-child exemption; gifts vs clubbing; planning points.
Demand: sweep ac269 (29 Nov 2026), all 7 markets: 'clubbing of income minor child' (coverage 0.25), 'clubbing of income of
spouse minor child etc' (0.17), '... of minor child exemption / section / deduction' (0.40), 'how much income of minor child is
exempt' (0.40); 'gift to wife tax clubbing' seed. Only passing mentions on 3 pages. Families moving money between spouses and
children, and NRIs gifting to relatives in India, need planning help. User steer 26 Nov 2026: more call bookings.
Facts (Income-tax Act, 1961, section 64 and section 10(32)): income from assets transferred directly or indirectly to a spouse
without adequate consideration (other than under an agreement to live apart) is clubbed with the transferor; income earned on
the clubbed income itself is not clubbed; salary, commission or fees paid to a spouse by a concern in which the individual has a
substantial interest (20% or more of voting power or profits) is clubbed, unless the spouse has technical or professional
qualifications and the income is solely attributable to them; assets transferred to a son's wife without adequate consideration
- income clubbed; a minor child's income is clubbed with the parent whose total income is higher (or, if the marriage has
ended, the parent who maintains the child), except income from manual work or from an activity involving the child's skill,
talent or specialised knowledge, and the income of a minor with a disability of the kind in section 80U; the parent can claim an
exemption of up to INR 1,500 a year per minor child for clubbed income (section 10(32)); when an individual converts self-acquired
property into HUF property, income from it is clubbed with the individual; gifts to relatives are not taxed in the recipient's
hands (section 56(2)(x)) but clubbing still applies to income from gifted assets; no clubbing for gifts to adult children (other
than a son's wife). The same rules continue in the Income-tax Act, 2025 from tax year 2026-27 under new section numbers (matched
to the site's other 2025-Act references). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "clubbing-of-income-india-spouse-minor-child-section-64-gift-to-wife-1500-exemption-huf-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with who gave what to whom (cash, property, shares, "
     "deposits), when, whether anything was paid for it, the income it now earns, the ages of children, and whether anyone "
     "is an NRI. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Clubbing of Income in India (2026): Income of Spouse and Minor Child, Gift to Wife, Section 64, the INR 1,500 Per-Child Exemption and HUF Conversions",
    em="the gift is tax-free, the income from it may not be.",
    kicker="/ Families planning gifts and investments between spouses, children and HUFs &middot; Clubbing provisions &middot; Updated 2026-11-29",
    lead=("<strong>Clubbing rules make you pay tax on income that legally belongs to someone else: income from money or property you gave your spouse or son's wife without adequate consideration, most income of your minor child, and income from property you converted into HUF property. "
          "A gift to a relative is not taxed when received, but the income it earns can still be clubbed with the giver. "
          "Gifts to adult children are generally outside clubbing.</strong>"),
    sections=[
        ("/ Whose income is clubbed", "Section 64 of the Income-tax Act, 1961.",
         table(["Situation", "Clubbed with"], [
             ["Asset transferred to spouse without adequate consideration", "The person who transferred it - income from the asset"],
             ["Spouse paid salary or fees by your concern (you hold 20% or more)", "You, unless the spouse has technical or professional qualifications and the income is solely due to them"],
             ["Asset transferred to son's wife without adequate consideration", "The person who transferred it"],
             ["Income of a minor child", "The parent with the higher total income (or the parent maintaining the child if the marriage has ended)"],
             ["Own property converted into HUF property", "The individual who converted it"],
             ["Gift to an adult son or daughter", "Not clubbed - taxed in the child's hands"]])
         + ul("<strong>Second-generation income:</strong> clubbing covers income from the transferred asset, not income earned later by reinvesting that income.",
              "<strong>Both regimes:</strong> clubbing applies under the new and old tax regimes alike.",
              "<strong>New Act:</strong> the same rules continue in the Income-tax Act, 2025 from tax year 2026-27, under new section numbers.")),
        ("/ Minor children and planning", "Exceptions, the exemption and what works.",
         ul("<strong>Not clubbed:</strong> a minor child's income from manual work or from an activity involving the child's own skill, talent or specialised knowledge, and income of a minor with a disability of the kind covered by section 80U.",
            "<strong>Exemption:</strong> the parent can claim up to INR 1,500 a year per minor child against the clubbed income.",
            "<strong>Loans instead of gifts:</strong> a genuine loan on documented terms is not a transfer without consideration - interest, repayment and records matter.",
            "<strong>Investing in the spouse&rsquo;s own name from the spouse&rsquo;s own income:</strong> no clubbing, so keep the money trail clean.",
            "<strong>NRIs gifting to family in India:</strong> clubbing follows the giver&rsquo;s residential status and the source of income - check before large gifts or property transfers.")
         + call_box("clubbing and family tax planning", ["Reviewing gifts and transfers within the family",
                                                        "Loan vs gift documentation",
                                                        "Minor children's income and the exemption",
                                                        "HUF formation and conversions",
                                                        "Reporting clubbed income in the ITR"],
                    "Who gave what, when, any payment, current income, children's ages, NRI status.")
         + sources("Income-tax Act, 1961 (sections 10(32), 27, 56(2)(x) and 64) and the corresponding provisions of the Income-tax Act, 2025; site HUF taxation, gift tax under section 56(2)(x) and gift deed pages.")),
    ],
    faqs=[("What is clubbing of income?", "Clubbing means including someone else's income in your own taxable income. It applies mainly to income from assets you transferred to your spouse or son's wife without adequate consideration, your minor child's income, and income from property you converted into HUF property."),
          ("Is income from a gift to my wife taxable in my hands?", "Yes. The gift itself is not taxed in her hands because she is a relative, but the income from the gifted money or asset - interest, rent, dividends or capital gains - is clubbed with your income. Income she earns by reinvesting that income is not clubbed."),
          ("Is a minor child's income clubbed with the parents?", "Yes, with the parent whose total income is higher, or with the parent who maintains the child if the marriage has ended. Income from the child's own manual work, skill or talent is not clubbed, and nor is the income of a minor with a disability covered by section 80U."),
          ("How much of a minor child's income is exempt?", "The parent in whose income it is clubbed can claim an exemption of up to INR 1,500 a year for each minor child under section 10(32)."),
          ("Is income from a gift to an adult son or daughter clubbed?", "No. Once the child is an adult, income from the gift is taxed in the child's own hands. The exception is a gift to a son's wife, where the income is clubbed with the giver."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with who gave what to whom, when, any payment, the income it earns, the children's ages and any NRI status. Or book a call directly.")],
    related=[("huf-taxation-india-2026-tax-slab-new-regime-benefits-exemption-limit-no-87a-rebate.html", "HUF taxation in India"),
             ("section-56-2-x-gift-tax-india-2026.html", "Gift tax under section 56(2)(x)"),
             ("gift-deed-to-nri-son-daughter-india-property-registration-fema-tax-stamp-duty-2026.html", "Gift deed to an NRI son or daughter"),
             ("nri-gift-indian-relatives-section-56-fema-2026.html", "NRI gifts to Indian relatives")],
    cta_h="Moving money or property within the family?", cta_b=C,
    keywords="clubbing of income, clubbing of income minor child, clubbing of income of spouse, gift to wife tax clubbing, section 64 income tax, how much income of minor child is exempt, 1500 exemption minor child, clubbing of income huf, son's wife clubbing",
    desc="Clubbing of income in India: income from assets gifted to a spouse or son's wife, a minor child's income, and HUF conversions taxed in your hands under section 64; exceptions, the INR 1,500 per-child exemption, adult children and planning points.",
    howto={"name": "How to check whether income will be clubbed", "description": "Who, what, how, when.", "steps": [
        {"name": "Identify the relationship", "text": "Spouse, son's wife, minor child, adult child or HUF."},
        {"name": "Check the consideration", "text": "Gift, loan on proper terms, or purchase at value."},
        {"name": "Apply the exceptions", "text": "Spouse's qualifications, child's own skill, disability, second-generation income."},
        {"name": "Report correctly", "text": "Include clubbed income in the right person's return and claim the per-child exemption."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MH complete")
