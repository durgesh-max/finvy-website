# -*- coding: utf-8 -*-
"""Batch GQ (24 Nov 2026): FPI registration in India - what a foreign portfolio investor is, Category I vs II, who can
register (including family offices and individuals), the process through a designated depository participant (DDP) with
the Common Application Form (CAF) that also allots PAN, fees now in rupees, continuance, SWAGAT-FI for trusted investors,
investment limits, tax on FPI income, and FPI vs FDI. Call-first page for foreign funds, family offices and NRIs.
Demand: sweep ac78 (24 Nov 2026), all 7 markets: "fpi registration", "fpi registration process / with sebi / fees /
certificate", "foreign portfolio investors meaning", "foreign portfolio investors category i".
Facts (checked 24 Nov 2026): SEBI (FPI) Regulations, 2019 - Category I (government and related, regulated entities from
FATF member jurisdictions, IFSC entities) and Category II (others, including unregulated funds, corporates, family offices
and individuals); registration through a DDP using the CAF, which also allots PAN, with digital signature integration
from January 2026; SEBI moved FPI fees to rupees in 2026 with a transition; fees for continuance due at least 15 days
before validity ends; SWAGAT-FI for trusted investors with longer registration validity (SEBI circulars, NSDL DDP
guidelines, Nishith Desai, Mondaq, Kotak). Investment limit below 10% of a company per FPI group; tax rates as on site
pages (12.5% LTCG above INR 1.25 lakh on listed equity, 20% STCG, 20% on interest and dividends subject to treaties)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "fpi-registration-india-2026-foreign-portfolio-investor-category-i-ii-process-ddp-tax"

C = contact("who the investor is (fund, family office, company, individual), where it is based and regulated, what it wants to buy in India, and whether any NRI, OCI or resident Indian is involved")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="FPI Registration in India (2026): Foreign Portfolio Investor Categories, Process Through a DDP, Limits and Tax",
    em="register once with a custodian, then invest in listed India.",
    kicker="/ Foreign investors &middot; FPI &middot; Updated 2026-11-24",
    lead=("<strong>A foreign portfolio investor (FPI) is a foreign fund, institution, company, family office or individual registered with SEBI to invest in listed Indian shares, bonds and other securities, holding less than 10% of any one company.</strong> "
          "Registration is done through a <strong>designated depository participant (DDP)</strong>, usually a custodian bank, using SEBI&rsquo;s Common Application Form, which also gets the investor an Indian PAN. "
          "Investors are classed as <strong>Category I</strong> (governments, central banks, pension funds and regulated entities from FATF member countries) or <strong>Category II</strong> (everyone else). Fees moved to rupees in 2026, and trusted investors can use SEBI&rsquo;s SWAGAT-FI route for simpler, longer registration. "
          "Indian tax applies to gains, interest and dividends, often reduced by a tax treaty."),
    sections=[
        ("/ Quick answers", "What foreign investors ask.",
         ul("<strong>What is a foreign portfolio investor?</strong> A non-resident investor registered with SEBI to buy listed Indian securities as a portfolio investment, below 10% of any one company.",
            "<strong>Who can register?</strong> Funds, banks, insurers, pension funds, sovereign funds, corporates, family offices and individuals resident outside India, subject to KYC and source-of-funds checks.",
            "<strong>What are Category I and Category II?</strong> Category I covers governments, central banks, sovereign and pension funds, and appropriately regulated entities from FATF member jurisdictions; Category II is everyone else.",
            "<strong>How long does registration take?</strong> It depends on documents and the DDP&rsquo;s checks; complete applications are often processed in a few weeks.",
            "<strong>Can NRIs and OCIs invest through an FPI?</strong> Yes, as constituents within SEBI&rsquo;s limits; individually, NRIs usually invest more simply through the portfolio investment scheme instead.")),
        ("/ Process and limits", "Steps and the rules that follow.",
         table(["Step or rule", "What it involves"], [
             ["Choose a DDP and custodian", "A SEBI-approved DDP, typically a global or Indian custodian bank"],
             ["Common Application Form", "Filed online with KYC documents; also allots PAN, with digital signature built in since January 2026"],
             ["Category and KYC", "Category I or II, beneficial owner details, source of funds"],
             ["Registration and fees", "DDP grants registration on SEBI's behalf; fees payable in rupees under the 2026 revision; continuance fees due before validity ends"],
             ["Bank and demat accounts", "Special non-resident rupee and foreign currency accounts, demat and broker accounts"],
             ["Investment limits", "Below 10% of any company per FPI group, within sector caps and any aggregate FPI limit"],
             ["Ongoing", "Reporting through the custodian, KYC refresh, tax filings in India"]])
         + '<p>FPI or FDI? Holdings of 10% or more, or strategic stakes in unlisted companies, are foreign direct investment instead; see ' + L("fdi-vs-fpi-india-startup-investment.html", "FDI vs FPI") + ' and ' + L("aif-vs-pms-vs-fpi.html", "AIF vs PMS vs FPI") + '.</p>'),
        ("/ Tax on FPI income", "What India deducts and what you can recover.",
         ul("<strong>Capital gains on listed shares:</strong> 12.5% on long-term gains above INR 1.25 lakh a year, 20% on short-term gains; securities gains of FPIs are taxed as capital gains.",
            "<strong>Interest and dividends:</strong> generally 20% under Indian law, reduced to the treaty rate with a tax residency certificate and Form 41 (formerly Form 10F).",
            "<strong>Tax return:</strong> an FPI with Indian income usually files an Indian return to settle the final tax and claim any refund.",
            "<strong>GIFT City:</strong> funds set up in the International Financial Services Centre have separate, often lower-tax routes; see " + L("gift-city.html", "GIFT City") + ".")
         + call_box("FPI registration and tax", ["Category and structure for a fund or family office",
                                                  "Coordinating the DDP and custodian application",
                                                  "NRI, OCI or resident Indian participation limits",
                                                  "Treaty rates, TRC and Form 41",
                                                  "Indian tax returns and refunds for FPIs"],
                    "who the investor is, where it is based and what it plans to buy.")
         + sources("SEBI (Foreign Portfolio Investors) Regulations, 2019 and SEBI master circular for FPIs; SEBI circulars of 2026 on the Common Application Form, digital signatures, SWAGAT-FI and rupee-denominated fees; NSDL DDP operational guidelines; commentary from Nishith Desai Associates, Mondaq and Kotak; Income-tax Act provisions on FPI income. Fee amounts change; confirm with the DDP. Checked 24 November 2026.")),
    ],
    faqs=[("What is a foreign portfolio investor (FPI) in India?", "A non-resident investor such as a fund, institution, company, family office or individual registered with SEBI to invest in listed Indian securities, holding less than 10% of any one company. Larger or strategic stakes are foreign direct investment instead."),
          ("How do you register as an FPI in India?", "Through a SEBI-approved designated depository participant, usually a custodian bank: file the online Common Application Form with KYC documents, which also allots an Indian PAN, pay the registration fee, then open the bank, demat and broker accounts."),
          ("What is the difference between Category I and Category II FPIs?", "Category I covers governments, central banks, sovereign wealth and pension funds, and appropriately regulated entities from FATF member jurisdictions. Category II covers all other eligible investors, such as unregulated funds, corporates, family offices and individuals."),
          ("What are the FPI registration fees?", "SEBI moved FPI fees to rupees in 2026, with a transition period, and fees for continuance must be paid before the registration validity ends. Ask the DDP for the current amount for your category."),
          ("How is FPI income taxed in India?", "Long-term gains on listed shares at 12.5% above INR 1.25 lakh a year and short-term gains at 20%; interest and dividends generally at 20%, reduced to the treaty rate with a tax residency certificate and Form 41."),
          ("Can BQP help with FPI registration and tax?", "Yes. " + C)],
    related=[("fdi-vs-fpi-india-startup-investment.html", "FDI vs FPI"),
             ("aif-vs-pms-vs-fpi.html", "AIF vs PMS vs FPI"),
             ("how-to-invest-in-indian-stock-market-from-usa-uk-uae-nri-oci-foreigner-demat-pis-tax-2026.html", "Investing in Indian shares from abroad"),
             ("gift-city.html", "GIFT City"),
             ("what-is-dtaa.html", "What is a DTAA")],
    cta_h="Investing in India as a foreign fund or family office?", cta_b=C,
    keywords="FPI registration, FPI registration India, FPI registration process, FPI registration with SEBI, foreign portfolio investor meaning, FPI category I, FPI category II, designated depository participant, FPI tax India",
    desc="FPI registration in India (2026): foreign portfolio investors register with SEBI through a designated depository participant using the Common Application Form (which also allots PAN); Category I vs II; below 10% per company; fees now in rupees; SWAGAT-FI; tax at 12.5% / 20% on gains and 20% on interest and dividends subject to treaties.",
    howto={"name": "How to register as a foreign portfolio investor in India", "description": "Steps from category to first trade.", "steps": [
        {"name": "Confirm eligibility and category", "text": "Category I for governments and regulated entities from FATF countries; Category II for others."},
        {"name": "Appoint a DDP and custodian", "text": "A SEBI-approved designated depository participant."},
        {"name": "File the Common Application Form", "text": "With KYC and beneficial owner documents; PAN is allotted in the same process."},
        {"name": "Pay fees and get registered", "text": "Fees in rupees under the 2026 revision."},
        {"name": "Open accounts and invest", "text": "Bank, demat and broker accounts; stay below 10% of any company."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GQ complete")
