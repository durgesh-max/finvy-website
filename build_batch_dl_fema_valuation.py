# -*- coding: utf-8 -*-
"""Batch DL (19 Nov 2026): FEMA valuation report for foreign investment in an Indian company. Call-first page.
Demand: autocomplete sweep 19 Nov 2026 (ac16), all 7 markets: "fema valuation report validity", "fema valuation report
90 days", "fema valuation report format", "fema valuation report timeline", "fema fair market value", "fema valuation
guidelines", "rights issue fema valuation report"; no dedicated page.
Facts: NDI Rules rule 21 - issue or transfer to a person resident outside India of unlisted equity instruments at not
less than fair value under an internationally accepted pricing methodology on an arm's length basis, certified by a
chartered accountant, SEBI-registered merchant banker or practising cost accountant; transfer from non-resident to
resident at not more than fair value; listed companies follow SEBI pricing; convertible instruments - price or
conversion formula fixed upfront, conversion price not less than fair value at issue; share swaps valued by a
SEBI-registered merchant banker or an investment banker regulated abroad; rights issue to non-residents at a price
not lower than offered to residents; no fixed validity in the rules, but banks and practice expect the report to be
no more than 90 days old at allotment or transfer (Taxmann, Corporate Professionals; a Bombay Chamber representation
sought 180 days). Income-tax: angel tax (section 56(2)(viib)) abolished from FY 2024-25; Rule 11UA fair market value
still matters for section 50CA / 56(2)(x)-type provisions (carried into the Income-tax Act, 2025); Companies Act
preferential allotments need a registered valuer's report."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
ACQ = "how-to-acquire-a-company-in-india-foreign-buyer-process-fema-cci-tax-2026"
VAL = "fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026"

C_VAL = contact("the transaction (fresh issue, transfer, rights issue, conversion or swap), the instrument, the investor's country and the target date")
PAGES = [dict(
    slug=VAL,
    title="Valuation Report for Share Transfer Under FEMA (2026): Fair Value Rules, Who Can Sign, Methods, Preference Shares, Buyback and Income-Tax Overlap",
    em="for foreign investors, buyers and Indian companies raising from abroad.",
    kicker="/ Foreign investors &middot; FEMA &middot; Valuation &middot; Updated 2026-11-19",
    lead=("When an Indian company issues shares to a foreign investor, or shares move between a resident and a non-resident, FEMA requires a <strong>price at fair value</strong>. "
          "For an unlisted company, the price for a non-resident investor must be <strong>no less than fair value</strong>, and a non-resident selling to a resident must receive <strong>no more than fair value</strong>. Fair value is worked out by an internationally accepted method on an arm's-length basis and certified by a <strong>chartered accountant, a SEBI-registered merchant banker or a practising cost accountant</strong>. Listed companies follow SEBI pricing. "
          "The rules fix no validity period, but banks and standard practice expect the report to be <strong>no more than 90 days old</strong> on the date of allotment or transfer. The same deal may also need an <strong>income-tax fair market value</strong> report (Rule 11UA) and, for a preferential allotment, a <strong>registered valuer's</strong> report under the Companies Act. Plan all three together so the numbers do not conflict."),
    sections=[
        ("/ When a FEMA valuation is needed", "And which direction the price must go.",
         table(["Transaction", "Price rule", "Valuer", "Filing"], [
             ["Fresh issue to a non-resident (unlisted)", "Not less than fair value", "CA, SEBI merchant banker or cost accountant", "FC-GPR within 30 days of allotment"],
             ["Transfer from resident to non-resident", "Not less than fair value", "As above", "FC-TRS within 60 days"],
             ["Transfer from non-resident to resident", "Not more than fair value", "As above", "FC-TRS within 60 days"],
             ["Convertible instruments (CCPS, CCDs, convertible notes)", "Price or conversion formula fixed upfront; conversion price not less than fair value at issue", "As above", "FC-GPR (and CN reporting for convertible notes)"],
             ["Share swap", "Fair value of both sides", "SEBI-registered merchant banker or investment banker regulated abroad", "FC-GPR / FC-TRS"],
             ["Rights issue to non-resident shareholders", "Not lower than the price offered to residents", "Valuation often still obtained for the record", "FC-GPR"],
             ["Listed company", "SEBI pricing (preferential allotment or market price)", "Per SEBI rules", "As applicable"]])
         + call_box("a FEMA valuation", ["Which valuations your transaction needs (FEMA, income-tax, Companies Act)",
                                          "The method that fits the company's stage (DCF, net assets, market comparables)",
                                          "Timing so the report is current at allotment or transfer",
                                          "How the valuation fits the term sheet price, conversion terms and escrow",
                                          "The FC-GPR or FC-TRS filing that follows"],
                    "the term sheet or share purchase agreement, latest financials, projections (if any) and the expected allotment or transfer date.")),
        ("/ Methods, validity and format", "What the report should contain.",
         ul("<strong>Methods:</strong> discounted cash flow is common for operating companies; net asset value for holding or asset-heavy companies; market multiples or recent transaction prices as cross-checks. The report must explain why the method suits the company.",
            "<strong>Validity:</strong> FEMA does not set a period, but authorised dealer banks and practice treat a report older than 90 days at allotment or transfer as stale; a request to standardise at 180 days has been made but is not law. Re-date or refresh if the deal slips.",
            "<strong>Contents:</strong> purpose and transaction, valuation date, information relied on, method and key assumptions, fair value per share, and the valuer's certification and registration details.",
            "<strong>Convertibles:</strong> record the conversion formula or price at issue; the conversion price cannot be below fair value at the time of issue.",
            "<strong>Signatories:</strong> a chartered accountant, a SEBI-registered merchant banker, or a practising cost accountant.")),
        ("/ Income-tax and company-law overlap", "Avoid three different numbers.",
         ul("<strong>Angel tax:</strong> the income-tax charge on share premium above fair value (section 56(2)(viib)) was abolished from FY 2024-25, so issue prices above fair value no longer trigger it.",
            "<strong>Transfers below fair market value:</strong> income-tax still deems fair market value (Rule 11UA) for the seller and can tax the buyer on a shortfall, so FEMA and income-tax values should be consistent.",
            "<strong>Preferential allotment under the Companies Act:</strong> needs a registered valuer's report (IBBI-registered); one engagement can often cover FEMA, income-tax and Companies Act purposes if planned.",
            "<strong>Late or missing valuation:</strong> an allotment without a valid report is a FEMA contravention; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding</a>.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="form-fc-gpr-filing-checklist-india-2026.html">FC-GPR checklist</a> &middot; <a href="form-fc-trs-filing-checklist-india-2026.html">FC-TRS checklist</a> &middot; <a href="best-ca-esop-valuation-409a-rule-11ua-india.html">Rule 11UA and 409A valuations</a> &middot; <a href="{ACQ}.html">acquiring an Indian company</a>.</p>'
         + sources("Foreign Exchange Management (Non-Debt Instruments) Rules, 2019 (rule 21, pricing guidelines); RBI Master Direction on Foreign Investment in India; Companies Act, 2013 (sections 42, 62) and the Companies (Registered Valuers and Valuation) Rules, 2017; Income-tax Act, 2025 and Rule 11UA; Finance (No. 2) Act, 2024 (abolition of angel tax). Commentary checked 19 November 2026: Taxmann, Corporate Professionals, Treelife, Bombay Chamber representation (2023).")),
    ],
    faqs=[("What is a FEMA valuation report?", "A certificate of the fair value of an Indian company's shares, prepared under an internationally accepted method, needed when shares are issued to or transferred between residents and non-residents."),
          ("Who can sign a FEMA valuation report?", "A chartered accountant, a SEBI-registered merchant banker or a practising cost accountant; share swaps need a SEBI-registered merchant banker or an investment banker regulated abroad."),
          ("How long is a FEMA valuation report valid?", "The rules do not fix a period, but banks and practice expect the report to be no more than 90 days old on the date of allotment or transfer."),
          ("Must a foreign investor pay at least fair value?", "Yes, for unlisted shares issued or sold to a non-resident; when a non-resident sells to a resident, the price cannot exceed fair value."),
        ("Do I need a valuation report for a share transfer?", "It depends on who is buying and selling. Between a resident and a non-resident, yes: FEMA requires the price to be at least fair value when a non-resident buys (and not more than fair value when a non-resident sells), backed by a valuation report, and the transfer is reported in Form FC-TRS within 60 days. Between two residents, FEMA does not apply, but income tax does: if unlisted shares change hands below their fair market value worked out under rule 11UA, the buyer can be taxed on the shortfall and the seller's sale price is deemed to be that fair value - so a valuation report is the safest record. WhatsApp +91 78018 87130 with the company's latest audited accounts, the number of shares, the proposed price and who the buyer and seller are, and we tell you which valuation is needed."),
        ("Is a valuation report needed for preference shares or a share buyback?", "Often yes. Preference shares, including compulsorily convertible preference shares issued to foreign investors, need a fair-value report under FEMA and, for income tax, a value under rule 11UA. In a buyback, shares bought back from a non-resident shareholder must follow the FEMA pricing rules, so a valuation supports the price; for residents, the buyback amount has been taxed in the shareholder's hands as dividend since 1 October 2024, and a valuation still helps justify the price paid. The report must be by the person the rule allows - a chartered accountant, SEBI-registered merchant banker or cost accountant under FEMA, and a merchant banker or accountant under rule 11UA depending on the method."),
          ("Is angel tax still a concern for foreign investment?", "No. The angel tax on share premium above fair value was abolished from FY 2024-25, though income-tax fair market value rules still apply to transfers."),
          ("Can BQP prepare the valuation and filings?", "Yes. " + C_VAL)],
    related=[("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist"), ("form-fc-trs-filing-checklist-india-2026.html", "FC-TRS checklist"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Need a FEMA valuation for a deal?", cta_b=C_VAL,
    keywords="FEMA valuation report, FEMA valuation report validity 90 days, FEMA fair market value, FEMA valuation guidelines, FEMA valuation report format, rights issue FEMA valuation, FDI pricing guidelines India, valuation for foreign investment India",
    desc="FEMA valuation report for foreign investment in India (2026): fair value floor for issues and transfers to non-residents and ceiling for exits, who can certify, methods, 90-day practice, convertibles, swaps, rights issues, and overlap with Rule 11UA and registered valuer reports.",
    howto={"name": "How to get a FEMA valuation right", "description": "Steps for issues and transfers involving non-residents.", "steps": [
        {"name": "Identify the transaction", "text": "Fresh issue, transfer, conversion, swap or rights issue, and the price direction."},
        {"name": "Plan all valuations", "text": "FEMA, income-tax (Rule 11UA) and Companies Act registered valuer, aligned."},
        {"name": "Choose the method", "text": "DCF, net assets or market approach suited to the company."},
        {"name": "Time the report", "text": "Keep it within 90 days of allotment or transfer."},
        {"name": "File", "text": "FC-GPR within 30 days of allotment or FC-TRS within 60 days of transfer."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DL complete:", len(PAGES))
