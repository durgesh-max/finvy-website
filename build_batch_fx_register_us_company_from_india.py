# -*- coding: utf-8 -*-
"""Batch FX (24 Nov 2026): how to register an LLC or company in the USA from India - US steps plus the Indian side
(FEMA overseas investment, LRS, TCS, APR, Indian tax, Schedule FA, POEM). Call-first page for Indian founders and freelancers.
Demand: sweep ac50 (24 Nov 2026), all 7 markets: "how to register a business in usa from india", "how to register llc company
in usa from india", "how to register a company in usa online from india". Site had Canada, Australia and UAE versions and
ODI / Form 5472 / BOIR pages, but no US step-by-step page.
Facts (checked 24 Nov 2026):
- FEMA (Overseas Investment) Rules, 2022: a resident individual may make ODI within the LRS limit (USD 250,000 per financial
  year) in an operating foreign entity not engaged in financial services, which must not have a subsidiary or step-down
  subsidiary where the individual has control (RBI OI Rules / Directions, 22 August 2022). Reporting through the AD bank
  (Form ODI); Annual Performance Report due 31 December each year (site APR page).
- TCS: LRS remittances for investment attract 20% above INR 10 lakh a year (bank TCS FAQs; site TCS page).
- US: state filing (articles of organization / certificate of incorporation), registered agent, EIN (Form SS-4; no SSN
  needed), operating agreement. FinCEN interim final rule (March 2025) exempts US-formed companies from beneficial ownership
  reporting (site BOIR page). Foreign-owned single-member LLC: Form 5472 with a pro forma Form 1120 each year; USD 25,000
  penalty for failure (site Form 5472 pages).
- India: a resident is taxed on worldwide income; the US entity goes in Schedule FA; a company effectively managed from
  India can be treated as Indian resident (place of effective management)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "how-to-register-llc-company-in-usa-from-india-odi-ein-form-5472-tax-2026"

C = contact("what the US entity will do, who will own it, whether you live in India, where your customers are, and whether you plan to raise funding")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="How to Register an LLC or Company in the USA From India as a Non-US Citizen (2026): Steps, EIN, FEMA ODI Rules, Form 5472 and Indian Tax",
    em="the US filing takes days; the Indian side is where people slip.",
    kicker="/ Founders &middot; US incorporation from India &middot; Updated 2026-11-24",
    lead=("<strong>You can form a US LLC or corporation from India online, without visiting the US: file with a state such as Delaware or Wyoming through a registered agent, get an EIN, and open a US bank account.</strong> "
          "The part most people miss is Indian law. A resident Indian putting money into a foreign company is making an <strong>overseas direct investment (ODI)</strong> under FEMA: it must be reported through your bank in <strong>Form ODI</strong>, fits within the <strong>USD 250,000 a year</strong> Liberalised Remittance Scheme limit, needs an <strong>Annual Performance Report by 31 December</strong> each year, and is allowed only in an operating business with no controlled subsidiaries below it. "
          "On the US side, a single-member LLC owned by a non-US person files <strong>Form 5472</strong> every year (USD 25,000 penalty if missed). In India you stay taxable on worldwide income and must show the entity in Schedule FA."),
    sections=[
        ("/ Quick answers", "What Indian founders ask first.",
         ul("<strong>Can I register a US company from India?</strong> Yes, entirely online, through a registered agent in the state you choose. You do not need a US visa, address or SSN.",
            "<strong>LLC or C-Corp?</strong> An LLC suits a services or trading business owned by one or a few people. A Delaware C-Corp suits a startup that will raise venture capital or issue stock options. See " + L("delaware-c-corp-vs-llc.html", "C-Corp vs LLC") + ".",
            "<strong>Do I need RBI approval?</strong> No prior approval for a resident individual investing in an operating business within the limits, but the investment must be reported through your bank as ODI, and the Annual Performance Report filed each year.",
            "<strong>Do I pay tax in the US?</strong> It depends on whether the business has US-connected income. A single-member LLC is ignored for US income tax but still files Form 5472; a C-Corp pays US corporate tax.",
            "<strong>Do I pay tax in India?</strong> If you live in India, yes, on your worldwide income, and the US entity must be reported in Schedule FA of your return.")),
        ("/ The steps", "From India to a working US entity.",
         table(["Step", "What it involves"], [
             ["1. Choose entity and state", "LLC or C-Corp; Delaware for investor-backed startups, Wyoming or Delaware for small LLCs"],
             ["2. Registered agent and filing", "The agent files the articles of organization (LLC) or certificate of incorporation (corporation) and gives you a US address for official mail"],
             ["3. Operating agreement or bylaws", "Ownership, management and what happens if a member leaves"],
             ["4. EIN", "Apply to the IRS on Form SS-4; no SSN needed. The EIN is required for the bank, payments platforms and filings"],
             ["5. Indian ODI reporting", "Remit your capital through an authorised dealer bank, which reports it in Form ODI; keep share or membership certificates"],
             ["6. US bank account", "Many US banks and fintech accounts open remotely for non-resident owners with the EIN and formation documents"],
             ["7. Yearly compliance", "State annual report or franchise tax, Form 5472 and pro forma 1120 for a foreign-owned single-member LLC, Indian APR by 31 December, Schedule FA in your Indian return"]])
         + '<p>Beneficial ownership reporting: under FinCEN&rsquo;s final rule effective August 2026, companies formed in the US are exempt; see ' + L("boir-cta-us-llc-indian-owner.html", "BOIR status") + '.</p>'),
        ("/ The Indian side", "FEMA, TCS and tax.",
         ul("<strong>ODI rules for individuals:</strong> the US entity must run a real business (not financial services), and must not have a subsidiary or step-down subsidiary that you control. Invest within the USD 250,000 per financial year LRS limit. See " + L("fema-odi-us-entity-indian-founder.html", "FEMA ODI for a US entity") + ".",
            "<strong>TCS:</strong> the bank collects 20% TCS on LRS remittances for investment above INR 10 lakh in a year; it is credited against your Indian tax.",
            "<strong>Annual Performance Report:</strong> due by 31 December each year for the previous financial year; see " + L("form-odi-apr-annual-performance-report-india-2026.html", "Form ODI APR") + ".",
            "<strong>Indian tax:</strong> as a resident you are taxed on worldwide income, including your share of the US business&rsquo;s profit or the salary or dividends it pays you, with credit for US tax. Show the entity in Schedule FA.",
            "<strong>Place of effective management:</strong> if the US company is in substance run from India, India can treat it as an Indian resident company and tax all its profits. Keep board decisions and records real.",
            "<strong>Freelancers billing foreign clients</strong> often do not need a US entity at all; compare " + L("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "exporting services directly from India") + ".")
         + call_box("forming a US company from India", ["LLC or C-Corp, and which state",
                                                         "FEMA ODI reporting and the APR",
                                                         "Form 5472 and US filings",
                                                         "Indian tax, Schedule FA and POEM risk",
                                                         "Flip and fundraising structure if you will raise money"],
                    "the business, owners, where you live and your plans to raise funding.")
         + sources("Foreign Exchange Management (Overseas Investment) Rules, 2022 and Directions (RBI, 22 August 2022); RBI Liberalised Remittance Scheme (USD 250,000 per financial year); Finance Act, 2025 TCS threshold of INR 10 lakh; IRS Form SS-4 and Form 5472 instructions; FinCEN final rule on beneficial ownership information reporting (effective August 2026); Income-tax Act provisions on residence, place of effective management and Schedule FA reporting. Checked 24 November 2026.")),
    ],
    faqs=[("How do I register an LLC in the USA from India?", "Choose a state, appoint a registered agent who files the articles of organization online, sign an operating agreement, get an EIN from the IRS on Form SS-4, and open a US bank account. On the Indian side, remit capital through your bank as overseas direct investment in Form ODI and file the Annual Performance Report each year."),
          ("Do I need RBI approval to start a US company from India?", "Not prior approval for a resident individual investing in an operating business within the LRS limit of USD 250,000 a year, but the investment must be reported through an authorised dealer bank in Form ODI, and the entity must not have a subsidiary that you control."),
          ("Can an Indian resident own a US LLC?", "Yes. It is an overseas direct investment under FEMA. The LLC files Form 5472 in the US every year if it is a single-member LLC owned by a non-US person, and you report it in Schedule FA of your Indian return."),
        ("Can a non-US citizen or foreigner open an LLC in the US?", "Yes. US states do not require LLC owners to be US citizens or residents, and you do not need a US visa, address or SSN to form one. You need a registered agent in the state of formation, and you get an EIN from the IRS on Form SS-4. Owning an LLC is not the same as working in the US: working there in person still needs a valid visa. Indian residents must also follow the FEMA ODI rules and report the LLC in their Indian return."),
          ("Do I need an SSN to get an EIN?", "No. A non-resident owner applies on Form SS-4 without an SSN."),
          ("Is a US LLC owned by an Indian taxed in India?", "If you live in India, your income from the LLC is taxable in India as part of your worldwide income, with credit for any US tax. If the LLC is managed from India, it can also be treated as an Indian resident."),
        ("What is the US tax rate for an LLC owned by a non-resident?", "It depends on how the LLC is taxed and where the work happens. A single-member LLC is disregarded by default, so its income belongs to the owner: if the business has no US trade or business (no US office, staff or dependent agents, and the work is done from India), its profits are generally not taxed in the US, although Form 5472 with a pro forma Form 1120 is still due every year. Income effectively connected with a US business is taxed at the graduated individual rates on Form 1040-NR, and US-source passive income such as dividends, interest or royalties faces 30% withholding unless the India-US treaty gives a lower rate. An LLC that elects to be a corporation pays 21% federal corporate tax. State taxes vary. If you live in India, the income is also taxable in India, with credit for US tax."),
          ("Can BQP help register a US company and handle the Indian side?", "Yes. " + C)],
    related=[("fema-odi-us-entity-indian-founder.html", "FEMA ODI for a US entity"),
             ("delaware-c-corp-vs-llc.html", "Delaware C-Corp vs LLC"),
             ("file-form-5472-foreign-owned-us-llc.html", "Filing Form 5472"),
             ("boir-cta-us-llc-indian-owner.html", "BOIR status for US LLCs"),
             ("form-odi-apr-annual-performance-report-india-2026.html", "Form ODI APR")],
    cta_h="Starting a US company from India?", cta_b=C,
    keywords="how to register llc in usa from india, how to register a company in usa from india, register business in usa from india online, US LLC Indian resident ODI, EIN without SSN India, Form 5472 Indian owner, FEMA ODI US LLC, Delaware LLC from India",
    desc="How to register an LLC or company in the USA from India (2026): state filing via registered agent, EIN without SSN, US bank; FEMA ODI reporting within the USD 250,000 LRS limit, APR by 31 December, 20% TCS above INR 10 lakh; Form 5472; Indian tax, Schedule FA and POEM.",
    howto={"name": "How to register a US LLC from India", "description": "US and Indian steps.", "steps": [
        {"name": "Choose entity and state", "text": "LLC or C-Corp; Delaware or Wyoming."},
        {"name": "File through a registered agent", "text": "Articles of organization or certificate of incorporation."},
        {"name": "Get an EIN", "text": "Form SS-4 to the IRS; no SSN needed."},
        {"name": "Report the ODI in India", "text": "Remit capital through an authorised dealer bank, reported in Form ODI."},
        {"name": "Keep up yearly filings", "text": "State report, Form 5472, Indian APR by 31 December, Schedule FA."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FX complete")
