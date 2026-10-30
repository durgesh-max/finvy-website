# -*- coding: utf-8 -*-
"""Batch AH: Round 18 - verified late-October 2026 news pages (FAST-DS, Form 141, Income-tax Act 2025, US remittance tax, CBDT Circular 07/2026, news hub)."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours; work delivered remotely."
LEAD = "Bharat Quantum Prospera (BQP), led by CA Durgesh Chavda (ICAI)"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


def updated(note=""):
    return f"<p><em>Last updated: 30 October 2026.{(' ' + note) if note else ''} Confirm against the official notification on incometax.gov.in before acting.</em></p>"


def steps(*pairs):
    return [{"name": n, "text": t} for n, t in pairs]


S_FASTDS = [("Outlook Money", "https://www.outlookmoney.com/personal-finance/fast-ds-2026-goes-live-small-taxpayers-get-window-to-declare-foreign-assets-income"),
            ("The Accountant", "https://www.theaccountant-online.com/news/india-launches-limited-tax-amnesty-for-small-foreign-asset-disclosures/")]
S_F141 = [("Outlook Money", "https://www.outlookmoney.com/tax/buying-a-home-from-an-nri-you-no-longer-need-a-tan-for-tds"),
          ("Taxscan", "https://www.taxscan.in/other-taxations/eligible-persons-can-use-pan-for-tds-compliance-on-buying-property-from-nri-all-about-new-tds-rules-from-oct-1")]
S_ACT = [("ClearTax", "https://cleartax.in/s/tds-and-tcs-changes-from-april-2026"),
         ("EXIMPE", "https://eximpe.com/blog/payments/section-195-tds-non-residents-section-393")]
S_US = [("Cherry Bekaert", "https://www.cbh.com/insights/articles/excise-tax-on-remittance-transfers-irc-section-4475-explained/"),
        ("Greenback Tax Services", "https://www.greenbacktaxservices.com/blog/irs-remittance-transfer-tax-proposed-regulations/")]
S_CIRC = [("India Briefing", "https://www.india-briefing.com/news/india-cbdt-extends-itr-due-date-tax-audit-cases-ay-2026-27-47142.html/"),
          ("Angel One", "https://www.angelone.in/news/taxation/cbdt-revises-ay-2026-27-tax-deadlines-itr-due-date-now-november-21-2026")]
S_TCS = [("Lulu Forex", "https://luluforex.com/blog/complete-guide-to-tcs-changes-effective-april-1-2026")]

PAGES = [
    dict(
        slug="fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline",
        title="FAST-DS 2026: Declare Undisclosed Foreign Assets by 31 December 2026",
        em="the one-time window for small taxpayers.",
        kicker="/ News &middot; FAST-DS 2026 &middot; Updated 2026-10-30",
        lead="FAST-DS 2026 (Foreign Assets of Small Taxpayers Disclosure Scheme) lets eligible taxpayers declare foreign income or assets they left out of their Indian returns and get immunity under the Black Money Act. Declarations opened on 16 August 2026 and close on 31 December 2026. It is aimed at returning students, young professionals, technology employees and former NRIs who still hold overseas accounts, shares, ESOPs or property. <a href=\"fast-ds-2026-calculator-foreign-asset-disclosure-cost.html\">Estimate your amount with the FAST-DS 2026 calculator &rarr;</a> Got an email from the Department about foreign assets? <a href=\"income-tax-email-foreign-assets-fast-ds-what-to-do.html\">Here is what it means &rarr;</a>",
        sections=[
            ("/ The two categories", "Which one applies to you.",
             "<table><thead><tr><th></th><th>Category 1</th><th>Category 2</th></tr></thead><tbody>"
             "<tr><td>What it covers</td><td>Foreign income or assets never offered to tax in India</td><td>Assets already taxed, or acquired while you were a non-resident, but not shown in the return's foreign-asset schedule</td></tr>"
             "<tr><td>Value limit</td><td>Up to INR 1 crore in aggregate</td><td>Up to INR 5 crore</td></tr>"
             "<tr><td>Cost</td><td>30% tax plus an equal additional amount: 60% of the value</td><td>Flat fee of INR 1 lakh</td></tr></tbody></table>"
             "<p>Foreign assets are valued at fair market value as on 31 March 2026. CBDT's own illustration: an undisclosed foreign account of INR 60 lakh plus INR 20 lakh of related income gives INR 80 lakh; at 60% the amount payable is INR 48 lakh.</p>"),
            ("/ What you get", "Immunity and finality.",
             ul("Protection from further tax, penalty and prosecution under the Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, for the asset or income declared.",
                "The declared amount is not added again to your total income under the Income-tax Act or the Black Money Act.",
                "Black Money Act penalties outside the scheme can be far higher, and prosecution is possible, so the scheme is materially cheaper for most eligible people.")),
            ("/ Who should look at this now", "Common cases.",
             ul("You returned to India and are now resident, but your US 401(k), UK ISA, foreign bank account or RSUs are not in Schedule FA.",
                "You studied or worked abroad and kept a foreign account open after moving back.",
                "You hold ESOPs or RSUs of a foreign employer that vested while you were resident in India.",
                "You were resident in a year but filed as a non-resident, so foreign assets were never reported.",
                "You inherited or received a gift of foreign assets and did not report them.")),
            ("/ How BQP handles it", "Fixed scope, confidential.",
             ul("Review your residential status for each year and identify which assets and income fall in Category 1 or Category 2.",
                "Value each asset at fair market value as on 31 March 2026 with supporting statements.",
                "Prepare and file the declaration, and compute the amount payable and its due dates.",
                "Fix Schedule FA in future returns so the problem does not recur.") + src(*S_FASTDS) + updated("Rates and limits are as reported by these sources.")),
        ],
        howto=dict(name="How to use FAST-DS 2026", description="Steps to declare foreign assets under FAST-DS before 31 December 2026.",
                   steps=steps(("List foreign assets and income", "Bank accounts, shares, ESOPs/RSUs, retirement accounts, property and related income."),
                               ("Check residential status", "Confirm which years you were resident and should have reported them."),
                               ("Sort into categories", "Untaxed (Category 1, up to INR 1 crore) or taxed-but-unreported (Category 2, up to INR 5 crore)."),
                               ("Value as on 31 March 2026", "Use fair market value with supporting statements."),
                               ("File before 31 December 2026", "Submit the declaration online and pay within the stated time."))),
        faqs=[
            ("What is FAST-DS 2026?", "A one-time scheme for small taxpayers to declare foreign income or assets missed in Indian returns, with immunity under the Black Money Act. It opened on 16 August 2026 and closes on 31 December 2026."),
            ("How much does FAST-DS cost?", "Category 1 (untaxed foreign income or assets up to INR 1 crore): 30% tax plus an equal additional amount, 60% in total. Category 2 (already-taxed assets up to INR 5 crore that were not reported): a flat INR 1 lakh fee."),
            ("Who is FAST-DS meant for?", "Returning students, young professionals, technology employees and former NRIs with overseas accounts, shares, ESOPs or retirement savings that were not reported after they became resident in India."),
            ("What happens after 31 December 2026?", "Declarations cannot be filed after that date. Undisclosed foreign assets found later fall under the Black Money Act, with higher tax, penalties and possible prosecution."),
            ("Can BQP file my FAST-DS declaration?", "Yes. We review residential status, categorise and value each asset, file the declaration and correct future Schedule FA reporting. " + CONTACT),
        ],
        related=[("income-tax-email-foreign-assets-fast-ds-what-to-do.html", "Got the FAST-DS email? What to do"), ("nri-returning-india-tax-rnor-transition.html", "Returning to India: RNOR planning"), ("nri-tax-services-worldwide-by-country.html", "NRI taxation by country")],
        cta_h="Foreign assets not in your Indian return?",
        cta_b="FAST-DS closes on 31 December 2026. " + CONTACT,
        keywords="FAST-DS 2026, foreign assets disclosure scheme 2026, undisclosed foreign assets India, Schedule FA not reported, Black Money Act disclosure, FAST-DS last date 31 December 2026",
        desc="FAST-DS 2026 lets small taxpayers declare undisclosed foreign income or assets by 31 December 2026: Category 1 up to INR 1 crore at 60%, Category 2 up to INR 5 crore for a flat INR 1 lakh, with Black Money Act immunity.",
    ),
    dict(
        slug="buying-property-from-nri-no-tan-form-141-from-1-october-2026",
        title="Buying Property From an NRI: No TAN Needed From 1 October 2026 (Form 141)",
        em="TDS under your own PAN.",
        kicker="/ News &middot; NRI Property &middot; Updated 2026-10-30",
        lead="From 1 October 2026, a resident individual or HUF buying property from a non-resident Indian can deposit and report the TDS using their own PAN through Form 141, instead of first obtaining a TAN. The obligation to deduct tax, the rates and the penalties for getting it wrong have not changed.",
        sections=[
            ("/ What changed", "Before and after.",
             ul("<strong>Before</strong>: a buyer purchasing from an NRI needed a TAN, then had to deposit TDS and file a quarterly TDS return like a business.",
                "<strong>From 1 October 2026</strong>: resident individual and HUF buyers can use their PAN and report the deduction in Form 141 (new Schedule E), reported to be under the Income-tax (Fifth Amendment) Rules, 2026.",
                "<strong>Not covered</strong>: companies, firms and other buyers still need a TAN.",
                "<strong>Timing</strong>: the date tax is deducted decides which route applies. An instalment where TDS was deducted before 1 October 2026 stays on the TAN route.")),
            ("/ What the buyer still has to deduct", "Rates are unchanged.",
             ul("Long-term gain (property held more than 24 months): 12.5% plus surcharge and cess.",
                "Short-term gain: 30% plus surcharge and cess (higher slab rates can apply for some sellers).",
                "There is no INR 50 lakh threshold when the seller is an NRI; that limit applies only to resident sellers.",
                "Without a lower deduction certificate, buyers usually deduct on the full sale price, which can be far more than the tax on the gain.",
                "If the NRI seller has no PAN, higher rates can apply.")),
            ("/ For the NRI seller", "Get the deduction right first.",
             ul("Apply for a lower deduction certificate well before registration so the buyer deducts only the tax actually due on the gain.",
                "Plan Section 54/54F/54EC exemptions if you are reinvesting.",
                "After the sale, file an Indian return to claim any excess TDS, then repatriate through Form 15CA/15CB.") + src(*S_F141) + updated()),
        ],
        howto=dict(name="How a resident buyer pays TDS on property bought from an NRI (from 1 October 2026)", description="Steps for individual and HUF buyers using PAN and Form 141.",
                   steps=steps(("Get the seller's details", "PAN, residential status and any lower deduction certificate."),
                               ("Compute TDS", "12.5% (long-term) or 30% (short-term) plus surcharge and cess, or the certificate rate."),
                               ("Deduct at payment", "Deduct when each instalment is paid or credited."),
                               ("Deposit and report under your PAN", "Use Form 141 (Schedule E) on the e-filing portal."),
                               ("Give the seller the TDS certificate", "So the NRI can claim credit in their Indian return."))),
        faqs=[
            ("Do I need a TAN to buy property from an NRI?", "Not from 1 October 2026 if you are a resident individual or HUF: you can use your PAN and Form 141. Companies, firms and other buyers still need a TAN."),
            ("What is the TDS rate when buying from an NRI?", "12.5% plus surcharge and cess on long-term gains (held over 24 months) and 30% plus surcharge and cess on short-term gains, unless the seller gives you a lower deduction certificate."),
            ("Is there a minimum property value for TDS from an NRI?", "No. The INR 50 lakh threshold applies only when the seller is resident. TDS applies to any purchase from an NRI."),
            ("I paid an instalment in September 2026. Which route applies?", "The TAN route for that instalment, because TDS was deducted before 1 October 2026. Later instalments can use the PAN route."),
            ("Can BQP handle the TDS for a buyer or seller?", "Yes, for buyers (computation, Form 141, certificates) and NRI sellers (lower deduction certificate, return, repatriation). " + CONTACT),
        ],
        related=[("when-is-tds-applicable-on-nri-sale-of-property-india.html", "TDS on NRI property sales"), ("nri-india-property-ldc-lower-deduction-certificate.html", "Lower deduction certificate for NRIs")],
        cta_h="Buying from or selling to an NRI?",
        cta_b="Get the TDS right before registration. " + CONTACT,
        keywords="buying property from NRI TDS no TAN, Form 141 Schedule E, TDS on property purchase from NRI 2026, NRI property TDS PAN, TDS NRI seller 12.5%",
        desc="From 1 October 2026, resident individual and HUF buyers can pay TDS on property bought from an NRI under their own PAN through Form 141, without a TAN. Rates (12.5% long-term, 30% short-term) and obligations are unchanged.",
    ),
    dict(
        slug="income-tax-act-2025-section-195-now-393-what-changed-nri-foreign",
        title="Income-tax Act 2025: Section 195 Is Now Section 393(2). What Changed for NRIs and Foreign Payments",
        em="new law, same obligations.",
        kicker="/ News &middot; Income-tax Act 2025 &middot; Updated 2026-10-30",
        lead="The Income-tax Act, 2025 replaced the Income-tax Act, 1961 from 1 April 2026. For anyone paying non-residents, the familiar Section 195 is now Section 393(2) for payments made or credited on or after 1 April 2026. The obligation to deduct tax, treaty relief and the need for a CA certificate on foreign remittances continue; the section numbers, some forms and the terminology are new.",
        sections=[
            ("/ The changes that matter most", "For NRIs, foreign companies and Indian payers.",
             "<table><thead><tr><th>Topic</th><th>Income-tax Act, 1961</th><th>Income-tax Act, 2025</th></tr></thead><tbody>"
             "<tr><td>TDS on payments to non-residents</td><td>Section 195</td><td>Section 393(2)</td></tr>"
             "<tr><td>TDS on salary</td><td>Section 192</td><td>Section 392</td></tr>"
             "<tr><td>Other TDS provisions</td><td>Sections 193-194T</td><td>Consolidated in Section 393</td></tr>"
             "<tr><td>TCS, including on LRS remittances</td><td>Section 206C (206C(1G) for LRS)</td><td>Section 394</td></tr>"
             "<tr><td>Penalty waiver applications</td><td>&mdash;</td><td>Section 440(2), Form 161 (Notification 134/2026)</td></tr>"
             "</tbody></table>"),
            ("/ Which law applies to what", "The transition rule.",
             ul("Payments made or credited up to 31 March 2026 stay under the 1961 Act and Section 195.",
                "Payments made or credited from 1 April 2026 fall under the 2025 Act and Section 393(2).",
                "Returns for FY 2025-26 (assessment year 2026-27), due this year, are still filed under the 1961 Act, which is why CBDT's 2026 due-date circulars still cite Section 139.")),
            ("/ What to update now", "Practical checklist.",
             ul("Contracts, invoices and board resolutions that quote Section 195 for payments after 1 April 2026.",
                "Payroll and accounting software TDS codes, which now map to Section 393 entries.",
                "Treaty documentation: a Tax Residency Certificate and Form 10F are still needed to apply treaty rates.",
                "Remittance paperwork with your bank, which uses the new form references for CA certificates.",
                "Buyers of NRI property: see the separate change allowing PAN-based TDS from 1 October 2026.") + src(*S_ACT) + updated("Form numbers under the new rules vary between sources; check the portal for the current form.")),
        ],
        howto=None,
        faqs=[
            ("What replaced Section 195?", "Section 393(2) of the Income-tax Act, 2025, for payments to non-residents made or credited on or after 1 April 2026. Earlier payments stay under Section 195 of the 1961 Act."),
            ("When did the Income-tax Act, 2025 come into force?", "On 1 April 2026, replacing the Income-tax Act, 1961."),
            ("Are FY 2025-26 returns filed under the new Act?", "No. Returns for FY 2025-26 (assessment year 2026-27) are filed under the 1961 Act; the new Act governs income from 1 April 2026."),
            ("Do treaty benefits still apply?", "Yes. Payments to treaty residents can use the lower treaty rate with a Tax Residency Certificate and Form 10F."),
            ("Can BQP update our compliance for the new Act?", "Yes: contract language, TDS mapping, remittance certificates and treaty documentation for Indian entities paying foreign parties and for NRIs. " + CONTACT),
        ],
        related=[("what-is-form-15cb-and-when-is-it-required-india.html", "CA certificate for foreign remittances"), ("section-195-tds-foreign-payer-indian-vendor.html", "TDS on payments to non-residents")],
        cta_h="Paying non-residents from India?",
        cta_b="Make sure your TDS and remittance paperwork reflects the 2025 Act. " + CONTACT,
        keywords="Section 195 new section 393, Income-tax Act 2025 section mapping, Section 393(2) TDS non resident, Income Tax Act 2025 NRI changes, Section 394 TCS",
        desc="Under the Income-tax Act, 2025 (in force from 1 April 2026), Section 195 TDS on non-resident payments is Section 393(2), TCS moves to Section 394 and salary TDS to Section 392. Transition rules and what NRIs and foreign payers should update.",
    ),
    dict(
        slug="us-1-percent-remittance-tax-nri-sending-money-to-india-2026",
        title="US 1% Remittance Tax: What NRIs in the USA Pay When Sending Money to India",
        em="cash is taxed, bank transfers are not.",
        kicker="/ News &middot; USA &middot; Updated 2026-10-30",
        lead="Since 1 January 2026, the US charges a 1% excise tax (Internal Revenue Code Section 4475, enacted by the One Big Beautiful Bill Act) on certain money transfers sent abroad. It applies to transfers paid for in cash, by money order, cashier's check or similar instruments. Transfers funded from a US bank account or a US-issued debit or credit card are exempt.",
        sections=[
            ("/ Who pays and when", "The rule in brief.",
             ul("Applies to the sender regardless of citizenship or immigration status, so it covers NRIs, green-card holders and US citizens alike.",
                "The remittance provider collects it at the point of sale; on a USD 1,000 cash transfer the tax is USD 10.",
                "Exempt: transfers funded by withdrawal from a US bank account, and those paid with a US-issued debit or credit card.",
                "IRS proposed regulations published in April 2026 set out the tax base and which physical instruments count.")),
            ("/ What NRIs in the US should do", "Avoiding the tax legally.",
             ul("Send money from your US bank account (wire or app linked to the account) rather than paying cash at a counter.",
                "Keep transfer records: inward remittances are not taxable in India by themselves, but the money's source can matter in Indian scrutiny.",
                "Gifts to relatives in India are generally exempt in the recipient's hands under Section 56; gifts to non-relatives above INR 50,000 a year are taxable to the recipient.",
                "If you are resident in India for tax, US accounts and income also need to be reported in your Indian return.") + src(*S_US) + updated("US proposed regulations may change before they are finalised.")),
        ],
        howto=None,
        faqs=[
            ("Is there a US tax on sending money to India?", "A 1% US excise tax applies from 1 January 2026 to transfers abroad paid for in cash, money orders, cashier's checks or similar instruments. Transfers from a US bank account or with a US-issued debit or credit card are exempt."),
            ("Does the 1% remittance tax apply to green-card holders and NRIs?", "Yes. It applies to the sender regardless of citizenship or immigration status."),
            ("How do I avoid the US remittance tax?", "Fund the transfer from your US bank account or a US-issued card instead of cash or a money order."),
            ("Is money received in India taxable?", "Not by itself. Tax in India depends on the nature of the money; gifts from relatives are exempt for the recipient."),
            ("Can BQP advise on India-US money movement?", "Yes: Indian tax on income and gifts, repatriation from NRO accounts, and Indian reporting for US-resident clients. " + CONTACT),
        ],
        related=[("indian-ca-for-clients-in-usa.html", "Indian CA for clients in the USA"), ("nri-gift-indian-relatives-section-56-fema-2026.html", "Gifts to relatives in India")],
        cta_h="Living in the US with money in India?",
        cta_b=CONTACT,
        keywords="US remittance tax 1%, Section 4475 remittance tax, NRI sending money to India tax 2026, US remittance tax green card holder, remittance tax bank transfer exempt",
        desc="Since 1 January 2026 the US charges a 1% excise tax (Section 4475) on transfers abroad paid in cash, money orders or cashier's checks. Bank-account and US card-funded transfers are exempt. What NRIs in the USA should do.",
    ),
    dict(
        slug="itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026",
        title="ITR Due Date Extended to 21 November 2026 for Audit Cases: CBDT Circular 07/2026",
        em="transfer pricing cases did not move.",
        kicker="/ News &middot; Income Tax Deadline &middot; Updated 2026-10-30",
        lead="CBDT Circular 07/2026, dated 28 September 2026, extended the assessment year 2026-27 ITR due date for taxpayers whose accounts must be audited from 31 October to 21 November 2026, and the tax audit report from 30 September to 21 October 2026. Transfer pricing cases were not covered: Form 3CEB is still due on 31 October 2026 and their ITR on 30 November 2026.",
        sections=[
            ("/ The dates now", "AY 2026-27 (FY 2025-26).",
             "<table><thead><tr><th>Who</th><th>Report</th><th>ITR</th></tr></thead><tbody>"
             "<tr><td>Companies and other taxpayers needing an audit (and working partners of audited firms)</td><td>Tax audit report: 21 October 2026</td><td>21 November 2026</td></tr>"
             "<tr><td>Transfer pricing cases (international or specified domestic transactions)</td><td>Form 3CEB: 31 October 2026</td><td>30 November 2026</td></tr>"
             "<tr><td>Belated or revised return (all taxpayers)</td><td>&mdash;</td><td>31 December 2026</td></tr></tbody></table>"),
            ("/ What to do this week", "With Form 3CEB due on 31 October.",
             ul("If you have transactions with a foreign parent, subsidiary or other associated enterprise, Form 3CEB must be filed by 31 October 2026 even though audit-case ITRs moved.",
                "Pay self-assessment tax early: an extended filing date does not stop interest on unpaid tax.",
                "Companies opting into Section 115BAA should file Form 10-IC by the ITR due date.",
                "Foreign tax credit claims need Form 67 filed on or before the ITR due date.") + src(*S_CIRC) + updated()),
        ],
        howto=None,
        faqs=[
            ("What is the ITR due date for audit cases for AY 2026-27?", "21 November 2026, extended from 31 October by CBDT Circular 07/2026 dated 28 September 2026."),
            ("What is the tax audit report due date for AY 2026-27?", "21 October 2026, extended from 30 September 2026."),
            ("Was the Form 3CEB deadline extended?", "No. Form 3CEB remains due on 31 October 2026 and the ITR for transfer pricing cases on 30 November 2026."),
            ("Does the extension waive interest?", "An extended filing date does not by itself stop interest on tax that remains unpaid. Pay self-assessment tax as early as possible."),
            ("Can BQP still file Form 3CEB before 31 October?", "Yes, subject to data availability. " + CONTACT),
        ],
        related=[("form-3ceb-tp-audit-india-2026-30-november-checklist.html", "Form 3CEB checklist"), ("itr-filing-ay-2026-27-deadlines-changes-india.html", "AY 2026-27 ITR deadlines")],
        cta_h="Form 3CEB due 31 October?",
        cta_b="Transfer pricing cases did not get the extension. " + CONTACT,
        keywords="ITR due date 21 November 2026, CBDT Circular 07/2026, tax audit due date 21 October 2026, Form 3CEB due date 2026, AY 2026-27 audit ITR extension",
        desc="CBDT Circular 07/2026 extended the AY 2026-27 ITR due date for audit cases to 21 November 2026 and the tax audit report to 21 October 2026. Form 3CEB stays due 31 October and transfer pricing ITRs 30 November 2026.",
    ),
]

NEWS_ITEMS = [
    ("1 Oct 2026", "New FEMA export rules: nine months to realise proceeds", "FEMA (Export and Import of Goods and Services) Regulations, 2026 in force; RBI's 22 September amendment cut the period from 15 to 9 months (12 for INR exports). Service exporters file a monthly EDF within 30 days of month-end.", "fema-export-rules-1-october-2026-nine-month-realisation-edf-services.html", ("TaxUpdate", "https://taxupdate.in/finance/983/fema-export-realisation-period-october-1-2026-nine-months-rbi-amendment/")),
    ("27-30 Oct 2026", "Income Tax Department emails taxpayers about foreign assets", "Advisory emails based on CRS/FATCA data in AIS point taxpayers to FAST-DS 2026 (declarations by 31 December 2026). Not a notice, but check AIS against Schedule FA and FSI.", "income-tax-email-foreign-assets-fast-ds-what-to-do.html", ("TaxGuru", "https://taxguru.in/income-tax/received-fast-ds-email-foreign-assets-check-ais-31-december-2026.html")),
    ("Oct 2026", "Refunds still pending for many ITR filers", "Returns can be processed up to nine months after the end of the year of filing. Common fixes: e-verification, bank pre-validation, TDS mismatches; delayed refunds earn 0.5% a month under Section 244A.", "itr-refund-delayed-2026-why-and-what-to-do.html", ("TaxGuru", "https://taxguru.in/income-tax/income-tax-refund-delay-tracking-causes-section-244a-interest.html")),
    ("Tax year 2026-27", "IT services safe harbour: 15.5%, limit INR 2,000 crore", "A single safe harbour for software, ITeS, KPO and software contract R&amp;D replaces the old 17-24% margins and INR 300 crore limit; one Form 49 covers five years. Foreign cloud firms using Indian data centres get a tax holiday to 2047, subject to conditions.", "foreign-cloud-companies-tax-holiday-indian-data-centres-2047.html", ("Treelife", "https://treelife.in/?p=16081")),
    ("24 Oct 2026", "MCA waives late fees on FY 2025-26 AOC-4 and MGT-7", "General Circular 05/2026: no additional fee if AOC-4 is filed by 31 December 2026 and MGT-7/7A by 31 January 2027. Due dates and the AGM deadline are unchanged; LLP Form 8 (due 30 October) is not covered.", "aoc-4-filing-deadline-30-october-2026-late-fee-india.html", ("CAclubindia", "https://www.caclubindia.com/articles/mca-general-circular-05-2026-additional-fee-relaxation-for-fy-2025-26-annual-filings-56490.asp")),
    ("30 Oct 2026", "LLP Form 8 due today, no extension", "Statement of Account and Solvency for FY 2025-26; late fees rise as multiples of the normal fee.", "llp-form-8-due-30-october-2026-no-extension-late-fee.html", ("TaxAJ", "https://www.taxaj.com/learn/?p=90969")),
    ("14 Oct 2026", "SEBI proposes SME IPO overhaul", "Consultation paper: ₹3 crore average operating profit, market-cap eligibility, ₹1 lakh minimum application, 500 allottees, no compulsory market making. Comments by 4 November.", "sebi-sme-ipo-consultation-paper-october-2026-proposed-rules.html", ("Upstox", "https://upstox.com/news/market-news/ipo/sme-ipo-rules-set-for-major-overhaul-here-s-what-sebi-proposes/article-201897/")),
    ("19-25 Oct 2026", "RBI moves some FEMA compounding to Regional Offices", "Compounding applications for overseas investment and borrowing/lending/guarantee contraventions now go to designated RBI Regional Offices.", "fema-compounding-foreign-subsidiary-india.html", ("Weekly RBI roundup", "https://iamitsengupta.substack.com/p/weekly-enforcement-and-supervisory")),
    ("26-27 Oct 2026", "GST: 8 CBIC circulars and changes from 1 November", "After the 57th GST Council (8 October): 90% provisional inverted duty refunds, no INR 1,000 minimum on courier export refunds, reverse charge and GST TDS on scrap and e-waste, registration and adjudication safeguards.", "gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html", ("TaxO", "https://taxo.online/latest-news/27-10-2026-cbic-issued-various-circulars-following-recommendations-of-57th-gst-council-meeting-covering-smoother-registration-fairer-adjudication-and-major-relief-on-itc-and-export-refunds/")),
    ("26 Oct 2026", "Rule 96(10) omitted retrospectively from 2017", "Circular 264/10/2026 accepts the Supreme Court's Goodluck India ruling: IGST refund demands on exporters based on Rule 96(10) cannot be sustained.", "rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html", ("TaxGuru", "https://taxguru.in/goods-and-service-tax/rule-96-10-beginning-cbic-accepts-goodluck-india-circular-264-10-2026.html")),
    ("30 Oct / 30 Nov 2026", "UAE corporate tax and top-up tax deadlines", "Returns for 31 January 2026 year-ends due by Friday 30 October; multinational groups under the 15% top-up tax must register by 30 November.", "uae-corporate-tax-deadline-30-october-2026-top-up-tax-registration-30-november.html", ("Crowe UAE", "https://www.crowe.com/ae/news/uae-top-up-tax")),
    ("Oct 2026", "H-1B fee in limbo: Indian professionals weigh return", "The US$100,000 H-1B fee is not being collected after court rulings, but the position is unsettled. Returning NRIs should plan RNOR status and US retirement accounts.", "h1b-holders-returning-to-india-tax-rnor-401k-2026.html", ("Forbes", "https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/")),
    ("2026", "Any foreign individual can buy listed Indian shares", "FEMA Schedule III opened beyond NRIs and OCIs: under 10% per individual, 24% aggregate, reported on Form LEC (IFI).", "foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html", ("India Briefing", "https://www.india-briefing.com/news/fema-non-debt-amendment-foreign-individuals-45618.html/")),
    ("16 Aug - 31 Dec 2026", "FAST-DS 2026 foreign asset disclosure window open", "Small taxpayers can declare undisclosed foreign income or assets: up to INR 1 crore at 60%, or up to INR 5 crore of taxed-but-unreported assets for a flat INR 1 lakh. Closes 31 December 2026.", "fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", S_FASTDS[0]),
    ("1 Oct 2026", "No TAN needed to buy property from an NRI", "Resident individual and HUF buyers can pay TDS under their own PAN through Form 141. Rates unchanged: 12.5% long-term, 30% short-term, plus surcharge and cess.", "buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", S_F141[0]),
    ("28 Sep 2026", "Audit-case ITR due date moved to 21 November", "CBDT Circular 07/2026: tax audit report 21 October, ITR 21 November. Transfer pricing cases unchanged: Form 3CEB 31 October, ITR 30 November.", "itr-due-date-21-november-2026-audit-cases-cbdt-circular-07-2026.html", S_CIRC[0]),
    ("8 Oct 2026", "New penalty-waiver form under the Income-tax Act, 2025", "Notification 134/2026 introduced a revised Form 161 for penalty-waiver applications under Section 440(2) of the new Act.", "income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", ("India Briefing", "https://www.india-briefing.com/news/india-income-tax-compliance-calendar-october-2026-47160.html/")),
    ("From 1 Apr 2026", "Section 195 is now Section 393(2)", "The Income-tax Act, 2025 is in force. TDS on payments to non-residents made from 1 April 2026 falls under Section 393(2); TCS, including on LRS remittances, under Section 394.", "income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", S_ACT[0]),
    ("From 1 Apr 2026", "TCS on education and medical remittances cut to 2%", "Self-funded education and medical remittances under LRS: 2% above INR 10 lakh (was 5%). Overseas tour packages: flat 2%. Other LRS remittances: 20% above INR 10 lakh.", "lrs-tcs-calculator.html", S_TCS[0]),
    ("From 1 Jan 2026", "US 1% tax on cash-funded remittances", "Transfers abroad paid in cash, money orders or cashier's checks attract a 1% US excise tax. Bank-account and US card-funded transfers are exempt.", "us-1-percent-remittance-tax-nri-sending-money-to-india-2026.html", S_US[0]),
]

news_rows = "".join(
    f'<li><strong>{d}: {a_title}</strong><br>{text} <a href="{href}">Read more</a> &middot; <a href="{s_url}" rel="nofollow noopener" target="_blank">Source: {s_name}</a></li>'
    for d, a_title, text, href, (s_name, s_url) in NEWS_ITEMS)

PAGES.append(dict(
    slug="india-tax-nri-cross-border-news-october-2026",
    title="India Tax, NRI and Cross-Border News: October 2026 Roundup",
    em="what changed and what to do about it.",
    kicker="/ News &middot; Roundup &middot; Updated 2026-10-30",
    lead=f"The tax and regulatory changes from the last few weeks that matter most to NRIs, Indian founders and foreign companies with Indian operations, each with the action to take. Compiled by {LEAD}.",
    sections=[
        ("/ This month's changes", "Newest first by effect.", "<ul>" + news_rows + "</ul>"),
        ("/ Deadlines in the next 10 weeks", "Put these in the calendar.",
         ul("30 October 2026: AOC-4 for companies whose AGM was on 30 September (additional fee waived until 31 December 2026); LLP Form 8; UAE corporate tax returns for 31 January year-ends.",
            "1 November 2026: GST changes from the 57th GST Council take effect.",
            "31 October 2026: Form 3CEB (transfer pricing report).",
            "21 November 2026: ITR for audit cases.",
            "31 October 2026: MSME Form I for April-September 2026 dues to micro and small suppliers.",
            "29 November 2026: MGT-7/MGT-7A annual return (additional fee waived until 31 January 2027); PAS-6 for the half-year.",
            "30 November 2026: ITR for transfer pricing cases; UAE top-up tax registration for in-scope multinational groups.",
            "15 December 2026: third advance tax instalment.",
            "31 December 2026: belated and revised ITRs for FY 2025-26; FAST-DS declarations; GSTR-9/9C for FY 2025-26.") + updated()),
    ],
    howto=None,
    faqs=[
        ("What are the biggest Indian tax changes in October 2026?", "GST changes from 1 November after the 57th GST Council, retrospective relief for exporters on Rule 96(10), the FAST-DS foreign asset disclosure window (closes 31 December 2026), PAN-based TDS for buying property from NRIs, and the audit-case ITR date moving to 21 November 2026."),
        ("What changed for NRIs in 2026?", "Buyers of NRI property no longer need a TAN, TCS on education and medical remittances fell to 2%, the FAST-DS window opened for undisclosed foreign assets, and the US introduced a 1% tax on cash-funded remittances."),
        ("Is Section 195 still in force?", "For payments made or credited from 1 April 2026, TDS on non-resident payments is under Section 393(2) of the Income-tax Act, 2025."),
        ("Who can help me act on these changes?", f"{LEAD} advises NRIs, Indian founders and foreign companies on each of these changes. " + CONTACT),
    ],
    related=[("nri-tax-services-worldwide-by-country.html", "NRI taxation by country"), ("for-foreign-clients.html", "Services for clients worldwide")],
    cta_h="Not sure which change affects you?",
    cta_b=CONTACT,
    keywords="India tax news October 2026, NRI news October 2026, India tax changes 2026, CBDT news October 2026, India cross-border tax update",
    desc="October 2026 India tax and NRI news: FAST-DS foreign asset disclosure (closes 31 December), no TAN to buy property from NRIs, audit-case ITR due 21 November, Section 195 now 393(2), TCS cut to 2% on education, US 1% remittance tax.",
))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)

print(f"Batch AH complete: {len(PAGES)} news pages")
