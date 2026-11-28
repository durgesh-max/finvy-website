# -*- coding: utf-8 -*-
"""Batch MJ (29 Nov 2026): REIT and InvIT taxation in India - what REITs and InvITs are, how each component of a distribution
is taxed (interest, dividend, rental income, repayment of debt), TDS under section 194LBA, capital gains on listed units, and
NRI points.
Demand: sweep ac270 (29 Nov 2026), all 7 markets: 'reit invit in india' and 'what is invit and reit' (coverage 0.00),
'difference between invit and reit' (0.25), 'is income from reit taxable', 'reit invit full form' (0.50). No page on the site.
Investors and NRIs holding REIT / InvIT units need help reporting mixed distributions. User steer 26 Nov 2026: more calls.
Facts (verified by web search 29 Nov 2026 - Income Tax Department section 194LBA page, ClearTax / PrimeInvestor / Finnovate
explainers, Business Standard and EY Budget 2024 notes; matched to the site's capital gains pages): REITs hold rent-yielding
real estate and InvITs hold infrastructure assets, both regulated by SEBI (2014 regulations) and required to distribute most of
their net distributable cash flows; distributions are passed through by component: interest from the SPV taxable at slab rates;
dividend from an SPV exempt in the unitholder's hands unless the SPV has opted for the concessional company tax regime (section
115BAA), in which case it is taxable; rental income from REIT-held property taxable at slab rates; amounts distributed as
repayment of debt / capital taxable as other income since FY 2023-24 (Finance Act 2023), subject to a deduction linked to the
cost of the units; TDS under section 194LBA - 10% for residents on taxable components, 5% on interest for non-residents (or the
treaty rate if lower); listed units are long-term after 12 months from 23 July 2024 (unlisted after 24 months), long-term gains
taxed at 12.5% without indexation and short-term gains on listed units at 20% where STT is paid. The 112A annual exemption point
is not stated (sources conflict). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 29 November 2026."
SLUG = "reit-invit-taxation-india-distribution-interest-dividend-repayment-of-debt-194lba-capital-gains-nri-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the REITs or InvITs you hold, the distribution "
     "statements showing each component, your purchase and sale dates, whether you are resident or NRI, and the TDS shown in "
     "your AIS or Form 26AS. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="REIT and InvIT Taxation in India (2026): What They Are, How Interest, Dividend, Rent and Repayment of Debt Are Taxed, TDS Under 194LBA and Capital Gains on Units",
    em="each part of the payout is taxed differently.",
    kicker="/ Resident and NRI investors in REITs and InvITs &middot; Business trust distributions &middot; Updated 2026-11-29",
    lead=("<strong>A REIT owns rent-yielding real estate and an InvIT owns infrastructure such as roads or power lines; both pass most of their cash to unitholders. "
          "That payout is split into components - interest and rent are taxed at your slab rate, dividend is exempt unless the underlying company chose the concessional tax regime, and repayment of debt has been taxable since FY 2023-24. "
          "Listed units held more than 12 months give long-term gains at 12.5%; shorter holdings are taxed at 20%.</strong>"),
    sections=[
        ("/ How a distribution is taxed", "Component by component.",
         table(["Component", "Tax in the unitholder's hands"], [
             ["Interest from the SPV", "Taxable at slab rates"],
             ["Dividend from the SPV", "Exempt, unless the SPV opted for the concessional company tax regime (section 115BAA) - then taxable"],
             ["Rental income (REIT-held property)", "Taxable at slab rates"],
             ["Repayment of debt / capital", "Taxable as other income since FY 2023-24, after a deduction linked to the cost of the units"],
             ["TDS (section 194LBA)", "10% for residents on taxable components; 5% on interest for non-residents, or the treaty rate if lower"]])
         + ul("<strong>Read the statement:</strong> each distribution notice shows the split - use it, not the bank credit, when filing.",
              "<strong>Check the AIS:</strong> match the TDS shown against each component before you file.")),
        ("/ REIT vs InvIT, and selling units", "Capital gains and NRI points.",
         ul("<strong>REIT:</strong> holds completed, rent-yielding real estate such as offices and malls; income is mostly rent and interest from SPVs.",
            "<strong>InvIT:</strong> holds infrastructure such as roads, power transmission and pipelines; income is mostly interest and repayment of debt from SPVs.",
            "<strong>Holding period:</strong> listed units are long-term after 12 months (unlisted after 24 months) for transfers from 23 July 2024.",
            "<strong>Rates:</strong> long-term gains at 12.5% without indexation; short-term gains on listed units at 20% where securities transaction tax is paid.",
            "<strong>NRIs:</strong> TDS is deducted on distributions and gains; claim treaty relief with a tax residency certificate and Form 10F, and file a return to recover any excess.")
         + call_box("REIT and InvIT income", ["Splitting distributions correctly in the ITR",
                                              "Repayment of debt and cost tracking",
                                              "Capital gains on sale of units",
                                              "NRI TDS and treaty relief",
                                              "AIS and Form 26AS reconciliation"],
                    "Holdings, distribution statements, purchase and sale dates, residency, TDS in AIS.")
         + sources("Income-tax Act, 1961 (sections 10(23FD), 56, 111A, 112A, 115UA and 194LBA) and the corresponding provisions of the Income-tax Act, 2025; Finance Act 2023 and Finance (No. 2) Act 2024; SEBI REIT and InvIT Regulations, 2014; Income Tax Department guidance on section 194LBA; site capital gains, mutual fund and NRI share tax pages.")),
    ],
    faqs=[("What is the difference between a REIT and an InvIT?", "A REIT (real estate investment trust) owns rent-yielding real estate such as offices and malls. An InvIT (infrastructure investment trust) owns infrastructure such as roads, power transmission lines and pipelines. Both are SEBI-regulated trusts listed on stock exchanges that distribute most of their cash flows to unitholders."),
          ("Is income from a REIT taxable?", "Partly. Interest and rental income are taxable at your slab rate; dividend is exempt unless the underlying company opted for the concessional tax regime; and repayment of debt has been taxable as other income since FY 2023-24. The distribution statement shows the split."),
          ("How much TDS is deducted on REIT and InvIT distributions?", "Under section 194LBA, 10% for resident unitholders on taxable components, and 5% on interest for non-residents or the treaty rate if lower. The TDS is credited against your final tax."),
          ("How are capital gains on REIT units taxed?", "Listed units held more than 12 months are long-term and taxed at 12.5% without indexation; listed units sold within 12 months are taxed at 20% where securities transaction tax is paid. Unlisted units need 24 months to be long-term."),
          ("Can NRIs invest in REITs and InvITs?", "Yes. TDS is deducted on distributions and capital gains, and NRIs can claim treaty relief with a tax residency certificate and Form 10F and file an Indian return to claim any refund."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your holdings, distribution statements, purchase and sale dates, residency and the TDS in your AIS. Or book a call directly.")],
    related=[("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Capital gains tax in India"),
             ("mutual-fund-taxation-india-2026-equity-debt-hybrid-ltcg-12-5-stcg-20-examples.html", "Mutual fund taxation"),
             ("nri-capital-gains-tax-on-indian-shares-ltcg-12-5-stcg-20-tds-refund-2026.html", "NRI capital gains on Indian shares"),
             ("tax-on-gold-india-2026-jewellery-digital-gold-etf-sovereign-gold-bond-ltcg-12-5-percent.html", "Tax on gold and SGBs")],
    cta_h="Holding REIT or InvIT units?", cta_b=C,
    keywords="reit invit taxation india, what is invit and reit, difference between invit and reit, is income from reit taxable, reit dividend tax india, invit interest tax, 194lba tds, reit capital gains tax, reit invit full form, reit for nri",
    desc="REIT and InvIT taxation in India: interest and rent at slab rates, dividend exempt unless the SPV chose section 115BAA, repayment of debt taxable since FY 2023-24, TDS under 194LBA (10% residents, 5% interest for NRIs), and 12.5% LTCG / 20% STCG on listed units.",
    howto={"name": "How to report REIT and InvIT income", "description": "Split, match, report.", "steps": [
        {"name": "Get the statements", "text": "Download each distribution's component split."},
        {"name": "Classify each part", "text": "Interest, dividend (exempt or taxable), rent, repayment of debt."},
        {"name": "Match TDS", "text": "Reconcile with the AIS and Form 26AS."},
        {"name": "Report sales", "text": "Holding period, 12.5% LTCG or 20% STCG, and cost adjustments."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MJ complete")
