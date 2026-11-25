# -*- coding: utf-8 -*-
"""Batch HW (25 Nov 2026): GST registration cancellation - voluntary (REG-16, officer's order REG-19, usually within 30
days, GSTIN suspended meanwhile), cancellation by the officer (show cause REG-17, reply REG-18, order REG-19), final return
GSTR-10 within three months of the cancellation date or order (whichever is later, section 45), reversal of ITC on stock
(section 29(5)), revocation (REG-21) only where the officer cancelled - time limit conflicts in sources, stated as under
section 30 / rule 23 and to be checked; cancellation order download; liabilities continue.
Demand: sweep ac105 (25 Nov 2026), all 7 markets: "gst cancellation", "gst cancellation certificate download", "gst
cancellation charges", "gst cancellation certificate".
Facts (checked 25 Nov 2026): Tally, Razorpay, Busy, IndiaFilings, CAclubindia, Angel One GST cancellation guides; CGST Act
sections 29, 30 and 45. No government fee figures given (none for cancellation itself)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "gst-registration-cancellation-reg-16-reg-19-gstr-10-revocation-reg-21-certificate-download-2026"

C = contact("your GSTIN, whether you want to cancel or the officer cancelled it, the reason, pending returns, stock on hand and any notices received")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="GST Registration Cancellation (2026): REG-16 Process, REG-19 Order Download, Final Return GSTR-10 and Revocation",
    em="cancelling the GSTIN does not cancel what you owe.",
    kicker="/ Businesses closing or restructuring &middot; GST &middot; Updated 2026-11-25",
    lead=("<strong>A business that closes, transfers its business, falls below the GST threshold or changes its constitution can apply to cancel its GST registration in Form REG-16 on the GST portal; the officer issues the cancellation order in Form REG-19, generally within 30 days, and the GSTIN is suspended in the meantime.</strong> "
          "Within three months of the cancellation date or order (whichever is later) the business must file the final return, GSTR-10, and pay tax on input tax credit for stock held. "
          "There is no government fee to cancel. An officer can also cancel registration, for example for not filing returns, after a show-cause notice; that kind of cancellation can be revoked by applying in Form REG-21 within the time allowed."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>How do I cancel GST registration?</strong> On the GST portal, file Form REG-16 with the reason, the date of closure and details of stock and tax on it; reply to any query, and the officer issues Form REG-19.",
            "<strong>How do I download the GST cancellation certificate?</strong> The cancellation is an order in Form REG-19, not a separate certificate; download it from the notices and orders section of your GST portal login.",
            "<strong>Is there a fee to cancel GST registration?</strong> No government fee. Late fees can apply to returns still pending, including the final return.",
            "<strong>What is GSTR-10?</strong> The final return, due within three months of the cancellation date or the date of the order, whichever is later.",
            "<strong>Can I cancel if returns are pending?</strong> File the pending returns first; the officer can refuse or delay cancellation until they are in.",
            "<strong>Can a cancelled GSTIN be restored?</strong> If the officer cancelled it, apply for revocation in Form REG-21 within the time allowed after filing the overdue returns. A voluntary cancellation that has been approved generally cannot be revoked; apply for a new registration instead.")),
        ("/ Voluntary vs cancellation by the officer", "Two different routes.",
         table(["Step", "Voluntary cancellation", "Cancellation by the officer"], [
             ["Start", "You file REG-16", "Officer issues show-cause notice REG-17"],
             ["Your response", "Answer any query", "Reply in REG-18 within the time given"],
             ["Order", "REG-19 cancellation order", "REG-19 cancellation order (or REG-20 dropping proceedings)"],
             ["Common reasons", "Closure, sale or transfer of business, turnover below threshold, change of constitution", "Returns not filed for a continuous period, business not at the registered place, fraud"],
             ["Final return", "GSTR-10 within three months", "GSTR-10 within three months"],
             ["Undo", "Generally not revocable; register afresh", "Revocation application in REG-21 within the time allowed in section 30 and rule 23"]])
         + '<p>Sources differ on the revocation time limit (30, 90 or up to 180 days with extension); check section 30 and rule 23 and the portal before relying on a date.</p>'),
        ("/ Before and after cancelling", "Avoid surprises.",
         ul("<strong>Stock and capital goods:</strong> pay an amount equal to the input tax credit on stock and capital goods held on the cancellation date (section 29(5)).",
            "<strong>Liabilities continue:</strong> tax, interest and penalties for the period before cancellation can still be demanded; keep records for the full retention period.",
            "<strong>Notices:</strong> respond to anything pending on the portal; see " + L("gst-notice-response-india-asmt-drc-gstr.html", "GST notice response") + ".",
            "<strong>Annual return:</strong> check whether GSTR-9 is due for the year of cancellation; see " + L("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9 and GSTR-9C") + ".",
            "<strong>Closing the company too?</strong> See " + L("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "closing a company in India") + ".")
         + call_box("GST cancellation and revocation", ["Pending returns and late fees",
                                                         "REG-16 filing and officer queries",
                                                         "GSTR-10 final return and stock reversal",
                                                         "Reply to REG-17 show-cause notice",
                                                         "Revocation in REG-21"],
                    "your GSTIN, reason and pending items.")
         + sources("Central Goods and Services Tax Act, 2017, sections 29, 30 and 45; CGST Rules 20 to 23; Tally, Razorpay, Busy, IndiaFilings, CAclubindia and Angel One guides on GST cancellation and revocation. Revocation time limits are reported differently; confirm on the GST portal. Checked 25 November 2026.")),
    ],
    faqs=[("How do I cancel my GST registration online?", "File Form REG-16 on the GST portal with the reason, the date from which cancellation is sought and details of stock and tax payable on it. The officer may raise a query and then issues the cancellation order in Form REG-19, generally within 30 days."),
          ("How do I download the GST cancellation certificate?", "There is no separate certificate: the cancellation order is Form REG-19, which you can download from the notices and orders section after logging in to the GST portal."),
          ("What is GSTR-10 and when is it due?", "GSTR-10 is the final return after cancellation, due within three months of the date of cancellation or the date of the cancellation order, whichever is later. Late fees apply if it is filed late."),
          ("Is there a fee for GST cancellation?", "No government fee is charged to cancel a GST registration, but late fees and interest on any pending returns, including the final return, must be paid."),
          ("Can a cancelled GST registration be revoked?", "Where the officer cancelled it, you can apply for revocation in Form REG-21 within the time allowed under section 30 and rule 23, after filing pending returns and paying dues. An approved voluntary cancellation generally cannot be revoked; you apply for a fresh registration."),
          ("Can BQP handle GST cancellation or revocation?", "Yes. CA Durgesh Chavda can clear pending returns, file REG-16 and GSTR-10, reply to show-cause notices and apply for revocation. " + C)],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice response"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration threshold"),
             ("gst-composition-scheme-turnover-limit-1-5-crore-rates-service-providers-6-percent-rules-2026.html", "GST composition scheme"),
             ("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9 and GSTR-9C"),
             ("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "Closing a company")],
    cta_h="Closing a GSTIN or restoring a cancelled one?", cta_b=C,
    keywords="GST cancellation, GST registration cancellation, GST cancellation certificate download, GST cancellation charges, REG-16, REG-19, GSTR-10 final return, GST revocation REG-21, cancel GST registration online",
    desc="GST registration cancellation (2026): REG-16 voluntary process, REG-19 order (download, not a certificate), no government fee, GSTR-10 within three months, ITC on stock, officer cancellation (REG-17/18) and revocation in REG-21.",
    howto={"name": "How to cancel GST registration", "description": "Voluntary cancellation on the GST portal.", "steps": [
        {"name": "File pending returns", "text": "Clear GSTR-1 and GSTR-3B (or CMP-08) up to date."},
        {"name": "File REG-16", "text": "Reason, cancellation date, stock and tax details."},
        {"name": "Answer queries", "text": "Respond to any officer query in time."},
        {"name": "Download REG-19", "text": "From the notices and orders section."},
        {"name": "File GSTR-10", "text": "Within three months, paying tax on stock credit."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HW complete")
