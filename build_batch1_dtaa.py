# -*- coding: utf-8 -*-
"""Batch 1: 5 India-X DTAA treaty pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- 1. India-US DTAA --------
write_page("india-us-tax-treaty-dtaa", build_page(
    slug="india-us-tax-treaty-dtaa",
    title="India-US Tax Treaty (DTAA) Explained | Rates, Articles, Forms - BQP",
    description="India-US DTAA: withholding rates on dividends, interest, royalties and FTS, tie-breaker residency, Form 10F, Tax Residency Certificate. CA-led guide for Indian founders and investors.",
    keywords="India US DTAA, India US tax treaty, DTAA withholding rate USA, Article 12 India US, Form 10F India US, tax residency certificate India US, royalties DTAA India, FTS India US treaty, dividend withholding USA India, treaty benefits Form W-8BEN",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-US",
    hero_title_html="The India-US DTAA, <em>explained.</em>",
    hero_lead="Signed in 1989, this is the treaty that decides whether your US royalties, dividends, interest income, and technical fees are taxed at 30%, 15%, or nothing at all. A working CA guide for Indian founders, SaaS exporters and cross-border investors.",
    sections=[
        ("Overview", "What the India-US DTAA actually does",
         "<p>The India-US Double Taxation Avoidance Agreement is a treaty between two sovereign tax systems that decides which country gets to tax which slice of your cross-border income. When an Indian resident earns US-sourced income (or vice versa), both countries have a claim. The DTAA allocates that claim, caps withholding rates below domestic law, and gives you a credit mechanism so you are not taxed twice on the same rupee. For most Indian founders selling into the US, the treaty is what makes the economics workable. Without it, your SaaS revenue could face 30% US withholding on gross receipts, not net profit.</p>"),
        ("Key articles", "The four articles you will actually use",
         "<p><strong>Article 10 (Dividends):</strong> US withholding on dividends paid to an Indian resident is capped at 15% (portfolio) or 25% (default without treaty). Domestic US rate is 30%.</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 15% on cross-border interest, with narrower carve-outs for bank loans (10%) and government debt (exempt).</p>"
         "<p><strong>Article 12 (Royalties &amp; Fees for Included Services / FTS):</strong> The most contested article for Indian tech and consulting exporters. Cap of 15% on both royalties and FIS. The FIS definition uses the &quot;make available&quot; test — the service must transfer skill or know-how to the recipient, not merely provide a deliverable.</p>"
         "<p><strong>Article 4 (Residence &amp; Tie-Breaker):</strong> If both countries treat you as resident, the tie-breaker cascade runs: permanent home &rarr; centre of vital interests &rarr; habitual abode &rarr; nationality.</p>"),
        ("Applicability", "Who can actually claim treaty benefits",
         "<p>To claim treaty benefits as an Indian resident receiving US income, you need three things in hand: (i) an Indian <strong>Tax Residency Certificate (TRC)</strong> from your jurisdictional Assessing Officer under Section 90(4), (ii) <strong>Form 10F</strong> filed electronically on the Indian tax portal (mandatory from 2023 for all non-residents claiming DTAA relief in India, and used as supporting proof for US withholding agents too), and (iii) a properly executed <strong>Form W-8BEN</strong> (individuals) or <strong>W-8BEN-E</strong> (entities) given to your US payer, quoting the treaty article you rely on. Without any one of these, the US payer will withhold at the full 30% domestic rate — and getting a refund from the IRS takes 6–18 months.</p>"),
        ("How to claim in practice", "The mechanics of getting the reduced rate",
         "<p>The 3-step operational playbook we run for our clients:</p>"
         "<ol>"
         "<li><strong>Get your TRC</strong> annually from the Indian income-tax department. Application under Rule 21AB. Turnaround 15–45 days.</li>"
         "<li><strong>File Form 10F</strong> electronically each financial year (or when facts change). Do this BEFORE your US counterparty makes the first payment.</li>"
         "<li><strong>Deliver a W-8BEN-E</strong> to every US customer or payer, referencing the exact treaty article. For SaaS revenue where the payment is genuinely business profits (not royalties/FTS), the whole withholding disappears under Article 7 once the recipient has no US permanent establishment — but you must be able to defend that classification.</li>"
         "</ol>"
         "<p>On the Indian side, you then claim <strong>Foreign Tax Credit</strong> on Schedule TR of your ITR, capped at the Indian tax otherwise payable on the same income.</p>"),
    ],
    faqs=[
        ("Do I need both a TRC and Form 10F?",
         "Yes. The TRC is issued by the Indian tax department and proves you are an Indian resident. Form 10F is your own declaration filed on the Indian portal (electronic filing became mandatory from 2023). Both are required to claim treaty benefits in India, and W-8BEN-E in the US usually references them."),
        ("What is the withholding rate on US SaaS revenue paid to an Indian company?",
         "If genuinely business profits with no US permanent establishment, US withholding under Article 7 is nil — but the payer will only agree if you file W-8BEN-E and can defend the classification. If reclassified as royalties or FIS, the cap is 15% under Article 12. If no treaty invoked, US default is 30%."),
        ("What is the 'make available' test for FTS?",
         "Article 12(4)(b) of the India-US DTAA defines Fees for Included Services narrowly: the service must 'make available' technical knowledge, skill or process to the recipient, so they can use it independently later. A one-time deliverable that doesn't transfer skill is not FIS. This distinction has saved Indian IT and consulting exporters materially."),
        ("Can I claim foreign tax credit for US taxes paid on Indian ITR?",
         "Yes, under Section 90 read with the DTAA. You must file Form 67 on the Indian portal before your ITR due date, attaching proof of US tax paid (Form 1099, tax receipts, IRS transcripts). The credit is limited to the lower of the Indian tax on the same income or the actual US tax paid."),
        ("Is capital gains on US stocks taxed under the DTAA?",
         "Capital gains under Article 13 largely follows the source country rule, but for most portfolio holdings the treaty leaves taxation to the residence country. Indian residents pay Indian capital gains tax on US shares (LTCG at 12.5% above INR 1.25 lakh, STCG at slab rate). The US does not tax capital gains for non-resident aliens except for US real estate under FIRPTA."),
        ("What if the treaty rate is higher than the domestic Indian rate?",
         "You always get the lower of the treaty rate and the domestic rate — Section 90(2) of the Income Tax Act. Treaty is a ceiling, not a floor. If Indian domestic law taxes a particular income at 10% and the treaty allows 15%, the 10% applies."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("international-expansion.html", "Service", "International Expansion Advisory"),
    ],
    cta_headline="Structuring a US-India cash flow?",
    cta_body="If you receive US dividends, royalties, SaaS revenue, or investment income, the difference between a properly-claimed treaty position and a default 30% withholding is often 10-20% of your gross receipts. BQP handles the TRC application, Form 10F filing, W-8BEN-E, Form 67 and Schedule TR — end to end.",
))

# -------- 2. India-UAE DTAA --------
write_page("india-uae-tax-treaty-dtaa", build_page(
    slug="india-uae-tax-treaty-dtaa",
    title="India-UAE DTAA | Dubai Tax Planning for Indian Founders - BQP",
    description="India-UAE tax treaty explained: withholding rates on dividends, interest, royalties, capital gains position, POEM implications, and impact of UAE Corporate Tax 2023. CA-led guide.",
    keywords="India UAE DTAA, India UAE tax treaty, Dubai tax India, UAE corporate tax 2023, POEM India UAE, capital gains India UAE, withholding UAE dividends, family office UAE India, RAK ICC India, Dubai holding company",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-UAE",
    hero_title_html="India-UAE DTAA, <em>after Corporate Tax.</em>",
    hero_lead="The UAE introduced a 9% federal corporate tax in June 2023, changing the calculus for every Indian entrepreneur who set up a holding company in Dubai. What still works, what got clipped, and how the DTAA interacts with the new UAE CT regime — from a working CA.",
    sections=[
        ("Overview", "The treaty and the new landscape",
         "<p>The India-UAE DTAA was signed in 1992 (protocol amendments 2007, 2012) and remains one of the most widely-used treaties by Indian residents structuring outbound investment, family offices, and holding structures. Historically, its attractiveness rested on the UAE's zero-tax regime — a Dubai holdco paid no corporate tax, and the DTAA delivered low withholding into India. The introduction of UAE Federal Corporate Tax (Federal Decree-Law 47 of 2022, effective 1 June 2023) at 9% on profits above AED 375,000 changed the analysis materially. The treaty still applies, but the value it delivers must now be re-priced against a live UAE tax cost.</p>"),
        ("Key articles", "Rates and residence",
         "<p><strong>Article 10 (Dividends):</strong> Withholding capped at 10% of gross dividend. India applies this on repatriations to UAE shareholders; the UAE has no withholding on outbound dividends.</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 12.5% on cross-border interest. Special carve-outs for government and central bank debt.</p>"
         "<p><strong>Article 12 (Royalties):</strong> Cap of 10% on royalties. No separate FTS article &mdash; fees for technical services fall under Article 7 (business profits) unless attributable to a PE.</p>"
         "<p><strong>Article 4 (Residence):</strong> An individual is UAE-resident if physically present 183 days in a 12-month window; for a company, place of effective management (POEM) is decisive. This is where the trouble usually is.</p>"),
        ("Applicability", "The POEM trap for Indian founders",
         "<p>Indian tax law (Section 6(3), 2016 amendment) treats a foreign company as Indian tax resident if its <strong>Place of Effective Management is in India</strong> during the year. If you set up a Dubai holdco but continue to run it from your Bandra office &mdash; board meetings in India, key management decisions in India, key personnel in India &mdash; the Indian tax authority will assert POEM in India and tax the entire worldwide income of the Dubai entity at Indian corporate rates. The DTAA does not override POEM &mdash; it just says the treaty rate applies to the residual withholding, not that India cannot tax the entity as its own resident.</p>"
         "<p>To hold POEM in the UAE, you need: (i) genuine UAE-resident directors, (ii) board meetings held in UAE with minutes, (iii) key business decisions made in UAE, (iv) UAE office / substance, (v) UAE bank accounts operated from there.</p>"),
        ("How to claim in practice", "Getting the treaty rate on your Indian dividends",
         "<p>If your UAE holdco receives dividends from an Indian portfolio company or subsidiary, the Indian payer must withhold at the treaty-reduced rate. The playbook:</p>"
         "<ol>"
         "<li>Obtain a <strong>UAE Tax Residency Certificate</strong> from the UAE Ministry of Finance (renewed annually).</li>"
         "<li>File <strong>Form 10F</strong> electronically on the Indian tax portal referencing the UAE TRC.</li>"
         "<li>Provide the Indian payer with a no-PE declaration and treaty invocation letter.</li>"
         "<li>File your Indian ITR for the Dubai holdco (as a non-resident) declaring the Indian-source dividend and claiming treaty position.</li>"
         "</ol>"
         "<p>The 9% UAE CT on the Dubai entity's income is now a real cost. Free Zone entities meeting Qualifying Free Zone Person conditions may retain 0% on qualifying income, but the rules are technical and the Federal Tax Authority scrutiny is real. Plan around the new UAE CT before you plan around the DTAA.</p>"),
    ],
    faqs=[
        ("Does UAE Corporate Tax kill the Dubai holding structure?",
         "No, but it changes the arithmetic. A Dubai holdco now pays 9% UAE CT on profits above AED 375,000. For genuine operating income that's still often lower than Indian corporate tax. For pure holding companies with qualifying income (dividends from qualifying subsidiaries), Free Zone status can preserve 0% — but the conditions are strict and change frequently."),
        ("What is POEM and why does it matter?",
         "Place of Effective Management. Under Section 6(3) of the Indian Income Tax Act, a foreign company is treated as Indian tax resident if its POEM is in India. If asserted, the Dubai holdco is taxed in India on worldwide income. Genuine UAE substance — directors, board meetings, decisions, office, staff — is the only defence."),
        ("Can I claim treaty benefits without a UAE TRC?",
         "No. The Indian payer will not apply the reduced treaty rate without seeing a current-year UAE Tax Residency Certificate plus Form 10F. Without them, the default Indian withholding rate applies (20% on dividends to non-residents, sometimes higher)."),
        ("Is a RAK ICC or offshore UAE entity treaty-eligible?",
         "RAK ICC and other Offshore companies historically had ambiguous DTAA eligibility because they did not pay UAE tax. Post-2023 UAE CT changes reduce this ambiguity for taxable Free Zone/mainland companies. Offshore companies remain contentious — consult before relying on treaty benefits from an offshore structure."),
        ("Are capital gains on Indian shares taxable in a Dubai holdco?",
         "Under the India-UAE DTAA, capital gains on shares of Indian companies remain taxable in India (Article 13). The 2013 protocol closed the earlier planning window that used the treaty to sidestep Indian capital gains. Plan accordingly if the Dubai entity holds Indian equity."),
        ("How does the DTAA interact with Vivad se Vishwas or ongoing Indian assessments?",
         "The DTAA is a treaty right; it does not itself resolve pending Indian tax disputes. If the department has taken a position on POEM or beneficial ownership in your case, the treaty position is one input into resolution but not automatic. Litigation strategy plus MAP (Mutual Agreement Procedure) under Article 27 is the escalation path."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("gift-city.html", "Service", "GIFT City IFSC Setup"),
        ("international-expansion.html", "Service", "International Expansion"),
    ],
    cta_headline="Running a Dubai holdco or thinking about one?",
    cta_body="UAE CT changed the game. Whether you already have a Dubai entity or are planning one, the structure needs to be re-priced against the 9% CT, POEM defences hardened, and Free Zone qualifying status tested. BQP runs Dubai-India structuring end-to-end.",
))

# -------- 3. India-Singapore DTAA --------
write_page("india-singapore-tax-treaty-dtaa", build_page(
    slug="india-singapore-tax-treaty-dtaa",
    title="India-Singapore DTAA | Post-2017 Protocol, LOB, PPT - BQP",
    description="India-Singapore tax treaty after the 2016-2017 protocol: end of capital gains exemption, Limitation of Benefits, Principal Purpose Test, and current planning options for Indian founders.",
    keywords="India Singapore DTAA, Singapore tax treaty India, LOB Singapore treaty, capital gains Singapore India, 2016 protocol Singapore, Singapore holding company India, PPT Singapore India, MLI Singapore, fund manager Singapore India",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-SINGAPORE",
    hero_title_html="India-Singapore DTAA, <em>after the protocol.</em>",
    hero_lead="Once the workhorse structure for foreign investment into India, the treaty was rewritten by the 2016 protocol effective April 2017 — killing the capital-gains exemption Singapore holdcos relied on. What survived, what needs LOB compliance, and what the MLI adds.",
    sections=[
        ("Overview", "The treaty in three phases",
         "<p>The India-Singapore DTAA has had three lives. Phase 1 (2005 to 2016) mirrored the India-Mauritius treaty and exempted capital gains on Indian shares from Indian tax in the hands of Singapore residents. Phase 2 (April 2017 to March 2019) applied a grandfathering window plus half-rate transition. Phase 3 (April 2019 onwards) applies full Indian capital gains tax on shares of Indian companies acquired on or after 1 April 2017, subject only to Article 24A's Limitation of Benefits (LOB) safeguards. The Multilateral Instrument (MLI), effective for the treaty from 1 April 2020, layered the Principal Purpose Test (PPT) on top of everything. Structures need to satisfy both LOB and PPT to be defensible.</p>"),
        ("Key articles", "What still bites",
         "<p><strong>Article 10 (Dividends):</strong> Cap at 15% (Singapore withholding on outbound dividends is nil, so the burden is on the Indian side).</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 15% on cross-border interest. Special rate of 10% for banking loans.</p>"
         "<p><strong>Article 12 (Royalties):</strong> Cap of 10% on royalties and fees for technical services.</p>"
         "<p><strong>Article 13 (Capital Gains):</strong> Post-2017, shares of Indian companies acquired on or after 1 April 2017 are fully taxable in India in the hands of the Singapore resident. Pre-1-April-2017 acquisitions remain grandfathered.</p>"
         "<p><strong>Article 24A (LOB):</strong> Treaty benefits denied to shell entities that do not meet a bona fide business test or the 'expenditure test' (SGD 200,000 annual operational expenditure in Singapore in the preceding 24 months). This test is separate from and additional to PPT under MLI.</p>"),
        ("Applicability", "LOB and PPT — the two gates",
         "<p>Two independent tests decide whether a Singapore holdco actually receives treaty benefits today:</p>"
         "<p><strong>LOB (Article 24A):</strong> The Singapore entity must (i) have listed shares, or (ii) be a subsidiary of a listed Singapore parent, or (iii) demonstrate that the entity is not a 'conduit company'. The conduit test requires SGD 200,000 of operating expenditure in Singapore over the preceding 24 months. Rent, salaries, professional fees to Singapore-based staff count; intra-group management fees do not.</p>"
         "<p><strong>PPT (MLI):</strong> Even if LOB is passed, benefits are denied if obtaining the treaty benefit was one of the principal purposes of the arrangement. This is a subjective, facts-and-circumstances test administered by the Indian tax authority.</p>"
         "<p>Meeting one is not enough. Both must be satisfied on ongoing facts, tested year by year at the point of claiming the treaty position.</p>"),
        ("How to claim in practice", "The current playbook",
         "<p>For any Singapore structure claiming India treaty benefits today, the operational reality is:</p>"
         "<ol>"
         "<li>Obtain a <strong>Singapore Certificate of Residence</strong> annually from IRAS.</li>"
         "<li>File <strong>Form 10F</strong> in India for the Singapore entity each financial year.</li>"
         "<li>Maintain <strong>substance file</strong>: Singapore directors, board meetings held in Singapore with minutes, Singapore office and staff, Singapore books, evidence of SGD 200,000+ Singapore expenditure.</li>"
         "<li>Document the <strong>commercial rationale</strong> beyond tax — why Singapore for this business? (regional hub, ASEAN access, capital markets, talent). Written contemporaneously.</li>"
         "<li>For fund managers, consider <strong>Section 13X / 13R (now merged into Section 13O and 13U)</strong> approved fund structures that carry their own regulatory footprint and strengthen the substance argument.</li>"
         "</ol>"
         "<p>Singapore remains a serviceable jurisdiction for regional operating hubs, fund management, and IP holding. It is no longer a low-friction way to avoid Indian capital gains.</p>"),
    ],
    faqs=[
        ("Is the capital gains exemption for Singapore holdcos completely gone?",
         "For shares of Indian companies acquired on or after 1 April 2017, yes. Pre-April-2017 acquisitions are grandfathered and remain exempt. New investments made through Singapore holdcos face full Indian capital gains tax on exit."),
        ("What is the SGD 200,000 test under LOB?",
         "Article 24A(3) requires a Singapore claimant of treaty benefits to have made at least SGD 200,000 of expenditure on operations in Singapore in the immediately preceding 24 months. This filters out shell entities. Genuine operating expenses count; intra-group management fees do not."),
        ("Does MLI's PPT override the treaty?",
         "MLI's PPT rule is now grafted onto the treaty and can deny benefits even where the treaty article otherwise allows them, if obtaining the benefit was one of the principal purposes. Both LOB and PPT must be satisfied — LOB is objective, PPT is subjective."),
        ("Is Singapore still useful for holding Indian equity?",
         "For pre-2017 investments, yes (grandfathering). For new investments, the treaty value is limited to reduced withholding on dividends, interest, and royalties, plus regional hub benefits (Section 13O/U fund structures, treaty network across ASEAN). Not for capital gains."),
        ("How does India tax a Singapore VCC (Variable Capital Company)?",
         "The Indian revenue's position on VCC treaty eligibility remains untested. Sub-funds within a VCC are separate cells for Singapore tax purposes but the Indian characterisation is unsettled. Structuring should assume conservative treatment and build substance at the VCC and sub-fund level."),
        ("Is Section 13O / 13U approval enough substance for the LOB test?",
         "Section 13O / 13U approval by MAS carries regulatory footprint (compliance officer, fund administrator, minimum AUM) that goes toward substance, but the LOB expenditure test is a separate arithmetic check. Approved fund managers still need to demonstrate the SGD 200,000 expenditure threshold."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("gift-city.html", "Service", "GIFT City IFSC Setup"),
        ("fund-structuring.html", "Service", "Fund Structuring"),
    ],
    cta_headline="Reviewing a Singapore structure post-MLI?",
    cta_body="If you set up a Singapore holdco between 2010 and 2016, the substance requirements you originally satisfied are now insufficient. LOB, PPT, and current-year expenditure tests need to be re-run every year. BQP audits and restructures Singapore-India positions.",
))

# -------- 4. India-UK DTAA --------
write_page("india-uk-tax-treaty-dtaa", build_page(
    slug="india-uk-tax-treaty-dtaa",
    title="India-UK Tax Treaty (DTAA) | Withholding, Royalties, FTS - BQP",
    description="India-UK DTAA explained: withholding rates on dividends, interest, royalties and fees for technical services, MFN clause, tie-breaker residency. CA-led guide for founders and consultants.",
    keywords="India UK DTAA, India UK tax treaty, UK withholding India, royalties India UK, FTS India UK treaty, MFN clause India UK, permanent establishment India UK, IT services India UK, UK holding company India, offshore treaty India UK",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-UK",
    hero_title_html="India-UK DTAA, <em>working guide.</em>",
    hero_lead="Signed 1993, protocol amended 2013. For Indian IT services and consulting firms exporting to the UK, this treaty decides whether your fees face 20% UK withholding or nothing. The MFN clause and Article 13 (Royalties/FTS) are where the fights happen.",
    sections=[
        ("Overview", "What the treaty does",
         "<p>The India-UK DTAA covers taxation of cross-border income between two of the largest partner jurisdictions for Indian services exports. UK is India's third-largest trading partner for services, and the treaty is directly load-bearing for IT/ITES, engineering consulting, financial services, and cross-border employment. The treaty allocates taxing rights on income, caps withholding rates below domestic law (UK's 20% default withholding on royalties/FTS is capped at 15% by the treaty), and provides the residence country with a credit for tax paid in the source country.</p>"),
        ("Key articles", "The relevant tax cash flows",
         "<p><strong>Article 11 (Dividends):</strong> Cap of 15% for portfolio, 10% for holdings above 10%. UK has largely eliminated withholding on outbound dividends unilaterally, so the treaty binds mostly in the India-outbound direction.</p>"
         "<p><strong>Article 12 (Interest):</strong> Cap of 15%. Bank loan interest capped at 10%. Government debt exempt.</p>"
         "<p><strong>Article 13 (Royalties &amp; FTS):</strong> Cap of 15%. The FTS definition uses the &quot;make available&quot; test (similar in principle to the India-US treaty). Software licensing, cloud services, and cross-border professional services are the frequently-litigated categories.</p>"
         "<p><strong>MFN Clause (Protocol):</strong> India-UK treaty carries an MFN clause on the FTS definition — if India signs a subsequent treaty with an OECD member that has a narrower FTS scope, the narrower scope automatically applies to the UK treaty too. This has been actively litigated.</p>"
         "<p><strong>Article 4 (Residence):</strong> Standard tie-breaker cascade: permanent home &rarr; centre of vital interests &rarr; habitual abode &rarr; nationality.</p>"),
        ("Applicability", "The FTS classification battleground",
         "<p>For Indian IT and consulting firms invoicing UK customers, whether the fee is characterised as <strong>Article 7 business profits</strong> (nil withholding if no UK PE) or <strong>Article 13 FTS</strong> (15% cap) determines cash flow. HMRC has generally taken a narrower FTS view than the Indian revenue's expansive stance. The 'make available' test asks whether the service transfers technical knowledge, skill, experience, know-how or processes to the recipient in a way they can use independently afterwards.</p>"
         "<p>Recurring subscription services, hosted software, and one-time deliverables typically fall outside FTS on this test. Bespoke development where the customer retains ongoing capability may fall inside. Written scope of work matters materially — courts have decided characterisation on the SOW's language.</p>"),
        ("How to claim in practice", "The compliance sequence",
         "<p>For an Indian resident receiving UK-source income:</p>"
         "<ol>"
         "<li><strong>Get an Indian TRC</strong> (Section 90(4), Rule 21AB) each financial year.</li>"
         "<li><strong>File Form 10F</strong> electronically on the Indian portal.</li>"
         "<li><strong>File the UK Certificate of Residence request</strong> and provide it to your UK payer with the treaty article invocation.</li>"
         "<li>If UK tax was withheld, claim <strong>Foreign Tax Credit</strong> on your Indian ITR via Form 67, filed before the ITR due date.</li>"
         "<li>Maintain <strong>SOW and delivery evidence</strong> supporting the Article 7 business-profits characterisation, in case of Indian AO or HMRC scrutiny.</li>"
         "</ol>"
         "<p>For UK residents receiving Indian-source income, mirror-image compliance applies. Where MAP (Mutual Agreement Procedure) is needed, the treaty carries Article 27 and India-UK MAP outcomes are typically achieved in 24-36 months.</p>"),
    ],
    faqs=[
        ("What is the MFN clause and how does it help?",
         "The India-UK protocol carries a most-favoured-nation clause on the FTS definition. If India later signs a treaty with an OECD member using a narrower FTS scope, that narrower scope automatically applies to the India-UK treaty. Indian courts have invoked this to import narrower FTS definitions from later India-Portugal, India-Belgium and similar treaties."),
        ("Is UK software licensing revenue taxable in India as royalties?",
         "The Indian revenue's traditional position was yes; the Engineering Analysis Centre of Excellence Supreme Court ruling (2021) held that payments for shrink-wrap and cloud software are not royalties under the treaty definition. Indian source withholding on these payments is no longer required if the treaty definition applies."),
        ("Do I need a UK Certificate of Residence to claim treaty benefits in India?",
         "Yes. If you are a UK resident receiving Indian-source income, the Indian payer will only apply the reduced treaty rate against a valid UK CoR issued by HMRC plus Form 10F filed in India. Without them, default Indian withholding rates apply."),
        ("How is a UK LLP treated under the India-UK DTAA?",
         "UK LLPs are transparent for UK tax purposes. Indian treatment depends on whether the LLP has a permanent establishment in India and how the partners are characterised. Cross-border partnership taxation is unsettled — case-by-case analysis is needed, especially for professional services LLPs invoicing India."),
        ("Is cross-border employment income covered?",
         "Yes, under Article 16. Employment income is generally taxable in the country of work. Short-term secondments (under 183 days in a 12-month window) may retain home-country taxation if the employer is not resident in and does not bear the cost via a PE in the work country."),
        ("What about the UK's Digital Services Tax on Indian companies?",
         "DST is a UK domestic tax on gross revenue from UK users for search engines, social media, and online marketplaces (2%). It is not covered by the DTAA (not an income tax). Indian companies exceeding the thresholds pay it in addition to any income tax exposure."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("international-expansion.html", "Service", "International Expansion"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
    ],
    cta_headline="Invoicing UK customers or receiving UK dividends?",
    cta_body="The difference between Article 7 (no withholding) and Article 13 (15% withholding) on your UK invoicing is often the difference between a scalable services business and a working-capital drag. BQP handles the classification, TRC/CoR paperwork, Form 67, and MAP where needed.",
))

# -------- 5. India-Mauritius DTAA --------
write_page("india-mauritius-tax-treaty-dtaa", build_page(
    slug="india-mauritius-tax-treaty-dtaa",
    title="India-Mauritius DTAA | Post-2016 Protocol, Current Position - BQP",
    description="India-Mauritius tax treaty explained: end of capital gains exemption after the 2016 protocol, grandfathering rules, LOB safeguards, and current planning constraints. CA-led guide.",
    keywords="India Mauritius DTAA, India Mauritius tax treaty, 2016 protocol Mauritius, capital gains Mauritius India, GAAR Mauritius, Global Business License Mauritius, Mauritius holding company India, LOB Mauritius, treaty shopping Mauritius",
    hero_kicker="CROSS-BORDER TAX · DTAA · INDIA-MAURITIUS",
    hero_title_html="India-Mauritius DTAA, <em>after the protocol.</em>",
    hero_lead="For 33 years this treaty was the most-used vehicle for foreign investment into India. The 2016 protocol changed the economics. Grandfathering, transitional half-rate, and what remains of the Mauritius route for post-2017 investments.",
    sections=[
        ("Overview", "The 1983 treaty and its 2016 rewrite",
         "<p>Signed in 1983 and effective from 1985, the India-Mauritius DTAA exempted Mauritius residents from Indian tax on capital gains from the sale of Indian company shares. Combined with Mauritius's own zero tax on such gains, this made Mauritius the dominant conduit for FDI and private-equity investment into India — for years, over 40% of India's inbound FDI was routed through it. The 2016 protocol, effective 1 April 2017, ended that regime. Post-2017 acquisitions no longer enjoy the capital gains exemption. Pre-2017 acquisitions are grandfathered. The treaty still applies for dividends, interest, and royalties, but the reason most people used it is now gone.</p>"),
        ("Key articles", "What the current treaty allows",
         "<p><strong>Article 10 (Dividends):</strong> Cap of 5% for holdings above 10%, 15% otherwise. Given Mauritius has no domestic withholding on outbound dividends, the burden is on the Indian side.</p>"
         "<p><strong>Article 11 (Interest):</strong> Cap of 7.5% on cross-border interest.</p>"
         "<p><strong>Article 12 (Royalties):</strong> Cap of 15%.</p>"
         "<p><strong>Article 13 (Capital Gains, post-2016 protocol):</strong> Shares of Indian companies acquired on or after 1 April 2017 are taxable in India in the hands of the Mauritius resident. Transitional half-rate for the period 1 April 2017 to 31 March 2019 (50% of Indian domestic capital gains rate). Full Indian rate applies from 1 April 2019 onwards. Pre-1-April-2017 acquisitions remain grandfathered indefinitely.</p>"
         "<p><strong>Article 27A (LOB, added by 2016 protocol):</strong> Grandfathering benefits denied to shell entities that do not meet the 'main purpose' and 'bona fide business activities' tests. Requires expenditure of at least MUR 1,500,000 in Mauritius in the preceding 12 months.</p>"),
        ("Applicability", "Grandfathering and its limits",
         "<p>The grandfathering position looks generous but the LOB safeguard is real. A Mauritius entity claiming grandfathered capital gains exemption on pre-2017 acquisitions must still, at the time of the sale, satisfy:</p>"
         "<ul>"
         "<li>Bona fide business activities test (not a shell)</li>"
         "<li>Expenditure of at least MUR 1,500,000 (approximately USD 33,000) in Mauritius in the immediately preceding 12 months</li>"
         "<li>Not have its 'affairs arranged with the primary purpose of obtaining treaty benefits' (a GAAR-adjacent test)</li>"
         "</ul>"
         "<p>India's GAAR (General Anti-Avoidance Rule, effective 1 April 2017) sits on top and can override the treaty where the arrangement lacks commercial substance or was primarily tax-motivated. Structures set up in the 2010s that satisfied the treaty at the time may not survive current-day GAAR + LOB scrutiny at the exit event.</p>"),
        ("How to claim in practice", "For grandfathered positions and new setups",
         "<p>For a Mauritius entity claiming grandfathered capital gains exemption on a pre-April-2017 acquisition of Indian shares:</p>"
         "<ol>"
         "<li>Maintain a <strong>Mauritius Category 1 Global Business License</strong> (or the current post-2018 equivalent 'Global Business Company' status).</li>"
         "<li>Obtain <strong>Mauritius Tax Residency Certificate</strong> annually from the Mauritius Revenue Authority.</li>"
         "<li>Document <strong>MUR 1,500,000+ Mauritius expenditure</strong> in each preceding 12-month period.</li>"
         "<li>Hold <strong>board meetings in Mauritius</strong> with genuine local directors, minutes filed.</li>"
         "<li>Maintain <strong>commercial rationale</strong> documentation contemporaneous with the original investment.</li>"
         "</ol>"
         "<p>For any new investment into India routed via Mauritius: run the numbers assuming full Indian capital gains at exit. The treaty no longer delivers the exemption. Consider Singapore (LOB / PPT), Netherlands (participation exemption), or direct India investment depending on the fund structure.</p>"),
    ],
    faqs=[
        ("Is capital gains still exempt for pre-2017 Mauritius investments?",
         "Yes, grandfathered — but only if the LOB safeguards (Article 27A) are met at the time of sale, including the MUR 1,500,000 Mauritius expenditure test in the preceding 12 months. GAAR also sits on top and can override in commercial-substance cases."),
        ("What does the transitional half-rate mean?",
         "For shares acquired between 1 April 2017 and 31 March 2019, if sold, Indian tax applies at 50% of the domestic Indian capital gains rate. This transitional relief expired on 1 April 2019; sales after that face the full Indian rate regardless of acquisition date in this transitional window."),
        ("Does GAAR override the grandfathering?",
         "Potentially. If the Indian tax authority determines the arrangement lacks commercial substance or was primarily tax-motivated, GAAR can override treaty benefits even in grandfathered positions. Documentation of genuine commercial rationale contemporaneous with the original investment is the primary defence."),
        ("Is Mauritius still useful for African investment?",
         "Yes. Mauritius has a well-developed treaty network with African jurisdictions (Kenya, Ghana, South Africa historically), a mature offshore fund industry, and a strong regulatory framework via the FSC. For India-Africa or intra-Africa investment corridors, Mauritius remains serviceable. The 2016 protocol only changed the India-outbound capital gains position."),
        ("Can I still get 5% dividend withholding on Indian dividends?",
         "Yes, if the Mauritius entity holds 10% or more in the Indian company and satisfies the LOB test. Below 10%, the rate is 15%. Since Mauritius has no domestic withholding on outbound dividends, the treaty rate is effectively the total burden on the flow."),
        ("Is a new Mauritius setup for India investment still defensible?",
         "For dividend/interest/royalty flows, yes, provided you maintain LOB-compliant substance. For capital gains on Indian equity, no — the exemption is closed for new acquisitions. Any new structure needs a clear commercial reason beyond tax, contemporaneous documentation, and ongoing substance."),
    ],
    related=[
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("gift-city.html", "Service", "GIFT City IFSC Setup"),
        ("fund-structuring.html", "Service", "Fund Structuring"),
    ],
    cta_headline="Sitting on a pre-2017 Mauritius position?",
    cta_body="If you have pre-April-2017 Indian equity held through a Mauritius entity, the grandfathered exemption is only as good as your current-year LOB compliance and GAAR defence. Getting this right at the exit event is a nine-figure decision. BQP structures and defends Mauritius positions.",
))

print("Batch 1 complete: 5 DTAA pages written")
