# -*- coding: utf-8 -*-
"""Batch AP: Round 27 - pages answering what people ask on X: FAST-DS emails, ITR refund delays, foreign cloud tax holiday."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


def steps(*pairs):
    return [{"name": n, "text": t} for n, t in pairs]


PAGES = [
    dict(
        slug="income-tax-email-foreign-assets-fast-ds-what-to-do",
        title="Got an Income Tax Email About Foreign Assets (FAST-DS)? What It Means and What to Do",
        em="an advisory, not a notice, but do not ignore it.",
        kicker="/ FAST-DS &middot; Updated 2026-10-30",
        lead="The Income Tax Department is emailing taxpayers whose AIS shows foreign bank accounts, shares, custodial accounts or property, based on data received from other countries under CRS and FATCA. The email says the Department's records indicate you may have overseas financial interests and points you to FAST-DS 2026, the one-time disclosure scheme that closes on 31 December 2026. It is an advisory, not a legal notice, but the Department now has a record that you were told.",
        sections=[
            ("/ First, check the facts", "Before you do anything else.",
             "<ol><li>Log in to the e-filing portal yourself (type the address; do not use links in the email).</li>"
             "<li>Open your AIS and the Foreign Assets Information section.</li>"
             "<li>For each year, compare the entries with Schedule FA (foreign assets) and Schedule FSI (foreign income) in the returns you filed.</li>"
             "<li>Check your residential status for each year: Schedule FA is required only in years you were resident and ordinarily resident.</li></ol>"),
            ("/ Then pick the right route", "Depending on what you find.",
             "<table><thead><tr><th>What you find</th><th>What to do</th></tr></thead><tbody>"
             "<tr><td>Everything was reported correctly</td><td>No action; keep your working papers</td></tr>"
             "<tr><td>You hold nothing abroad, or the AIS entry is wrong</td><td>Give feedback on the AIS entry; do not file anything just to be safe</td></tr>"
             "<tr><td>Asset bought while non-resident or from taxed income, but missing from Schedule FA</td><td>FAST-DS Category 2: flat INR 1 lakh fee (assets up to INR 5 crore)</td></tr>"
             "<tr><td>Foreign income or assets never taxed in India</td><td>FAST-DS Category 1: 60% of the value (up to INR 1 crore in aggregate)</td></tr>"
             "<tr><td>Error only in the AY 2026-27 return</td><td>A revised return before 31 December 2026 may be simpler</td></tr></tbody></table>"
             "<p>Foreign assets (other than immovable property) with an aggregate value up to INR 20 lakh fall below the Black Money Act penalty threshold for non-reporting; check your exposure before paying anything.</p>"),
            ("/ How FAST-DS filing works", "Four forms.",
             ul("<strong>Form 1</strong>: your declaration, filed on the e-filing portal by 31 December 2026. One form can cover several assets.",
                "<strong>Form 2</strong>: the Department's order stating the amount payable.",
                "<strong>Form 3</strong>: your payment details.",
                "<strong>Form 4</strong>: the certificate confirming the declaration.",
                "Payment is due within two months from the end of the month in which you receive Form 2; a further two months is allowed with 1% simple interest a month. After that, the declaration is void.",
                "The 31 December date is for declaring, not paying. Assets are valued as on 31 March 2026.")),
            ("/ Watch for phishing", "Stay safe.",
             ul("The genuine email's links pass through an email-tracking domain before reaching the Income Tax site, so you cannot judge it by the link alone.",
                "Never upload documents or enter your password through an emailed link; go to the portal directly.") +
             src(("TaxGuru: received a FAST-DS email?", "https://taxguru.in/income-tax/received-fast-ds-email-foreign-assets-check-ais-31-december-2026.html"),
                 ("Income Tax India on X: FAST-DS 2026", "https://x.com/IncomeTaxIndia/status/2114991810850562273")) +
             "<p><em>Last updated: 30 October 2026. Payment timing as per published practitioner readings of the Department's FAQ; confirm in the FAST-DS Rules (Notification 114/2026).</em></p>"),
        ],
        howto=dict(name="What to do after a FAST-DS email", description="Steps to respond to the Income Tax Department's foreign assets email.",
                   steps=steps(("Log in directly", "Open the e-filing portal yourself, not through the email link."),
                               ("Check AIS foreign assets", "Compare each entry with Schedule FA and FSI in past returns."),
                               ("Decide the route", "No action, AIS feedback, revised return, or FAST-DS Category 1 or 2."),
                               ("File Form 1 by 31 December 2026", "If FAST-DS applies, declare all relevant assets in one form."),
                               ("Pay after Form 2", "Pay within the window and collect Form 4."))),
        faqs=[
            ("Is the FAST-DS email from the Income Tax Department a notice?", "No. It is an advisory based on foreign-account data in your AIS. But the Department has a record that you were informed, so check your returns against the data."),
            ("I received the email but reported everything. Do I need to do anything?", "No. If your Schedule FA and FSI already show the assets and income, keep your working papers and take no further action."),
            ("What if the AIS entry is wrong?", "Submit feedback on the AIS entry on the portal. Do not file a FAST-DS declaration just to be safe."),
            ("When do I have to pay under FAST-DS?", "After you receive the Form 2 order: within two months from the end of that month, or two more months with 1% interest a month. The 31 December 2026 deadline is for filing the declaration."),
            ("Can BQP check my position and file FAST-DS?", "Yes: AIS review, residential status, category, valuation and filing. " + CONTACT),
        ],
        related=[("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS 2026 guide"), ("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS calculator")],
        cta_h="Received the foreign assets email?", cta_b=CONTACT,
        keywords="income tax email foreign assets, FAST-DS email what to do, AIS foreign assets information, FAST-DS Form 1 Form 2, income tax foreign asset advisory 2026, FAST-DS payment due date",
        desc="Received an Income Tax Department email about foreign assets and FAST-DS 2026? It is an advisory based on CRS/FATCA data in your AIS. How to check, which route applies, how Forms 1-4 and payment work, and how to avoid phishing.",
    ),
    dict(
        slug="itr-refund-delayed-2026-why-and-what-to-do",
        title="ITR Refund Delayed in 2026? Why It Happens and What You Can Do",
        em="and the interest you are owed.",
        kicker="/ Income Tax &middot; Updated 2026-10-30",
        lead="Many taxpayers who filed on time are still waiting for refunds. The Department can process a return up to nine months after the end of the financial year in which it was filed, so a return filed in 2026 can lawfully be processed as late as December 2026. Refunds are often held up by mismatches the taxpayer can fix, and a delayed refund earns interest of 0.5% a month under Section 244A.",
        sections=[
            ("/ Common reasons", "Check these first.",
             ul("The return was never e-verified, or was verified late.",
                "The bank account is not pre-validated on the portal, or the PAN-bank name does not match.",
                "TDS claimed in the return does not match Form 26AS or AIS.",
                "A defective-return notice or a proposed adjustment is waiting for your response.",
                "The refund was adjusted against an earlier outstanding demand.",
                "The return is selected for further verification or scrutiny.")),
            ("/ What you can do", "In order.",
             "<ol><li>Check the return status on the e-filing portal: filed, verified, processed, refund issued.</li>"
             "<li>Re-validate the bank account and make sure it is nominated for refund.</li>"
             "<li>Look under Pending Actions and e-Proceedings for notices and respond within the time given.</li>"
             "<li>Compare TDS in Form 26AS and AIS with the return; ask deductors to correct their TDS statements if needed.</li>"
             "<li>If processed but not paid, check the refund status and request a refund reissue on the portal.</li>"
             "<li>Raise a grievance through e-Nivaran on the portal if nothing moves.</li></ol>"),
            ("/ Interest on delayed refunds", "Section 244A.",
             ul("0.5% per month or part of a month.",
                "For returns filed by the due date, interest generally runs from 1 April of the assessment year; for later returns, from the date of filing.",
                "Interest can be reduced for delay caused by the taxpayer, and is not paid on very small refunds relative to the tax determined.",
                "Interest received on a refund is taxable income in the year received.") +
             src(("TaxGuru: refund delay and Section 244A interest", "https://taxguru.in/income-tax/income-tax-refund-delay-tracking-causes-section-244a-interest.html"),
                 ("Business Standard: what slows down your ITR refund", "https://www.business-standard.com/finance/personal-finance/from-bank-details-to-e-verification-what-really-slows-down-your-itr-refund-125082900991_1.html")) +
             "<p><em>Last updated: 30 October 2026.</em></p>"),
        ],
        howto=dict(name="How to chase a delayed income tax refund", description="Steps to find and fix the reason for a delayed ITR refund.",
                   steps=steps(("Check status", "See whether the return is verified, processed and the refund issued."),
                               ("Fix the bank account", "Pre-validate and nominate the account for refund."),
                               ("Respond to notices", "Check Pending Actions and e-Proceedings."),
                               ("Match TDS", "Reconcile with Form 26AS and AIS."),
                               ("Escalate", "Request reissue or raise an e-Nivaran grievance."))),
        faqs=[
            ("Why is my ITR refund delayed in 2026?", "Common reasons are a return that was not e-verified, a bank account that is not pre-validated, TDS mismatches with Form 26AS or AIS, pending notices, or adjustment against an old demand. The Department can also take up to nine months after the end of the year of filing to process the return."),
            ("How long can the Income Tax Department take to process my return?", "Up to nine months from the end of the financial year in which the return was filed."),
            ("Do I get interest on a delayed refund?", "Yes, generally 0.5% per month under Section 244A, from 1 April of the assessment year if you filed on time. It can be reduced for delays caused by the taxpayer."),
            ("How do I complain about a delayed refund?", "Raise a grievance through e-Nivaran on the e-filing portal after checking that no notice or verification is pending."),
            ("Can BQP chase my refund?", "Yes, including NRI refunds. " + CONTACT),
        ],
        related=[("section-143-1-intimation-response-india-2026.html", "Responding to a Section 143(1) intimation"), ("form-26as-vs-ais-vs-tis-india-2026.html", "Form 26AS, AIS and TIS")],
        cta_h="Refund stuck?", cta_b=CONTACT,
        keywords="ITR refund delayed 2026, income tax refund not received, why is my ITR refund delayed, refund interest 244A, ITR processing time 9 months, e-Nivaran refund grievance",
        desc="ITR refund delayed in 2026? The Department can process returns up to nine months after the year of filing. Common causes (e-verification, bank validation, TDS mismatch, notices), steps to fix them, and 0.5% monthly interest under Section 244A.",
    ),
    dict(
        slug="foreign-cloud-companies-tax-holiday-indian-data-centres-2047",
        title="Tax Holiday Until 2047 for Foreign Cloud Companies Using Indian Data Centres",
        em="what Budget 2026 offers and the conditions.",
        kicker="/ Foreign Companies &middot; Updated 2026-10-30",
        lead="Budget 2026-27 (1 February 2026) proposed a tax holiday until 2047 for foreign companies that provide cloud services to customers worldwide using data centre services from India. The conditions: the data centre is operated by an Indian company, the foreign company is notified, and services to Indian customers go through an Indian reseller, which remains taxable in India. Where the Indian data centre is a related party working on cost-plus, a 15% safe harbour margin on cost was proposed.",
        sections=[
            ("/ The conditions", "As announced.",
             ul("The foreign company provides cloud services to customers globally using data centre services procured from India.",
                "The data centre services come from an Indian company operating a data centre in India.",
                "Sales to Indian customers are made through an Indian reseller entity, which is taxed in India normally.",
                "The foreign company is notified under the relevant provisions.",
                "Related-party Indian data centres operating on cost-plus can use a 15% margin on cost as a safe harbour.")),
            ("/ Why it matters", "The permanent establishment question.",
             "<p>Foreign cloud providers have been cautious about putting large infrastructure in India because of the risk that it creates a permanent establishment and exposes global cloud income to Indian tax. The holiday removes that cost for the specified income, while keeping the Indian data centre operator and the Indian reseller fully taxable.</p>"),
            ("/ What foreign cloud and SaaS companies should check", "Practical points.",
             ul("Whether your Indian data centre arrangement meets the conditions and notification requirements.",
                "Reseller structure for Indian customers: contracts, pricing, GST on supplies to Indian customers and transfer pricing.",
                "Transfer pricing for a related Indian data centre: whether to use the 15% safe harbour.",
                "Permanent establishment exposure for other activities in India not covered by the holiday.",
                "Separately, Budget 2026 announced a single IT services safe harbour (15.5% margin) with the eligibility threshold raised from INR 300 crore to INR 2,000 crore.") +
             src(("Business Today", "https://www.businesstoday.in/amp/union-budget/news/story/budget-2026-nirmala-sitharaman-announces-tax-holiday-to-lure-foreign-data-centre-firms-as-ai-demand-surges-513930-2026-02-01"),
                 ("Outlook Business", "https://www.outlookbusiness.com/budget/budget-govt-proposes-tax-holiday-till-2047-to-boost-data-centre-investments"),
                 ("Takshashila Institution", "https://takshashila.org.in/content/blogs/20260201-union-budget-proposes-tax-holiday-for-global-cloud-services.html")) +
             "<p><em>Last updated: 30 October 2026. Based on Budget announcements; check the enacted Finance Act 2026 provisions and notifications for the final conditions.</em></p>"),
        ],
        howto=None,
        faqs=[
            ("What is the Budget 2026 tax holiday for cloud companies?", "A tax holiday until 2047 for foreign companies providing cloud services globally using data centre services from India, subject to conditions including an Indian reseller for Indian customers and notification of the foreign company."),
            ("Does the Indian data centre also get a tax holiday?", "No. The Indian data centre operator and the Indian reseller remain taxable in India. A related-party data centre on cost-plus can use a 15% margin on cost as a safe harbour."),
            ("Why was this introduced?", "To attract global cloud workloads to Indian data centres by removing the permanent establishment tax risk that foreign providers feared."),
            ("Can BQP structure the Indian side for a foreign cloud provider?", "Yes: reseller entity set-up, transfer pricing, GST, FEMA and permanent establishment review. " + CONTACT),
        ],
        related=[("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs"), ("best-ca-oidar-gst-foreign-saas-india-2026.html", "GST for foreign SaaS")],
        cta_h="Foreign cloud or SaaS company using India?", cta_b=CONTACT,
        keywords="tax holiday 2047 foreign cloud companies India, Budget 2026 data centre tax holiday, foreign cloud provider Indian data centre tax, data centre safe harbour 15%, permanent establishment cloud India",
        desc="Budget 2026-27 proposed a tax holiday until 2047 for foreign cloud companies using Indian data centres, with an Indian reseller for Indian customers and a 15% cost-plus safe harbour for related data centres. Conditions and what to check.",
    ),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print(f"Batch AP complete: {len(PAGES)} pages")
