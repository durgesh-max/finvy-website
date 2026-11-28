# -*- coding: utf-8 -*-
"""Batch KW (28 Nov 2026): E-way bill expired or goods detained - validity, extension, and detention and release under section 129
of the CGST Act.
Demand: sweep ac224 (28 Nov 2026), all 7 markets: 'e way bill expiry', 'e way bill expired', 'e way bill expired penalty',
'e way bill expired due to vehicle breakdown', 'e way bill expired but goods not delivered' - only an FAQ on the site (PR #887).
A gift-deed page was considered first but would duplicate the section 56(2)(x) and NRI gift pages. User steer 26 Nov 2026: more
call bookings / WhatsApp enquiries.
Facts: rule 138 CGST Rules - validity of one day for every 200 km (or part) for normal cargo (20 km for over-dimensional cargo),
counted from generation of Part B; extension by the generator or transporter within eight hours before or after expiry, giving
the reason and current location; total life capped at 360 days from generation (GSTN advisory, from 1 January 2025); goods moving
without a valid e-way bill can be detained under section 129: notice within seven days of detention and order within seven days
of service of the notice; release on payment of tax and penalty - for the owner coming forward, a penalty equal to 200% of the
tax payable (for exempt goods, 2% of the value or INR 25,000, whichever is lower); for others, the higher of 50% of the value or
200% of the tax (for exempt goods, 5% of the value or INR 25,000, whichever is lower) - or on furnishing security; appeal
against the order. Statutory penalties only (allowed by the user's 27 Nov rule); no fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "e-way-bill-expired-extension-goods-detained-section-129-mov-07-penalty-release-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the e-way bill number and its expiry, where the vehicle "
     "is now, why it was delayed, and any detention notice or order received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="E-Way Bill Expired or Goods Detained (2026): Validity, Extension Within Eight Hours, Section 129 Detention, Penalty and Release",
    em="extend in time, or act fast on detention.",
    kicker="/ Traders, manufacturers and transporters &middot; GST e-way bills &middot; Updated 2026-11-28",
    lead=("<strong>An e-way bill is valid for one day for every 200 km of normal cargo. If the goods will not arrive in time, the generator or transporter can extend it within eight hours before or after expiry. "
          "Goods moving on an expired e-way bill are treated as moving without one and can be detained under section 129 until tax and penalty are paid or security is given.</strong>"),
    sections=[
        ("/ Validity and extension", "Rule 138.",
         table(["Point", "Rule"], [
             ["Validity, normal cargo", "One day for every 200 km or part"],
             ["Validity, over-dimensional cargo", "One day for every 20 km or part"],
             ["Who can extend", "The generator or the transporter"],
             ["When", "Within eight hours before or after expiry"],
             ["What to state", "Reason (for example breakdown, accident, transhipment) and current location"],
             ["Overall limit", "360 days from the date of generation"]])
         + ul("<strong>Missed the window?</strong> Generate a fresh e-way bill before the goods move again.",
              "<strong>Change of vehicle:</strong> update Part B for the new vehicle before moving the goods.")),
        ("/ If goods are detained", "Section 129.",
         ul("<strong>Notice and order:</strong> the officer issues a notice within seven days of detention and passes an order within seven days of serving it - reply promptly with the invoice, e-way bill history and reasons for delay.",
            "<strong>Release as owner:</strong> on payment of the tax and a penalty equal to 200% of the tax payable (for exempt goods, 2% of the value or INR 25,000, whichever is lower).",
            "<strong>Release where the owner does not come forward:</strong> the higher of 50% of the value or 200% of the tax (for exempt goods, 5% of the value or INR 25,000, whichever is lower).",
            "<strong>Or furnish security</strong> for the amount while contesting the detention.",
            "<strong>Genuine delays matter:</strong> breakdowns, accidents and technical errors without intent to evade are grounds to argue and, if needed, to appeal.",
            "<strong>Appeal:</strong> the order can be appealed to the appellate authority.")
         + call_box("an expired e-way bill or detained goods", ["Extension or fresh e-way bill",
                                                               "Reply to the detention notice",
                                                               "Release on payment or security",
                                                               "Arguing a genuine delay",
                                                               "Appeal against the order"],
                    "E-way bill number and expiry, vehicle location, reason for delay, any notice or order.")
         + sources("CGST Act, 2017 (section 129); CGST Rules, 2017 (rule 138 and the MOV forms for detention and release); GSTN advisories on e-way bill validity and extension; site GST consultant and GST notice response pages.")),
    ],
    faqs=[("What happens if an e-way bill expires before the goods reach?", "If the goods cannot arrive in time, the generator or transporter can extend the e-way bill within eight hours before or after expiry, giving the reason and current location. Goods moving on an expired e-way bill are treated as moving without one and can be detained under section 129."),
          ("How is e-way bill validity calculated?", "One day for every 200 km (or part) for normal cargo, and one day for every 20 km for over-dimensional cargo, counted from when Part B is first entered. The total life, including extensions, is capped at 360 days from generation."),
          ("What is the penalty for an expired e-way bill?", "If goods are detained under section 129, the owner can get them released by paying the tax and a penalty equal to 200% of the tax payable (for exempt goods, 2% of the value or INR 25,000, whichever is lower), or by furnishing security. Where the owner does not come forward, the penalty is higher."),
          ("The e-way bill expired because the truck broke down. What now?", "Extend it within eight hours of expiry giving the breakdown as the reason, or generate a fresh one before moving. If the goods were already detained, reply to the notice with the breakdown evidence; a genuine delay without intent to evade is a strong ground in reply and in appeal."),
          ("How long can goods be held after detention?", "The officer must issue a notice within seven days of detention and pass an order within seven days of serving the notice. Paying the tax and penalty, or furnishing security, gets the goods released."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the e-way bill number and expiry, where the vehicle is, why it was delayed and any detention notice or order. Or book a call directly.")],
    related=[("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply"),
             ("itc-blocked-rule-86a-gst-electronic-credit-ledger-blocked-how-to-unblock-2026.html", "ITC blocked under Rule 86A"),
             ("best-ca-logistics-supply-chain-tech-india-2026.html", "CA for logistics and supply chain")],
    cta_h="E-way bill expired or goods held?", cta_b=C,
    keywords="e way bill expired, e way bill expiry, e way bill expired penalty, e way bill extension, e way bill expired due to vehicle breakdown, goods detained section 129, mov-07 notice reply",
    desc="E-way bill expired or goods detained: validity one day per 200 km, extension within eight hours before or after expiry, 360-day cap; section 129 detention, notice and order within seven days each, release on 200% penalty or security, appeal.",
    howto={"name": "How to handle an expiring e-way bill", "description": "Before and after expiry.", "steps": [
        {"name": "Check validity", "text": "One day per 200 km from Part B; note the expiry time."},
        {"name": "Extend in time", "text": "Within eight hours before or after expiry, with reason and location."},
        {"name": "If detained, reply", "text": "Answer the notice with invoice, e-way bill history and delay evidence."},
        {"name": "Release and appeal", "text": "Pay tax and penalty or give security; appeal the order if needed."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KW complete")
