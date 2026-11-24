# -*- coding: utf-8 -*-
"""Batch GG (24 Nov 2026): angel tax abolished - effective date, which year, what it means for startups and investors,
and what still applies (FEMA pricing, section 56(2)(x) on investors, Companies Act valuation). Call-first page.
Demand: sweep ac56 (24 Nov 2026), all 7 markets: "angel tax abolished effective date", "angel tax abolished in which
year", "angel tax abolished upsc". Site mentioned the abolition in passing but had no page.
Facts (checked 24 Nov 2026): Finance (No. 2) Act, 2024 omitted section 56(2)(viib) of the Income-tax Act, 1961 (tax on
share premium above fair market value received by closely held companies) with effect from 1 April 2025, i.e. from
assessment year 2025-26, covering share issues in financial year 2024-25 onwards; announced in the Union Budget of
23 July 2024 for all classes of investors. The Income-tax Act, 2025 has no equivalent. FEMA pricing guidelines for issue
of shares to non-residents (not less than fair value) still apply; section 56(2)(x) still taxes a recipient of shares
for less than fair market value; Companies Act preferential allotment needs a registered valuer's report."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "angel-tax-abolished-effective-date-which-year-startups-section-56-2-viib-2026"

C = contact("your company's stage, the round you are raising, the investors' residence, the price per share and any valuation report you have")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Angel Tax Abolished (2026): Effective Date, Which Year, and What Still Applies to Startup Fundraising",
    em="gone for share premium, but valuation still matters.",
    kicker="/ Startups &middot; Fundraising &middot; Updated 2026-11-24",
    lead=("<strong>Angel tax was abolished by the Finance (No. 2) Act, 2024 for all investors, resident and foreign: section 56(2)(viib) was omitted with effect from 1 April 2025, so it does not apply to shares issued in financial year 2024-25 (assessment year 2025-26) or later.</strong> "
          "It was announced in the Union Budget of 23 July 2024. The new Income-tax Act, 2025, in force from 1 April 2026, has no equivalent provision. "
          "A startup raising at a premium no longer pays tax on the premium above fair market value. "
          "But valuation still matters: <strong>foreign investors</strong> must pay at least fair value under FEMA, an <strong>investor</strong> who gets shares below fair market value can be taxed on the difference, and the Companies Act still needs a registered valuer&rsquo;s report for a preferential allotment."),
    sections=[
        ("/ Quick answers", "The short version.",
         ul("<strong>When was angel tax abolished?</strong> By the Finance (No. 2) Act, 2024, announced in the Budget on 23 July 2024; section 56(2)(viib) was omitted from 1 April 2025.",
            "<strong>From which year does it not apply?</strong> Assessment year 2025-26 onwards, which covers shares issued from 1 April 2024 (financial year 2024-25).",
            "<strong>Was it abolished for all investors?</strong> Yes, resident and non-resident investors alike, not only DPIIT-recognised startups (which already had an exemption).",
            "<strong>What about old cases?</strong> Share issues up to financial year 2023-24 remain under the old law, so notices for those years can still arise; DPIIT-recognised startups could claim the earlier exemption.",
            "<strong>Do I still need a valuation report?</strong> Usually yes: for FEMA pricing when foreign investors come in, for the Companies Act preferential allotment, and to protect investors from tax on a below-value issue.")),
        ("/ What changed and what did not", "Before and after.",
         table(["Point", "Up to FY 2023-24", "From FY 2024-25"], [
             ["Tax on premium above FMV received by the company (section 56(2)(viib))", "Taxable as the company's income, unless exempt (DPIIT startups, notified investors)", "Abolished"],
             ["Investor receiving shares below fair market value (section 56(2)(x))", "Taxable on the difference", "Still taxable on the difference"],
             ["Foreign investor price (FEMA)", "At least fair value", "At least fair value"],
             ["Companies Act preferential allotment", "Registered valuer's report", "Registered valuer's report"],
             ["Valuation methods (Rule 11UA)", "Used for 56(2)(viib) and 56(2)(x)", "Still used for 56(2)(x) and other purposes"]])
         + '<p>Instruments for early rounds: see ' + L("convertible-instruments-india-ccd-ccps.html", "CCDs and CCPS") + '. Foreign investors: ' + L("raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026.html", "raising from foreign and NRI investors") + '.</p>'),
        ("/ What founders should still do", "Clean rounds without angel tax.",
         ul("<strong>Get a valuation</strong> from a registered valuer (and a SEBI-registered merchant banker or CA where FEMA requires) before issuing shares to foreign investors.",
            "<strong>Price foreign rounds at or above fair value</strong> and file FC-GPR within 30 days of allotment.",
            "<strong>Protect resident investors</strong> by not issuing below fair market value.",
            "<strong>Keep old-year files ready</strong> if you raised money up to FY 2023-24 without a DPIIT exemption.",
            "<strong>Plan ESOP and secondary pricing</strong> with the same valuation discipline; see " + L("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback tax") + ".")
         + call_box("startup fundraising after angel tax", ["Valuation for FEMA and the Companies Act",
                                                             "Investor tax on below-value issues",
                                                             "FC-GPR and foreign investor pricing",
                                                             "Old-year angel tax notices",
                                                             "CCD, CCPS and SAFE-style instruments"],
                    "your round details, investors' residence and any valuation report.")
         + sources("Finance (No. 2) Act, 2024, omitting section 56(2)(viib) of the Income-tax Act, 1961 with effect from 1 April 2025; Union Budget speech, 23 July 2024; Income-tax Act, 2025; Income-tax Act, 1961, section 56(2)(x) and Rule 11UA (carried into the 2025 Act and Rules, 2026); FEMA (Non-debt Instruments) Rules, 2019 pricing guidelines; Companies Act, 2013, section 62(1)(c) and the Companies (Share Capital and Debentures) Rules. Checked 24 November 2026.")),
    ],
    faqs=[("When was angel tax abolished in India?", "By the Finance (No. 2) Act, 2024, announced in the Union Budget on 23 July 2024. Section 56(2)(viib) was omitted with effect from 1 April 2025, so it does not apply from assessment year 2025-26, covering shares issued from financial year 2024-25."),
          ("Angel tax was abolished in which year?", "In 2024: the Finance (No. 2) Act, 2024 removed it, effective from assessment year 2025-26 (financial year 2024-25 onwards)."),
          ("Was angel tax abolished for foreign investors too?", "Yes. The abolition applies to all investors, resident and non-resident. Foreign investors must still pay at least fair value under FEMA pricing rules."),
          ("Do startups still need a valuation report after angel tax was abolished?", "Usually yes: for FEMA pricing on foreign investment, for a preferential allotment under the Companies Act, and to avoid tax for investors who receive shares below fair market value under section 56(2)(x)."),
          ("Can old angel tax cases still be raised?", "For share issues up to financial year 2023-24, the old provision still applies, so assessments for those years can raise it, subject to time limits and exemptions such as the DPIIT startup exemption."),
          ("Can BQP help with fundraising compliance?", "Yes. " + C)],
    related=[("convertible-instruments-india-ccd-ccps.html", "CCDs and CCPS"),
             ("raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026.html", "Raising from foreign and NRI investors"),
             ("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "Startup tax holiday (section 140)"),
             ("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback taxation"),
             ("buy-sell-unlisted-pre-ipo-shares-india-legal-sebi-caution-tax-nri-fema-2026.html", "Buying or selling unlisted shares")],
    cta_h="Raising a round?", cta_b=C,
    keywords="angel tax abolished, angel tax abolished effective date, angel tax abolished in which year, section 56(2)(viib) omitted, angel tax startup India 2026, angel tax foreign investors, valuation report startup India",
    desc="Angel tax abolished: Finance (No. 2) Act, 2024 omitted section 56(2)(viib) from 1 April 2025, so it does not apply from AY 2025-26 (FY 2024-25 share issues) for any investor. What still applies: FEMA fair value pricing, section 56(2)(x) for investors, Companies Act valuation.",
    howto={"name": "How to price a startup round after angel tax was abolished", "description": "Steps that still apply.", "steps": [
        {"name": "Get a valuation report", "text": "Registered valuer, and the FEMA-required valuer for foreign investors."},
        {"name": "Price at or above fair value for foreign investors", "text": "FEMA pricing guidelines."},
        {"name": "Avoid below-value issues to residents", "text": "Section 56(2)(x) taxes the investor on the shortfall."},
        {"name": "Complete Companies Act steps", "text": "Board and shareholder approvals, private placement filings."},
        {"name": "Report foreign investment", "text": "FC-GPR within 30 days of allotment."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GG complete")
