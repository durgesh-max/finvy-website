# -*- coding: utf-8 -*-
"""Batch DF (19 Nov 2026): foreign companies looking for an Indian professional - hub plus joint venture, acquiring an
Indian company, finding a distributor/partner, and sell-side due diligence. Every page pushes a scheduled call.
Demand: autocomplete sweep 19 Nov 2026 (ac13), all 7 markets: "joint venture in india with foreign company", "how to
acquire a company in india", "acquisition company in india", "find distributors in india", "how to find distributors
for my product in india", "sell my business to overseas buyers", "india business consultant for foreign companies".
Facts (checked 19 Nov 2026):
- FDI: sector caps and routes per Consolidated FDI Policy; land-border beneficial owners need government approval
  (Press Note 3 of 2020, eased by Press Note 2 of 2026 for small non-controlling stakes - site page); the old Press
  Note 1 (2005) requirement for an existing Indian JV partner's NOC was removed in 2011.
- NDI Rules: issue/transfer to non-residents at not less than fair value (exit by non-resident at not more than fair
  value); optionality clauses allowed with minimum one-year lock-in and no assured exit price; deferred consideration
  or escrow up to 25% of total consideration within 18 months of the transfer agreement (rule 9(6)); FC-GPR within 30
  days of allotment, FC-TRS within 60 days of receipt/remittance of consideration.
- Competition Act: deal value threshold INR 2,000 crore with substantial business operations in India (from 10 Sept
  2024); de minimis target exemption - Indian assets up to INR 450 crore or Indian turnover up to INR 1,250 crore; DVT
  overrides de minimis (AZB, Cyril Amarchand, Trilegal, Morgan Lewis summaries).
- SEBI Takeover Regulations: open offer when acquiring 25% or more of a listed company.
- Stamp duty on share transfer 0.015%; seller taxed on capital gains (unlisted shares held over 24 months: 12.5%
  long-term); income-tax deemed FMV rules for unlisted shares (section 50CA / 56(2)(x) of the 1961 Act); loss carry-
  forward of a closely held company lapses when shareholding with voting power changes by more than 49% (section 79,
  1961 Act; carried into the 2025 Act).
- Royalty / fees for technical services to a foreign partner: 20% under domestic law (section 115A) or treaty rate.
- No Indian statute gives distributors or agents goodwill compensation on termination (contract governs); Competition
  Act covers vertical restraints such as resale price maintenance; dependent agent PE if an agent habitually concludes
  contracts for the foreign company."""
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
    """Schedule-a-call box: what the call covers and what to send before it."""
    msg = f"Hi Durgesh, I would like to schedule a call about {topic} in India. Company: ... Country: ... What we want to do: ... Timeline: ..."
    mail = ("mailto:info@bharatquantumprospera.com?subject=" + quote("Call request: " + topic + " in India")
            + "&body=" + quote("Hi Durgesh,\n\nI would like to schedule a call about " + topic + " in India.\n\nCompany and country:\nWhat we want to do in India:\nTimeline:\nPreferred times (with time zone):\n\nThanks"))
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:18px 20px;margin:20px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 6px;font-weight:700">Schedule a call with CA Durgesh Chavda</p>'
            f'<p style="margin:0 0 10px">Every India plan depends on your sector, your home country and who your partner is. A short call is the fastest way to get it right. On the call we cover:</p>'
            + ul(*agenda)
            + f'<p style="margin:10px 0 6px"><strong>Helpful to send before the call:</strong> {bring}</p>'
            f'<p style="margin:10px 0 0"><a href="book-a-call.html"><strong>Book a call</strong></a> &middot; '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp +91 78018 87130</strong></a> &middot; '
            f'<a href="{mail}"><strong>Email info@bharatquantumprospera.com</strong></a>. Calls work across time zones (the Gulf, Europe, the UK, the US, Singapore and Australia). Everything you share is kept confidential.</p></div>')


