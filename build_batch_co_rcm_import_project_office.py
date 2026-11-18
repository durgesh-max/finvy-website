# -*- coding: utf-8 -*-
"""Batch CO (15 Nov 2026): two gaps from the foreign-company autocomplete sweep (all seven markets):
1) GST reverse charge on import of services: IGST Act s.5(3) with Notification 10/2017-Integrated Tax (Rate), entry 1 -
   services supplied by a person in a non-taxable territory to a person in the taxable territory, other than a
   non-taxable online recipient, taxed in the recipient's hands; recipient issues a self-invoice, pays IGST in cash and
   reports in GSTR-3B Table 3.1(d), then claims ITC in Table 4 if eligible; foreign OIDAR suppliers to consumers pay GST
   themselves; time of supply for reverse-charge services is generally the earlier of payment or 60 days from the
   supplier's invoice; import from a related person or own establishment abroad can be a supply even without
   consideration (Schedule I).
2) Project office in India: FEMA Regulations, 2016 on branch, liaison, project offices; general permission through the
   AD bank if the foreign company has a contract from an Indian company and the project is funded by inward remittance,
   by a bilateral/multilateral international financing agency, cleared by the appropriate authority, or the Indian
   company has a term loan from an Indian public financial institution or bank; prior RBI approval for applicants from
   certain countries; CA certificate on Indian liabilities including tax before repatriation; inter-project transfers
   need RBI regional office permission; annual activity certificate filed with the AD bank; a project office is a
   place of business, so the foreign company registers with the ROC; profits taxed as a PE at 35% plus surcharge/cess.
Sources: TaxGuru, Disytax, GSTZen (RCM); RBI master circulars and TaxGuru (project office) - checked 15 Nov 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, body, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">{body} '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')


def src(text):
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not advice for your situation.</p>'


C_RCM = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your list of foreign vendors and what you pay them for. "
         "We reply within one working day with the GST and withholding position and a fixed-scope quote.")
C_PO = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the contract, the Indian client, how the project is funded and its length. "
        "We reply within one working day with the route (project office, branch or subsidiary) and a fixed-scope quote.")

RCM = dict(
    slug="gst-reverse-charge-import-of-services-india-rcm-self-invoice-itc-2026",
    title="GST Reverse Charge on Import of Services in India (2026): When RCM Applies, Self-Invoice, Payment, GSTR-3B Reporting and ITC",
    em="the Indian buyer pays the GST, then claims it back.",
    kicker="/ GST &middot; Import of services &middot; RCM &middot; Updated 2026-11-15",
    lead=("When a business in India buys services from a supplier located outside India (software subscriptions, consulting, design, cloud, legal or marketing services, intra-group charges), <strong>the Indian recipient pays the GST under reverse charge</strong>, not the foreign supplier. "
          "The levy comes from <strong>section 5(3) of the IGST Act</strong> read with <strong>Notification 10/2017-Integrated Tax (Rate)</strong>, which covers services supplied by a person in a non-taxable territory to a person in India other than a non-taxable online recipient. "
          "The recipient issues a <strong>self-invoice</strong>, pays IGST <strong>in cash</strong>, reports it in <strong>GSTR-3B Table 3.1(d)</strong>, and can then claim the same amount as input tax credit if the service is used for business. Consumers buying online services are different: the foreign supplier must register and charge GST itself."),
    sections=[
        ("/ Does RCM apply to you?", "Quick test.",
         table(["Situation", "Who pays GST"], [
             ["Indian GST-registered business buys services from a foreign supplier", "The Indian business, under reverse charge"],
             ["Indian business receives services from its foreign parent or group company, with or without a charge", "The Indian business; services from a related person abroad can be a supply even without consideration"],
             ["Indian consumer (not registered) buys online services (apps, streaming, SaaS) from abroad", "The foreign supplier, through simplified OIDAR registration; see <a href=\"oidar-gst-foreign-saas-ecommerce-india.html\">OIDAR GST</a>"],
             ["Service performed and consumed entirely outside India (place of supply outside India)", "Generally not an import of services; check the place-of-supply rules"]])),
        ("/ What to do each time", "Self-invoice, pay, report, claim.",
         ul("<strong>Self-invoice:</strong> issue an invoice on yourself for the imported service, and a payment voucher when you pay.",
            "<strong>Time of supply:</strong> generally the earlier of the payment date or 60 days from the foreign supplier's invoice; for associated enterprises, also watch the date of entry in your books.",
            "<strong>Pay:</strong> IGST at the applicable rate (often 18%) in cash through the electronic cash ledger; reverse-charge tax cannot be paid using input credit.",
            "<strong>Report:</strong> the liability in GSTR-3B Table 3.1(d) and the eligible credit in Table 4; keep the self-invoice and payment proof.",
            "<strong>Also check withholding:</strong> income tax withholding on the payment to the foreign supplier, the treaty position and Forms 145/146 (formerly 15CA/15CB) are separate from GST.")
         + box("Missed RCM on foreign software and services?", "It is common, and fixable: pay the tax with interest, take the credit where eligible, and align it before the annual return or an audit picks it up.",
               "Hi Durgesh, we pay several foreign vendors and are not sure we have paid GST under reverse charge. Can you review?")
         + '<p>Related: <a href="significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026.html">foreign SaaS and Indian tax</a> &middot; <a href="what-is-form-15cb-and-when-is-it-required-india.html">Form 15CB (now 146)</a> &middot; <a href="gstr-9-gstr-9c-annual-return-india-2026.html">GSTR-9 annual return</a>.</p>'
         + src("IGST Act, 2017, sections 5(3) and 13; Notification No. 10/2017-Integrated Tax (Rate) dated 28 June 2017; CGST Act, 2017, sections 13 (time of supply), 31(3)(f) (self-invoice) and Schedule I; GSTR-3B form. Secondary summaries checked 15 November 2026: TaxGuru, Disytax, GSTZen.")),
    ],
    faqs=[("Is GST applicable on import of services?", "Yes. Services imported by a business in India are taxed under reverse charge: the Indian recipient pays IGST, under section 5(3) of the IGST Act and Notification 10/2017-Integrated Tax (Rate)."),
          ("Is RCM applicable on import of services?", "Yes, when the supplier is located outside India and the recipient is in India (other than a non-taxable online recipient). The recipient pays the tax and can claim credit if eligible."),
          ("Which notification covers reverse charge on import of services?", "Notification No. 10/2017-Integrated Tax (Rate) dated 28 June 2017, entry 1."),
          ("Can reverse-charge GST be paid from input tax credit?", "No. It must be paid in cash through the electronic cash ledger; the amount paid can then be claimed as input tax credit if the service is used for business."),
          ("Where is import of services reported in GSTR-3B?", "The tax liability in Table 3.1(d) (inward supplies liable to reverse charge) and the eligible credit in Table 4."),
          ("Can BQP review our foreign vendor payments?", "Yes. " + C_RCM)],
    related=[("oidar-gst-foreign-saas-ecommerce-india.html", "OIDAR GST for foreign SaaS"), ("what-is-form-15cb-and-when-is-it-required-india.html", "Form 15CB (now Form 146)"),
             ("gstr-9-gstr-9c-annual-return-india-2026.html", "GSTR-9 annual return")],
    cta_h="Paying foreign vendors from India?", cta_b=C_RCM,
    keywords="GST reverse charge on import of services, is RCM applicable on import of services, import of services under GST reverse charge, notification 10/2017 integrated tax rate, is GST applicable on import of services, self invoice import of services, GSTR-3B 3.1(d) import of services",
    desc="GST reverse charge on import of services in India (2026): when RCM applies (IGST s.5(3), Notification 10/2017-IT (Rate)), related-party imports, OIDAR exception, self-invoice, time of supply, cash payment, GSTR-3B Table 3.1(d) and ITC.",
    howto={"name": "How to pay GST on imported services under reverse charge", "description": "Steps for Indian GST-registered businesses.", "steps": [
        {"name": "Identify imported services", "text": "List payments to suppliers located outside India, including group charges."},
        {"name": "Issue a self-invoice", "text": "Raise a self-invoice and payment voucher for each imported service."},
        {"name": "Pay IGST in cash", "text": "Pay at the applicable rate through the electronic cash ledger by the time-of-supply date."},
        {"name": "Report and claim credit", "text": "Report in GSTR-3B Table 3.1(d) and claim eligible credit in Table 4."}]})

PO = dict(
    slug="project-office-india-foreign-company-registration-fema-conditions-tax-2026",
    title="Setting Up a Project Office in India (2026): Who Qualifies, the FEMA Conditions, Registration, Tax and Closing It",
    em="for one contract, not a permanent business.",
    kicker="/ Foreign companies &middot; India entry &middot; FEMA &middot; Updated 2026-11-15",
    lead=("A <strong>project office</strong> lets a foreign company that has <strong>won a contract from an Indian company</strong> execute that project in India without forming a subsidiary. "
          "Under the FEMA regulations on branch, liaison and project offices (2016), it can be opened through the company's <strong>authorised dealer bank without prior RBI approval</strong> if the project is funded by <strong>inward remittance from abroad</strong>, by a <strong>bilateral or multilateral international financing agency</strong>, is <strong>cleared by the appropriate Indian authority</strong>, or the Indian client has a <strong>term loan from an Indian public financial institution or bank</strong>; applicants from certain countries need prior approval. "
          "A project office is a taxable presence: its profits are taxed in India as a permanent establishment at the foreign company rate of 35% plus surcharge and cess."),
    sections=[
        ("/ Project office vs other options", "Pick the right vehicle.",
         table(["Vehicle", "Use it for", "Key limits"], [
             ["Project office", "Executing a specific contract awarded by an Indian company", "Only that project's activities; closes when the project ends"],
             ["Branch office", "Ongoing permitted activities (export/import, consultancy, research)", "RBI/AD bank approval; no manufacturing; 35% tax"],
             ["Liaison office", "Representation and market research only", "No income-earning activity"],
             ["Subsidiary (Pvt Ltd)", "Any business allowed under FDI rules", "22% tax option; Indian company compliance"]])
         + '<p>Comparison in detail: <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">branch vs liaison vs subsidiary</a>.</p>'),
        ("/ Setting it up and running it", "Steps and obligations.",
         ul("Confirm the contract and funding route meet one of the general-permission conditions; otherwise apply for approval.",
            "Submit the application through the authorised dealer bank (Form FNC with the contract and company documents); applicants from countries needing prior approval go to the RBI.",
            "Register the place of business with the Registrar of Companies as a foreign company, and obtain PAN, TAN and GST registration as needed.",
            "Open the project office bank accounts (a foreign currency account can be permitted for the project).",
            "Every year: audited accounts, Indian tax return as a foreign company with a PE, and the annual activity certificate to the bank.",
            "Transfers between projects need permission from the RBI regional office; repatriation of surplus needs a chartered accountant's certificate that Indian liabilities, including tax, are provided for.")
         + box("Won an Indian contract and need to start on site quickly?", "We check whether the general permission applies, prepare the bank application and set up tax, GST and payroll so the project office is compliant from day one.",
               "Hi Durgesh, we have a contract from an Indian company and need a project office in India. Can you help?")),
        ("/ Closing the project office", "When the project ends.",
         ul("Complete the project and settle all Indian liabilities, including tax.",
            "Obtain the chartered accountant's certificate and the auditor's statement of assets and liabilities.",
            "Apply through the bank for closure and repatriation of the surplus, and close the ROC, GST and tax registrations.")
         + '<p>Related: <a href="permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html">permanent establishment in India</a> &middot; <a href="fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules.html">FDI rules in India</a> &middot; <a href="foreign-company-setup-indian-subsidiary-wos.html">setting up a subsidiary</a>.</p>'
         + src("Foreign Exchange Management (Establishment in India of a Branch Office or a Liaison Office or a Project Office or any other Place of Business) Regulations, 2016 and the RBI Master Direction; Companies Act, 2013, Chapter XXII (foreign companies); Income-tax Act, 2025. Secondary summaries checked 15 November 2026: RBI master circulars, TaxGuru.")),
    ],
    faqs=[("What is a project office in India?", "An office a foreign company opens in India to execute a specific contract awarded by an Indian company. It may only carry out activities related to that project and is closed when the project ends."),
          ("Does a project office need RBI approval?", "Not if the foreign company has an Indian contract and the project is funded by inward remittance, an international financing agency, cleared by the appropriate authority, or financed by an Indian public financial institution or bank; it is then opened through the authorised dealer bank. Applicants from certain countries need prior approval."),
          ("How is a project office taxed?", "As a permanent establishment of the foreign company: profits attributable to it are taxed at 35% plus surcharge and cess, with an Indian tax return each year."),
          ("Does a project office need ROC registration?", "Yes. It is a place of business of a foreign company in India and must be registered with the Registrar of Companies."),
          ("Can BQP set up and run the project office?", "Yes. " + C_PO)],
    related=[("branch-office-vs-liaison-vs-wos-india-foreign.html", "Branch vs liaison vs subsidiary"), ("permanent-establishment-india-meaning-types-risk-tax-foreign-company-2026.html", "Permanent establishment in India"),
             ("fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules.html", "FDI rules in India")],
    cta_h="Executing a project in India?", cta_b=C_PO,
    keywords="project office India, project office registration in India, what is a project office, foreign company project office India FEMA, project office setup India, project office tax India 35%, project office closure India, branch office vs project office India",
    desc="Project office in India for foreign companies (2026): who qualifies (Indian contract plus funding condition), general permission through the AD bank vs RBI approval, ROC registration, tax as a PE at 35%, annual activity certificate, inter-project transfers and closure.",
    howto={"name": "How to set up a project office in India", "description": "Steps for a foreign company with an Indian contract.", "steps": [
        {"name": "Check eligibility", "text": "Indian contract plus one of the funding conditions; otherwise seek approval."},
        {"name": "Apply through the AD bank", "text": "Submit Form FNC with the contract and company documents."},
        {"name": "Register and set up", "text": "Register with the ROC as a foreign company; obtain PAN, TAN and GST; open bank accounts."},
        {"name": "Comply and close", "text": "File returns and the annual activity certificate; on completion settle liabilities and repatriate the surplus."}]})

for p in [RCM, PO]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CO complete")
