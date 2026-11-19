# -*- coding: utf-8 -*-
"""Batch DH (19 Nov 2026): RBI approval to establish a place of business in India (liaison, branch, project office) and
franchising a foreign brand in India. Call-first pages.
Demand: autocomplete sweep 19 Nov 2026 (ac14), all 7 markets: "rbi approval to establish a place of business in
india", "certificate for establishment of place of business in india", "place of business in india", "franchise india
brands", "franchise india international brands".
Facts (checked 19 Nov 2026): 2016 Regulations still in force (India Briefing, 13 May 2026: the October 2025 draft
'Establishment in India of a branch or office' Regulations not yet notified); 2016 criteria - branch office: profit
in the preceding five years and net worth at least USD 100,000; liaison office: profit in the preceding three years
and net worth at least USD 50,000; letter of comfort from parent if the applicant falls short; application in Form FNC
through an AD Category-I bank; RBI prior approval (with Government consultation) for applicants from Pakistan,
Bangladesh, Sri Lanka, Afghanistan, Iran, China, Hong Kong and Macau, for defence, telecom, private security and
information & broadcasting sectors, and for NGOs/non-profits; UIN allotted; liaison office validity three years
(extendable); Form FC-1 with the ROC within 30 days of establishment; annual activity certificate by 30 September. Draft
proposes removing net worth/profit criteria, a negative list, no tenure limit. Franchise: royalty and franchise fees
are current-account payments without RBI approval; withholding 20% plus surcharge and cess or treaty rate (e.g. 10%
UAE) with TRC and Form 10F; 18% GST reverse charge; FDI in single-brand retail 100% automatic (30% local sourcing
above 51%); multi-brand retail 51% government route; no franchise-specific statute in India."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
ROY = "technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026"
DIST = "find-distributor-business-partner-in-india-foreign-company-agreement-checks-2026"
POB = "rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026"
FR = "franchise-foreign-brand-in-india-master-franchise-royalty-tax-gst-trademark-2026"

PAGES = []

C_POB = contact("your company's country, what the Indian office will do, your last three to five years' results and your preferred city")
PAGES.append(dict(
    slug=POB,
    title="RBI Approval to Establish a Place of Business in India (2026): Liaison, Branch or Project Office - Eligibility, Form FNC, Who Needs RBI Approval and After-Approval Filings",
    em="for foreign companies opening an office in India.",
    kicker="/ Foreign companies &middot; Liaison office &middot; Branch office &middot; Updated 2026-11-19",
    lead=("A foreign company that wants a <strong>liaison office, branch office or project office</strong> in India applies in <strong>Form FNC</strong> through an Indian <strong>authorised dealer (AD Category-I) bank</strong>. The bank approves most cases under the RBI's 2016 regulations. "
          "Under those regulations a branch office needs <strong>profits in each of the last five years and a net worth of at least USD 100,000</strong>. A liaison office needs <strong>profits in the last three years and a net worth of at least USD 50,000</strong>. A parent's letter of comfort can fill the gap. "
          "<strong>RBI approval</strong> (with government consultation) is needed for applicants from Pakistan, Bangladesh, Sri Lanka, Afghanistan, Iran, China, Hong Kong or Macau, for the defence, telecom, private security and broadcasting sectors, and for non-profits. "
          "After approval, the office gets a <strong>unique identification number</strong>, registers with the ROC in <strong>Form FC-1 within 30 days</strong>, and files an <strong>Annual Activity Certificate by 30 September</strong> each year. RBI's October 2025 draft would drop the net worth and profit tests, but as of the latest reports the 2016 rules still apply."),
    sections=[
        ("/ Which office, and what it may do", "Pick by activity.",
         table(["Office", "What it may do", "Income in India?", "Eligibility (2016 rules)"], [
             ["Liaison office", "Represent the parent, promote trade and technical or financial collaboration, act as a communication channel", "No; expenses funded by remittances from the parent", "Profits in the preceding 3 years; net worth at least USD 50,000; validity usually 3 years, extendable"],
             ["Branch office", "Export and import, professional or consultancy services, research, technical support, representing the parent as buying or selling agent", "Yes; taxed as a foreign company", "Profits in the preceding 5 years; net worth at least USD 100,000"],
             ["Project office", "Execute a specific contract in India", "Yes, from the project", "A contract with an Indian company, funded from abroad or by Indian/multilateral funding as specified"],
             ["Subsidiary (alternative)", "Any activity allowed under FDI policy", "Yes; taxed as an Indian company at lower rates", "No RBI office approval; incorporate and file FC-GPR"]])
         + call_box("opening a liaison, branch or project office", ["Whether an office or a subsidiary suits your activity and tax position",
                                                                     "Eligibility and whether a letter of comfort is needed",
                                                                     "Whether your country or sector needs RBI approval",
                                                                     "Documents, apostille and the AD bank process",
                                                                     "Post-approval registrations and annual compliance"],
                    "the parent's last three to five years' audited accounts, the planned activity in India and the city.")),
        ("/ The process", "From application to operating.",
         ul("<strong>Documents:</strong> Form FNC, certificate of incorporation and constitutional documents, last audited financial statements (or a CPA-certified net worth), board resolution, KYC of the parent and its authorised signatory, and a letter of comfort if needed; foreign documents notarised and apostilled or consularised.",
            "<strong>AD bank review:</strong> the bank checks eligibility and KYC and approves, or forwards to the RBI where RBI approval is required; the RBI allots a unique identification number.",
            "<strong>After approval:</strong> Form FC-1 with the Registrar of Companies within 30 days; PAN and TAN; bank account; GST registration for a branch or project office that makes taxable supplies.",
            "<strong>Every year:</strong> audited accounts and the Annual Activity Certificate by 30 September to the AD bank and the income-tax department; a branch files an income-tax return. See <a href=\"liaison-office-branch-office-annual-activity-certificate-aac-form-49c-162-india-2026.html\">annual activity certificate</a>.",
            "<strong>Closing or converting:</strong> closure through the AD bank with auditor's certificates, or conversion to a subsidiary; see <a href=\"branch-office-vs-liaison-vs-wos-india-foreign.html\">liaison vs branch vs subsidiary</a>.")),
        ("/ What is changing", "RBI's draft regulations.",
         ul("<strong>Status:</strong> RBI issued draft 'Establishment in India of a branch or office' Regulations in October 2025; reports in May 2026 said they were not yet notified, so check the current position when you apply.",
            "<strong>Proposed:</strong> no profit or net worth test, a negative list of prohibited activities instead of a permitted list, no tenure limit for liaison offices, more offices without prior RBI approval, and a simpler route for changes of ownership.",
            "<strong>Unchanged in principle:</strong> AD bank processing, security-related approvals for certain countries and sectors, and annual reporting.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="project-office-india-foreign-company-registration-fema-conditions-tax-2026.html">project office</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">subsidiary set-up</a> &middot; <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment</a>.</p>'
         + sources("Foreign Exchange Management (Establishment in India of a branch office or a liaison office or a project office or any other place of business) Regulations, 2016 and the RBI Master Direction; RBI draft Establishment in India of a branch or office Regulations, 2025; Companies (Registration of Foreign Companies) Rules, 2014. Secondary summaries checked 19 November 2026: India Briefing (13 May 2026), Vinod Kothari Consultants, Nishith Desai Associates.")),
    ],
    faqs=[("How does a foreign company get approval for a place of business in India?", "It applies in Form FNC through an AD Category-I bank in India, which approves most liaison, branch and project office applications under the 2016 regulations; some countries and sectors need RBI approval."),
          ("What are the eligibility criteria for a liaison or branch office?", "Under the 2016 rules, a branch office needs profits in the preceding five years and net worth of at least USD 100,000; a liaison office needs profits in the preceding three years and net worth of at least USD 50,000. A parent's letter of comfort can help."),
          ("Who needs RBI approval rather than just the bank?", "Applicants from Pakistan, Bangladesh, Sri Lanka, Afghanistan, Iran, China, Hong Kong or Macau; offices in defence, telecom, private security or information and broadcasting; and non-profit organisations."),
          ("What is filed after approval?", "Form FC-1 with the ROC within 30 days, PAN and tax registrations, and each year the audited accounts and Annual Activity Certificate by 30 September."),
          ("Is the net worth requirement being removed?", "RBI's October 2025 draft proposes removing the profit and net worth tests, but as of the latest reports the 2016 regulations were still in force; check before applying."),
          ("Can BQP handle the application?", "Yes. " + C_POB)],
    related=[("branch-office-vs-liaison-vs-wos-india-foreign.html", "Liaison vs branch vs subsidiary"), ("liaison-office-branch-office-annual-activity-certificate-aac-form-49c-162-india-2026.html", "Annual activity certificate"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Opening an office in India?", cta_b=C_POB,
    keywords="RBI approval to establish a place of business in India, liaison office approval India, branch office India eligibility net worth, Form FNC, certificate for establishment of place of business in India, project office India approval, FC-1 30 days, liaison office 2026 draft regulations",
    desc="RBI approval for a place of business in India (2026): liaison, branch or project office via Form FNC through an AD bank; 2016 criteria (BO: 5 years' profit, USD 100,000; LO: 3 years, USD 50,000); RBI approval for certain countries and sectors; FC-1 within 30 days; AAC by 30 September; RBI's 2025 draft.",
    howto={"name": "How a foreign company establishes a liaison or branch office in India", "description": "Steps under the 2016 regulations.", "steps": [
        {"name": "Choose the office type", "text": "Liaison, branch or project office, or a subsidiary instead."},
        {"name": "Check eligibility", "text": "Profit record and net worth, or a parent's letter of comfort; country and sector approvals."},
        {"name": "Apply in Form FNC", "text": "Through an AD Category-I bank with apostilled documents."},
        {"name": "Register after approval", "text": "UIN from RBI; Form FC-1 within 30 days; PAN, TAN, bank account, GST if needed."},
        {"name": "Comply every year", "text": "Audited accounts and Annual Activity Certificate by 30 September; tax filings."}]}))

C_FR = contact("your brand, home country, the format (unit, area or master franchise) and any Indian partner you are talking to")
PAGES.append(dict(
    slug=FR,
    title="Franchising a Foreign Brand in India (2026): Master or Unit Franchise, Partner Checks, Royalty Tax, GST, Trademark and FDI Rules",
    em="for international brands entering India through franchising.",
    kicker="/ Foreign brands &middot; Franchising &middot; Updated 2026-11-19",
    lead=("Most international brands enter India through a <strong>master franchise</strong> (one Indian partner develops the whole country or a region and may sub-franchise), an <strong>area developer</strong>, or <strong>unit franchises</strong>. Some later move to a joint venture or their own subsidiary. "
          "India has <strong>no franchise-specific law</strong>, so the franchise agreement, trademark registration and tax set-up do the protecting. The Indian franchisee can pay franchise fees and royalties to the foreign franchisor <strong>without RBI approval</strong>. It withholds <strong>tax at 20%</strong> plus surcharge and cess, or the lower <strong>treaty rate</strong> (10% under the UAE treaty, for example) if the franchisor gives a tax residency certificate and Form 10F. It also pays <strong>18% GST under reverse charge</strong>. "
          "If the franchisor takes equity in the Indian business, <strong>FDI rules</strong> apply: 100% under the automatic route for single-brand retail, with 30% local sourcing above 51%, and 51% with government approval for multi-brand retail."),
    sections=[
        ("/ Franchise models", "Choose by control and capital.",
         table(["Model", "How it works", "Watch"], [
             ["Master franchise", "One Indian partner gets national or regional rights and opens or sub-franchises outlets", "Partner's capital and execution capacity; development schedule; exit and step-in rights"],
             ["Area developer", "Partner must open a set number of outlets in a territory, no sub-franchising", "Realistic opening targets; territory definitions by state or city"],
             ["Unit franchise", "Franchisor contracts directly with each outlet owner", "Needs your own India support team; may create a permanent establishment"],
             ["JV or subsidiary franchising", "Franchisor holds equity in the master franchisee", "FDI route for the sector; shareholders' agreement; transfer pricing on royalties"]])
         + call_box("franchising our brand", ["Which franchise model fits your brand and capital",
                                               "How to check a prospective master franchisee",
                                               "Royalty and fee structure, withholding tax and GST",
                                               "Trademark protection and agreement terms",
                                               "Whether equity or a JV changes the FDI position"],
                    "your brand deck, home country, target cities and any Indian partners you are talking to.")),
        ("/ Tax and money flows", "What the franchisee pays and withholds.",
         ul("<strong>FEMA:</strong> initial fees, royalties and other franchise payments are current-account remittances without RBI approval, made through the franchisee's bank with Forms 15CA/15CB (145/146).",
            "<strong>Withholding:</strong> 20% plus surcharge and cess under domestic law, or the treaty rate (often 10% to 15%) with a TRC and Form 10F; a franchisor without a PAN should give the details required by the rules to avoid a higher rate.",
            "<strong>GST:</strong> the franchisee pays 18% under reverse charge on the imported franchise service and can usually claim credit.",
            "<strong>Permanent establishment:</strong> franchisor staff stationed in India to run training or supervision for long periods can create a taxable presence.",
            "<strong>Transfer pricing:</strong> applies if the franchisor and franchisee are associated enterprises.",
            "More detail: <a href=\"" + ROY + ".html\">royalty payments from India</a>.")),
        ("/ Protect the brand and the deal", "Before you sign.",
         ul("<strong>Trademark:</strong> register your marks in India in your own name before disclosing your system; see <a href=\"india-trademark-patent-ip-foreign-company.html\">IP for foreign companies</a>.",
            "<strong>Partner checks:</strong> company and financial records, existing franchise performance, litigation and references; see <a href=\"how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html\">verify an Indian company</a>.",
            "<strong>Agreement:</strong> territory, development schedule, fees, audit rights, quality standards, supply obligations, non-compete, termination and step-in, arbitration seat.",
            "<strong>Licences for outlets:</strong> FSSAI for food, shop and establishment registration, trade licences and fire safety, obtained by the franchisee.",
            "<strong>Competition law:</strong> resale price maintenance and exclusive supply clauses should be reviewed.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="{DIST}.html">distributors and partners</a> &middot; <a href="joint-venture-in-india-with-foreign-company-structure-fdi-shareholders-agreement-exit-2026.html">joint ventures</a>.</p>'
         + sources("Foreign Exchange Management (Current Account Transactions) Rules, 2000 as liberalised; Consolidated FDI Policy (single-brand and multi-brand retail); Income-tax Act, 2025 and India&rsquo;s tax treaties; IGST Act, 2017 (import of services, reverse charge); Trade Marks Act, 1999; Competition Act, 2002. Secondary commentary checked 19 November 2026: Khaitan &amp; Co (Legal 500 franchise guide), ATB Legal, TaxGuru.")),
    ],
    faqs=[("How can a foreign brand franchise in India?", "Usually through a master franchise or area developer with an Indian partner, or unit franchises supported by the brand; there is no franchise-specific law, so the agreement and trademark registration matter most."),
          ("Can an Indian franchisee pay royalty to a foreign franchisor?", "Yes, without RBI approval. The franchisee withholds tax at 20% plus surcharge and cess or the lower treaty rate with a TRC and Form 10F, and remits through its bank with Forms 15CA/15CB."),
          ("Is GST payable on franchise fees paid abroad?", "Yes. The Indian franchisee pays 18% GST under reverse charge and can usually claim input tax credit."),
          ("Can the foreign franchisor own part of the Indian franchisee?", "Yes, subject to FDI rules: single-brand retail allows 100% under the automatic route (30% local sourcing above 51%), while multi-brand retail is capped at 51% with government approval."),
          ("Should I register my trademark before franchising in India?", "Yes. Register it in India in your own name before you disclose your system or sign with a partner."),
          ("Can BQP help us franchise in India?", "Yes. " + C_FR)],
    related=[(ROY + ".html", "Royalty payments from India"), ("india-trademark-patent-ip-foreign-company.html", "IP for foreign companies"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Bringing your brand to India?", cta_b=C_FR,
    keywords="franchise foreign brand in India, master franchise India, international franchise India, franchise royalty TDS India, GST on franchise fee foreign franchisor, single brand retail FDI franchise, franchise agreement India 2026",
    desc="Franchising a foreign brand in India (2026): master, area or unit franchise; no franchise law, so agreement and trademark matter; royalty without RBI approval, 20% or treaty withholding, 18% GST reverse charge; PE and transfer pricing; FDI for single-brand and multi-brand retail.",
    howto={"name": "How a foreign brand franchises in India", "description": "Steps from model choice to first outlet.", "steps": [
        {"name": "Choose the model", "text": "Master franchise, area developer, unit franchise or JV."},
        {"name": "Protect the brand", "text": "Register trademarks in India before disclosing your system."},
        {"name": "Check the partner", "text": "Financial, legal and track-record checks on the master franchisee."},
        {"name": "Set the money flows", "text": "Fee structure, withholding with TRC and Form 10F, GST reverse charge."},
        {"name": "Sign and launch", "text": "Agreement with development schedule and step-in rights; outlet licences."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DH complete:", len(PAGES))
