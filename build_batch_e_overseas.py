# -*- coding: utf-8 -*-
"""Batch E: Overseas Incorporation umbrella + 5 jurisdictions for Indian founders."""
from build_lib import page, write_page

# 1. PILLAR: Overseas Incorporation Guide
write_page("overseas-incorporation-guide-indian-founder", page(
    slug="overseas-incorporation-guide-indian-founder",
    title="Overseas Incorporation for Indian Founders 2026 | US, UAE, SG, UK - BQP",
    description="Complete overseas incorporation guide for Indian founders 2026: US Delaware vs UAE vs Singapore vs UK vs Estonia vs Hong Kong. Decision framework, FEMA ODI mechanics, tax implications, bank account. CA Durgesh Chavda.",
    keywords="overseas incorporation India, Indian founder foreign company, Delaware vs Singapore vs UAE, best country to incorporate from India, FEMA ODI, Indian founder global entity",
    hero_kicker="/ Overseas incorporation &middot; Pillar",
    hero_title_html="Overseas incorporation for Indian founders, <em>the full decision tree.</em>",
    hero_lead="There is no universally-right overseas jurisdiction &mdash; the right choice depends on your product (SaaS vs D2C vs services), your customer location, your funding plan (US VC vs bootstrapped vs India VC), your tax residence, and your exit horizon. This pillar walks the decision across six main jurisdictions with the trade-offs that actually matter.",
    sections=[
        ("/ Why Indian founders go overseas", "The real reasons.",
         "<p>Setting up an entity outside India is driven by one or more of:</p>"
         "<ul>"
         "<li><strong>Enterprise customers won't contract with an Indian entity.</strong> US / UK / EU Fortune 500 procurement teams require their vendor to be domiciled in a familiar jurisdiction. A Delaware C-Corp or UK Ltd is the common unlock.</li>"
         "<li><strong>US venture capital invests only in Delaware C-Corps.</strong> If US seed or Series A is the plan, Delaware is non-optional.</li>"
         "<li><strong>Payment rails require it.</strong> Stripe (US), Mercury, Brex, Apple Developer, Google Play, PayPal Business &mdash; many prefer or require a US entity for optimal onboarding.</li>"
         "<li><strong>Lower corporate tax or no personal tax.</strong> UAE (9% CT), Singapore (17% but partial exemption), Delaware (21% federal + 8.7% Delaware). India 25-30% for corporates.</li>"
         "<li><strong>Founder residence or planned relocation.</strong> If the founder is moving to Dubai or Singapore, an entity in that jurisdiction aligns residence with operation.</li>"
         "<li><strong>IP ownership.</strong> Delaware or Singapore IP ownership is sometimes preferred by acquirors or VCs.</li>"
         "</ul>"),
        ("/ The six-way comparison", "US, UAE, Singapore, UK, Estonia, Hong Kong.",
         "<p><strong>US (Delaware / Wyoming):</strong> Default for VC-fundable startups. 21% federal + ~1-9% state corporate tax. Delaware franchise tax USD 400+. Delaware C-Corp supports US VC term-sheet mechanics. Wyoming LLC: lower cost, pass-through, not VC-fundable. US employee hiring + Stripe + Mercury banking.</p>"
         "<p><strong>UAE (Mainland / Free Zone):</strong> 9% Corporate Tax above AED 375,000 (post-2023). Free Zone Qualifying Person: 0% possible on qualifying income. No personal income tax (relevant if founder is UAE resident). Golden Visa + residency pathway. Weaker: VC infrastructure, enterprise-customer familiarity, employee pool for tech.</p>"
         "<p><strong>Singapore (Pte Ltd):</strong> 17% corporate tax with partial exemption (effective 10-12% on first SGD 300K). GST 9%. Strong tax treaty network. Excellent VC infrastructure (Antler, Sequoia Southeast Asia, Golden Gate Ventures). Strong banking (DBS, OCBC, Mercury via partner). SGD 50-100K effective minimum operating cost per year.</p>"
         "<p><strong>UK (Ltd):</strong> 25% corporation tax (19% for small-profit companies). GBP 100 incorporation. UK tax treaty network strong. Easier EU-facing entity post-Brexit. Weaker: no capital gains preferential rate at exit (ETMO replaced), ongoing CA / company secretary cost.</p>"
         "<p><strong>Estonia (OU, e-Residency):</strong> 20% distributed-profit tax &mdash; no tax on retained profits. e-Residency program allows fully-remote company setup. Attractive for digital-only businesses that reinvest. Weaker: limited banking without physical presence, lower treaty rate ambiguities, EU VAT compliance.</p>"
         "<p><strong>Hong Kong (Private Limited):</strong> 16.5% corporate tax; 0% on foreign-source income. Historically strong banking (though tighter post-2020). CPA and HK company secretary required. Weaker since 2020 political environment.</p>"),
        ("/ Decision framework", "Match jurisdiction to your situation.",
         "<p><strong>Scenario 1: AI startup planning US VC round in 6-12 months.</strong> &rarr; Delaware C-Corp. Set up with 83(b)-ready founder stock, QSBS 5-year clock starts immediately, standard VC term-sheet machinery applies.</p>"
         "<p><strong>Scenario 2: SaaS startup selling to US and UK enterprises; founder in Bengaluru; bootstrapped and cash-flow positive.</strong> &rarr; Delaware C-Corp or Wyoming LLC. C-Corp if US customer contracts require signed-by-C-Corp paperwork. LLC if pure pass-through is sufficient and no US VC.</p>"
         "<p><strong>Scenario 3: Founder moving to Dubai; running a trading / consulting business with Middle East customers.</strong> &rarr; UAE Free Zone LLC. Golden Visa, 0% personal tax, Free Zone Qualifying Person for low corporate tax.</p>"
         "<p><strong>Scenario 4: Southeast Asia expansion; selling to Indonesian / Singaporean customers; need regional licensing.</strong> &rarr; Singapore Pte Ltd. MAS fintech licensing available, strong treaty network for intra-Asia operations.</p>"
         "<p><strong>Scenario 5: European customers; need VAT-registered entity in EU.</strong> &rarr; UK Ltd or Estonia OU (e-Residency). UK for enterprise-sales mechanics; Estonia for digital reinvestment-heavy businesses.</p>"
         "<p><strong>Scenario 6: Family office or UHNI capital structuring, not operating business.</strong> &rarr; UAE DIFC, Singapore VCC, Mauritius GBL, or Delaware LP depending on specific needs.</p>"),
        ("/ The FEMA ODI side", "Common to all jurisdictions.",
         "<p>Any Indian resident setting up or investing in an overseas entity triggers Overseas Direct Investment (ODI) under FEMA. The 2022 Overseas Investment Rules provide an Automatic Route for most startup-scale investments and a specific Approval Route for larger or specific-sector investments.</p>"
         "<p>Automatic Route key features:</p>"
         "<ul>"
         "<li>Investment via authorised dealer bank, no RBI approval needed.</li>"
         "<li>Investor must file Form ODI within 30 days of remittance.</li>"
         "<li>Investment capped at 400% of Indian net worth (for Indian company investors); unlimited for LRS individual up to USD 250K per financial year.</li>"
         "<li>Specific sector carve-outs apply (real estate, financial services, pharmaceuticals etc.).</li>"
         "</ul>"
         "<p>Approval Route triggers:</p>"
         "<ul>"
         "<li>Investment exceeds Automatic Route limits.</li>"
         "<li>Target entity is in a restricted sector.</li>"
         "<li>Investment structure involves specific financial instruments (debt from Indian individual).</li>"
         "</ul>"
         "<p>The flip side (US-side considerations) depends on jurisdiction &mdash; Form 5472 for Delaware foreign-owned LLC, UAE ESR compliance, Singapore LOB substance test, UK PSC (Persons of Significant Control) register, etc.</p>"),
    ],
    faqs=[
        ("Which overseas jurisdiction is best for Indian SaaS founders?",
         "Default: Delaware C-Corp if US VC is in the plan, Wyoming LLC if bootstrapped. The Indian SaaS founder landscape is heavily US-oriented &mdash; US customers, US VCs, US payment rails. Singapore or UAE become relevant for specific regional expansion. There is no universally-best; the honest answer requires modelling your 12-month funding plan + customer location + revenue profile."),
        ("What is the cheapest overseas jurisdiction to incorporate from India?",
         "Estonia OU via e-Residency: ~EUR 300 incorporation + ~EUR 200/year ongoing. Wyoming LLC: ~USD 100 incorporation + USD 150-250/year. Delaware LLC: ~USD 90 + USD 400-700/year franchise tax. UAE Free Zone: USD 5,000-15,000 setup + USD 2,000-5,000/year. Cheapest doesn't mean best &mdash; weigh against your business needs."),
        ("Do I need to go to the US to incorporate in Delaware?",
         "No. Fully remote. Delaware incorporation + EIN (via Form SS-4 fax or international phone) + Mercury or Brex business bank account can all be done from India. Full setup typically 3-6 weeks. Even post-formation operations rarely require physical visit."),
        ("Does FEMA ODI apply to US / UAE / Singapore incorporation by Indian individuals?",
         "Yes to all. Indian resident individual: LRS limit of USD 250K per financial year under Automatic Route. Indian resident company: 400% of Indian net worth under Automatic Route. Investor files Form ODI within 30 days of remittance; the Indian authorised dealer bank processes the outward remittance after seeing Form ODI."),
        ("Can I pay myself a salary from my Delaware C-Corp while living in India?",
         "Yes. The Delaware C-Corp can pay you a salary, which is a US-source expense from the C-Corp's perspective and an India-taxable salary from your perspective. US withholding: typically none if services are performed in India (Section 864 ECI analysis). Indian tax: full slab-rate taxable in India. India-US DTAA Article 15 applies &mdash; India has primary taxing right for services performed in India."),
        ("Does BQP handle overseas incorporation across jurisdictions?",
         "Yes. Delaware (primary), Wyoming, UAE Free Zone (Dubai IFZA, DMCC, DIFC where applicable), Singapore (Pte Ltd), UK (Ltd), Estonia (OU via e-Residency), Hong Kong (Private Ltd), Mauritius (GBL where it still fits). We scope the right jurisdiction against your 12-month plan, then handle incorporation + FEMA ODI + first-year compliance under one engagement. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp"),
        ("singapore-incorporation-indian-founder.html", "Guide", "Singapore for Indian Founder"),
        ("uae-incorporation-indian-founder.html", "Guide", "UAE for Indian Founder"),
    ],
    cta_headline="Not sure which jurisdiction? Start with a scoping call.",
    cta_body="A 60-minute scoping call covers: your 12-month funding plan, customer / employee / investor geography, product + revenue profile, founder residence. We produce a written recommendation across 2-3 jurisdictions with cost comparison, FEMA + tax mechanics, and setup timeline. Standard pricing for incorporation starts at INR 99,000+.",
))

