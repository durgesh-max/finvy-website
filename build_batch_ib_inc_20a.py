# -*- coding: utf-8 -*-
"""Batch IB (25 Nov 2026): Form INC-20A - declaration for commencement of business under section 10A of the Companies
Act, 2013 (inserted by the Companies (Amendment) Ordinance, 2018 / Act, 2019) read with rule 23A of the Companies
(Incorporation) Rules, 2014: companies with share capital incorporated on or after 2 November 2018 must file within 180
days of incorporation a declaration that every subscriber has paid the value of shares agreed in the memorandum, and must
have filed verification of the registered office (section 12(2)); until then the company cannot commence business or
exercise borrowing powers. Penalty: company Rs 50,000; every officer in default Rs 1,000 per day, up to Rs 1,00,000. If
not filed and the Registrar has reasonable cause to believe no business is being carried on, the name can be removed
under Chapter XVIII (section 248). Form is certified by a practising CA / CS / CMA; filed on the MCA V3 portal.
Demand: sweep ac107 (25 Nov 2026), all 7 markets: "inc 20a", "inc 20a meaning", "inc 20a penalty", "inc 20a
applicability", "inc 20a form purpose".
Facts (checked 25 Nov 2026): MCA INC-20A instruction kit; Taxguru commentary on section 10A and INC-20A; IndiaFilings on a
Rs 2.5 lakh ROC penalty order; Quicko and Cleartax explainers. Filing fee is not stated because sources conflict."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "form-inc-20a-commencement-of-business-180-days-penalty-applicability-india-2026"

C = contact("the company name, date of incorporation, whether share capital has been received in the company's bank account, and whether the registered office verification has been filed")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Form INC-20A (2026): Commencement of Business Declaration, 180-Day Deadline, Penalty and Who Must File",
    em="file it before the company starts trading or borrowing.",
    kicker="/ New private limited companies &middot; Company law &middot; Updated 2026-11-25",
    lead=("<strong>Form INC-20A is the declaration for commencement of business that a company with share capital must file with the Registrar of Companies within 180 days of incorporation, confirming that every subscriber to the memorandum has paid for the shares they agreed to take.</strong> "
          "It comes from section 10A of the Companies Act, 2013, which applies to companies incorporated on or after 2 November 2018. Until the declaration is filed, the company cannot commence business or exercise borrowing powers. "
          "If it is not filed, the company faces a penalty of &#8377;50,000 and each officer in default &#8377;1,000 per day up to &#8377;1,00,000, and the Registrar can start striking off the company if it believes no business is being carried on."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is INC-20A?</strong> A one-time e-form declaring that subscribers have paid the subscription money for their shares, so the company can start business.",
            "<strong>Who must file it?</strong> Every company having share capital incorporated on or after 2 November 2018, including private limited companies and foreign-owned subsidiaries. Companies without share capital are outside section 10A.",
            "<strong>What is the deadline?</strong> Within 180 days of the date of incorporation shown on the certificate of incorporation.",
            "<strong>What is the penalty for not filing?</strong> &#8377;50,000 on the company and &#8377;1,000 per day on each officer in default, up to &#8377;1,00,000 per officer; late filing also attracts additional fees on the MCA portal.",
            "<strong>What is attached?</strong> Proof that subscription money was received, usually the company bank statement, and the form must be certified by a practising chartered accountant, company secretary or cost accountant.",
            "<strong>Is a certificate issued?</strong> No separate certificate is issued; the filed form and its acknowledgement are the record.")),
        ("/ Steps after incorporation", "Where INC-20A fits.",
         table(["Step", "Timing", "Why it matters"], [
             ["Open the company bank account", "Immediately after incorporation", "Subscription money must reach the company account"],
             ["Subscribers pay for their shares", "Before filing INC-20A", "The declaration confirms this payment"],
             ["Registered office verification", "Within 30 days of incorporation where not given at incorporation", "Section 10A also requires it to be on record"],
             ["Appoint the first auditor", "Within 30 days of incorporation", L("form-aoc-5-registered-office-location-filing-india-2026.html", "Other ROC forms") + " and the annual cycle follow"],
             ["File INC-20A", "Within 180 days of incorporation", "Needed before starting business or borrowing"],
             ["Foreign investment reporting", "FC-GPR within 30 days of allotment", L("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist")]])),
        ("/ If the deadline has passed", "Fix it before it compounds.",
         ul("<strong>File late:</strong> the form can still be filed with additional fees; file as soon as the subscription money is in and evidenced.",
            "<strong>Expect adjudication:</strong> Registrars have issued penalty orders for non-filing, so keep the bank evidence and board records ready.",
            "<strong>Avoid strike-off:</strong> an unfiled declaration combined with no business activity can lead to removal of the company&rsquo;s name; respond to any Registrar notice within its deadline.",
            "<strong>Foreign subsidiaries:</strong> match the INC-20A amount with the inward remittance and the FC-GPR filing; see " + L("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "company registration for foreign nationals") + ".",
            "<strong>Annual compliance next:</strong> " + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "subsidiary compliance calendar") + " and " + L("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 filing") + ".")
         + call_box("Post-incorporation filings", ["INC-20A preparation and certification",
                                                    "Subscription money evidence",
                                                    "Late INC-20A and penalty exposure",
                                                    "First auditor and statutory registers",
                                                    "FC-GPR for foreign-owned companies"],
                    "the incorporation date and the share capital position.")
         + sources("Companies Act, 2013, sections 10A, 12 and 248; Companies (Incorporation) Rules, 2014, rule 23A; MCA instruction kit for e-form INC-20A; Taxguru commentary on section 10A; IndiaFilings report on an ROC penalty order for non-filing. Filing fees vary with share capital and delay; check the MCA portal. Checked 25 November 2026.")),
    ],
    faqs=[("What is Form INC-20A?", "The declaration for commencement of business under section 10A of the Companies Act, 2013. A company with share capital files it to confirm that every subscriber has paid the value of the shares they agreed to take, before it starts business or borrows."),
          ("What is the due date for INC-20A?", "Within 180 days of incorporation, for companies with share capital incorporated on or after 2 November 2018."),
          ("What is the penalty for not filing INC-20A?", "Rs 50,000 on the company and Rs 1,000 per day on each officer in default, up to Rs 1,00,000. The Registrar can also start removing the company's name if it believes no business is being carried on."),
          ("Is INC-20A applicable to all companies?", "It applies to companies having share capital incorporated on or after 2 November 2018. Companies without share capital and companies incorporated before that date are outside section 10A."),
          ("Who certifies INC-20A?", "A practising chartered accountant, company secretary or cost accountant, with a director's digital signature, and with proof that the subscription money was received attached."),
          ("Can BQP file INC-20A for my company?", "Yes. CA Durgesh Chavda can prepare and certify INC-20A, check the subscription evidence, and handle late filing and related post-incorporation compliance. " + C)],
    related=[("startup-registration.html", "Startup registration in India"),
             ("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Company registration for foreign nationals"),
             ("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar"),
             ("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 filing")],
    cta_h="Incorporated recently and INC-20A still pending?", cta_b=C,
    keywords="INC-20A, form INC 20A, commencement of business declaration, section 10A Companies Act, INC 20A due date, INC 20A penalty, INC 20A applicability, INC 20A meaning, MCA V3 INC-20A",
    desc="Form INC-20A (2026): declaration for commencement of business under section 10A, due within 180 days of incorporation for companies with share capital; penalty Rs 50,000 plus Rs 1,000/day per officer (max Rs 1 lakh); who files, certification, late filing.",
    howto={"name": "How to file Form INC-20A", "description": "On the MCA V3 portal.", "steps": [
        {"name": "Collect subscription money", "text": "Subscribers pay for their shares into the company bank account."},
        {"name": "Keep the evidence", "text": "Bank statement showing the receipts."},
        {"name": "Check registered office verification", "text": "It must be on record with the Registrar."},
        {"name": "Prepare and certify the form", "text": "Director's DSC and certification by a practising professional."},
        {"name": "File within 180 days", "text": "On the MCA portal; late filing carries additional fees and penalty."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IB complete")
