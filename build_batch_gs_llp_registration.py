# -*- coding: utf-8 -*-
"""Batch GS (24 Nov 2026): LLP registration in India - the process on MCA V3 (DSC for designated partners, name through
RUN-LLP or within FiLLiP, FiLLiP form with DPIN for up to two designated partners, certificate of incorporation, LLP
agreement in Form 3 within 30 days), documents, who can be a partner (NRIs and foreign nationals; FDI in LLPs under the
automatic route where 100% FDI is automatic without performance conditions), resident designated partner, and the
compliance that follows (Form 11, Form 8, ITR, audit thresholds). Call-first page for founders, NRIs and foreign promoters.
Demand: sweep ac84 (24 Nov 2026), 6-7 markets: "llp registration", "llp registration online / documents / procedure /
fees / certificate", "llp registration full form".
Facts (checked 24 Nov 2026): MCA FiLLiP instruction kit; LLP Act 2008 section 7 (at least two designated partners, one
resident in India; resident = 120 days in the financial year after the 2021 amendment); LLP Rules 2009 (Form 3 within 30
days of incorporation); name approval valid three months; guides from Tally, CAclubindia, TaxGuru, ClearTax. Annual filings
and audit thresholds as on site pages (Form 11 by 30 May, Form 8 by 30 October, audit above INR 40 lakh turnover or INR 25
lakh contribution). Government fees depend on contribution and state stamp duty; not quoted."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner"

C = contact("who the partners will be and where they live, the business the LLP will run, the capital contribution, and whether any partner is an NRI, foreign national or foreign company")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="LLP Registration in India (2026): Online Process on MCA, Government Fees, Documents, Designated Partners and NRI or Foreign Partners",
    em="one integrated form, then the LLP agreement within 30 days.",
    kicker="/ Founders, NRIs and foreign promoters &middot; LLP &middot; Updated 2026-11-24",
    lead=("<strong>A limited liability partnership (LLP) is registered online with the Ministry of Corporate Affairs on the MCA V3 portal through a single form, FiLLiP, after each designated partner has a digital signature certificate.</strong> "
          "You need at least two designated partners, one of them resident in India, a registered office in India, and an LLP agreement filed in Form 3 within 30 days of incorporation. "
          "NRIs and foreign nationals can be partners, and foreign investment in an LLP is allowed under the automatic route in sectors where 100% FDI is automatic without performance conditions. "
          "After registration come the yearly filings: Form 11, Form 8 and the income tax return, with an audit once turnover or contribution crosses the limits."),
    sections=[
        ("/ Quick answers", "What people registering an LLP ask.",
         ul("<strong>How do I register an LLP online?</strong> Get DSCs for the designated partners, reserve the name through RUN-LLP or within FiLLiP, file FiLLiP on the MCA V3 portal with the documents, receive the certificate of incorporation with the LLPIN, then file the LLP agreement in Form 3 within 30 days.",
            "<strong>How many partners are needed?</strong> At least two partners, and at least two designated partners who are individuals, with one designated partner resident in India (in India for at least 120 days in the financial year).",
            "<strong>Can an NRI or foreigner be a partner?</strong> Yes. An NRI or foreign national can be a partner or designated partner; the LLP still needs one resident designated partner, and foreign contribution must follow FEMA rules for LLPs.",
            "<strong>How long does it take?</strong> Usually one to three weeks once DSCs and documents are ready, depending on name approval and any resubmission the registrar asks for.",
            "<strong>LLP or private limited company?</strong> An LLP is cheaper to run and has no dividend tax layer, but investors and ESOPs need a company; see " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + ".")),
        ("/ Documents and steps", "What to prepare and file.",
         table(["Step or item", "What it involves"], [
             ["DSC", "Class 3 digital signature for every designated partner"],
             ["Name", "RUN-LLP, or propose the name inside FiLLiP; an approved name is held for three months"],
             ["Partner documents", "PAN (passport for foreign nationals), address proof, photo; foreign documents notarised or apostilled"],
             ["Registered office", "Utility bill not older than two months and the owner's no-objection, or a rent agreement"],
             ["FiLLiP", "Integrated incorporation form; allots DPIN to up to two designated partners without a separate application"],
             ["Subscription sheet and consents", "Partners' consent to act and the subscription details, signed with DSC"],
             ["Certificate of incorporation", "Issued with the LLPIN; PAN and TAN follow"],
             ["Form 3", "LLP agreement filed within 30 days of incorporation, stamped under state law"],
             ["Bank and registrations", "Current account, GST if required, and FEMA reporting for foreign contribution"]])
         + '<p>NRI and foreign promoters: see ' + L("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "business options for NRIs") + ' and ' + L("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "India entry structures for foreign companies") + '.</p>'),
        ("/ After registration", "The compliance an LLP must keep up.",
         ul("<strong>Form 11 (annual return)</strong> by 30 May each year, listing partners and contributions.",
            "<strong>Form 8 (statement of accounts and solvency)</strong> by 30 October; see " + L("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "Form 8 due date and late fee") + ".",
            "<strong>Income tax return</strong>: an LLP is taxed at 30% plus surcharge and cess, and partners&rsquo; share of profit is exempt in their hands; alternate minimum tax can apply.",
            "<strong>Audit</strong> once turnover exceeds INR 40 lakh or contribution exceeds INR 25 lakh, plus a tax audit where income tax limits are crossed.",
            "<strong>Changes</strong> in partners, office or agreement are filed with the registrar within the set time.",
            "<strong>Later conversion</strong> to a company is possible; see " + L("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "converting an LLP to a company") + ".")
         + call_box("LLP registration and compliance", ["Structure choice: LLP, company or branch",
                                                         "FiLLiP filing and the LLP agreement",
                                                         "NRI and foreign partner contribution under FEMA",
                                                         "Form 11, Form 8, ITR and audit",
                                                         "Conversion to a private limited company later"],
                    "the partners, the business and the planned contribution.")
         + sources("Limited Liability Partnership Act, 2008 (section 7 as amended in 2021) and LLP Rules, 2009; MCA FiLLiP instruction kit and MCA V3 portal; Foreign Exchange Management (Non-debt Instruments) Rules, 2019 on investment in LLPs; guides from Tally, CAclubindia, TaxGuru and ClearTax (2026). Government fees depend on contribution and state stamp duty (the MCA filing fee slabs are in the FAQ below). Checked 24 November 2026.")),
    ],
    faqs=[("How do I register an LLP in India online?", "Get a digital signature certificate for each designated partner, reserve the name through RUN-LLP or inside the FiLLiP form, file FiLLiP on the MCA V3 portal with partner and office documents, receive the certificate of incorporation with the LLPIN, and file the LLP agreement in Form 3 within 30 days of incorporation."),
          ("What documents are needed for LLP registration?", "For each partner: PAN (or passport for a foreign national), address proof and a photograph, with foreign documents notarised or apostilled; for the registered office: a recent utility bill and the owner's no-objection or a rent agreement; plus DSCs for the designated partners, their consent and the subscription details."),
        ("What are the government fees for LLP registration?", "MCA fees depend on the total contribution. The FiLLiP incorporation form is generally Rs 500 for contribution up to Rs 1 lakh, Rs 2,000 for Rs 1 lakh to Rs 5 lakh, Rs 4,000 for Rs 5 lakh to Rs 10 lakh and Rs 5,000 above Rs 10 lakh; name reservation through RUN-LLP is Rs 200; the LLP agreement (Form 3) has a separate small fee, and stamp duty on the agreement varies by state. Digital signatures for partners cost extra. Check the current MCA fee schedule when filing."),
        ("What is the full form of LLP?", "Limited Liability Partnership: a separate legal entity registered under the LLP Act, 2008, in which partners have limited liability, at least two designated partners are needed and one must be resident in India."),
          ("How many partners does an LLP need, and must one be resident in India?", "At least two partners and at least two designated partners who are individuals, with at least one designated partner resident in India, meaning in India for at least 120 days in the financial year."),
          ("Can an NRI or foreign national be a partner in an Indian LLP?", "Yes. NRIs and foreign nationals can be partners or designated partners, as long as one designated partner is resident in India. Foreign contribution is allowed under the automatic route in sectors where 100% FDI is automatic without performance conditions, and must be reported under FEMA."),
          ("What compliance does an LLP have after registration?", "Form 11 annual return by 30 May, Form 8 statement of accounts by 30 October, the income tax return, an audit once turnover exceeds INR 40 lakh or contribution exceeds INR 25 lakh, and filings for any change in partners, office or the LLP agreement."),
          ("Can BQP help register an LLP?", "Yes. " + C)],
    related=[("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "LLP Form 8 due date"),
             ("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "Converting an LLP to a company"),
             ("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "Business options for NRIs"),
             ("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "India entry structures")],
    cta_h="Registering an LLP in India?", cta_b=C,
    keywords="LLP registration, LLP registration online, LLP registration documents, LLP registration procedure, LLP registration India, FiLLiP form, designated partner, NRI partner LLP, foreign partner LLP India, LLP agreement Form 3",
    desc="LLP registration in India (2026): DSCs, name through RUN-LLP or FiLLiP, the FiLLiP form on MCA V3 with DPIN, certificate of incorporation, LLP agreement in Form 3 within 30 days; documents; two designated partners with one resident; NRI and foreign partners; Form 11, Form 8, ITR and audit.",
    howto={"name": "How to register an LLP in India", "description": "From DSC to LLP agreement.", "steps": [
        {"name": "Get DSCs", "text": "Class 3 digital signatures for each designated partner."},
        {"name": "Reserve the name", "text": "Through RUN-LLP or inside FiLLiP."},
        {"name": "File FiLLiP", "text": "With partner, office and consent documents on the MCA V3 portal."},
        {"name": "Receive the certificate", "text": "Certificate of incorporation with LLPIN; PAN and TAN follow."},
        {"name": "File the LLP agreement", "text": "Form 3 within 30 days of incorporation."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GS complete")
