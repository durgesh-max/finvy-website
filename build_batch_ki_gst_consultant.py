# -*- coding: utf-8 -*-
"""Batch KI (27 Nov 2026): GST consultant service page - what a GST consultant (CA) handles for small businesses, startups,
freelancers, exporters and foreign companies, and how to engage one online when searching 'GST consultant near me'.
Demand: sweep ac163 (27 Nov 2026), all 7 markets: "gst consultant near me", "gst consultant"; the site had GST topic pages
(registration, returns, cancellation, notices, refunds, GSTR-9) but no general GST consultant service page.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - GST registration, returns, notices and refunds need a CA.
Facts (site pages and earlier verified rounds): registration threshold Rs 20 lakh for services in most states (lower in
special category states), compulsory registration in some cases regardless of turnover; GSTR-1 and GSTR-3B monthly or
quarterly under QRMP; GSTR-3B needs the tax paid; nil returns are mandatory; late fee Rs 50 a day (Rs 20 for nil) with
caps; interest 18%; LUT in RFD-11 for each financial year for zero-rated exports; GSTR-9 for FY 2025-26 due 31 December
2026; cancelled registration revoked in REG-21 within 90 days (extendable); notices in ASMT-10 / DRC-01 / DRC-01B / DRC-01C /
REG-17 need replies within the stated time. No fees, no office claims (the work is done online), no statistics, no portal
menu paths, never ask for portal passwords."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026"

C = contact("your GSTIN (or PAN and business details if not yet registered), the state, what you sell and to whom (India or abroad), the returns pending, and a copy of any GST notice or portal message")
PAGES = [dict(
    slug=SLUG,
    title="GST Consultant and GST Registration Consultant Online (2026): Registration, Returns, LUT and Refunds, Notice Replies and GSTR-9 - Near Me, in Chennai, Delhi, Bangalore, Jaipur or Anywhere",
    em="registered right, filed on time, notices answered.",
    kicker="/ Small businesses, startups, freelancers, exporters and foreign companies &middot; GST registration, returns, refunds and notices &middot; Updated 2026-11-27",
    lead=("<strong>A GST consultant gets you registered when the law requires it, files GSTR-1 and GSTR-3B on time, keeps input tax credit matching, and answers notices before they turn into demands.</strong> "
          "Exporters also need an LUT each year and refunds of unused credit; foreign companies selling into India may need their own registration. "
          "All of this is done on the GST portal from documents, so a GST consultant does not have to be near you - a call and shared documents are enough."),
    sections=[
        ("/ What a GST consultant handles", "From registration to notices.",
         table(["Situation", "What is done"], [
             ["Starting a business or crossing the threshold", "Check whether registration is required (Rs 20 lakh for services in most states, or compulsory in some cases) and apply"],
             ["Every month or quarter", "GSTR-1 (sales) and GSTR-3B (summary and tax payment), QRMP if eligible, reconciliation with GSTR-2B"],
             ["Exporting goods or services", "LUT in Form RFD-11 for each financial year, zero-rated invoices, refund of unused input tax credit"],
             ["Every year", "GSTR-9 annual return (FY 2025-26 due 31 December 2026) and GSTR-9C where it applies"],
             ["A notice arrives", "Reply to ASMT-10, DRC-01, DRC-01B / DRC-01C mismatch notices, REG-17 show cause notices and summons within the time stated"],
             ["Registration cancelled or suspended", "File pending returns and apply for revocation in REG-21 within the time allowed"],
             ["Foreign company or non-resident supplier", "Registration as a non-resident taxable person or OIDAR supplier where required"]])
         + ul("<strong>Why it matters:</strong> late returns attract a daily late fee and 18% interest, block the next return and e-way bills, and stop your buyers getting input tax credit.",
              "<strong>Credit is the biggest risk:</strong> most notices come from mismatches between your returns and your suppliers' or buyers' returns - monthly reconciliation prevents them.",
              "<strong>Your login stays yours:</strong> returns can be prepared from your sales and purchase data and filed with your approval; you never need to hand over portal passwords in an email or message.")),
        ("/ How to engage one from anywhere", "Near you, or not.",
         ul("<strong>Online by design:</strong> GST work runs on invoices, purchase registers, bank statements and the GST portal - none of it needs an office visit.",
            "<strong>Start with a health check:</strong> list the returns filed and pending, compare GSTR-1, GSTR-3B and GSTR-2B for the year, and check any portal notices.",
            "<strong>Then fix in order:</strong> notices with deadlines first, pending returns next (oldest first, as each return blocks the next), then annual returns and refunds.",
            "<strong>Keep a calendar:</strong> GSTR-1, GSTR-3B, the yearly LUT before the first export of the year, and GSTR-9 by 31 December.")
         + call_box("GST consultant", ["GST registration and amendments",
                                       "Monthly / quarterly GSTR-1 and GSTR-3B",
                                       "LUT and export refunds",
                                       "Notice and show cause notice replies",
                                       "GSTR-9 / 9C, revocation of cancelled registration"],
                    "GSTIN or PAN, sales and purchase data, pending returns and any notice.")
         + sources("Central Goods and Services Tax Act, 2017 and CGST Rules, 2017 (registration, returns, late fee, interest, LUT, refunds, revocation); GST portal notifications on GSTR-9 / 9C for FY 2025-26; site GST registration, return filing, cancellation, notice reply, export refund and GSTR-9 guides. Checked 27 November 2026.")),
    ],
    faqs=[("What does a GST consultant do?", "They check whether you need GST registration and apply for it, file GSTR-1 and GSTR-3B every month or quarter, reconcile your input tax credit with GSTR-2B, file the LUT and refund claims for exports, prepare the GSTR-9 annual return, and reply to GST notices and show cause notices. For a cancelled or suspended registration they file the pending returns and the revocation application."),
          ("How does a GST registration consultant register my business, and what documents are needed?", "The application (REG-01) is filed online on the GST portal with the PAN of the business, Aadhaar and photographs of the proprietor, partners or directors, proof of the principal place of business (electricity bill, property tax receipt, rent agreement or owner's consent letter), bank account details, and the constitution documents (partnership deed, LLP agreement or certificate of incorporation). Aadhaar authentication follows, and some applicants are asked to complete biometric verification at a GST Suvidha Kendra. The officer then approves the application or raises a query in REG-03, which is answered in REG-04 with documents. A consultant checks the documents before filing so that queries and rejections are less likely, and the work is done online, whether you are in Chennai, Delhi, Bangalore, Jaipur or abroad. WhatsApp +91 78018 87130 with the PAN, the type of business, the state and address of the place of business and what you sell, and we tell you whether registration is needed and what to send."),
          ("I am searching for a GST consultant near me. Does location matter?", "Not for the work. GST registration, returns, refunds and most notice replies are prepared from documents and filed online on the GST portal, so a call and shared documents are enough wherever you are. A personal hearing, where one is fixed, can usually be attended online or through an authorised representative."),
          ("Do I need GST registration?", "For services, registration is generally required once aggregate turnover crosses Rs 20 lakh in a financial year in most states (lower in special category states); some cases need registration regardless of turnover, such as certain inter-state or e-commerce supplies. Exporters below the threshold often register to export under LUT and claim refunds. Check your own case before deciding."),
          ("What happens if I do not file GST returns on time?", "A late fee runs every day (Rs 50, or Rs 20 for a nil return, up to the caps), 18% interest runs on tax paid late, the next return cannot be filed, e-way bills can be blocked and your buyers lose input tax credit. Continued non-filing can lead to a show cause notice in REG-17 and cancellation of the registration."),
          ("I got a GST notice. What should I do first?", "Note the form (for example ASMT-10, DRC-01, DRC-01B, DRC-01C or REG-17), the period and the reply date, then gather the returns, invoices and reconciliations for that period. Reply within the time stated, with documents, even if only to explain and ask for time - an unanswered notice is usually decided against you."),
        ("How long do I have to reply to a GST show cause notice?", "Reply in Form GST DRC-06 within the period stated in the notice, usually 30 days. If more time is needed, ask the officer in writing before the date passes; personal hearings can be adjourned only three times. An unanswered notice can be decided ex parte, and the demand, interest and penalty then have to be challenged in appeal instead. Read the notice for the section (73, 74 or 74A), the period and the amounts, collect the returns, invoices and reconciliations it relies on, and reply point by point. Book a call to have the reply drafted and filed on time."),
        ("What happens if an e-way bill expires before the goods reach?", "An e-way bill is valid for one day for every 200 km (or part) for normal cargo. If the goods cannot reach in time, for example because of a vehicle breakdown, the generator or transporter can extend it on the e-way bill portal within eight hours before or after expiry, giving the reason and the current location; the total life is capped at 360 days from generation. Goods moving on an expired e-way bill are treated as moving without one and can be detained under section 129 until the tax and penalty are paid or security is furnished. Book a call if goods have been detained or a penalty order issued."),
        ("Do export invoices need a GST e-invoice?", "Yes, if your aggregate turnover in any financial year from 2017-18 onwards has crossed INR 5 crore. Exports of goods and services, with IGST paid or under LUT without tax, are reported on the Invoice Registration Portal as export supplies, and the IRN and QR code must appear on the invoice; if your turnover is INR 10 crore or more, the invoice must be reported within 30 days of its date. Below the threshold an ordinary tax invoice, with the LUT reference where relevant, is enough. Book a call to check your e-invoicing and LUT set-up."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN (or PAN and business details if not registered), the state, what you sell and to whom, the returns pending and a copy of any notice. We tell you what is due and in what order, or book a call.")],
    related=[("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and late fee"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice replies"),
             ("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST cancellation and revocation"),
             ("gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026.html", "GST refund for exporters"),
             ("gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html", "GSTR-9 / 9C for FY 2025-26")],
    cta_h="Need GST registration, returns or a notice reply?", cta_b=C,
    keywords="gst consultant, gst consultant near me, gst registration consultant, gst registration consultants in chennai, gst registration consultants in delhi, gst registration consultants in bangalore, gst registration consultants in jaipur, gst consultant online, gst return filing consultant, gst registration consultant, gst notice reply consultant, gst practitioner, gst refund consultant, gstr-9 filing, gst services for small business",
    desc="GST consultant online: registration check and application, GSTR-1 / GSTR-3B filing, input tax credit reconciliation, LUT and export refunds, GST notice and REG-17 replies, revocation and GSTR-9 by 31 December 2026 - for anyone searching for a GST consultant near me.",
    howto={"name": "How to get GST compliance in order", "description": "From health check to annual return.", "steps": [
        {"name": "Run a GST health check", "text": "List returns filed and pending, and compare GSTR-1, GSTR-3B and GSTR-2B for the year."},
        {"name": "Answer notices first", "text": "Reply to any notice with a deadline, with documents."},
        {"name": "File pending returns", "text": "Oldest first, paying tax, interest and late fee."},
        {"name": "Close the year", "text": "GSTR-9 / 9C, LUT for the next year and any refund claims."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KI complete")
