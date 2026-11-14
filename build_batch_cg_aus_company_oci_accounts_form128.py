# -*- coding: utf-8 -*-
"""Batch CG (14 Nov 2026): demand-led pages from the seven-market autocomplete list (playbook 14):
- Australian company from India: Pty Ltd needs at least one director ordinarily resident in Australia (Corporations
  Act 2001, s.201A); company tax 25% for base rate entities (aggregated turnover under A$50 million including connected
  entities and affiliates, passive income 80% or less), otherwise 30%; FEMA ODI (individual within LRS USD 250,000
  per financial year, operating company, Schedule III conditions; Indian company up to 400% of net worth); Form ODI,
  UIN, APR by 31 December; India-Australia DTAA dividends 15%.
- OCI and NRI bank accounts: NRIs and OCI cardholders resident outside India can open NRE, NRO and FCNR(B) accounts
  (FEMA (Deposit) Regulations, 2016); NRE/FCNR interest exempt in India for non-residents and fully repatriable; NRO
  interest taxable (TDS 30% plus surcharge and cess, treaty rate with TRC), repatriation up to USD 1 million per
  financial year; on becoming resident, accounts must be redesignated.
- Nil or lower TDS certificate: Form 128 (formerly Form 13) under section 395(1) of the Income-tax Act, 2025 (formerly
  section 197), rule 213 of the Income-tax Rules, 2026; filed on TRACES; certificate verified and downloaded by the
  deductor on TRACES; a section 197 certificate issued for 2026-27 receipts remains usable.
Sources: CBDT Form 128 FAQ; ClearTax, Busy; RBI 'Accounts in India by non-residents'; bank FAQs; Deloitte Australia
highlights 2026; accounts-os (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."
DATE = "2026-11-14"


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


C_AUS = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with who will own the Australian company, the business and expected turnover. "
         "We reply the same working day with the FEMA route, the Indian tax position and a fixed-scope quote, and coordinate with your Australian accountant.")
C_ACC = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your residence status, passport and OCI details and what the money is for. "
         "We reply the same working day.")
C_128 = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the payment type, the payer, the expected amount for the year and your estimated tax. "
         "We reply the same working day and can file Form 128 for you.")

AUS = dict(
    slug="register-company-in-australia-from-india-pty-ltd-odi-resident-director-tax-2026",
    title="Registering a Company in Australia From India (2026): Pty Ltd, Resident Director, 25% or 30% Company Tax and the FEMA ODI Route",
    em="one Australian-resident director, and FEMA first.",
    kicker=f"/ Indians going global &middot; Australia &middot; FEMA ODI &middot; Updated {DATE}",
    lead=("An Indian resident or Indian company can own an Australian <strong>Pty Ltd</strong>, but the company needs <strong>at least one director who ordinarily lives in Australia</strong> (Corporations Act 2001, section 201A). "
          "Australian company tax is <strong>25% for a base rate entity</strong> (aggregated turnover under A$50 million, counting connected and affiliated entities, and passive income no more than 80%) and <strong>30% otherwise</strong>, so a subsidiary of a larger Indian group often pays 30%. "
          "On the Indian side it is <strong>overseas direct investment (ODI)</strong>: an individual within the LRS limit of USD 250,000 a financial year, an Indian company up to 400% of net worth, reported through the bank with an annual performance report by 31 December."),
    sections=[
        ("/ Australian side", "What the company needs.",
         table(["Requirement", "Detail"], [
             ["Entity", "Proprietary limited company (Pty Ltd), registered with ASIC; a foreign company can instead register a branch"],
             ["Directors", "At least one director ordinarily resident in Australia (section 201A)"],
             ["Company tax", "25% for base rate entities (aggregated turnover under A$50 million, passive income 80% or less); 30% for others"],
             ["Dividends to India", "Franked dividends carry no Australian withholding; unfranked dividends are capped at 15% under the India-Australia treaty"]])),
        ("/ Indian side (FEMA)", "ODI rules for the owner.",
         table(["Investor", "Route and limits"], [
             ["Resident individual", "ODI within LRS (USD 250,000 per financial year); operating business only; no financial services; no subsidiary of the Australian company where the individual has control"],
             ["Indian company or LLP", "ODI up to 400% of net worth; two-layer limit on step-down subsidiaries"],
             ["Reporting", "Form ODI through the bank before or at the time of remittance (UIN allotted), share evidence within the prescribed time, annual performance report by 31 December, Schedule FA in the Indian return"]])
         + box("Already set up the Australian company without the bank's ODI filing?", "Late reporting can usually be regularised with a late submission fee, or through compounding at the RBI Regional Office for your UIN.",
               "Hi Durgesh, I own an Australian company from India. Can you check my FEMA ODI compliance?")),
        ("/ Tax planning points", "Avoid surprises in both countries.",
         ul("<strong>Place of effective management:</strong> if the company is in substance run from India, India can treat it as Indian-resident and tax its global profit.",
            "<strong>Transfer pricing:</strong> charges between the Indian parent and the Australian company must be at arm's length in both countries.",
            "<strong>Dividends received in India:</strong> taxable in India, with credit for Australian withholding under the treaty.",
            "<strong>Moving to Australia yourself:</strong> once you become non-resident in India, the ODI rules for resident individuals stop applying to new investments.")
         + '<p>Related: <a href="set-up-company-in-dubai-uae-from-india-odi-lrs-poem-corporate-tax-2026.html">UAE company from India</a> &middot; <a href="india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html">India-Australia DTAA</a> &middot; <a href="form-odi-apr-annual-performance-report-india-2026.html">ODI annual performance report</a> &middot; <a href="fema-compounding-odi-rbi-regional-office-uin-circular-28-october-2026.html">FEMA compounding for ODI</a>.</p>'
         + src("Corporations Act 2001 (Cth), section 201A; Treasury Laws Amendment (Enterprise Tax Plan Base Rate Entities) Act 2018 and ATO base rate entity rules; India-Australia DTAA; Foreign Exchange Management (Overseas Investment) Rules and Regulations, 2022; Liberalised Remittance Scheme. Secondary summaries checked 14 November 2026: Deloitte Australia tax highlights 2026, accounts-os.")),
    ],
    faqs=[("Can an Indian resident register a company in Australia?", "Yes. It is overseas direct investment under FEMA (within the LRS limit of USD 250,000 a year for an individual), and the Pty Ltd needs at least one director ordinarily resident in Australia."),
          ("Does an Australian company need a resident director?", "Yes. Section 201A of the Corporations Act 2001 requires a proprietary company to have at least one director who ordinarily resides in Australia."),
          ("What is the company tax rate in Australia?", "25% for base rate entities (aggregated turnover under A$50 million and passive income no more than 80%), 30% for other companies. Turnover of connected entities and affiliates counts towards the A$50 million."),
          ("Can my Indian company set up an Australian subsidiary?", "Yes, under the ODI route for Indian entities, with total financial commitment up to 400% of net worth."),
          ("What yearly filings does the Indian owner have?", "The ODI annual performance report by 31 December, the Australian company in Schedule FA, and Australian company tax returns."),
          ("Can BQP handle the Indian side?", "Yes. " + C_AUS)],
    related=[("set-up-company-in-dubai-uae-from-india-odi-lrs-poem-corporate-tax-2026.html", "UAE company from India"), ("india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html", "India-Australia DTAA"),
             ("fema-odi-us-entity-indian-founder.html", "FEMA ODI for Indian founders")],
    cta_h="Starting an Australian company from India?", cta_b=C_AUS,
    keywords="register company in Australia from India, Australian Pty Ltd Indian owner, Australia resident director requirement 201A, Australia company tax 25% 30% base rate entity, Indian company Australian subsidiary ODI, FEMA ODI Australia, Indian founder Australia company",
    desc="How an Indian resident or company registers an Australian company in 2026: Pty Ltd with one Australian-resident director (s.201A), company tax 25% (base rate entity) or 30%, FEMA ODI route (LRS USD 250,000; 400% of net worth), Form ODI, APR by 31 December, POEM and treaty points.",
    howto={"name": "How to set up an Australian company from India", "description": "Steps for Indian residents and companies.", "steps": [
        {"name": "Arrange a resident director", "text": "Appoint at least one director ordinarily resident in Australia."},
        {"name": "File ODI with your bank", "text": "Submit Form ODI; the bank reports and a UIN is allotted."},
        {"name": "Register with ASIC and remit capital", "text": "Incorporate the Pty Ltd, remit the investment under the ODI route and submit share evidence."},
        {"name": "Keep both sides compliant", "text": "Australian tax returns, annual performance report by 31 December and Schedule FA in India."}]})

ACC = dict(
    slug="can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026",
    title="Can an OCI Cardholder Have an NRI Account? NRE, NRO and FCNR Accounts for NRIs and OCIs (2026): Tax, Repatriation and What Changes When You Return",
    em="yes, while you live outside India.",
    kicker=f"/ NRI &middot; OCI &middot; Banking &middot; FEMA &middot; Updated {DATE}",
    lead=("<strong>Yes.</strong> An OCI cardholder living outside India can open the same accounts as an NRI: <strong>NRE, NRO and FCNR(B)</strong> (FEMA (Deposit) Regulations, 2016). "
          "<strong>NRE and FCNR interest is tax-free in India</strong> for non-residents and the money is fully repatriable; <strong>NRO interest is taxable</strong>, with the bank deducting 30% plus surcharge and cess unless you give treaty documents, and repatriation from NRO is capped at <strong>USD 1 million per financial year</strong>. "
          "If you move back to India and become resident, the bank must redesignate the accounts as resident accounts."),
    sections=[
        ("/ Which account for what", "NRE vs NRO vs FCNR.",
         table(["", "NRE", "NRO", "FCNR(B)"], [
             ["What goes in", "Money earned abroad, in rupees", "Indian income (rent, dividends, pension, sale proceeds) and foreign money", "Money earned abroad, kept in foreign currency"],
             ["Who can open", "NRIs and OCIs resident outside India", "NRIs and OCIs resident outside India", "NRIs and OCIs resident outside India (term deposits)"],
             ["Interest taxed in India?", "No, while you are non-resident", "Yes; TDS 30% plus surcharge and cess, or treaty rate with TRC and Form 41", "No, while you are non-resident"],
             ["Repatriation", "Fully repatriable", "Current income repatriable after tax; capital up to USD 1 million per financial year", "Fully repatriable"],
             ["Currency risk", "Rupee", "Rupee", "None (held in foreign currency)"]])
         + box("NRO interest losing 30% to TDS?", "If you live in a treaty country, a tax residency certificate and Form 41 bring the deduction down to the treaty rate, often 10% or 15%.",
               "Hi Durgesh, I am an OCI/NRI and my bank deducts 30% TDS on NRO interest. Can you help me reduce it?")),
        ("/ Points to watch", "Common mistakes.",
         ul("Indian income such as rent must be credited to the NRO account, not NRE.",
            "Interest that is tax-free in India is usually still taxable in your country of residence (for example, the US, UK, Canada and Australia tax worldwide income).",
            "Your tax residence and FEMA residence are tested separately; spending long periods in India can change both.",
            "On return to India, NRE and NRO accounts are redesignated as resident accounts; FCNR deposits can run to maturity, and you may be RNOR for a few years.",
            "US persons also report Indian accounts on FBAR and FATCA forms.")
         + '<p>Related: <a href="nre-nro-fcnr-account-tax-rules.html">NRE, NRO and FCNR tax rules</a> &middot; <a href="nri-nre-nro-conversion-returning-india-2026.html">converting accounts when returning</a> &middot; <a href="oci-cardholder-tax-india-complete-2026.html">OCI tax guide</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating up to USD 1 million</a>.</p>'
         + src("Foreign Exchange Management (Deposit) Regulations, 2016; RBI note 'Accounts in India by non-residents'; Income-tax Act, 2025 (exemption for NRE and FCNR interest for non-residents, TDS on NRO interest); bank FAQs checked 14 November 2026.")),
    ],
    faqs=[("Can an OCI cardholder open an NRE or NRO account?", "Yes. OCI cardholders resident outside India can open NRE, NRO and FCNR(B) accounts, like NRIs."),
          ("Is NRE interest taxable in India?", "No, while the account holder is non-resident. It may still be taxable in the country where you live."),
          ("How much TDS is deducted on NRO interest?", "30% plus surcharge and cess by default; the treaty rate applies if you give the bank a tax residency certificate, Form 41 and PAN."),
          ("How much can I send abroad from an NRO account?", "Current income such as rent and dividends after tax, plus up to USD 1 million per financial year of other balances, with the CA certificate and bank forms."),
          ("What happens to NRE and NRO accounts when I move back to India?", "They must be redesignated as resident accounts once you become resident; FCNR deposits can continue to maturity."),
          ("Can BQP help with NRI banking and tax?", "Yes. " + C_ACC)],
    related=[("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"), ("oci-cardholder-tax-india-complete-2026.html", "OCI tax guide"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "Repatriate money from India")],
    cta_h="OCI or NRI with money in India?", cta_b=C_ACC,
    keywords="can OCI have NRI account, OCI NRE account, OCI NRO account, NRE vs NRO vs FCNR, NRE account interest tax, NRO account TDS 30%, NRO repatriation USD 1 million, OCI bank account India",
    desc="Can an OCI cardholder have an NRI account? Yes: NRE, NRO and FCNR(B) for OCIs and NRIs resident abroad (FEMA Deposit Regulations, 2016). Interest tax, TDS on NRO, repatriation limits and what changes on return to India (2026).",
    howto={"name": "How an OCI or NRI chooses and uses Indian bank accounts", "description": "Steps for non-residents.", "steps": [
        {"name": "Open NRE for foreign earnings", "text": "Use NRE or FCNR for money earned abroad; interest is tax-free in India while non-resident."},
        {"name": "Open NRO for Indian income", "text": "Credit rent, dividends and sale proceeds to NRO."},
        {"name": "Cut the TDS", "text": "Give the bank a TRC, Form 41 and PAN to get the treaty rate on NRO interest."},
        {"name": "Redesignate on return", "text": "Inform the bank when you become resident so the accounts are converted."}]})

F128 = dict(
    slug="nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026",
    title="How to Get a Nil or Lower TDS Certificate in 2026: Form 128 (Formerly Form 13) Under Section 395, Who Should Apply and How",
    em="stop over-deduction before it happens.",
    kicker=f"/ TDS &middot; Income-tax Act 2025 &middot; NRIs and businesses &middot; Updated {DATE}",
    lead=("To have tax deducted at a lower rate or not at all, apply in <strong>Form 128</strong> (formerly Form 13) on the <strong>TRACES</strong> portal under <strong>section 395(1) of the Income-tax Act, 2025</strong> (formerly section 197). "
          "The tax officer issues a certificate stating the rate and the payer it applies to; the payer verifies it on TRACES and deducts at that rate. "
          "It is most useful when the TDS would far exceed your actual tax: <strong>NRIs selling property or receiving rent</strong>, contractors and professionals with low margins, and businesses with losses. A certificate issued under the old section 197 for 2026-27 receipts remains valid."),
    sections=[
        ("/ Who benefits most", "Typical cases.",
         table(["You are", "Why it helps"], [
             ["NRI selling property", "Without a certificate the buyer deducts up to about 14.95% of the full sale price, not of the gain; a certificate based on the actual gain reduces it; see the <a href=\"nri-property-tds-ldc-calculator.html\">NRI property TDS calculator</a>"],
             ["NRI landlord", "Tenants deduct about 31.2% on gross rent; see <a href=\"nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html\">NRI rental income</a>"],
             ["Contractor or professional with thin margins", "TDS on gross receipts can exceed tax on net profit"],
             ["Company or firm with losses or exempt income", "Avoids refunds locked up for months"],
             ["Non-resident receiving fees or royalties", "Certificate can align TDS with treaty or actual income"]])
         + box("Waiting a year for TDS refunds?", "A certificate before the payments start keeps the cash with you. We prepare the projections and documents the officer asks for.",
               "Hi Durgesh, I want a lower or nil TDS certificate (Form 128). Can you file it for me?")),
        ("/ How to apply", "On TRACES.",
         ul("Log in to TRACES as a taxpayer (PAN) and choose the Form 128 request.",
            "Enter the payers (deductors) and their TANs, the type of payment, and the estimated amounts for the year.",
            "Attach the projections: estimated income and tax for the year, and the last few years' returns; NRIs selling property attach the sale agreement and purchase cost.",
            "Verify and submit; respond to any query from the tax officer.",
            "The certificate is issued with the rate, period, payer and amount limit; the payer verifies it on TRACES and you can download it under Lower/Nil Deduction Certificates.")
         + '<p>Related: <a href="nri-india-property-ldc-lower-deduction-certificate.html">NRI property lower deduction certificate</a> &middot; <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old vs new form numbers</a>.</p>'
         + src("Income-tax Act, 2025, section 395(1) (formerly section 197 of the 1961 Act); Income-tax Rules, 2026, rule 213 and Form 128; CBDT FAQs on Form 128. Secondary summaries checked 14 November 2026: ClearTax, Busy.")),
    ],
    faqs=[("What is Form 128?", "The application for a certificate for lower or nil deduction (or lower collection) of tax under section 395 of the Income-tax Act, 2025. It replaced Form 13 from 1 April 2026."),
          ("Where do I file Form 128?", "Online on the TRACES portal. The certificate is issued there, and the payer verifies it on TRACES."),
          ("Is a certificate issued under section 197 still valid?", "Yes, if it was issued for projected receipts for 2026-27, it remains usable for payments on or after 1 April 2026."),
          ("Can an NRI get a nil TDS certificate when selling property?", "If the gain is nil or very low, the certificate can be at a nil or low rate; the officer decides based on the sale and purchase documents."),
          ("Can BQP file it?", "Yes. " + C_128)],
    related=[("nri-india-property-ldc-lower-deduction-certificate.html", "NRI property lower deduction certificate"), ("nri-property-tds-ldc-calculator.html", "NRI property TDS calculator"),
             ("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "NRI rental income")],
    cta_h="TDS far above your actual tax?", cta_b=C_128,
    keywords="how to get nil TDS certificate, lower TDS certificate, Form 128 income tax, Form 13 now Form 128, section 395 lower deduction certificate, section 197 lower TDS, TRACES lower deduction certificate, NRI lower TDS certificate",
    desc="How to get a nil or lower TDS certificate in 2026: Form 128 (formerly Form 13) on TRACES under section 395(1) of the Income-tax Act, 2025 (formerly section 197), rule 213; who benefits (NRI property sellers and landlords, contractors, loss-making businesses) and the steps.",
    howto={"name": "How to apply for a nil or lower TDS certificate", "description": "Steps on TRACES using Form 128.", "steps": [
        {"name": "Prepare projections", "text": "Estimate the year's receipts, income and tax; gather past returns and transaction documents."},
        {"name": "File Form 128 on TRACES", "text": "Enter the payers, TANs, payment types and amounts, and submit."},
        {"name": "Answer queries", "text": "Respond to the tax officer's questions."},
        {"name": "Share the certificate", "text": "Give the payer the certificate; they verify it on TRACES and deduct at the certified rate."}]})

for p in [AUS, ACC, F128]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CG complete")
