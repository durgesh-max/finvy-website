# -*- coding: utf-8 -*-
"""Batch LJ (28 Nov 2026): GST on job work - sending inputs and capital goods to a job worker without tax under section 143,
the one-year and three-year return limits, deemed supply if not returned, challans, direct supply from the job worker's premises,
waste and scrap, input tax credit, and Form ITC-04 (half-yearly or annual).
Demand: 'job work under gst', 'itc-04 due date', 'section 143 gst', 'goods sent for job work not returned', 'job work challan' -
0 pages on the site. Manufacturers using job workers need compliance help and ITC-04 filing. User steer 26 Nov 2026: more call
bookings / WhatsApp enquiries.
Facts (CGST Act sections 19 and 143; CGST Rules rules 45 and 55): a registered principal can send inputs and capital goods to a
job worker without paying tax, under a challan; inputs must be brought back (or supplied from the job worker's place) within one
year, capital goods within three years - moulds, dies, jigs, fixtures and tools are outside these limits; if not returned in time,
the goods are treated as supplied by the principal on the day they were sent, and tax is paid with interest; goods can be supplied
directly from the job worker's premises if the job worker is registered or the principal declares the premises as an additional
place of business (exporters and notified goods aside); waste and scrap can be supplied by the job worker directly if registered,
otherwise by the principal; input tax credit is available to the principal on inputs and capital goods sent directly to the job
worker (section 19); Form ITC-04 - half-yearly (by 25 October and 25 April) for principals with aggregate turnover above INR 5
crore, annually by 25 April for others (from FY 2021-22). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-job-work-section-143-itc-04-due-date-1-year-3-year-return-deemed-supply-challan-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with a list of job workers, the challans issued and goods "
     "received back, any goods outstanding beyond one year (inputs) or three years (capital goods), and your last ITC-04. Or "
     "book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST on Job Work (2026): Section 143, Sending Goods Without Tax, the One-Year and Three-Year Limits, Deemed Supply, Challans and Form ITC-04 Due Dates",
    em="track every challan until the goods come home.",
    kicker="/ Manufacturers, brand owners and job workers &middot; GST job work &middot; Updated 2026-11-28",
    lead=("<strong>A registered manufacturer can send inputs and capital goods to a job worker without paying GST, under a challan, as long as inputs come back within one year and capital goods within three years. "
          "If they do not, the goods are treated as supplied on the day they were sent, and tax is payable with interest. "
          "Movements are reported in Form ITC-04 - half-yearly if turnover exceeds INR 5 crore, annually otherwise.</strong>"),
    sections=[
        ("/ The job work rules", "Section 143 and rule 45.",
         table(["Point", "Rule"], [
             ["Sending goods", "Inputs and capital goods can go to a job worker without tax, under a challan"],
             ["Return limit - inputs", "One year from the date sent"],
             ["Return limit - capital goods", "Three years from the date sent"],
             ["Outside the limits", "Moulds, dies, jigs, fixtures and tools"],
             ["Not returned in time", "Deemed supply by the principal on the day the goods were sent; tax with interest"],
             ["Supply from job worker's place", "Allowed if the job worker is registered, or the premises are declared as the principal's additional place of business"],
             ["Waste and scrap", "Job worker can supply directly if registered; otherwise the principal supplies it"],
             ["Input tax credit", "Principal can take credit on inputs and capital goods sent, including those delivered directly to the job worker"]])
         + ul("<strong>ITC-04 due dates:</strong> principals with aggregate turnover above INR 5 crore file half-yearly - by 25 October (April-September) and 25 April (October-March); others file annually by 25 April.",
              "<strong>Challans:</strong> issue a challan for each movement, both ways, with the details the rules require, and keep it with the goods.")),
        ("/ Staying compliant", "Where principals get caught.",
         ul("<strong>Ageing report:</strong> track every challan by date; flag inputs nearing one year and capital goods nearing three years.",
            "<strong>Deemed supply:</strong> where the limit has passed, pay tax with interest and treat the goods as supplied - it is cheaper to fix early than in an audit.",
            "<strong>Losses at the job worker:</strong> account for process loss, wastage and scrap consistently in challans and ITC-04.",
            "<strong>Job worker side:</strong> the job work service itself is taxable for the job worker if registered; goods received are not the job worker&rsquo;s stock.",
            "<strong>Audits and notices:</strong> ITC-04 and challan records are routinely matched with stock in GST audits.")
         + call_box("GST job work", ["Challan formats and job work process",
                                     "Ageing review against the one- and three-year limits",
                                     "Deemed supply tax and interest",
                                     "ITC-04 preparation and filing",
                                     "Audit and notice support"],
                    "Job workers, challans, outstanding goods, last ITC-04.")
         + sources("CGST Act, 2017 (sections 19 and 143); CGST Rules, 2017 (rules 45 and 55; Form GST ITC-04); CBIC notifications on ITC-04 frequency from FY 2021-22; site GST return filing, GST audit and blocked credits pages.")),
    ],
    faqs=[("What is job work under GST?", "Processing or working on goods belonging to another registered person (the principal). Under section 143, the principal can send inputs and capital goods to the job worker without paying GST, under a challan."),
          ("What is the time limit for goods sent for job work?", "Inputs must be brought back, or supplied from the job worker's place, within one year, and capital goods within three years. Moulds, dies, jigs, fixtures and tools are outside these limits."),
          ("What happens if job work goods are not returned in time?", "They are treated as supplied by the principal on the day they were originally sent, and GST is payable with interest from that date."),
          ("What is the due date for ITC-04?", "Principals with aggregate turnover above INR 5 crore file ITC-04 half-yearly, by 25 October for April-September and by 25 April for October-March. Others file annually by 25 April."),
          ("Can the job worker sell finished goods directly?", "Yes, from the job worker's premises, if the job worker is registered or the principal has declared those premises as an additional place of business."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your job workers, challans issued and received back, goods outstanding beyond the limits and your last ITC-04. Or book a call directly.")],
    related=[("gst-return-filing-2026-due-dates-gstr-1-gstr-3b-qrmp-cmp-08-gstr-9-process-late-fee.html", "GST return filing and due dates"),
             ("gst-audit-by-department-section-65-adt-01-notice-documents-timeline-adt-02-findings-2026.html", "GST audit by the department"),
             ("gst-interest-on-late-payment-section-50-18-percent-net-cash-liability-wrong-itc-rule-88b-2026.html", "GST interest under section 50"),
             ("best-ca-firm-indore-manufacturing-pli.html", "CA for manufacturing businesses")],
    cta_h="Goods lying with job workers?", cta_b=C,
    keywords="job work under gst, itc-04 due date, section 143 gst, goods sent for job work not returned, job work challan gst, job work 1 year 3 years, itc-04 half yearly annual",
    desc="GST job work under section 143: send inputs and capital goods without tax under challan, return inputs within one year and capital goods within three (moulds, dies, jigs, fixtures, tools excluded), deemed supply with interest if not returned, direct supply from job worker, scrap, ITC, and ITC-04 due dates.",
    howto={"name": "How to manage GST job work", "description": "From challan to ITC-04.", "steps": [
        {"name": "Issue challans", "text": "For every movement to and from the job worker."},
        {"name": "Track ageing", "text": "Inputs within one year, capital goods within three years."},
        {"name": "Fix overdue goods", "text": "Pay tax with interest as deemed supply where limits have passed."},
        {"name": "File ITC-04", "text": "Half-yearly above INR 5 crore turnover, annually otherwise."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LJ complete")
