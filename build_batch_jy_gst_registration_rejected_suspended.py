# -*- coding: utf-8 -*-
"""Batch JY (27 Nov 2026): GST registration rejected or suspended - the REG-03 query, REG-04 reply, REG-05 rejection,
reapplying or appealing, and suspension under rule 21A (REG-31) - what it means and how to get it lifted.
Demand: sweep ac142 (27 Nov 2026), all 7 markets: "gst application rejected", "... what next", "... by tax officer what to
do", "... without reason", "gst registration rejected reason / appeal", "gst suspended application", "gst registration
suspended means / reason / arbitrarily / status suspended", "gst registration suspension rules"; no page covered rejection
or suspension.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - a rejected or suspended GSTIN usually needs a CA.
Facts (verified 27 Nov 2026): rule 9 CGST Rules - if the officer needs clarification a notice is issued in REG-03 and the
applicant replies in REG-04 within seven working days; if not satisfied the officer rejects the application in REG-05 with
reasons recorded; site fact: Circular 257/03/2026 bars unwarranted document requests, deficiencies must be raised in REG-03,
missed timelines result in deemed approval; a rejection can be appealed under section 107 (APL-01, three months) or a fresh
application filed after fixing the defect. Rule 21A - registration is suspended when the person applies for cancellation,
when the officer believes it is liable to cancellation (with the REG-17 show cause notice), or on significant discrepancies
or specified non-compliance detected by the system (rule 21A(2A), intimated in REG-31); during suspension no taxable supply
and no refund (rule 21A(3A)); suspension is revoked on completion of the proceedings. Reply period stated as the time given
in the notice. No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "gst-registration-rejected-or-suspended-reg-03-reg-05-rule-21a-reg-31-what-to-do-2026"

C = contact("the rejection order (REG-05) or the suspension intimation (REG-31 or REG-17), the REG-03 query and your REG-04 reply if any, the ARN or GSTIN, your PAN, the business address proof and rent agreement or ownership papers, and your recent GST returns if registered")
PAGES = [dict(
    slug=SLUG,
    title="GST Registration Rejected or Suspended (2026): REG-03 Query, REG-05 Rejection, Reapply or Appeal, and Rule 21A Suspension (REG-31)",
    em="fix the defect, then reply or reapply.",
    kicker="/ New businesses, startups, NRIs and foreign-owned subsidiaries &middot; GST registration problems &middot; Updated 2026-11-27",
    lead=("<strong>A GST application is usually rejected because the officer was not satisfied with the place-of-business proof, the identity or signatory documents, or the reply to a clarification notice; a registration is suspended when cancellation proceedings start or the system finds serious mismatches or missed returns.</strong> "
          "Rejection can be fixed by a fresh, better-documented application or challenged in appeal. "
          "Suspension needs a prompt reply - while it lasts you should not make taxable supplies and refunds are blocked."),
    sections=[
        ("/ Rejection: how it happens", "The registration steps that go wrong.",
         table(["Stage", "What happens"], [
             ["Clarification notice", "If the officer needs more information, a notice is issued in REG-03"],
             ["Your reply", "Reply in REG-04 within seven working days with the clarification and documents asked for"],
             ["Rejection", "If not satisfied, the officer rejects the application in REG-05, with the reasons recorded"],
             ["Officer limits", "CBIC's Circular 257/03/2026 bars unwarranted document requests: deficiencies must be raised in REG-03, and missed timelines lead to deemed approval"],
             ["Remedy", "File a fresh application with the defect fixed, or appeal the REG-05 order under section 107 in APL-01 within three months"]])
         + ul("<strong>Common reasons:</strong> rent agreement or consent letter missing or unsigned, utility bill in another name or address mismatch, unclear photographs of the premises, signatory authorisation missing, a reply that did not answer the query, or a mismatch between PAN, Aadhaar and the application.",
              "<strong>'Rejected without reason':</strong> a rejection must record reasons; an order that does not, or that ignores your REG-04 reply, is a ground of appeal.")),
        ("/ Suspension under rule 21A", "What a suspended GSTIN means.",
         ul("<strong>When it happens:</strong> you have applied for cancellation; the officer believes the registration is liable to cancellation and issues a show cause notice (REG-17); or the system detects significant differences between your returns (for example GSTR-1, GSTR-3B and GSTR-2B) or other specified non-compliance, intimated in REG-31.",
            "<strong>Effect:</strong> you should not make taxable supplies while suspended, and no refund is granted for the period of suspension.",
            "<strong>How to lift it:</strong> reply to the REG-31 or REG-17 within the time given in the notice, explain or correct the mismatch, and file any pending returns; the suspension is revoked when the proceedings are completed in your favour.",
            "<strong>If it turns into cancellation:</strong> revocation is applied for in REG-21, and an order can be appealed in APL-01.")),
        ("/ What to do now", "A short checklist.",
         ul("Read the REG-05 or REG-31 / REG-17 carefully - the reason and the deadline decide the route.",
            "For a rejection, fix the document gap and reapply, or appeal if the reasons are wrong or missing.",
            "For a suspension, reconcile GSTR-1, GSTR-3B and GSTR-2B, file overdue returns, and reply on time with the working.",
            "NRIs and foreign companies: check whether normal registration or non-resident (REG-09) registration is the right route before reapplying.")
         + call_box("GST registration problems", ["Replying to REG-03 queries",
                                                  "Fresh applications after rejection",
                                                  "Appeals against REG-05 orders",
                                                  "Replies to REG-31 and REG-17 suspension notices",
                                                  "Revocation in REG-21 after cancellation"],
                    "The order or notice, ARN / GSTIN and documents.")
         + sources("CGST Act, 2017 (sections 25, 29, 107) and CGST Rules (rules 9, 21A, 22, 23; Forms REG-03, REG-04, REG-05, REG-17, REG-21, REG-31); CBIC Circular 257/03/2026 on registration (as summarised on the site's GST changes page); site GST registration, cancellation and appeal guides. Checked 27 November 2026.")),
    ],
    faqs=[("Why was my GST registration application rejected?", "Usually because the officer was not satisfied with the documents or the reply to a clarification notice (REG-03): missing or unsigned rent agreement or consent letter, address or name mismatch on the utility bill, unclear premises photographs, missing signatory authorisation, or a PAN / Aadhaar mismatch. The rejection order in REG-05 must record the reasons."),
          ("What should I do if my GST application is rejected?", "Read the reasons in the REG-05 order. If it was a document gap, fix it and file a fresh application. If the reasons are wrong, missing or ignore your reply, you can appeal under section 107 in Form APL-01 within three months of the order."),
          ("What does GST registration suspended mean?", "Under rule 21A your GSTIN is suspended while cancellation proceedings are pending - because you applied for cancellation, the officer issued a show cause notice, or the system found significant return mismatches or other non-compliance (intimated in REG-31). While suspended you should not make taxable supplies and no refund is granted for that period."),
          ("How do I remove a GST suspension?", "Reply to the REG-31 or REG-17 notice within the time given, explain or correct the mismatch, and file any pending returns. The suspension is revoked once the proceedings are completed in your favour; if the registration is cancelled instead, apply for revocation in REG-21 or appeal the order."),
          ("Can a GST officer ask for any document they like during registration?", "No. Per CBIC Circular 257/03/2026 as summarised on the site's GST changes page, unwarranted document requests are barred, deficiencies must be raised in REG-03, and missed timelines result in deemed approval."),
          ("What should I send if my GST registration was rejected or suspended?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the REG-05 order or the REG-31 / REG-17 notice, the REG-03 query and your reply if any, the ARN or GSTIN, PAN, address proof and rent or ownership papers, and recent returns if registered. We find the cause and prepare the reply, fresh application or appeal. You keep your own GST login."),
          ("Can BQP handle GST registration rejections and suspensions?", "Yes. CA Durgesh Chavda works online with new businesses, startups, NRIs and foreign-owned subsidiaries. " + C)],
    related=[("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?"),
             ("gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026.html", "GST cancellation and revocation"),
             ("gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026.html", "GST appeal in APL-01"),
             ("gst-drc-01c-drc-01b-notice-reply-itc-mismatch-gstr-2b-3b-liability-mismatch-gstr-1-3b-rule-88c-88d-2026.html", "DRC-01C / DRC-01B mismatch notices"),
             ("gst-registration-non-resident-taxable-person-india-foreign-company-reg-09-gstr-5-2026.html", "GST registration for a foreign company or NRI")],
    cta_h="GST registration rejected or suspended?", cta_b=C,
    keywords="gst application rejected, gst registration rejected what next, gst registration rejected appeal, gst registration suspended, gst registration suspended reason, gst suspension rule 21a, reg-31 reply, reg-03 reply, reg-05 rejection",
    desc="GST registration rejected or suspended: the REG-03 query and REG-04 reply, rejection in REG-05 and whether to reapply or appeal, suspension under rule 21A and the REG-31 notice, how to get it lifted, and what to send.",
    howto={"name": "How to fix a rejected or suspended GST registration", "description": "From the order or notice to a cleared GSTIN.", "steps": [
        {"name": "Read the reason", "text": "Check the REG-05 order or the REG-31 / REG-17 notice and its deadline."},
        {"name": "Fix the cause", "text": "Correct the document gap, or reconcile returns and file overdue ones."},
        {"name": "Reply, reapply or appeal", "text": "Reply to the suspension notice, file a fresh application, or appeal a wrong rejection."},
        {"name": "Track the outcome", "text": "Confirm the GSTIN is active or the registration certificate is issued."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JY complete")
