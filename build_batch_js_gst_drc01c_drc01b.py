# -*- coding: utf-8 -*-
"""Batch JS (27 Nov 2026): GST DRC-01C (ITC mismatch, GSTR-2B vs GSTR-3B, rule 88D) and DRC-01B (liability mismatch,
GSTR-1 vs GSTR-3B, rule 88C) intimations - what they are, how to reply in Part B or pay through DRC-03, the seven-day
window and what happens if you ignore them.
Demand: sweep ac137 (27 Nov 2026), all 7 markets: "notice for itc mismatch form gst drc 01c", "... reply", "how to download
notice for itc mismatch form gst drc 01c", "gst notice reply for itc mismatch", "gst notification for itc mismatch"; no
page title covered DRC-01C or DRC-01B.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - a reconciliation-based reply usually needs a CA.
Facts (verified 27 Nov 2026): rule 88D inserted by Notification 38/2023-CT (4 August 2023); DRC-01C is issued when ITC
claimed in GSTR-3B exceeds ITC available in GSTR-2B by more than the prescribed amount / percentage; Part A shows the
period-wise difference; within seven days pay the excess (with interest under section 50) through DRC-03 or explain in
Part B; rule 88C / DRC-01B is the equivalent for output tax shown in GSTR-1 / IFF higher than GSTR-3B; not responding can
block filing of the next GSTR-1 until the intimation is dealt with (GSTN advisories). Thresholds not restated (verify on
portal). No fees, no timings beyond statutory, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026"

C = contact("your GSTIN, the DRC-01C or DRC-01B intimation (a screenshot or PDF from the portal), GSTR-3B, GSTR-2B and GSTR-1 for the months shown, your purchase register or books for those months, and any DRC-03 payment already made")
PAGES = [dict(
    slug=SLUG,
    title="GST DRC-01C and DRC-01B Notice Reply (2026): ITC Mismatch (GSTR-2B vs GSTR-3B) and Liability Mismatch (GSTR-1 vs GSTR-3B) - Rules 88D and 88C, Part B Reply, Seven-Day Window",
    em="reconcile, then pay or explain in seven days.",
    kicker="/ GST-registered businesses &middot; System-generated intimations &middot; Updated 2026-11-27",
    lead=("<strong>DRC-01C and DRC-01B are system-generated intimations on the GST portal, not show cause notices: DRC-01C flags input tax credit claimed in GSTR-3B that is higher than the credit shown in GSTR-2B, and DRC-01B flags output tax shown in GSTR-1 that is higher than the tax paid through GSTR-3B.</strong> "
          "You have seven days to either pay the difference with interest through DRC-03 or explain it in Part B of the form. "
          "Ignoring them can block your next GSTR-1 and usually leads to a proper notice later, so a quick, reconciled reply matters."),
    sections=[
        ("/ The two intimations", "What each one means.",
         table(["Form", "Rule", "What it flags", "Common genuine reasons"], [
             ["DRC-01C", "Rule 88D", "ITC claimed in GSTR-3B is more than ITC available in GSTR-2B beyond the prescribed limit", "Supplier filed GSTR-1 late, import IGST, ITC of an earlier period claimed now, ISD credit, timing of the 2B cut-off"],
             ["DRC-01B", "Rule 88C", "Tax liability in GSTR-1 / IFF is more than tax paid in GSTR-3B beyond the prescribed limit", "Invoice reported in GSTR-1 but tax paid in a later 3B, amendments, advances adjusted, typing errors in GSTR-1"]])),
        ("/ How to respond", "Within seven days, on the portal.",
         ul("<strong>Reconcile first:</strong> compare GSTR-3B with GSTR-2B (for DRC-01C) or GSTR-1 (for DRC-01B) invoice by invoice for the months shown, and work out how much is a timing difference and how much is a real excess.",
            "<strong>If the excess is real:</strong> pay it with interest under section 50 through DRC-03 and quote the DRC-03 reference in Part B.",
            "<strong>If it is explained:</strong> give the reason in Part B - for example supplier filed late and the credit appears in a later GSTR-2B, IGST on imports, or tax paid in the next month's GSTR-3B - and keep the reconciliation on file.",
            "<strong>Part payment and part explanation</strong> are allowed; the reply must cover the full difference.",
            "<strong>Find the form</strong> in the notices and intimations area of your GST portal login and the registered email; the reply is filed against the same reference number.")),
        ("/ If you ignore it", "Why a reply matters.",
         ul("The portal can stop you filing GSTR-1 for the next period until you pay or reply, which delays your customers' credit.",
            "The difference stays on record and is a common starting point for a scrutiny notice (ASMT-10) or a demand notice (DRC-01) later.",
            "A short, reconciled Part B reply now is far easier to defend than a demand two years later.")
         + call_box("DRC-01C and DRC-01B replies", ["GSTR-3B vs GSTR-2B and GSTR-1 reconciliation",
                                                    "Part B explanation with supporting working",
                                                    "DRC-03 payment and interest computation",
                                                    "Follow-up ASMT-10 or DRC-01 notices",
                                                    "Supplier follow-up for missing GSTR-1 invoices"],
                    "GSTIN, the intimation and the months shown.")
         + sources("CGST Rules, 2017 (rules 59, 88C and 88D; Notification 38/2023-Central Tax inserting rule 88D); CGST Act, 2017 (sections 16, 39, 50, 75(12)); GSTN advisories on DRC-01B and DRC-01C; site GST notice reply and section 16(4) guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a DRC-01C notice in GST?", "A system-generated intimation under rule 88D that the input tax credit you claimed in GSTR-3B is higher than the credit available in your GSTR-2B by more than the prescribed limit. It is not a show cause notice, but you must pay the excess or explain it within seven days."),
          ("How do I reply to a DRC-01C ITC mismatch notice?", "Reconcile GSTR-3B with GSTR-2B for the months shown. Pay any genuine excess with interest through DRC-03 and quote it in Part B, and explain the rest in Part B - for example supplier filed late and the credit appears in a later GSTR-2B, IGST on imports, or ITC of an earlier period. Reply within seven days on the GST portal."),
          ("What is DRC-01B?", "An intimation under rule 88C that the tax liability you reported in GSTR-1 (or IFF) is higher than the tax you paid through GSTR-3B by more than the prescribed limit. Pay the shortfall with interest through DRC-03 or explain the difference in Part B within seven days."),
          ("What happens if I do not reply to DRC-01C or DRC-01B?", "The portal can block your next GSTR-1 until you pay or reply, and the unexplained difference often leads to a scrutiny notice (ASMT-10) or a demand notice (DRC-01) later."),
          ("Can I explain part of the difference and pay the rest?", "Yes. Part B lets you show an amount paid through DRC-03 and give reasons for the remaining difference; the reply should account for the whole amount in the intimation."),
          ("What should I send to reply to a DRC-01C or DRC-01B notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your GSTIN, the intimation (screenshot or PDF), GSTR-3B, GSTR-2B and GSTR-1 for the months shown, your purchase register or books for those months, and any DRC-03 already paid. We reconcile, work out what to pay and what to explain, and draft the Part B reply. You keep your own GST login."),
          ("Can BQP reply to GST mismatch intimations for my business?", "Yes. CA Durgesh Chavda works online with GST-registered businesses, exporters and foreign-owned subsidiaries. " + C)],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply (ASMT-10, DRC-01)"),
             ("gst-itc-last-date-30-november-2026-fy-2025-26-section-16-4-claim-before-cutoff.html", "Section 16(4) ITC time limit"),
             ("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and due dates"),
             ("gstr-9-gstr-9c-fy-2025-26-mandatory-optional-tables-notification-05-2026-due-31-december-2026.html", "GSTR-9 for FY 2025-26"),
             ("income-tax-gst-notice-reply-draft-letter-generator-free-tool-format-word.html", "Free notice reply draft tool")],
    cta_h="Got a DRC-01C or DRC-01B?", cta_b=C,
    keywords="drc-01c notice reply, notice for itc mismatch form gst drc 01c, drc 01c reply, gst itc mismatch notice, gstr 2b vs 3b mismatch, drc-01b notice, gstr 1 vs 3b mismatch, rule 88d, rule 88c",
    desc="GST DRC-01C and DRC-01B explained: ITC mismatch between GSTR-2B and GSTR-3B (rule 88D) and liability mismatch between GSTR-1 and GSTR-3B (rule 88C), how to reply in Part B or pay through DRC-03 within seven days, and what happens if you ignore them.",
    howto={"name": "How to reply to a DRC-01C or DRC-01B intimation", "description": "Reconcile, then pay or explain within seven days.", "steps": [
        {"name": "Download the intimation", "text": "Open it from the notices area of your GST login and note the months and amounts."},
        {"name": "Reconcile", "text": "Compare GSTR-3B with GSTR-2B or GSTR-1 invoice by invoice for those months."},
        {"name": "Pay any real excess", "text": "Pay it with interest through DRC-03."},
        {"name": "File Part B", "text": "Quote the DRC-03 and explain the rest of the difference within seven days."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JS complete")