# 2. Singapore for Indian founder
write_page("singapore-incorporation-indian-founder", page(
    slug="singapore-incorporation-indian-founder",
    title="Singapore Incorporation for Indian Founders 2026 | Pte Ltd Guide - BQP",
    description="Singapore Pte Ltd incorporation for Indian founders: ACRA registration, S-Pass / EP, 17% corporate tax with partial exemption, GST, MAS fintech licensing, bank account (DBS/OCBC), FEMA ODI. CA guide.",
    keywords="Singapore incorporation India, Pte Ltd Singapore Indian founder, ACRA Singapore, Singapore corporate tax Indian company, Singapore vs Delaware India, FEMA ODI Singapore",
    hero_kicker="/ Overseas incorporation &middot; Singapore",
    hero_title_html="Singapore for Indian founders, <em>when it beats Delaware.</em>",
    hero_lead="Singapore is the standard pick for Indian founders expanding into Southeast Asia, raising from Southeast Asian VCs, running regulated fintech or regional-licence businesses, or holding IP for intra-Asia operations. It is not the default for US-VC-track startups &mdash; Delaware is. Here is where Singapore wins and where it doesn't.",
    sections=[
        ("/ Singapore company types", "Pte Ltd is the standard.",
         "<p>Primary vehicle: <strong>Private Company Limited by Shares (Pte Ltd)</strong> registered with ACRA (Accounting and Corporate Regulatory Authority).</p>"
         "<ul>"
         "<li>Minimum 1 director (must be ordinarily resident in Singapore).</li>"
         "<li>Minimum 1 shareholder (can be foreign individual or foreign company).</li>"
         "<li>Minimum paid-up capital SGD 1.</li>"
         "<li>Company secretary required within 6 months of incorporation.</li>"
         "<li>Registered Singapore address.</li>"
         "</ul>"
         "<p>The resident director requirement is the single operational constraint for Indian founders &mdash; without a Singapore-resident director, the entity cannot be registered. Options: hire a nominee director service (SGD 1,500-3,500 per year), move a founder to Singapore (via EntrePass / Employment Pass), or appoint a Singapore co-founder.</p>"
         "<p>Other vehicle types for specific use cases: Variable Capital Company (VCC) for funds, Limited Liability Partnership (LLP) for professional services.</p>"),
        ("/ Singapore corporate tax", "17% headline, lower effective.",
         "<p><strong>Headline rate:</strong> 17% on taxable income.</p>"
         "<p><strong>Partial Tax Exemption Scheme:</strong> for first SGD 10,000 of chargeable income, 75% exempt; next SGD 190,000, 50% exempt. Effective rate on first SGD 200K is roughly 8.5% (first year post-incorporation startups qualify for an even more generous Startup Tax Exemption for 3 years).</p>"
         "<p><strong>Startup Tax Exemption (SUTE):</strong> for the first 3 years of assessment, first SGD 100K is 75% exempt and next SGD 100K is 50% exempt &mdash; effective rate first SGD 100K is ~4.25%, first SGD 200K is ~6.4%.</p>"
         "<p><strong>No capital gains tax</strong> in Singapore for genuine investments.</p>"
         "<p><strong>Withholding tax</strong> on outbound payments: 15% on royalties, 10% on technical service fees to non-residents, 15% on interest. Treaty reductions apply (India-SG treaty caps at 10% for royalties/FTS).</p>"
         "<p><strong>GST:</strong> 9% (post-2024). Registration mandatory if annual turnover exceeds SGD 1M, voluntary below.</p>"),
        ("/ Setting up from India", "The practical steps.",
         "<ol>"
         "<li><strong>Name reservation</strong> via ACRA BizFile. SGD 15. 1-2 days.</li>"
         "<li><strong>Appoint resident director</strong> &mdash; either move a co-founder on EntrePass / Employment Pass (processing 1-2 months) or engage a nominee director service.</li>"
         "<li><strong>Engage company secretary</strong> &mdash; SGD 300-600 per year typically.</li>"
         "<li><strong>Register the Pte Ltd</strong> with ACRA. SGD 300. Approval 1-3 days for standard filings.</li>"
         "<li><strong>Open bank account</strong> &mdash; DBS Business, OCBC Business, UOB Business, or fintech alternatives (ANEXT, Aspire, Wise Business). Traditional bank accounts increasingly require resident director interview; fintechs are more remote-friendly.</li>"
         "<li><strong>Register for GST</strong> if applicable, Corppass for government-portal access.</li>"
         "<li><strong>Register for CPF</strong> if hiring Singapore-resident employees.</li>"
         "<li><strong>FEMA ODI compliance</strong> on the India side &mdash; Form ODI within 30 days of outward remittance.</li>"
         "</ol>"
         "<p>Typical total setup time: 3-8 weeks depending on director approach and bank-account processing.</p>"),
        ("/ Singapore vs Delaware for Indian founders", "The honest comparison.",
         "<p><strong>Choose Singapore if:</strong></p>"
         "<ul>"
         "<li>Primary customers are in Southeast Asia or China.</li>"
         "<li>You are raising from Southeast Asian VCs (Antler, Sequoia Southeast Asia, Golden Gate, East Ventures, 500 Southeast Asia).</li>"
         "<li>You are running a fintech / payments / regulated business &mdash; MAS licensing (PSA, CMS, licenses for digital assets).</li>"
         "<li>Founder is planning to relocate to Singapore long-term.</li>"
         "<li>IP ownership in a tax-efficient jurisdiction with strong treaty network.</li>"
         "</ul>"
         "<p><strong>Choose Delaware if:</strong></p>"
         "<ul>"
         "<li>Primary customers / investors are in the US.</li>"
         "<li>Target is US VC capital.</li>"
         "<li>Payment rail is Stripe / Mercury / Brex.</li>"
         "<li>83(b) + QSBS matter.</li>"
         "<li>Lower incorporation cost (DE ~USD 500/year total; SG ~SGD 2000-4000/year with nominee director).</li>"
         "</ul>"
         "<p>Many Indian founders use both: Delaware C-Corp as the parent, Singapore Pte Ltd as the Southeast Asia operating subsidiary. Costs ~USD 5-8K setup + USD 3-5K/year ongoing, but opens both US VC and SEA customer paths.</p>"),
    ],
    faqs=[
        ("Can an Indian citizen be the sole shareholder of a Singapore Pte Ltd?",
         "Yes. ACRA allows 100% foreign ownership. The only resident requirement is for at least one director to be ordinarily resident in Singapore &mdash; a Singapore citizen, PR, Employment Pass holder, or EntrePass holder. If no founder qualifies, a nominee director service fills the role."),
        ("Is Singapore cheaper than Delaware for incorporation?",
         "No, usually not. Delaware is roughly USD 90 incorporation + USD 400-700/year franchise + USD 100-200/year registered agent = USD 600-1,000/year steady state. Singapore is roughly SGD 300 incorporation + SGD 1,500-3,500/year nominee director + SGD 300-600 company secretary + SGD 300-500 bookkeeping = SGD 2,500-5,000/year (USD 1,900-3,800). Delaware is cheaper for small operating entities."),
        ("Do I need a Singapore employment visa to run my Pte Ltd?",
         "Not technically to own it &mdash; but if you want to be the director (fulfilling the resident-director requirement) and / or draw a Singapore salary, you need Employment Pass or EntrePass. Alternative: nominee director + remote operation from India + draw dividend / consulting fee instead of salary."),
        ("What is Singapore's tax rate on dividends to Indian shareholder?",
         "Singapore does not withhold tax on dividends paid to shareholders (one-tier corporate tax system). So the Singapore Pte Ltd pays 17% (or lower effective rate) corporate tax, and the Indian shareholder receives dividends with no Singapore withholding. The Indian shareholder reports the dividend as foreign income and pays Indian tax; India-Singapore DTAA Article 10 provides for FTC."),
        ("Can I convert my Indian Pvt Ltd to a Singapore Pte Ltd?",
         "Not directly &mdash; you can set up a Singapore Pte Ltd and transfer the Indian company's business, assets, or shareholding to it via FEMA-compliant transactions. Full flip (making the Singapore entity the parent of the Indian entity) is possible via share swap, with FEMA ODI compliance and Indian capital gains for the shareholders. The 2017 India-Singapore DTAA protocol closed the capital-gains exemption that made this cheap &mdash; now Indian LTCG applies on the swap."),
        ("Does BQP handle Singapore incorporation for Indian founders?",
         "Yes. ACRA registration, nominee director co-ordination, company secretary setup, DBS / OCBC / fintech bank account introduction, GST registration where applicable, FEMA ODI on India side, and ongoing annual compliance (XBRL filing, AGM, directors' report, corporate tax return). Standard package pricing available. Request via get-a-quote.html."),
    ],
    related=[
        ("overseas-incorporation-guide-indian-founder.html", "Pillar", "Overseas Incorp Pillar"),
        ("india-singapore-tax-treaty-dtaa.html", "DTAA", "India-Singapore DTAA"),
        ("us-incorporation.html", "Guide", "US Incorporation (compare)"),
    ],
    cta_headline="Singapore makes sense for ~30% of Indian founders. The scoping call tells you.",
    cta_body="A 60-minute scoping covers Delaware-vs-Singapore-vs-UAE-vs-UK across your actual business parameters &mdash; customers, VC plan, founder residence, product + regulatory profile. We produce written recommendation + cost model. Standard Singapore setup from BQP starts at SGD 3,500 all-in.",
))

