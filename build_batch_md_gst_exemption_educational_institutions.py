# -*- coding: utf-8 -*-
"""Batch MD (28 Nov 2026): GST exemption for educational institutions - who counts as an 'educational institution', services by
the institution to students, faculty and staff, services to the institution (transport, catering, security and housekeeping,
admission and examination), what stays taxable (coaching, private tuition, most online courses, sale of goods), and ed-tech.
Demand: sweep ac249 (28 Nov 2026), all 7 markets: 'gst exemption for educational institutions', '... notification', '...
notification pdf' (coverage 0.33-0.50) - only a line on the ed-tech page. Schools, colleges, coaching centres and ed-tech companies
need a CA to classify. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Notification 12/2017-Central Tax (Rate), entry 66 and paragraph 2 definition; verified by web search 28 Nov 2026 - GST
Council e-flyer on education services, CBIC flyer, AAAR rulings; no 2025 amendment found): an 'educational institution' provides
pre-school education and education up to higher secondary or equivalent, education as part of a curriculum for a qualification
recognised by law, or education as part of an approved vocational education course; services by an educational institution to its
students, faculty and staff are exempt; services to an educational institution by way of transportation of students, faculty and
staff, catering (including government-sponsored mid-day meals), and security, cleaning or housekeeping are exempt where the
institution provides pre-school to higher secondary education; services relating to admission to or conduct of examinations by such
institutions are exempt; coaching, private tuition, test preparation and most online courses without a recognised qualification are
taxable (18% for most such services - matched to the site ed-tech page); eligibility is decided case by case (a Gujarat AAAR ruling
denied the benefit where the definition was not met). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-exemption-educational-institutions-notification-12-2017-entry-66-schools-coaching-edtech-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the type of institution or business (school, college, "
     "university, coaching, vocational, ed-tech), the courses and whether they lead to a qualification recognised by law, the "
     "services you buy and sell, and any GST notice received. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Exemption for Educational Institutions (2026): Who Qualifies Under Notification 12/2017 Entry 66, Services to Students and to Schools, and What Stays Taxable for Coaching and Ed-Tech",
    em="exempt depends on who you are and what you teach.",
    kicker="/ Schools, colleges, universities, vocational institutes, coaching centres and ed-tech &middot; GST on education &middot; Updated 2026-11-28",
    lead=("<strong>GST exempts services by an &lsquo;educational institution&rsquo; to its students, faculty and staff - but only institutions that provide school education up to higher secondary, education leading to a qualification recognised by law, or approved vocational courses. "
          "Some services bought by schools - transport, catering, security and housekeeping, admission and exam services - are exempt too. "
          "Coaching, private tuition, test preparation and most online courses without a recognised qualification remain taxable.</strong>"),
    sections=[
        ("/ Who qualifies and what is exempt", "Notification 12/2017-Central Tax (Rate), entry 66.",
         table(["Point", "Position"], [
             ["Educational institution", "Provides pre-school to higher secondary education; or education for a qualification recognised by law; or approved vocational education courses"],
             ["Services by the institution to students, faculty, staff", "Exempt"],
             ["Transport, catering, security / cleaning / housekeeping to the institution", "Exempt where the institution provides pre-school to higher secondary education"],
             ["Admission and conduct of examinations", "Exempt for qualifying institutions"],
             ["Coaching, tuition, test prep", "Taxable - not education for a recognised qualification"],
             ["Online courses and ed-tech", "Taxable unless they form part of a curriculum for a recognised qualification"],
             ["Books, uniforms, other goods", "Separate supplies taxed at their own rates"]])
         + ul("<strong>Case by case:</strong> advance ruling authorities have denied the exemption where the body did not meet the definition, so check the curriculum and the recognising law.",
              "<strong>Colleges and universities:</strong> services to students for recognised degrees are exempt, but bought-in services like catering for higher education institutions are generally taxable.")),
        ("/ Practical GST for education businesses", "Registration, credits and notices.",
         ul("<strong>Mixed supplies:</strong> an institution with exempt courses and taxable services (for example short certificate courses or sponsored training) may need registration and must reverse input tax credit on exempt supplies.",
            "<strong>Ed-tech exports:</strong> online courses to foreign learners can be export of services if the conditions are met; foreign platforms selling to Indian learners raise OIDAR questions.",
            "<strong>Hostels and other services:</strong> treatment depends on who provides them and to whom - get the arrangement checked rather than assuming exemption.",
            "<strong>Advance ruling:</strong> where classification is unclear and the amounts are significant, an advance ruling gives certainty.",
            "<strong>Notices:</strong> departments question exemptions claimed by coaching centres and private training providers - keep recognition documents and curriculum records ready.")
         + call_box("GST for education", ["Checking if you are an educational institution for GST",
                                           "Classifying each course and service",
                                           "Registration and credit reversal for mixed supplies",
                                           "Ed-tech, exports and OIDAR",
                                           "Advance rulings and notice replies"],
                    "Institution type, courses and recognition, services bought and sold, any notice.")
         + sources("Notification 12/2017-Central Tax (Rate), entry 66 and paragraph 2 (definition of educational institution); GST Council e-flyer on education services; CBIC flyers and advance ruling authority decisions; site ed-tech, GST advance ruling and blocked credits pages.")),
    ],
    faqs=[("Are educational institutions exempt from GST?", "Services by an educational institution to its students, faculty and staff are exempt, if it meets the GST definition: pre-school to higher secondary education, education for a qualification recognised by law, or approved vocational education courses."),
          ("Is GST applicable on coaching classes and private tuition?", "Yes. Coaching, private tuition and test preparation do not lead to a qualification recognised by law, so they are taxable, usually at 18%, once the provider crosses the registration threshold."),
          ("Which services to schools are exempt from GST?", "Transport of students, faculty and staff, catering including government-sponsored mid-day meals, and security, cleaning or housekeeping performed in the school are exempt for institutions providing pre-school to higher secondary education. Admission and examination services are also exempt for qualifying institutions."),
          ("Is GST charged on online courses and ed-tech?", "Generally yes, unless the course forms part of a curriculum for a qualification recognised by law. Courses to foreign learners may qualify as export of services."),
          ("Which notification gives the GST exemption for education?", "Entry 66 of Notification 12/2017-Central Tax (Rate), read with the definition of educational institution in paragraph 2 of the same notification."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the institution type, courses and recognition, the services you buy and sell, and any GST notice. Or book a call directly.")],
    related=[("best-ca-edtech-india-2026.html", "CA for ed-tech companies"),
             ("gst-advance-ruling-aar-how-to-apply-ara-01-questions-section-97-90-days-binding-appeal-aaar-2026.html", "GST advance ruling"),
             ("gst-for-consultants-professionals-india-registration-threshold-18-percent-export-lut-reimbursement-pure-agent-2026.html", "GST for consultants and professionals"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "Is GST registration mandatory?")],
    cta_h="School, coaching centre or ed-tech working out GST?", cta_b=C,
    keywords="gst exemption for educational institutions, gst exemption for educational institutions notification, notification 12/2017 entry 66, gst on coaching classes, gst on school transport catering, gst on online courses edtech, educational institution definition gst",
    desc="GST exemption for educational institutions: entry 66 of Notification 12/2017 - who qualifies (school to higher secondary, recognised qualifications, approved vocational courses), services to students and to schools (transport, catering, security, exams), and what stays taxable for coaching, tuition and ed-tech.",
    howto={"name": "How to check GST exemption for education", "description": "Who you are, then what you supply.", "steps": [
        {"name": "Test the definition", "text": "School education, recognised qualification or approved vocational course?"},
        {"name": "Classify each supply", "text": "Services to students, services bought in, goods, other courses."},
        {"name": "Register if needed", "text": "Mixed supplies may need registration and credit reversal."},
        {"name": "Get certainty", "text": "Advance ruling where amounts are significant; keep recognition records."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch MD complete")
