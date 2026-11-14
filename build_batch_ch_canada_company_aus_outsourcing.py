# -*- coding: utf-8 -*-
"""Batch CH (14 Nov 2026): demand-led pages (playbook 14):
- Registering a company in Canada from India. CBCA s.105(3): at least 25% of directors resident Canadians, and at least
  one if fewer than four directors (current to 2026); Ontario repealed its residency requirement effective 5 July 2021;
  BC and Alberta have none; Saskatchewan removed it in March 2023; Manitoba and Newfoundland and Labrador still require
  it. Shareholders need not be Canadian. A foreign-controlled corporation is not a CCPC, so the small business rate does
  not apply: federal general rate 15% plus provincial (e.g. Ontario 11.5%, BC 12%). India-Canada DTAA dividends 15%
  (10% holding) / 25%. FEMA ODI on the Indian side.
- Australian accounting and tax practices outsourcing to India. TPB Code of Professional Conduct item 6: no disclosure
  of client information to a third party without client consent unless a legal duty; consent should cover what is
  disclosed, to whom and where, where data is stored, AI use and further outsourcing; item 7 covers outsourced and
  offshore work; responsibility stays with the registered practitioner (TPB Outsourcing and offshoring factsheet,
  December 2025). Privacy Act 1988 APP 8 (cross-border disclosure; the Australian entity remains accountable).
  Australian individual returns: 31 October for self-lodgers; later dates under a registered tax agent's lodgement
  program for clients on the agent's list by 31 October.
Sources: Justice Laws CBCA s.105; Substance Law; Tax and Trade Law (Ontario repeal); Gowling WLG (Alberta); TPB
factsheet and Accountants Daily; OAIC APP 8 guidance (checked 14 Nov 2026)."""
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
    return f'<p><strong>Sources:</strong> {text} <em>{UPDATED}</em> General information, not legal or tax advice for your situation.</p>'


C_CAN = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with who will own the Canadian company, the province you prefer and the business. "
         "We reply the same working day with the FEMA route, the Indian tax position and a fixed-scope quote, and coordinate with your Canadian lawyer and accountant.")
C_AUO = ("Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130 with your practice size, the work you want to outsource (bookkeeping, BAS, individual or company returns, SMSF) and your software. "
         "We reply within one working day with a pilot plan and a fixed-scope quote.")