# 3. UAE for Indian founder
write_page("uae-incorporation-indian-founder", page(
    slug="uae-incorporation-indian-founder",
    title="UAE Incorporation for Indian Founders 2026 | Free Zone, DIFC - BQP",
    description="UAE incorporation for Indian founders: Mainland LLC, Free Zone (IFZA, DMCC, Meydan, DIFC), 9% Corporate Tax, 0% QFZP, Golden Visa, ESR compliance, Dubai bank account. Working CA guide.",
    keywords="UAE incorporation India, Dubai company Indian founder, Free Zone UAE, DMCC IFZA DIFC, UAE Corporate Tax 9%, QFZP qualifying free zone person, UAE Golden Visa",
    hero_kicker="/ Overseas incorporation &middot; UAE",
    hero_title_html="UAE for Indian founders, <em>Mainland vs Free Zone vs DIFC.</em>",
    hero_lead="UAE is the leading relocation destination for Indian HNIs and the fastest-growing hub for Indian consumer-trading, consulting, holding-structure and family-office businesses. Post-2023 Corporate Tax changed the economics; the Free Zone 0% route is still available for Qualifying Free Zone Persons. Here is the full working-CA map.",
    sections=[
        ("/ UAE jurisdiction types", "Mainland, Free Zone, DIFC/ADGM.",
         "<p><strong>Mainland (Dubai Economic Department / equivalent emirate authority):</strong></p>"
         "<ul>"
         "<li>Can trade freely with UAE customers and across all emirates.</li>"
         "<li>Up to 100% foreign ownership post-2020 reforms (previously 51% UAE partner required for most activities; sector-specific exceptions remain).</li>"
         "<li>9% UAE Corporate Tax applies above AED 375,000 profit.</li>"
         "<li>Standard choice for consumer-facing, services-with-UAE-customers, or Mainland-regulated businesses.</li>"
         "</ul>"
         "<p><strong>Free Zone (IFZA, DMCC, Dubai South, Meydan, RAK, Ajman, Fujairah):</strong></p>"
         "<ul>"
         "<li>100% foreign ownership from day one.</li>"
         "<li>Limited to intra-Free Zone and international business; needs Mainland distributor to sell to UAE Mainland customers.</li>"
         "<li>Qualifying Free Zone Person (QFZP) status under Corporate Tax: 0% on qualifying income if ESR and substance conditions met; 9% on non-qualifying income.</li>"
         "<li>Dedicated residence visa quota based on licence type and office space.</li>"
         "</ul>"
         "<p><strong>DIFC (Dubai International Financial Centre) / ADGM (Abu Dhabi Global Market):</strong></p>"
         "<ul>"
         "<li>Common-law jurisdictions within UAE (English common law, separate courts).</li>"
         "<li>Preferred for financial services, family offices, holding companies, fund management.</li>"
         "<li>DIFC Prescribed Company regime: lightweight holding structure.</li>"
         "<li>ADGM Private Family Office regime: dedicated for family-office holdings.</li>"
         "<li>Higher setup and ongoing costs; stronger regulatory + legal infrastructure.</li>"
         "</ul>"),
        ("/ UAE Corporate Tax 2023", "What changed and what matters.",
         "<p>Federal Decree-Law 47 of 2022, effective 1 June 2023, introduced UAE Corporate Tax:</p>"
         "<ul>"
         "<li><strong>Standard rate 9%</strong> on taxable income above AED 375,000 (~USD 102K).</li>"
         "<li><strong>0% rate</strong> on first AED 375,000 of profit (small-business relief for all entities).</li>"
         "<li><strong>Free Zone Qualifying Free Zone Person (QFZP):</strong> 0% on qualifying income; 9% on non-qualifying income. Qualifying income rules are technical and under FTA scrutiny.</li>"
         "<li><strong>Economic Substance Regulations (ESR):</strong> continuing from pre-2023 regime; applies to relevant activities (banking, insurance, fund management, headquarters, holding company, IP, distribution, service centre). Annual notification + report mandatory.</li>"
         "<li><strong>Country-by-Country Reporting (CbCR):</strong> for MNE groups above EUR 750M.</li>"
         "<li><strong>Transfer Pricing:</strong> arm's length principle, OECD-aligned documentation.</li>"
         "</ul>"
         "<p>Historical pure-zero-tax UAE positioning is over. Current positioning: low-tax (9%) with QFZP 0% route available for genuine Free Zone businesses with Qualifying Activities.</p>"),
        ("/ Golden Visa + residency", "What it unlocks.",
         "<p>UAE Golden Visa (10-year residence) is available for:</p>"
         "<ul>"
         "<li>Investors in real estate (AED 2M+ property).</li>"
         "<li>Entrepreneurs holding a licence with specified minimum capital or revenue.</li>"
         "<li>Skilled professionals in specified sectors with minimum salary thresholds.</li>"
         "<li>Scientists, researchers, specialised talents.</li>"
         "</ul>"
         "<p>Golden Visa provides UAE residence (not citizenship), access to UAE banking as a resident, UAE Tax Residency Certificate eligibility (post 183 days physical presence).</p>"
         "<p>Important: UAE Golden Visa does NOT automatically make the holder a UAE tax resident. UAE tax residence for individuals requires 183 days of physical presence in UAE in the tax year (post-2023 Resolution). Golden Visa holders spending most of the year in India remain Indian tax residents.</p>"),
        ("/ Setup from India", "Practical mechanics.",
         "<ol>"
         "<li><strong>Choose jurisdiction</strong> &mdash; Mainland vs Free Zone vs DIFC. Scope based on activity, customer, visa quota needs.</li>"
         "<li><strong>Choose activity classification</strong> &mdash; Trading, Consulting, Services, Industrial. Specific activity codes within each.</li>"
         "<li><strong>Reserve name</strong> with the authority. 1-3 days.</li>"
         "<li><strong>Initial approval</strong> + licence application. Depending on Free Zone, 1-3 weeks.</li>"
         "<li><strong>Lease office space</strong> &mdash; Free Zones often bundle flexi-desk packages (AED 10K-30K/year); DIFC / ADGM higher.</li>"
         "<li><strong>Receive licence</strong> + Chamber of Commerce membership (Mainland).</li>"
         "<li><strong>Investor residence visa</strong> processing (medical + Emirates ID + visa stamping) &mdash; 2-4 weeks after licence.</li>"
         "<li><strong>Bank account</strong> &mdash; most banks require resident director interview with Emirates ID. Processing 2-6 weeks (varies dramatically bank-to-bank; UAE banks have been tightening KYC post-2020).</li>"
         "<li><strong>FEMA ODI</strong> on India side &mdash; Form ODI within 30 days of outward remittance.</li>"
         "<li><strong>Corporate Tax registration</strong> + ESR notification + Transfer Pricing documentation setup.</li>"
         "</ol>"
         "<p>Total setup time: 6-12 weeks from kickoff to funded bank account.</p>"),
    ],
    faqs=[
        ("Is UAE still a 0% tax jurisdiction after 2023 Corporate Tax?",
         "Not generally. Standard 9% Corporate Tax applies above AED 375,000 profit on Mainland and Free Zone non-qualifying income. Free Zone Qualifying Free Zone Person (QFZP) status provides 0% on qualifying income &mdash; but the qualifying activity + substance tests are technical and the FTA scrutiny is real. Expect to pay something; model 9% as the base case."),
        ("What is Qualifying Free Zone Person (QFZP) status?",
         "A Free Zone entity that satisfies: adequate substance (actual activities in UAE Free Zone, qualified employees, operating expenditure), derives Qualifying Income (specific list including distribution to Free Zone persons, ownership of qualifying intangibles, holding shares and securities, treasury financing to related parties), maintains audited financial statements, and complies with Transfer Pricing documentation. QFZP income is taxed at 0% up to de-minimis limit; non-qualifying income taxed at 9%."),
        ("Does UAE Golden Visa make me a UAE tax resident?",
         "No, not automatically. UAE tax residence for individuals requires 183 days of physical presence in UAE in the tax year (per Cabinet Resolution 85/2022). Golden Visa provides UAE residence (immigration status) but not tax residence by itself. A Golden Visa holder spending 60 days in UAE and 300 days in India remains Indian tax resident."),
        ("Can I incorporate in UAE Free Zone from India without visiting?",
         "Partially. Name reservation, initial approval, and licence application can be done remotely. Office lease is required (physical or flexi-desk). Investor residence visa requires physical visit to UAE for medical, biometric and visa stamping. Bank account typically requires in-person account-opening interview. Expect at least one 7-10 day UAE visit during setup."),
        ("What is UAE Economic Substance Regulations (ESR)?",
         "ESR requires UAE entities carrying out Relevant Activities (banking, insurance, fund management, HQ, holding, IP, distribution, lease-finance, shipping, service centre) to demonstrate substance in UAE &mdash; core income-generating activities, adequate employees, adequate expenditure, physical premises. Annual notification + report filed with the regulatory authority. Non-compliance penalty AED 20K-50K+."),
        ("Does BQP handle UAE incorporation for Indian founders?",
         "Yes. We co-ordinate IFZA / DMCC / Meydan / DIFC setup, Golden Visa application support, UAE bank account introduction, Corporate Tax + ESR + TP registration, and FEMA ODI on India side. Standard package SGD-equivalent for Free Zone setup starts at USD 10,000 all-in including investor visa and bank account introduction. Request via get-a-quote.html."),
    ],
    related=[
        ("overseas-incorporation-guide-indian-founder.html", "Pillar", "Overseas Incorp Pillar"),
        ("india-uae-tax-treaty-dtaa.html", "DTAA", "India-UAE DTAA"),
        ("us-incorporation.html", "Guide", "US (compare)"),
    ],
    cta_headline="UAE is popular, but QFZP + ESR + 9% CT need real planning.",
    cta_body="For Indian founders moving to Dubai or setting up Free Zone trading / consulting structures, the right QFZP activity + ESR compliance pack + Golden Visa pathway is what determines whether UAE delivers its promise. Scoping call is free; package setup from USD 10,000.",
))

