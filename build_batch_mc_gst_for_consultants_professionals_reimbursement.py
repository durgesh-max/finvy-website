# -*- coding: utf-8 -*-
"""Batch MC (28 Nov 2026): GST for consultants and professionals - when registration is needed, the usual rate, foreign clients
(export of services and LUT), the services composition scheme, reverse charge on legal services, exempt health care, and whether
GST applies to reimbursement of expenses (pure agent rule 33).
Demand: sweep ac249 (28 Nov 2026), all 7 markets: 'gst for consultants', 'gst for consultants in india', 'gst number for
consultants', 'gst for professional consultants' (coverage 0.33-0.50) and 'is gst applicable on reimbursement of expenses' (6
markets, 0.25) - the site's GST consultant page is a service page, not a guide for consultants as suppliers. Consultants and
professionals are core prospects. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act sections 9(3), 15, 22, 24 and 2(6); IGST Act section 16; CGST Rules rule 33; services composition under
Notification 2/2019-Central Tax (Rate) matched to the site composition page): registration once aggregate turnover crosses INR 20 lakh
for services (INR 10 lakh in some special category states), or voluntarily; inter-state services alone do not force registration
below the threshold; most professional and consulting services are taxed at 18%; services to foreign clients that meet the export
conditions are zero-rated - supply under LUT without IGST, or pay IGST and claim refund; the services composition scheme lets eligible
service providers with turnover up to INR 50 lakh in the previous year pay 6% without input tax credit and without charging GST;
legal services by an advocate or firm of advocates to a business entity are under reverse charge (the recipient pays); health care
services by clinical establishments and authorised medical practitioners are exempt; reimbursements charged to the client generally
form part of the value of the supply (section 15(2)), except expenses incurred as a pure agent meeting rule 33 conditions (written
agreement, payment on the client's behalf, separately shown on the invoice, recovered at actual, the client receives the procured
supply). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-for-consultants-professionals-india-registration-threshold-18-percent-export-lut-reimbursement-pure-agent-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the services you provide, your turnover for this "
     "and last year, how many clients are in India and abroad, the states you serve, and how you bill expenses to clients. Or "
     "book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST for Consultants and Professionals in India (2026): When to Register, the 18% Rate, Foreign Clients and LUT, Composition at 6%, Reverse Charge and GST on Reimbursements",
    em="register at the right time, bill it the right way.",
    kicker="/ Consultants, freelancers, advisers, designers and other professionals &middot; GST on professional services &middot; Updated 2026-11-28",
    lead=("<strong>A consultant or professional needs GST registration once turnover crosses INR 20 lakh (INR 10 lakh in some special category states), or earlier by choice. "
          "Most professional services are taxed at 18%; services to foreign clients that meet the export conditions are zero-rated under an LUT; small service providers can opt for composition at 6%. "
          "Expenses you recharge to clients usually attract GST too - unless you incur them strictly as a pure agent.</strong>"),
    sections=[
        ("/ Registration, rate and foreign clients", "The basics for professionals.",
         table(["Point", "Rule"], [
             ["Registration threshold", "Aggregate turnover above INR 20 lakh for services (INR 10 lakh in some special category states)"],
             ["Inter-state clients only", "Do not by themselves force registration below the threshold"],
             ["Usual rate", "18% for most professional and consulting services"],
             ["Foreign clients", "Export of services is zero-rated: supply under an LUT without IGST, or pay IGST and claim refund; payment must come in convertible foreign exchange (or as RBI permits)"],
             ["Composition for services", "6% without input tax credit, for eligible providers with turnover up to INR 50 lakh in the previous year; cannot charge GST to clients"],
             ["Legal services by advocates", "Reverse charge - a business client pays the GST"],
             ["Health care by doctors and clinics", "Exempt"]])
         + ul("<strong>Voluntary registration:</strong> worth considering if business clients want to claim input tax credit or you export services and want refunds.",
              "<strong>Aggregate turnover:</strong> counts all your supplies across India under the same PAN, including exempt and export supplies.")),
        ("/ GST on reimbursement of expenses", "Pure agent or part of your fee?",
         ul("<strong>General rule:</strong> travel, hotel, courier and other expenses you recharge to a client are part of the value of your service and attract GST at the same rate.",
            "<strong>Pure agent exception (rule 33):</strong> expenses are excluded only if you act as the client&rsquo;s pure agent under a written agreement, pay on the client&rsquo;s behalf, show them separately on the invoice, recover them at actual, and the client receives the supply you procured (for example government fees paid in the client&rsquo;s name).",
            "<strong>Invoices:</strong> show fees, taxable reimbursements and pure agent recoveries as separate lines.",
            "<strong>Input tax credit:</strong> a registered consultant can claim credit on business purchases, except blocked items.",
            "<strong>Returns:</strong> monthly or quarterly returns (QRMP), plus annual return where applicable.")
         + call_box("GST for consultants and professionals", ["Registration and threshold check",
                                                              "Export of services and LUT",
                                                              "Composition vs regular scheme",
                                                              "Invoice structure for fees and reimbursements",
                                                              "Returns, credits and notices"],
                    "Services, turnover, clients in India and abroad, states served, how you bill expenses.")
         + sources("CGST Act, 2017 (sections 2(6), 9(3), 15, 22 and 24); IGST Act, 2017 (sections 2(6) and 16); CGST Rules, 2017 (rule 33); CBIC rate and reverse charge notifications including Notification 2/2019-Central Tax (Rate); site GST registration, composition, export of services and blocked credits pages.")),
    ],
    faqs=[("Do consultants need GST registration in India?", "Yes, once aggregate turnover crosses INR 20 lakh for services (INR 10 lakh in some special category states). Below that, registration is optional - many register voluntarily for business clients or to export services under an LUT."),
          ("What is the GST rate for consultancy and professional services?", "Most professional and consulting services are taxed at 18%. Some services have special treatment - for example legal services by advocates to businesses are under reverse charge, and health care by doctors is exempt."),
          ("Is GST charged on consulting services to foreign clients?", "Services that meet the export of services conditions are zero-rated. You can supply under a Letter of Undertaking without paying IGST, or pay IGST and claim a refund, with payment received in convertible foreign exchange or as RBI permits."),
          ("Is GST applicable on reimbursement of expenses?", "Generally yes - expenses recharged to a client are part of the value of the service. They are excluded only when you act as a pure agent under rule 33: a written agreement, payment on the client's behalf, separate disclosure on the invoice, recovery at actual, and the client receiving the procured supply."),
          ("Can a consultant use the GST composition scheme?", "Yes, eligible service providers with turnover up to INR 50 lakh in the previous year can pay 6% under the services composition scheme, without input tax credit and without charging GST to clients."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your services, turnover, clients in India and abroad, states served and how you bill expenses. Or book a call directly.")],
    related=[("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?"),
             ("gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html", "GST on export of services and LUT"),
             ("gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026.html", "GST composition scheme"),
             ("best-ca-freelancer-consultant-tax-india-2026.html", "Income tax for freelancers and consultants")],
    cta_h="Consultant or professional working out GST?", cta_b=C,
    keywords="gst for consultants, gst for consultants in india, gst number for consultants, gst for professional consultants, gst rate on consultancy services 18 percent, is gst applicable on reimbursement of expenses, pure agent rule 33 gst",
    desc="GST for consultants and professionals: registration above INR 20 lakh (INR 10 lakh in some states), 18% on most professional services, zero-rated export of services under LUT, composition at 6% up to INR 50 lakh, reverse charge on legal services, exempt health care, and GST on reimbursements (pure agent rule 33).",
    howto={"name": "How consultants should handle GST", "description": "Register, bill, file.", "steps": [
        {"name": "Check the threshold", "text": "Aggregate turnover above INR 20 lakh (INR 10 lakh in some states) - or register voluntarily."},
        {"name": "Choose the scheme", "text": "Regular at 18% with credit, or composition at 6% if eligible."},
        {"name": "Handle foreign clients", "text": "File an LUT and meet the export of services conditions."},
        {"name": "Bill correctly", "text": "Separate fees, taxable reimbursements and pure agent recoveries."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MC complete")