CAN = dict(
    slug="register-company-in-canada-from-india-resident-director-province-odi-tax-2026",
    title="Registering a Company in Canada From India (2026): Federal or Provincial, Resident Director Rules, Corporate Tax and the FEMA ODI Route",
    em="pick the province before you pick the name.",
    kicker=f"/ Indians going global &middot; Canada &middot; FEMA ODI &middot; Updated {DATE}",
    lead=("An Indian resident or Indian company can own a Canadian corporation, and shareholders do not need to be Canadian, but <strong>director residency depends on where you incorporate</strong>: "
          "a <strong>federal (CBCA)</strong> corporation needs at least 25% resident Canadian directors (at least one if it has fewer than four), while <strong>Ontario, British Columbia and Alberta have no residency requirement</strong> (Ontario repealed it on 5 July 2021). "
          "A Canadian corporation controlled from abroad is not a Canadian-controlled private corporation, so it pays the <strong>general rate: 15% federal plus provincial tax</strong> (for example 11.5% in Ontario or 12% in BC). "
          "On the Indian side it is <strong>overseas direct investment</strong> under FEMA, reported through your bank."),
    sections=[
        ("/ Where to incorporate", "Director residency by jurisdiction.",
         table(["Jurisdiction", "Resident director rule"], [
             ["Federal (CBCA)", "At least 25% of directors resident Canadians; at least one if fewer than four directors"],
             ["Ontario", "No residency requirement since 5 July 2021"],
             ["British Columbia", "No residency requirement"],
             ["Alberta", "No residency requirement"],
             ["Saskatchewan", "Requirement removed in March 2023"],
             ["Manitoba, Newfoundland and Labrador", "Still require resident directors"]])
         + "<p>A federal corporation can use its name across Canada; a provincial one registers extra-provincially to operate in other provinces. Confirm current rules with a Canadian corporate lawyer before filing.</p>"),
        ("/ Tax and the Indian side", "Both countries.",
         table(["Point", "Position"], [
             ["Canadian corporate tax", "General rate: 15% federal plus provincial (e.g. Ontario 11.5%, BC 12%); the small business rate is for Canadian-controlled private corporations only"],
             ["Dividends to India", "India-Canada treaty caps Canadian withholding at 15% for a company holding at least 10%, 25% otherwise; taxable in India with credit"],
             ["FEMA (individual owner)", "ODI within LRS (USD 250,000 per financial year); operating business; no subsidiary where the individual has control; Form ODI, UIN, annual performance report by 31 December"],
             ["FEMA (Indian company owner)", "ODI up to 400% of net worth; two-layer limit"],
             ["Place of effective management", "If the company is run from India, India can treat it as Indian-resident"]])
         + box("Moving to Canada and keeping an Indian company, or the reverse?", "The order of steps (FEMA filings, residence change, Canadian tax registration) decides what is taxed where. Plan it before you move.",
               "Hi Durgesh, I want to set up a company in Canada from India. Can you advise on FEMA and tax?")
         + '<p>Related: <a href="india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html">India-Canada DTAA</a> &middot; <a href="register-company-in-australia-from-india-pty-ltd-odi-resident-director-tax-2026.html">Australian company from India</a> &middot; <a href="set-up-company-in-dubai-uae-from-india-odi-lrs-poem-corporate-tax-2026.html">UAE company from India</a> &middot; <a href="indian-ca-for-clients-in-canada.html">Indian CA for clients in Canada</a>.</p>'
         + src("Canada Business Corporations Act, section 105 (current to 2026); Ontario Business Corporations Act amendment effective 5 July 2021; provincial corporate statutes; Income Tax Act (Canada); India-Canada DTAA; Foreign Exchange Management (Overseas Investment) Rules and Regulations, 2022. Secondary sources checked 14 November 2026: Substance Law, Tax and Trade Law, Gowling WLG.")),
    ],
    faqs=[("Can an Indian resident register a company in Canada?", "Yes. Shareholders need not be Canadian. On the Indian side it is overseas direct investment under FEMA, within the LRS limit of USD 250,000 a year for an individual."),
          ("Does a Canadian company need a Canadian resident director?", "A federal (CBCA) corporation needs at least 25% resident Canadian directors, or one if it has fewer than four. Ontario, British Columbia and Alberta have no residency requirement."),
          ("Which province is best for a foreign-owned company?", "Many foreign owners choose Ontario or British Columbia because neither requires resident directors; the right choice depends on where the business will operate."),
          ("What tax does a foreign-owned Canadian company pay?", "The general corporate rate: 15% federal plus provincial tax, for example 11.5% in Ontario. The small business rate applies only to Canadian-controlled private corporations."),
          ("Can my Indian company set up a Canadian subsidiary?", "Yes, under the ODI route for Indian entities, up to 400% of net worth."),
          ("Can BQP handle the Indian side?", "Yes. " + C_CAN)],
    related=[("india-canada-dtaa-tax-treaty-nri-rates-capital-gains-foreign-tax-credit-2026.html", "India-Canada DTAA"), ("register-company-in-australia-from-india-pty-ltd-odi-resident-director-tax-2026.html", "Australian company from India"),
             ("fema-odi-us-entity-indian-founder.html", "FEMA ODI for Indian founders")],
    cta_h="Starting a Canadian company from India?", cta_b=C_CAN,
    keywords="register company in Canada from India, Canadian corporation Indian owner, Canada resident director requirement CBCA 25%, Ontario no resident director, BC corporation foreign owner, Canada corporate tax foreign owned 15% provincial, Indian company Canadian subsidiary ODI",
    desc="How an Indian resident or company registers a Canadian corporation in 2026: federal CBCA (25% resident directors) vs Ontario, BC and Alberta (no residency requirement), general corporate tax 15% federal plus provincial, treaty dividends, FEMA ODI route and POEM.",
    howto={"name": "How to set up a Canadian company from India", "description": "Steps for Indian residents and companies.", "steps": [
        {"name": "Choose the jurisdiction", "text": "Federal needs 25% resident directors; Ontario, BC and Alberta do not."},
        {"name": "File ODI with your bank", "text": "Submit Form ODI; the bank reports and a UIN is allotted."},
        {"name": "Incorporate and remit", "text": "Incorporate, register for Canadian tax, remit capital under the ODI route and submit share evidence."},
        {"name": "Stay compliant", "text": "Canadian corporate returns, the annual performance report by 31 December and Schedule FA in India."}]})