# 4. UK for Indian founder
write_page("uk-incorporation-indian-founder", page(
    slug="uk-incorporation-indian-founder",
    title="UK Incorporation for Indian Founders 2026 | Ltd, PSC, Tax - BQP",
    description="UK Private Limited (Ltd) incorporation for Indian founders: Companies House, 25% corporation tax, VAT 20%, PSC register, Tier 1 Innovator visa, UK bank account from India. CA guide.",
    keywords="UK Ltd incorporation India, Companies House Indian founder, UK corporation tax 25%, PSC register UK, UK Innovator visa, HSBC Barclays UK business account Indian",
    hero_kicker="/ Overseas incorporation &middot; UK",
    hero_title_html="UK Ltd for Indian founders, <em>when and why.</em>",
    hero_lead="UK Private Limited Company (Ltd) is the European-facing alternative to Delaware C-Corp for Indian founders. UK is weaker than US for VC-fundability but stronger for European enterprise sales, financial services licensing, and consumer-facing operations in the UK and EU post-Brexit.",
    sections=[
        ("/ UK Ltd basics", "Companies House mechanics.",
         "<p><strong>Private Limited Company (Ltd):</strong> primary vehicle for Indian founders.</p>"
         "<ul>"
         "<li>Minimum 1 director (no UK residence requirement &mdash; Indian founder can be sole director).</li>"
         "<li>Minimum 1 shareholder.</li>"
         "<li>Minimum share capital GBP 1.</li>"
         "<li>UK registered office address required.</li>"
         "<li>Companies House registration GBP 50 (standard) or GBP 78 (same-day).</li>"
         "<li>Annual confirmation statement + accounts filing mandatory.</li>"
         "</ul>"
         "<p><strong>PSC Register:</strong> Persons of Significant Control &mdash; individuals holding 25%+ shares, 25%+ voting rights, or significant influence. Must be registered at Companies House and publicly visible.</p>"),
        ("/ UK corporate tax", "25% headline (post-2023).",
         "<p><strong>Main rate 25%</strong> on taxable profits above GBP 250,000.</p>"
         "<p><strong>Small-profits rate 19%</strong> on profits up to GBP 50,000.</p>"
         "<p><strong>Marginal relief</strong> between GBP 50K and GBP 250K &mdash; smooth taper.</p>"
         "<p><strong>VAT 20%</strong> &mdash; registration mandatory above GBP 90K annual turnover (post-April 2024).</p>"
         "<p><strong>No capital gains preferential rate for individual shareholders at exit:</strong> ER / Business Asset Disposal Relief now has GBP 1M lifetime cap (reduced from GBP 10M in 2020). Essentially the exit-tax edge UK offered historically has eroded.</p>"
         "<p><strong>Dividends:</strong> no UK withholding on dividend paid to Indian shareholder. Indian shareholder reports as foreign income; India-UK DTAA FTC applies.</p>"),
        ("/ Setup from India", "Mechanics.",
         "<ol>"
         "<li><strong>Name availability check</strong> at Companies House.</li>"
         "<li><strong>UK registered office</strong> &mdash; London virtual office service (GBP 20-50/month) is standard. Some banks require this.</li>"
         "<li><strong>Incorporate</strong> via Companies House &mdash; online filing, GBP 50 fee, 24-hour approval typical.</li>"
         "<li><strong>HMRC registration</strong> for Corporation Tax (automatic within 3 months) and PAYE / VAT if applicable.</li>"
         "<li><strong>Bank account</strong> &mdash; HSBC, Barclays, Lloyds, NatWest; traditional banks require UK-resident director for interview or extensive video KYC. Fintech alternatives: Wise Business, Revolut Business, Starling &mdash; more remote-friendly, UK IBAN provided.</li>"
         "<li><strong>FEMA ODI</strong> on India side &mdash; Form ODI within 30 days.</li>"
         "</ol>"
         "<p>Setup time: 1-4 weeks for formation + HMRC; bank account 2-8 weeks (fintech faster than traditional).</p>"),
        ("/ When UK beats other jurisdictions", "The case for UK Ltd.",
         "<p>Choose UK Ltd if:</p>"
         "<ul>"
         "<li>Primary customers are in UK + Europe post-Brexit. UK contracts prefer UK counterparty.</li>"
         "<li>Running financial services needing FCA authorisation (payments, lending, investment management).</li>"
         "<li>Consumer D2C brand targeting UK market.</li>"
         "<li>Founder planning Tier 1 Innovator or Tier 2 Skilled Worker visa to UK.</li>"
         "<li>Need the EEA-era legacy structuring where UK Ltd was the European holding (reduced relevance post-Brexit).</li>"
         "</ul>"
         "<p>Choose Delaware instead if:</p>"
         "<ul>"
         "<li>US customers / US VC / US payment rail (Stripe default).</li>"
         "<li>83(b) + QSBS matter.</li>"
         "<li>SaaS targeting global English-speaking enterprise.</li>"
         "</ul>"),
    ],
    faqs=[
        ("Can an Indian citizen be the sole director of a UK Ltd?",
         "Yes. The UK has no residence requirement for directors or shareholders of a Private Limited Company. An Indian founder can be the sole director from India without visiting UK."),
        ("Is UK Ltd VC-fundable?",
         "Partially. UK Ltd can take UK or European VC investment under standard UK Articles + Shareholder Agreement. US VCs typically prefer Delaware C-Corp &mdash; a UK Ltd would need a Delaware parent flip for US VC round. For pure UK / European VC rounds, UK Ltd works."),
        ("What is PSC and does it affect privacy?",
         "PSC (Persons of Significant Control) is a public register at Companies House naming shareholders with 25%+ ownership or significant influence. Address, date of birth, nationality are visible publicly. If privacy matters, UK Ltd is weaker than Delaware (which does not publicly disclose shareholders)."),
        ("What is the UK VAT threshold?",
         "GBP 90,000 of annual VATable turnover (post-April 2024). Below the threshold, VAT registration is voluntary. Many Indian-founder UK Ltd businesses register voluntarily to be able to reclaim input VAT, especially if customer base is other VAT-registered businesses."),
        ("Can I open a UK bank account from India without visiting?",
         "Fintech routes (Wise Business, Revolut Business, Starling): yes, fully remote, 1-2 weeks. Traditional banks (HSBC, Barclays, Lloyds, NatWest): generally require UK-resident director interview; some HSBC Premier / Business routes allow video KYC with longer processing (4-8 weeks). Many Indian founders use fintech for operations + traditional later as scale grows."),
        ("Does BQP handle UK incorporation for Indian founders?",
         "Yes. Companies House registration, UK registered office arrangement, HMRC Corporation Tax + PAYE + VAT registration, Wise / Revolut bank account introduction, FEMA ODI on India side, and ongoing annual accounts + confirmation statement filing. Request via get-a-quote.html."),
    ],
    related=[
        ("overseas-incorporation-guide-indian-founder.html", "Pillar", "Overseas Incorp Pillar"),
        ("india-uk-tax-treaty-dtaa.html", "DTAA", "India-UK DTAA"),
        ("us-incorporation.html", "Guide", "US (compare)"),
    ],
    cta_headline="UK Ltd makes sense for UK + Europe-facing businesses.",
    cta_body="For US-oriented SaaS and VC-track companies, Delaware wins. For UK / Europe enterprise sales, UK FCA licensing, or UK consumer brands, UK Ltd fits. Scoping call includes side-by-side cost + regulatory analysis. UK Ltd setup from BQP: GBP 1,500 all-in including Wise account.",
))

