# -*- coding: utf-8 -*-
"""Batch DJ (19 Nov 2026): downstream investment by a foreign-owned Indian company; bank and demat accounts in India for
a foreign company (SNRR changes of June 2026). Call-first pages.
Demand: autocomplete sweep 19 Nov 2026 (ac15), all 7 markets: "downstream investment in india", "downstream investment
by indian companies", "can a foreign company open current account in india", "can a foreign company open a demat
account in india".
Facts (checked 19 Nov 2026): NDI Rules rule 23 and the Master Direction - an Indian company owned (more than 50%) or
controlled by non-residents is a foreign-owned or controlled company; its downstream investment counts as indirect
foreign investment and must meet sectoral caps, entry route and pricing; funding from internal accruals, funds
raised abroad or share swaps (valued by a registered merchant banker), not domestic borrowings; deferred consideration
up to 25% within 18 months; Form DI on FIRMS within 30 days of allotment; notify DPIIT within 30 days; board
resolution and shareholders' agreement where applicable; annual statutory auditor certificate, confirmed in the
directors' report; NRI/OCI-owned companies investing on a non-repatriation basis are treated as domestic; draft FEMA
(Foreign Investment) Rules, 2026 issued 21 July 2026 propose a 'foreign controlled entity' concept (not yet in force)
- Vinod Kothari (22 Oct 2026), JSA, AZB. SNRR: FEMA (Deposit) (Sixth Amendment) Regulations, 2026, notification FEMA
5(R)(6)/2026-RB dated 18 June 2026 - business-interest requirement removed, accounts with AD banks, their overseas
branches and IFSC branches, permissible current and capital account transactions and bona fide transactions with
other non-residents; old seven-year limit paragraphs deleted (King Stubb & Kasiva, 16 Jul 2026). Ordinary current
accounts need an Indian presence (liaison/branch/project office or subsidiary). Unlisted public companies and private
companies (other than small companies) must issue and hold securities in demat form (Rule 9A / 9B)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
ACQ = "how-to-acquire-a-company-in-india-foreign-buyer-process-fema-cci-tax-2026"
DS = "downstream-investment-india-foreign-owned-company-fema-form-di-funding-rules-2026"
BA = "foreign-company-bank-account-in-india-snrr-current-account-demat-2026"

PAGES = []

C_DS = contact("the group structure, the foreign shareholding of the investing company, the target and the sector")
PAGES.append(dict(
    slug=DS,
    title="Downstream Investment in India by a Foreign-Owned Company (2026): When It Counts as Foreign Investment, Funding Rules, Pricing and Form DI",
    em="for foreign groups with Indian holding or operating companies.",
    kicker="/ Foreign groups &middot; FEMA &middot; Indirect foreign investment &middot; Updated 2026-11-19",
    lead=("When an Indian company that is <strong>owned (more than 50%) or controlled by non-residents</strong> invests in another Indian company or LLP, the investment is <strong>indirect foreign investment</strong>. It must follow the same rules as direct FDI: the <strong>sector cap, the approval route and the pricing rules</strong>. What cannot be done directly cannot be done indirectly. "
          "The investing company must fund the investment from <strong>internal accruals, money raised abroad, or a share swap</strong>. It <strong>cannot use money borrowed in India</strong>. "
          "It reports the investment in <strong>Form DI within 30 days</strong> of allotment on the RBI's FIRMS portal and notifies DPIIT within 30 days. Its statutory auditor certifies compliance every year. "
          "Companies owned and controlled by NRIs or OCIs that invest on a non-repatriation basis are treated as domestic. In July 2026 RBI issued <strong>draft Foreign Investment Rules</strong> that would redefine these entities, but they are not yet in force."),
    sections=[
        ("/ Does the rule apply to you?", "Ownership and control tests.",
         table(["Situation", "Indirect foreign investment?", "Notes"], [
             ["Indian company more than 50% owned by non-residents invests in an Indian company", "Yes", "Sector cap, route and pricing apply to the target"],
             ["Indian company controlled by non-residents (right to appoint a majority of directors or control management or policy) invests", "Yes", "Even if foreign shareholding is 50% or less"],
             ["Indian company owned and controlled by resident Indians invests", "No", "Domestic investment"],
             ["NRI- or OCI-owned company investing on a non-repatriation basis", "No", "Treated as domestic under Schedule IV"],
             ["Company becomes foreign-owned after it already made investments", "Yes, from the date of reclassification", "Report in Form DI within 30 days of the change"]])
         + call_box("downstream investment", ["Whether your Indian company is foreign-owned or controlled",
                                               "Sector caps, approval route and pricing for the target",
                                               "How to fund the investment within the rules",
                                               "Form DI, DPIIT notification and the auditor's certificate",
                                               "Whether a share swap or deferred consideration helps"],
                    "a group structure chart, the investing company's shareholding and board rights, and details of the target.")),
        ("/ The rules in practice", "Funding, pricing and reporting.",
         ul("<strong>Funding:</strong> internal accruals (post-tax profits transferred to reserves), equity or debt raised from abroad, or a share swap valued by a registered merchant banker; not domestic borrowings (non-convertible debentures subscribed by non-residents are not treated as domestic borrowing).",
            "<strong>Pricing:</strong> buy from residents at no less than fair value; buy from non-residents at no more than fair value.",
            "<strong>Deferred consideration:</strong> up to 25% of the price, within 18 months of the agreement, if not used to get around the rules.",
            "<strong>Reporting:</strong> Form DI on FIRMS within 30 days of allotment, with the standard declaration; notify DPIIT within 30 days.",
            "<strong>Governance:</strong> board resolution, and a shareholders' agreement where applicable.",
            "<strong>Annual check:</strong> the statutory auditor certifies compliance; the directors' report confirms it, and a qualified certificate must be reported to the RBI regional office.",
            "<strong>LLPs:</strong> a foreign-owned LLP can invest downstream only in sectors open to 100% automatic-route FDI without performance conditions.")),
        ("/ Common structures and problems", "What we see.",
         ul("<strong>Indian holding company</strong> owning several operating companies: plan funding from abroad or accruals, since bank loans in India cannot fund the downstream investment.",
            "<strong>Acquisitions by an Indian subsidiary</strong> of a foreign group: pricing, sector cap and Form DI apply; see <a href=\"" + ACQ + ".html\">acquiring an Indian company</a>.",
            "<strong>Missed Form DI filings:</strong> regularise with the late submission fee or compounding; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.",
            "<strong>Draft rules:</strong> the July 2026 draft FEMA (Foreign Investment) Rules would replace the current concept with a 'foreign controlled entity'; watch for the final text before restructuring.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">subsidiary set-up</a> &middot; <a href="press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html">Press Note 2 (2026)</a>.</p>'
         + sources("Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (rule 23 and Schedule IV); RBI Master Direction on Foreign Investment in India (updated January 2025); Foreign Exchange Management (Mode of Payment and Reporting of Non-Debt Instruments) Regulations; RBI draft FEMA (Foreign Investment) Rules, 2026 (21 July 2026). Commentary checked 19 November 2026: Vinod Kothari Consultants (22 October 2026), JSA, AZB &amp; Partners, Trilegal.")),
    ],
    faqs=[("What is downstream investment in India?", "An investment by an Indian company or LLP that is owned or controlled by non-residents into another Indian company or LLP; it is treated as indirect foreign investment and must follow FDI rules."),
          ("When is an Indian company foreign-owned or controlled?", "When non-residents hold more than 50% of its equity, or have the right to appoint a majority of its directors or otherwise control its management or policy decisions."),
          ("Can downstream investment be funded with an Indian bank loan?", "No. It must be funded from internal accruals, funds raised from abroad or a share swap; domestic borrowings are not allowed."),
          ("What is Form DI?", "The report of downstream investment filed on the RBI's FIRMS portal within 30 days of allotment of the equity instruments, alongside a notification to DPIIT within 30 days."),
          ("Does it apply to NRI-owned companies?", "Not if the company is owned and controlled by NRIs or OCIs and the investment is on a non-repatriation basis; that is treated as domestic investment."),
          ("Can BQP review our group structure?", "Yes. " + C_DS)],
    related=[("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding"), (ACQ + ".html", "Acquiring an Indian company"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Investing through an Indian subsidiary?", cta_b=C_DS,
    keywords="downstream investment India, downstream investment by Indian companies, indirect foreign investment India, FOCC downstream investment rules, Form DI 30 days, downstream investment domestic borrowing, foreign owned or controlled company India 2026",
    desc="Downstream investment in India by a foreign-owned company (2026): owned (over 50%) or controlled by non-residents; sector caps, route and pricing apply; funded from internal accruals, foreign funds or share swaps, not domestic borrowing; Form DI and DPIIT within 30 days; auditor certificate; draft 2026 rules.",
    howto={"name": "How a foreign-owned Indian company makes a downstream investment", "description": "Compliance steps.", "steps": [
        {"name": "Confirm status", "text": "Test ownership (over 50%) and control by non-residents."},
        {"name": "Check the target's sector", "text": "Sector cap, approval route and any conditions."},
        {"name": "Arrange compliant funding", "text": "Internal accruals, funds from abroad or a share swap; no domestic borrowing."},
        {"name": "Price and approve", "text": "Fair-value report, board resolution, shareholders' agreement."},
        {"name": "Report", "text": "Form DI within 30 days, DPIIT notification, annual auditor certificate."}]}))

C_BA = contact("your company's country, whether you have or plan an Indian office or subsidiary, and what the account is for")
PAGES.append(dict(
    slug=BA,
    title="Can a Foreign Company Open a Bank Account or Demat Account in India? (2026) SNRR Account, Current Account Through an Indian Entity, and Demat for FDI Shares",
    em="for foreign companies paying, receiving or investing in rupees.",
    kicker="/ Foreign companies &middot; Banking &middot; FEMA &middot; Updated 2026-11-19",
    lead=("A foreign company with <strong>no Indian office or subsidiary</strong> cannot open an ordinary current account in India, but it can open a <strong>Special Non-Resident Rupee (SNRR) account</strong>. Since the <strong>June 2026 amendment</strong> to the FEMA deposit rules, an SNRR account no longer requires a 'business interest in India'. It can be opened with an Indian bank, its overseas branch or a GIFT City (IFSC) branch, and used for <strong>permitted current and capital account transactions</strong>, including bona fide dealings with other non-residents. The old seven-year limit was also removed. "
          "Once the company has a <strong>liaison, branch or project office</strong> or an <strong>Indian subsidiary</strong>, that entity opens normal current accounts. "
          "For investments, foreign shareholders of most Indian private companies must hold their shares in <strong>demat form</strong>, so they open a <strong>demat account</strong> with an Indian depository participant. Portfolio investment in listed shares goes through the <strong>FPI</strong> route."),
    sections=[
        ("/ Which account for which purpose", "Pick by presence and use.",
         table(["Need", "Account", "Who opens it", "Notes"], [
             ["Receive or pay rupees without an Indian entity (trade, services, investment flows)", "SNRR account", "The foreign company with an Indian AD bank, its overseas branch or an IFSC branch", "Since June 2026: no business-interest test; permitted current and capital account transactions; NRO-to-SNRR transfers allowed within limits"],
             ["Run day-to-day operations in India", "Current account", "Indian subsidiary, or the liaison/branch/project office", "Normal KYC on the entity and its foreign shareholders and signatories"],
             ["Hold FDI shares in an Indian company", "Demat account with an Indian depository participant", "Foreign shareholder", "Private companies other than small companies must issue and hold securities in demat form"],
             ["Invest in listed securities as a portfolio investor", "FPI registration plus demat and custody", "Foreign fund or company", "Through a designated depository participant and custodian"],
             ["Indian exporter keeping foreign currency", "EEFC account", "The Indian company", "Not for the foreign company itself"]])
         + call_box("banking and accounts in India", ["Whether you need an SNRR account, an Indian entity, or both",
                                                       "What the 2026 SNRR changes allow for your transactions",
                                                       "KYC documents and how to avoid repeated bank queries",
                                                       "Demat for FDI shares and the related FEMA filings",
                                                       "Tax withholding on payments into and out of the account"],
                    "your company documents, the purpose of the account and the expected transactions.")),
        ("/ SNRR accounts after the June 2026 amendment", "What changed.",
         ul("<strong>Who:</strong> any person resident outside India; the 'business interest in India' requirement was removed.",
            "<strong>Where:</strong> with authorised dealer banks in India, their overseas branches, and IFSC branches in GIFT City.",
            "<strong>Use:</strong> permissible current and capital account transactions, and bona fide transactions with other non-residents processed by the bank on your instructions.",
            "<strong>Tenure:</strong> the paragraphs that set the earlier seven-year limit were deleted; confirm the bank's own terms.",
            "<strong>Transfers:</strong> transfers from NRO accounts to SNRR accounts are now permitted, subject to the remittance-of-assets limits.",
            "<strong>Tax:</strong> interest and payments through the account follow normal Indian withholding rules; the account does not change who must deduct tax.")),
        ("/ Practical points", "Before you approach a bank.",
         ul("Expect KYC on the company, its beneficial owners and signatories, with apostilled documents.",
            "State the purpose and expected transactions clearly; banks now apply a principles-based check on each use.",
            "If you will hire staff, sign leases or invoice Indian customers regularly, an Indian entity is usually needed anyway; see <a href=\"can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html\">registering a company</a> and <a href=\"rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html\">liaison and branch offices</a>.",
            "Demat for unlisted shares: see <a href=\"rule-9b-demat-missed-fundraising-blocked-urgent-india.html\">Rule 9B demat requirement</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">subsidiary set-up</a>.</p>'
         + sources("Foreign Exchange Management (Deposit) Regulations, 2016 as amended by the Sixth Amendment Regulations, 2026 (notification FEMA 5(R)(6)/2026-RB, 18 June 2026); RBI Master Direction on Deposits and Accounts; Companies (Prospectus and Allotment of Securities) Rules, 2014 (rules 9A and 9B); SEBI (Foreign Portfolio Investors) Regulations. Commentary checked 19 November 2026: King Stubb &amp; Kasiva (16 July 2026), Kotak Mahindra Bank, Canara Bank.")),
    ],
    faqs=[("Can a foreign company open a bank account in India?", "Without an Indian entity it can open a Special Non-Resident Rupee (SNRR) account; with a liaison, branch or project office or an Indian subsidiary, that entity opens normal current accounts."),
          ("What changed for SNRR accounts in 2026?", "The FEMA Deposit (Sixth Amendment) Regulations of 18 June 2026 removed the business-interest requirement, allowed accounts at overseas and IFSC branches of Indian banks, covered permitted current and capital account transactions, and deleted the earlier seven-year limit."),
          ("Can a foreign company open a current account in India?", "Not directly without an Indian presence. Its Indian subsidiary or office can; otherwise it uses an SNRR account."),
          ("Can a foreign company open a demat account in India?", "Yes. Foreign shareholders holding FDI shares in Indian companies open demat accounts with Indian depository participants, and portfolio investors use the FPI route."),
          ("Is interest on an SNRR account taxable in India?", "Payments and interest follow normal Indian tax and withholding rules; the account type does not create an exemption."),
          ("Can BQP help open accounts and handle KYC?", "Yes. " + C_BA)],
    related=[("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Registering a company"), ("rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html", "Liaison and branch offices"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Need an Indian bank or demat account?", cta_b=C_BA,
    keywords="can a foreign company open bank account in India, can a foreign company open current account in India, SNRR account 2026, SNRR business interest removed, can a foreign company open demat account in India, foreign company rupee account India",
    desc="Can a foreign company open a bank or demat account in India (2026)? SNRR account without an Indian entity (June 2026 amendment: no business-interest test, overseas and IFSC branches, current and capital account transactions, seven-year limit deleted); current accounts via an Indian entity; demat for FDI shares; FPI route.",
    howto={"name": "How a foreign company sets up banking in India", "description": "Choosing and opening accounts.", "steps": [
        {"name": "Define the purpose", "text": "Trade payments, investment flows, operations or holding shares."},
        {"name": "Choose the account", "text": "SNRR without an entity; current account through a subsidiary or office; demat for shares."},
        {"name": "Prepare KYC", "text": "Apostilled company documents, beneficial owner and signatory KYC."},
        {"name": "Open and document", "text": "State expected transactions; keep invoices and agreements for each flow."},
        {"name": "Stay compliant", "text": "Withholding tax, FEMA reporting and annual KYC updates."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DJ complete:", len(PAGES))