AUO = dict(
    slug="australian-accounting-firms-outsourcing-to-india-tpb-offshoring-consent-app-8-2026",
    title="Australian Accounting and Tax Practices Outsourcing to India (2026): TPB Offshoring Rules, Client Consent, APP 8 and a Safe Set-Up",
    em="the client consent comes first, the capacity second.",
    kicker=f"/ Outsourcing &middot; Australia &middot; TPB &middot; Privacy &middot; Updated {DATE}",
    lead=("An Australian registered tax or BAS agent can outsource work to India, but under the Tax Practitioners Board's Code of Professional Conduct (item 6) it <strong>must not disclose client information to a third party without the client's consent</strong>. "
          "The TPB expects the consent to say <strong>what information is disclosed, to whom and where, where it is stored, whether AI tools are used, and any further outsourcing</strong>, and the Australian practice <strong>stays responsible</strong> for the work (TPB outsourcing and offshoring factsheet, December 2025). "
          "The Privacy Act's APP 8 also keeps the Australian entity accountable for personal information it discloses overseas."),
    sections=[
        ("/ What the rules require", "TPB and Privacy Act.",
         table(["Requirement", "What to do"], [
             ["Client consent (TPB Code item 6)", "Engagement letter or signed consent naming the offshore provider, the country, the data involved, storage location, AI use and any sub-outsourcing"],
             ["Responsibility (TPB Code item 7)", "Review and sign off all outsourced work; the registered agent remains accountable to the client and the TPB"],
             ["Cross-border disclosure (APP 8)", "Contractual privacy obligations on the provider; the Australian practice remains accountable for breaches"],
             ["Security", "Access through your systems (cloud ledger, practice software), no local copies, named staff, NDAs, audit logs"],
             ["Indian side", "The provider's own obligations under India's DPDP Act and its contracts; check who signs for confidentiality"]])
         + box("Want capacity for BAS, individual and company returns without a compliance headache?", "We work inside your systems with named staff, under your engagement letters, and give you the consent wording and data map your clients and the TPB expect.",
               "Hi Durgesh, we are an Australian accounting practice and want to outsource bookkeeping and tax work to India. Can we discuss a pilot?")),
        ("/ What Australian practices typically outsource", "And how to start.",
         ul("Bookkeeping and reconciliations in Xero, MYOB or QuickBooks; BAS and IAS preparation for review.",
            "Individual and company return preparation for agent review; workpapers and tax reconciliations.",
            "SMSF accounts preparation and audit-ready files; year-end financial statements.",
            "Season planning: individual returns are due by 31 October for self-lodgers, with later dates for clients on a registered agent's list, so work can be spread across the lodgement program.",
            "Start with a 30 to 60 day pilot on a small client set, measured on turnaround and review points, before scaling.")
         + '<p>Related: <a href="outsourced-tax-preparation-accounting-for-us-cpa-firms-india.html">outsourcing for US CPA firms</a> &middot; <a href="outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india.html">outsourcing for UK practices</a> &middot; <a href="india-accounting-bookkeeping-outsourcing-foreign-smb.html">bookkeeping for foreign SMBs</a> &middot; <a href="india-australia-dtaa-tax-treaty-nri-rates-capital-gains-fito-2026.html">India-Australia DTAA</a>.</p>'
         + src("Tax Agent Services Act 2009, Code of Professional Conduct items 6 and 7; Tax Practitioners Board outsourcing and offshoring factsheet (December 2025) and guidance on confidentiality of client information; Privacy Act 1988, APP 8; Digital Personal Data Protection Act, 2023 (India). Secondary sources checked 14 November 2026: Accountants Daily, Public Accountant.")),
    ],
    faqs=[("Can an Australian tax agent outsource work to India?", "Yes, but under TPB Code item 6 client information cannot be disclosed to a third party without the client's consent, and the agent remains responsible for the work."),
          ("What must the client consent cover?", "According to the TPB: what information will be disclosed, to whom and where, where it will be stored, whether AI tools may be used, and any further outsourcing by the provider."),
          ("Does the Privacy Act apply to offshoring?", "Yes. APP 8 governs cross-border disclosure of personal information, and the Australian entity generally remains accountable for how the overseas recipient handles it."),
          ("What work do Australian practices usually outsource?", "Bookkeeping, BAS and IAS preparation, individual and company return preparation for review, workpapers, year-end accounts and SMSF files."),
          ("Can BQP work as an offshore team for an Australian practice?", "Yes. " + C_AUO)],
    related=[("outsourced-tax-preparation-accounting-for-us-cpa-firms-india.html", "Outsourcing for US CPA firms"), ("outsourced-accounting-bookkeeping-for-uk-accountancy-practices-india.html", "Outsourcing for UK practices"),
             ("india-accounting-bookkeeping-outsourcing-foreign-smb.html", "Bookkeeping for foreign SMBs")],
    cta_h="Australian practice looking for capacity?", cta_b=C_AUO,
    keywords="Australian accounting outsourcing companies in India, outsource accounting to India Australia, TPB offshoring rules, tax agent offshore outsourcing client consent, APP 8 cross border disclosure accountants, BAS outsourcing India, SMSF outsourcing India, Xero bookkeeping outsourcing India Australia",
    desc="Australian accounting and tax practices outsourcing to India in 2026: TPB Code item 6 client consent (what, to whom, where, storage, AI, sub-outsourcing), item 7 responsibility, Privacy Act APP 8, security set-up, typical work (bookkeeping, BAS, returns, SMSF) and a pilot plan.",
    howto={"name": "How an Australian practice sets up compliant outsourcing to India", "description": "Steps under TPB and Privacy Act rules.", "steps": [
        {"name": "Update engagement letters", "text": "Obtain client consent naming the provider, country, data, storage, AI use and sub-outsourcing."},
        {"name": "Sign the provider contract", "text": "Confidentiality, privacy obligations under APP 8, security controls and audit rights."},
        {"name": "Set up access", "text": "Work inside your cloud ledger and practice software with named users and no local copies."},
        {"name": "Run a pilot and review", "text": "Start with a small client set, review all work, then scale through the lodgement program."}]})

for p in [CAN, AUO]:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CH complete")
