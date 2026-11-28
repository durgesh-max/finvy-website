# -*- coding: utf-8 -*-
"""Batch LI (28 Nov 2026): Tax for e-commerce sellers (Amazon, Flipkart, Meesho and similar marketplaces) - TDS under section 194O
at 0.1%, GST TCS under section 52 at 0.5%, GSTR-8, claiming the credits, and registration.
Demand: 'tds 194o', 'tcs on e-commerce sellers gst', 'amazon seller tds tcs', 'how to claim tcs credit gst', 'e-commerce seller
gst registration' - 0 dedicated pages (194O mentioned on industry pages only). E-commerce sellers routinely need reconciliation and
filing help. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (verified by web search 28 Nov 2026): section 194O of the Income-tax Act - the e-commerce operator deducts TDS on the gross
amount of sales of goods or services facilitated through its platform; rate reduced from 1% to 0.1% from 1 October 2024 (Finance
(No. 2) Act, 2024; incometaxindia.gov.in); no deduction for an individual or HUF participant whose gross sales through the operator
do not exceed INR 5 lakh in the year and who has furnished PAN or Aadhaar. Section 52 of the CGST Act - the operator collects TCS on
the net value of taxable supplies made through it by other suppliers; rate reduced from 1% to 0.5% (0.25% CGST + 0.25% SGST, or
0.5% IGST) from 10 July 2024 (Notification 15/2024-Central Tax and 01/2024-Integrated Tax); the operator files GSTR-8 monthly;
the seller accepts the TCS credit, which goes to the electronic cash ledger. TDS under 194O appears in Form 26AS / AIS and is
claimed in the ITR. Sellers of goods through operators generally need GST registration irrespective of turnover, with a
conditional exemption since 1 October 2023 for small intra-state suppliers. No fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "ecommerce-seller-tax-tds-194o-0-1-percent-gst-tcs-section-52-0-5-percent-gstr-8-claim-credit-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the marketplaces you sell on, your GSTIN, monthly "
     "settlement reports, your Form 26AS / AIS, and any mismatch between marketplace reports, GSTR-1 and the TCS credit shown. "
     "Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Tax for E-Commerce Sellers (2026): TDS Under Section 194O at 0.1%, GST TCS Under Section 52 at 0.5%, GSTR-8, Claiming Credits and GST Registration",
    em="reconcile every settlement, claim every credit.",
    kicker="/ Amazon, Flipkart, Meesho and other marketplace sellers &middot; TDS 194O and GST TCS &middot; Updated 2026-11-28",
    lead=("<strong>When you sell through an e-commerce marketplace, the operator deducts two things from your payouts: income tax TDS under section 194O at 0.1% of gross sales (since 1 October 2024), and GST TCS under section 52 at 0.5% of net taxable supplies (since 10 July 2024). "
          "Both are your money - the TDS is claimed in your income tax return and the TCS is credited to your GST cash ledger - but only if your records reconcile.</strong>"),
    sections=[
        ("/ The two deductions", "Income tax and GST.",
         table(["Point", "TDS under section 194O (income tax)", "TCS under section 52 (GST)"], [
             ["Rate", "0.1% (from 1 October 2024; earlier 1%)", "0.5% - 0.25% CGST + 0.25% SGST, or 0.5% IGST (from 10 July 2024; earlier 1%)"],
             ["Base", "Gross amount of sales through the platform", "Net value of taxable supplies (after returns)"],
             ["Exemption", "Individual / HUF with gross sales up to INR 5 lakh in the year who gave PAN or Aadhaar", "None for taxable supplies through the operator"],
             ["Operator files", "TDS return; credit shows in your Form 26AS / AIS", "GSTR-8 each month"],
             ["How you get it back", "Claim in your income tax return against your tax", "Accept the TCS credit; it goes to your electronic cash ledger"]])
         + ul("<strong>GST registration:</strong> sellers of goods through e-commerce operators generally need GST registration whatever their turnover; since 1 October 2023 small intra-state sellers can sell without registration if they meet the conditions.",
              "<strong>Services:</strong> service providers selling through operators below the threshold have a separate registration exemption.")),
        ("/ Reconciliation and common problems", "Where money gets stuck.",
         ul("<strong>Monthly match:</strong> marketplace settlement report vs your GSTR-1 vs the supplies the operator reports in GSTR-8 - differences create TCS mismatches and notices.",
            "<strong>Returns and cancellations:</strong> net them correctly in the same period; GSTR-8 uses net values.",
            "<strong>Unclaimed TCS:</strong> accept the credit and use it from the cash ledger, or claim a refund of excess cash balance.",
            "<strong>194O TDS in Form 26AS:</strong> match it with your books; claim it in the ITR for the right year; book income on the gross sales, not the net payout.",
            "<strong>Multiple marketplaces:</strong> keep a platform-wise ledger for sales, commissions, TDS and TCS.")
         + call_box("e-commerce seller tax", ["GST registration and marketplace onboarding",
                                              "Monthly settlement, GSTR-1 and GSTR-8 reconciliation",
                                              "TCS credit acceptance and refunds",
                                              "194O TDS matching and ITR",
                                              "Notices on TCS or turnover mismatch"],
                    "Marketplaces, GSTIN, settlement reports, Form 26AS / AIS, mismatches.")
         + sources("Income-tax Act, 1961 (section 194O, as amended by the Finance (No. 2) Act, 2024) and the corresponding provisions of the Income-tax Act, 2025; CGST Act, 2017 (sections 24 and 52); Notification 15/2024-Central Tax and 01/2024-Integrated Tax (10 July 2024); site GST registration, GST return filing and e-invoicing pages.")),
    ],
    faqs=[("What is TDS under section 194O for e-commerce sellers?", "Income tax deducted by the e-commerce operator on the gross amount of sales made through its platform. The rate is 0.1% from 1 October 2024 (earlier 1%). It shows in your Form 26AS and AIS and is claimed in your income tax return."),
          ("What is the GST TCS rate for e-commerce sellers?", "0.5% of the net value of taxable supplies from 10 July 2024 - 0.25% CGST plus 0.25% SGST for intra-state supplies, or 0.5% IGST for inter-state supplies. It was 1% earlier."),
          ("How do I claim GST TCS credit?", "The operator reports your supplies and the TCS in GSTR-8. You accept the TCS credit, and it is added to your electronic cash ledger, where it can be used to pay GST or claimed as a refund of excess balance."),
          ("Is 194O TDS deducted for small sellers?", "No deduction is required for an individual or HUF seller whose gross sales through the operator do not exceed INR 5 lakh in the year and who has furnished PAN or Aadhaar."),
          ("Do I need GST registration to sell on Amazon or Flipkart?", "Sellers of goods through e-commerce operators generally need GST registration regardless of turnover. Since 1 October 2023, small intra-state sellers can sell without registration if they meet the conditions."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your marketplaces, GSTIN, settlement reports, Form 26AS / AIS and any mismatches. Or book a call directly.")],
    related=[("best-ca-d2c-ecommerce-india-2026.html", "CA for D2C and e-commerce brands"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and due dates"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?"),
             ("gst-e-invoicing-applicability-5-crore-30-day-reporting-limit-irn-exemptions-cancellation-2026.html", "GST e-invoicing")],
    cta_h="Selling on marketplaces and not sure your TDS and TCS add up?", cta_b=C,
    keywords="tds 194o, 194o rate 0.1 percent, tcs on e-commerce sellers gst, gst tcs 0.5 percent, amazon seller tds tcs, how to claim tcs credit gst, gstr-8, e-commerce seller gst registration",
    desc="Tax for e-commerce sellers: TDS under section 194O at 0.1% of gross sales from 1 October 2024 (INR 5 lakh small-seller exemption), GST TCS under section 52 at 0.5% of net taxable supplies from 10 July 2024, GSTR-8, claiming credits, reconciliation and GST registration.",
    howto={"name": "How e-commerce sellers recover TDS and TCS", "description": "Monthly and yearly.", "steps": [
        {"name": "Reconcile monthly", "text": "Settlement report vs GSTR-1 vs GSTR-8 supplies."},
        {"name": "Accept TCS credit", "text": "Move it to the cash ledger; use it or claim refund."},
        {"name": "Match 194O TDS", "text": "Form 26AS / AIS vs books; book income on gross sales."},
        {"name": "Claim in the ITR", "text": "Claim 194O TDS against your tax for the year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LI complete")
