# -*- coding: utf-8 -*-
"""Batch JG (25 Nov 2026): LLP vs partnership firm in India (2026) - law (LLP Act, 2008 vs Indian Partnership Act, 1932),
separate legal entity and limited liability vs unlimited joint and several liability, registration (mandatory with MCA
via FiLLiP vs optional with the state Registrar of Firms; an unregistered firm cannot sue to enforce contracts),
partners (minimum 2 designated partners, one resident 120 days, no maximum vs maximum 50 partners under rule 10 of the
Companies (Miscellaneous) Rules, 2014), compliance (Form 11 by 30 May, Form 8 by 30 October, audit above Rs 40 lakh
turnover or Rs 25 lakh contribution vs no ROC filings), tax (same 30% + 12% surcharge above Rs 1 crore + 4% cess,
section 40(b) remuneration and 12% interest for both; AMT under 115JC for both; 44AD for firms, not LLPs; 194T TDS on
payments to partners), foreign investment (LLP: automatic route where 100% FDI is automatic without performance
conditions; firm: NRIs / OCIs on non-repatriation basis, other foreign investment generally needs approval), conversion
of a registered firm into an LLP (Form 17, all partners consent, no security interest outstanding). Short note on
'LLP vs LLC' (US LLC formed under US state law) linking to US LLC pages. No fee figures.
Demand: sweep ac117 (25 Nov 2026): "llp vs partnership" (7 markets), "llp vs partnership firm" (5), "llp vs llc" (7),
"llp vs company" (5), "llp vs proprietorship" (4).
Facts (checked 25 Nov 2026): site LLP registration, LLP annual filing, partnership firm registration / tax, NRI business
structure pages; Mondaq (structure FAQ), Razorpay Rize (firm-to-LLP conversion conditions), Mondaq (FDI in LLPs)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "llp-vs-partnership-firm-india-2026-liability-tax-compliance-registration-fdi-conversion"

C = contact("the business you plan to run, the number of partners and where they live, expected turnover, whether foreign or NRI money is involved, and whether you already have a firm to convert")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="LLP vs Partnership Firm in India (2026): Liability, Tax, Compliance, Registration, Foreign Partners and Converting a Firm to an LLP",
    em="same tax rate, very different risk.",
    kicker="/ Founders, professionals and family businesses &middot; Business structure &middot; Updated 2026-11-25",
    lead=("<strong>An LLP and a partnership firm pay income tax at the same rate (30% plus surcharge and cess), but an LLP is a separate legal entity whose partners' liability is limited to their agreed contribution, while partners in a firm are personally liable without limit for all of its debts.</strong> "
          "The trade-off is compliance: an LLP must register with the Ministry of Corporate Affairs and file Form 11 and Form 8 every year, while a firm has no annual ROC filings. "
          "An LLP can also take foreign investment under the automatic route in many sectors; a firm generally cannot."),
    sections=[
        ("/ LLP vs partnership firm at a glance", "The differences that decide the choice.",
         table(["Point", "LLP", "Partnership firm"], [
             ["Law", "Limited Liability Partnership Act, 2008", "Indian Partnership Act, 1932"],
             ["Legal status", "Separate legal entity with perpetual succession", "Not separate from its partners"],
             ["Liability", "Limited to each partner's contribution (except fraud)", "Unlimited, joint and several"],
             ["Registration", "Mandatory, with the MCA (FiLLiP)", "Optional, with the state Registrar of Firms; an unregistered firm cannot sue to enforce its contracts"],
             ["Partners", "At least 2 designated partners, one resident in India (120 days in the year); no maximum", "At least 2; maximum 50"],
             ["Annual filings", "Form 11 by 30 May, Form 8 by 30 October, plus ITR-5", "ITR-5 only; no ROC filings"],
             ["Audit", "Accounts audit above &#8377;40 lakh turnover or &#8377;25 lakh contribution; tax audit where limits apply", "Tax audit only where income-tax limits apply"],
             ["Income tax", "30% + surcharge 12% above &#8377;1 crore + 4% cess; no presumptive scheme", "30% + surcharge 12% above &#8377;1 crore + 4% cess; can use section 44AD"],
             ["Foreign investment", "Automatic route where 100% FDI is automatic without performance conditions", "NRIs / OCIs on a non-repatriation basis; other foreign investment generally needs approval"],
             ["Transfer and exit", "Change partners by filing with the MCA; the LLP continues", "Firm may dissolve when partners change, unless the deed provides otherwise"]])
         + '<p>Registering either: ' + L("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration") + ' and ' + L("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "partnership firm registration") + '.</p>'),
        ("/ Tax: what is the same and what is not", "Both are taxed as firms.",
         ul("<strong>Same rate:</strong> 30% on total income, surcharge of 12% above &#8377;1 crore and 4% cess; partners' share of profit is exempt in their hands.",
            "<strong>Remuneration and interest:</strong> both can deduct working-partner remuneration within the section 40(b) limits and interest on capital up to 12%, taxable in the partners' hands; see " + L("partnership-firm-tax-rate-india-2026-30-percent-40b-remuneration-audit-limit-itr-5-due-date.html", "partnership firm tax rate and 40(b)") + ".",
            "<strong>TDS on payments to partners:</strong> 10% under section 194T above &#8377;20,000 a year, for firms and LLPs alike; see " + L("section-194t-tds-partnership-firm-partners-india.html", "section 194T") + ".",
            "<strong>Alternate minimum tax:</strong> both can be liable to AMT at 18.5% when they claim certain deductions (" + L("section-115jc-amt-18-5-percent-individual-llp-india.html", "section 115JC") + ").",
            "<strong>The main tax difference:</strong> the presumptive scheme under section 44AD is open to firms but not LLPs.")),
        ("/ Which should you choose?", "A practical view.",
         ul("<strong>Choose an LLP</strong> when outside creditors, contracts or employees create real liability risk, when partners may change, when you want foreign or NRI partners with repatriable investment, or when you want a structure you can later convert into a company.",
            "<strong>A firm can still suit</strong> small family or professional businesses with trusted partners, low liability risk and a preference for minimal paperwork.",
            "<strong>Raising equity?</strong> Investors usually want a private limited company; compare " + L("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited") + " and " + L("convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026.html", "converting an LLP into a company") + ".",
            "<strong>NRIs and foreign founders:</strong> see " + L("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "which structure an NRI can use") + ".",
            "<strong>LLP vs LLC:</strong> an LLC is a US entity formed under US state law, not an Indian structure; Indian founders who own one have separate US and Indian tax filings; see " + L("us-llc-indian-member-k1-pass-through-tax-ca.html", "US LLC with an Indian member") + " and " + L("delaware-c-corp-vs-llc.html", "C-Corp vs LLC") + ".")),
        ("/ Converting a partnership firm into an LLP", "How existing firms move over.",
         ul("<strong>Who can convert:</strong> a registered firm where all partners agree and become partners of the LLP, and no security interest on the firm's assets is outstanding.",
            "<strong>Process:</strong> reserve the name, incorporate the LLP with the conversion application (Form 17) and its statement of partners' consent, then inform the Registrar of Firms.",
            "<strong>Effect:</strong> the firm's assets, liabilities, contracts and proceedings vest in the LLP, which continues the business; check GST, bank, licence and tax registrations for updating.",
            "<strong>Afterwards:</strong> follow the " + L("llp-annual-filing-form-11-form-8-due-date-fees-late-fee-first-year-status-2026.html", "LLP annual filing calendar") + ".")
         + call_box("Choosing or converting a structure", ["LLP vs firm vs company for your business",
                                                            "LLP or firm registration",
                                                            "Firm-to-LLP conversion",
                                                            "Partnership deed or LLP agreement review",
                                                            "Tax, 40(b) and 194T planning for partners"],
                    "your partners, turnover and plans.")
         + sources("Limited Liability Partnership Act, 2008 (sections 7, 55 and Second Schedule) and LLP Rules; Indian Partnership Act, 1932 (section 69); Companies Act, 2013 (section 464) and Companies (Miscellaneous) Rules, 2014 (rule 10); Income-tax Act (firm tax rate, section 40(b), 44AD, 115JC, 194T); FEMA (Non-Debt Instruments) Rules, 2019 and Consolidated FDI Policy; Mondaq and Razorpay Rize commentary; site LLP, partnership firm and NRI structure guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the difference between an LLP and a partnership firm?", "An LLP is a separate legal entity under the LLP Act, 2008 with partners' liability limited to their contribution and mandatory MCA registration and annual filings; a partnership firm under the Partnership Act, 1932 is not separate from its partners, who have unlimited liability, and has no ROC filings."),
          ("Which is better, LLP or partnership firm?", "An LLP is usually better where there is liability risk, changing partners or foreign or NRI investment; a firm can suit small businesses with trusted partners that want minimal compliance."),
          ("Is the tax rate the same for an LLP and a partnership firm?", "Yes. Both pay 30% plus surcharge of 12% above Rs 1 crore and 4% cess, and both can deduct partner remuneration under section 40(b) and interest up to 12%. The main difference is that only firms can use the presumptive scheme under section 44AD."),
          ("How many partners can an LLP or a firm have?", "A firm can have at most 50 partners. An LLP has no maximum but needs at least two designated partners, one of whom is resident in India."),
          ("Can a partnership firm be converted into an LLP?", "Yes. A registered firm can convert by filing Form 17 with the incorporation documents, provided all partners consent and become LLP partners and no security interest on its assets is outstanding."),
          ("Can NRIs or foreigners be partners?", "Foreign investment in an LLP is allowed under the automatic route in sectors with 100% automatic FDI and no performance conditions. In a firm, NRIs and OCIs can invest on a non-repatriation basis; other foreign investment generally needs approval."),
          ("What is the difference between an LLP and an LLC?", "An LLP is an Indian entity under the LLP Act, 2008; an LLC is a US entity formed under US state law. Indians who own a US LLC deal with US filings and report it in India."),
          ("Can BQP help us choose or convert?", "Yes. CA Durgesh Chavda advises on LLP vs firm vs company, registers LLPs and firms, converts firms into LLPs and handles partners' tax planning. " + C)],
    related=[("which-is-better-llp-vs-private-limited-india.html", "LLP vs private limited"),
             ("llp-registration-india-2026-process-documents-fillip-designated-partner-nri-foreign-partner.html", "LLP registration"),
             ("partnership-firm-registration-india-online-documents-certificate-form-1-registrar-of-firms-2026.html", "Partnership firm registration"),
             ("partnership-firm-tax-rate-india-2026-30-percent-40b-remuneration-audit-limit-itr-5-due-date.html", "Partnership firm tax rate"),
             ("can-nri-start-business-in-india-sole-proprietorship-partnership-opc-llp-company-2026.html", "Business structures for NRIs")],
    cta_h="LLP or partnership firm?", cta_b=C,
    keywords="llp vs partnership, llp vs partnership firm, difference between llp and partnership firm, llp or partnership which is better, llp vs llc, convert partnership firm to llp, llp tax rate vs partnership",
    desc="LLP vs partnership firm in India 2026: limited vs unlimited liability, mandatory vs optional registration, Form 11 / Form 8 vs no ROC filings, same 30% tax, foreign partners, 50-partner limit and converting a firm to an LLP (Form 17).",
    howto={"name": "How to choose between an LLP and a partnership firm", "description": "For founders and partners.", "steps": [
        {"name": "Assess liability risk", "text": "Creditors, contracts, employees and lenders."},
        {"name": "Check who the partners are", "text": "Number, residence and whether foreign money is involved."},
        {"name": "Compare compliance", "text": "LLP: Form 11, Form 8 and audit limits; firm: ITR-5 only."},
        {"name": "Compare tax", "text": "Same rate; 44AD only for firms."},
        {"name": "Register or convert", "text": "FiLLiP for an LLP, Form 17 to convert a firm."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JG complete")
