# -*- coding: utf-8 -*-
"""Batch DG (19 Nov 2026): foreign-company advisory, part 2 (call-first): China plus one / moving sourcing or
manufacturing to India; technology licensing and royalty payments from India; types of due diligence in India.
Demand: autocomplete sweep 19 Nov 2026 (ac14), all 7 markets: "china plus one strategy india", "companies moving
manufacturing to india", "contract manufacturing in india", "technology transfer agreement india", "royalty payment by
indian company to foreign", "is gst applicable on royalty", "financial due diligence services in india", "legal due
diligence report india".
Facts (checked 19 Nov 2026): section 115BAB (15%) closed to companies starting manufacturing after 31 March 2024, so new
manufacturers use section 115BAA (22% plus surcharge and cess, 25.168%); SEZ income-tax deduction (section 10AA)
unavailable to units starting after 30 June 2020; MOOWR (customs section 65) allows manufacturing in a bonded
warehouse with duty deferred on imported inputs; PLI schemes in 14 sectors; Press Note 3 (2020) - government approval
for investors with beneficial owners in land-border countries, eased by Press Note 2 (2026) for small non-controlling
stakes. Royalty: FEMA allows royalty and technical fee payments for technology collaboration and brand use without
RBI approval or caps (liberalised 2009-2010); withholding 20% plus surcharge and cess (section 115A) or treaty rate
(typically 10% to 15%) with TRC and Form 10F; Indian payer pays 18% GST under reverse charge on imported IP / services
(creditable); transfer pricing for related parties; disallowance if tax not withheld."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 19 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def call_box(topic, agenda, bring):
    msg = f"Hi Durgesh, I would like to schedule a call about {topic} in India. Company: ... Country: ... What we want to do: ... Timeline: ..."
    mail = ("mailto:info@bharatquantumprospera.com?subject=" + quote("Call request: " + topic + " in India")
            + "&body=" + quote("Hi Durgesh,\n\nI would like to schedule a call about " + topic + " in India.\n\nCompany and country:\nWhat we want to do in India:\nTimeline:\nPreferred times (with time zone):\n\nThanks"))
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:18px 20px;margin:20px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 6px;font-weight:700">Schedule a call with CA Durgesh Chavda</p>'
            f'<p style="margin:0 0 10px">The right answer depends on your product, your home country and your Indian counterparty. A short call is the fastest way to get it right. On the call we cover:</p>'
            + ul(*agenda)
            + f'<p style="margin:10px 0 6px"><strong>Helpful to send before the call:</strong> {bring}</p>'
            f'<p style="margin:10px 0 0"><a href="https://topmate.io/cadurgesh_chavda/741484" target="_blank" rel="noopener"><strong>Book a call</strong></a> &middot; '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp +91 78018 87130</strong></a> &middot; '
            f'<a href="{mail}"><strong>Email info@bharatquantumprospera.com</strong></a>. Calls work across time zones. Everything you share is kept confidential.</p></div>')


def sources(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not advice for a specific transaction.</p>'


def contact(what):
    return (f"Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with {what}. "
            "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")


HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
DIST = "find-distributor-business-partner-in-india-foreign-company-agreement-checks-2026"
ACQ = "how-to-acquire-a-company-in-india-foreign-buyer-process-fema-cci-tax-2026"
CP1 = "china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026"
ROY = "technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026"
DDT = "types-of-due-diligence-india-financial-tax-legal-hr-commercial-forensic-esg-2026"

PAGES = []

C_CP1 = contact("your product, annual volumes, current supplier country and whether you want to buy, contract-manufacture or build")
PAGES.append(dict(
    slug=CP1,
    title="China Plus One: Moving Sourcing or Manufacturing to India (2026) - Sourcing, Contract Manufacturing or Your Own Factory, Incentives, Tax and Checks",
    em="for foreign brands, importers and manufacturers.",
    kicker="/ Foreign companies &middot; Manufacturing &middot; China plus one &middot; Updated 2026-11-19",
    lead=("Companies adding India to a China-heavy supply chain usually move in three stages. First they <strong>source from Indian suppliers</strong>, then they use an Indian <strong>contract manufacturer</strong>, then they build their <strong>own factory</strong> through an Indian subsidiary. Each stage needs more diligence and gives more control. "
          "The numbers that decide the business case: a new manufacturing company pays <strong>22% corporate tax plus surcharge and cess (25.168%)</strong>, because the old 15% rate closed to companies starting production after 31 March 2024. <strong>Production-linked incentive (PLI)</strong> schemes cover 14 sectors. Duty on imported inputs can be deferred by manufacturing in a <strong>bonded warehouse (MOOWR)</strong> or in an SEZ. "
          "Two checks come first: whether your group has <strong>beneficial owners in China or another land-border country</strong>, which needs Indian government approval to invest; and whether your supplier or partner is genuine and can deliver quality and volume."),
    sections=[
        ("/ Three ways in", "Compare control, cost and risk.",
         table(["Route", "What you do", "Indian set-up", "Main risks"], [
             ["Source from Indian suppliers", "Buy finished goods or components", "None needed; buy from abroad", "Supplier quality, capacity, documentation; export incentives and rules of origin for your market"],
             ["Contract manufacturing", "Indian manufacturer makes to your specification", "Optional liaison office or quality team; tooling consigned", "IP leakage, quality control, permanent establishment if your staff direct production"],
             ["Own factory", "Indian subsidiary owns or leases the plant", "Private limited company; land, approvals, labour", "Approvals timeline, labour codes, working capital; PLI eligibility conditions"]])
         + call_box("moving sourcing or manufacturing", ["Which route suits your product, volume and timeline",
                                                          "FDI route, including the Press Note 3 position for your group",
                                                          "Tax and duty in outline: corporate tax, PLI, MOOWR or SEZ, GST on inputs",
                                                          "How to check suppliers and contract manufacturers",
                                                          "Entity, people and compliance if you build your own plant"],
                    "product details, annual volumes, current supplier country and your target cost or launch date.")),
        ("/ Incentives, duty and tax", "What changes the landed cost.",
         ul("<strong>Corporate tax:</strong> 25.168% effective under section 115BAA for a new manufacturing company; the 15% concessional regime closed to companies starting manufacturing after 31 March 2024.",
            "<strong>PLI schemes:</strong> production-linked incentives in 14 sectors (for example electronics, pharmaceuticals, auto components, textiles, specialty steel, solar modules) with eligibility thresholds and investment and sales targets; check whether your sector's window is still open.",
            "<strong>Imported inputs:</strong> manufacturing in a customs bonded warehouse (MOOWR) defers duty on imported inputs and removes it for exported output; SEZ units get duty-free inputs (the SEZ income-tax holiday is closed to units starting after 30 June 2020).",
            "<strong>GST:</strong> exports are zero-rated; input tax credit on domestic purchases is refundable for exporters.",
            "<strong>State incentives:</strong> capital subsidies, stamp duty and electricity concessions vary by state; compare two or three states before choosing land.",
            "<strong>Your market:</strong> check current tariffs and rules of origin for the US, EU or UK, which decide whether goods qualify as Indian.")),
        ("/ Checks before you commit", "Where projects go wrong.",
         ul("<strong>Supplier and partner diligence:</strong> company records, financials, GST and export history, litigation, factory audit. See <a href=\"how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html\">verify an Indian company</a> and <a href=\"india-vendor-supplier-verification-foreign-buyer.html\">supplier verification</a>.",
            "<strong>Land-border ownership:</strong> investment by an entity whose beneficial owner is in China or another land-border country needs government approval; small non-controlling stakes were eased in 2026. See <a href=\"press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html\">Press Note 2 (2026)</a>.",
            "<strong>Contract terms:</strong> IP ownership, tooling, quality, exclusivity, audit rights and arbitration.",
            "<strong>Permanent establishment:</strong> your engineers supervising a contract manufacturer for long periods can create a taxable presence; see <a href=\"permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html\">permanent establishment</a>.",
            "<strong>Import-export set-up:</strong> import-export code, customs and GST registration; see <a href=\"india-iec-gst-customs-foreign-exporter-importer-2026.html\">IEC, GST and customs</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="best-ca-pli-scheme-application-foreign-manufacturer.html">PLI applications</a> &middot; <a href="{DIST}.html">finding a partner in India</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up a subsidiary</a>.</p>'
         + sources("Income-tax Act, 2025 (corporate tax regimes carried from sections 115BAA and 115BAB of the 1961 Act); Customs Act, 1962 section 65 and the MOOWR regulations; SEZ Act, 2005; PLI scheme notifications; Press Note 3 (2020) and Press Note 2 (2026).")),
    ],
    faqs=[("What is the China plus one strategy for India?", "Adding India as a second supply base alongside China, usually by sourcing from Indian suppliers first, then contract manufacturing, then building an own factory through an Indian subsidiary."),
          ("What tax does a new manufacturing company pay in India?", "22% plus surcharge and cess (25.168% effective) under section 115BAA. The 15% regime for new manufacturers closed to companies starting manufacturing after 31 March 2024."),
          ("Are there incentives for manufacturing in India?", "Yes: production-linked incentive schemes in 14 sectors, duty deferral on imported inputs through MOOWR or SEZ units, GST refunds for exporters, and state-level subsidies."),
          ("Can a company with Chinese shareholders invest in India?", "It needs Indian government approval if a beneficial owner is in China or another country sharing a land border with India; small non-controlling stakes were eased in 2026."),
          ("Should we contract-manufacture or build our own plant?", "Contract manufacturing is faster and needs less capital; an own plant gives control over quality and IP. Many companies start with a contract manufacturer and build later."),
          ("Can BQP help plan our India move?", "Yes. " + C_CP1)],
    related=[("best-ca-pli-scheme-application-foreign-manufacturer.html", "PLI scheme applications"), ("india-vendor-supplier-verification-foreign-buyer.html", "Supplier verification"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Moving sourcing or manufacturing to India?", cta_b=C_CP1,
    keywords="china plus one India, moving manufacturing to India, companies moving manufacturing to India, contract manufacturing in India foreign company, set up factory in India, PLI scheme foreign manufacturer, MOOWR India, 115BAA manufacturing 2026",
    desc="China plus one: moving sourcing or manufacturing to India (2026). Sourcing, contract manufacturing or own factory; 25.168% corporate tax (15% regime closed after 31 March 2024); PLI in 14 sectors; MOOWR and SEZ; Press Note 3 for land-border owners; supplier checks and PE risk.",
    howto={"name": "How a foreign company moves sourcing or manufacturing to India", "description": "Stages from sourcing to own factory.", "steps": [
        {"name": "Define the product and volume", "text": "Specification, annual volume, target landed cost and timeline."},
        {"name": "Check ownership rules", "text": "Confirm whether Press Note 3 applies to your group."},
        {"name": "Shortlist and check partners", "text": "Supplier or contract manufacturer diligence and factory audits."},
        {"name": "Model tax and duty", "text": "Corporate tax, PLI, MOOWR or SEZ, GST refunds, state incentives."},
        {"name": "Set up and scale", "text": "Contracts, IEC and GST registration; subsidiary and plant when volumes justify it."}]}))

C_ROY = contact("the licensor's country, what is licensed (technology, brand, software), the royalty basis and whether the parties are related")
PAGES.append(dict(
    slug=ROY,
    title="Technology Licensing and Royalty Payments from India to a Foreign Company (2026): FEMA, Withholding Tax, GST Reverse Charge and Transfer Pricing",
    em="for foreign licensors and the Indian companies paying them.",
    kicker="/ Foreign companies &middot; Licensing &middot; Royalty &middot; Updated 2026-11-19",
    lead=("An Indian company can pay royalty or technical fees to a foreign company for technology, know-how, trademarks or software <strong>without RBI approval and without any cap</strong>. India removed those limits in 2009-2010. "
          "The payment carries three Indian costs. The payer <strong>withholds income tax at 20%</strong> plus surcharge and cess under domestic law, or the lower <strong>treaty rate (typically 10% to 15%)</strong> if the licensor gives a tax residency certificate and Form 10F. The payer also <strong>pays 18% GST under reverse charge</strong> on the imported licence, usually recoverable as input credit. If the parties are related, the royalty must be at <strong>arm's length</strong> under transfer pricing. "
          "Get the licence agreement, the withholding certificate and the remittance forms (15CA/15CB) right from the first payment. Tax not withheld means the Indian company also loses the deduction."),
    sections=[
        ("/ What applies to a royalty payment", "At a glance.",
         table(["Point", "Rule", "Who acts"], [
             ["FEMA", "Current account transaction; no RBI approval or cap for technology or brand royalty", "Indian payer through its bank"],
             ["Income-tax withholding", "20% plus surcharge and cess, or treaty rate with TRC and Form 10F (Form 41)", "Indian payer deducts and deposits; files withholding return"],
             ["Remittance forms", "Form 15CA and, where required, CA certificate 15CB (Forms 145/146 under the new rules)", "Payer and its chartered accountant"],
             ["GST", "18% under reverse charge on import of the licence or services; input credit generally available", "Indian payer"],
             ["Transfer pricing", "Arm's-length royalty rate and benchmarking where licensor and licensee are associated enterprises", "Indian company; Form 3CEB"],
             ["Licensor's home tax", "Claims credit for Indian tax withheld under the treaty", "Foreign licensor"]])
         + call_box("technology licensing or royalty payments", ["Whether the payment is royalty, technical fees or business profits under the treaty",
                                                                    "The withholding rate and documents (TRC, Form 10F, no-PE declaration)",
                                                                    "GST reverse charge and credit",
                                                                    "Arm's-length royalty rate for related parties",
                                                                    "Agreement terms: scope, territory, sub-licensing, improvements, audit and termination"],
                    "the draft licence agreement, the licensor's country and the expected annual royalty basis.")),
        ("/ Treaty points that change the answer", "Read the treaty, not just the Act.",
         ul("<strong>Rates:</strong> many of India's treaties set 10% (for example Singapore, UAE, Germany, Japan, Netherlands); the US and UK treaties allow 10% or 15% depending on the type of royalty.",
            "<strong>Fees for technical services:</strong> some treaties (US, UK, Canada, Singapore) tax them only if the services 'make available' technical knowledge to the payer; others tax all technical fees.",
            "<strong>Software:</strong> after the Supreme Court's 2021 Engineering Analysis decision, payments for off-the-shelf software licences are generally not royalty under the treaties.",
            "<strong>Permanent establishment:</strong> if the licensor has a PE in India to which the licence is connected, business-profit rules apply instead.",
            "<strong>Most-favoured-nation clauses</strong> in some treaties were narrowed by the Supreme Court's 2023 Nestle decision; do not assume a lower rate from another treaty.")),
        ("/ Agreement and compliance checklist", "Before the first invoice.",
         ul("Define what is licensed (patents, know-how, trademarks, software) and the royalty base (net sales, units, fixed fee).",
            "Register the trademark and record the licence where useful; see <a href=\"india-trademark-patent-ip-foreign-company.html\">IP for foreign companies</a>.",
            "Collect the TRC, Form 10F and a no-PE declaration from the licensor each year.",
            "Deduct tax at the right rate, deposit it, issue the withholding certificate and file the quarterly return.",
            "Pay GST under reverse charge and claim input credit; keep the invoice and agreement on file.",
            "For related parties, prepare transfer pricing documentation and file Form 3CEB by 31 October (31 October 2026 for FY 2025-26).")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="{DIST}.html">licensing and distribution partners</a> &middot; <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment</a> &middot; <a href="form-3ceb-tp-audit-india-2026-30-november-checklist.html">Form 3CEB</a>.</p>'
         + sources("Foreign Exchange Management (Current Account Transactions) Rules, 2000 as liberalised (technology collaboration and trademark royalty, 2009-2010); Income-tax Act, 2025 (rate carried from section 115A of the 1961 Act; withholding on payments to non-residents); India&rsquo;s tax treaties; IGST Act, 2017 and reverse-charge notifications; Engineering Analysis Centre of Excellence v. CIT (Supreme Court, 2021); AO v. Nestle SA (Supreme Court, 2023).")),
    ],
    faqs=[("Can an Indian company pay royalty to a foreign company?", "Yes. Royalty and technical fees for technology, know-how, trademarks or software can be paid without RBI approval and without any cap, through the company's bank with the remittance forms."),
          ("What TDS applies on royalty paid to a foreign company?", "20% plus surcharge and cess under domestic law, or the lower treaty rate (often 10% or 15%) if the foreign company provides a tax residency certificate and Form 10F."),
          ("Is GST applicable on royalty paid abroad?", "Yes. The Indian payer pays 18% GST under reverse charge on the imported licence or service, and can usually claim it back as input tax credit."),
          ("Is a software licence payment a royalty?", "Payments for off-the-shelf software licences are generally not royalty under India's treaties after the Supreme Court's 2021 Engineering Analysis decision, but customised software and other cases need review."),
          ("Does transfer pricing apply to royalty?", "Yes, when the licensor and licensee are associated enterprises: the royalty must be at arm's length and documented, with Form 3CEB filed."),
          ("Can BQP set up the royalty process?", "Yes. " + C_ROY)],
    related=[("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment"), ("india-trademark-patent-ip-foreign-company.html", "IP for foreign companies"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Licensing technology or a brand to India?", cta_b=C_ROY,
    keywords="royalty payment by Indian company to foreign company, technology transfer agreement India, technology licensing India foreign company, TDS on royalty to non-resident, is GST applicable on royalty, royalty treaty rate India, transfer pricing royalty India",
    desc="Technology licensing and royalty payments from India to a foreign company (2026): no RBI approval or cap, 20% withholding or treaty rate with TRC and Form 10F, 18% GST reverse charge, 15CA/15CB, transfer pricing, software royalty after Engineering Analysis, and licence terms.",
    howto={"name": "How an Indian company pays royalty to a foreign licensor", "description": "Steps for compliant payments.", "steps": [
        {"name": "Sign the licence", "text": "Define the licensed rights, territory and royalty basis."},
        {"name": "Collect treaty documents", "text": "TRC, Form 10F and no-PE declaration from the licensor."},
        {"name": "Withhold and remit", "text": "Deduct tax at the right rate, file 15CA/15CB, remit through the bank."},
        {"name": "Pay GST", "text": "Pay 18% under reverse charge and claim input credit."},
        {"name": "Document", "text": "Transfer pricing study and Form 3CEB for related parties; withholding returns and certificates."}]}))

C_DDT = contact("the type of transaction, the target's sector and size, and your deadline")
PAGES.append(dict(
    slug=DDT,
    title="Types of Due Diligence in India (2026): Financial, Tax, Legal, HR, Commercial, Forensic and ESG - What Each Covers and What the Report Contains",
    em="for foreign buyers, investors, lenders and partners.",
    kicker="/ Foreign buyers &middot; Due diligence &middot; Updated 2026-11-19",
    lead=("Due diligence on an Indian company usually combines <strong>financial</strong> (quality of earnings, net debt, working capital), <strong>tax</strong> (income tax, withholding, GST, transfer pricing), <strong>legal and regulatory</strong> (title, contracts, licences, litigation, FEMA) and <strong>HR</strong> (employment terms, provident fund and labour-code compliance). "
          "Larger or riskier deals add <strong>commercial</strong> (market and customers), <strong>forensic</strong> (fraud, related parties, cash leakage), <strong>IT and data</strong>, and <strong>ESG</strong> reviews. "
          "The scope should match the deal: a supplier check may take days, while a full acquisition review takes weeks. In India, <strong>FEMA history and indirect-tax compliance</strong> are the two areas foreign buyers most often underestimate. A chartered accountant usually leads the financial, tax and FEMA work, and lawyers handle the legal opinion."),
    sections=[
        ("/ The main types", "What each one answers.",
         table(["Type", "Key question", "Typical work in India"], [
             ["Financial", "Are the earnings, debt and working capital what they seem?", "Quality of earnings, normalisation, net debt and debt-like items, working capital trends, related-party transactions"],
             ["Tax", "What tax could we inherit?", "Income-tax assessments and notices, TDS/TCS compliance, GST returns and input credit, transfer pricing, past restructurings"],
             ["FEMA and regulatory", "Was foreign money handled correctly?", "FC-GPR, FC-TRS, ODI, ECB and annual returns; pricing on past share issues; sector licences"],
             ["Legal", "Do they own what they sell and can they keep operating?", "Title to assets and IP, material contracts, change-of-control clauses, litigation, approvals (by lawyers)"],
             ["HR and labour", "Are people costs and liabilities complete?", "Provident fund and ESI, gratuity, bonus, contractor use, labour-code compliance, key-person terms"],
             ["Commercial", "Is the market and customer story real?", "Customer interviews, concentration, pricing, competition"],
             ["Forensic", "Is anything hidden?", "Related parties, cash and round-tripping, vendor and payroll anomalies, background checks on promoters"],
             ["IT and data", "Are systems and data safe and compliant?", "Systems, cyber security, DPDP Act readiness"],
             ["ESG", "Any environmental, social or governance exposure?", "Pollution consents, safety, governance practices"]])
         + call_box("due diligence", ["Which types of diligence your deal actually needs",
                                       "Red-flag areas specific to the target's sector",
                                       "How the work splits between us, Indian lawyers and specialists",
                                       "Data room requests and management access",
                                       "Timeline and the report format your investment committee wants"],
                    "the target's name or sector, approximate size, the deal type (acquisition, investment, JV, loan, supplier) and your deadline.")),
        ("/ What the report contains", "A typical structure.",
         ul("<strong>Executive summary:</strong> key findings ranked by money and risk, deal-breakers, price adjustments.",
            "<strong>Financial:</strong> adjusted EBITDA, net debt and debt-like items, normalised working capital.",
            "<strong>Tax and FEMA:</strong> quantified exposures with probability, and what to cover by indemnity, escrow or pre-closing fixes.",
            "<strong>SPA points:</strong> specific indemnities, warranties, conditions precedent and completion-accounts mechanics.",
            "<strong>Post-deal actions:</strong> compliance fixes, integration steps and the first 100 days.")),
        ("/ Choosing the scope", "Match effort to risk.",
         ul("<strong>Supplier or distributor check:</strong> background, financial and compliance check; see <a href=\"how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html\">verify an Indian company</a>.",
            "<strong>Minority investment:</strong> financial, tax, FEMA and legal red-flag review.",
            "<strong>Acquisition or JV:</strong> full financial, tax, FEMA, legal and HR, plus commercial or forensic as needed; see <a href=\"" + ACQ + ".html\">acquiring an Indian company</a>.",
            "<strong>Selling or raising:</strong> vendor (sell-side) diligence first; see <a href=\"sell-side-due-diligence-india-selling-indian-company-to-foreign-buyer-2026.html\">sell-side due diligence</a>.")
         + f'<p>Related: <a href="transaction-due-diligence-india-for-global-buyers.html">transaction due diligence</a> &middot; <a href="due-diligence-indian-company-foreign-buyer.html">due diligence for foreign buyers</a> &middot; <a href="india-counterparty-background-check-compliance-dd.html">counterparty background checks</a> &middot; <a href="{HUB}.html">working with an Indian CA</a>.</p>'
         + sources("Companies Act, 2013; Income-tax Act, 2025; CGST/IGST Acts; Foreign Exchange Management (Non-Debt Instruments) Rules, 2019; labour codes and Employees&rsquo; Provident Funds scheme; Digital Personal Data Protection Act, 2023.")),
    ],
    faqs=[("What types of due diligence are done in India?", "Financial, tax, FEMA/regulatory, legal and HR are the core; commercial, forensic, IT/data and ESG are added for larger or riskier deals."),
          ("Who performs financial due diligence in India?", "Usually chartered accountants, who also cover tax and FEMA; legal due diligence is done by lawyers, and specialists handle technical or environmental reviews."),
          ("What does a financial due diligence report contain?", "An executive summary of key findings, adjusted EBITDA, net debt and debt-like items, normalised working capital, quantified tax exposures and recommended contract protections."),
          ("What do foreign buyers most often miss in Indian targets?", "Gaps in FEMA filings on past foreign investment and indirect-tax (GST) issues, both of which can be costly to fix after completion."),
          ("How long does due diligence take?", "From a few days for a supplier check to several weeks for an acquisition, depending on scope, data room quality and management access."),
          ("Can BQP run due diligence for us?", "Yes. " + C_DDT)],
    related=[("transaction-due-diligence-india-for-global-buyers.html", "Transaction due diligence"), ("sell-side-due-diligence-india-selling-indian-company-to-foreign-buyer-2026.html", "Sell-side due diligence"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Need due diligence on an Indian company?", cta_b=C_DDT,
    keywords="types of due diligence India, financial due diligence India, tax due diligence India, legal due diligence India, HR due diligence India, forensic due diligence India, financial due diligence report India, due diligence services India foreign buyer",
    desc="Types of due diligence in India (2026): financial, tax, FEMA, legal, HR, commercial, forensic, IT/data and ESG; what each covers, what the report contains, and how to match scope to a supplier check, investment, acquisition or sale.",
    howto={"name": "How to scope due diligence on an Indian company", "description": "Steps for foreign buyers and investors.", "steps": [
        {"name": "Define the deal", "text": "Supplier, investment, acquisition, JV or loan, and the decision you need to make."},
        {"name": "Pick the types", "text": "Core financial, tax, FEMA, legal and HR; add commercial, forensic, IT or ESG by risk."},
        {"name": "Agree the data room", "text": "Request list, management access and timeline."},
        {"name": "Run and report", "text": "Findings ranked by money and risk, with SPA protections."},
        {"name": "Act on it", "text": "Price, indemnities, escrow, pre-closing fixes and post-deal actions."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DG complete:", len(PAGES))
