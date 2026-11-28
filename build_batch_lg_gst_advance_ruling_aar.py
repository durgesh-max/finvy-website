# -*- coding: utf-8 -*-
"""Batch LG (28 Nov 2026): GST advance ruling - who can apply, the questions allowed under section 97(2), Form ARA-01, the 90-day
timeline, when an application is rejected, who is bound, and appeal to the appellate authority.
Demand: 'gst advance ruling', 'how to apply for advance ruling in gst', 'aar gst', 'advance ruling time limit', 'is advance ruling
binding' - only mentioned on three pages; no dedicated page. Businesses with classification or rate doubts need help framing the
question and submissions. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (CGST Act sections 95 to 106; CGST Rules rules 103 to 107A): an applicant (registered, or seeking registration) can ask the
Authority for Advance Ruling (AAR) on questions listed in section 97(2) - classification of goods or services, applicability of a
notification, time and value of supply, admissibility of input tax credit, liability to pay tax, whether registration is needed,
and whether a transaction is a supply; application in Form GST ARA-01; the AAR must pronounce its ruling within 90 days of receiving
the application; it will not admit a question already pending or decided in any proceeding in the applicant's case; the ruling binds
only the applicant and the jurisdictional officer, as long as the law and facts do not change; it is void if obtained by fraud or
suppression; an appeal lies to the Appellate Authority for Advance Ruling (AAAR) within 30 days (extendable by a further 30 days)
in Form GST ARA-02, and the AAAR decides within 90 days. Rulings are state-specific. No fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-advance-ruling-aar-how-to-apply-ara-01-questions-section-97-90-days-binding-appeal-aaar-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with a short description of the transaction, the GST "
     "question you need answered (classification, rate, credit, valuation or registration), the contracts or product details, "
     "and whether any notice or proceeding is already pending on it. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Advance Ruling (2026): Who Can Apply, Questions Allowed Under Section 97(2), Form ARA-01, 90-Day Timeline, Binding Effect and Appeal to the AAAR",
    em="certainty before you charge the rate.",
    kicker="/ Manufacturers, traders, service providers and new businesses &middot; GST advance ruling &middot; Updated 2026-11-28",
    lead=("<strong>A GST advance ruling gives a written answer from the Authority for Advance Ruling on how GST applies to a transaction you are doing or plan to do - classification, rate, input tax credit, valuation, registration or whether something is a supply at all. "
          "The ruling is due within 90 days, binds you and your jurisdictional officer, and can be appealed to the Appellate Authority within 30 days.</strong>"),
    sections=[
        ("/ The process", "Sections 95 to 106 of the CGST Act.",
         table(["Point", "Rule"], [
             ["Who can apply", "A registered person, or a person seeking registration"],
             ["Questions allowed (s.97(2))", "Classification; applicability of a notification; time and value of supply; admissibility of input tax credit; liability to pay tax; need for registration; whether a transaction is a supply"],
             ["Form", "GST ARA-01, with a statement of facts and the applicant&rsquo;s interpretation"],
             ["Not admitted", "If the question is already pending or decided in any proceeding in the applicant&rsquo;s case"],
             ["Timeline", "Ruling within 90 days of receiving the application"],
             ["Binding on", "Only the applicant and the jurisdictional officer, while the law and facts stay the same"],
             ["Appeal", "To the Appellate Authority for Advance Ruling within 30 days (extendable by 30) in Form GST ARA-02; decided within 90 days"]])
         + ul("<strong>State-specific:</strong> the AAR sits in each state, and a ruling binds only the applicant for that registration - rulings for other businesses are persuasive at most.",
              "<strong>Void if obtained by fraud:</strong> a ruling obtained by fraud, suppression or misrepresentation of facts can be declared void.")),
        ("/ When it is worth applying", "And how to frame it.",
         ul("<strong>Good candidates:</strong> new products or services with unclear classification, composite or mixed supplies, rate disputes, credit on large capital spending, and contract structures where the tax position decides the price.",
            "<strong>Apply before a notice:</strong> once a proceeding on the same question starts in your case, the AAR cannot take it up.",
            "<strong>Frame the question narrowly:</strong> one clear question per issue, tied to the actual contract or product, with your own interpretation and supporting law.",
            "<strong>Plan for the outcome:</strong> an unfavourable ruling binds you too - consider the appeal route and how prices and invoices will change.",
            "<strong>Alternatives:</strong> CBIC circulars, earlier rulings and professional opinions may answer simpler questions faster.")
         + call_box("a GST advance ruling", ["Deciding whether a ruling is worth seeking",
                                             "Framing questions under section 97(2)",
                                             "Drafting the ARA-01 statement of facts and interpretation",
                                             "Personal hearing submissions",
                                             "Appeal to the AAAR"],
                    "Transaction details, the question, contracts or product details, any pending proceeding.")
         + sources("CGST Act, 2017 (sections 95 to 106); CGST Rules, 2017 (rules 103 to 107A; Forms GST ARA-01 and ARA-02); site GST notice reply, GST appeal, blocked credits and e-invoicing pages.")),
    ],
    faqs=[("What is an advance ruling under GST?", "A written decision by the Authority for Advance Ruling on how GST applies to a transaction the applicant is doing or proposes to do, on questions such as classification, rate, input tax credit, valuation, registration or whether something is a supply."),
          ("Who can apply for a GST advance ruling?", "Any registered person, or a person seeking registration, by filing Form GST ARA-01 with a statement of facts and their own interpretation of the law."),
          ("How long does a GST advance ruling take?", "The Authority must pronounce its ruling within 90 days of receiving the application. An appeal to the Appellate Authority must be filed within 30 days, extendable by 30 days, and is decided within 90 days."),
          ("Is a GST advance ruling binding?", "It binds only the applicant and the jurisdictional officer, and only while the law and facts remain the same. It is void if obtained by fraud or suppression of facts."),
          ("When can an advance ruling application be rejected?", "When the question is already pending or has been decided in any proceeding in the applicant's case, or when it falls outside the questions listed in section 97(2)."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the transaction details, the GST question, the contracts or product details, and whether any proceeding is pending. Or book a call directly.")],
    related=[("gst-notice-response-india-asmt-drc-gstr.html", "GST notice reply"),
             ("gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026.html", "GST appeal (APL-01)"),
             ("gst-blocked-credits-section-17-5-itc-on-car-food-insurance-construction-csr-gifts-exceptions-2026.html", "GST blocked credits under section 17(5)"),
             ("gst-consultant-online-india-registration-returns-lut-refund-notice-reply-gstr-9-near-me-2026.html", "GST consultant online")],
    cta_h="Unsure of the GST rate or classification?", cta_b=C,
    keywords="gst advance ruling, how to apply for advance ruling in gst, aar gst, advance ruling time limit 90 days, is advance ruling binding, appeal against advance ruling aaar, gst ara-01",
    desc="GST advance ruling: who can apply, questions allowed under section 97(2) (classification, notification, value, ITC, liability, registration, supply), Form ARA-01, ruling within 90 days, binding only on applicant and officer, void if by fraud, appeal to AAAR within 30 days.",
    howto={"name": "How to apply for a GST advance ruling", "description": "From question to ruling.", "steps": [
        {"name": "Check eligibility", "text": "Question within section 97(2) and not pending in any proceeding."},
        {"name": "Frame the question", "text": "Narrow, tied to the actual transaction, with your interpretation."},
        {"name": "File ARA-01", "text": "With statement of facts, documents and submissions; attend the hearing."},
        {"name": "Act on the ruling", "text": "Apply it, or appeal to the AAAR within 30 days."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LG complete")
