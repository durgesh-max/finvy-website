# -*- coding: utf-8 -*-
"""Batch EI (20 Nov 2026): Moving abroad from India - becoming an NRI checklist: can an NRI keep a savings account
(no - redesignate to NRO), demat and mutual fund status, PPF, EPF, PAN/Aadhaar, tax in the year of leaving. Call-first.
Demand: sweep 20 Nov 2026 (ac23), all 7 markets: "can nri keep savings account", "can nri keep normal savings account
in india", "is it mandatory to convert savings account to nro account", "convert savings account to nro" (SBI, HDFC,
ICICI, Axis, PNB, Union Bank), "moving abroad from india checklist", "things to do before moving abroad from india",
"how to update nri status in demat account", "how to change nri status in mutual funds", "moving to usa / canada /
australia / dubai from india checklist". No site page for people leaving India.
Facts (checked 20 Nov 2026): FEMA (Deposit) Regulations, 2016 and RBI Master Direction on Deposits and Accounts - resident
accounts, including fixed and recurring deposits, must be redesignated as NRO when the holder becomes non-resident;
banks ask for proof of leaving for employment, business or vocation; NRO accounts can be held jointly with residents;
NRO interest taxed with TDS; penalties under FEMA section 13 for continuing contraventions (banks cite up to INR 5,000 a
day); demat and trading accounts must be re-classified to NRI (non-PIS NRO for existing holdings); mutual fund status,
bank mandate and FATCA to be updated with the AMC/RTA, some AMCs restrict US and Canada residents; PPF continues to
maturity, no new account, no extension (site PPF page); EPF can stay or be withdrawn on settling abroad (site EPF page);
PAN and Aadhaar stay valid; an Indian citizen leaving India for employment abroad is resident in that year only if in
India 182 days or more (the 60-day test does not apply); file the Indian return for the year of leaving; Schedule FA
and foreign assets questions return if you later come back as resident."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "moving-abroad-from-india-becoming-nri-checklist-savings-account-to-nro-demat-mutual-funds-tax-2026"

C = contact("the country you are moving to, your move date, your Indian bank accounts, demat and mutual fund holdings, PPF/EPF, any property or loans, and whether you plan to return")
PAGES = [dict(
    slug=SLUG,
    title="Moving Abroad from India (2026): Becoming an NRI Checklist - Can You Keep Your Savings Account? NRO Conversion, Demat, Mutual Funds, PPF, EPF and Tax",
    em="what to change in India when you move to the US, UK, Canada, Australia, Singapore or the Gulf.",
    kicker="/ Becoming an NRI &middot; Bank accounts &middot; Investments &middot; Tax &middot; Updated 2026-11-20",
    lead=("<strong>No, an NRI cannot keep an ordinary resident savings account.</strong> Under the FEMA deposit rules, your savings account, fixed deposits and recurring deposits must be <strong>redesignated as NRO accounts</strong> once you become non-resident, which usually means once you leave India for a job, business or an indefinite stay. "
          "An NRO account can be held <strong>jointly with a resident relative</strong>. NRO interest is taxed in India with TDS. Most people also open an <strong>NRE account</strong>, which is tax-free in India and fully repatriable, for money they earn abroad. "
          "Also tell your broker, fund houses and insurer about the change of status: <strong>demat accounts</strong> must become NRI accounts, and <strong>mutual fund</strong> folios need NRI status, an NRO or NRE bank mandate and FATCA details. An existing <strong>PPF</strong> continues to maturity but cannot be extended. "
          "For tax, an Indian citizen leaving for <strong>employment abroad</strong> stays resident in the year of departure only if in India for <strong>182 days or more</strong>. File the Indian return for that year."),
    sections=[
        ("/ The checklist", "What to change and when.",
         table(["Item", "What to do", "When"], [
             ["Savings account, FDs, RDs", "Ask the bank to redesignate them as NRO; give passport, visa or job offer and overseas address", "Soon after you leave"],
             ["NRE account", "Open for foreign earnings: tax-free interest in India, fully repatriable", "Before or after leaving"],
             ["Demat and trading account", "Convert to an NRI demat account (non-PIS NRO for existing shares); a new PIS route for repatriable investments", "Before your next trade"],
             ["Mutual funds", "Update status to NRI, bank mandate to NRO or NRE, overseas address and FATCA with the fund house or RTA; check restrictions for US and Canada residents", "Soon after you leave"],
             ["PPF", "Continues to 15-year maturity, deposits from NRO allowed, no extension", "Ongoing"],
             ["EPF", "Keep it or withdraw on settling or working abroad; interest after you stop contributing can be taxable", "When you decide"],
             ["Insurance, loans, credit cards", "Tell the insurer and lender; pay EMIs from NRO or NRE", "Before leaving"],
             ["Property and rent", "A tenant paying an NRI must deduct TDS on rent", "From the first rent after you leave"],
             ["PAN and Aadhaar", "Both stay valid; update address, email and mobile", "Before leaving"],
             ["Income-tax return", "File for the year you leave; check residential status and claim refunds", "By the due date"]])
         + call_box("Becoming an NRI: getting India right", ["Your residential status in the year you leave and the next",
                                                             "Bank accounts: NRO redesignation, NRE and what can be repatriated",
                                                             "Demat, mutual funds, PPF and EPF after the move",
                                                             "Rent, property and loans you keep in India",
                                                             "Tax in your new country (US, UK, Canada, Australia, Singapore, UAE) and treaty relief"],
                    "your move date, destination country, list of Indian accounts and investments, and last ITR.")),
        ("/ Tax in the year you leave", "Residential status and filing.",
         ul("<strong>Leaving for employment:</strong> an Indian citizen who leaves for a job abroad is resident that year only if in India for 182 days or more; the 60-day test does not apply. See the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.",
            "<strong>Gulf moves:</strong> if your Indian income exceeds INR 15 lakh and you are not taxed anywhere, the deemed-resident rule can apply; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">UAE NRIs and the INR 15 lakh rule</a>.",
            "<strong>Your new country:</strong> most countries tax you on worldwide income once resident; a split year or part-year status may apply. Indian income can be taxed in both countries, with treaty credit.",
            "<strong>Filing:</strong> file the Indian return for the year of leaving and for any later year with Indian income above the exemption limit or with TDS to recover; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR an NRI files</a>.",
            "<strong>Coming back later:</strong> plan for RNOR years and foreign asset reporting; see <a href=\"nri-returning-india-tax-rnor-transition.html\">returning NRI and RNOR</a>.")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR accounts</a> &middot; <a href="nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html">PPF for NRIs</a> &middot; <a href="nri-epf-pf-withdrawal-process-online-tax-form-19-15g-2026.html">EPF withdrawal for NRIs</a> &middot; <a href="nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html">NRI demat and digital KYC</a> &middot; <a href="nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html">NRI rent and tenant TDS</a>.</p>'
         + sources("Foreign Exchange Management (Deposit) Regulations, 2016 (FEMA 5(R)/2016-RB, as amended) and RBI Master Direction on Deposits and Accounts (redesignation of resident accounts as NRO; joint holding with residents); FEMA section 13 (penalties); bank guidance (ICICI Bank on converting savings accounts to NRO); Income-tax law on residential status (182-day rule for citizens leaving for employment; deemed residence). Checked 20 November 2026. Your bank's documents list may differ.")),
    ],
    faqs=[("Can an NRI keep a normal savings account in India?", "No. Under the FEMA deposit rules, resident savings accounts, fixed deposits and recurring deposits must be redesignated as NRO accounts when the holder becomes non-resident."),
          ("Is it mandatory to convert a savings account to NRO?", "Yes. Continuing to operate a resident account after becoming non-resident is a FEMA contravention and penalties can apply. Banks redesignate it on request with proof of your move."),
          ("Can an NRO account be joint with a resident?", "Yes. An NRO account can be held jointly with a resident."),
          ("Do I need to update my demat and mutual funds when I move abroad?", "Yes. Demat and trading accounts must be converted to NRI accounts, and mutual fund folios need NRI status, an NRO or NRE bank mandate, an overseas address and FATCA details. Some fund houses restrict US and Canada residents."),
          ("Am I an NRI in the year I leave India for a job?", "An Indian citizen leaving for employment abroad is resident in that year only if in India for 182 days or more; the 60-day test does not apply."),
          ("Can BQP help me before I move abroad?", "Yes. " + C)],
    related=[("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR accounts"), ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"),
             ("nri-ppf-account-rules-continue-maturity-premature-closure-extension-repatriation-2026.html", "PPF for NRIs")],
    cta_h="Moving abroad from India?", cta_b=C,
    keywords="can NRI keep savings account in India, is it mandatory to convert savings account to NRO, convert savings account to NRO, moving abroad from India checklist, things to do before moving abroad from India, update NRI status demat, change NRI status mutual funds, becoming NRI checklist",
    desc="Moving abroad from India (2026): an NRI cannot keep a resident savings account - FEMA requires redesignation to NRO (joint with a resident allowed); open NRE; convert demat, update mutual funds and FATCA; PPF continues; 182-day rule for the year you leave; file the ITR.",
    howto={"name": "How to change your Indian finances when you move abroad", "description": "Becoming an NRI, step by step.", "steps": [
        {"name": "Redesignate bank accounts", "text": "Savings, FDs and RDs to NRO, with proof of the move."},
        {"name": "Open an NRE account", "text": "For foreign earnings, tax-free in India and repatriable."},
        {"name": "Update investments", "text": "Convert demat to NRI; update mutual fund status, bank mandate and FATCA."},
        {"name": "Review PPF, EPF, loans and insurance", "text": "Keep, continue or withdraw as the rules allow; tell lenders and insurers."},
        {"name": "Check residential status and file", "text": "182-day rule for the year you leave; file the Indian return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EI complete")
