# -*- coding: utf-8 -*-
"""Batch GH (24 Nov 2026): is GST registration mandatory for a startup, new or small business - turnover thresholds and
the compulsory-registration cases that apply regardless of turnover. Call-first page for founders.
Demand: sweep ac56 (24 Nov 2026), all 7 markets: "is gst registration mandatory for startup", "... for new business",
"... for small business". No such page on the site.
Facts (checked 24 Nov 2026): thresholds of aggregate turnover INR 40 lakh for suppliers of only goods (in most states, if
opted) and INR 20 lakh for services or mixed supplies; lower limits in special category states (INR 10 lakh for services,
and for goods in some states) (Tally, Razorpay, CAclubindia). Section 24 CGST Act requires registration regardless of
turnover for, among others: inter-state taxable supplies of goods; persons liable under reverse charge; casual and
non-resident taxable persons; persons required to deduct TDS or collect TCS; input service distributors; e-commerce
operators; suppliers of OIDAR services from outside India to unregistered persons (CAclubindia; Taxscan on reverse charge).
Inter-state supplies of services below the threshold are exempt from compulsory registration (Notification 10/2017-IT).
Exports of services count towards aggregate turnover (site GST export page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026"

C = contact("what you sell (goods, services or both), where your customers are (in your state, other states, abroad), your expected annual turnover and whether you sell through marketplaces")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Is GST Registration Mandatory for a Startup or Small Business? (2026): Turnover Thresholds, Amazon and Flipkart Sellers, and When You Must Register Anyway",
    em="turnover decides, unless one of the compulsory cases applies.",
    kicker="/ Startups &middot; GST &middot; Registration &middot; Updated 2026-11-24",
    lead=("<strong>A startup or small business must register for GST once its aggregate turnover crosses INR 20 lakh a year for services (INR 40 lakh for businesses supplying only goods in most states), with lower limits in some special category states.</strong> "
          "Being a startup or DPIIT-recognised does not exempt you. "
          "Some businesses must register <strong>from the first rupee</strong> whatever their turnover: anyone making <strong>inter-state sales of goods</strong>, anyone liable to pay GST under <strong>reverse charge</strong>, casual and non-resident taxable persons, and those required to deduct or collect tax at source. "
          "Service providers selling to other states or abroad below INR 20 lakh need not register, but exports count towards the threshold. "
          "Many startups register voluntarily anyway, to claim input tax credit and to work with large clients."),
    sections=[
        ("/ Quick answers", "What new founders ask.",
         ul("<strong>Is GST registration mandatory for a startup?</strong> Only once turnover crosses the threshold (INR 20 lakh for services, INR 40 lakh for goods-only in most states), or if a compulsory case applies. Startup recognition gives no GST exemption.",
            "<strong>Is GST registration mandatory for a new business with no sales yet?</strong> No, unless a compulsory case applies, such as inter-state sales of goods. You must apply within 30 days of becoming liable.",
            "<strong>Do I need GST for selling services to clients in other states?</strong> Not below INR 20 lakh of aggregate turnover; services supplied inter-state are exempt from compulsory registration up to the threshold.",
            "<strong>Do I need GST for selling goods online?</strong> Usually yes for inter-state sales of goods; small sellers of goods within their own state face special rules on marketplaces, so check your case.",
            "<strong>Should I register voluntarily?</strong> Often yes for B2B startups: you can claim input tax credit, large clients may insist, and exporters need registration to file an LUT.")),
        ("/ Thresholds and compulsory cases", "When registration is required.",
         table(["Situation", "Registration needed?"], [
             ["Services or mixed supplies, aggregate turnover above INR 20 lakh", "Yes (INR 10 lakh in special category states)"],
             ["Only goods, aggregate turnover above INR 40 lakh (most states)", "Yes (lower in some special category states)"],
             ["Inter-state taxable supply of goods", "Yes, regardless of turnover"],
             ["Inter-state supply of services below INR 20 lakh", "No"],
             ["Liable to pay GST under reverse charge", "Yes, regardless of turnover"],
             ["Casual taxable person or non-resident taxable person", "Yes, regardless of turnover"],
             ["Required to deduct TDS or collect TCS under GST", "Yes, regardless of turnover"],
             ["Export of services", "Counts towards turnover; register above the threshold, and file an LUT to export without GST"]])
         + '<p>Exporting services? See ' + L("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services") + '. Foreign companies: ' + L("gst-registration-non-resident-taxable-person-india-foreign-company-reg-09-gstr-5-2026.html", "GST registration as a non-resident taxable person") + '.</p>'),
        ("/ Getting registered", "Steps and what follows.",
         ul("<strong>Apply online</strong> on the GST portal (Form REG-01) with PAN, Aadhaar authentication, business address proof and bank details.",
            "<strong>Timing:</strong> within 30 days of becoming liable; a voluntary registration can be taken any time.",
            "<strong>After registration:</strong> monthly or quarterly returns (GSTR-1 and GSTR-3B), annual return where applicable, and invoices with your GSTIN.",
            "<strong>Composition scheme:</strong> small businesses may opt for a simpler scheme with a low rate and no input tax credit, but it is not available for inter-state supplies or most services.",
            "<strong>Founders setting up:</strong> see " + L("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "the startup tax holiday") + " for income tax.")
         + call_box("GST registration for a startup", ["Whether you must register now",
                                                       "Voluntary registration: pros and cons",
                                                       "LUT for exports",
                                                       "Returns and invoices",
                                                       "Composition scheme eligibility"],
                    "what you sell, where your customers are and your expected turnover.")
         + sources("Central Goods and Services Tax Act, 2017, sections 22 (threshold) and 24 (compulsory registration); Notification 10/2017-Integrated Tax (inter-state service suppliers below threshold); notifications raising the goods threshold to INR 40 lakh; practitioner guides from Tally, Razorpay and CAclubindia; Taxscan on reverse charge and section 24. Checked 24 November 2026.")),
    ],
    faqs=[("Is GST registration mandatory for a startup?", "Only when aggregate turnover crosses INR 20 lakh for services (INR 40 lakh for goods-only businesses in most states), or when a compulsory case applies, such as inter-state sales of goods or reverse charge liability. Startup or DPIIT recognition does not exempt you from GST."),
          ("Is GST registration mandatory for a new business?", "Not before the turnover threshold, unless a compulsory case applies. Once you become liable, apply within 30 days. You can also register voluntarily from day one."),
          ("Is GST registration mandatory for a small business selling services to other states?", "No, if aggregate turnover is within INR 20 lakh (INR 10 lakh in special category states). Inter-state supplies of services below the threshold do not trigger compulsory registration."),
        ("Is GST registration mandatory to sell on Amazon, Flipkart or other marketplaces?", "Not always, since 1 October 2023. Section 24 makes registration compulsory for anyone selling goods through an e-commerce operator, but Notification 34/2023-Central Tax waives it for a seller whose aggregate turnover is within the registration threshold and who supplies goods through e-commerce operators in only one state or union territory. Such a seller must first get an enrolment number on the GST portal by validating their PAN, give it to the marketplace, and must not sell before it is issued; the enrolment lapses once they take a regular registration. Selling to buyers in other states from your state, selling on marketplaces in more than one state, crossing the threshold, or wanting input tax credit or an LUT for exports all point to a regular GST registration. Many marketplaces also ask for a GSTIN in their own seller terms, so check before listing. Service providers selling through e-commerce operators below the threshold are separately exempt. WhatsApp +91 78018 87130 with what you sell, which marketplaces and states, and your expected turnover, or book a call."),
          ("Do exports count for the GST threshold?", "Yes. Exports of services count towards aggregate turnover. Above the threshold you must register, and an LUT lets you export without charging GST."),
          ("Should a startup register for GST voluntarily?", "Often, if it sells to businesses or exports: registration lets you claim input tax credit, meets client requirements and allows an LUT for exports. The trade-off is regular returns."),
        ("How do I apply for GST registration online?", "On the GST portal, file Form GST REG-01: Part A with PAN, legal name, email and mobile to get a temporary reference number, then Part B with business details, place of business, bank account, authorised signatory and documents, verified with EVC or a digital signature. Every person named in the form must then complete Aadhaar authentication, by OTP link or by biometric verification and document check at a GST Suvidha Kendra when the portal asks for an appointment."),
        ("How do I check my GST registration status?", "Use the track application status option under Services on the GST portal with the ARN (application reference number) issued after submission. If biometric authentication or document verification is not completed within 15 days of submitting Part B, the ARN is not generated, and a clarification notice (REG-03) must be answered in REG-04 within seven working days."),
        ("What are the GSTR-1 and GSTR-3B due dates?", "Monthly filers: GSTR-1 by the 11th and GSTR-3B by the 20th of the following month. Under the QRMP scheme (turnover up to Rs 5 crore, quarterly returns): GSTR-1 by the 13th and GSTR-3B by the 22nd or 24th, depending on the state, of the month after each quarter, with tax for the first two months paid in PMT-06 by the 25th and optional invoice uploads (IFF) by the 13th. Check the GST portal calendar for any extension."),
        ("What is the GST late fee per day?", "For GSTR-3B and GSTR-1 the late fee is Rs 50 a day (Rs 25 CGST plus Rs 25 SGST), or Rs 20 a day for a nil return, up to a cap per return that is commonly reported as Rs 500 for nil returns and Rs 2,000, Rs 5,000 or Rs 10,000 depending on turnover. Separately, interest at 18% a year runs on tax paid late. The late fee is paid in cash before the return can be filed."),
          ("Can BQP handle GST registration and returns?", "Yes. " + C)],
    related=[("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services"),
             ("gst-registration-non-resident-taxable-person-india-foreign-company-reg-09-gstr-5-2026.html", "GST for non-resident taxable persons"),
             ("how-to-receive-payment-from-foreign-clients-in-india-purpose-code-fira-firc-gst-2026.html", "Receiving payments from foreign clients"),
             ("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "Startup tax holiday"),
             ("angel-tax-abolished-effective-date-which-year-startups-section-56-2-viib-2026.html", "Angel tax abolished")],
    cta_h="Starting up and unsure about GST?", cta_b=C,
    keywords="is GST registration mandatory for startup, is GST registration mandatory for new business, is GST registration mandatory for small business, GST threshold 20 lakh 40 lakh, compulsory GST registration section 24, GST registration startup India 2026",
    desc="Is GST registration mandatory for a startup or small business (2026)? Above INR 20 lakh turnover for services or INR 40 lakh for goods (most states); compulsory regardless of turnover for inter-state goods, reverse charge, casual and non-resident persons, TDS/TCS; exports count; voluntary registration pros.",
    howto={"name": "How to decide whether your startup needs GST registration", "description": "Checks in order.", "steps": [
        {"name": "Check compulsory cases", "text": "Inter-state goods, reverse charge, casual or non-resident, TDS/TCS."},
        {"name": "Estimate aggregate turnover", "text": "Including exports and exempt supplies, across the PAN."},
        {"name": "Compare with the threshold", "text": "INR 20 lakh services, INR 40 lakh goods-only (most states)."},
        {"name": "Consider voluntary registration", "text": "For input tax credit, B2B clients and exports under LUT."},
        {"name": "Apply on the GST portal", "text": "Form REG-01 within 30 days of becoming liable."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GH complete")
