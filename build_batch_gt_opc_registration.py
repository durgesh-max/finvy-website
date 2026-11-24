# -*- coding: utf-8 -*-
"""Batch GT (24 Nov 2026): One Person Company (OPC) registration in India - who can form one (one Indian citizen, resident
or not, since 1 April 2021), nominee, director and the resident director rule, the SPICe+ process on MCA V3 (DSC, name,
SPICe+ Part B with e-MOA and e-AOA, AGILE-PRO-S, nominee consent in INC-3), documents, no capital or turnover caps and
conversion at any time, and the compliance that follows (board meetings, audit, AOC-4, MGT-7A, ITR). Call-first page.
Demand: sweep ac84 (24 Nov 2026), 7 markets: "opc registration", "opc registration online / documents / requirements /
fees mca".
Facts (checked 24 Nov 2026): Companies (Incorporation) Second Amendment Rules, 2021 (PIB 1 Feb 2021; Mondaq, S.S. Rana,
Vinod Kothari, SCC Online): NRIs allowed, residency for OPC reduced to 120 days, paid-up capital (INR 50 lakh) and turnover
(INR 2 crore) caps removed, conversion at any time. Companies Act 2013: section 2(62), section 96 (no AGM for OPC),
section 149(3) (one director resident 182 days in the financial year), section 173(5) (one board meeting in each half of
the calendar year), section 137 (AOC-4 within 180 days of year end for OPC). Fees not quoted."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "opc-registration-india-2026-one-person-company-process-documents-nri-nominee-compliance"

C = contact("who will own the OPC and where they live, who the nominee and director will be, the business it will run, and whether you plan to bring in co-founders or investors later")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="OPC Registration in India (2026): One Person Company Process, Documents, Nominee, NRI Owners and Compliance",
    em="one owner, limited liability, and a company you can grow.",
    kicker="/ Solo founders and NRIs &middot; OPC &middot; Updated 2026-11-24",
    lead=("<strong>A One Person Company (OPC) is a private company with a single shareholder, registered online with the Ministry of Corporate Affairs through the SPICe+ form on the MCA V3 portal.</strong> "
          "Since 1 April 2021 any Indian citizen, whether resident in India or not, can form one; you must name an Indian-citizen nominee who takes over if you die or become incapable, and appoint at least one director. "
          "The old caps of INR 50 lakh paid-up capital and INR 2 crore turnover were removed, so an OPC can grow and convert into a private or public company at any time. "
          "It needs a statutory audit and yearly filings, but no annual general meeting."),
    sections=[
        ("/ Quick answers", "What solo founders ask.",
         ul("<strong>Who can form an OPC?</strong> One natural person who is an Indian citizen, resident in India or not. A person can be a member of only one OPC, and foreign nationals cannot form one.",
            "<strong>Can an NRI register an OPC?</strong> Yes, since 2021. But every company needs at least one director who stays in India for 182 days in the financial year, so an NRI owner usually appoints a resident director as well.",
            "<strong>What is the nominee?</strong> An Indian citizen named in the memorandum who becomes the member if the owner dies or cannot act; the nominee gives written consent in Form INC-3 and can be changed later.",
            "<strong>Is there a minimum capital?</strong> No minimum capital, and since 2021 no upper limit on capital or turnover that forces conversion.",
            "<strong>OPC, LLP or private limited?</strong> An OPC suits one owner; for two or more founders or outside investors, a private limited company or LLP fits better. See " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ".")),
        ("/ Process and documents", "How an OPC is registered.",
         table(["Step or item", "What it involves"], [
             ["DSC", "Digital signature for the proposed director and member"],
             ["Name", "Reserve through SPICe+ Part A or RUN; the name ends with (OPC) Private Limited"],
             ["SPICe+ Part B", "Incorporation form with e-MOA (INC-33) and e-AOA (INC-34); allots DIN, PAN and TAN"],
             ["Nominee consent", "Form INC-3 with the nominee's PAN or passport and address proof"],
             ["AGILE-PRO-S", "Linked form for GST (if needed), EPFO, ESIC, professional tax and the bank account"],
             ["Owner and director documents", "PAN or passport, address proof, photograph; documents from abroad notarised or apostilled"],
             ["Registered office", "Recent utility bill and the owner's no-objection, or a rent agreement"],
             ["Certificate of incorporation", "Issued with the CIN, PAN and TAN"]])
         + '<p>NRIs comparing structures: see ' + L("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "can an NRI start a business in India") + ' and ' + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + '.</p>'),
        ("/ After registration", "What an OPC must keep up.",
         ul("<strong>Board meetings:</strong> at least one in each half of the calendar year, with a gap of at least 90 days; an OPC with only one director is exempt and records its decisions in the minutes book instead.",
            "<strong>No AGM:</strong> an OPC is exempt from holding an annual general meeting.",
            "<strong>Audit:</strong> a statutory audit by a chartered accountant every year, whatever the turnover.",
            "<strong>Filings:</strong> financial statements in Form AOC-4 within 180 days of the year end, the annual return in Form MGT-7A, and the director KYC.",
            "<strong>Tax:</strong> the OPC files a company income tax return and is taxed as a company, about 25% under the concessional regime; the owner pays tax on salary or dividends taken out.",
            "<strong>Growing:</strong> convert into a private limited company when you add shareholders; see " + L("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "founder salary vs dividend") + ".")
         + call_box("OPC registration and compliance", ["OPC vs LLP vs private limited for your plans",
                                                         "SPICe+ filing, nominee and resident director",
                                                         "NRI owners: FEMA, bank accounts and tax",
                                                         "Audit, AOC-4, MGT-7A and ITR",
                                                         "Conversion when co-founders or investors join"],
                    "who will own and run the OPC and what it will do.")
         + sources("Companies Act, 2013 (sections 2(62), 96, 137, 149(3) and 173(5)); Companies (Incorporation) Rules, 2014 as amended by the Companies (Incorporation) Second Amendment Rules, 2021 (MCA press release of 1 February 2021); MCA V3 SPICe+ forms; commentary from Mondaq, S.S. Rana, Vinod Kothari and SCC Online. Government fees and stamp duty vary by state and capital and are not quoted here. Checked 24 November 2026.")),
    ],
    faqs=[("How do I register a One Person Company in India?", "Get a DSC, reserve the name through SPICe+ Part A or RUN, file SPICe+ Part B on the MCA V3 portal with the e-MOA, e-AOA, nominee consent in Form INC-3 and the AGILE-PRO-S form, and receive the certificate of incorporation with CIN, PAN and TAN."),
          ("What documents are needed for OPC registration?", "PAN (or passport for documents from abroad), address proof and a photograph of the member, director and nominee, the nominee's consent in Form INC-3, proof of the registered office with the owner's no-objection or a rent agreement, and DSCs for those signing."),
          ("Can an NRI register an OPC in India?", "Yes. Since 1 April 2021 any Indian citizen, resident or not, can form an OPC. The company still needs at least one director who stays in India for 182 days in the financial year, so an NRI owner usually appoints a resident director."),
          ("Is there a capital or turnover limit for an OPC?", "No. The INR 50 lakh paid-up capital and INR 2 crore turnover caps were removed in 2021, there is no minimum capital, and an OPC can convert into a private or public company at any time."),
          ("What are the annual compliances of an OPC?", "At least one board meeting in each half of the calendar year (unless the OPC has only one director), a statutory audit, financial statements in Form AOC-4 within 180 days of the year end, the annual return in Form MGT-7A, director KYC and the company income tax return. No annual general meeting is needed."),
          ("Can BQP help register and run an OPC?", "Yes. " + C)],
    related=[("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "Can an NRI start a business in India"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration"),
             ("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("pvt-ltd-vs-llp.html", "Private limited vs LLP"),
             ("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "Founder salary vs dividend")],
    cta_h="Starting a One Person Company?", cta_b=C,
    keywords="OPC registration, OPC registration online, OPC registration documents, OPC registration requirements, one person company registration India, NRI OPC, OPC nominee, OPC compliance, SPICe+ OPC",
    desc="OPC registration in India (2026): one Indian citizen (resident or NRI) with a nominee and at least one director; SPICe+ on MCA V3 with e-MOA, e-AOA, INC-3 and AGILE-PRO-S; documents; no capital or turnover caps since 2021; resident director rule; audit, AOC-4, MGT-7A and ITR.",
    howto={"name": "How to register a One Person Company in India", "description": "From DSC to certificate of incorporation.", "steps": [
        {"name": "Get a DSC", "text": "For the proposed director and member."},
        {"name": "Reserve the name", "text": "Through SPICe+ Part A or RUN."},
        {"name": "File SPICe+ Part B", "text": "With e-MOA, e-AOA, nominee consent in INC-3 and AGILE-PRO-S."},
        {"name": "Receive the certificate", "text": "Certificate of incorporation with CIN, PAN and TAN."},
        {"name": "Open the bank account and start compliance", "text": "Board meetings, audit, AOC-4, MGT-7A and ITR."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GT complete")
