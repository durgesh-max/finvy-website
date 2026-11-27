# -*- coding: utf-8 -*-
"""Batch JA (25 Nov 2026): GST return filing 2026 - which returns, due dates and process. GSTR-1 by the 11th (monthly);
QRMP taxpayers (turnover up to Rs 5 crore) file GSTR-1 quarterly by the 13th of the month after the quarter (optional
IFF by the 13th for the first two months); GSTR-3B by the 20th (monthly) or the 22nd / 24th by state (QRMP, with
PMT-06 payments by the 25th for the first two months); composition: CMP-08 by the 18th of the month after each quarter
and GSTR-4 annual (30 June after the year since 2024); GSTR-9 annual by 31 December (optional up to Rs 2 crore
turnover), GSTR-9C self-certified above Rs 5 crore; GSTR-7 (TDS) and GSTR-8 (TCS) by the 10th; GSTR-5 for
non-resident taxable persons; GSTR-10 final return on cancellation. Nil returns still due; late fee Rs 50 a day
(Rs 20 for nil returns) subject to caps; interest 18% a year on tax paid late; ITC only for invoices in GSTR-2B.
Demand: sweep ac110 (25 Nov 2026), all 7 markets: "gst return filing", "gst return filing due date / date /
deadline", "gst return filing process step by step", "gst return filing online", "gst return filing fees".
Facts (checked 25 Nov 2026): Cleartax, Tally, IndiaFilings, Gimbooks GST calendars (FY 2026-27); site compliance
calendar, composition scheme, GSTR-9 and ITC pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee"

C = contact("your GSTIN, state, turnover, whether you file monthly or quarterly (QRMP), and any returns you have missed")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="GST Return Filing 2026: Due Dates (GSTR-1, GSTR-3B, QRMP, CMP-08, GSTR-9), What Happens If a GST Return Is Not Filed, Late Fee Per Day, Maximum Cap and the 3-Year Filing Bar",
    em="nil returns are due too, and late fees run every day.",
    kicker="/ GST-registered businesses &middot; GST compliance &middot; Updated 2026-11-25",
    lead=("<strong>Most GST-registered businesses file two returns: GSTR-1 (sales) by the 11th and GSTR-3B (summary and tax payment) by the 20th of the next month, or quarterly under QRMP if turnover is up to &#8377;5 crore.</strong> "
          "Composition dealers file CMP-08 every quarter and GSTR-4 once a year, and most regular taxpayers above &#8377;2 crore turnover also file the annual GSTR-9 by 31 December. "
          "Returns are due even with no business in the period; late filing attracts a daily late fee and 18% interest on tax paid late."),
    sections=[
        ("/ GST returns and due dates", "Who files what, and when.",
         table(["Return", "What it reports", "Due date"], [
             ["GSTR-1 (monthly)", "Outward supplies (sales invoices)", "11th of the next month"],
             ["GSTR-1 (QRMP)", "Quarterly sales; optional IFF for the first two months", "13th of the month after the quarter"],
             ["GSTR-3B (monthly)", "Summary of sales, ITC and tax payment", "20th of the next month"],
             ["GSTR-3B (QRMP)", "Quarterly summary; tax paid monthly via PMT-06 by the 25th", "22nd or 24th after the quarter, by state"],
             ["CMP-08", "Composition tax payment", "18th of the month after each quarter"],
             ["GSTR-4", "Composition annual return", "30 June after the year (confirm on the portal)"],
             ["GSTR-9 / GSTR-9C", "Annual return / reconciliation", "31 December after the year"],
             ["GSTR-7 / GSTR-8", "TDS deductors / e-commerce TCS", "10th of the next month"],
             ["GSTR-10", "Final return after cancellation", "Within three months of cancellation"]])
         + '<p>Composition rules: ' + L("gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026.html", "GST composition scheme") + '. Annual return: ' + L("gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html", "GSTR-9 and 9C for FY 2025-26") + '. All dates: ' + L("india-tax-compliance-calendar-fy-2026-27-complete.html", "compliance calendar FY 2026-27") + '.</p>'),
        ("/ How to file GST returns online", "Step by step on the GST portal.",
         ul("<strong>Log in</strong> at the GST portal with your GSTIN-linked user ID.",
            "<strong>Reconcile purchases:</strong> accept or reject supplier invoices and check GSTR-2B; input tax credit is allowed only for invoices that appear in it; see " + L("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "input tax credit rules") + ".",
            "<strong>File GSTR-1</strong> (or IFF) with invoice-wise B2B sales, B2C summaries, credit notes and HSN details.",
            "<strong>Check GSTR-3B:</strong> it is auto-drafted from GSTR-1 and GSTR-2B; correct any genuine differences before filing.",
            "<strong>Pay tax</strong> through the electronic cash and credit ledgers, then file with DSC or EVC.",
            "<strong>Nil periods:</strong> file nil GSTR-1 and GSTR-3B even when there are no sales.")),
        ("/ Late fees, interest and fixes", "What missing a date costs.",
         ul("<strong>Late fee:</strong> &#8377;50 a day (&#8377;20 a day for nil returns) for GSTR-3B and GSTR-1, subject to caps linked to turnover.",
            "<strong>Interest:</strong> 18% a year on tax paid after the due date.",
            "<strong>Blocked actions:</strong> continued non-filing can block e-way bills and lead to cancellation of registration; see " + L("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST cancellation and revocation") + ".",
            "<strong>Notices:</strong> mismatches between GSTR-1, GSTR-3B and GSTR-2B trigger ASMT-10 and DRC notices; see " + L("gst-notice-response-india-asmt-drc-gstr.html", "GST notice response") + ".",
            "<strong>Do you need GST at all?</strong> See " + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration thresholds") + ".")
         + call_box("GST return filing", ["Monthly or QRMP GSTR-1 and GSTR-3B",
                                           "GSTR-2B and ITC reconciliation",
                                           "GSTR-9 and GSTR-9C annual returns",
                                           "Catch-up filing of missed returns",
                                           "GST notices and DRC replies"],
                    "your GSTIN and filing status.")
         + sources("CGST Act, 2017 and CGST Rules (returns, late fee, interest); GST portal; Cleartax, Tally, IndiaFilings and Gimbooks GST calendars for FY 2026-27; site compliance calendar, composition, GSTR-9 and ITC guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the due date for GST return filing?", "GSTR-1 by the 11th and GSTR-3B by the 20th of the next month for monthly filers; under QRMP, GSTR-1 by the 13th and GSTR-3B by the 22nd or 24th (by state) of the month after the quarter."),
          ("Which GST returns does a regular business file?", "GSTR-1 for sales and GSTR-3B for the summary and tax payment, monthly or quarterly, plus the annual GSTR-9 where turnover exceeds Rs 2 crore (optional below) and GSTR-9C self-certification above Rs 5 crore."),
          ("How do I file a GST return online?", "Log in to the GST portal, reconcile purchases with GSTR-2B, file GSTR-1 (or IFF), review the auto-drafted GSTR-3B, pay tax through the cash and credit ledgers and file with DSC or EVC."),
          ("Is a nil GST return mandatory?", "Yes. A registered person must file GSTR-1 and GSTR-3B even when there are no sales or purchases in the period; nil returns attract a lower late fee if filed late."),
        ("What happens if a GST return is not filed?", "Late fee runs every day the return is late - Rs 50 a day (Rs 20 a day for a nil return) up to the caps per return - and 18% a year interest runs on any tax paid late. Beyond the money, the next period's return cannot be filed until the earlier one is, the GSTIN can be blocked from generating e-way bills, your buyers lose input tax credit because your invoices do not reach their GSTR-2B, and continued non-filing can lead to a show cause notice in REG-17 and cancellation of the registration. Filing the pending returns as early as possible stops the late fee growing and keeps revocation open if the registration has already been cancelled."),
        ("Can I file a GST return without paying the tax?", "Not GSTR-3B: it can be filed only after the tax shown as payable is paid from the cash or credit ledger, so a return with tax due stays unfiled until payment. GSTR-1 (the sales statement) can be filed on its own without payment, and filing it on time keeps your buyers' input tax credit flowing. If cash is short, file GSTR-1, pay what you can and file GSTR-3B as soon as possible - interest runs only on the tax paid late. WhatsApp +91 78018 87130 with your GSTIN and the periods pending, and we work out the tax, interest and late fee and file them."),
          ("What is the late fee for GST returns?", "Rs 50 a day (Rs 20 a day for nil returns) for GSTR-3B and GSTR-1, subject to caps linked to turnover, plus 18% a year interest on tax paid late."),
        ("What is the maximum late fee for GSTR-3B?", "The daily late fee (Rs 50 a day, or Rs 20 a day for a nil return, split equally between CGST and SGST) stops at a cap per return based on the previous year's aggregate turnover: Rs 500 for a nil return, Rs 2,000 for turnover up to Rs 1.5 crore, Rs 5,000 for Rs 1.5 crore to Rs 5 crore, and Rs 10,000 above Rs 5 crore. Interest at 18% a year under section 50 runs separately on any tax paid late, and a return cannot be filed after three years from its due date (section 39(11)), so old pending returns should be cleared quickly."),
        ("Can I still file a GST return that is three years old?", "No. Since the Finance Act, 2023 amendments (in force from 1 October 2023), GSTR-1, GSTR-3B, GSTR-4, GSTR-5, GSTR-6, GSTR-7, GSTR-8 and GSTR-9 cannot be filed after three years from their own due date, and the GST portal now blocks them on a rolling basis. Counting from the due date: GSTR-3B for October 2023 (due 20 November 2023) is already closed; GSTR-1 for November 2023 closes after 11 December 2026 and GSTR-3B for November 2023 after 20 December 2026; the FY 2022-23 annual return (GSTR-9) closes after 31 December 2026. Quarterly (QRMP) filers should check the due date of each quarter. Once a return is barred, the tax and credit for that period can no longer be set right through the return - an officer can assess the period on a best-judgment basis or raise a demand, and continued non-filing can lead to cancellation of registration. So file every pending return that is still open now, pay any shortfall with interest (DRC-03 where it cannot go through the return), and keep the reconciliation ready in case a notice follows. WhatsApp +91 78018 87130 with your GSTIN and a screenshot of the return dashboard showing what is pending, or book a call."),
        ("What should I send to clear pending GST returns?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, the list of returns pending (or a screenshot of the return dashboard), sales and purchase details for those months, and any notice received. We work out the tax, interest and late fee, file the pending GSTR-1 and GSTR-3B in order, and handle any cancellation or mismatch notice that has come up. You keep your own GST login."),
          ("What is the GST return due date for composition dealers?", "CMP-08 by the 18th of the month after each quarter and the annual GSTR-4, now due by 30 June after the year (confirm the current date on the portal)."),
          ("Can BQP file my GST returns?", "Yes. CA Durgesh Chavda files GSTR-1, GSTR-3B and annual returns, reconciles ITC, clears missed returns and handles GST notices. " + C)],
    related=[("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "Input tax credit"),
             ("gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html", "GSTR-9 and 9C FY 2025-26"),
             ("gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026.html", "Composition scheme"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice response"),
             ("india-tax-compliance-calendar-fy-2026-27-complete.html", "Compliance calendar FY 2026-27")],
    cta_h="Behind on GST returns?", cta_b=C,
    keywords="gst return filing, gst return filing due date, gst return filing process step by step, gst return filing online, gstr-1 due date, gstr-3b due date, qrmp due date, gst late fee, nil gst return, cmp-08 due date",
    desc="GST return filing 2026: GSTR-1 by the 11th, GSTR-3B by the 20th, QRMP quarterly dates (13th, 22nd / 24th), CMP-08, GSTR-4, GSTR-9 by 31 December, step-by-step online filing, nil returns, late fee and interest.",
    howto={"name": "How to file GST returns online", "description": "For regular GST taxpayers.", "steps": [
        {"name": "Log in to the GST portal", "text": "Use your GSTIN user ID."},
        {"name": "Reconcile GSTR-2B", "text": "Claim ITC only on invoices that appear in it."},
        {"name": "File GSTR-1", "text": "By the 11th (monthly) or 13th (QRMP)."},
        {"name": "Review and pay GSTR-3B", "text": "Pay through the cash and credit ledgers."},
        {"name": "File with DSC or EVC", "text": "By the 20th, or the 22nd / 24th under QRMP."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JA complete")
