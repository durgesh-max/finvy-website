# -*- coding: utf-8 -*-
"""Batch HQ (25 Nov 2026): Section 8 company (non-profit company under the Companies Act, 2013) - what it is, objects,
licence, no dividend, name without 'Limited', no minimum capital, process, 12A / 80G, CSR-1 for CSR implementing agencies,
annual compliance (audit, AOC-4, MGT-7, income tax return), comparison with trust and society, foreign founders.
Demand: sweep ac100 (25 Nov 2026), all 7 markets: "section 8 company", "section 8 company financial statements format",
"section 8 company companies act 2013", "section 8 company kya hoti hai".
Facts (checked 25 Nov 2026): IndiaFilings, Sansa Legal, LegalSuvidha, Taxguru Section 8 registration guides (dividends
prohibited and licence revocable on breach; licence applied for through the MCA incorporation filing - sources differ on
whether a separate INC-12 is still filed for new companies, INC-12 used for converting an existing company; CSR-1
registration needs 12A and 80G); Companies Act, 2013 section 8; Companies (Amendment) Act, 2015 removal of minimum paid-up
capital. No fee figures given."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "section-8-company-registration-india-non-profit-licence-12a-80g-csr-1-compliance-2026"

C = contact("the charitable objects, who the founders are (including any foreign founders or funders), the state, and whether you plan to receive CSR or foreign contributions")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Section 8 Company in India (2026): What It Is, Registration, Licence, 12A and 80G, CSR-1 and Annual Compliance",
    em="a non-profit with the structure of a company.",
    kicker="/ NGOs, foundations and CSR teams &middot; Companies Act 2013 &middot; Updated 2026-11-25",
    lead=("<strong>A Section 8 company is a non-profit company under section 8 of the Companies Act, 2013, formed to promote objects such as charity, education, science, art, sports, social welfare, religion or environmental protection.</strong> "
          "It must apply its income only to those objects and cannot pay dividends to members; breaching the conditions can lead to the licence being revoked. "
          "It is incorporated on the MCA portal with a licence under section 8, needs no minimum capital, and can drop &ldquo;Limited&rdquo; from its name. "
          "For tax exemption and donor deductions it registers under sections 12A and 80G, and to take CSR money as an implementing agency it also registers on the MCA CSR-1 form."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>What is a Section 8 company?</strong> (Section 8 company kya hoti hai?) A company formed for charitable or other public-benefit objects that cannot distribute profits to its members.",
            "<strong>Is there a minimum capital?</strong> No. Minimum paid-up capital for companies was removed in 2015.",
            "<strong>How many directors and members?</strong> A private Section 8 company needs at least two directors and two members.",
            "<strong>Can it make a profit?</strong> It can earn a surplus, but must use it for its objects; no dividend can be paid.",
            "<strong>Is it tax-exempt automatically?</strong> No. Exemption needs registration under section 12A, and donors get a deduction only if it also has 80G registration.",
            "<strong>What financial statements does it prepare?</strong> Full financial statements under Schedule III of the Companies Act, audited by a chartered accountant, plus the income and expenditure presentation required for a non-profit.")),
        ("/ Section 8 company vs trust vs society", "Choosing the vehicle.",
         table(["Point", "Section 8 company", "Trust", "Society"], [
             ["Law", "Companies Act, 2013 (central)", "Indian Trusts Act / state public trust laws", "Societies Registration Act / state laws"],
             ["Regulator", "Registrar of Companies (MCA)", "State charity authorities where applicable", "State Registrar of Societies"],
             ["Governance", "Board of directors, company law compliance", "Trustees under the trust deed", "Governing body under bye-laws"],
             ["Credibility with CSR donors and foreign funders", "Usually highest, with public MCA filings", "Varies", "Varies"],
             ["Compliance load", "Highest (audit, AOC-4, MGT-7, board meetings)", "Lower", "Moderate"]])),
        ("/ Registration and compliance", "From licence to annual filings.",
         ul("<strong>Incorporation:</strong> reserve the name, draft the memorandum and articles with non-profit objects, and file the incorporation and section 8 licence application on the MCA portal. A separate Form INC-12 is used to convert an existing company into a Section 8 company.",
            "<strong>Tax registrations:</strong> apply for 12A (income exemption) and 80G (donor deduction) after incorporation; provisional registration is granted first and must later be converted to regular registration.",
            "<strong>CSR:</strong> to receive CSR funds as an implementing agency, register on the MCA CSR-1 form, which needs 12A and 80G; see " + L("best-ca-csr-section-135-companies-act-india-2026.html", "CSR under section 135") + ".",
            "<strong>Annual compliance:</strong> statutory audit, AOC-4 (financial statements) and MGT-7 (annual return) with the Registrar, the income tax return claiming exemption, board and general meetings, and DIR-3 KYC for directors once every three years.",
            "<strong>Foreign money:</strong> foreign contributions need FCRA registration or prior permission before they are received.")
         + call_box("Section 8 company setup and compliance", ["Objects, memorandum and licence application",
                                                               "12A and 80G registration",
                                                               "CSR-1 registration",
                                                               "Audit, AOC-4, MGT-7 and income tax",
                                                               "Foreign founders and funding"],
                    "the objects, founders and funding plans.")
         + sources("Companies Act, 2013, section 8 and Companies (Incorporation) Rules, 2014; Companies (Amendment) Act, 2015 (minimum paid-up capital removed); Companies (CSR Policy) Rules, 2014 (Form CSR-1); income-tax provisions on registration of charitable entities (12A / 80G); Foreign Contribution (Regulation) Act, 2010; IndiaFilings, Sansa Legal, LegalSuvidha and Taxguru Section 8 guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is a Section 8 company?", "A non-profit company registered under section 8 of the Companies Act, 2013 to promote objects such as charity, education, science, art, sports, social welfare or environmental protection. It must apply its income to those objects and cannot pay dividends to its members."),
          ("What is the minimum capital for a Section 8 company?", "There is no minimum paid-up capital requirement. A private Section 8 company needs at least two directors and two members."),
          ("Is a Section 8 company exempt from income tax?", "Only after it registers under section 12A and meets the conditions for charitable exemption. Donors can claim a deduction only if it also holds 80G registration."),
          ("Can a Section 8 company receive CSR funds?", "Yes, as a CSR implementing agency, if it registers on the MCA CSR-1 form, which requires 12A and 80G registration."),
          ("What annual filings does a Section 8 company have?", "Audited financial statements in AOC-4 and the annual return in MGT-7 with the Registrar, the income tax return, board and general meetings, and director KYC. Foreign contributions need FCRA registration or permission."),
          ("Can BQP set up and run compliance for a Section 8 company?", "Yes. CA Durgesh Chavda can handle incorporation, 12A, 80G and CSR-1 registration, audit and annual filings. " + C)],
    related=[("best-ca-csr-section-135-companies-act-india-2026.html", "CSR under section 135"),
             ("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "Partnership firm registration"),
             ("sole-proprietorship-registration-india-documents-gst-udyam-shop-licence-online-2026.html", "Sole proprietorship registration"),
             ("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC"),
             ("startup-registration.html", "Company registration")],
    cta_h="Setting up a non-profit company?", cta_b=C,
    keywords="section 8 company, section 8 company registration, section 8 company companies act 2013, section 8 company kya hoti hai, section 8 company 12A 80G, section 8 company CSR-1, section 8 company financial statements, non-profit company India",
    desc="Section 8 company in India (2026): non-profit company under the Companies Act 2013; no dividend, no minimum capital, licence, registration, 12A and 80G, CSR-1 for CSR funds, audit, AOC-4, MGT-7, FCRA; vs trust and society.",
    howto={"name": "How to register a Section 8 company", "description": "On the MCA portal.", "steps": [
        {"name": "Define the objects", "text": "Charitable or public-benefit objects; no profit distribution."},
        {"name": "Draft MoA and AoA", "text": "With the non-profit clauses required for a section 8 licence."},
        {"name": "File incorporation and licence", "text": "On the MCA portal with directors' and members' documents."},
        {"name": "Register for 12A and 80G", "text": "Provisional first, then regular registration."},
        {"name": "Register CSR-1 if needed", "text": "To act as a CSR implementing agency."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HQ complete")
