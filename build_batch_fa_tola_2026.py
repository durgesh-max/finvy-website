# -*- coding: utf-8 -*-
"""Batch FA (21 Nov 2026): Taxation and Other Laws (Amendment) Act, 2026 - what it changes for foreign companies,
funds and investors, with the electronics contract-manufacturing exemptions. Call-first page.
Gap: no site page mentioned this Act; a sweep on 'contract manufacturing in India' surfaced it.
Facts (checked 21 Nov 2026; India Briefing, 19 Aug 2026; KSMG summary citing Gazette Act No. 21 of 2026 dated
17 August 2026; PRS bill page; Income Tax Department FAQs on the Bill; Corpseed; Bar Bulletin):
- Presidential assent 17 August 2026; deemed in force from 1 April 2026 unless a provision says otherwise; amends the
  Income-tax Act, 2025, the Finance Act, 2026 and the Payment and Settlement Systems Act, 2007; replaces the Income-tax
  (Amendment) Ordinance, 2026 of 5 June 2026.
- FIIs and the Bank for International Settlements: nil tax on interest and capital gains from Indian government
  securities for income arising on or after 1 April 2026, subject to prescribed information (earlier 20% interest,
  30% short-term, 12.5% long-term per KSMG).
- Safe harbour for offshore funds with an Indian fund manager (Schedule I replaced): removed - minimum 25 members, 10%
  single-investor cap, INR 100 crore minimum corpus, 25% single-entity investment cap; kept - fund established outside
  India, non-resident, qualifying jurisdiction, resident Indians hold no more than 5% of corpus (tested 1 April and
  1 October, four months to cure; manager contribution up to INR 25 crore in first three years excluded), manager
  registered, not an employee or connected person, not entitled to more than 20% of profits, statement within 90 days
  of the tax year end.
- Electronics (Schedule IV): Sl. No. 13A - foreign company's income from providing capital goods, equipment and
  tooling to an Indian contract manufacturer of specified electronic goods, extended from tax year 2030-31 to 2040-41;
  Sl. No. 13G (new) - foreign company's income from storing components in a customs-bonded warehouse (section 65,
  Customs Act) and selling them to an Indian contract manufacturer, for income arising on or after 1 October 2026 and
  up to 31 March 2041, subject to prescribed information. Specified electronic goods: mobile phones, laptops,
  all-in-one PCs, tablets, servers and ultra-small form factor devices, sub-assemblies, hearables, wearables and
  accessories. Contract manufacturer = Indian company producing these for a foreign company in a customs-bonded area.
- Rough diamonds sold in notified special zones by foreign miners and connected sellers: exempt from 1 October 2026
  to 31 March 2041.
- Data centres: 'specified data centre' must be operated by an Indian company that owns or leases it, with other
  conditions to be prescribed; KSMG reports the foreign company no longer needs individual notification.
- Business trust SPVs: surcharge raised from 10% to 25% (KSMG; India Briefing presents 10% / 25%), with relief for
  unit holders on the related dividend.
- FDI policy: contract manufacturing in India counts as manufacturing, 100% under the automatic route, on principal-to-
  principal or principal-to-agent basis (Press Note 4 of 2019; DPIIT clarification)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "taxation-and-other-laws-amendment-act-2026-foreign-companies-electronics-contract-manufacturing-funds-fii"

C = contact("whether you are a foreign manufacturer or brand, an offshore fund, or an investor in Indian government bonds, and what you plan to do in India")
PAGES = [dict(
    slug=SLUG,
    title="Taxation and Other Laws (Amendment) Act, 2026: What It Changes for Foreign Companies - Electronics Contract Manufacturing, Offshore Funds and Bond Investors",
    em="what it does, in plain terms.",
    kicker="/ Foreign companies &middot; New law &middot; Contract manufacturing &middot; Updated 2026-11-21",
    lead=("The <strong>Taxation and Other Laws (Amendment) Act, 2026</strong> received assent on <strong>17 August 2026</strong> and mostly applies from 1 April 2026. It gives foreign businesses and investors five things. "
          "A foreign company that keeps components in an Indian <strong>customs-bonded warehouse</strong> and sells them to an Indian <strong>contract manufacturer of electronics</strong> pays <strong>no Indian income tax on that income</strong> from 1 October 2026 until 31 March 2041. "
          "The existing exemption for supplying <strong>capital goods, equipment and tooling</strong> to such a manufacturer now runs to tax year 2040-41. "
          "Foreign institutional investors pay <strong>no tax on Indian government bond interest and gains</strong> from 1 April 2026. "
          "The <strong>safe harbour for offshore funds managed from India</strong> has fewer conditions. Foreign sellers of rough diamonds in notified zones are exempt, and the data-centre exemption wording is tightened. "
          "Separately, foreign investment in <strong>contract manufacturing</strong> is allowed up to 100% without approval. Each exemption needs prescribed information to be filed, so the structure and paperwork matter."),
    sections=[
        ("/ What the Act changes", "For foreign companies, funds and investors.",
         table(["Who", "Change", "From / until"], [
             ["Foreign electronics brands and component suppliers", "Income from storing components in a customs-bonded warehouse and selling them to an Indian contract manufacturer is exempt", "Income from 1 October 2026 to 31 March 2041"],
             ["Foreign companies lending capital goods, equipment or tooling", "Existing exemption for supplying these to an Indian contract manufacturer of specified electronic goods extended", "Tax year 2030-31 extended to 2040-41"],
             ["Foreign institutional investors and the BIS", "Nil tax on interest and capital gains from Indian government securities", "Income from 1 April 2026"],
             ["Offshore funds with an Indian fund manager", "Safe harbour simplified: no minimum of 25 investors, no 10% single-investor cap, no INR 100 crore minimum corpus, no 25% single-entity cap; resident Indians limited to 5% of the corpus", "From 1 April 2026"],
             ["Foreign rough-diamond sellers", "Income from sales in notified special zones exempt", "1 October 2026 to 31 March 2041"],
             ["Foreign companies using Indian data centres", "The foreign company no longer needs to be individually notified; the data centre can be owned or leased by the Indian company operating it; further conditions to be prescribed", "From 1 April 2026"],
             ["REIT and InvIT structures", "Surcharge on a business trust&rsquo;s special purpose vehicle raised from 10% to 25%; unit holders exempt on the related dividend income", "From 1 April 2026"]])
         + "<p><strong>Specified electronic goods</strong> are mobile phones, laptops, all-in-one PCs, tablets, servers and ultra-small form factor devices, their sub-assemblies, and hearables, wearables and accessories. The contract manufacturer must be an Indian company producing them for the foreign company in a customs-bonded area.</p>"
         + call_box("Using the 2026 exemptions for our India manufacturing or investment", ["Whether your goods and structure fit the electronics exemptions",
                                                                                        "Bonded warehouse and in-bond manufacturing set-up with the contract manufacturer",
                                                                                        "Permanent establishment, transfer pricing and GST around the exemption",
                                                                                        "The information filings each exemption depends on",
                                                                                        "For funds: testing the 5% Indian-participation limit and manager conditions"],
                    "your products, the Indian manufacturer or fund manager involved, the planned flow of goods or money, and timelines.")),
        ("/ Contract manufacturing in India: how it fits together", "For foreign brands moving production.",
         ul("<strong>Foreign investment:</strong> contract manufacturing counts as manufacturing, so 100% foreign ownership is allowed without approval, whether the Indian manufacturer acts as principal or as your agent.",
            "<strong>Without an Indian entity:</strong> a foreign brand can buy finished goods from an Indian contract manufacturer and export them. Watch for a permanent establishment if your own people or stock in India go beyond purchasing; see the <a href=\"permanent-establishment-risk-checker-india-foreign-company-2026.html\">PE risk checker</a>.",
            "<strong>The new exemptions:</strong> for specified electronic goods, components you hold in a bonded warehouse and equipment you place with the manufacturer no longer create Indian income tax on that income, if the conditions and filings are met.",
            "<strong>Customs and GST:</strong> in-bond manufacturing defers duty on imported inputs; exports are zero-rated. Get the customs set-up reviewed with the manufacturer.",
            "<strong>Related-party pricing:</strong> if the manufacturer is your subsidiary, transfer pricing applies; see <a href=\"transfer-pricing-india-foreign-mnc.html\">transfer pricing for foreign groups</a>.",
            "<strong>Company tax for an Indian manufacturing subsidiary:</strong> 25.17%; the 15% rate is closed to new companies.",
            "<strong>Choosing the route:</strong> see <a href=\"china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html\">China plus one: moving sourcing or manufacturing to India</a> and the <a href=\"india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html\">entry structure chooser</a>.")
         + '<p>Related: <a href="foreign-cloud-companies-tax-holiday-indian-data-centres-2047.html">foreign cloud companies and Indian data centres</a> &middot; <a href="gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html">GIFT City</a> &middot; <a href="branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html">branch vs subsidiary calculator</a>.</p>'
         + sources("Taxation and Other Laws (Amendment) Act, 2026 (Act No. 21 of 2026, assent 17 August 2026), amending the Income-tax Act, 2025 (Schedules I and IV), the Finance Act, 2026 and the Payment and Settlement Systems Act, 2007, as summarised by India Briefing (19 August 2026), KSMG, PRS Legislative Research and the Income Tax Department's FAQs on the Bill; DPIIT Press Note 4 of 2019 and clarification on contract manufacturing. Rules prescribing the information to be furnished should be checked before relying on an exemption.")),
    ],
    faqs=[("What is the Taxation and Other Laws (Amendment) Act, 2026?", "A law that received assent on 17 August 2026 and mostly applies from 1 April 2026. It amends the Income-tax Act, 2025, the Finance Act, 2026 and the Payment and Settlement Systems Act, 2007, with exemptions for foreign investors, offshore funds and electronics manufacturing."),
          ("Is a foreign company taxed in India on components kept in a bonded warehouse?", "For specified electronic goods, income from storing components in a customs-bonded warehouse and selling them to an Indian contract manufacturer is exempt for income arising from 1 October 2026 until 31 March 2041, subject to prescribed information being furnished."),
          ("Can a foreign company use contract manufacturing in India without setting up there?", "Yes. It can buy from an Indian contract manufacturer, and foreign investment in contract manufacturing is also allowed up to 100% without approval. Permanent establishment risk depends on what the foreign company's own people and stock do in India."),
          ("Do foreign investors pay tax on Indian government bonds?", "Foreign institutional investors and the Bank for International Settlements pay no tax on interest or capital gains from Indian government securities for income arising on or after 1 April 2026, subject to prescribed information."),
          ("What changed in the safe harbour for offshore funds managed from India?", "Four conditions were removed: the minimum of 25 investors, the 10% single-investor cap, the INR 100 crore minimum corpus and the 25% single-entity investment cap. Resident Indians may still hold no more than 5% of the corpus, and the Indian manager must meet registration and independence conditions."),
          ("Can BQP help us use these exemptions?", "Yes. " + C)],
    related=[("china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html", "China plus one: moving to India"),
             ("permanent-establishment-risk-checker-india-foreign-company-2026.html", "PE risk checker"),
             ("foreign-cloud-companies-tax-holiday-indian-data-centres-2047.html", "Foreign cloud companies and Indian data centres")],
    cta_h="Planning electronics manufacturing or fund management in India?", cta_b=C,
    keywords="Taxation and Other Laws Amendment Act 2026, contract manufacturing India foreign company tax, bonded warehouse components exemption India 2041, electronics contract manufacturer foreign company exemption, FII government securities tax exemption India, offshore fund safe harbour India fund manager 2026",
    desc="Taxation and Other Laws (Amendment) Act, 2026 (assent 17 Aug 2026): foreign companies exempt on components sold from bonded warehouses to Indian electronics contract manufacturers (1 Oct 2026 to 2041), tooling exemption to 2040-41, nil tax for FIIs on government bonds, simpler fund safe harbour.",
    howto={"name": "How a foreign electronics brand uses the 2026 contract-manufacturing exemptions", "description": "From structure to filings.", "steps": [
        {"name": "Check the goods", "text": "Confirm they are specified electronic goods or sub-assemblies."},
        {"name": "Choose the manufacturer and bonded set-up", "text": "An Indian company manufacturing in a customs-bonded area."},
        {"name": "Structure the flows", "text": "Components through a bonded warehouse; equipment and tooling placed with the manufacturer."},
        {"name": "Review PE, transfer pricing and GST", "text": "Keep activities within the exemption and price related-party dealings at arm's length."},
        {"name": "File the prescribed information", "text": "Each exemption depends on it."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FA complete")
