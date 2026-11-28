# -*- coding: utf-8 -*-
"""Batch KR (28 Nov 2026): Input tax credit blocked by the GST department under Rule 86A - the grounds, the one-year limit and
how to get the electronic credit ledger unblocked.
Demand: sweep ac224 (28 Nov 2026), all 7 markets: 'itc blocked by gst department', 'itc blocked' variants - no page on the
site (FAQ added in PR #887 on the DRC-01C page). User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: Rule 86A of the CGST Rules, 2017 - the Commissioner or an officer authorised by the Commissioner, not below the rank of
Assistant Commissioner, who has reasons to believe that input tax credit in the electronic credit ledger was fraudulently
availed or is ineligible may, for reasons recorded in writing, disallow the debit of an amount equal to that credit. Grounds:
credit on invoices of a supplier found non-existent or not conducting business; credit without receipt of goods or services;
tax charged not paid to the Government; the recipient itself found non-existent or not conducting business; credit without
a tax invoice or other valid document. The officer may allow the debit once satisfied the conditions no longer exist; the
restriction ceases after one year from the date it is imposed. Courts have required recorded reasons. No fees, no portal
menu paths, no case names, no statistics. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "itc-blocked-rule-86a-gst-electronic-credit-ledger-blocked-how-to-unblock-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, the amount blocked and the date, any "
     "communication or reasons you received, and the suppliers whose invoices are questioned. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="ITC Blocked by the GST Department Under Rule 86A (2026): Why the Electronic Credit Ledger Is Blocked, the One-Year Limit and How to Get It Unblocked",
    em="answer the reasons, with evidence.",
    kicker="/ GST-registered businesses &middot; Credit ledger blocked &middot; Updated 2026-11-28",
    lead=("<strong>If you cannot use input tax credit because the credit ledger shows a block, the department has usually acted under Rule 86A, which lets an officer of at least Assistant Commissioner rank stop the use of credit the officer has reasons to believe was fraudulently availed or is ineligible.</strong> "
          "Only the questioned amount can be blocked, reasons must be recorded, and the block lapses after one year - but a clear written representation with evidence can get it lifted sooner."),
    sections=[
        ("/ When an officer can block credit", "The grounds in Rule 86A.",
         table(["Ground", "What it usually means in practice"], [
             ["Supplier non-existent or not conducting business", "A supplier's registration was cancelled or found fake after you took credit"],
             ["Goods or services not received", "Movement or service evidence is doubted"],
             ["Tax not paid by the supplier", "The supplier collected GST on the invoice but did not pay it to the Government"],
             ["Recipient non-existent or not conducting business", "Your own place of business could not be verified"],
             ["No valid tax invoice or document", "Credit taken without the document the law requires"]])
         + ul("<strong>Who decides:</strong> the Commissioner, or an officer authorised by the Commissioner who is at least an Assistant Commissioner.",
              "<strong>How much:</strong> an amount equal to the credit in question - not the whole ledger.",
              "<strong>How long:</strong> the restriction ends one year after it was imposed, or earlier if the officer is satisfied.",
              "<strong>Reasons:</strong> the officer must record reasons in writing; ask for them if they were not shared.")),
        ("/ How to get the block lifted", "Representation first.",
         ul("<strong>Find out what was blocked and why:</strong> the amount, the date, the suppliers and invoices behind it, and the recorded reasons.",
            "<strong>Build the evidence:</strong> tax invoices, e-way bills and transport records, goods receipt or service delivery proof, payment to the supplier through the bank, and the supplier's returns showing the invoice.",
            "<strong>File a written representation</strong> with the officer asking for the debit to be allowed, point by point against each ground.",
            "<strong>If a supplier did not pay the tax:</strong> pursue the supplier, and consider reversing credit that cannot be supported to limit interest and penalty.",
            "<strong>If the block is arbitrary</strong> - no reasons, beyond the rule's grounds, or more than the questioned credit - it can be challenged before the High Court.",
            "<strong>Watch for what follows:</strong> a block is often followed by a show cause notice; prepare for it with the same evidence.")
         + call_box("input tax credit blocked under Rule 86A", ["What was blocked and the recorded reasons",
                                                               "Evidence for each questioned supplier and invoice",
                                                               "Written representation to the officer",
                                                               "Reversal of credit that cannot be supported",
                                                               "Show cause notice and High Court options"],
                    "GSTIN, blocked amount and date, any communication received, questioned suppliers.")
         + sources("CGST Rules, 2017 (rule 86A); CGST Act, 2017 (sections 16, 73, 74 and 74A); site GST notice response, DRC-01C / DRC-01B and GST consultant pages.")),
    ],
    faqs=[("Why has my input tax credit been blocked?", "Usually because an officer acted under Rule 86A after forming a belief that some credit was fraudulently availed or is ineligible - most often because a supplier was found non-existent, did not pay the tax it charged, or the goods or services were not received. The block covers only an amount equal to the credit in question."),
          ("How long can ITC stay blocked under Rule 86A?", "Up to one year from the date the restriction is imposed. The officer can allow the debit earlier once satisfied that the grounds no longer exist."),
          ("Can I use blocked credit to pay GST?", "No. While the block is in place, that amount cannot be debited from the electronic credit ledger, so tax due in the meantime has to be paid from other credit or in cash."),
          ("How do I get the ITC block removed?", "Ask for the recorded reasons, then file a written representation with the officer, with tax invoices, e-way bills, transport and receipt records, bank payment proof and the supplier's returns. If the block has no recorded reasons or goes beyond the rule, it can be challenged before the High Court."),
          ("Will a show cause notice follow a Rule 86A block?", "Often it does, proposing to recover the credit with interest and penalty. Prepare the same evidence for the reply, and reverse any credit that genuinely cannot be supported to limit interest."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, the amount blocked and the date, any communication or reasons received, and the suppliers whose invoices are questioned. Or book a call directly.")],
    related=[("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01C and DRC-01B notice reply"),
             ("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply"),
             ("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online"),
             ("gst-registration-rejected-or-suspended-reg-03-reg-05-rule-21a-reg-31-what-to-do-2026.html", "GST registration suspended or rejected")],
    cta_h="Input tax credit blocked?", cta_b=C,
    keywords="itc blocked by gst department, rule 86a, electronic credit ledger blocked, itc blocked how to unblock, gst credit blocked, itc blocked supplier non existent",
    desc="ITC blocked by the GST department under Rule 86A: the five grounds, who can block, only the questioned amount, one-year limit, recorded reasons, and how to get the electronic credit ledger unblocked with a representation and evidence.",
    howto={"name": "How to respond to an ITC block under Rule 86A", "description": "From reasons to representation.", "steps": [
        {"name": "Get the details", "text": "Amount, date, suppliers, invoices and the recorded reasons."},
        {"name": "Collect evidence", "text": "Invoices, e-way bills, receipts, bank payments, supplier returns."},
        {"name": "File a representation", "text": "Point by point against each ground; ask for the debit to be allowed."},
        {"name": "Prepare for next steps", "text": "Reverse unsupported credit; get ready for a show cause notice or a High Court challenge."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KR complete")
