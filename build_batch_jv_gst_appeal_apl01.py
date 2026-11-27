# -*- coding: utf-8 -*-
"""Batch JV (27 Nov 2026): GST appeal in Form APL-01 under section 107 - who can appeal, time limit, pre-deposit, filing
on the portal, the stay on recovery and the next step to the GST Appellate Tribunal.
Demand: sweep ac140 (27 Nov 2026), all 7 markets: "gst appeal apl 01", "apl 01 format", "gst appeal form apl 01", "gst apl
01 appeal to appellate authority", "gst apl 01 time limit", "what is gst apl 01", "gst appeal due date", "gst appeal time
limit"; no page covered GST appeals.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - an appeal against a demand order needs a CA.
Facts (verified 27 Nov 2026): section 107 CGST Act - appeal to the Appellate Authority within three months of
communication of the order, a further one month on sufficient cause; filed online in Form APL-01; pre-deposit of the full
admitted amount plus 10% of the disputed tax, capped at Rs 20 crore each under CGST and SGST (Rs 40 crore IGST) from
1 November 2024; once the pre-deposit is paid, recovery of the balance is stayed (section 107(7)); pre-deposit rules for
penalty-only orders were amended in 2025 - not restated in detail; second appeal to the GST Appellate Tribunal under
section 112 with a further pre-deposit. No fees, no timings beyond statutory, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026"

C = contact("the order you want to appeal (DRC-07 summary and the full order), the date it was communicated to you, the show cause notice and your reply, the hearing record if any, and payments already made against the demand")
PAGES = [dict(
    slug=SLUG,
    title="GST Appeal in Form APL-01 (2026): Time Limit, Pre-Deposit (10%, Rs 20 Crore Cap), Format, Filing Online and the Stay on Recovery",
    em="three months, 10% and a well-argued ground.",
    kicker="/ Businesses with GST demand, refund or cancellation orders &middot; First appeal under section 107 &middot; Updated 2026-11-27",
    lead=("<strong>If a GST officer passes an order you disagree with - a demand under section 73 or 74, a refund rejection, a cancellation of registration - your first remedy is an appeal to the Appellate Authority in Form APL-01 under section 107.</strong> "
          "It must be filed within three months of the order being communicated (one more month only with sufficient cause), and with a pre-deposit of the full admitted amount plus 10% of the disputed tax. "
          "Once the pre-deposit is paid, recovery of the rest of the demand is stayed while the appeal is pending."),
    sections=[
        ("/ The key rules", "What section 107 requires.",
         table(["Point", "Rule"], [
             ["Who can appeal", "Any person aggrieved by an order or decision of an adjudicating authority under GST"],
             ["Time limit", "Three months from the date the order is communicated; the Appellate Authority can allow one more month for sufficient cause"],
             ["Form", "APL-01, filed online on the GST portal with the grounds of appeal and the order"],
             ["Pre-deposit", "Full admitted tax, interest, fine, fee and penalty, plus 10% of the disputed tax - capped at Rs 20 crore each under CGST and SGST (Rs 40 crore under IGST)"],
             ["Stay", "Once the pre-deposit is paid, recovery of the balance is deemed stayed (section 107(7))"],
             ["Next step", "Second appeal to the GST Appellate Tribunal under section 112, with a further pre-deposit"]])),
        ("/ How to file", "Building an appeal that holds.",
         ul("<strong>Check the date of communication</strong> and count the three months from it; late appeals need a condonation request with reasons.",
            "<strong>Work out the admitted and disputed amounts</strong> and pay the pre-deposit (through the electronic cash or credit ledger as allowed).",
            "<strong>Draft the grounds:</strong> statement of facts, each ground of appeal with the legal basis - limitation, wrong section invoked, ITC eligibility, natural justice, calculation errors - and the relief sought.",
            "<strong>Attach the evidence</strong> that was before the officer and explain any new evidence and why it was not produced earlier.",
            "<strong>File APL-01</strong> on the portal, keep the acknowledgement, and attend the personal hearing.",
            "<strong>Penalty-only orders:</strong> the pre-deposit rules for appeals against orders that only impose a penalty were changed in 2025, so check the current requirement for your order before filing.")),
        ("/ Common grounds", "Where appeals succeed.",
         ul("Demand raised after the limitation period, or section 74 invoked without real evidence of fraud or suppression.",
            "Input tax credit denied on supplier default where you have invoices, payment and receipt of goods or services.",
            "Order passed without considering the reply or without a personal hearing.",
            "Arithmetical errors, double counting, or interest and penalty charged on amounts already paid.")
         + call_box("GST appeals", ["Checking limitation and communication dates",
                                    "Computing and paying the pre-deposit",
                                    "Drafting APL-01 grounds and statement of facts",
                                    "Appellate hearings and written submissions",
                                    "Second appeals to the GST Appellate Tribunal"],
                    "The order, the notice and your reply.")
         + sources("CGST Act, 2017 (sections 73, 74, 107, 112); CGST Rules (rule 108, Form APL-01); amendments effective 1 November 2024 to the pre-deposit caps and the 2025 amendment on penalty-only orders; site GST notice reply and DRC-01C guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is GST APL-01?", "APL-01 is the form for filing a first appeal to the GST Appellate Authority under section 107 against an order or decision of a GST officer, such as a demand order, refund rejection or cancellation of registration. It is filed online on the GST portal with the grounds of appeal."),
          ("What is the time limit for a GST appeal in APL-01?", "Three months from the date the order is communicated to you. The Appellate Authority can allow one further month if you show sufficient cause for the delay; beyond that the appeal cannot be admitted."),
          ("How much pre-deposit is required for a GST appeal?", "The full amount of tax, interest, fine, fee and penalty you admit, plus 10% of the disputed tax - capped at Rs 20 crore each under CGST and SGST (Rs 40 crore under IGST). The rules for appeals against penalty-only orders were amended in 2025, so check the requirement for your order."),
          ("Does filing a GST appeal stop recovery of the demand?", "Yes. Once the pre-deposit is paid and the appeal is filed, recovery of the balance of the demand is deemed stayed under section 107(7) until the appeal is decided."),
          ("Is there a format for a GST appeal?", "APL-01 itself is a prescribed online form, but the statement of facts and grounds of appeal are drafted by you: the facts, each ground with its legal basis, the evidence relied on and the relief sought. Well-structured grounds on limitation, wrong section, ITC eligibility and natural justice carry most appeals."),
          ("What should I send to file a GST appeal?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the order (DRC-07 summary and the full order), the date it was communicated, the show cause notice and your reply, any hearing record, and payments already made. We check the time left, compute the pre-deposit, draft the grounds and file APL-01. You keep your own GST login."),
          ("Can BQP handle GST appeals for my business?", "Yes. CA Durgesh Chavda works online with businesses facing GST demand, refund and cancellation orders. " + C)],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply (ASMT-10, DRC-01)"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01C / DRC-01B replies"),
             ("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST cancellation and revocation"),
             ("gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026.html", "GST refunds for exporters"),
             ("gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html", "GST changes from 1 November 2026")],
    cta_h="Got a GST order you want to challenge?", cta_b=C,
    keywords="gst appeal apl 01, apl 01 format, gst appeal time limit, gst appeal pre deposit, section 107 gst appeal, gst appellate authority, gst appeal due date, what is gst apl 01",
    desc="GST appeal in Form APL-01 under section 107: three-month time limit (plus one month on sufficient cause), pre-deposit of the admitted amount plus 10% of disputed tax capped at Rs 20 crore, filing online, the stay on recovery and the next step to the GST Appellate Tribunal.",
    howto={"name": "How to file a GST appeal in APL-01", "description": "From the order to a filed appeal.", "steps": [
        {"name": "Check the date", "text": "Count three months from the date the order was communicated."},
        {"name": "Pay the pre-deposit", "text": "Pay the admitted amount plus 10% of the disputed tax, within the cap."},
        {"name": "Draft the grounds", "text": "Statement of facts, grounds with legal basis, evidence and relief sought."},
        {"name": "File APL-01", "text": "File online on the GST portal and attend the hearing."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JV complete")
