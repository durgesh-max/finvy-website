# -*- coding: utf-8 -*-
"""Batch IP (25 Nov 2026): education loan tax benefit 2026 - section 80E of the 1961 Act, section 129 of the 2025 Act
from tax year 2026-27: deduction for the full interest (no upper limit) on a loan for higher education of self,
spouse, children or a student of whom the individual is legal guardian; individuals only; loan from a financial
institution (bank) or approved charitable institution; allowed for the year interest repayment starts and the seven
following years (8 years) or until the interest is paid, if earlier; principal not deductible; India or abroad, any
course after senior secondary; old regime only; distinct from 80C tuition fees.
Demand: sweep ac112 (25 Nov 2026), 6-7 markets: "education loan tax benefit", "education loan tax exemption",
"education loan tax deduction", "education loan tax rebate", "education loan tax exemption calculator",
"education loan tax benefit india".
Facts (checked 25 Nov 2026): Income Tax Department pages on section 80E, Schedule 80E (8 assessment years from the year
interest payment starts) and section 129; Bajaj Finserv; Taxtmi notes."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "education-loan-tax-benefit-section-80e-now-section-129-interest-deduction-8-years-no-limit-2026"

C = contact("the education loan lender, who took the loan and for whom, the year interest repayment started, the interest paid this year, and the tax regime you use")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Education Loan Tax Benefit 2026 (Section 80E, Now Section 129): Full Interest Deduction for 8 Years, No Limit, Who Can Claim",
    em="all the interest, for eight years, with no upper limit.",
    kicker="/ Students, parents and graduates &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>The entire interest you pay on an education loan for higher studies is deductible under section 80E, with no upper limit, for up to eight years starting from the year you begin repaying interest.</strong> "
          "The principal is not deductible, the loan must come from a bank, financial institution or approved charitable institution, and the deduction is available only under the old tax regime. "
          "From tax year 2026-27 it sits in section 129 of the Income-tax Act, 2025."),
    sections=[
        ("/ Conditions at a glance", "Who, what and for how long.",
         table(["Point", "Rule"], [
             ["Who can claim", "Individuals only (not HUFs or companies), who took the loan and pay the interest"],
             ["For whose education", "Self, spouse, children, or a student for whom you are the legal guardian"],
             ["Which courses", "Higher education after senior secondary (Class 12), in India or abroad"],
             ["Lender", "Bank, financial institution or approved charitable institution; not relatives or employers"],
             ["Amount", "Full interest paid in the year; no upper limit; principal not deductible"],
             ["Period", "Year interest repayment starts plus the next seven years, or until the interest is paid, if earlier"],
             ["Regime", "Old regime only"]])
         + '<p>Tuition fees for up to two children are a separate deduction within section 80C; see the ' + L("section-80c-complete-list-india-2026.html", "80C list") + '.</p>'),
        ("/ Worked example (illustrative)", "Graduate repaying a loan, 30% slab, old regime.",
         ul("Interest paid in the year: &#8377;1,20,000, all deductible.",
            "Tax saved at 30% plus 4% cess: &#8377;37,440.",
            "If repayment started in 2024-25, the last year to claim is 2031-32.",
            "Check whether the old regime still comes out ahead with the " + L("new-vs-old-tax-regime-calculator.html", "new vs old regime calculator") + ".")),
        ("/ Practical points", "Avoid losing the deduction.",
         ul("<strong>Start repaying interest early:</strong> the eight-year clock starts when interest repayment begins, so paying interest during the course or moratorium can bring forward the benefit.",
            "<strong>Who pays matters:</strong> if a parent took the loan for a child, the parent claims; a child who later takes over the loan in their own name claims from then.",
            "<strong>Keep the interest certificate:</strong> lenders issue a yearly certificate splitting interest and principal; give it to your employer for payroll TDS and keep it for the return.",
            "<strong>Studying abroad:</strong> remittances for fees may attract TCS under the Liberalised Remittance Scheme; see " + L("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "sending money to a child studying abroad") + " and the " + L("lrs-tcs-calculator.html", "LRS TCS calculator") + ".",
            "<strong>Other deductions:</strong> combine with " + L("section-80d-health-insurance-tax-benefit-2026-25000-50000-parents-senior-citizens-section-126.html", "health insurance (80D)") + " and 80C when deciding your regime.")
         + call_box("Deductions", ["80E and 80C planning",
                                    "Old vs new regime choice",
                                    "Study-abroad remittances and TCS",
                                    "Payroll proof and TDS",
                                    "ITR filing"],
                    "your loan interest certificate.")
         + sources("Income-tax Act, 1961 section 80E; Income-tax Act, 2025 section 129 (Income Tax Department section pages and Schedule 80E guidance); Bajaj Finserv and Taxtmi explainers. Checked 25 November 2026.")),
    ],
    faqs=[("How much tax benefit is there on an education loan?", "The entire interest paid in the year is deductible under section 80E, with no upper limit, under the old regime. The principal repayment is not deductible."),
          ("For how many years can I claim the education loan deduction?", "For the year in which you start repaying interest and the seven years after it (eight years in all), or until the interest is fully paid, whichever is earlier."),
          ("Is the education loan deduction available in the new tax regime?", "No. Section 80E (section 129 of the Income-tax Act, 2025) can be claimed only under the old regime."),
          ("Can parents claim the education loan tax benefit?", "Yes, if the parent took the loan for the child's higher education and pays the interest. The deduction goes to whoever is the borrower and pays."),
          ("Does an education loan for studying abroad qualify?", "Yes. Higher education in India or abroad after Class 12 qualifies, provided the loan is from a bank, financial institution or approved charitable institution."),
          ("Can BQP help with education loan and study-abroad tax?", "Yes. CA Durgesh Chavda can work out the 80E deduction, compare regimes, plan study-abroad remittances and file your return. " + C)],
    related=[("section-80c-complete-list-india-2026.html", "Section 80C list"),
             ("section-80d-health-insurance-tax-benefit-2026-25000-50000-parents-senior-citizens-section-126.html", "Health insurance (80D)"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "Sending money for studies abroad"),
             ("lrs-tcs-calculator.html", "LRS TCS calculator")],
    cta_h="Repaying an education loan?", cta_b=C,
    keywords="education loan tax benefit, education loan tax exemption, section 80E, education loan interest deduction, 80E 8 years, education loan tax benefit new regime, education loan abroad tax benefit, section 129 Income-tax Act 2025",
    desc="Education loan tax benefit 2026: section 80E (section 129 of the 2025 Act) deducts the full interest with no limit for 8 years from when repayment starts; self, spouse, children or ward; bank or approved lender; old regime only; worked example.",
    howto={"name": "How to claim the education loan deduction", "description": "Under the old regime.", "steps": [
        {"name": "Confirm eligibility", "text": "Individual borrower, higher education, bank or approved lender."},
        {"name": "Get the interest certificate", "text": "From the lender for the year."},
        {"name": "Track the eight-year window", "text": "From the year interest repayment starts."},
        {"name": "Give proof to your employer", "text": "So payroll TDS reflects the deduction."},
        {"name": "Claim in the return", "text": "Under the old regime, full interest paid."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IP complete")