# 5. Estonia e-Residency
write_page("estonia-eresidency-indian-founder", page(
    slug="estonia-eresidency-indian-founder",
    title="Estonia e-Residency for Indian Founders 2026 | OU Setup, Tax - BQP",
    description="Estonia e-Residency + OU company for Indian founders: fully-remote EU incorporation, 20% distributed-profit tax, no tax on retained earnings, EU VAT, banking challenges. Working CA guide.",
    keywords="Estonia e-Residency India, Estonia OU Indian founder, 20% distributed profit tax Estonia, EU company Indian founder remote, Estonia company bank account",
    hero_kicker="/ Overseas incorporation &middot; Estonia",
    hero_title_html="Estonia e-Residency for Indian founders, <em>fully-remote EU entity.</em>",
    hero_lead="Estonia's e-Residency program is the only truly-remote EU incorporation path for Indian founders. The OU (Osaühing / Private Limited Company) has a unique 20% distributed-profit tax regime: no tax on retained earnings. Where it fits: digital-only, reinvestment-heavy, EU-customer businesses. Where it does not fit: businesses needing a serious bank account.",
    sections=[
        ("/ What e-Residency actually is", "Not immigration, not tax residence.",
         "<p>Estonia e-Residency is a digital identity issued by the Estonian government to foreign individuals. It is <strong>NOT</strong>:</p>"
         "<ul>"
         "<li>EU residence or EU citizenship.</li>"
         "<li>Estonian tax residence.</li>"
         "<li>Schengen visa.</li>"
         "</ul>"
         "<p>It <strong>IS</strong>:</p>"
         "<ul>"
         "<li>A smart-card ID that lets you sign EU legal documents, incorporate an Estonian company, operate it digitally, file taxes.</li>"
         "<li>Access to EU-regulated service providers (fintech banks like Wise, Payoneer, Payhawk).</li>"
         "<li>A fully-remote path to operate a legitimate EU company.</li>"
         "</ul>"
         "<p>Application: online, EUR 100-120, decision in 1-3 months. Card collected at Estonian embassy or consulate (New Delhi / Mumbai).</p>"),
        ("/ Estonia OU corporate tax", "The retained-earnings advantage.",
         "<p><strong>Estonia corporate tax: 20% on distributed profits only.</strong> No tax on retained / reinvested earnings.</p>"
         "<p>Mechanics:</p>"
         "<ul>"
         "<li>Earn profits in Estonia OU &mdash; no immediate tax.</li>"
         "<li>Keep profits in the company for reinvestment, employee salaries, operating expenses &mdash; no tax.</li>"
         "<li>Distribute as dividends to shareholder (yourself) &mdash; 20% Estonia withholding at distribution.</li>"
         "<li>Shareholder (Indian) receives dividend; India tax applies with FTC under India-Estonia DTAA Article 10.</li>"
         "</ul>"
         "<p>For a business that reinvests all cash into growth (hiring, marketing, product), the effective Estonian corporate tax is close to zero until distribution. Compare US (21% federal + state), UK (19-25%), India (25%+) &mdash; Estonia is materially more cash-flow friendly for reinvestment-heavy businesses.</p>"
         "<p><strong>EU VAT:</strong> standard 20%, registration mandatory above EUR 40K turnover for most activities. Reverse-charge for most B2B EU-cross-border services.</p>"),
        ("/ Setup via e-Residency", "Timeline and cost.",
         "<ol>"
         "<li><strong>e-Residency application</strong> at e-resident.gov.ee. EUR 100-120. 1-3 months processing. Pickup at Indian consulate.</li>"
         "<li><strong>Choose a Service Provider</strong> &mdash; Xolo, Enty, 1Office, Companio, LeapIN. These provide registered Estonian address + accounting + legal representation. EUR 20-100/month.</li>"
         "<li><strong>Incorporate the OU</strong> &mdash; done online via e-Business Register. State fee EUR 265. Minimum share capital EUR 2,500 (can be deferred for up to 10 years for most activities).</li>"
         "<li><strong>Bank account</strong> &mdash; the hard part. Estonian banks (LHV, SEB, Swedbank) have tightened KYC and generally decline non-resident founders without physical visit. Alternatives: Wise Business (EU IBAN, remote), Payoneer, Payhawk, Finom, Jeeves. For high-volume transactions, Wise Business handles well.</li>"
         "<li><strong>EU VAT registration</strong> if applicable.</li>"
         "<li><strong>FEMA ODI</strong> on India side.</li>"
         "</ol>"
         "<p>Total setup time including e-Residency approval: 3-5 months. Incorporation itself (post e-Residency) is 1-2 days.</p>"),
        ("/ Where Estonia OU fits", "And where it does not.",
         "<p><strong>Good fit:</strong></p>"
         "<ul>"
         "<li>Digital-only business: SaaS, consulting, content, agency services.</li>"
         "<li>EU customer base needing VAT invoice from EU vendor.</li>"
         "<li>Reinvestment-heavy &mdash; profits plowed back into product + growth.</li>"
         "<li>No physical goods / inventory.</li>"
         "<li>Founder comfortable with Wise Business as primary banking.</li>"
         "</ul>"
         "<p><strong>Poor fit:</strong></p>"
         "<ul>"
         "<li>US-VC-funded startup &mdash; Delaware wins.</li>"
         "<li>Physical goods / fulfillment / warehousing &mdash; needs operations near customers.</li>"
         "<li>Need traditional banking relationship with letter of credit / trade finance &mdash; Estonian banks reject non-residents.</li>"
         "<li>Regulated activity (payments, lending, investment management) &mdash; EU licensing complex from Estonia.</li>"
         "<li>Large employee base needing EU work permits &mdash; different pathway.</li>"
         "</ul>"),
    ],
    faqs=[
        ("Does Estonia e-Residency give me EU residence or citizenship?",
         "No. e-Residency is purely a digital identity for business purposes. It does not grant you EU residence, EU citizenship, Schengen visa access, or any right to live or work in EU. You remain Indian tax resident unless you physically relocate and meet another EU country's residence rules."),
        ("Is Estonia OU tax-free for Indian founders?",
         "Not tax-free &mdash; but tax-deferred. Estonia OU pays 0% on retained / reinvested earnings and 20% on distributed dividends. The Indian shareholder pays Indian tax on received dividends (slab rate or Section 115A 20%) with FTC under India-Estonia DTAA. Net Indian tax is often 5-15% depending on income bracket, but the deferral is valuable: no tax while profits remain in the company."),
        ("Can I open a bank account for my Estonia OU from India?",
         "Not easily with traditional Estonian banks (LHV, SEB, Swedbank) &mdash; they typically require physical visit and non-residents often rejected. Fintech alternatives work: Wise Business, Payoneer, Payhawk, Finom, Jeeves &mdash; all fully remote with EU IBAN. For most Indian founders Wise Business is the practical choice."),
        ("What is the minimum share capital for Estonia OU?",
         "EUR 2,500. For most activities, you can incorporate with EUR 0 upfront and defer the share-capital contribution up to 10 years (with specific restrictions). This makes Estonia OU effectively zero-capital friendly for digital-only startups."),
        ("Does India have a DTAA with Estonia?",
         "Yes. The India-Estonia DTAA (effective 2011) provides for reduced rates on dividends (10%), interest (10%), royalties (10% / 20% depending). FTC available for Indian shareholder on Estonia withholding tax."),
        ("Does BQP handle Estonia OU setup?",
         "Yes, with a local Estonian Service Provider partnership. We handle e-Residency application coaching, OU incorporation co-ordination, VAT registration, Wise Business account introduction, FEMA ODI on India side. Standard package EUR 1,500 setup + EUR 500/year ongoing. Request via get-a-quote.html."),
    ],
    related=[
        ("overseas-incorporation-guide-indian-founder.html", "Pillar", "Overseas Incorp Pillar"),
        ("uk-incorporation-indian-founder.html", "Guide", "UK Ltd (compare)"),
        ("us-incorporation.html", "Guide", "US (compare)"),
    ],
    cta_headline="Estonia OU fits ~10% of Indian founders. Scoping tells you if you are one.",
    cta_body="Digital-only, EU customers, reinvestment-heavy, no need for traditional banking &mdash; that is the profile. We scope Estonia vs UK vs Delaware honestly, handle e-Residency application + OU incorporation + Wise onboarding + FEMA ODI. Package from EUR 1,500.",
))

