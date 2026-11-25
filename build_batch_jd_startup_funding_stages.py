# -*- coding: utf-8 -*-
"""Batch JD (25 Nov 2026): Startup funding stages in India 2026 - hub. Stages: bootstrapping / friends and family,
pre-seed, seed, Series A, Series B and later, pre-IPO; who invests at each (angels and angel networks, incubators,
seed funds, VCs, growth funds, AIFs backed by Fund of Funds 2.0); instruments (equity, CCPS, CCDs, iSAFE / SAFE-style
notes); government schemes (Startup India Seed Fund Scheme - 2026 call closed May 2026 per guides, Fund of Funds 2.0
Rs 10,000 crore via AIFs, Credit Guarantee Scheme for Startups, state schemes, section 80-IAC); legal steps per round
(valuation report under rule 11UA and FEMA pricing for non-residents, private placement under section 42 with PAS-4
offer letter and separate bank account, return of allotment PAS-3, FC-GPR within 30 days of allotment for foreign
investment, allotment within 60 days of receiving foreign money); angel tax under section 56(2)(viib) abolished by
the Finance (No. 2) Act, 2024 from FY 2024-25. No round-size or valuation figures (not stated - vary widely).
Demand: sweep ac116 (25 Nov 2026), 6-7 markets: "startup funding", "startup funding stages", "startup funding rounds",
"startup funding india", "startup funding schemes", "startup funding platform".
Facts (checked 25 Nov 2026): site seed funding, SISFS, FC-GPR, valuation, convertible instruments and DPIIT pages;
Companies Act, 2013 section 42; FEMA (Non-Debt Instruments) Rules, 2019."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "startup-funding-stages-india-2026-pre-seed-seed-series-a-b-government-schemes-instruments-compliance"

C = contact("your stage, revenue or traction, how much you plan to raise and from whom (Indian or foreign investors), and the instrument being discussed")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Startup Funding Stages in India (2026): Pre-Seed, Seed, Series A and Beyond, Government Funding Schemes, Instruments and the Compliance Each Round Needs",
    em="each round brings new paperwork, not just new money.",
    kicker="/ Founders &middot; Startup funding &middot; Updated 2026-11-25",
    lead=("<strong>Indian startups usually raise money in stages: friends and family or pre-seed, a seed round from angels and seed funds, then Series A and later rounds from venture capital and growth funds.</strong> "
          "Alongside private money, founders can use government routes such as the Startup India Seed Fund (through incubators), funds backed by the &#8377;10,000 crore Fund of Funds 2.0, credit guarantees and state schemes. "
          "Every round also needs company-law and, for foreign investors, FEMA filings, which is where most founders need a CA."),
    sections=[
        ("/ Funding stages at a glance", "Who invests and what they look for.",
         table(["Stage", "Typical investors", "What investors look for", "Common instruments"], [
             ["Pre-seed / friends and family", "Founders, family, early angels", "Team and problem", "Equity, convertible notes"],
             ["Seed", "Angels, angel networks, seed funds, incubators", "Product, early users or revenue", "Equity, CCPS, CCDs, SAFE-style notes"],
             ["Series A", "Venture capital funds", "Repeatable growth and unit economics", "CCPS with investor rights"],
             ["Series B and later", "Growth funds, larger VCs, strategic investors", "Scale and path to profit", "CCPS, secondary sales"],
             ["Pre-IPO", "Late-stage and crossover funds", "Governance and IPO readiness", "Equity, secondaries"]])
         + '<p>Round sizes and valuations vary widely by sector and market, so this page does not quote figures. Detail on each step: ' + L("how-to-raise-seed-funding-india-startup.html", "how to raise seed funding") + ', ' + L("seed-vs-series-a.html", "seed vs Series A") + ', ' + L("angel-vs-vc-funding.html", "angel vs VC") + ' and ' + L("vc-term-sheet-india-key-terms.html", "VC term sheet terms") + '.</p>'),
        ("/ Government funding schemes", "Non-dilutive and fund-of-funds routes.",
         ul("<strong>Startup India Seed Fund Scheme:</strong> grants and debt for early DPIIT startups through selected incubators; the 2026 call closed in May 2026 per published guides; see " + L("startup-india-seed-fund-scheme-sisfs-2026-status-20-lakh-grant-50-lakh-debt-eligibility-alternatives.html", "SISFS 2026 status") + ".",
            "<strong>Fund of Funds 2.0:</strong> a &#8377;10,000 crore corpus notified in April 2026 that invests through SEBI-registered AIFs, so startups raise from those funds.",
            "<strong>Credit Guarantee Scheme for Startups:</strong> collateral-free loans from lenders backed by a government guarantee.",
            "<strong>Tax holiday:</strong> eligible DPIIT startups can apply for section 80-IAC; start with " + L("how-to-register-startup-india-dpiit.html", "DPIIT recognition") + ".",
            "<strong>State schemes:</strong> many states offer seed grants, sustenance allowances and incubation support.")),
        ("/ Compliance at every round", "What has to be filed when money comes in.",
         ul("<strong>Valuation:</strong> a valuation report is needed for share issues, under the income-tax rules and, for foreign investors, FEMA pricing; see " + L("fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html", "FEMA valuation reports") + ".",
            "<strong>Private placement:</strong> shares are offered under section 42 with an offer letter (PAS-4), money into a separate bank account, and the return of allotment (PAS-3) filed with the Registrar within 15 days of allotment; the money cannot be used until PAS-3 is filed.",
            "<strong>Foreign or NRI investors:</strong> allot within 60 days of receiving the money and file FC-GPR within 30 days of allotment; see " + L("raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026.html", "raising money from a foreign investor") + " and the " + L("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist") + ".",
            "<strong>Instruments:</strong> CCPS, CCDs and SAFE-style notes each have different tax and FEMA treatment; see " + L("convertible-instruments-india-ccd-ccps.html", "CCDs and CCPS") + " and " + L("safe-vs-convertible-note-india-founder.html", "SAFE vs convertible note") + ".",
            "<strong>Angel tax:</strong> the section 56(2)(viib) tax on share premium was abolished by the Finance (No. 2) Act, 2024 from FY 2024-25.")
         + call_box("Startup fundraising", ["Valuation and share allotment",
                                             "Private placement filings (PAS-4, PAS-3)",
                                             "FC-GPR and FEMA for foreign investors",
                                             "Term sheet and cap table review",
                                             "DPIIT, 80-IAC and scheme applications"],
                    "your round and investors.")
         + sources("Companies Act, 2013 (section 42) and Companies (Prospectus and Allotment of Securities) Rules; FEMA (Non-Debt Instruments) Rules, 2019 and RBI reporting directions; Income-tax rules on valuation; Finance (No. 2) Act, 2024; Startup India and Fund of Funds 2.0 announcements; site funding, SISFS, FC-GPR, valuation and instrument guides. Checked 25 November 2026.")),
    ],
    faqs=[("What are the stages of startup funding in India?", "Usually pre-seed (founders, friends and family, early angels), seed (angels, angel networks, seed funds), Series A (venture capital), Series B and later (growth funds) and pre-IPO rounds."),
          ("What government funding schemes are available for startups in India?", "The Startup India Seed Fund Scheme through incubators (2026 call closed in May 2026 per guides), funds backed by Fund of Funds 2.0, the Credit Guarantee Scheme for Startups, the section 80-IAC tax holiday and state schemes."),
          ("Which instruments do Indian startups use to raise money?", "Equity shares, compulsorily convertible preference shares (CCPS), compulsorily convertible debentures (CCDs) and SAFE-style convertible notes, each with different tax and FEMA treatment."),
          ("What compliance is needed when a startup raises funding?", "A valuation report, a private placement under section 42 with an offer letter and separate bank account, the return of allotment (PAS-3) within 15 days, and for foreign investors allotment within 60 days and FC-GPR within 30 days of allotment."),
          ("Is angel tax still applicable in India?", "No. The angel tax under section 56(2)(viib) was abolished by the Finance (No. 2) Act, 2024 from FY 2024-25."),
          ("Can BQP help with a funding round?", "Yes. CA Durgesh Chavda handles valuation, private placement and allotment filings, FC-GPR for foreign investors, term sheet and cap table review, and DPIIT and scheme applications. " + C)],
    related=[("how-to-raise-seed-funding-india-startup.html", "How to raise seed funding"),
             ("seed-vs-series-a.html", "Seed vs Series A"),
             ("startup-india-seed-fund-scheme-sisfs-2026-status-20-lakh-grant-50-lakh-debt-eligibility-alternatives.html", "SISFS 2026"),
             ("raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026.html", "Raising from foreign investors"),
             ("vc-term-sheet-india-key-terms.html", "VC term sheet terms")],
    cta_h="Raising your next round?", cta_b=C,
    keywords="startup funding stages, startup funding rounds india, startup funding india, startup funding schemes, pre-seed seed series a, government funding for startups india, startup funding compliance, fc-gpr, private placement pas-4",
    desc="Startup funding stages in India 2026: pre-seed, seed, Series A and later, who invests at each stage, government schemes (SISFS, Fund of Funds 2.0, credit guarantee, 80-IAC), instruments (CCPS, CCDs, SAFEs) and the filings every round needs.",
    howto={"name": "How to prepare a startup funding round in India", "description": "For founders.", "steps": [
        {"name": "Pick the stage and investors", "text": "Angels and seed funds early; VCs from Series A."},
        {"name": "Agree the instrument", "text": "Equity, CCPS, CCDs or a SAFE-style note."},
        {"name": "Get a valuation", "text": "Income-tax and, for non-residents, FEMA pricing."},
        {"name": "Run the private placement", "text": "PAS-4 offer, separate bank account, allotment, PAS-3."},
        {"name": "File FEMA forms", "text": "FC-GPR within 30 days for foreign investment."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JD complete")
