# -*- coding: utf-8 -*-
"""Batch DI (19 Nov 2026): can a foreign national register a company in India (and how long it takes); getting capital
back from an Indian subsidiary (dividend, buyback, capital reduction, share sale, liquidation). Call-first pages.
Demand: autocomplete sweep 19 Nov 2026 (ac15), all 7 markets: "can a foreign national open/register a company in
india", "how long does it take to register a business in india", "how many days to register a company in india",
"capital reduction india", "capital reduction tax implications india", "profit repatriation from india".
Facts: private company needs at least two directors (one resident in India for 182 days in the financial year) and two
shareholders; foreign nationals and foreign companies may own up to 100% in automatic-route sectors; DIN via SPICe+,
Class 3 DSC, apostilled documents; PAN/TAN issued with incorporation; share money received through banking channels,
shares allotted within 60 days of receipt, FC-GPR within 30 days of allotment; INC-20A commencement declaration within
180 days; first auditor within 30 days. Capital back: dividend (20% domestic withholding or treaty rate); buyback under
section 68 of the Companies Act (up to 25% of paid-up capital and free reserves, 10% with board approval, debt-equity
not above 2:1 after buyback, no further buyback within one year) taxed as capital gains for shareholders from 1 April
2026 with an additional levy for promoters (Finance Act, 2026); capital reduction under section 66 needs NCLT
confirmation, and the part of the payout covered by accumulated profits is taxed as dividend, the balance as capital
gains; share sale (FC-TRS, pricing); liquidation or strike-off. Sources checked 19 Nov 2026: Trilegal, Vinod Kothari,
TaxGuru, Business Today on buyback; Companies Act provisions."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
FN = "can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026"
CAP = "get-capital-back-from-indian-subsidiary-dividend-buyback-capital-reduction-tax-2026"

PAGES = []

C_FN = contact("your nationality, whether a foreign company or individuals will own the Indian company, the business activity and who could act as resident director")
PAGES.append(dict(
    slug=FN,
    title="Can a Foreign National Register a Company or Start a Business in India? (2026) Ownership, Resident Director, Documents, Bank Account and How Long It Takes",
    em="for foreign founders and parent companies.",
    kicker="/ Foreign founders &middot; Company registration &middot; Updated 2026-11-19",
    lead=("Yes. A foreign national, or a foreign company, can own up to <strong>100% of an Indian private limited company</strong> in sectors open to automatic-route foreign investment, and can be a director. "
          "The company needs at least <strong>two shareholders and two directors</strong>, and <strong>one director must be resident in India</strong> (in India for at least 182 days in the financial year). Directors need a DIN, which is allotted through the SPICe+ incorporation form, and a Class 3 digital signature. Foreign documents are usually <strong>notarised and apostilled</strong>. "
          "Once the documents are ready, incorporation usually takes <strong>one to three weeks</strong>, depending on name approval and MCA processing. PAN and TAN come with the certificate. Opening the bank account, receiving the share money, allotting shares (within 60 days of receipt) and filing <strong>FC-GPR within 30 days</strong> of allotment take a few more weeks. "
          "Nationals of countries sharing a land border with India need government approval to invest, and security clearance before getting a DIN."),
    sections=[
        ("/ Requirements at a glance", "Private limited company.",
         table(["Item", "Requirement", "Foreign-owner notes"], [
             ["Shareholders", "At least 2", "A foreign parent plus a nominee or second group company; or two individuals"],
             ["Directors", "At least 2, one resident in India (182 days in the financial year)", "Foreign directors can serve; the resident director can be an Indian professional or employee"],
             ["DIN and DSC", "DIN through SPICe+; Class 3 DSC for each signatory", "Passport and recent address proof, apostilled; see the DIN guide"],
             ["Registered office", "An Indian address with proof and owner's no-objection", "Can be a serviced office"],
             ["Capital", "No minimum", "Money must come through banking channels from the investor's account"],
             ["FDI route", "Automatic in most sectors", "Government approval for some sectors and for land-border beneficial owners"]])
         + call_box("registering a company", ["Whether a company, LLP, branch or liaison office fits your plan",
                                               "Shareholding and resident-director options",
                                               "Documents, apostille and digital signatures from your country",
                                               "Realistic timeline to an operating bank account",
                                               "First-year compliance and tax registrations"],
                    "passport copies of proposed directors, the parent company's documents (if any), the business activity and your target start date.")),
        ("/ Timeline", "What typically takes how long.",
         table(["Stage", "Typical time", "Notes"], [
             ["Documents and apostille abroad", "1-2 weeks", "Passport, address proof, parent's board resolution and constitutional documents"],
             ["Digital signatures", "A few days", "Video verification with an Indian certifying authority"],
             ["Name and incorporation (SPICe+)", "1-3 weeks", "Depends on name approval and any resubmission; PAN, TAN and DINs issued with incorporation"],
             ["Bank account", "1-3 weeks", "Banks do KYC on foreign shareholders and directors"],
             ["Share money and allotment", "Within 60 days of receipt", "Valuation report for the issue price"],
             ["FC-GPR", "Within 30 days of allotment", "Through the FIRMS portal via the AD bank"]])
         + ul("<strong>Also in the first months:</strong> appoint the first auditor within 30 days of incorporation, file the commencement-of-business declaration (INC-20A) within 180 days, and register for GST and shops and establishments where needed.")),
        ("/ Common questions from foreign founders", "Before you start.",
         ul("<strong>No resident director?</strong> Options include an Indian employee, a trusted professional, or a nominee director service with proper agreements; see <a href=\"nominee-resident-director-india-foreign-company.html\">resident director options</a>.",
            "<strong>Signing from abroad:</strong> all filings are electronic with digital signatures; see <a href=\"din-for-foreign-national-director-india-documents-apostille-dsc-process-2026.html\">DIN and DSC for foreign directors</a>.",
            "<strong>One-person company?</strong> Only Indian citizens can form an OPC; foreigners use a private limited company.",
            "<strong>Tax:</strong> the company pays 25.168% under section 115BAA; dividends to the foreign owner carry withholding tax at the domestic or treaty rate.",
            "<strong>Alternatives:</strong> an LLP, a branch or liaison office, or an employer of record for a first hire; see <a href=\"rbi-approval-place-of-business-india-liaison-branch-project-office-form-fnc-2026.html\">offices needing RBI approval</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up a wholly owned subsidiary</a> &middot; <a href="form-fc-gpr-filing-checklist-india-2026.html">FC-GPR checklist</a>.</p>'
         + sources("Companies Act, 2013 (sections 3, 149(3), 152) and the Companies (Incorporation) Rules, 2014; Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 and the Mode of Payment and Reporting Regulations (allotment within 60 days; FC-GPR within 30 days); Consolidated FDI Policy and Press Note 3 (2020). Timelines are typical and depend on documents and MCA processing.")),
    ],
    faqs=[("Can a foreign national open a company in India?", "Yes. A foreign national or foreign company can own up to 100% of an Indian private limited company in automatic-route sectors and can be a director, but the company needs one director resident in India."),
          ("How long does it take to register a company in India?", "Usually one to three weeks for incorporation once documents are ready, and a few more weeks for the bank account, share allotment and FC-GPR filing."),
        ("How do I register an Indian subsidiary of a foreign company?", "Check that your sector allows foreign investment under the automatic route; get digital signatures for the directors; reserve the name and file the SPICe+ incorporation form with the memorandum, articles and apostilled parent documents, which also issues PAN and TAN; open the company's bank account; receive the share capital from the parent through banking channels and allot shares within 60 days; report the investment in Form FC-GPR within 30 days of allotment; and file the commencement of business declaration (INC-20A) within 180 days of incorporation."),
        ("Can a foreign company own 100% of an Indian subsidiary?", "Yes, in sectors open to 100% foreign investment under the automatic route. A private limited company needs at least two shareholders, so the parent usually holds all but one share and a group company or nominee holds the other; it also needs two directors, one of them resident in India."),
          ("Does a foreign-owned company need an Indian director?", "It needs at least one director who is resident in India, meaning in India for at least 182 days in the financial year; the director does not have to be an Indian citizen."),
          ("Can a foreigner be a director in an Indian company?", "Yes. A foreign national can be a director of an Indian private or public company after getting a Director Identification Number (DIN), using apostilled or consularised identity and address proof and a digital signature certificate. At least one director on the board must be resident in India (in India for 182 days or more in the previous calendar year), so a board made up only of foreign directors needs a resident director added. Nationals of countries that share a land border with India also need security clearance before they can be appointed."),
          ("What documents does a foreign national need?", "Passport, recent address proof, photograph, and for a corporate shareholder its incorporation documents and board resolution, usually notarised and apostilled."),
          ("Can I use a virtual office address for company registration in India?", "Only if the address comes with documents the Registrar accepts - a rent, lease or service agreement or a no-objection letter from the owner, plus a recent utility bill - and the company can actually receive and acknowledge letters there. The Registrar can order a physical verification of the registered office, and GST officers verify the principal place of business, so a shared or virtual address without a proper agreement risks rejection of the GST application or action against the company. The registered office can be shifted later, but changing it has its own filings."),
          ("Can a foreigner form a one person company in India?", "No. Only Indian citizens, resident or not, can form an OPC; foreigners use a private limited company."),
        ("Can a foreigner open a bank account in India?", "It depends on residence and purpose. A foreign national living in India, for example on an employment visa, can open an ordinary resident savings account with a passport, visa and residence registration. A foreign national of Indian origin or an OCI cardholder living abroad can open NRE and NRO accounts like an NRI. A foreign tourist can open an NRO account for up to six months. A person living abroad with a business interest in India can use a Special Non-Resident Rupee (SNRR) account, and a foreign company doing business in India banks through its Indian subsidiary, branch or liaison office. Book a call to choose the right account before money moves."),
          ("Can BQP register our company?", "Yes. " + C_FN)],
    related=[("foreign-company-setup-indian-subsidiary-wos.html", "Wholly owned subsidiary set-up"), ("nominee-resident-director-india-foreign-company.html", "Resident director options"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Registering a company in India from abroad?", cta_b=C_FN,
    keywords="can a foreign national open a company in India, foreign national register company India, how long to register company in India, how many days to register a company in India, foreigner company India resident director, company registration India for foreigners 2026",
    desc="Can a foreign national register a company in India (2026)? Yes: up to 100% ownership in automatic-route sectors; two directors (one resident 182 days) and two shareholders; DIN via SPICe+ and DSC; apostilled documents; incorporation in about 1-3 weeks; allotment within 60 days and FC-GPR within 30 days.",
    howto={"name": "How a foreign national registers a company in India", "description": "Steps for a private limited company.", "steps": [
        {"name": "Plan ownership and directors", "text": "Two shareholders, two directors, one resident in India."},
        {"name": "Prepare documents", "text": "Passports, address proofs, parent documents; notarise and apostille."},
        {"name": "Get digital signatures", "text": "Class 3 DSC for each signatory."},
        {"name": "Incorporate through SPICe+", "text": "Name, DINs, PAN and TAN issued with incorporation."},
        {"name": "Fund and report", "text": "Open the bank account, receive share money, allot within 60 days, file FC-GPR within 30 days."}]}))

C_CAP = contact("the parent's country, the subsidiary's reserves and cash, the amount you want back and your timeline")
PAGES.append(dict(
    slug=CAP,
    title="Getting Money Back from an Indian Subsidiary (2026): Dividend, Buyback, Capital Reduction, Share Sale or Liquidation - Tax and Process Compared",
    em="for foreign parent companies.",
    kicker="/ Foreign parents &middot; Repatriation &middot; Capital reduction &middot; Updated 2026-11-19",
    lead=("A foreign parent can take money out of its Indian subsidiary in five main ways. A <strong>dividend</strong> comes out of profits, with withholding tax at 20% or the lower treaty rate. A <strong>buyback</strong> is limited to 25% of paid-up capital and free reserves and is taxed as <strong>capital gains from 1 April 2026</strong>, with an extra levy for promoters. A <strong>capital reduction</strong> needs <strong>NCLT approval</strong>, and the part paid out of accumulated profits is taxed as dividend. A <strong>sale of shares</strong> needs an FC-TRS filing. <strong>Liquidation or strike-off</strong> is the final exit. "
          "Royalties, service fees and interest are separate current-account routes for ongoing payments. "
          "The best route depends on the subsidiary's reserves, your treaty, your home-country tax on the receipt, and whether you want to keep the company. Model each option before the board meets."),
    sections=[
        ("/ The options compared", "Tax and process.",
         table(["Route", "Indian tax on the parent", "Process and limits", "Best for"], [
             ["Dividend", "Withholding at 20% plus surcharge and cess, or the treaty rate (often 5% to 15%) with TRC and Form 10F", "Board (interim) or shareholders (final); out of profits", "Regular repatriation of profits"],
             ["Buyback (section 68)", "Capital gains from 1 April 2026; additional levy for promoter shareholders; treaty may help", "Up to 25% of paid-up capital and free reserves (10% with board approval only); debt-equity not above 2:1 after; no new buyback within one year; FC-TRS", "Returning surplus cash while keeping the company"],
             ["Capital reduction (section 66)", "Payout covered by accumulated profits taxed as dividend; balance as capital gains", "Special resolution and NCLT confirmation; creditor notice; several months", "Large one-off return of capital or clean-up of losses"],
             ["Sale of shares", "Capital gains in India (buyer withholds); treaty rarely exempts gains on Indian shares", "FEMA pricing (exit not above fair value to a resident buyer); FC-TRS within 60 days", "Exit to a buyer"],
             ["Liquidation or strike-off", "Distribution taxed as dividend to the extent of accumulated profits, balance as capital gains", "Voluntary liquidation or strike-off (STK-2) after clearing liabilities", "Closing India operations"]])
         + call_box("getting money back from our Indian subsidiary", ["Which route gives the best after-tax result for your parent country",
                                                                       "Reserves, cash and Companies Act limits",
                                                                       "Treaty position and home-country tax on the receipt",
                                                                       "Process, approvals and timeline",
                                                                       "FEMA filings and bank documentation"],
                    "the subsidiary's latest audited accounts, the parent's country and the amount and timing you want.")),
        ("/ Points that change the answer", "Check before you choose.",
         ul("<strong>Treaty rates on dividends</strong> differ by country and shareholding (for example 5% to 15%); some home countries exempt dividends from a substantial holding, which can make a dividend cheaper overall than a buyback.",
            "<strong>Promoter levy on buybacks:</strong> the Finance Act, 2026 added an extra levy for promoter shareholders; model how it applies to a foreign parent and whether the treaty helps.",
            "<strong>Accumulated profits:</strong> in a capital reduction or liquidation, distributions are dividend to the extent of accumulated profits, so the reserve position decides the tax mix.",
            "<strong>Withholding documents:</strong> TRC, Form 10F and a no-PE declaration from the parent; Forms 15CA/15CB for the remittance.",
            "<strong>Ongoing alternatives:</strong> arm's-length royalties, management fees and interest move money regularly but need transfer pricing support; see <a href=\"technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html\">royalty payments</a>.")),
        ("/ After the decision", "Execution.",
         ul("Board and shareholder approvals, solvency checks and statutory forms with the Registrar.",
            "For buyback and share sale: FC-TRS within 60 days of the remittance; for capital reduction: NCLT petition and order.",
            "Withhold and deposit tax, issue certificates and remit through the AD bank.",
            "For closure: see <a href=\"close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html\">closing a company in India</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="repatriate-profits-india-foreign-parent.html">repatriating profits</a> &middot; <a href="ca-for-india-dividend-repatriation-foreign-parent-step-by-step.html">dividend repatriation step by step</a>.</p>'
         + sources("Companies Act, 2013 (sections 66, 68, 123); Income-tax Act, 2025 (dividend and capital gains; buyback provisions as amended by the Finance Act, 2026); Foreign Exchange Management (Non-Debt Instruments) Rules, 2019; India&rsquo;s tax treaties. Commentary checked 19 November 2026: Trilegal (Budget 2026 and M&amp;A), Vinod Kothari Consultants, TaxGuru, Business Today.")),
    ],
    faqs=[("How can a foreign parent get money out of an Indian subsidiary?", "Through dividends, a buyback, a capital reduction, a sale of shares or liquidation, plus ongoing royalties, service fees or interest at arm's length."),
          ("How are dividends from an Indian subsidiary taxed for a foreign parent?", "The subsidiary withholds tax at 20% plus surcharge and cess, or the lower treaty rate (often 5% to 15%) if the parent provides a tax residency certificate and Form 10F."),
          ("How is a buyback taxed from 1 April 2026?", "As capital gains in the shareholder's hands, with an additional levy for promoter shareholders under the Finance Act, 2026; between 1 October 2024 and 31 March 2026 it was taxed as dividend."),
          ("What are the tax implications of capital reduction in India?", "The payout is treated as dividend to the extent of the company's accumulated profits and as capital gains for the balance; the reduction needs NCLT confirmation."),
          ("How much can an Indian company buy back?", "Up to 25% of paid-up capital and free reserves (10% with board approval only), with debt not more than twice equity afterwards and no further buyback within one year."),
          ("Can BQP model and execute the repatriation?", "Yes. " + C_CAP)],
    related=[("repatriate-profits-india-foreign-parent.html", "Repatriating profits"), ("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "Closing a company in India"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Want money back from your Indian subsidiary?", cta_b=C_CAP,
    keywords="capital reduction India, capital reduction tax implications India, buyback tax 2026 foreign parent, profit repatriation from India, get money out of Indian subsidiary, dividend from Indian subsidiary to parent, section 66 NCLT capital reduction",
    desc="Getting money back from an Indian subsidiary (2026): dividend (20% or treaty), buyback (capital gains from 1 April 2026 with promoter levy; 25% limit), capital reduction (NCLT; dividend to the extent of accumulated profits), share sale (FC-TRS) or liquidation, compared.",
    howto={"name": "How a foreign parent takes capital back from an Indian subsidiary", "description": "Choosing and executing the route.", "steps": [
        {"name": "Review reserves and cash", "text": "Accumulated profits, free reserves, debt and solvency."},
        {"name": "Model the options", "text": "Dividend, buyback, capital reduction, share sale or liquidation, with treaty and home-country tax."},
        {"name": "Approve", "text": "Board and shareholder resolutions; NCLT petition for a capital reduction."},
        {"name": "Withhold and remit", "text": "Deduct tax, file 15CA/15CB, remit through the AD bank."},
        {"name": "Report", "text": "FC-TRS where shares move; ROC forms and tax filings."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DI complete:", len(PAGES))