# 6. Hong Kong for Indian founder
write_page("hong-kong-incorporation-indian-founder", page(
    slug="hong-kong-incorporation-indian-founder",
    title="Hong Kong Incorporation for Indian Founders 2026 | Setup, Tax - BQP",
    description="Hong Kong Private Limited incorporation for Indian founders: 16.5% profits tax, 0% on foreign-source income, two-tier rate first HKD 2M, banking challenges post-2020, Companies Registry. CA guide.",
    keywords="Hong Kong incorporation India, HK Private Limited Indian founder, Hong Kong profits tax 16.5%, HK offshore claim, HK bank account difficulty, HSBC HK Indian business",
    hero_kicker="/ Overseas incorporation &middot; Hong Kong",
    hero_title_html="Hong Kong for Indian founders, <em>a thinner case than before.</em>",
    hero_lead="Hong Kong was historically a top-tier overseas incorporation choice for Indian founders doing China trade or Asia-Pacific business. Post-2020 the case has thinned: banking is harder, political uncertainty is higher, mainland-China operations are riskier. For specific use cases (0% tax on genuine offshore income, legacy Asia operations) it remains viable.",
    sections=[
        ("/ HK Private Limited basics", "Companies Registry mechanics.",
         "<p><strong>Private Company Limited by Shares:</strong></p>"
         "<ul>"
         "<li>Minimum 1 director (no HK residence requirement, but a HK-resident company secretary is required).</li>"
         "<li>Minimum 1 shareholder.</li>"
         "<li>Minimum share capital HKD 1 (no concept of paid-up capital minimum in practice).</li>"
         "<li>HK registered office required.</li>"
         "<li>HK-resident Company Secretary required &mdash; typically outsourced to a licensed CSP (Corporate Services Provider), HKD 5,000-15,000/year.</li>"
         "<li>Annual return filing with Companies Registry.</li>"
         "<li>Annual audit mandatory for all HK private companies regardless of turnover (unique globally).</li>"
         "</ul>"),
        ("/ HK profits tax", "Two-tier and the offshore claim.",
         "<p><strong>Two-tier profits tax (effective 2018):</strong></p>"
         "<ul>"
         "<li>First HKD 2 million of profits: 8.25% (corporations) or 7.5% (unincorporated).</li>"
         "<li>Above HKD 2 million: 16.5% (corporations) or 15% (unincorporated).</li>"
         "</ul>"
         "<p><strong>The offshore claim:</strong> HK operates a territorial tax system. Only profits sourced in HK are taxable. Profits from genuine offshore operations (contracts negotiated and concluded outside HK, services performed outside HK, goods bought and sold outside HK) are <em>not taxable</em> in HK.</p>"
         "<p>The offshore claim is made in the Profits Tax Return &mdash; IRD scrutinises it heavily. Documentation of where contracts were negotiated, who signed, where services were performed is critical. A HK Ltd with HK-based director, HK office, HK employees generally cannot sustain an offshore claim.</p>"
         "<p><strong>No capital gains tax, no VAT, no withholding on dividends to shareholders.</strong></p>"),
        ("/ Setup and banking", "The hard part is banking.",
         "<ol>"
         "<li><strong>Name check</strong> at Companies Registry &mdash; HKD 100.</li>"
         "<li><strong>Appoint HK Company Secretary</strong> via a Corporate Services Provider &mdash; HKD 5-15K/year.</li>"
         "<li><strong>Incorporate</strong> &mdash; HKD 1,720 government fee + CSP service fee. 1-2 days online.</li>"
         "<li><strong>Business Registration Certificate</strong> from Inland Revenue Department &mdash; HKD 2,150/year or HKD 5,650/3-year.</li>"
         "<li><strong>Bank account</strong> &mdash; the actual bottleneck. HSBC, Standard Chartered, Bank of China (HK), DBS HK have all tightened KYC post-2020. Non-resident founders with no HK ties frequently rejected. Alternatives: ZA Bank (virtual, remote-friendly), Airwallex (fintech), Statrys (fintech), Neat (fintech). Allow 4-12 weeks and often multiple rejections before successful account opening.</li>"
         "<li><strong>FEMA ODI</strong> on India side.</li>"
         "</ol>"
         "<p>Total time: 1 week incorporation + 4-12 weeks bank account = 5-13 weeks realistic.</p>"),
        ("/ When HK still fits", "The remaining use cases.",
         "<p><strong>Good fit:</strong></p>"
         "<ul>"
         "<li>Trading business with mainland China customers / suppliers where HK is the standard counterparty.</li>"
         "<li>Services business with existing Asia-Pacific client base where HK Ltd is the historical structure.</li>"
         "<li>Family offices with legacy HK infrastructure (lawyers, banks, trustees).</li>"
         "<li>Business genuinely offshore in nature (contracts, operations, employees outside HK) &mdash; offshore claim sustainable at 0% HK tax.</li>"
         "</ul>"
         "<p><strong>Poor fit:</strong></p>"
         "<ul>"
         "<li>US-VC-track SaaS startup &mdash; Delaware.</li>"
         "<li>Pure digital business with EU / US customers &mdash; UK Ltd, Delaware, Estonia.</li>"
         "<li>New founder with no Asia network &mdash; bank-account friction is prohibitive.</li>"
         "<li>Political-exposure-sensitive founders &mdash; HK's status is contested post-2020.</li>"
         "</ul>"),
    ],
    faqs=[
        ("What is the HK profits tax rate for an Indian-founder HK Ltd?",
         "Two-tier: 8.25% on first HKD 2 million of profits, 16.5% above. If the HK Ltd's profits are genuinely offshore (contracts negotiated and performed outside HK), an offshore claim can be made for 0% HK tax &mdash; subject to IRD approval and documentation."),
        ("Is Hong Kong still a good jurisdiction for Indian founders in 2026?",
         "Thinner than before. The core advantages (low tax, strong banking, international hub) remain in principle but banking has tightened dramatically post-2020. For new Indian founders without existing HK ties, Singapore or UAE often serves the same purposes with better remote-setup experience."),
        ("Can an Indian founder be sole director of HK Ltd?",
         "Yes. HK has no residence requirement for directors or shareholders. However a HK-resident Company Secretary is required &mdash; this is handled by a Corporate Services Provider on a service basis for HKD 5,000-15,000/year."),
        ("What is the offshore profits claim in Hong Kong?",
         "A specific procedure where a HK Ltd declares that its profits derived during the year are from genuine offshore sources (outside HK). If accepted by IRD, those profits are 0% HK tax. Documentation requirements are heavy: evidence of where contracts were negotiated, who signed, where services were performed, where customers are. Not casual; needs preparation."),
        ("Can I open a HSBC HK business account as an Indian founder remotely?",
         "Historically yes, now very difficult. HSBC HK post-2020 has tightened to the point where new non-resident founder accounts are frequently rejected. Virtual banks (ZA Bank, Mox) are more remote-friendly. Fintech alternatives (Airwallex, Statrys, Neat) are the practical path."),
        ("Does BQP handle Hong Kong incorporation for Indian founders?",
         "Yes, with a HK Corporate Services Provider partnership. Formation, Business Registration, HK Company Secretary service, bank account introduction (Statrys / Airwallex typically), audit co-ordination, Profits Tax return + offshore claim support where applicable. Request via get-a-quote.html."),
    ],
    related=[
        ("overseas-incorporation-guide-indian-founder.html", "Pillar", "Overseas Incorp Pillar"),
        ("singapore-incorporation-indian-founder.html", "Guide", "Singapore (compare)"),
        ("uae-incorporation-indian-founder.html", "Guide", "UAE (compare)"),
    ],
    cta_headline="HK still works for specific trade / Asia-Pacific cases.",
    cta_body="For Indian founders with China trade, Asia-Pacific services, or legacy HK infrastructure, HK Ltd remains viable. For new founders without existing HK ties, Singapore or UAE is usually the better choice. Scoping call is free; we recommend honestly based on your facts.",
))

print("Batch E complete: 6 overseas incorporation pages written")
