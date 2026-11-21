# -*- coding: utf-8 -*-
"""Batch FF (21 Nov 2026): Indirect transfer tax in India - when the sale of a foreign holding company is taxed in India.
Call-first page for foreign groups, funds and founders with offshore holding structures.
Demand: sweeps 21 Nov 2026 (ac38, ac39), all 7 markets: "indirect transfer rules india", "indirect transfer provisions
in india", "india indirect transfer tax rules", "india indirect transfer tax rate", "india indirect share transfer tax".
Site mentioned indirect transfers in one M&A FAQ only.
Facts (checked 21 Nov 2026):
- Section 9(1)(i) of the Income-tax Act, 1961 with Explanations 5, 6 and 7 (Finance Act 2012 and 2015), now section 9(10)
  of the Income-tax Act, 2025 (TaxGuru, Taxmann and other 2026 commentary): a share or interest in a foreign company or
  entity is deemed situated in India if it derives its value substantially from assets located in India - Indian assets
  above INR 10 crore AND at least 50% of the value of all assets, at fair market value without deducting liabilities, on
  the specified date (end of the last accounting period, or the transfer date if book value of assets has risen by 15%
  or more). Only the gain reasonably attributable to Indian assets is taxed (formerly Rule 11UC formula).
- Small shareholder exemption: transferor, with associated enterprises, holds no right of management or control and not
  more than 5% of voting power, share capital or interest at any time in the 12 months before the transfer.
- Category I foreign portfolio investors' investors are outside the rule. Foreign amalgamations and demergers are exempt
  on conditions. Dividends declared by a foreign company outside India are not covered (CBDT Circular 4/2015).
- Taxation Laws (Amendment) Act, 2021 withdrew the rule for transfers before 28 May 2012.
- Reporting by the Indian concern: formerly section 285A, Rule 114DB and Form 49D - within 90 days from the end of the
  financial year of the transfer, or within 90 days of the transaction where management or control of the Indian
  concern is transferred; penalty 2% of the transaction value in that case, INR 5 lakh otherwise (formerly section
  271GA). Reported as section 506 and Form 163 under the 2025 Act and 2026 Rules (secondary commentary).
- Patron Accounting guide (updated 6 April 2026) used as a cross-check on the tests and exemptions."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "indirect-transfer-tax-india-sale-of-foreign-holding-company-shares-50-percent-inr-10-crore-rules-2026"
STDS = "tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026.html"

C = contact("the structure (which foreign company is being sold and what it owns in India), the seller's country and percentage holding, the deal value and the expected closing date")
PAGES = [dict(
    slug=SLUG,
    title="Indirect Transfer Tax in India (2026): When Selling a Foreign Holding Company Is Taxed in India - the 50% and INR 10 Crore Tests, Exemptions and What Buyers Must Withhold",
    em="offshore share sales with Indian value underneath.",
    kicker="/ Foreign companies &middot; M&amp;A &middot; Capital gains &middot; Updated 2026-11-21",
    lead=("<strong>India can tax the sale of shares in a foreign company if those shares get most of their value from assets in India.</strong> "
          "The rule applies when the Indian assets are worth more than <strong>INR 10 crore</strong> and make up <strong>at least 50%</strong> of the foreign company&rsquo;s total assets. "
          "Only the part of the gain that relates to the Indian assets is taxed, at India&rsquo;s capital gains rates: <strong>12.5%</strong> for holdings over 24 months, plus surcharge and cess. "
          "<strong>Small shareholders are outside the rule</strong>: those with no more than 5% and no management or control in the previous 12 months. "
          "The buyer, even a foreign one, must withhold the Indian tax, and the Indian company underneath has its own reporting duty. "
          "A tax treaty can remove the charge in some cases. This is the rule that followed the Vodafone case; it applies to transfers from 28 May 2012."),
    sections=[
        ("/ The tests", "Is an offshore sale taxable in India?",
         table(["Step", "Test", "Result"], [
             ["1", "Is the company being sold outside India, and does it own Indian assets directly or through other companies?", "If not, the rule does not apply"],
             ["2", "Are the Indian assets worth more than INR 10 crore at fair market value?", "If not, outside the rule"],
             ["3", "Are the Indian assets at least 50% of the value of all its assets?", "If not, outside the rule"],
             ["4", "Does the seller, with its associated enterprises, hold more than 5% or have management or control in the last 12 months?", "If neither, the small shareholder exemption applies"],
             ["5", "Is an exemption available: investor in a Category I foreign portfolio investor, qualifying foreign merger or demerger, or a tax treaty?", "If yes, no Indian tax or reduced tax"],
             ["6", "If still taxable, how much of the gain relates to India?", "Gain &times; value of Indian assets &divide; value of all assets"]])
         + '<p>Values are taken at fair market value without deducting liabilities, normally at the end of the last accounting period before the sale. If the book value of assets has grown by 15% or more since then, the date of the sale is used.</p>'
         + call_box("Sale or restructuring of a foreign holding company with an Indian business", ["Whether the 50% and INR 10 crore tests are met on your numbers",
                                                                                                  "How much of the gain India would tax, and at what rate",
                                                                                                  "Treaty position for the seller&rsquo;s country",
                                                                                                  "What the buyer must withhold and how to document it",
                                                                                                  "The Indian company&rsquo;s reporting and the valuation report"],
                    "a structure chart, the latest balance sheets of the foreign company and the Indian company, the seller&rsquo;s country and stake, and the deal timetable.")),
        ("/ Who has to do what", "Seller, buyer and the Indian company.",
         ul("<strong>Seller:</strong> pays capital gains tax on the India-related part of the gain, gets an accountant&rsquo;s valuation report under the prescribed method, and files an Indian tax return. A PAN is needed.",
            "<strong>Buyer:</strong> withholds Indian tax on that gain before paying, even if both buyer and seller are outside India. See <a href=\"" + STDS + "\">TDS on buying shares from a non-resident</a>.",
            "<strong>Indian company:</strong> reports the transfer and the group shareholding to the tax department: within 90 days of the deal if control of the Indian company changes, otherwise within 90 days after the financial year ends. The old form was Form 49D; it is reported as Form 163 under the 2026 rules.",
            "<strong>Penalty on the Indian company:</strong> 2% of the transaction value if control changed and the report was not filed; INR 5 lakh in other cases.")),
        ("/ Practical points", "What deal teams should check early.",
         ul("<strong>Rates:</strong> 12.5% on long-term gains (held over 24 months); short-term gains at normal rates, 35% for a foreign company; plus surcharge and 4% cess.",
            "<strong>Treaties:</strong> several Indian treaties give the right to tax shares of a non-Indian company only to the seller&rsquo;s home country, which can switch the Indian charge off. Others, including the US and UK treaties, let India tax under its own law. The seller needs a tax residency certificate and must pass anti-abuse tests.",
            "<strong>Group restructurings:</strong> an internal transfer is still a transfer. Foreign mergers and demergers are exempt only if their conditions are met, so check before moving a holding company within the group.",
            "<strong>Funds:</strong> investors in Category I foreign portfolio investors are outside the rule. Private equity and venture funds exiting through an offshore holding company are not automatically exempt.",
            "<strong>Founders and investors living outside India:</strong> selling shares of a Delaware or Singapore parent whose value sits in an Indian subsidiary can be taxed in India, unless the 5% exemption or a treaty applies. Founders resident in India are taxed here on the sale in any case. See <a href=\"triangular-structure-indian-founders-us-parent-indian-subsidiary-odi-schedule-iii-2026.html\">US parent with an Indian subsidiary</a>.",
            "<strong>Dividends:</strong> a dividend paid by the foreign company outside India is not caught by this rule.",
            "<strong>Old transactions:</strong> transfers before 28 May 2012 are no longer taxed under this rule, following the 2021 amendment.",
            "<strong>Sale agreements:</strong> the price mechanics, the withholding clause, the tax indemnity and who obtains the valuation should be settled before signing.")
         + '<p>Related: <a href="due-diligence-indian-company-foreign-buyer.html">due diligence on an Indian company</a> &middot; <a href="ma-transactions.html">M&amp;A transactions</a> &middot; <a href="india-mauritius-tax-treaty-dtaa.html">India-Mauritius treaty</a> &middot; <a href="india-singapore-tax-treaty-dtaa.html">India-Singapore treaty</a> &middot; <a href="foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026.html">advisor for foreign companies in India</a>.</p>'
         + sources("Income-tax Act, 1961, section 9(1)(i), Explanations 5, 6 and 7, and sections 47(viab), 47(vicc), 285A and 271GA; the corresponding provisions of the Income-tax Act, 2025 (section 9(10) and section 506, per 2026 commentary by TaxGuru and Taxmann); Income-tax Rules on fair market value, attribution and reporting (formerly Rules 11UB, 11UC and 114DB); CBDT Circular No. 4/2015 on dividends; Taxation Laws (Amendment) Act, 2021; Patron Accounting guide updated 6 April 2026. Checked 21 November 2026. Section and form numbers under the new Act should be confirmed against the official text before filing.")),
    ],
    faqs=[("What is indirect transfer tax in India?", "India taxes the gain on a sale of shares or an interest in a foreign company or entity if the shares derive their value substantially from assets located in India. Only the part of the gain attributable to the Indian assets is taxed."),
          ("When does a foreign company derive substantial value from Indian assets?", "When the Indian assets are worth more than INR 10 crore and represent at least 50% of the value of all the assets of the foreign company, measured at fair market value without deducting liabilities."),
          ("What is the indirect transfer tax rate in India?", "India's capital gains rates apply to the India-related part of the gain: 12.5% for long-term gains (held over 24 months), and normal rates for short-term gains, 35% for a foreign company, plus surcharge and 4% cess."),
          ("Who is exempt from India's indirect transfer rules?", "A seller who, with associated enterprises, holds no more than 5% and has no right of management or control in the 12 months before the transfer; investors in Category I foreign portfolio investors; qualifying foreign mergers and demergers; and sellers protected by a tax treaty."),
          ("Does the buyer have to withhold tax on an indirect transfer?", "Yes. The buyer must deduct Indian tax on the taxable gain before paying the seller, even when both are outside India."),
          ("Does the Indian company have to report an indirect transfer?", "Yes. The Indian company through which the foreign company holds its Indian assets must report the transfer: within 90 days of the deal if control of the Indian company changes, otherwise within 90 days after the end of the financial year."),
          ("Can BQP advise on an indirect transfer?", "Yes. " + C)],
    related=[(STDS, "TDS on buying shares from a non-resident"),
             ("due-diligence-indian-company-foreign-buyer.html", "Due diligence on an Indian company"),
             ("ma-transactions.html", "M&A transactions")],
    cta_h="Selling or restructuring a foreign company that owns an Indian business?", cta_b=C,
    keywords="indirect transfer tax India, indirect transfer rules India, indirect transfer provisions in India, India indirect transfer tax rate, section 9(1)(i) Explanation 5, substantial value 50% INR 10 crore, small shareholder exemption 5%, Vodafone tax India, Form 49D Form 163",
    desc="Indirect transfer tax in India (2026): a sale of foreign company shares is taxed in India if Indian assets exceed INR 10 crore and are at least 50% of total assets. Only the India-related gain is taxed (12.5% long-term). 5% small shareholder exemption, treaties, buyer withholding, reporting.",
    howto={"name": "How to check if an offshore share sale is taxed in India", "description": "Indirect transfer tests.", "steps": [
        {"name": "Map the structure", "text": "Which foreign company is sold and what it owns in India."},
        {"name": "Value the assets", "text": "Indian assets above INR 10 crore and at least 50% of all assets at fair market value."},
        {"name": "Check exemptions", "text": "5% small shareholder rule, Category I FPI investors, mergers and treaties."},
        {"name": "Attribute the gain", "text": "Gain multiplied by Indian asset value over total asset value."},
        {"name": "Withhold and report", "text": "Buyer withholds; seller files a return; the Indian company reports the transfer."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FF complete")