def sources(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not advice for a specific transaction.</p>'


def contact(what):
    return (f"Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with {what}. "
            "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")


HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
JV = "joint-venture-in-india-with-foreign-company-structure-fdi-shareholders-agreement-exit-2026"
ACQ = "how-to-acquire-a-company-in-india-foreign-buyer-process-fema-cci-tax-2026"
DIST = "find-distributor-business-partner-in-india-foreign-company-agreement-checks-2026"
SELL = "sell-side-due-diligence-india-selling-indian-company-to-foreign-buyer-2026"

PAGES = []

# ---------------- HUB ----------------
C_HUB = contact("your company, country, what you want to do in India and your timeline")
PAGES.append(dict(
    slug=HUB,
    title="Working with an Indian CA as a Foreign Company (2026): Market Research, Entity Set-Up, Due Diligence, M&A, Joint Ventures and Partnerships",
    em="what foreign businesses ask an Indian professional for, and how the first call works.",
    kicker="/ Foreign companies &middot; Investors &middot; India advisory &middot; Updated 2026-11-19",
    lead=("Foreign companies and investors usually come to an Indian chartered accountant with one of eight questions. Is there a market for us in India? Which entity or place of business should we set up? Is this Indian company, supplier or partner genuine? What will we find in due diligence before we buy or invest? How do we acquire an Indian company, or sell one? How should a joint venture be structured? How do we appoint a distributor or licensee, or set up a capability centre? And what will tax, FEMA and the filings cost us each year? "
          "Each answer depends on your sector, your home country's treaty with India and who your Indian counterparty is. That is why the work starts with a <strong>call with CA Durgesh Chavda</strong>: we map your objective, the regulatory route, the diligence you need, the timeline and the documents, then send a written scope."),
    sections=[
        ("/ What foreign businesses ask us for", "And where to read more.",
         table(["You want to", "What we do", "Read"], [
             ["Test the Indian market", "Market and regulatory research: demand, competitors, pricing and landed cost, licences, tax on your business model", '<a href="india-market-research-foreign-company.html">India market research</a>'],
             ["Set up in India", "Choose and set up a subsidiary, LLP, branch, liaison or project office, or use an employer of record; bank account, tax and GST registration", '<a href="india-market-entry-foreign-company-guide.html">market entry guide</a> &middot; <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">entity options</a> &middot; <a href="rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html">RBI approval for an office</a> &middot; <a href="can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html">registering as a foreign national</a> &middot; <a href="foreign-company-bank-account-in-india-snrr-current-account-demat-2026.html">bank accounts</a>'],
             ["Check a company, supplier or partner", "Background and financial checks from MCA, GST, court and credit records, site visits through partners", '<a href="how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html">verify an Indian company</a>'],
             ["Buy or invest", "Buy-side financial, tax and FEMA due diligence; valuation; deal structuring; completion filings", f'<a href="{ACQ}.html">acquiring an Indian company</a> &middot; <a href="transaction-due-diligence-india-for-global-buyers.html">transaction due diligence</a> &middot; <a href="types-of-due-diligence-india-financial-tax-legal-hr-commercial-forensic-esg-2026.html">types of due diligence</a>'],
             ["Sell to a foreign buyer (Indian owners)", "Sell-side (vendor) due diligence, clean-up of tax and FEMA gaps, data room, valuation", f'<a href="{SELL}.html">sell-side due diligence</a>'],
             ["Form a joint venture", "Structure, FDI route, shareholders' agreement terms, valuation, tax on royalties and dividends", f'<a href="{JV}.html">joint ventures in India</a>'],
             ["Distribute, license or manufacture", "Partner checks, distributor and licence terms, PE and withholding tax, product registrations", f'<a href="{DIST}.html">finding a distributor or partner</a> &middot; <a href="technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html">licensing and royalty</a> &middot; <a href="china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026.html">moving manufacturing to India</a> &middot; <a href="franchise-foreign-brand-in-india-master-franchise-royalty-tax-gst-trademark-2026.html">franchising</a>'],
             ["Build a team or GCC", "Capability centre set-up, transfer pricing safe harbour, payroll and compliance", '<a href="gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html">GCC set-up</a>'],
             ["Stay compliant", "Accounting, tax, transfer pricing, FEMA and ROC filings for your Indian entity", '<a href="get-capital-back-from-indian-subsidiary-dividend-buyback-capital-reduction-tax-2026.html">getting money back</a> &middot; <a href="downstream-investment-india-foreign-owned-company-fema-form-di-funding-rules-2026.html">downstream investment</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">all services for foreign companies</a>']])
         + call_box("our India plans", ["Your objective and the realistic routes (entity, partner, acquisition or JV)",
                                        "FDI route and approvals for your sector and ownership",
                                        "The diligence or research you need and what it will show",
                                        "Tax, FEMA and annual compliance in outline",
                                        "Timeline, documents and next steps; we follow up with a written scope"],
                    "a one-paragraph description of the business, your home country, the Indian counterparty (if any) and any deadline.")),
        ("/ How an engagement runs", "From first call to completion.",
         ul("<strong>1. Call:</strong> we listen, ask the questions that change the answer, and tell you plainly if you do not need us yet.",
            "<strong>2. Written scope:</strong> what we will do, what we need from you, the timeline and a fixed fee.",
            "<strong>3. Work:</strong> research, diligence or set-up, with weekly updates in your time zone and a named point of contact.",
            "<strong>4. Report and decision:</strong> findings in plain English, red flags ranked by money and risk, and what to put in the contract.",
            "<strong>5. Completion and after:</strong> FEMA and ROC filings, then ongoing compliance if you want it.")),
        ("/ Who you will speak with", "Entity facts.",
         ul("<strong>CA Durgesh Chavda</strong>, chartered accountant, leads every engagement personally.",
            "<strong>Bharat Quantum Prospera Private Limited</strong>, Ahmedabad, India: tax, FEMA, company law, due diligence and cross-border advisory for foreign companies, investors and NRIs.",
            "Work involving other disciplines (Indian legal opinions, environmental or technical diligence) is coordinated with specialist firms on your instructions.")
         + sources("Consolidated FDI Policy; Foreign Exchange Management (Non-Debt Instruments) Rules, 2019; Companies Act, 2013; Competition Act, 2002; Income-tax Act, 2025.")),
    ],
    faqs=[("Why would a foreign company need an Indian chartered accountant?", "For market and regulatory research, choosing and setting up the Indian entity, checking Indian companies and partners, buy-side or sell-side due diligence, structuring acquisitions and joint ventures, and running tax, FEMA and company-law compliance afterwards."),
          ("What happens on the first call?", "We discuss your objective, the possible routes, FDI approvals, the diligence or research you need, tax and compliance in outline, and the timeline. Afterwards we send a written scope and fixed fee."),
          ("Can you work with our lawyers and advisers abroad?", "Yes. We regularly work alongside foreign counsel, accountants and investment bankers, and coordinate Indian legal and technical specialists where needed."),
          ("Do you work across time zones?", "Yes. Calls are scheduled for the Gulf, Europe, the UK, the US, Singapore and Australia."),
          ("How do I schedule a call?", "Use the book-a-call page, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with a short description of what you want to do in India."),
          ("Can BQP help with our India plans?", "Yes. " + C_HUB)],
    related=[("india-market-entry-foreign-company-guide.html", "India market entry guide"), ("transaction-due-diligence-india-for-global-buyers.html", "Transaction due diligence"),
             ("india-services-for-foreign-companies-complete-list.html", "Services for foreign companies")],
    cta_h="Planning something in India?", cta_b=C_HUB,
    keywords="Indian CA for foreign companies, India business consultant for foreign companies, India market entry advisor, due diligence India foreign buyer, joint venture India advisor, acquire company in India advisor, schedule call Indian chartered accountant",
    desc="How foreign companies work with an Indian CA (2026): market research, entity and place of business, company and partner checks, buy-side and sell-side due diligence, acquisitions, joint ventures, distribution, GCCs and compliance - and how the first call with CA Durgesh Chavda works.",
    howto={"name": "How a foreign company starts working with an Indian CA", "description": "From first call to completion.", "steps": [
        {"name": "Schedule a call", "text": "Share a short description of the business, your country, the Indian counterparty and your timeline."},
        {"name": "Agree the scope", "text": "Receive a written scope, timeline and fixed fee."},
        {"name": "Do the work", "text": "Research, diligence or set-up with weekly updates in your time zone."},
        {"name": "Decide", "text": "Get findings ranked by money and risk, and the points to put in your contract."},
        {"name": "Complete and comply", "text": "File FEMA and ROC forms and run ongoing compliance if needed."}]}))

# ---------------- JV ----------------
C_JV = contact("your sector, the proposed Indian partner, the intended shareholding and what each side contributes")
PAGES.append(dict(
    slug=JV,
    title="Joint Venture in India with a Foreign Company (2026): Structures, FDI Route, Shareholders' Agreement, Valuation, Tax and Exit",
    em="for foreign companies partnering with an Indian business.",
    kicker="/ Foreign companies &middot; Joint ventures &middot; FDI &middot; Updated 2026-11-19",
    lead=("A foreign company usually forms a joint venture in India as a new <strong>private limited company</strong> owned with an Indian partner. Less often it uses an LLP (only in sectors open to 100% automatic-route FDI without conditions) or a purely contractual JV. "
          "Before signing, check four things. First, the <strong>FDI route and cap</strong> for the sector: most sectors allow 100% under the automatic route, while some need government approval, as does any investor with a beneficial owner in a country sharing a land border with India. Second, the <strong>valuation</strong>: shares must be issued to the foreign partner at no less than fair value. Third, the <strong>exit terms</strong>: put and call options are allowed with a one-year lock-in but <strong>no assured return</strong>. Fourth, the <strong>tax cost</strong> of royalties, technical fees and dividends paid to the foreign partner. "
          "Most JV disputes come from a weak shareholders' agreement and a partner who was never properly checked, so diligence on the partner comes first."),
    sections=[
        ("/ JV structures", "Which one fits.",
         table(["Structure", "When it fits", "Watch"], [
             ["Equity JV company (private limited)", "Long-term business with shared ownership; most common", "FDI cap and route; board and reserved matters; FC-GPR within 30 days of share allotment"],
             ["LLP", "Services businesses in sectors open to 100% automatic FDI without conditions", "Cannot be used where FDI conditions apply; fewer investors familiar with it"],
             ["Contractual JV (consortium, cooperation agreement)", "Single project or tender; no new entity", "Permanent establishment risk for the foreign party; liability allocation"],
             ["Technology or brand licence with minority stake", "Foreign party contributes know-how, Indian party runs the business", "Royalty withholding and transfer pricing; IP ownership on exit"]])
         + call_box("a joint venture", ["Whether a JV is the right route or a subsidiary, licence or acquisition fits better",
                                        "FDI route, approvals and the Press Note 3 position",
                                        "Valuation and how contributions (cash, technology, brand) are priced",
                                        "Key shareholders' agreement terms: board, reserved matters, deadlock, exit",
                                        "Diligence on the Indian partner and the tax cost of payments between you"],
                    "the proposed partner's name, the sector, the intended shareholding and what each side brings.")),
        ("/ Shareholders' agreement: points that matter in India", "Agree them before money moves.",
         ul("<strong>Board and reserved matters:</strong> list the decisions that need both partners (budget, borrowing, related-party transactions, new business, auditor) and put them in the articles of association so they bind the company.",
            "<strong>Exit:</strong> put and call options are permitted under the FEMA Non-Debt Instruments Rules with a minimum one-year lock-in and no assured exit price; a non-resident cannot exit above fair value, and a resident cannot buy out the foreign partner below it.",
            "<strong>Deadlock:</strong> escalation, then buy-sell (shotgun) or put/call at fair value, then winding up as a last resort.",
            "<strong>Non-compete and conflicts:</strong> the Indian partner's other businesses, use of the JV's customers and staff.",
            "<strong>Dispute resolution:</strong> arbitration with a neutral seat (Singapore, London or India) is common; India enforces foreign awards under the New York Convention.",
            "<strong>Related-party payments:</strong> royalties, technical fees, management charges and supplies between the JV and either partner need board approval and arm's-length pricing.",
            "<strong>Competition law:</strong> a JV can be notifiable to the Competition Commission of India if the asset, turnover or deal value thresholds are met.")),
        ("/ Tax and compliance", "What the JV and the partners pay and file.",
         ul("<strong>JV company:</strong> 22% plus surcharge and cess (25.168%) under section 115BAA, or the regular rate.",
            "<strong>Royalty and technical fees to the foreign partner:</strong> withholding at 20% under domestic law (plus surcharge and cess) or the lower treaty rate with a tax residency certificate and Form 10F; transfer pricing documentation applies.",
            "<strong>Dividends to the foreign partner:</strong> 20% under domestic law or the treaty rate (for example 10% or 15% depending on the treaty and shareholding).",
            "<strong>FEMA:</strong> FC-GPR within 30 days of allotment; annual FLA return; FC-TRS on any later share transfer between resident and non-resident.",
            "<strong>History:</strong> the old rule requiring an existing Indian JV partner's no-objection for a new venture in the same field was removed in 2011; today the shareholders' agreement governs.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html">Press Note 2 (2026)</a> &middot; <a href="how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html">checking an Indian partner</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">wholly owned subsidiary</a>.</p>'
         + sources("Consolidated FDI Policy; Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (pricing and optionality); Press Note 3 (2020) and Press Note 2 (2026); Companies Act, 2013; Competition Act, 2002; Income-tax Act, 2025. Secondary commentary checked 19 November 2026: TaxGuru, BCAJ, JSA.")),
    ],
    faqs=[("Can a foreign company form a joint venture in India?", "Yes. Most sectors allow up to 100% foreign investment under the automatic route, so a foreign company can hold any agreed share in a JV company with an Indian partner, subject to sector caps, approvals for some sectors and Press Note 3 for land-border investors."),
          ("What is the best structure for a JV in India?", "Usually a private limited company with a shareholders' agreement whose key terms are also written into the articles. LLPs suit some services businesses; contractual JVs suit single projects."),
          ("Can a JV agreement give the foreign partner a guaranteed exit price?", "No. Put and call options are allowed with a one-year lock-in, but the exit must be at a price based on fair value at the time of exit, without an assured return."),
          ("Does the JV need approval from the Competition Commission?", "Only if the parties or the deal cross the asset, turnover or deal value thresholds; many small JVs are exempt, but it should be checked."),
          ("How do we check the Indian partner?", "Company records, financial statements, GST and tax compliance, litigation, related parties and reputation, before signing a term sheet."),
          ("Can BQP help structure our JV?", "Yes. " + C_JV)],
    related=[(HUB + ".html", "Working with an Indian CA"), ("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026)"),
             ("foreign-company-setup-indian-subsidiary-wos.html", "Wholly owned subsidiary")],
    cta_h="Planning a joint venture in India?", cta_b=C_JV,
    keywords="joint venture in India with foreign company, JV structure India FDI, shareholders agreement India foreign partner, put option FEMA one year lock-in, joint venture company India 2026, find JV partner India, JV tax royalty India",
    desc="Joint venture in India with a foreign company (2026): equity JV, LLP or contractual JV; FDI route and Press Note 3; fair-value pricing; put/call options with one-year lock-in and no assured return; shareholders' agreement terms; CCI; tax on royalties and dividends; FC-GPR.",
    howto={"name": "How a foreign company forms a joint venture in India", "description": "Steps from partner search to completion.", "steps": [
        {"name": "Check the partner", "text": "Financial, tax, legal and reputation checks on the Indian partner."},
        {"name": "Confirm the FDI route", "text": "Sector cap, automatic or government route, Press Note 3."},
        {"name": "Agree the term sheet", "text": "Shareholding, contributions, board, reserved matters, exit and deadlock."},
        {"name": "Value and incorporate", "text": "Fair-value report, incorporate or subscribe, embed rights in the articles."},
        {"name": "File and run", "text": "FC-GPR within 30 days, transfer pricing, annual FEMA and ROC filings."}]}))

# ---------------- ACQUISITION ----------------
C_ACQ = contact("the target's sector, approximate size, the stake you want and your timeline")
PAGES.append(dict(
    slug=ACQ,
    title="How to Acquire a Company in India as a Foreign Buyer (2026): Process, Due Diligence, FEMA Pricing, CCI, Tax and Completion Filings",
    em="for foreign strategic buyers, PE funds and family offices.",
    kicker="/ Foreign buyers &middot; M&A &middot; FEMA &middot; Updated 2026-11-19",
    lead=("A foreign buyer acquires an Indian company in six steps. <strong>Check the FDI route</strong> for the sector (most are automatic, some need government approval, and so do buyers with land-border beneficial owners). Run <strong>due diligence</strong>. Agree a <strong>price at no less than fair value</strong> backed by a valuation report. Get <strong>Competition Commission</strong> approval if the deal crosses the thresholds (for example a deal value above <strong>INR 2,000 crore</strong> where the target has substantial Indian operations). Sign with escrow or deferred payment of <strong>up to 25% for up to 18 months</strong> if needed. Complete and file <strong>Form FC-TRS within 60 days</strong> of the payment. "
          "A listed target adds a <strong>SEBI open offer</strong> at 25%. The Indian sellers pay capital gains tax. The buyer pays <strong>0.015% stamp duty</strong> on the share transfer and should check whether the target's tax losses survive the change of ownership."),
    sections=[
        ("/ The process", "Typical sequence for a share purchase.",
         table(["Stage", "What happens", "Indian points"], [
             ["1. Screening", "Identify target, initial call, NDA", "Check the sector's FDI cap and route; land-border ownership in your group"],
             ["2. Term sheet", "Price range, structure, exclusivity", "Share purchase vs asset purchase (slump sale) vs fresh issue; earn-outs"],
             ["3. Due diligence", "Financial, tax, legal, FEMA, labour, IT", "Past FC-GPR / FC-TRS filings, GST and TDS defaults, related-party loans, pending notices"],
             ["4. Valuation", "Fair value report", "FEMA: no less than fair value by a CA, SEBI-registered merchant banker or cost accountant; income-tax fair market value rules"],
             ["5. Approvals", "Regulatory clearances", "Government route if applicable; CCI if thresholds are met; sector regulators (RBI, IRDAI, SEBI) for regulated targets"],
             ["6. Signing and completion", "SPA, escrow, closing", "Escrow or deferred consideration up to 25% within 18 months; stamp duty 0.015%; FC-TRS within 60 days; ROC filings and board changes"]])
         + call_box("acquiring a company", ["Whether the target's sector allows your stake and which route applies",
                                            "Share deal vs asset deal and the tax cost of each",
                                            "The diligence scope that fits the deal size and risk",
                                            "Valuation, escrow, earn-out and CCI questions",
                                            "Timeline from term sheet to FC-TRS"],
                    "the target's name or sector, approximate revenue, the stake you want, and any letter of intent.")),
        ("/ Due diligence: what usually comes up", "Red flags we look for in Indian targets.",
         ul("<strong>FEMA history:</strong> late or missing FC-GPR, FC-TRS, ODI or annual return filings; these need compounding before or at completion. See <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.",
            "<strong>Tax:</strong> TDS defaults, GST input credit mismatches, pending assessments and notices, transfer pricing on related-party dealings.",
            "<strong>Company law:</strong> loans to directors, unfiled forms, share issues without proper valuation or approvals.",
            "<strong>Revenue quality:</strong> customer concentration, cash sales, related-party revenue.",
            "<strong>People and contracts:</strong> key employees, change-of-control clauses, leases and licences in the promoters' personal names.",
            "See also <a href=\"transaction-due-diligence-india-for-global-buyers.html\">transaction due diligence</a> and <a href=\"due-diligence-indian-company-foreign-buyer.html\">due diligence for foreign buyers</a>.")),
        ("/ Tax and filings", "Who pays what.",
         ul("<strong>Sellers:</strong> taxed on capital gains (long-term at 12.5% on unlisted shares held over 24 months for residents); if a seller is non-resident, the buyer must withhold tax from the price.",
            "<strong>Price below fair market value:</strong> income-tax deems fair market value for the seller and can tax the buyer on the shortfall, so price and valuation must line up.",
            "<strong>Losses:</strong> a closely held company's carried-forward business losses generally lapse when more than 49% of voting shareholding changes hands.",
            "<strong>Stamp duty:</strong> 0.015% of the consideration on a share transfer; asset deals attract state stamp duty on property and goods, but a business transferred as a going concern is exempt from GST.",
            "<strong>FEMA:</strong> FC-TRS within 60 days of receipt or remittance of consideration; then FLA return annually.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="form-fc-trs-filing-checklist-india-2026.html">FC-TRS checklist</a> &middot; <a href="{SELL}.html">sell-side due diligence</a> &middot; <a href="{JV}.html">joint ventures</a>.</p>'
         + sources("Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (pricing; rule 9(6) deferred consideration); Competition Act, 2002 and the 2024 deal value threshold and de minimis notifications; SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011; Indian Stamp Act; Income-tax Act, 2025. Law-firm summaries checked 19 November 2026: AZB &amp; Partners, Cyril Amarchand Mangaldas, Trilegal, Morgan Lewis, Treelife.")),
    ],
    faqs=[("Can a foreign company acquire an Indian company?", "Yes. In most sectors a foreign buyer can acquire up to 100% under the automatic route; some sectors have caps or need government approval, and buyers with beneficial owners in land-border countries need approval."),
          ("What price must a foreign buyer pay for Indian shares?", "No less than fair value, determined by a chartered accountant, SEBI-registered merchant banker or practising cost accountant using an internationally accepted method; listed shares follow SEBI pricing."),
          ("When is Competition Commission approval needed?", "When the parties or target cross the asset or turnover thresholds and the de minimis exemption does not apply, or when the deal value exceeds INR 2,000 crore and the target has substantial business operations in India."),
          ("Can part of the price be paid later?", "Yes. Up to 25% of the total consideration can be deferred or held in escrow for up to 18 months from the transfer agreement, within the pricing rules."),
          ("What filing is needed after an acquisition?", "Form FC-TRS within 60 days of receipt or remittance of the consideration, plus ROC filings for board changes and the annual FLA return."),
          ("Can BQP run the diligence and filings?", "Yes. " + C_ACQ)],
    related=[("transaction-due-diligence-india-for-global-buyers.html", "Transaction due diligence"), ("form-fc-trs-filing-checklist-india-2026.html", "FC-TRS checklist"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Looking at an acquisition in India?", cta_b=C_ACQ,
    keywords="how to acquire a company in India, foreign company acquire Indian company, acquisition process India foreign buyer, CCI deal value threshold 2000 crore, FC-TRS acquisition, deferred consideration 25 percent 18 months, buy Indian company shares 2026",
    desc="How to acquire a company in India as a foreign buyer (2026): FDI route, due diligence, fair-value pricing, CCI (INR 2,000 crore deal value threshold, de minimis exemption), SEBI open offer, escrow up to 25% for 18 months, seller tax, stamp duty 0.015%, loss lapse and FC-TRS within 60 days.",
    howto={"name": "How a foreign buyer acquires an Indian company", "description": "Share purchase steps.", "steps": [
        {"name": "Confirm the FDI route", "text": "Check the sector cap, approval route and land-border ownership."},
        {"name": "Run due diligence", "text": "Financial, tax, FEMA, legal and labour review of the target."},
        {"name": "Value and agree the price", "text": "Fair-value report; escrow or deferred consideration within 25% and 18 months."},
        {"name": "Get approvals", "text": "Government route, CCI and sector regulators where applicable."},
        {"name": "Complete and file", "text": "Stamp duty, FC-TRS within 60 days, ROC filings and board changes."}]}))

# ---------------- DISTRIBUTOR / PARTNER ----------------
C_DIST = contact("your product or service, target customers in India, and any partners you are already talking to")
PAGES.append(dict(
    slug=DIST,
    title="Finding a Distributor or Business Partner in India (2026): Where to Look, How to Check Them, Agreement Terms, Tax and Product Registrations",
    em="for foreign brands and manufacturers selling into India.",
    kicker="/ Foreign companies &middot; Distribution &middot; Partners &middot; Updated 2026-11-19",
    lead=("Most foreign companies start selling in India through a <strong>distributor</strong> who buys and resells your product, an <strong>agent</strong> on commission, a <strong>licensee or franchisee</strong>, or a <strong>contract manufacturer</strong>. They set up their own entity later. "
          "Good leads come from your home country's trade service and embassy commercial section, Indian export promotion councils and industry associations, trade fairs and existing customers. "
          "Before signing, <strong>check the partner</strong>: company and GST records, financial statements, litigation and references. Then sign an agreement covering <strong>territory and exclusivity, minimum purchases, pricing, trademark ownership, termination and arbitration</strong>. India has no statute that pays distributors compensation when an agreement ends, so the contract decides. "
          "A buy-sell distributor rarely creates tax exposure for you, but an agent who habitually concludes contracts in your name can create a <strong>permanent establishment</strong>."),
    sections=[
        ("/ Partner models compared", "Choose by control and risk.",
         table(["Model", "How it works", "Your tax and risk"], [
             ["Importer-distributor", "Buys from you, imports, resells in India", "Low permanent-establishment risk; distributor needs an import-export code and product registrations"],
             ["Commission agent", "Finds customers; you sell directly", "Dependent agent PE risk if the agent concludes contracts; GST on commission"],
             ["Licensing or franchise", "Partner uses your brand or technology for a royalty", "Royalty withholding (20% domestic or treaty rate); protect the trademark in India first"],
             ["Contract manufacturing", "Indian manufacturer makes to your specification", "Quality and IP controls; transfer pricing if related; export obligations"],
             ["Own subsidiary", "You sell and employ directly", "Full control; full compliance; see entity options"]])
         + call_box("finding a distributor or partner", ["Which partner model suits your product and margins",
                                                         "How to check a shortlisted partner before you sign",
                                                         "Agreement terms that protect you in India",
                                                         "Permanent establishment, withholding tax and GST in outline",
                                                         "Product registrations and labelling the partner will need"],
                    "a product description, target customers, and the names of any partners you are already talking to.")),
        ("/ Checking a partner", "Before the first shipment.",
         ul("<strong>Company records:</strong> registration, directors, charges and filing history from the MCA portal; GST registration status and return filing; import-export code for importers. See <a href=\"how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html\">verify an Indian company</a>.",
            "<strong>Financials:</strong> filed financial statements, working capital, credit references and payment history with other suppliers.",
            "<strong>Litigation and reputation:</strong> court records, regulatory actions, news and customer references.",
            "<strong>Capability:</strong> warehousing, sales team, coverage of the states you care about, after-sales service.",
            "<strong>Deeper checks:</strong> site visits and background reports when the commitment is large; see <a href=\"india-vendor-supplier-verification-foreign-buyer.html\">supplier and vendor verification</a>.")),
        ("/ Agreement, tax and registrations", "Put it in writing.",
         ul("<strong>Territory and exclusivity:</strong> by state or channel, with minimum purchase targets that end exclusivity if missed.",
            "<strong>Pricing:</strong> you can recommend resale prices, but fixing them can raise Competition Act issues.",
            "<strong>Trademark:</strong> register your mark in India in your own name before appointing anyone; see <a href=\"india-trademark-patent-ip-foreign-company.html\">IP for foreign companies</a>.",
            "<strong>Termination:</strong> notice period, buy-back of stock, return of materials; India has no statutory goodwill compensation for distributors.",
            "<strong>Disputes:</strong> arbitration with a neutral seat; payment terms backed by letters of credit or advance payment where credit is uncertain.",
            "<strong>Product registrations:</strong> depending on the product, BIS certification, FSSAI (food), CDSCO (medical devices and drugs), Legal Metrology labelling, and extended producer responsibility for packaging, e-waste or batteries.",
            "<strong>Tax:</strong> payments for goods do not attract Indian withholding; commissions to an Indian agent carry GST; royalties and service fees from India to you carry withholding tax.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment</a> &middot; <a href="{JV}.html">joint ventures</a> &middot; <a href="india-market-research-foreign-company.html">India market research</a>.</p>'
         + sources("Indian Contract Act, 1872; Competition Act, 2002 (vertical agreements); Trade Marks Act, 1999; Income-tax Act, 2025 and India&rsquo;s tax treaties (permanent establishment, royalties); product rules under the BIS Act, Food Safety and Standards Act, Drugs and Cosmetics Act / Medical Devices Rules and Legal Metrology (Packaged Commodities) Rules.")),
    ],
    faqs=[("How do I find a distributor in India?", "Through your home country's trade service and embassy commercial section, Indian export promotion councils and industry associations, trade fairs, and referrals from existing customers. Shortlist two or three and check each before negotiating."),
          ("How do I check an Indian distributor before signing?", "Review MCA company records, GST registration and return filing, filed financial statements, litigation, credit references and capability, and visit if the commitment is significant."),
          ("Does appointing a distributor create a tax presence in India?", "A buy-sell distributor usually does not. An agent who habitually concludes contracts on your behalf can create a permanent establishment, making part of your profit taxable in India."),
          ("Do Indian distributors get compensation when the agreement ends?", "There is no statute giving goodwill compensation in India; the agreement decides notice, stock buy-back and any payment."),
          ("Should I register my trademark in India first?", "Yes. Register it in your own name before appointing a distributor or licensee, so the brand stays yours if the relationship ends."),
          ("Can BQP help find and check partners?", "Yes. " + C_DIST)],
    related=[("how-to-verify-indian-company-is-genuine-mca-gst-iec-check-foreign-buyers-2026.html", "Verify an Indian company"), ("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Looking for the right partner in India?", cta_b=C_DIST,
    keywords="find distributor in India, how to find distributors for my product in India, business partner India foreign company, distributor agreement India, check Indian distributor, India agent permanent establishment, licensing India royalty, contract manufacturing India foreign company",
    desc="Finding a distributor or business partner in India (2026): distributor, agent, licensee or contract manufacturer; where to find partners; how to check them; agreement terms (exclusivity, pricing, trademark, termination, arbitration); permanent establishment and withholding tax; BIS, FSSAI, CDSCO and labelling.",
    howto={"name": "How a foreign company appoints a distributor in India", "description": "From search to signed agreement.", "steps": [
        {"name": "Choose the model", "text": "Distributor, agent, licensee or contract manufacturer, by control and risk."},
        {"name": "Build a shortlist", "text": "Trade services, export councils, associations, fairs and referrals."},
        {"name": "Check the partner", "text": "Company, GST, financial, litigation and capability checks."},
        {"name": "Protect your brand", "text": "Register the trademark in India and confirm product registrations."},
        {"name": "Sign and monitor", "text": "Agreement with territory, targets, termination and arbitration; review performance yearly."}]}))

# ---------------- SELL-SIDE ----------------
C_SELL = contact("your company's sector, size, shareholding and the type of buyer or investor you expect")
PAGES.append(dict(
    slug=SELL,
    title="Sell-Side Due Diligence in India (2026): Preparing an Indian Company for a Foreign Buyer or Investor - Clean-Up, Data Room, Valuation and Tax",
    em="for Indian founders, promoters and family businesses.",
    kicker="/ Indian sellers &middot; Foreign buyers &middot; Vendor due diligence &middot; Updated 2026-11-19",
    lead=("<strong>Sell-side (vendor) due diligence</strong> is a review of your own company, done before a foreign buyer or investor starts theirs. It finds the problems first: unfiled FEMA forms, tax and GST defaults, related-party loans, weak contracts. You can then fix them or disclose them on your terms instead of losing value in negotiation. "
          "Foreign buyers look closely at <strong>FEMA compliance</strong> (every past foreign investment filed on time), <strong>tax and GST</strong>, <strong>company law</strong>, <strong>revenue quality</strong> and <strong>key contracts</strong>. "
          "On the deal itself, a non-resident buyer must pay <strong>at least fair value</strong>. Up to <strong>25% of the price can be held in escrow or deferred for up to 18 months</strong>. Resident sellers pay <strong>12.5% long-term capital gains tax</strong> on unlisted shares held over 24 months. Clean-up usually takes weeks to months, so start before you meet buyers."),
    sections=[
        ("/ What a foreign buyer will check", "And what to fix first.",
         table(["Area", "Common issue", "Fix before the sale"], [
             ["FEMA", "Late or missing FC-GPR, FC-TRS, ODI or annual returns; share issues below fair value", "File and compound through the RBI; obtain missing valuation reports"],
             ["Income tax and TDS", "TDS defaults, pending notices, cash expenses, unexplained credits", "Rectify returns, pay and document, respond to notices"],
             ["GST", "Input credit mismatches, unfiled annual returns, export refunds pending", "Reconcile and regularise"],
             ["Company law", "Loans to directors, missing approvals, unfiled ROC forms", "Regularise and update registers and minutes"],
             ["Revenue and customers", "Customer concentration, related-party sales, undocumented contracts", "Document contracts, explain concentration, separate related-party dealings"],
             ["People and IP", "Key staff without agreements, IP in founders' names, open-source issues", "Sign agreements, assign IP to the company"]])
         + call_box("selling our company or raising from a foreign investor", ["What a foreign buyer is likely to find, and in what order to fix it",
                                                                                 "Valuation for FEMA and income-tax, and how price, escrow and earn-out interact",
                                                                                 "Your capital gains tax and structuring options",
                                                                                 "Data room contents and timeline",
                                                                                 "How we work with your bankers and lawyers"],
                    "the latest audited accounts, cap table and a note on any foreign investment received so far.")),
        ("/ Deal terms that affect the seller", "Know them before the term sheet.",
         ul("<strong>Price:</strong> a non-resident buyer must pay no less than fair value under FEMA; income-tax also deems fair market value for unlisted shares, so a low price can be taxed as if it were higher.",
            "<strong>Escrow and deferred consideration:</strong> up to 25% of the total price for up to 18 months from the agreement; earn-outs beyond that need careful structuring.",
            "<strong>Indemnities and warranties:</strong> sell-side diligence narrows them; disclosed issues are excluded from claims.",
            "<strong>Stamp duty:</strong> 0.015% on transfer of shares.",
            "<strong>Filing:</strong> Form FC-TRS within 60 days of receipt of the consideration; see <a href=\"form-fc-trs-filing-checklist-india-2026.html\">FC-TRS checklist</a>.")),
        ("/ Tax for the seller", "Plan before signing.",
         ul("<strong>Resident individual sellers:</strong> long-term capital gains at 12.5% on unlisted shares held over 24 months; short-term at slab rates.",
            "<strong>Company sellers or slump sale of a business:</strong> different computation; a business transferred as a going concern is exempt from GST.",
            "<strong>Reinvestment exemptions:</strong> gains from shares reinvested in a residential house can qualify for exemption within limits.",
            "<strong>Founders moving abroad after the sale:</strong> residency affects tax on deferred and earn-out payments; plan the timing.")
         + f'<p>Related: <a href="vendor-due-diligence.html">vendor due diligence</a> &middot; <a href="{ACQ}.html">how a foreign buyer acquires an Indian company</a> &middot; <a href="fema-compounding-foreign-subsidiary-india.html">FEMA compounding</a> &middot; <a href="{HUB}.html">working with an Indian CA</a>.</p>'
         + sources("Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (pricing; rule 9(6)); Companies Act, 2013; Income-tax Act, 2025 (capital gains and deemed fair market value); CGST Act notifications (transfer of a going concern); Indian Stamp Act. Commentary checked 19 November 2026: Treelife, Global Law Experts.")),
    ],
    faqs=[("What is sell-side due diligence?", "A review of your own company before a buyer or investor starts theirs, so problems are fixed or disclosed on your terms and the deal is not repriced late."),
          ("What do foreign buyers look for in an Indian company?", "FEMA compliance on past foreign investment, tax and GST, company-law filings, revenue quality and customer contracts, key employees and IP ownership."),
          ("Can part of the sale price be paid later?", "Yes. Up to 25% of the total consideration can be held in escrow or deferred for up to 18 months from the transfer agreement."),
          ("How is the seller taxed when selling shares to a foreign buyer?", "Resident individuals pay 12.5% long-term capital gains tax on unlisted shares held over 24 months (short-term gains at slab rates); a price below fair market value can be taxed as if it were fair market value."),
          ("How long does sell-side preparation take?", "Usually several weeks for the review, and longer if FEMA compounding or tax rectification is needed, so it should start before buyer meetings."),
          ("Can BQP prepare our company for sale?", "Yes. " + C_SELL)],
    related=[("vendor-due-diligence.html", "Vendor due diligence"), (ACQ + ".html", "How foreign buyers acquire Indian companies"),
             ("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding")],
    cta_h="Preparing to sell or raise from abroad?", cta_b=C_SELL,
    keywords="sell side due diligence India, vendor due diligence India foreign buyer, sell my business to overseas buyers, sell Indian company to foreign company, data room India, FC-TRS seller, capital gains on sale of unlisted shares 12.5 percent, escrow 25 percent 18 months",
    desc="Sell-side due diligence in India (2026): what foreign buyers check (FEMA, tax, GST, company law, revenue, people, IP), how to fix it, fair-value pricing, escrow up to 25% for 18 months, stamp duty, FC-TRS and the seller's capital gains tax.",
    howto={"name": "How an Indian company prepares for a foreign buyer", "description": "Sell-side due diligence steps.", "steps": [
        {"name": "Review the company", "text": "FEMA, tax, GST, company law, contracts, people and IP."},
        {"name": "Fix or disclose", "text": "File and compound FEMA gaps, rectify tax issues, document contracts."},
        {"name": "Value", "text": "FEMA fair value and income-tax fair market value reports."},
        {"name": "Build the data room", "text": "Organised documents and a vendor due diligence report."},
        {"name": "Negotiate and complete", "text": "Price, escrow, warranties; FC-TRS within 60 days of receipt."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DF complete:", len(PAGES))
