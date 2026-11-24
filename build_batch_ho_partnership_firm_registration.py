# -*- coding: utf-8 -*-
"""Batch HO (25 Nov 2026): partnership firm registration in India - Indian Partnership Act, 1932: registration optional
(section 58 statement to the state Registrar of Firms) but section 69 bars an unregistered firm and its partners from suing
third parties to enforce contracts; documents; process (deed, stamp duty, PAN, Form 1 with the Registrar, certificate);
partner limits; tax (firm rate, section 40(b), TDS on partner payments, ITR-5); NRI partners; when an LLP is better.
Demand: sweep ac100 (25 Nov 2026), all 7 markets: "partnership firm registration online", "partnership firm registration
fees", "partnership firm registration certificate", "partnership firm registration certificate download", plus state
variants (Karnataka, Maharashtra, Telangana, Assam).
Facts (checked 25 Nov 2026): Indian Partnership Act, 1932 (India Code PDF) sections 58 and 69; Indian Kanoon judgments and
Mondaq / Casemine commentary on section 69 (optional registration; bar on suits to enforce contracts; statutory and common
law rights not barred; defect curable by registering before suing); site pages on NRI partners (non-repatriation basis,
barred activities) and section 194T (TDS on partner payments from 1 April 2025)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026"

C = contact("the state where the firm will operate, the number of partners and whether any is an NRI, the business activity, and whether you already have a partnership deed")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Partnership Firm Registration in India (2026): Online Process, Documents, Certificate, Form 1 and Why an Unregistered Firm Cannot Sue",
    em="optional in law, essential in practice.",
    kicker="/ Founders and family businesses &middot; Business registration &middot; Updated 2026-11-25",
    lead=("<strong>A partnership firm is formed by a partnership deed between two or more people; registering it with the state Registrar of Firms is optional under the Indian Partnership Act, 1932, but an unregistered firm and its partners cannot sue third parties to enforce the firm&rsquo;s contracts (section 69).</strong> "
          "Registration is done by filing a statement (usually Form 1) signed by all partners with the Registrar of Firms of the state where the firm does business, with the stamped deed and the prescribed fee; many states now accept it online. "
          "The Registrar then enters the firm in the register and issues a certificate of registration. Fees and stamp duty are set by each state."),
    sections=[
        ("/ Quick answers", "What people search for.",
         ul("<strong>Is registration compulsory?</strong> No, but section 69 bars an unregistered firm from suing to enforce its contracts, and partners from suing the firm or each other on the deed. Most firms register for that reason; banks and government buyers also often ask for it.",
            "<strong>Can I register online?</strong> In many states, yes, through the state Registrar of Firms or a state services portal. Other states still take paper filings.",
            "<strong>How do I download the registration certificate?</strong> Where the state registers online, the certificate is usually available from the same portal after approval; otherwise it is issued by the Registrar&rsquo;s office.",
            "<strong>What are the fees?</strong> Each state sets its own registration fee and stamp duty on the deed; check the state portal before filing.",
            "<strong>How many partners?</strong> At least two. The Companies Act rules cap a partnership at 50 partners.",
            "<strong>Can I register later?</strong> Yes. Registration can be done at any time, and a firm that needs to sue can register before filing the suit.")),
        ("/ Documents and process", "Typical sequence.",
         table(["Step", "What it involves"], [
             ["1. Partnership deed", "Names, capital, profit share, partner salaries and interest, business, place of business; signed by all partners on stamp paper of the value set by the state"],
             ["2. PAN for the firm", "Apply for the firm&rsquo;s PAN using the deed"],
             ["3. Form 1 statement", "Firm name, place of business, other places, partners&rsquo; names and addresses, dates of joining, duration; signed by all partners"],
             ["4. Supporting documents", "Stamped deed, partners&rsquo; ID and address proof, proof of place of business (rent agreement or ownership with NOC), firm PAN"],
             ["5. File with the Registrar", "State Registrar of Firms (online where available) with the prescribed fee"],
             ["6. Certificate", "Registrar records the firm and issues the certificate of registration"],
             ["7. After registration", "Bank account; GST if turnover crosses the threshold; Udyam and shop licence as needed; report changes in partners or address to the Registrar"]])),
        ("/ Tax and alternatives", "What changes after registration.",
         ul("<strong>Income tax:</strong> the firm is taxed as a separate entity and files ITR-5. Partner salaries and interest on capital are deductible within the limits of section 40(b), and from 1 April 2025 the firm deducts TDS on such payments to partners; see " + L("section-194t-tds-partnership-firm-partners-india.html", "TDS on payments to partners") + ".",
            "<strong>GST:</strong> see " + L("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "is GST registration mandatory?") + ".",
            "<strong>NRI partners:</strong> an NRI or OCI can contribute capital on a non-repatriation basis, except in barred activities; see " + L("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "can an NRI start a business in India") + ".",
            "<strong>Limited liability:</strong> partners in a firm have unlimited, joint liability. If that matters, compare " + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + " and " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ".")
         + call_box("Partnership firm registration", ["Partnership deed drafting",
                                                      "Firm PAN and Registrar of Firms filing",
                                                      "GST and Udyam registration",
                                                      "Tax on partner salary and interest",
                                                      "Converting a firm to an LLP or company"],
                    "the state, the partners and the business.")
         + sources("Indian Partnership Act, 1932, sections 56 to 59 and 69 (India Code); Supreme Court and High Court judgments on section 69 (Indian Kanoon) and commentary by Mondaq and Casemine; Companies (Miscellaneous) Rules, 2014 (limit of 50 partners); Income-tax provisions on firms (section 40(b)) and TDS on partner payments. State fees, stamp duty and online procedures vary. Checked 25 November 2026.")),
    ],
    faqs=[("Is partnership firm registration compulsory in India?", "No. Registration with the state Registrar of Firms is optional under the Indian Partnership Act, 1932, but under section 69 an unregistered firm cannot sue third parties to enforce its contracts, and partners cannot sue the firm or each other on the partnership, so most firms register."),
          ("How do I register a partnership firm online?", "Draft and stamp the partnership deed, get the firm's PAN, then file the Form 1 statement signed by all partners with the state Registrar of Firms, online where the state allows it, with the deed, partners' ID and address proof, proof of the place of business and the state fee. The Registrar then issues a certificate of registration."),
          ("What documents are required for partnership firm registration?", "The stamped partnership deed, Form 1 signed by all partners, the firm's PAN, ID and address proof of each partner, and proof of the place of business such as a rent agreement or ownership document with an NOC."),
          ("What is the fee for partnership firm registration?", "Each state sets its own registration fee and stamp duty on the partnership deed, so check the state Registrar of Firms' portal for the current amounts."),
          ("Can an unregistered partnership firm file a case?", "It cannot sue a third party to enforce a contract, but courts have held the bar does not apply to statutory or common law rights. The firm can also register before filing the suit to cure the defect."),
          ("Can BQP register our partnership firm?", "Yes. CA Durgesh Chavda can draft the deed, handle the firm PAN, Registrar filing, GST and tax set-up, or advise whether an LLP suits you better. " + C)],
    related=[("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "Business structures for NRIs"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration"),
             ("section-194t-tds-partnership-firm-partners-india.html", "TDS on payments to partners"),
             ("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("is-gst-registration-mandatory-for-startup-new-small-business-threshold-2026.html", "GST registration threshold")],
    cta_h="Starting a partnership business?", cta_b=C,
    keywords="partnership firm registration, partnership firm registration online, partnership firm registration documents, partnership firm registration certificate, partnership firm registration fees, registrar of firms, Form 1 partnership, unregistered partnership firm section 69",
    desc="Partnership firm registration in India (2026): optional under the Partnership Act 1932, but an unregistered firm cannot sue (section 69); documents, Form 1 with the Registrar of Firms, online filing, certificate, tax, NRI partners.",
    howto={"name": "How to register a partnership firm in India", "description": "With the state Registrar of Firms.", "steps": [
        {"name": "Draft and stamp the deed", "text": "Signed by all partners on stamp paper of the state's value."},
        {"name": "Get the firm's PAN", "text": "Using the partnership deed."},
        {"name": "Prepare Form 1", "text": "Firm and partner details, signed by all partners."},
        {"name": "File with the Registrar of Firms", "text": "Online where available, with documents and the state fee."},
        {"name": "Collect the certificate", "text": "Then open the bank account and complete GST and other registrations."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HO complete")
