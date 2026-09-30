# -*- coding: utf-8 -*-
"""Batch 4: 3 glossary / definition pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- 18. What is FATCA --------
write_page("what-is-fatca", build_page(
    slug="what-is-fatca",
    title="What is FATCA? | Foreign Account Tax Compliance Act - BQP",
    description="FATCA explained: what it is, who it applies to, IGA India, Form 8938 vs FBAR, FFI compliance, and what Indian founders and US persons in India need to know.",
    keywords="what is FATCA, FATCA India, FATCA Form 8938, FATCA FBAR difference, FATCA IGA India, FFI compliance FATCA, US person FATCA India, FATCA withholding 30 percent",
    hero_kicker="DEFINITION · US TAX",
    hero_title_html="FATCA, <em>explained.</em>",
    hero_lead="The Foreign Account Tax Compliance Act reshapes how non-US banks handle US customers, how US persons abroad report their foreign accounts, and how India-US financial data now flows automatically. A working definition for founders and expats.",
    sections=[
        ("Overview", "What FATCA is and why it exists",
         "<p>FATCA (Foreign Account Tax Compliance Act) is US legislation enacted in 2010 as part of the HIRE Act. It has two prongs: (i) requires <strong>foreign financial institutions (FFIs)</strong> — non-US banks, custodians, investment funds — to identify their US-person customers and report those customers' accounts to the IRS, on pain of a 30% US withholding tax on their US-source payments if they don't; and (ii) requires <strong>US persons</strong> with foreign financial assets above certain thresholds to file <strong>Form 8938</strong> annually with their tax return, disclosing those assets. The intent is to close the historical gap where US persons could hide income and assets in non-US accounts.</p>"),
        ("India-US IGA", "How India implements FATCA",
         "<p>India and the US signed an Inter-Governmental Agreement (IGA) in 2015 (effective 2016). Under this Model 1 IGA, Indian financial institutions report US-person customer information to the Central Board of Direct Taxes (CBDT), which then automatically transmits the data to the IRS. This means: if you are a US person with an Indian bank account, mutual fund folio, PPF, EPF, or brokerage account, your Indian financial institution has been asking you to complete FATCA self-certification forms since 2016, and your account information has been flowing to the IRS annually.</p>"
         "<p>Reverse direction: US financial institutions similarly report Indian-resident customers' account information to the IRS, which shares it with CBDT. This is why the Indian tax department now has visibility into Indian residents' US brokerage and bank accounts without needing a specific request.</p>"),
        ("Form 8938 filing obligation", "The US person side",
         "<p>US persons must file Form 8938 (Statement of Specified Foreign Financial Assets) with their annual Form 1040 if their aggregate foreign financial assets exceed:</p>"
         "<ul>"
         "<li><strong>Unmarried, living in US:</strong> USD 50,000 on the last day of the year OR USD 75,000 at any point during the year</li>"
         "<li><strong>Married filing jointly, living in US:</strong> USD 100,000 / USD 150,000</li>"
         "<li><strong>Unmarried, living abroad:</strong> USD 200,000 / USD 300,000</li>"
         "<li><strong>Married filing jointly, living abroad:</strong> USD 400,000 / USD 600,000</li>"
         "</ul>"
         "<p>&quot;Specified foreign financial assets&quot; include foreign bank and brokerage accounts, foreign stock or securities held outside a US account, foreign partnership interests, and foreign hedge funds. Direct-held foreign real estate is NOT reportable on Form 8938 (though holdings through a foreign entity are).</p>"
         "<p>Penalty for failure to file Form 8938: USD 10,000 per year, escalating to USD 50,000 for continued failure after IRS notice.</p>"),
        ("Form 8938 vs FBAR", "Two filings, overlapping but different",
         "<p>FATCA Form 8938 and FBAR (FinCEN 114) are commonly confused. Both report foreign accounts but they are separate filings with separate authorities:</p>"
         "<table><thead><tr><th>Feature</th><th>Form 8938 (FATCA)</th><th>FBAR (FinCEN 114)</th></tr></thead><tbody>"
         "<tr><td>Authority</td><td>IRS</td><td>FinCEN (Treasury)</td></tr>"
         "<tr><td>Filed with</td><td>Form 1040 (tax return)</td><td>Separate BSA E-Filing System</td></tr>"
         "<tr><td>Threshold (in US)</td><td>USD 50k unmarried / USD 100k joint</td><td>USD 10k aggregate</td></tr>"
         "<tr><td>Threshold (abroad)</td><td>USD 200k unmarried / USD 400k joint</td><td>USD 10k aggregate</td></tr>"
         "<tr><td>Direct-held real estate</td><td>Not reportable</td><td>Not reportable</td></tr>"
         "<tr><td>Foreign hedge fund interest</td><td>Reportable</td><td>Not directly (unless custodial)</td></tr>"
         "<tr><td>Signature authority only (no interest)</td><td>Not required</td><td>Required</td></tr>"
         "<tr><td>Penalty base</td><td>USD 10k, escalating</td><td>USD 10k non-wilful, higher wilful</td></tr>"
         "</tbody></table>"
         "<p>A US person in India may need to file both, only FBAR, or neither depending on the fact pattern. Test both separately.</p>"),
    ],
    faqs=[
        ("Am I a US person for FATCA purposes if I have an OCI card?",
         "OCI (Overseas Citizen of India) is an Indian immigration status, not a US tax status. Having an OCI does not itself make you a US person. You become a US person via US citizenship, US green card, or meeting the substantial presence test in the US. Many OCI holders are US citizens (dual status) — check your specific status."),
        ("Does India-US FATCA IGA mean my Indian income is now taxable in the US?",
         "The IGA is information-sharing, not a change in tax law. If you are a US person, your worldwide income was already US-taxable before FATCA — FATCA just closed the enforcement gap. If you are only an Indian resident (not a US person), FATCA reporting flows are neutral for you."),
        ("What is a 'reportable account' under India-US FATCA?",
         "Any financial account maintained by an Indian financial institution held by a US person, or by an entity with substantial US ownership (25%+), is reportable. Types include savings accounts, current accounts, deposits, brokerage accounts, mutual fund holdings, insurance products with cash value. Reported annually via CBDT to IRS."),
        ("Do I have to file Form 8938 if I already file FBAR?",
         "Yes, if you exceed the Form 8938 thresholds. Both are separate filings. FBAR does not substitute for Form 8938 and vice versa. Many US persons in India need to file both. Content overlaps but the forms and authorities are distinct."),
        ("What is the 30% FATCA withholding?",
         "Foreign financial institutions that do not comply with FATCA (do not identify and report US customers) face a 30% withholding tax on US-source payments they receive (interest, dividends, sales of US securities). This is the enforcement mechanism that pushed FFIs worldwide to become FATCA-compliant. Every major Indian bank is FATCA-compliant."),
        ("Can I renounce US citizenship to escape FATCA?",
         "US citizens can renounce citizenship. Long-term residents can surrender green cards. But 'expatriation' for tax purposes triggers Section 877A — a deemed sale of all assets at expatriation date, with US tax on the built-in gains if net worth exceeds USD 2M or average annual net tax liability exceeds a threshold. Expatriation is a major decision — get advice before initiating."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="US person in India and unsure of the paper trail?",
    cta_body="FATCA + FBAR + Form 8938 + Schedule B + potential state filings — the overlapping US disclosure regime is dense. Missed filings compound quickly. BQP handles the full US-side compliance for US persons in India, from annual filings to cure of past non-filings.",
))

# -------- 19. What is PFIC --------
write_page("what-is-pfic", build_page(
    slug="what-is-pfic",
    title="What is a PFIC? | Passive Foreign Investment Company Rules - BQP",
    description="PFIC explained: how the IRS treats Indian mutual funds held by US persons, QEF and mark-to-market elections, Form 8621, and the punitive default treatment to avoid.",
    keywords="what is PFIC, PFIC Indian mutual funds, PFIC US person India, Form 8621, QEF election PFIC, mark to market PFIC, PFIC excess distribution, PFIC penalty, PFIC Indian ETF",
    hero_kicker="DEFINITION · US TAX",
    hero_title_html="PFIC, <em>the trap for Indian mutual funds.</em>",
    hero_lead="If you are a US person holding Indian mutual funds, ETFs, or a wide range of pooled investment vehicles, the PFIC regime turns what looks like a simple portfolio into one of the most punitive corners of the US tax code. Here is what applies and how to defuse it.",
    sections=[
        ("Overview", "What a PFIC is and why the rules are so harsh",
         "<p>A PFIC (Passive Foreign Investment Company) is a foreign (non-US) corporation that meets either the <strong>income test</strong> (75% or more of gross income is passive — interest, dividends, capital gains, rents, royalties) or the <strong>asset test</strong> (50% or more of assets produce passive income or are held for the production of passive income). Nearly every non-US mutual fund, ETF, and pooled investment vehicle meets one of these tests. The Congressional intent was to prevent US persons from deferring US tax on portfolio income by parking it in a foreign fund.</p>"
         "<p>The regime achieves this by making the default tax treatment so punitive that no rational US taxpayer would use a PFIC voluntarily. Ordinary income rates apply (not capital gains); tax is calculated with a compounding interest charge over the holding period; and it is nearly impossible to fully recover if you get the treatment wrong for several years.</p>"),
        ("What counts", "Common Indian holdings that are PFICs",
         "<ul>"
         "<li><strong>Indian mutual funds (equity, debt, hybrid, index):</strong> All are PFICs.</li>"
         "<li><strong>Indian ETFs:</strong> All are PFICs.</li>"
         "<li><strong>Indian ULIPs (unit-linked insurance plans):</strong> Usually PFICs.</li>"
         "<li><strong>PMS (Portfolio Management Services):</strong> Generally not PFICs if held via a segregated account with individual holdings (the underlying stocks are not PFICs), but structure-dependent.</li>"
         "<li><strong>AIFs (Alternative Investment Funds):</strong> Usually PFICs, depending on structure and income composition.</li>"
         "<li><strong>Direct-held Indian stocks:</strong> Not PFICs (individual company shares are not pooled investment vehicles).</li>"
         "</ul>"
         "<p>PPF and EPF are pension products, not investment funds — they are contentious but generally not treated as PFICs by mainstream practitioners. The Section 402(b) foreign pension trust analysis applies instead.</p>"),
        ("The three treatments", "Excess distribution, QEF, mark-to-market",
         "<p><strong>1. Default — Excess Distribution regime (Section 1291):</strong> The punitive baseline. Gains and 'excess distributions' (distributions above 125% of the average distribution over the prior 3 years) are allocated pro-rata across the entire holding period. Each year's allocation is taxed at the highest ordinary income rate for that year, plus an interest charge on the deemed deferred tax. Result: effective rates commonly 40-60% of the gain, with the interest component growing over time.</p>"
         "<p><strong>2. QEF election (Section 1295) — Qualified Electing Fund:</strong> The taxpayer includes their pro-rata share of the PFIC's ordinary earnings and net capital gains in taxable income each year, whether or not distributed. In exchange, subsequent distributions and gains get regular character (capital gains treatment for the net capital gains portion). Requires the PFIC to provide an annual PFIC Annual Information Statement. Most Indian mutual funds do NOT provide QEF statements, making this election unavailable in practice.</p>"
         "<p><strong>3. Mark-to-market election (Section 1296):</strong> Available only for PFICs that are 'marketable stock' — listed on a qualified exchange. Taxpayer recognises the annual increase in fair market value as ordinary income each year (and a limited loss on decrease). Not usually available for Indian mutual funds; may be available for Indian ETFs listed on NSE/BSE if the exchange is treated as qualified.</p>"),
        ("Form 8621", "What you file and when",
         "<p>Form 8621 (Information Return by a Shareholder of a PFIC or Qualified Electing Fund) is filed annually with the US tax return by any US person holding PFIC stock. One form per PFIC per year. If you hold 10 Indian mutual funds, that is 10 Form 8621s each year. Content depends on which regime you are under (default excess distribution, QEF, or mark-to-market).</p>"
         "<p>Failure to file Form 8621 generally suspends the statute of limitations on the entire tax return until the form is filed. This means the IRS has an indefinite window to reopen the year — a significant compliance risk for anyone unaware.</p>"),
    ],
    faqs=[
        ("Are Indian mutual funds always PFICs?",
         "Effectively yes. Every mainstream Indian mutual fund and ETF meets the income and asset tests. Holding any Indian mutual fund as a US person triggers PFIC treatment for that fund. Direct-held Indian stocks are not PFICs, so switching from mutual funds to individual stocks is a common restructuring recommendation for US persons in India."),
        ("What is the practical difference in tax cost between default and QEF treatment?",
         "For a fund gained materially over a multi-year holding, the default excess distribution regime can extract 50-60% of the gain in tax plus interest charges. QEF, if available, taxes annual earnings at capital gains rates for the net capital gains portion. Difference can be 20-30 percentage points of the gain, plus a much simpler compliance footprint."),
        ("Do Indian mutual funds provide QEF statements?",
         "Almost none do. Providing a PFIC Annual Information Statement requires the fund to calculate its income under US tax principles — a niche requirement that Indian fund houses have no incentive to meet. This effectively closes the QEF option for Indian mutual fund holders."),
        ("Can I mark-to-market Indian ETF holdings?",
         "Section 1296 mark-to-market is available for PFICs that are 'marketable stock' on a qualified exchange. Whether NSE/BSE qualify has been debated. Some practitioners take the mark-to-market position for NSE/BSE-listed ETFs on comparable-market analysis; others prefer the conservative default treatment. Take a defensible position with your preparer."),
        ("What happens if I sell a PFIC and never filed Form 8621?",
         "Under the default regime, the entire gain plus deemed prior-year allocations are subject to ordinary income rates plus interest charge in the year of sale. If Form 8621 was never filed in earlier years, the statute of limitations on those years remains open — the IRS can potentially reassess. The 'purge' election under Section 1298 can clean past non-filings in some cases."),
        ("Should I just avoid Indian mutual funds as a US person?",
         "For most US persons in India, yes — the compliance cost and tax friction outweigh the benefits. Common substitutes: individual Indian stocks (not PFICs), US-listed India ETFs (US-domiciled, no PFIC issue), or holding through a taxable US brokerage account with India exposure via US-listed instruments. Existing PFIC holdings should be reviewed for structured exit."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("fund-structuring.html", "Service", "Fund Structuring"),
    ],
    cta_headline="US person holding Indian mutual funds?",
    cta_body="PFIC is a live and expensive exposure for US persons in India who hold Indian mutual funds through NRO accounts, joint holdings, or inherited portfolios. BQP audits PFIC exposure, elects mark-to-market where defensible, and structures exit plans that minimise the excess distribution regime cost.",
))

# -------- 20. What is Form W-8BEN --------
write_page("what-is-form-w-8ben", build_page(
    slug="what-is-form-w-8ben",
    title="What is Form W-8BEN? | For Indian Residents and Entities - BQP",
    description="Form W-8BEN and W-8BEN-E explained: who provides which form, how to claim India-US treaty benefits, the difference from W-9, and common line-by-line traps.",
    keywords="Form W-8BEN, W-8BEN-E, W-8BEN India, W-8BEN vs W-9, W-8BEN treaty benefits, W-8BEN Indian founder, W-8BEN Stripe, W-8BEN Upwork, Form W-8BEN-E company",
    hero_kicker="DEFINITION · US TAX FORMS",
    hero_title_html="Form W-8BEN, <em>demystified.</em>",
    hero_lead="Every Indian founder, freelancer, or entity receiving payment from a US customer is asked for a W-8. Which version, how to fill it, and how to claim the reduced India-US treaty withholding rate — from a CA who fills these weekly.",
    sections=[
        ("Overview", "What Form W-8BEN does",
         "<p>Form W-8BEN (Certificate of Foreign Status of Beneficial Owner for United States Tax Withholding and Reporting) is used by non-US individuals to certify to a US payer that they are foreign persons, and to claim a reduced or nil withholding rate under a US tax treaty. Form W-8BEN-E is the equivalent for foreign entities. The forms replace the W-9 (used by US persons and entities). The US payer collects the W-8 before making a payment and applies the appropriate withholding rate based on the form's information.</p>"
         "<p>Without a W-8, the US payer defaults to 30% withholding on US-source income to a foreign recipient. With a properly-executed W-8 claiming India-US treaty benefits, withholding on many payment types drops to zero or a treaty-reduced rate.</p>"),
        ("W-8BEN vs W-8BEN-E vs W-9", "Which form for whom",
         "<table><thead><tr><th>Form</th><th>For whom</th><th>Purpose</th></tr></thead><tbody>"
         "<tr><td>W-9</td><td>US persons (citizens, residents, US entities)</td><td>Provide TIN to US payer; no withholding on services income</td></tr>"
         "<tr><td>W-8BEN</td><td>Non-US individuals</td><td>Certify foreign status; claim treaty benefits</td></tr>"
         "<tr><td>W-8BEN-E</td><td>Non-US entities (companies, LLCs, partnerships)</td><td>Certify foreign entity status; claim treaty benefits + FATCA classification</td></tr>"
         "<tr><td>W-8IMY</td><td>Foreign intermediaries and flow-through entities</td><td>Used by foreign partnerships and trusts</td></tr>"
         "<tr><td>W-8ECI</td><td>Non-US persons with US trade/business</td><td>Income effectively connected with a US trade/business</td></tr>"
         "</tbody></table>"
         "<p>An Indian individual receiving payment from a US customer completes W-8BEN. An Indian Pvt Ltd company receiving payment from a US customer completes W-8BEN-E. This is the most common source of confusion — the -E suffix distinguishes entities from individuals.</p>"),
        ("Line-by-line for Indian claimants", "The fields that matter",
         "<p><strong>W-8BEN (individual):</strong></p>"
         "<ul>"
         "<li><strong>Line 1:</strong> Full legal name (matching passport)</li>"
         "<li><strong>Line 2:</strong> Country of citizenship (India)</li>"
         "<li><strong>Line 3:</strong> Permanent residence address (Indian address; not a US address)</li>"
         "<li><strong>Line 5:</strong> US TIN if you have one (usually blank for Indian residents without ITIN)</li>"
         "<li><strong>Line 6:</strong> Foreign tax identifying number — your Indian PAN</li>"
         "<li><strong>Line 9:</strong> Country claiming treaty benefits — India</li>"
         "<li><strong>Line 10:</strong> Article and paragraph of the treaty being claimed (e.g., 'Article 12 for royalties' or 'Article 7 for business profits'), type of income, and reason for the reduced rate</li>"
         "</ul>"
         "<p><strong>W-8BEN-E (entity):</strong> The complexity increases materially. The critical fields are Chapter 3 FATCA classification (line 5 — usually 'Active NFFE' or 'Passive NFFE' for most Indian operating companies), and Part III treaty benefit claim (line 14 with treaty article, line 15 with special limitations if applicable). Get W-8BEN-E wrong and it delays or blocks payment for weeks.</p>"),
        ("How to claim India-US treaty benefits", "Article by article",
         "<p>The India-US DTAA article you invoke on line 10 (individual) or Part III (entity) depends on the type of income:</p>"
         "<ul>"
         "<li><strong>Article 7 (Business Profits):</strong> Most Indian services exporters with no US PE claim Article 7 for a nil withholding rate. SaaS revenue, consulting, IT services, professional services fall here if properly classified as business profits (not FTS or royalties).</li>"
         "<li><strong>Article 10 (Dividends):</strong> Claim 15% cap (25% domestic default). For 10%+ ownership by a company, reduced further to 15% under the same article.</li>"
         "<li><strong>Article 11 (Interest):</strong> Claim 15% cap.</li>"
         "<li><strong>Article 12 (Royalties and FIS):</strong> Claim 15% cap. Applies when the classification is genuinely royalty or Fee for Included Services (which requires the 'make available' test).</li>"
         "<li><strong>Article 22 (Other Income):</strong> Rarely used; residual category.</li>"
         "</ul>"
         "<p>Wrong article on line 10 results in the US payer applying wrong rate (or refusing to reduce at all). Getting the right article is the entire game.</p>"),
    ],
    faqs=[
        ("As an Indian freelancer on Upwork, which form do I file?",
         "W-8BEN. You are a non-US individual providing services from India. Complete W-8BEN with your Indian address, PAN as your foreign TIN, and claim Article 7 (Business Profits) on line 10 for nil withholding on your services income. Upwork's platform walks you through the fields; verify the treaty article claim is entered correctly."),
        ("Does W-8BEN expire?",
         "Yes. Generally valid from the date signed through the end of the third calendar year following (approximately 3 years). Also expires on any change in circumstances that affects the information provided. Provide a fresh W-8BEN to each US payer every 3 years or on any relevant change."),
        ("Do I need a US ITIN to complete W-8BEN?",
         "No. You do not need a US ITIN to complete W-8BEN as an Indian individual. Line 5 (US TIN) can be left blank. Line 6 (Foreign TIN) should be your Indian PAN. Some US payers request an ITIN unnecessarily — pushback is appropriate; W-8BEN is complete without one for treaty-claim purposes."),
        ("What is the difference between claiming Article 7 and Article 12?",
         "Article 7 (Business Profits) gives nil US withholding if you have no US permanent establishment. Article 12 (Royalties and FIS) caps withholding at 15%. If your income is genuinely business profits from services rendered outside the US, Article 7 is correct and gives the better outcome. If it is a royalty or FIS, Article 12 is correct and 15% withholding applies. Getting the classification right requires understanding both the contract terms and the Article 12(4) 'make available' test."),
        ("My US customer says they cannot accept W-8BEN and needs a W-9 — what do I do?",
         "This is incorrect. W-9 is only for US persons. If your customer is asking a foreign individual or entity for W-9, they have misclassified you and are about to withhold nothing (which puts them in default of IRS backup withholding rules). Explain the correct form applies. Provide the correct W-8BEN or W-8BEN-E. Reference the IRS instructions if needed."),
        ("Does completing W-8BEN eliminate my Indian tax obligation?",
         "No. W-8BEN affects only US withholding on US-source payments. Your Indian tax obligation on the same income is unchanged. You pay Indian income tax on the receipts as your total worldwide income (Indian residents), and claim Foreign Tax Credit for any US tax that was withheld on Form 67 with your ITR."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("international-expansion.html", "Service", "International Expansion"),
    ],
    cta_headline="Invoicing US customers and W-8BEN blocks the payment?",
    cta_body="A wrong W-8BEN classification can hold up a payment for weeks or trigger unnecessary 30% withholding. BQP prepares W-8BEN and W-8BEN-E, files the underlying Form 10F and TRC, and defends the treaty claim if the US payer or their bank pushes back.",
))

print("Batch 4 complete: 3 glossary pages written")
