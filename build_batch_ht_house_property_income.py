# -*- coding: utf-8 -*-
"""Batch HT (25 Nov 2026): income from house property - annual value, municipal taxes, 30% standard deduction, interest
on borrowed capital (self-occupied up to Rs 2 lakh in the old regime; let-out without ceiling), new regime treatment (no
self-occupied interest; let-out loss not set off against other income), old-regime loss set-off (Rs 2 lakh, carry forward),
pre-construction interest, two self-occupied houses, NRIs; section 24 of the 1961 Act now section 22 of the 2025 Act.
Demand: sweep ac101 (25 Nov 2026), all 7 markets: "house property income calculation", "house property income tax problems
and solutions", "house property income deductions".
Facts (checked 25 Nov 2026): Income Tax Department section 22 (2025 Act) pages; CAclubindia 'Changes in income from house
property from April 2026'; Business Today (July and August 2025) on new regime and the new Act; ClearTax and Motilal Oswal
section 24 guides; Taxmann / TMI notes. Old-regime set-off limit, carry forward and two self-occupied houses from settled
law under the 1961 Act."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "income-from-house-property-calculation-deductions-30-percent-home-loan-interest-new-regime-2026"

C = contact("whether the property is self-occupied or let out, the rent, municipal taxes, home loan interest, the tax regime you use, and whether you are resident or NRI")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Income From House Property (2026): Calculation, 30% Deduction, Home Loan Interest, New vs Old Regime and Loss Set-Off",
    em="rent, minus taxes, minus 30%, minus interest.",
    kicker="/ Property owners, landlords and NRIs &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Income from house property is worked out as annual value (broadly the rent, or expected rent) minus municipal taxes paid, minus a flat 30% standard deduction, minus interest on a home loan.</strong> "
          "For a let-out property the interest has no ceiling in either regime, but under the new regime a loss from house property cannot be set off against salary or other income. "
          "For a self-occupied home the annual value is nil and, only under the old regime, interest up to &#8377;2 lakh a year is deductible. "
          "These deductions were in section 24 of the 1961 Act and are in section 22 of the Income-tax Act, 2025 from tax year 2026-27."),
    sections=[
        ("/ Quick answers", "What owners search for.",
         ul("<strong>How is house property income calculated?</strong> Gross annual value, less municipal taxes actually paid, gives net annual value; deduct 30% of that and the interest on borrowed capital.",
            "<strong>What is the 30% deduction?</strong> A flat standard deduction on net annual value for let-out (and deemed let-out) property, whatever you actually spend on repairs. It does not apply to a self-occupied home with nil annual value.",
            "<strong>How much home loan interest can I claim?</strong> Self-occupied: up to &#8377;2 lakh a year, old regime only. Let-out: the full interest in either regime, subject to the loss rules below.",
            "<strong>Can I set off a house property loss?</strong> Old regime: up to &#8377;2 lakh a year against other income, the rest carried forward for eight years against house property income. New regime: not against other income.",
            "<strong>What about interest before construction finished?</strong> It is deducted in five equal instalments starting from the year the construction is completed, within the limits above.",
            "<strong>Two homes, both self-occupied?</strong> Up to two houses can be treated as self-occupied with nil annual value; a third is treated as deemed let out.")),
        ("/ Worked calculation", "One let-out flat, tax year 2026-27.",
         table(["Step", "Amount"], [
             ["Rent received for the year (gross annual value)", "&#8377;3,60,000"],
             ["Less municipal tax paid", "&#8377;20,000"],
             ["Net annual value", "&#8377;3,40,000"],
             ["Less 30% standard deduction", "&#8377;1,02,000"],
             ["Less home loan interest", "&#8377;3,00,000"],
             ["Income (loss) from house property", "(&#8377;62,000)"]])
         + '<p>Old regime: the &#8377;62,000 loss can reduce salary or other income. New regime: it cannot be set off against other income. Figures are hypothetical.</p>'),
        ("/ Old vs new regime", "What changes for property owners.",
         table(["Item", "Old regime", "New regime"], [
             ["30% standard deduction on let-out property", "Yes", "Yes"],
             ["Interest on let-out property", "Full", "Full"],
             ["Interest on self-occupied home", "Up to &#8377;2 lakh", "Not allowed"],
             ["House property loss against salary or other income", "Up to &#8377;2 lakh a year", "Not allowed"],
             ["Principal repayment (section 80C)", "Within the 80C limit", "Not allowed"]])
         + ul("<strong>Joint owners</strong> each claim their share of income and interest, with separate limits.",
              "<strong>NRIs</strong> are taxed on Indian rent the same way; the tenant deducts tax and the NRI can claim refunds in the return; see " + L("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "NRI rental income and TDS") + " and " + L("nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html", "the NRI rent refund calculator") + ".",
              "<strong>Tenants</strong>: see " + L("hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html", "HRA exemption") + " and " + L("tds-on-rent-limit-fy-2026-27-section-393-194ib-194i-194ia-property-purchase-1-percent-nri-landlord.html", "TDS on rent") + ".")
         + call_box("House property income", ["Annual value and deductions",
                                              "Home loan interest and pre-construction interest",
                                              "Old vs new regime for property owners",
                                              "Loss set-off and carry forward",
                                              "NRI rental income and refunds"],
                    "the property, rent, loan and regime.")
         + sources("Income-tax Act, 1961, sections 22 to 27 and 71(3A); Income-tax Act, 2025, section 22 (Income Tax Department section pages); CAclubindia, changes in income from house property from April 2026; Business Today (July and August 2025); ClearTax and Motilal Oswal section 24 guides. Checked 25 November 2026.")),
    ],
    faqs=[("How is income from house property calculated?", "Take the gross annual value (actual or expected rent), deduct municipal taxes paid to get the net annual value, then deduct a flat 30% of the net annual value and the interest on any home loan. The result can be income or a loss."),
          ("Is home loan interest deductible in the new tax regime?", "For a let-out property, yes, in full, but a resulting loss cannot be set off against salary or other income. For a self-occupied home, interest is not deductible in the new regime; up to Rs 2 lakh is allowed only in the old regime."),
          ("What is the 30% standard deduction on house property?", "A flat deduction of 30% of the net annual value of a let-out or deemed let-out property, allowed regardless of actual repair costs. It does not apply to a self-occupied house with nil annual value."),
          ("How much house property loss can be set off?", "Under the old regime, up to Rs 2 lakh a year against other income, with the balance carried forward for eight years against house property income. Under the new regime, a house property loss cannot be set off against other income."),
          ("Which section covers house property deductions now?", "Section 24 of the Income-tax Act, 1961 for FY 2025-26 and earlier; from tax year 2026-27, section 22 of the Income-tax Act, 2025."),
          ("Can BQP compute my house property income?", "Yes. CA Durgesh Chavda can work out rent, deductions and interest, compare regimes and handle NRI rental tax and refunds. " + C)],
    related=[("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "NRI rental income and TDS"),
             ("hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html", "HRA exemption 2026"),
             ("section-80c-complete-list-india-2026.html", "Section 80C list"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27"),
             ("income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri.html", "Old vs new section numbers")],
    cta_h="Earning rent or paying a home loan?", cta_b=C,
    keywords="income from house property, house property income calculation, house property deductions, 30 percent standard deduction house property, home loan interest new regime, section 24 interest 2 lakh, house property loss set off, section 22 Income-tax Act 2025",
    desc="Income from house property (2026): annual value minus municipal tax, 30% standard deduction, home loan interest (Rs 2 lakh self-occupied old regime; full for let-out), new vs old regime, loss set-off, worked example, NRIs.",
    howto={"name": "How to calculate income from house property", "description": "For a let-out property.", "steps": [
        {"name": "Find the gross annual value", "text": "Actual rent or expected rent, whichever the rules require."},
        {"name": "Deduct municipal taxes paid", "text": "Gives the net annual value."},
        {"name": "Deduct 30% of net annual value", "text": "Flat standard deduction."},
        {"name": "Deduct home loan interest", "text": "Including pre-construction interest in five instalments."},
        {"name": "Apply the loss rules", "text": "Rs 2 lakh set-off in the old regime; none against other income in the new regime."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HT complete")
