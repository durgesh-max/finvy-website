# -*- coding: utf-8 -*-
"""Batch CX (18 Nov 2026): DIN (Director Identification Number) for a foreign national director of an Indian
company. Demand: autocomplete sweep 18 Nov 2026 - "din for foreign national", "documents required for din of foreign
national", "how to apply din for foreign national", "din requirements for foreign nationals" in all 7 markets; no
page on the site.
Facts: DIN is allotted through the SPICe+ incorporation form for proposed directors of a new company, or through Form
DIR-3 for appointment in an existing company; a Class 3 digital signature certificate from an Indian certifying
authority is needed; foreign nationals use the passport as identity proof (PAN not required) plus recent address
proof; foreign documents are commonly notarised and apostilled or consularised (practice varies; confirm with the
certifying professional); nationals of countries sharing a land border with India need Ministry of Home Affairs
security clearance before applying (Companies (Appointment and Qualification of Directors) Amendment Rules, 2022);
DIR-3 KYC once every three years from 31 March 2026; DIN alone does not meet section 149(3) - at least one director
must stay in India 182 days in the financial year. Sources: MCA forms; TaxGuru, Commenda, Incorpx, China Briefing
summaries (checked 18 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 18 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the director's nationality, country of residence and whether the company is new or existing. "
           "We reply within one working day with the document list, attestation route and timeline, with a fixed-scope quote.")
SLUG = "din-for-foreign-national-director-india-documents-apostille-dsc-process-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Most delays come from documents, not forms.</p>'
       f'<p style="margin:0">An address proof that is too old, a name that differs between passport and utility bill, or an apostille on the wrong document can cost weeks. We check the set before it is notarised. '
       f'<a href="{wa("Hi Durgesh, we need a DIN for a foreign director of our Indian company. Can you help?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="DIN for a Foreign National Director in India (2026): Documents, Apostille, Digital Signature and How to Apply",
    em="for directors of Indian subsidiaries and joint ventures.",
    kicker="/ Foreign companies &middot; Directors &middot; MCA &middot; Updated 2026-11-18",
    lead=("A foreign national needs a <strong>Director Identification Number (DIN)</strong> before becoming a director of an Indian company. For a <strong>new company</strong> the DIN is allotted through the <strong>SPICe+ incorporation form</strong>; to join an <strong>existing company</strong> the applicant files <strong>Form DIR-3</strong>. "
          "The applicant needs a <strong>Class 3 digital signature certificate (DSC)</strong> from an Indian certifying authority, their <strong>passport</strong> as identity proof (a PAN is not required for foreign nationals) and a <strong>recent address proof</strong> such as a bank statement or utility bill. Foreign documents are usually <strong>notarised and apostilled</strong>, or consularised where the country is not in the Hague Apostille Convention. "
          "Nationals of countries sharing a land border with India need <strong>Ministry of Home Affairs security clearance</strong> first. Once allotted, the DIN must be kept active by filing <strong>DIR-3 KYC once every three years</strong>."),
    sections=[
        ("/ Which route", "New company or existing company.",
         table(["Situation", "Route", "Notes"], [
             ["Incorporating a new Indian subsidiary or JV", "SPICe+ (incorporation form)", "DIN allotted to proposed directors as part of incorporation"],
             ["Joining an existing Indian company", "Form DIR-3, then DIR-12 by the company", "DIR-3 is signed by the applicant's DSC and certified by a director, company secretary, chartered accountant or cost accountant"],
             ["Already holds a DIN", "No new DIN", "A person can hold only one DIN; keep it active with DIR-3 KYC"]])
         + BOX),
        ("/ Documents", "What a foreign national usually provides.",
         ul("<strong>Passport</strong> (identity proof; mandatory for foreign nationals).",
            "<strong>Address proof</strong>: recent bank statement, utility bill or similar in the applicant's name, generally not older than two to three months; a driving licence or residence card may also be accepted.",
            "<strong>Photograph</strong>, email and mobile number (verified by OTP).",
            "<strong>Attestation</strong>: documents executed abroad are commonly notarised and apostilled (Hague Convention countries such as the US, UK, Canada, Australia and Singapore) or attested by the Indian mission; practice and form wording change, so confirm with the professional certifying the form.",
            "<strong>Translation</strong> into English where documents are in another language.",
            "<strong>MHA security clearance</strong> for nationals of countries sharing a land border with India (for example China), before applying.",
            "Consent to act as director (Form DIR-2) and the non-disqualification declaration (DIR-8) for the company's records.")),
        ("/ After the DIN", "Keep it active and the board compliant.",
         ul("<strong>DIR-3 KYC</strong>: once every three years by 30 June (from 31 March 2026), or when contact details change; a lapsed KYC deactivates the DIN and blocks filings. See <a href=\"dir-3-kyc-deactivated-mca-filings-blocked-urgent-india.html\">DIN deactivated: what to do</a>.",
            "<strong>Resident director</strong>: the board still needs at least one director who stays in India for 182 days or more in the financial year (section 149(3)); see <a href=\"nominee-resident-director-india-foreign-company.html\">resident director for a foreign company</a>.",
            "<strong>Signing</strong>: keep the DSC renewed (usually one or two years) so the director can sign MCA filings remotely.",
            "<strong>Tax</strong>: a non-resident director's sitting fees or remuneration from the Indian company are taxable in India, subject to the tax treaty.")
         + '<p>Related: <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up an Indian subsidiary</a> &middot; <a href="india-market-entry-foreign-company-guide.html">India market entry guide</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">services for foreign companies</a>.</p>'
         + f'<p><strong>Sources:</strong> Companies Act, 2013 (sections 149 and 152-154) and the Companies (Appointment and Qualification of Directors) Rules, 2014 as amended (including the 2022 security-clearance requirement and the 2026 triennial KYC); MCA SPICe+ and DIR-3 forms. Secondary summaries checked 18 November 2026: TaxGuru, Commenda, Incorpx, China Briefing. <em>{UPDATED}</em> Attestation practice varies; confirm the current requirement before notarising.</p>'),
    ],
    faqs=[("Can a foreign national get a DIN in India?", "Yes. A foreign national can obtain a DIN through SPICe+ when incorporating a company, or through Form DIR-3 to join an existing company, using a passport as identity proof and a Class 3 digital signature certificate."),
          ("Does a foreign director need a PAN for DIN?", "No. A PAN is required for Indian nationals; foreign nationals use their passport as identity proof."),
          ("Do the documents need an apostille?", "Documents executed abroad are commonly notarised and apostilled, or consularised where the country is not in the Hague Convention. Practice and form wording change, so confirm with the professional certifying the application."),
          ("Can a Chinese national become a director of an Indian company?", "Yes, but nationals of countries sharing a land border with India need Ministry of Home Affairs security clearance before applying for a DIN."),
          ("Does a foreign director satisfy the resident director rule?", "Not unless they stay in India for 182 days or more in the financial year. Every company needs at least one such director under section 149(3)."),
          ("Can BQP handle the DIN and DSC for our foreign directors?", "Yes. " + CONTACT)],
    related=[("nominee-resident-director-india-foreign-company.html", "Resident director for a foreign company"), ("foreign-company-setup-indian-subsidiary-wos.html", "Setting up an Indian subsidiary"),
             ("dir-3-kyc-deactivated-mca-filings-blocked-urgent-india.html", "DIN deactivated: what to do")],
    cta_h="Appointing a foreign director in India?", cta_b=CONTACT,
    keywords="DIN for foreign national, documents required for DIN of foreign national, how to apply DIN for foreign national, foreign director India DIN, DIR-3 foreign national, DSC for foreign national India, apostille documents DIN, foreign director Indian company 2026",
    desc="DIN for a foreign national director in India (2026): SPICe+ for new companies or DIR-3 for existing ones, Class 3 DSC, passport and recent address proof, apostille or consular attestation, MHA clearance for land-border nationals, triennial DIR-3 KYC and the 182-day resident director rule.",
    howto={"name": "How a foreign national obtains a DIN in India", "description": "Steps for directors of Indian subsidiaries.", "steps": [
        {"name": "Collect documents", "text": "Passport, recent address proof, photo; notarise and apostille (or consularise) where required."},
        {"name": "Get a Class 3 DSC", "text": "Apply to an Indian certifying authority with video verification."},
        {"name": "Choose the route", "text": "SPICe+ for a new company; Form DIR-3 for an existing company."},
        {"name": "File and get the DIN", "text": "File with professional certification; the company files DIR-12 on appointment."},
        {"name": "Stay compliant", "text": "File DIR-3 KYC every three years and keep a resident director on the board."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CX complete")
