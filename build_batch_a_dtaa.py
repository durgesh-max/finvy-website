# -*- coding: utf-8 -*-
"""Batch A: 5 India-X DTAA pages (UAE, UK, Singapore, Mauritius, Chile)."""
from build_lib import page, write_page

# 1. India-UAE DTAA
write_page("india-uae-tax-treaty-dtaa", page(
    slug="india-uae-tax-treaty-dtaa",
    title="India-UAE Tax Treaty (DTAA) 2026 | Rates, Articles, Form 10F - BQP",
    description="India-UAE DTAA rates and mechanics after UAE Corporate Tax 2023. Dividend 10%, interest 12.5%, royalties 10%. TRC, Form 10F, POEM considerations for Dubai holding companies owned by Indian founders.",
    keywords="India UAE DTAA, India UAE tax treaty, UAE withholding rates India, Dubai tax India founder, POEM UAE India, UAE corporate tax 2023, Form 10F UAE, India UAE treaty dividend rate",
    hero_kicker="/ Cross-border tax &middot; India-UAE DTAA",
    hero_title_html="India-UAE DTAA, <em>after UAE Corporate Tax.</em>",
    hero_lead="The India-UAE tax treaty (signed 1992, protocols 2007 and 2012) remains one of the most-used by Indian residents structuring outbound investment and family offices. UAE Federal Corporate Tax from June 2023 changed the economics materially &mdash; here is what the treaty still delivers, and what POEM means for your Dubai holdco.",
    sections=[
        ("/ Overview", "The treaty's role, before and after UAE CT.",
         "<p>Signed in 1992 and amended by protocols in 2007 and 2012, the India-UAE DTAA historically delivered two things to Indian residents: low Indian-side withholding on flows to the UAE, and a UAE jurisdiction that imposed no local corporate income tax. The combination made Dubai one of the most-used jurisdictions for Indian family offices, UHNI structures and outbound investment.</p>"
         "<p>The UAE Federal Corporate Tax (Federal Decree-Law 47 of 2022, effective 1 June 2023) introduced a 9% rate on profits above AED 375,000. The treaty still applies for its rate-reduction mechanics, but the UAE entity now pays real corporate tax &mdash; the structure must be re-priced.</p>"),
        ("/ Key articles &amp; rates", "What the treaty caps.",
         "<p><strong>Article 10 (Dividends):</strong> cap of 10% withholding. Indian domestic withholding on dividends to non-residents is 20%, so the treaty rate materially reduces outbound dividend flows from India to a UAE entity.</p>"
         "<p><strong>Article 11 (Interest):</strong> cap of 12.5% on cross-border interest. Specific carve-outs for government debt and central-bank-origin loans.</p>"
         "<p><strong>Article 12 (Royalties):</strong> cap of 10% on royalties. There is no separate FTS article in the India-UAE treaty &mdash; fees for technical services generally fall under Article 7 (business profits) unless attributable to a Permanent Establishment. This is a meaningful difference from the India-US and India-UK treaties where FTS is explicitly carved out.</p>"
         "<p><strong>Article 7 (Business profits):</strong> taxable only in the residence country unless there is a PE in the source country. An Indian company selling services to a UAE customer with no UAE PE is not UAE-taxable on those profits.</p>"
         "<p><strong>Article 4 (Residence):</strong> UAE individual residence requires 183 days of physical presence; UAE company residence is determined by place of effective management (POEM) &mdash; a key battleground for Indian family-office structures.</p>"),
        ("/ The POEM trap", "Why many Dubai holdcos fail Indian residency rules.",
         "<p>Indian tax law (Section 6(3), amended 2016) treats a foreign company as an Indian tax resident if its Place of Effective Management is in India during the relevant year. If the Indian revenue asserts POEM in India, the Dubai entity is taxed in India on worldwide income at Indian corporate rates &mdash; and the treaty cannot override this because the treaty rate applies only to cross-border flows between residents of different states.</p>"
         "<p>To defend POEM in UAE: UAE-resident directors (physically living and operating there), board meetings held in UAE with contemporaneous minutes, key business decisions actually made and recorded in UAE, UAE bank accounts operated from UAE, UAE office space with staff. Zoom board meetings from a Mumbai hotel room do not qualify. CBDT's 2017 POEM guidelines spell this out in detail.</p>"
         "<p>Many Dubai holdco structures built in 2010-2018 fail current POEM standards. The 2023 UAE Corporate Tax changes have also added UAE substance requirements under the Economic Substance Regulations, which help the POEM defence but require their own compliance.</p>"),
        ("/ Mechanics", "How to claim the treaty rate on Indian source payments.",
         "<p>For a UAE-resident entity receiving Indian-source dividends, interest or royalties and wanting the treaty-reduced rate at withholding:</p>"
         "<ol>"
         "<li>Obtain a <strong>UAE Tax Residency Certificate (TRC)</strong> from the UAE Ministry of Finance (renewed annually; usually processed in 1-3 weeks).</li>"
         "<li>File <strong>Form 10F</strong> electronically on the Indian income tax portal (mandatory from April 2023) by the UAE-resident recipient.</li>"
         "<li>Provide the Indian payer with the TRC + Form 10F + a no-PE declaration + treaty invocation letter referencing the specific article (Article 10 for dividends, etc.).</li>"
         "<li>The Indian payer then withholds at the treaty rate (10% for dividends) instead of the 20% domestic default.</li>"
         "<li>Keep contemporaneous documentation of UAE substance &mdash; POEM and ESR audits can look back several years.</li>"
         "</ol>"),
    ],
    faqs=[
        ("Does UAE Corporate Tax at 9% kill the Dubai holdco structure?",
         "No, but it changes the economics. A Dubai holdco now pays 9% UAE CT on profits above AED 375,000. For genuine operating income this is still often below Indian corporate tax (25-30%). Free Zone entities meeting Qualifying Free Zone Person conditions may retain 0% on qualifying income &mdash; but the rules are technical and the Federal Tax Authority scrutiny is real. Model the structure assuming 9% UAE CT by default."),
        ("What is POEM and why does it matter for my Dubai holdco?",
         "Place of Effective Management. Under Indian Section 6(3), a foreign company is treated as Indian tax resident if its POEM is in India &mdash; the India-UAE treaty does not override this residency determination. If POEM is asserted in India, the Dubai holdco is taxed in India on worldwide income. Genuine UAE substance (resident directors, UAE board meetings, UAE office, UAE staff) is the only defence."),
        ("Can I claim treaty benefits with just a UAE Free Zone licence?",
         "The free zone licence is evidence of registration but not of substance. A UAE TRC + Economic Substance Regulations (ESR) notification + genuine operational presence (lease, staff, bank activity) collectively establish UAE residence for treaty purposes. Shell structures with no substance face POEM assertion in India and treaty-benefit denial under GAAR."),
        ("Can an Indian individual with a Dubai Golden Visa claim UAE residency for the DTAA?",
         "Residency for DTAA purposes is a tax-residency question, not an immigration status. UAE requires 183 days of physical presence in a year for individual tax residency. A Golden Visa holder who spends most of the year in India is likely still an Indian tax resident and cannot claim UAE residence under the treaty."),
        ("Is capital gains on Indian shares taxable in a Dubai holdco?",
         "Under India-UAE DTAA Article 13 (as amended), capital gains on shares of Indian companies remain taxable in India in the hands of a UAE resident. The 2013 protocol closed the earlier planning window that used the treaty to avoid Indian capital gains. Plan on Indian LTCG/STCG applying regardless of Dubai holdco."),
        ("Does BQP structure Dubai-India setups?",
         "Yes &mdash; from new structures (with built-in POEM defence and ESR compliance) to audits of legacy structures where POEM exposure needs cleanup. For an existing Dubai holdco where you are concerned about POEM, we run a 90-day diagnostic that scores substance, identifies gaps, and gives you a remediation plan. Request via get-a-quote.html."),
    ],
    related=[
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("fema-odi-us-entity-indian-founder.html", "Guide", "FEMA ODI for Indian founders"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Running a Dubai holdco, or planning one?",
    cta_body="UAE Corporate Tax changed the math. We re-price existing Dubai structures against 9% CT, defend POEM with UAE substance evidence, handle Economic Substance Regulations compliance, and set up ESR-compliant new structures. 20-minute scoping call is free.",
))

# 2. India-UK DTAA
write_page("india-uk-tax-treaty-dtaa", page(
    slug="india-uk-tax-treaty-dtaa",
    title="India-UK Tax Treaty (DTAA) 2026 | Rates, Articles, Form 10F - BQP",
    description="India-UK Double Taxation Avoidance Agreement explained. Dividend caps 15% / 10%, interest 15% / 10%, royalties 15%, FTS 15% (make-available test). TRC, Form 10F, MFN clause, PE triggers. Working CA guide.",
    keywords="India UK DTAA, India UK tax treaty, UK withholding rates India, FTS India UK make available, India UK royalty rate, Form 10F UK, India UK capital gains, MFN clause India UK",
    hero_kicker="/ Cross-border tax &middot; India-UK DTAA",
    hero_title_html="India-UK DTAA, <em>rates, articles, mechanics.</em>",
    hero_lead="The India-UK tax treaty (signed 1993) is one of the most-used bilaterals for Indian service exporters, UK-based Indian promoters, and inbound UK investment into India. The FTS article uses a make-available test that controls how most IT and consultancy fees are taxed &mdash; getting it wrong triggers 15% withholding on gross receipts.",
    sections=[
        ("/ Overview", "A workhorse treaty, well-litigated.",
         "<p>The India-UK Double Taxation Avoidance Agreement was signed in 1993 and has seen protocols in 2013 (synthetic text post-MLI). It governs cross-border income between the two countries &mdash; most relevantly for Indian IT services exports to UK clients, UK-based NRIs with Indian investment income, Indian companies holding UK subsidiaries, and UK PE funds investing into India.</p>"
         "<p>The treaty is heavily litigated in India &mdash; characterisation of software, SaaS, back-office services, and management fees has produced a large body of case law. The <strong>make-available</strong> test in the FTS article is where most of the dispute happens.</p>"),
        ("/ Key articles &amp; rates", "What the treaty caps.",
         "<p><strong>Article 10 (Dividends):</strong> cap of 15% withholding for portfolio dividends; 10% where the beneficial owner is a company directly holding 10%+ of the paying company. UK generally does not withhold on outbound dividends domestically, so the treaty rate matters mainly for India-source dividend flows to UK recipients.</p>"
         "<p><strong>Article 11 (Interest):</strong> cap of 15%; 10% for interest paid to a UK bank or financial institution.</p>"
         "<p><strong>Article 12 (Royalties):</strong> cap of 15%.</p>"
         "<p><strong>Article 13 (Fees for Technical Services):</strong> cap of 15% &mdash; but only where the services <em>make available</em> technical knowledge, skill, know-how or processes to the recipient. Pure services that do not transfer technical capability to the recipient fall under Article 7 (business profits) with no Indian withholding if there is no Indian PE.</p>"
         "<p><strong>Article 7 (Business profits):</strong> taxable only in residence country unless attributable to a PE in the source country.</p>"
         "<p><strong>MFN clause:</strong> the India-UK treaty's FTS article is subject to a Most-Favoured-Nation protocol &mdash; if India agrees a lower FTS rate with another OECD member, the UK rate automatically steps down. This has been invoked in several Indian tribunal decisions.</p>"),
        ("/ The make-available test", "Where IT services and consulting cases hinge.",
         "<p>The India-UK FTS article defines fees for technical services as payments for services that <strong>make available</strong> technical knowledge, experience, skill, know-how or processes. If the service does not make such technical knowledge available to the recipient, it is Article 7 business profits.</p>"
         "<p>The Indian courts have held: training that transfers technique to the trainee is FTS. One-off consulting advice that is used and discarded is not FTS. SaaS where the user uses the software but does not learn how to build it is not FTS. Managed service agreements where the UK party operates the service for the Indian customer are typically not FTS.</p>"
         "<p>The practical implication: Indian IT services exports to UK clients that are structured as managed-service or outcome-based engagements (not training-and-transfer) typically fall under Article 7, triggering no Indian withholding when the UK vendor has no Indian PE. Many Indian clients still default to 15% FTS withholding out of caution and claim refunds later &mdash; this costs 15% of gross contract value as working capital for 12-24 months.</p>"),
        ("/ Mechanics", "The claim-the-treaty-rate checklist.",
         "<p>For an Indian resident paying FTS or royalty to a UK vendor and wanting to apply the treaty rate (15%) or the Article 7 nil rate:</p>"
         "<ol>"
         "<li>Obtain the UK vendor's <strong>UK TRC</strong> from HMRC (the UK equivalent of the Indian TRC).</li>"
         "<li>Obtain the vendor's <strong>Form 10F</strong> filed electronically on the Indian tax portal.</li>"
         "<li>Obtain a <strong>no-PE declaration</strong> if claiming Article 7.</li>"
         "<li>For FTS classification: review the contract. Does it make available technical knowledge to you? If not, document the Article 7 position with the SOW and deliverables.</li>"
         "<li>Deduct TDS at the treaty rate (15%) or nil under Article 7 as applicable. File Form 15CA and Form 15CB.</li>"
         "</ol>"
         "<p>The CA signing Form 15CB takes on the characterisation risk &mdash; most Indian CAs default to the conservative 15% withholding on anything that looks remotely technical. A properly-documented Article 7 position is defensible but requires a CA who understands the make-available test case law.</p>"),
    ],
    faqs=[
        ("What rate applies to UK vendor fees for pure services (no technology transfer)?",
         "If the services do not make available technical knowledge or know-how to the Indian recipient, the fees are Article 7 business profits &mdash; and if the UK vendor has no Indian PE, no Indian withholding applies. The vendor must provide a UK TRC, Form 10F, and a no-PE declaration. The Indian payer's CA must be comfortable signing Form 15CB on this basis."),
        ("How does the MFN clause work in the India-UK treaty?",
         "The India-UK treaty has a Most-Favoured-Nation clause in the FTS article: if India agrees a lower FTS rate with another OECD member country, the UK FTS rate automatically steps down to match. The Indian revenue has contested MFN auto-application in several cases, requiring an explicit notification to activate the lower rate. Current litigation and CBDT circulars should be checked before relying on an MFN-reduced rate."),
        ("Can an Indian IT company invoice UK clients without Indian withholding?",
         "The UK client is not an Indian payer and does not deduct Indian withholding. The Indian company reports the UK revenue in its Indian ITR and pays Indian corporate tax on it. UK withholding by the UK client is a different question &mdash; the UK does not generally withhold on service payments to overseas vendors."),
        ("Is capital gains on Indian shares taxable in a UK holding structure?",
         "Yes. Article 14 (capital gains) of the India-UK DTAA preserves India's right to tax capital gains on shares of Indian companies. UK PE funds and UK holding companies pay Indian LTCG or STCG on exits of Indian portfolio holdings. The GAAR + indirect-transfer rules can also apply."),
        ("What is Form 15CA and Form 15CB?",
         "Form 15CA is a self-declaration by the Indian remitter about the nature of the overseas payment and withholding applied. Form 15CB is a certificate from a Chartered Accountant certifying the characterisation and withholding rate. Both are filed on the Indian income tax portal before each cross-border remittance of INR 5 lakh+."),
        ("Does BQP handle India-UK vendor payments and treaty claims?",
         "Yes &mdash; both one-off (per-remittance 15CA/15CB) and ongoing (quarterly batches for Indian companies with recurring UK vendor payments). We also handle UK TRC co-ordination with the vendor and Form 10F filing. Standard pricing is per-remittance for small volumes and a monthly retainer for recurring payment programmes. Email durgesh@bharatquantumprospera.com or use get-a-quote.html."),
    ],
    related=[
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("india-uae-tax-treaty-dtaa.html", "Guide", "India-UAE DTAA"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="India-UK cross-border flows that need treaty positioning?",
    cta_body="For Indian IT services exporting to UK clients, UK PE funds investing in India, or Indian companies with UK vendor payments, correct treaty characterisation (make-available test, PE analysis, MFN) determines whether 15% or 0% applies. We structure the position and sign the Form 15CB.",
))

# 3. India-Singapore DTAA
write_page("india-singapore-tax-treaty-dtaa", page(
    slug="india-singapore-tax-treaty-dtaa",
    title="India-Singapore Tax Treaty (DTAA) 2026 | Post-2017 Protocol - BQP",
    description="India-Singapore DTAA after the 2017 protocol: end of capital-gains exemption, Limitation of Benefits (LOB), substance requirements. Dividend 10% / 15%, interest 15%, royalties / FTS 10%. CA-led guide.",
    keywords="India Singapore DTAA, India Singapore tax treaty 2017, LOB India Singapore, Singapore capital gains India, substance test LOB, Singapore fund India investment, India Singapore protocol",
    hero_kicker="/ Cross-border tax &middot; India-Singapore DTAA",
    hero_title_html="India-Singapore DTAA, <em>after the 2017 protocol.</em>",
    hero_lead="The India-Singapore treaty was the most-used route for foreign investment into India until the 2016 protocol closed its capital-gains exemption, mirroring the India-Mauritius change. The LOB substance test determines who still gets treaty benefits. For Singapore fund managers and holding structures investing in India, the rules changed materially.",
    sections=[
        ("/ Overview", "Three eras of the India-Singapore treaty.",
         "<p>The India-Singapore DTAA was signed in 1994 and became the workhorse for foreign investment into India after the 2000 protocol tied its capital-gains article to the India-Mauritius position. For a 20-year period, Singapore holdcos received Indian capital gains tax-free, mirroring Mauritius.</p>"
         "<p>The 2016 protocol (effective 1 April 2017) ended that regime. Shares of Indian companies acquired on or after 1 April 2017 are taxable on exit in India regardless of the Singapore residence of the seller. Shares acquired before are grandfathered. A transitional period 1 April 2017 to 31 March 2019 applied 50% of the Indian domestic rate; from 1 April 2019 full Indian rates apply.</p>"
         "<p>The protocol also introduced a Limitation of Benefits article: shell Singapore entities with inadequate substance lose treaty benefits even for the grandfathered period.</p>"),
        ("/ Key articles &amp; rates", "What the treaty caps today.",
         "<p><strong>Article 10 (Dividends):</strong> cap of 10% where the beneficial owner is a company directly holding 25%+ of the paying company; 15% in all other cases. Note Indian domestic dividend withholding is 20% for non-residents, so the treaty rate materially reduces outbound flows.</p>"
         "<p><strong>Article 11 (Interest):</strong> cap of 15%. 10% for interest paid to a Singapore bank.</p>"
         "<p><strong>Article 12 (Royalties and FTS):</strong> cap of 10%. The India-Singapore FTS definition does not use the make-available test (narrower than India-UK or India-US).</p>"
         "<p><strong>Article 13 (Capital gains, post-2017 protocol):</strong> Indian capital gains tax applies to shares of Indian companies acquired on or after 1 April 2017, regardless of Singapore residence. Shares acquired before are grandfathered, subject to LOB.</p>"
         "<p><strong>Article 24A (Limitation of Benefits):</strong> treaty benefits denied to Singapore entities that do not meet substance thresholds &mdash; broadly SGD 200,000+ annual Singapore expenditure in the 12 months preceding the gain, plus other indicators of genuine operations.</p>"),
        ("/ LOB substance test", "What Singapore substance actually means.",
         "<p>The LOB article (Article 24A, added by 2016 protocol) denies treaty benefits to a Singapore entity if it is a <em>shell</em> or <em>conduit</em>. Shell is defined with specific tests:</p>"
         "<ul>"
         "<li>Annual Singapore operating expenditure of less than SGD 200,000 in the 12 months preceding the claim.</li>"
         "<li>Primary purpose being to avail of treaty benefits.</li>"
         "<li>Negligible or no business operations in Singapore.</li>"
         "</ul>"
         "<p>Pass this and you keep treaty benefits even for post-2017 flows where the article allows them. Fail and even the grandfathered capital-gains exemption on pre-2017 shares can be denied.</p>"
         "<p>What qualifies as Singapore substance: office lease, local employees, Singapore directors genuinely making decisions, Singapore accounting and tax filings, Singapore bank operated from Singapore. Virtual office + nominee director + accounting outsourced to India does not pass. Many 2010-2015-vintage Singapore holdcos set up for Indian PE funds fail current LOB because substance was never built.</p>"),
        ("/ Mechanics", "Claiming the treaty position in India.",
         "<p>For a Singapore-resident entity receiving Indian source dividend, interest, royalty or FTS:</p>"
         "<ol>"
         "<li><strong>Singapore TRC</strong> from IRAS (Inland Revenue Authority of Singapore). Standard annual renewal.</li>"
         "<li><strong>Form 10F</strong> electronically on the Indian tax portal.</li>"
         "<li><strong>No-PE declaration</strong> if claiming Article 7.</li>"
         "<li><strong>LOB substance pack</strong>: Singapore P&amp;L showing SGD 200,000+ local expenditure, Singapore office evidence, director CVs, board minutes held in Singapore, Singapore bank statements.</li>"
         "<li>For post-2017 Indian share disposals: full Indian capital gains tax applies, structured through the Indian broker or counterparty withholding under Section 195.</li>"
         "<li>Grandfathered pre-2017 share disposals: capital gains exemption still available if LOB passed, documented in advance of the sale with ruling or Form 10F stack.</li>"
         "</ol>"),
    ],
    faqs=[
        ("Is capital gains tax still exempt for Singapore holdcos on Indian shares?",
         "Only for shares acquired before 1 April 2017 and only where the Singapore entity passes the LOB substance test (SGD 200,000+ annual Singapore expenditure, genuine operations). Shares acquired on or after 1 April 2017 face full Indian capital gains tax regardless of Singapore holding structure. The transitional half-rate for 1 April 2017 to 31 March 2019 acquisitions has expired."),
        ("What counts as SGD 200,000 of Singapore expenditure?",
         "Genuine operating expenditure booked in Singapore: office rent, Singapore employee salaries, local professional fees, Singapore audit fees, Singapore tax fees. Intra-group management fees paid to related parties are specifically excluded. The expenditure must be in the 12 months immediately preceding the treaty benefit claim."),
        ("Can I set up a new Singapore holdco today for Indian investment?",
         "Yes, but with eyes open. The treaty still delivers reduced withholding on dividends, interest, royalties and FTS where LOB is satisfied. It does NOT deliver capital gains exemption on new Indian equity. For Indian investment where the exit is equity sale, the Singapore route no longer saves Indian capital gains tax. For dividend/interest/royalty income flows, Singapore still works if you build genuine substance."),
        ("What is the GAAR interaction with the India-Singapore treaty?",
         "Indian General Anti-Avoidance Rules (GAAR) can override treaty benefits where the arrangement is primarily for tax avoidance. Even an LOB-compliant Singapore structure can be re-characterised by the Indian revenue under GAAR if the commercial rationale is weak. GAAR applies from 1 April 2017."),
        ("Is Singapore still useful for Indian PE and VC funds?",
         "Yes for operational and regulatory reasons: Section 13X / 13R fund tax incentives, MAS fund management licensing, familiar legal infrastructure for GP-LP arrangements. But the tax edge over direct India investment is thinner post-2017 and requires LOB-passing substance. Many India-focused funds have moved to GIFT City IFSC as a lower-friction alternative."),
        ("Does BQP structure Singapore-India flows?",
         "Yes. For existing Singapore holdcos we audit LOB compliance and build substance evidence before exits. For new structures we scope whether Singapore adds vs direct India vs GIFT City. For fund managers we handle Form 10F, TRC, LOB documentation and withholding tax position. Request via get-a-quote.html."),
    ],
    related=[
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("india-uae-tax-treaty-dtaa.html", "Guide", "India-UAE DTAA"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Running or planning a Singapore-India structure?",
    cta_body="Legacy structures need LOB substance audit before the next India exit. New structures need a honest LOB-vs-cost analysis before setup. We handle both: diagnostic for existing, scoping for new, and the ongoing documentation that defends the treaty position.",
))

# 4. India-Mauritius DTAA
write_page("india-mauritius-tax-treaty-dtaa", page(
    slug="india-mauritius-tax-treaty-dtaa",
    title="India-Mauritius Tax Treaty (DTAA) 2026 | Post-2016 Protocol - BQP",
    description="India-Mauritius DTAA after 2016 protocol: capital gains grandfathering, LOB tests, GAAR interaction. Dividend 5% / 15%, interest 7.5%, royalties 15%. Working CA guide for existing structures.",
    keywords="India Mauritius DTAA, India Mauritius tax treaty 2016, Mauritius capital gains India, grandfathering Mauritius India, LOB Mauritius, GAAR Mauritius India, Mauritius GBC fund India",
    hero_kicker="/ Cross-border tax &middot; India-Mauritius DTAA",
    hero_title_html="India-Mauritius DTAA, <em>what's left after 2016.</em>",
    hero_lead="The India-Mauritius treaty built most of India's modern inbound-FDI history. The 2016 protocol closed its capital-gains exemption for post-April-2017 Indian equity acquisitions. For structures still holding grandfathered pre-2017 shares and for the dividend/interest/royalty flows that remain, this is the current state.",
    sections=[
        ("/ Overview", "The treaty that built Indian FDI, then rewritten.",
         "<p>The India-Mauritius Double Taxation Avoidance Agreement was signed in 1982 and became the single most-used treaty for foreign investment into India. For 30+ years, it exempted Indian capital gains in the hands of Mauritius residents, which combined with Mauritius's own zero tax on such gains made it the default conduit for FDI and PE investment.</p>"
         "<p>The 2016 protocol ended the capital-gains exemption on Indian shares acquired on or after 1 April 2017. Pre-April-2017 acquisitions are grandfathered. A transitional 50%-rate window ran 1 April 2017 to 31 March 2019; from 1 April 2019, full Indian rates apply to post-protocol acquisitions.</p>"
         "<p>The protocol also added LOB tests, and GAAR (effective April 2017) sits on top of everything.</p>"),
        ("/ Key articles &amp; rates", "What the treaty still delivers.",
         "<p><strong>Article 10 (Dividends):</strong> cap of 5% where the beneficial owner is a company directly holding 10%+; 15% in all other cases. Material reduction from Indian domestic 20%.</p>"
         "<p><strong>Article 11 (Interest):</strong> cap of 7.5%.</p>"
         "<p><strong>Article 12 (Royalties):</strong> cap of 15%.</p>"
         "<p><strong>Article 13 (Capital gains, post-2016 protocol):</strong> Indian capital gains apply to shares acquired on or after 1 April 2017. Grandfathering for earlier acquisitions, subject to LOB.</p>"
         "<p><strong>LOB test:</strong> grandfathered benefits denied where the Mauritius entity is a shell &mdash; the substance test is similar to Singapore's but calibrated to Mauritius economic reality. Common benchmarks: a Category 1 Global Business Licence (now simply 'Global Business Licence' after 2019 reforms), genuine Mauritius directors, Mauritius operating expenditure, Mauritius-held board meetings.</p>"),
        ("/ Grandfathering mechanics", "What qualifies for the pre-2017 regime.",
         "<p>To claim grandfathered capital gains exemption on a post-protocol exit:</p>"
         "<ul>"
         "<li>The Indian shares being sold must have been acquired by the Mauritius entity before 1 April 2017.</li>"
         "<li>The Mauritius entity must have been in continuous existence as a Mauritius tax resident during the holding period.</li>"
         "<li>The entity must pass the LOB substance test at the time of the sale &mdash; not just at the acquisition.</li>"
         "<li>Documentation: Mauritius Global Business Licence (or evidence of former Category 1 status), Mauritius TRC for each year, Mauritius board minutes, operating expenditure records, local staff and office evidence.</li>"
         "</ul>"
         "<p>Many Indian PE and VC fund structures from 2008-2015 have grandfathered holdings in Indian portfolio companies waiting to be exited. Those exits need current-year LOB and GAAR analysis before closing.</p>"),
        ("/ GAAR + LOB + MLI", "Three overlapping tests to pass.",
         "<p>Even LOB-passing grandfathered structures can be denied benefits under Indian GAAR (applies from 1 April 2017) if the primary purpose test is failed. GAAR is triggered where the main purpose of the arrangement is to obtain tax benefit and the arrangement lacks commercial substance.</p>"
         "<p>Separately, the Multilateral Instrument (MLI) is in force between India and Mauritius since 2020 and layers a Principal Purpose Test (PPT) and additional anti-abuse provisions over the treaty text.</p>"
         "<p>Practical effect: a 2010-vintage Mauritius fund structure with grandfathered Indian equity holdings and no post-2016 substance build-out faces three sequential tests at exit &mdash; LOB (treaty), PPT (MLI), GAAR (Indian domestic). All three must be passed. Legacy structures that worked clean under pre-2017 rules often fail one or more of these today.</p>"),
    ],
    faqs=[
        ("Is capital gains tax still exempt for Mauritius holdcos on Indian shares?",
         "Only for shares acquired before 1 April 2017 and only where the Mauritius entity passes LOB substance (operating expenditure, genuine Mauritius activities, Global Business Licence) and PPT (MLI) and GAAR (Indian domestic). The three-filter test must be passed. Shares acquired on or after 1 April 2017 face full Indian capital gains tax."),
        ("What are the LOB expenditure thresholds for Mauritius?",
         "The India-Mauritius LOB does not specify a hard SGD-style dollar threshold. Instead it uses a facts-and-circumstances substance test: Mauritius Global Business Licence, Mauritius directors making decisions, Mauritius operating expenditure proportional to the structure's size, Mauritius bank operated from Mauritius. For a USD 100M portfolio holdco, expenditure in low tens of thousands USD per year is below reasonable substance. Verify with Mauritian local counsel."),
        ("Can I still use Mauritius for new Indian investment?",
         "For dividend/interest/royalty flows: yes, if LOB-passing substance is built. For capital gains on Indian equity: no longer. For Indian PE/VC fund structures, GIFT City IFSC is often the lower-friction current alternative."),
        ("What is the Multilateral Instrument (MLI) impact?",
         "MLI is in force between India and Mauritius since 2020. It adds a Principal Purpose Test (PPT) on top of the treaty's LOB &mdash; a treaty benefit can be denied under PPT where obtaining the benefit was one of the principal purposes of the arrangement. PPT is subjective and gives the Indian revenue broader authority than LOB alone."),
        ("Does Mauritius Global Business Licence prove substance?",
         "The Mauritius GBL (post-2019 reforms) requires minimum substance: core income-generating activities in Mauritius, local directors, local employees, local physical office. GBL on its own is necessary but not always sufficient for LOB under the India-Mauritius treaty &mdash; the LOB test looks at operational substance proportional to the structure, not just regulatory status."),
        ("Does BQP structure Mauritius-India positions?",
         "For existing Mauritius structures with grandfathered Indian equity, we run pre-exit LOB + PPT + GAAR diagnostics (90 days), build the substance evidence pack, and defend the treaty position if challenged. For new structures we honestly scope Mauritius vs GIFT City vs direct India. For fund managers we handle the ongoing Form 10F / TRC / documentation workstream. Request via get-a-quote.html."),
    ],
    related=[
        ("india-singapore-tax-treaty-dtaa.html", "Guide", "India-Singapore DTAA"),
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Sitting on grandfathered Mauritius-held Indian equity?",
    cta_body="Pre-exit diagnostics (LOB + PPT + GAAR) are the single most important workstream before an Indian portfolio exit. Legacy structures often fail current tests on substance. We audit, remediate, and defend &mdash; typically 60-90 days before the exit event.",
))

# 5. India-Chile DTAA
write_page("india-chile-tax-treaty-dtaa", page(
    slug="india-chile-tax-treaty-dtaa",
    title="India-Chile Tax Treaty (DTAA) 2026 | Rates, Articles, 2020 Treaty - BQP",
    description="India-Chile DTAA signed 2020, effective 2022. Rates on dividends, interest, royalties, FTS, mining-sector carve-outs. India's newest LatAm bilateral treaty &mdash; working CA guide.",
    keywords="India Chile DTAA, India Chile tax treaty 2020, Chile withholding India, India Chile mining treaty, India Chile FTS, Chile Indian company investment, Latin America India DTAA",
    hero_kicker="/ Cross-border tax &middot; India-Chile DTAA",
    hero_title_html="India-Chile DTAA, <em>India's newest LatAm bilateral.</em>",
    hero_lead="Signed in March 2020 and effective 1 January 2022, the India-Chile tax treaty is India's newest Latin American bilateral and the primary framework for Indian corporate investment in Chile's mining, agriculture and energy sectors. For Chilean investment coming into India (Chilean family offices, Chilean pension funds) it also sets predictable rules for the first time.",
    sections=[
        ("/ Overview", "A new treaty for a growing corridor.",
         "<p>The India-Chile Double Taxation Avoidance Agreement was signed on 9 March 2020 and entered into force in 2022. It is India's first comprehensive income-tax treaty with a Pacific Alliance country and reflects Indian interest in Chilean mining (lithium, copper), agribusiness and renewables, as well as growing Chilean sovereign-wealth and family-office interest in Indian equity and infrastructure.</p>"
         "<p>The treaty's rates and architecture are modern-OECD-aligned &mdash; low source-country withholding, make-available FTS, PE-based business profits, LOB and PPT built in from day one (not retrofitted via MLI).</p>"),
        ("/ Key articles &amp; rates", "What the treaty caps.",
         "<p><strong>Article 10 (Dividends):</strong> cap of 10% where the beneficial owner is a company directly holding 10%+; 15% in other cases.</p>"
         "<p><strong>Article 11 (Interest):</strong> cap of 10%. Specific exclusions for government and central-bank debt.</p>"
         "<p><strong>Article 12 (Royalties and FTS):</strong> cap of 10%. FTS uses a make-available test similar to the India-UK treaty.</p>"
         "<p><strong>Article 7 (Business profits):</strong> standard PE-based. An Indian company with Chilean customers but no Chilean PE is not Chilean-taxable on those business profits.</p>"
         "<p><strong>Article 13 (Capital gains):</strong> gains on shares of Chilean companies owning Chilean mining concessions or Chilean real estate may be taxed in Chile under domestic rules; portfolio equity gains follow source-country rules.</p>"
         "<p><strong>LOB and PPT:</strong> built into the treaty from inception rather than added via MLI. Chilean or Indian entities claiming treaty benefits must satisfy substance and purpose tests from day one.</p>"),
        ("/ Mining-sector specifics", "Why Chilean lithium matters to Indian capital.",
         "<p>Chile holds roughly 40% of global lithium reserves and is a leading copper producer. Indian strategic interest in Chilean lithium concessions has grown with India's electric-vehicle and battery-storage build-out. The India-Chile treaty structures a predictable tax framework for these flows.</p>"
         "<p>Specific points:</p>"
         "<ul>"
         "<li>Chilean mining concession gains can be Chilean-taxable even where the holding company is Indian &mdash; Article 13 preserves source taxation on real-property-rich entities.</li>"
         "<li>Chilean mining royalties paid to Indian technology licensors benefit from the 10% treaty cap (Chilean domestic withholding on royalties is 30% without treaty).</li>"
         "<li>Indian equipment supply contracts to Chilean mining operators: typically Article 7 business profits with no Chilean withholding if no Chilean PE.</li>"
         "<li>Indian engineering services to Chilean mining operators: FTS classification applies the make-available test. Pure consulting (no transfer of know-how) is Article 7.</li>"
         "</ul>"),
        ("/ Mechanics", "Claiming the treaty rate in India or Chile.",
         "<p>For Indian company receiving Chilean source dividend, interest, royalty or FTS:</p>"
         "<ol>"
         "<li>Obtain Indian TRC from Indian tax authority (Rule 21AB).</li>"
         "<li>File Form 10F electronically on the Indian income tax portal (also used for inbound-India flows under the treaty).</li>"
         "<li>Provide the Chilean payer with the TRC, Form 10F, and treaty invocation.</li>"
         "<li>Chilean payer applies the reduced withholding rate under domestic Chilean procedure.</li>"
         "<li>Indian company reports the Chilean income and claims foreign tax credit on Indian ITR against Indian corporate tax on the same income (Section 90 read with the treaty).</li>"
         "</ol>"
         "<p>For Chilean recipients of Indian income: the mirror process using Chilean TRC and Indian Form 10F. The Indian payer withholds at the treaty rate and the Chilean recipient claims FTC in Chile.</p>"),
    ],
    faqs=[
        ("Is the India-Chile DTAA fully in force?",
         "Yes. Signed 9 March 2020, entered into force in 2022, and effective for taxable years starting 1 January 2023 (Chile) and 1 April 2023 (India). Both countries have ratified and the treaty is fully operational."),
        ("Does the treaty cover Chilean mining royalties paid to Indian technology companies?",
         "Yes. Royalties under Article 12 are capped at 10% Chilean withholding (down from Chilean domestic 30% default) where the Indian recipient provides a Chilean TRC-equivalent process and Form 10F. The treaty-rate claim is made through the Chilean withholding agent."),
        ("Can Indian capital be deployed into Chilean mining via a holding company?",
         "Yes. Direct Indian company holding or an intermediate holding in Chile is both workable. The 2020 treaty's modern LOB/PPT means the structure must have genuine commercial substance &mdash; shell holding companies set up only to access the treaty rate face denial of benefits under PPT."),
        ("Does the India-Chile DTAA have LOB from day one?",
         "Yes. Unlike older Indian treaties (Mauritius, Singapore) that acquired LOB via 2016-2017 protocols or MLI, the India-Chile treaty was signed in 2020 with LOB and PPT built into the original text. Treaty benefits are substance-conditional from the first flow."),
        ("Is there a GIFT City / Chile angle for fund managers?",
         "GIFT City IFSC fund structures can invest into Chile under the India-Chile treaty. Combined with GIFT City's own tax incentives (Section 10(23FE), 10(4D), etc. where applicable) this is becoming the structure of choice for new Indian funds with Latin American allocations."),
        ("Does BQP structure India-Chile cross-border positions?",
         "Yes. For Indian corporates investing in Chilean operations (mining supply, services, equipment), we structure the Chilean entity, co-ordinate Chilean local counsel, handle the Indian ODI side (FEMA), and set up the treaty-rate withholding mechanics. For Chilean capital coming into India (family offices, pension funds) we handle the Indian-side Form 10F / treaty position. Request via get-a-quote.html."),
    ],
    related=[
        ("india-us-dtaa-withholding-rates.html", "Guide", "India-US DTAA Rates"),
        ("india-singapore-tax-treaty-dtaa.html", "Guide", "India-Singapore DTAA"),
        ("fema-odi-us-entity-indian-founder.html", "Guide", "FEMA ODI for outbound investment"),
    ],
    cta_headline="India-Chile corridor &mdash; mining, agribusiness, inbound equity?",
    cta_body="India's newest Latin America bilateral opened in 2022 and is still thinly serviced by Indian CA firms. We structure both outbound (Indian corporate into Chilean mining/agribusiness/energy) and inbound (Chilean family offices into Indian equity) under the treaty, co-ordinating with Chilean local counsel.",
))

print("Batch A complete: 5 India-X DTAA pages written")
