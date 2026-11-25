# -*- coding: utf-8 -*-
"""Batch IO (25 Nov 2026): medical / health insurance tax benefit 2026 - section 80D of the 1961 Act, section 126 of the
2025 Act from tax year 2026-27: self / spouse / dependent children Rs 25,000 (Rs 50,000 if the taxpayer or spouse is a
senior citizen); parents additional Rs 25,000 (Rs 50,000 if a parent is a senior citizen); maximum Rs 1 lakh;
preventive health check-up up to Rs 5,000 within those limits (cash allowed only for this); medical expenditure for
uninsured senior citizens up to Rs 50,000; premium in any mode other than cash; multi-year premium apportioned; old
regime only (not in new regime, no change in Budget 2026); employer-paid group medical cover is generally not a
taxable perquisite and cannot also be claimed under 80D by the employee.
Demand: sweep ac112 (25 Nov 2026), 6-7 markets: "medical insurance tax benefit", "medical insurance taxable benefit",
"medical insurance tax deductible", "medical insurance tax relief", "medical insurance tax form".
Facts (checked 25 Nov 2026): Income Tax Department pages on section 80D and section 126; Cleartax (section 126),
Motilal Oswal, Jio Finance, Upstox (Budget 2026, no change), Aditya Birla Sun Life (old vs new regime)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "section-80d-health-insurance-tax-benefit-2026-25000-50000-parents-senior-citizens-section-126"

C = contact("the health insurance premiums you pay for yourself, your family and your parents, everyone's age, any preventive check-up costs, and the tax regime you use")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Health Insurance Tax Benefit 2026 (Section 80D, Now Section 126): Rs 25,000 / Rs 50,000 Limits, Parents, Senior Citizens and New Regime",
    em="up to Rs 1 lakh a year, but only in the old regime.",
    kicker="/ Families and senior citizens &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Health insurance premiums paid for yourself, your spouse and children are deductible up to &#8377;25,000 a year under section 80D (&#8377;50,000 if you are a senior citizen), with a further &#8377;25,000 for your parents (&#8377;50,000 if a parent is a senior citizen), so the maximum is &#8377;1 lakh.</strong> "
          "The deduction is available only under the old tax regime. From tax year 2026-27 it sits in section 126 of the Income-tax Act, 2025, with the same limits."),
    sections=[
        ("/ Limits at a glance", "Old regime only.",
         table(["Who is covered", "All below 60", "Taxpayer below 60, parents 60+", "Taxpayer and parents 60+"], [
             ["Self, spouse, dependent children", "&#8377;25,000", "&#8377;25,000", "&#8377;50,000"],
             ["Parents", "&#8377;25,000", "&#8377;50,000", "&#8377;50,000"],
             ["Maximum deduction", "&#8377;50,000", "&#8377;75,000", "&#8377;1,00,000"]])
         + '<p>Preventive health check-ups up to &#8377;5,000 a year are included within these limits. Senior citizens with no health insurance can claim medical expenditure up to &#8377;50,000 instead.</p>'),
        ("/ Worked example (illustrative)", "Taxpayer aged 40, parents aged 65, 30% slab.",
         ul("Family floater premium for self, spouse and children: &#8377;30,000, deduction &#8377;25,000 (cap).",
            "Parents&rsquo; senior citizen policy: &#8377;55,000, deduction &#8377;50,000 (cap).",
            "Total deduction &#8377;75,000; tax saved at 30% plus 4% cess = &#8377;23,400.",
            "Compare the old and new regimes with the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + " before you decide; see also " + L("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "which regime to choose") + ".")),
        ("/ Rules and common questions", "What counts and what does not.",
         ul("<strong>Payment mode:</strong> premiums must be paid by any mode other than cash; only the preventive check-up can be paid in cash.",
            "<strong>Multi-year policies:</strong> a premium paid upfront for several years is deducted proportionately each year.",
            "<strong>Who can pay:</strong> you can claim for premiums you pay for your parents even if they are not dependent on you; premiums for in-laws, siblings or grandparents do not qualify.",
            "<strong>Employer group cover:</strong> health insurance bought by your employer for you is generally not a taxable perquisite, but you cannot also claim it under 80D; top-ups you pay yourself do qualify.",
            "<strong>New regime:</strong> no 80D deduction; Budget 2026 did not change this.",
            "<strong>In the return:</strong> report the insurer and policy details the ITR form asks for and keep the premium receipts.",
            "<strong>NRIs and returning seniors:</strong> see " + L("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI senior citizen tax") + " and the " + L("section-80c-complete-list-india-2026.html", "80C deduction list") + ".")
         + call_box("Deductions", ["80D and 80C planning",
                                    "Old vs new regime choice",
                                    "Parents' and senior citizen claims",
                                    "Payroll proof and TDS",
                                    "ITR filing"],
                    "your premium receipts.")
         + sources("Income-tax Act, 1961 section 80D; Income-tax Act, 2025 section 126 (Income Tax Department section pages); Cleartax, Motilal Oswal, Jio Finance, Upstox and Aditya Birla Sun Life explainers. Checked 25 November 2026.")),
    ],
    faqs=[("How much tax can I save on health insurance?", "Under the old regime you can deduct up to Rs 25,000 for yourself, spouse and children (Rs 50,000 if you are a senior citizen) and a further Rs 25,000 for parents (Rs 50,000 if they are senior citizens), up to Rs 1 lakh a year in total."),
          ("Is health insurance deductible under the new tax regime?", "No. Section 80D (section 126 of the Income-tax Act, 2025) is available only under the old regime."),
          ("Is employer-provided medical insurance a taxable benefit?", "Generally no. Premium paid by your employer for group health cover is not taxed as a perquisite, but you cannot claim 80D for it; premiums you pay yourself, such as a top-up or parents' policy, can be claimed."),
          ("Can I claim 80D for my parents' health insurance?", "Yes, even if they are not dependent on you: up to Rs 25,000, or Rs 50,000 if either parent is 60 or older. Premiums for in-laws do not qualify for you, though your spouse can claim for their own parents."),
          ("Is a preventive health check-up deductible?", "Yes, up to Rs 5,000 a year within the overall 80D limit, and it can be paid in cash."),
          ("Can BQP help me plan deductions?", "Yes. CA Durgesh Chavda can review your 80D and other deductions, compare regimes and file your return. " + C)],
    related=[("section-80c-complete-list-india-2026.html", "Section 80C list"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("which-regime-new-vs-old-tax-regime-decision-india-2026-27.html", "Which regime to choose"),
             ("nri-senior-citizen-tax-india-2026-exemption-limit-80ttb-advance-tax-15h-pension-retire-to-india.html", "NRI senior citizen tax"),
             ("tax-rates-in-india-2026-27-income-tax-slabs-percentage-corporate-gst-capital-gains-nri.html", "Tax rates 2026-27")],
    cta_h="Paying health insurance premiums?", cta_b=C,
    keywords="health insurance tax benefit, medical insurance tax benefit, section 80D limit 2026, 80D parents senior citizen 50000, medical insurance taxable benefit, 80D new tax regime, preventive health check up 5000, section 126 Income-tax Act 2025",
    desc="Health insurance tax benefit 2026: section 80D (section 126 of the 2025 Act) Rs 25,000 for self and family, Rs 50,000 for senior citizens, parents extra, Rs 1 lakh maximum, Rs 5,000 check-up, old regime only, employer cover, worked example.",
    howto={"name": "How to claim the health insurance deduction", "description": "Under the old regime.", "steps": [
        {"name": "Choose the old regime", "text": "80D is not available in the new regime."},
        {"name": "Collect receipts", "text": "Premium receipts for self, family and parents, paid other than in cash."},
        {"name": "Apply the limits", "text": "Rs 25,000 / Rs 50,000 for each group, check-up within them."},
        {"name": "Give proof to your employer", "text": "So payroll TDS reflects the deduction."},
        {"name": "Report in the return", "text": "With insurer and policy details."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IO complete")
