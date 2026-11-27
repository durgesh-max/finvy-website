# -*- coding: utf-8 -*-
"""Batch KH (27 Nov 2026): FEMA consultant service page - what a FEMA consultant (CA) handles for Indian companies with
foreign investment, Indian founders with overseas entities, NRIs and foreign companies, and how to engage one from any city.
Demand: sweep ac163 (27 Nov 2026), all 7 markets: "fema consultants in delhi ncr / mumbai / bangalore / pune / hyderabad /
chennai / delhi", "fema consultant near me", "fema consultants"; the site had FEMA topic pages and a compounding page but no
general FEMA consultant service page.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - FEMA reporting, late filings and compounding need a CA.
Facts (site pages and earlier verified rounds): FC-GPR within 30 days of allotment; FC-TRS within 60 days of transfer or
receipt / remittance of consideration; FLA return by 15 July; ODI: Form FC with UIN, APR by 31 December; late filings
regularised with the late submission fee (LSF) where available; contraventions compounded under the FEMA (Compounding
Proceedings) Rules, 2024; NRI repatriation from NRO up to USD 1 million per financial year with Form 146 (old 15CB) /
Form 145 (old 15CA); LRS USD 250,000 per financial year. No fees, no office claims (city names describe search demand only;
the work is done online), no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "fema-consultant-india-fdi-odi-nri-rbi-filings-compounding-mumbai-delhi-bangalore-pune-hyderabad-chennai-2026"

C = contact("a short note of the transaction (who invested or remitted, when and how much), the company's CIN or your PAN, copies of any FIRC / KYC, share allotment or transfer documents, and any RBI or bank email about a pending or late filing")
PAGES = [dict(
    slug=SLUG,
    title="FEMA Consultant in India (2026): FDI, ODI, NRI and RBI Filings, Late Filings and Compounding - Online for Mumbai, Delhi NCR, Bangalore, Pune, Hyderabad and Chennai",
    em="file on time, or fix it before RBI asks.",
    kicker="/ Indian companies with foreign investors, founders with overseas entities, NRIs and foreign companies &middot; FEMA reporting, late filings and compounding &middot; Updated 2026-11-27",
    lead=("<strong>A FEMA consultant makes sure money and shares that cross India's border are reported to RBI correctly and on time - and fixes it when they were not.</strong> "
          "That covers foreign investment into an Indian company (FDI), Indian money going into an overseas entity (ODI), NRI accounts and repatriation, and foreign companies setting up in India. "
          "The work is document-based and done online, so it does not depend on which city you or the company are in."),
    sections=[
        ("/ What a FEMA consultant handles", "The filings and the fixes.",
         table(["Situation", "What is filed or done"], [
             ["Foreign or NRI investor subscribes to shares", "Pricing / valuation, KYC through the bank, Form FC-GPR within 30 days of allotment"],
             ["Shares transferred between a resident and a non-resident", "Pricing check, Form FC-TRS within 60 days, tax on the sale"],
             ["Company with foreign investment, every year", "FLA return by 15 July; downstream investment reporting where relevant"],
             ["Indian founder or company invests abroad (ODI)", "Form FC through the bank, UIN, Annual Performance Report by 31 December, disinvestment reporting"],
             ["NRI sending money out of India", "Repatriation from NRO up to USD 1 million a financial year, Form 146 CA certificate (old 15CB) and Form 145 (old 15CA)"],
             ["Foreign company setting up in India", "Subsidiary, LLP, branch or liaison office route, RBI / AD bank approvals and annual filings"],
             ["A filing was missed or is late", "Late submission fee where available, or compounding under the FEMA (Compounding Proceedings) Rules, 2024"]])
         + ul("<strong>Why it matters:</strong> late or wrong FEMA reporting blocks later filings, delays share allotments and fund-raising, and can lead to compounding or penalty proceedings.",
              "<strong>Banks first:</strong> most FEMA filings go through the company's authorised dealer (AD) bank, which checks the documents before RBI sees them.",
              "<strong>Tax runs alongside:</strong> share pricing, TDS on payments abroad and DTAA claims are usually decided together with the FEMA filing.")),
        ("/ How to engage one from any city", "Mumbai, Delhi NCR, Bangalore, Pune, Hyderabad, Chennai or abroad.",
         ul("<strong>Online by design:</strong> FEMA work is done on documents - board resolutions, valuation reports, bank KYC, FIRCs and RBI portal filings - so a call and shared documents are enough.",
            "<strong>Start with a review:</strong> list every foreign inflow, outflow and share transfer since incorporation, check what was filed and when, and spot gaps before the next round or audit.",
            "<strong>Then fix in order:</strong> current filings first, then late filings with the late submission fee, then compounding for anything the fee does not cover.",
            "<strong>Keep a calendar:</strong> FC-GPR 30 days, FC-TRS 60 days, FLA 15 July and APR 31 December are the dates most often missed.")
         + call_box("FEMA consultant", ["FDI reporting: FC-GPR, FC-TRS, downstream investment",
                                        "ODI: Form FC, UIN, APR, disinvestment",
                                        "FLA return and annual FEMA health check",
                                        "NRI repatriation and Form 146 (old 15CB)",
                                        "Late filings and compounding applications"],
                    "Transaction note, CIN or PAN, allotment / transfer documents and bank emails.")
         + sources("Foreign Exchange Management Act, 1999; FEMA (Non-debt Instruments) Rules, 2019; FEMA (Overseas Investment) Rules and Regulations, 2022; FEMA (Compounding Proceedings) Rules, 2024; RBI Master Directions on Foreign Investment, Overseas Investment and Compounding; site FC-GPR, FC-TRS, FLA, ODI, late submission fee and compounding guides. Checked 27 November 2026.")),
    ],
    faqs=[("What does a FEMA consultant do?", "They make sure foreign investment into India, Indian investment abroad, NRI remittances and foreign companies' Indian operations are reported to RBI correctly and on time, through the authorised dealer bank. That includes FC-GPR and FC-TRS for share issues and transfers, the FLA return, ODI forms and the Annual Performance Report, repatriation certificates, and fixing late or missed filings through the late submission fee or compounding."),
          ("I am searching for a FEMA consultant in Mumbai, Delhi NCR, Bangalore, Pune, Hyderabad or Chennai. Does location matter?", "Not for the work itself. FEMA filings are prepared from documents and filed online through the bank and the RBI portal, so a call and shared documents are enough wherever you or the company are based, in India or abroad."),
          ("Which FEMA filings are most often missed?", "FC-GPR within 30 days of allotting shares to a foreign or NRI investor, FC-TRS within 60 days of a resident / non-resident share transfer, the FLA return by 15 July every year for a company with foreign investment, and the ODI Annual Performance Report by 31 December. Missing them blocks later filings and can lead to a late submission fee or compounding."),
          ("What happens if a FEMA filing was not done on time?", "Many reporting delays can be regularised by filing late with the late submission fee. Contraventions the fee does not cover are compounded: an application under the FEMA (Compounding Proceedings) Rules, 2024 with the facts, the delay and the documents, after which RBI decides the compounding amount. Acting before RBI or the bank raises it is usually simpler."),
          ("Do I need a FEMA consultant for NRI money transfers?", "For sending money out of an NRO account, the bank usually needs a CA certificate in Form 146 (old 15CB) and Form 145 (old 15CA), within the USD 1 million a financial year limit for NRO repatriation. A CA also checks that tax has been paid or deducted on the income or sale being remitted."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with a short note of the transaction (who invested or remitted, when and how much), the company's CIN or your PAN, any FIRC / KYC, share allotment or transfer documents and any RBI or bank email about a pending or late filing. We tell you what is due, what is late and the order to fix it, or book a call.")],
    related=[("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR filing checklist"),
             ("form-fc-trs-filing-checklist-india-2026.html", "FC-TRS filing checklist"),
             ("fla-return-foreign-liabilities-assets-rbi-india.html", "FLA return"),
             ("fema-late-submission-fee-calculator-fc-gpr-fc-trs-form-di-fla-apr-lsf-rbi-2026.html", "FEMA late submission fee calculator"),
             ("best-ca-fema-compounding-voluntary-india.html", "FEMA compounding"),
             ("ca-for-fema-odi-compliance.html", "ODI reporting and compliance")],
    cta_h="Need a FEMA filing done or fixed?", cta_b=C,
    keywords="fema consultant, fema consultants in mumbai, fema consultants in delhi ncr, fema consultants in bangalore, fema consultant pune, fema consultant hyderabad, fema consultant chennai, fema consultant near me, fdi compliance consultant, odi compliance, fc-gpr filing, fema compounding consultant",
    desc="FEMA consultant for FDI, ODI, NRI and RBI filings: FC-GPR within 30 days, FC-TRS within 60 days, FLA by 15 July, APR by 31 December, NRI repatriation (Form 146), late submission fee and compounding - done online for Mumbai, Delhi NCR, Bangalore, Pune, Hyderabad, Chennai and abroad.",
    howto={"name": "How to get FEMA reporting in order", "description": "From review to compounding.", "steps": [
        {"name": "List every cross-border transaction", "text": "Foreign inflows, outflows and share transfers since incorporation, with dates and amounts."},
        {"name": "Check what was filed", "text": "Match each transaction against FC-GPR, FC-TRS, FLA, ODI and repatriation filings."},
        {"name": "File what is current", "text": "Clear filings still within their time limit first."},
        {"name": "Regularise late filings", "text": "Late submission fee where available; compounding application for the rest."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KH complete")
