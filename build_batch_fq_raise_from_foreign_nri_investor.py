# -*- coding: utf-8 -*-
"""Batch FQ (23 Nov 2026): Raising money for an Indian startup from a foreign or NRI investor - issuing shares to
non-residents step by step: FDI route, investor checks, valuation floor, receiving money, allotment within 60 days,
FC-GPR within 30 days, private placement filings, convertibles, NRI non-repatriable route. Call-first hub for founders.
Demand: sweep 23 Nov 2026 (ac45, founders): "issue of shares to foreign investors", "issue shares to nri", "share allotment
fema", "valuation report for share issue", "valuation report for rights issue under fema".
Facts, each already sourced on a site page checked this month:
- Fair value floor for issue to non-residents, report by a CA, SEBI-registered merchant banker or practising cost
  accountant, usually not older than 90 days; angel tax (section 56(2)(viib)) abolished from FY 2024-25; rights issue to
  non-residents follows its own pricing rule (FEMA valuation page).
- Shares within 60 days of receiving the money, else refund within 15 days; FC-GPR within 30 days of allotment;
  late fee INR 7,500 + 0.025% a year (FC-GPR checklist and LSF calculator pages; Companies Act, section 42(6)).
- Press Note 2 (2026): investors with land-border beneficial ownership within 10% and non-controlling can use the
  automatic route; direct investment from China and Hong Kong needs approval (Press Note 2 page).
- NRI/OCI investment on a non-repatriation basis (Schedule IV) is treated as domestic investment (downstream
  investment page).
- CCPS and CCDs count as equity under FEMA when compulsorily convertible, with the conversion price or formula fixed
  upfront (convertible instruments page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026"

C = contact("the investor's country and type (fund, company, individual, NRI or OCI), the amount, the instrument (equity, CCPS, convertible note), your sector, and the target closing date")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Raising Money From a Foreign or NRI Investor (2026): How an Indian Startup Issues Shares to a Non-Resident - FDI Route, Valuation, 60-Day Allotment and FC-GPR",
    em="the order matters; most problems come from doing it out of order.",
    kicker="/ Startups &middot; Fundraising &middot; FEMA &middot; Updated 2026-11-23",
    lead=("<strong>An Indian startup can take money from a foreign investor or an NRI by issuing shares, compulsorily convertible preference shares or convertible notes, in most sectors without government approval.</strong> "
          "The order is fixed: check the sector and the investor&rsquo;s country, get a <strong>valuation</strong> (the price cannot be below fair value), receive the money into the company&rsquo;s bank account, <strong>allot within 60 days</strong> of receiving it, and report to the RBI in <strong>Form FC-GPR within 30 days</strong> of allotment. "
          "Investors linked to China or another country sharing India&rsquo;s land border need approval unless their land-border ownership is within 10% and non-controlling. "
          "An <strong>NRI or OCI investing on a non-repatriation basis</strong> is treated like a domestic investor, with far less paperwork. "
          "The <strong>angel tax on premium above fair value has been abolished</strong>, so a high price is no longer an income-tax problem."),
    sections=[
        ("/ Step by step", "Fresh issue to a non-resident.",
         table(["Step", "What to do", "Timing"], [
             ["1. Sector and route", "Check the sector cap and whether the automatic route applies", "Before the term sheet"],
             ["2. Investor check", "Country, beneficial ownership (land-border test), KYC through the bank", "Before money moves"],
             ["3. Valuation", "Fair value report by a CA, SEBI-registered merchant banker or cost accountant; issue price at or above it", "Usually not older than 90 days at allotment"],
             ["4. Corporate approvals", "Board and shareholder approvals; private placement offer letter where applicable", "Before receiving money"],
             ["5. Receive the money", "Through banking channels into the company&rsquo;s account; bank issues the remittance certificate and KYC", "Starts the 60-day clock"],
             ["6. Allot the shares", "Within 60 days of receiving the money, or refund within 15 days after that", "Within 60 days"],
             ["7. Report", "Form FC-GPR on the RBI portal through the bank; return of allotment to the Registrar of Companies", "Within 30 days of allotment"]])
         + call_box("Closing a round with a foreign or NRI investor", ["Sector, route and the land-border ownership test",
                                                                      "Valuation report and the right instrument",
                                                                      "Board and shareholder approvals and private placement papers",
                                                                      "Allotment and Form FC-GPR on time",
                                                                      "Investor-side tax: treaty, withholding on exit, and their home-country reporting"],
                    "the investor&rsquo;s country and type, the amount, the instrument, your sector and the closing date.")),
        ("/ Which investor, which rules", "Not every non-resident is treated the same.",
         table(["Investor", "Route", "Notes"], [
             ["Foreign fund, company or individual", "FDI, repatriable; automatic route in most sectors", "Valuation floor, 60-day allotment, FC-GPR"],
             ["NRI or OCI, repatriable", "Same as FDI", "Same paperwork as a foreign investor"],
             ["NRI or OCI, non-repatriable", "Treated as domestic investment", "No FDI pricing floor or FC-GPR; the money cannot later be sent abroad freely beyond NRO limits"],
             ["Investor with land-border beneficial ownership", "Approval needed, unless that ownership is within 10% and non-controlling (Press Note 2 of 2026)", "Direct investment from China or Hong Kong always needs approval; see " + L("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026)")],
             ["Existing non-resident shareholder in a rights issue", "FEMA pricing rule for rights issues", "See " + L("fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html", "valuation reports")]])),
        ("/ Instruments and traps", "What founders get wrong.",
         ul("<strong>Instruments:</strong> equity shares and compulsorily convertible preference shares or debentures count as foreign direct investment when the conversion price or formula is fixed upfront. Optionally convertible instruments are debt and fall under borrowing rules. See " + L("convertible-instruments-india-ccd-ccps.html", "CCPS and CCDs") + " and " + L("safe-vs-convertible-note-india-founder.html", "SAFE vs convertible note") + ".",
            "<strong>Money before paperwork:</strong> money that arrives before approvals are in place, or sits more than 60 days without allotment, creates a FEMA breach that needs regularising.",
            "<strong>Late FC-GPR:</strong> costs a late submission fee and can hold up the next round&rsquo;s due diligence; see the " + L("fema-late-submission-fee-calculator-fc-gpr-fc-trs-form-di-fla-apr-lsf-rbi-2026.html", "late fee calculator") + ".",
            "<strong>Downstream investment:</strong> once foreign-owned and controlled, the startup&rsquo;s own investments in other Indian companies follow FDI rules; see " + L("downstream-investment-india-foreign-owned-company-fema-form-di-funding-rules-2026.html", "downstream investment") + ".",
            "<strong>US parent instead?</strong> Some founders raise through a US holding company; that changes tax and FEMA for everyone. See " + L("triangular-structure-indian-founders-us-parent-indian-subsidiary-odi-schedule-iii-2026.html", "US parent with an Indian subsidiary") + ".")
         + '<p>Related: ' + L("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist") + ' &middot; ' + L("how-to-raise-seed-funding-india-startup.html", "raising seed funding") + ' &middot; ' + L("fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules.html", "FDI rules 2026") + ' &middot; ' + L("fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html", "FEMA health check") + ' &middot; ' + L("doing-business-in-india-2026-guide-for-foreign-companies-entity-tax-fdi-compliance-repatriation.html", "doing business in India") + '.</p>'
         + sources("Foreign Exchange Management (Non-debt Instruments) Rules, 2019 (pricing, Schedule I and Schedule IV) and Mode of Payment and Reporting Regulations; RBI reporting directions (Form FC-GPR); Press Note 2 (2026); Companies Act, 2013, section 42 (private placement, allotment within 60 days, refund within 15 days); Finance (No. 2) Act, 2024 (angel tax abolished). Each point is sourced in detail on the linked page. Checked 23 November 2026.")),
    ],
    faqs=[("Can an Indian startup take investment from a foreign investor?", "Yes. In most sectors a foreign investor can subscribe to equity shares or compulsorily convertible instruments under the automatic route, without government approval, subject to the sector cap and the pricing and reporting rules."),
          ("What is the minimum price for issuing shares to a foreign investor?", "The issue price cannot be below the fair value set by a chartered accountant, SEBI-registered merchant banker or practising cost accountant using an internationally accepted method. The report is usually expected to be no older than 90 days."),
          ("How long does a company have to allot shares after receiving foreign investment?", "60 days from receiving the money. If shares are not allotted by then, the money must be refunded within 15 days."),
          ("When is Form FC-GPR due?", "Within 30 days of allotting the shares, filed on the RBI's portal through the company's bank."),
          ("Does an NRI investment need FC-GPR?", "Only if it is on a repatriation basis. An NRI or OCI investing on a non-repatriation basis is treated as a domestic investor."),
          ("Can a startup take money from an investor linked to China?", "Direct investment from China or Hong Kong needs government approval. Under Press Note 2 of 2026, an investor incorporated elsewhere whose land-border beneficial ownership is within 10% and non-controlling can use the automatic route."),
          ("Is angel tax still a problem when raising from foreign investors?", "No. The income-tax charge on share premium above fair value was abolished from FY 2024-25. The FEMA pricing floor still applies."),
          ("Can BQP handle a foreign or NRI funding round?", "Yes. " + C)],
    related=[("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist"),
             ("fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html", "FEMA valuation reports"),
             ("convertible-instruments-india-ccd-ccps.html", "CCPS and CCDs")],
    cta_h="Raising from an investor outside India?", cta_b=C,
    keywords="issue of shares to foreign investors India, issue shares to NRI, raise funding from foreign investor India startup, FDI startup India process, FEMA pricing guidelines share issue, valuation report share issue non-resident, allotment within 60 days FEMA, FC-GPR 30 days, NRI non-repatriation investment",
    desc="Raising money from a foreign or NRI investor (2026): automatic route in most sectors; valuation floor by a CA or merchant banker; receive money, allot within 60 days (else refund in 15), FC-GPR within 30 days. Press Note 2 land-border test, NRI non-repatriable route, CCPS, angel tax abolished.",
    howto={"name": "How an Indian startup issues shares to a foreign or NRI investor", "description": "Fresh issue to a non-resident.", "steps": [
        {"name": "Check sector and investor", "text": "Sector cap, automatic route, land-border beneficial ownership."},
        {"name": "Get a valuation", "text": "Fair value report; issue at or above it."},
        {"name": "Approve and receive money", "text": "Board and shareholder approvals, then funds through banking channels."},
        {"name": "Allot within 60 days", "text": "Or refund within 15 days after that."},
        {"name": "File FC-GPR", "text": "Within 30 days of allotment, plus the return of allotment."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FQ complete")
