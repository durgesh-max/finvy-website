# -*- coding: utf-8 -*-
"""Batch MA (28 Nov 2026): Indian resident inheriting money or assets from a relative abroad - no inheritance tax in India,
inheritance outside the gift tax rule, FEMA permission to hold inherited foreign assets, Schedule FA / FSI reporting, tax on income
and sale, foreign estate taxes, and bringing the money to India.
Demand: sweep ac246 (28 Nov 2026): 'do i need to pay tax on inheritance from abroad' (5 markets, coverage 0.40), 'do i need to pay
tax on inheritance' (6 markets) - the site has the opposite direction (inheriting from India while living abroad) but no page for an
Indian resident inheriting from abroad. Families with relatives abroad need help with FEMA and reporting. User steer 26 Nov 2026.
Facts: India has no inheritance or estate tax, and receipts by inheritance are excluded from section 56(2)(x); FEMA section 6(4) lets
a person resident in India hold foreign assets inherited from a person resident outside India, and Schedule III of the Foreign
Exchange Management (Overseas Investment) Rules, 2022 lets a resident individual acquire foreign securities by inheritance without
limit (verified by web search 28 Nov 2026 - practitioner commentary); inheritance does not use the LRS limit; a resident (ROR) must
report foreign assets in Schedule FA and foreign income in Schedule FSI of the ITR (site Schedule FA page); income from the inherited
asset (dividends, interest, rent) and gains on sale are taxable in India for a resident, with the previous owner's cost and holding
period for capital gains (section 49); the country of the deceased may levy estate or inheritance tax on the estate - India's tax
treaties cover income taxes, so foreign estate tax is generally not creditable in India; money can be brought to India through
banking channels. No fees, no thresholds invented, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "inheritance-from-abroad-indian-resident-tax-fema-schedule-fa-foreign-estate-tax-bring-money-to-india-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the country of the deceased, what you inherited "
     "(cash, bank account, shares, property, retirement account), the probate or estate documents, whether you plan to keep or "
     "sell the assets, and your residency status in India. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Inheritance From Abroad for Indian Residents (2026): Is It Taxable in India, FEMA Rules for Inherited Foreign Assets, Schedule FA Reporting, Foreign Estate Tax and Bringing the Money Home",
    em="no tax on receiving it, but plenty to report.",
    kicker="/ Indian residents with parents or relatives abroad &middot; Inherited foreign money, shares and property &middot; Updated 2026-11-28",
    lead=("<strong>India has no inheritance tax, and money or assets you inherit from a relative abroad are not taxed as a gift. "
          "FEMA lets you keep foreign assets inherited from a non-resident, and inheritance does not use your LRS limit. "
          "But as a resident you must report those assets in Schedule FA of your return, pay Indian tax on the income they earn and on any gain when you sell - and the estate may face tax in the other country first.</strong>"),
    sections=[
        ("/ The position in India", "Tax and FEMA.",
         table(["Question", "Position"], [
             ["Tax on receiving the inheritance", "None - India has no inheritance tax and inheritance is outside the gift tax rule"],
             ["Can I keep the foreign assets?", "Yes - FEMA allows a resident to hold foreign assets inherited from a non-resident; foreign securities can be inherited without limit"],
             ["Does it use my LRS limit?", "No"],
             ["Reporting", "Schedule FA (foreign assets) and Schedule FSI (foreign income) in the ITR for a resident"],
             ["Income from the assets", "Dividends, interest and rent taxable in India; foreign tax credit for tax paid abroad on that income"],
             ["Selling later", "Capital gains in India using the previous owner&rsquo;s cost and holding period"]])
         + ul("<strong>Missing Schedule FA is costly:</strong> unreported foreign assets can attract penalties under the Black Money Act - report from the year you hold them.",
              "<strong>RNOR or NRI heirs:</strong> if you are not ordinarily resident or non-resident, foreign income and reporting work differently - confirm your status first.")),
        ("/ Abroad first, then India", "The estate, probate and moving money.",
         ul("<strong>Foreign estate or inheritance tax:</strong> the deceased&rsquo;s country may tax the estate before distribution; India&rsquo;s tax treaties cover income taxes, so such estate tax is generally not creditable in India.",
            "<strong>Probate abroad:</strong> foreign banks and brokers usually need probate or an equivalent court order before releasing assets to heirs.",
            "<strong>Bringing money to India:</strong> through banking channels into your Indian account; keep the estate documents and bank advice as the source of funds.",
            "<strong>Retirement accounts and insurance:</strong> inherited pensions, 401(k) / IRA balances and policies have their own rules in the other country and in India - check before withdrawing.",
            "<strong>Property abroad:</strong> you can keep or sell inherited foreign property; rent and sale gains are reportable and taxable in India for a resident.")
         + call_box("an inheritance from abroad", ["FEMA position on keeping inherited assets",
                                                    "Schedule FA and FSI reporting",
                                                    "Tax on income and sale with foreign tax credit",
                                                    "Bringing funds to India and source documents",
                                                    "Coordination with advisers in the other country"],
                    "Country, assets inherited, estate documents, keep or sell plans, your residency status.")
         + sources("Income-tax Act, 1961 (sections 5, 49 and 56(2)(x)) and the corresponding provisions of the Income-tax Act, 2025; Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015; FEMA, 1999 (section 6(4)); Foreign Exchange Management (Overseas Investment) Rules, 2022 (Schedule III); site Schedule FA, foreign income, Form 67 and inheriting-from-India pages.")),
    ],
    faqs=[("Do I need to pay tax in India on an inheritance from abroad?", "No. India has no inheritance tax, and assets received by inheritance are excluded from the gift tax rule. Tax arises only on income the inherited assets earn and on gains when you sell them."),
          ("Can an Indian resident keep foreign assets inherited from a relative abroad?", "Yes. FEMA allows a person resident in India to hold foreign assets inherited from a person resident outside India, and the Overseas Investment Rules let a resident individual acquire foreign securities by inheritance without limit. It does not use the LRS limit."),
          ("Do I have to report inherited foreign assets in my income tax return?", "Yes, if you are a resident and ordinarily resident. Foreign assets go in Schedule FA and foreign income in Schedule FSI. Not reporting can lead to penalties under the Black Money Act."),
          ("Is foreign estate or inheritance tax creditable in India?", "Generally not. India's tax treaties cover income taxes, so estate or inheritance tax paid on the estate abroad is usually not available as a credit in India. Tax paid abroad on income from the assets can be claimed as foreign tax credit."),
          ("How do I bring inherited money from abroad to India?", "Through normal banking channels into your Indian bank account, keeping the probate or estate documents and bank advice as proof of the source of funds."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the country, the assets inherited, the estate documents, your plans to keep or sell, and your residency status. Or book a call directly.")],
    related=[("do-i-need-to-report-foreign-assets-itr-schedule-fa-who-must-file-penalty-2026.html", "Do I need to report foreign assets (Schedule FA)?"),
             ("foreign-income-tax-india-2026-taxable-for-residents-rnor-nri-schedule-fsi-fa-foreign-tax-credit.html", "Foreign income tax for residents, RNORs and NRIs"),
             ("form-67-foreign-tax-credit-india-2026.html", "Form 67 foreign tax credit"),
             ("inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html", "Inheriting from India while living abroad")],
    cta_h="Inherited money or assets from abroad?", cta_b=C,
    keywords="do i need to pay tax on inheritance from abroad, inheritance from abroad india tax, inherited foreign assets fema, inherit foreign shares indian resident, schedule fa inherited assets, foreign estate tax credit india, bring inheritance money to india",
    desc="Inheritance from abroad for Indian residents: no inheritance tax in India, outside section 56(2)(x); FEMA section 6(4) and OI Rules allow holding inherited foreign assets, no LRS use; Schedule FA / FSI reporting; tax on income and sale; foreign estate tax generally not creditable; bringing money through banks.",
    howto={"name": "How to handle an inheritance from abroad", "description": "Abroad first, then India.", "steps": [
        {"name": "Complete the estate abroad", "text": "Probate or equivalent; foreign estate tax if any."},
        {"name": "Decide keep or bring home", "text": "FEMA allows holding inherited foreign assets; move cash through banks."},
        {"name": "Report in your ITR", "text": "Schedule FA for assets, FSI for income, from the year you hold them."},
        {"name": "Tax income and gains", "text": "Indian tax on income and sale; claim foreign tax credit on income tax paid abroad."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MA complete")
