# -*- coding: utf-8 -*-
"""Batch O: 20 trending-topic pages Oct 2026.

10 NRI pages + 10 foreign-company pages targeting what's genuinely
trending in late 2026 (post Finance Act 2024, post DPDP Act 2023,
post space/telecom FDI reforms, UPI/AA framework expansion).
"""
from build_lib import page, write_page

# ========== NRI PAGES (10) ==========

# 1. NRI Form 10F e-filing mandatory
write_page("nri-form-10f-e-filing-mandatory-india-2026", page(
    slug="nri-form-10f-e-filing-mandatory-india-2026",
    title="NRI Form 10F e-Filing Mandatory 2026 | PAN-less NRI Guide - BQP",
    description="Form 10F e-filing on Indian income tax portal mandatory post Oct 2023 for every NRI claiming DTAA treaty rate: electronic filing route, PAN-less registration for non-residents, TRC coordination, validity 1 year, consequences of non-filing. Complete 2026 practitioner's guide. CA Durgesh Chavda.",
    keywords="NRI Form 10F e-filing, Form 10F electronic India, PAN-less Form 10F NRI, Form 10F DTAA India, Form 10F mandatory 2026",
    hero_kicker="/ NRI Guide &middot; Form 10F &middot; Updated 2026-10-15",
    hero_title_html="Form 10F, <em>what every NRI claiming DTAA needs.</em>",
    hero_lead="Post October 2023, electronic Form 10F is mandatory on India's e-filing portal for every non-resident claiming a Double Taxation Avoidance Agreement (DTAA) treaty rate. CBDT's Notification 03/2022 followed by extensions and clarifications. Without Form 10F, DTAA relief denied; higher Section 195 TDS deducted. Here's the complete practitioner's guide for NRIs + foreign payees.",
    sections=[
        ("/ The e-Form 10F mandate", "What changed in 2023.",
         "<p>Earlier: Form 10F was a self-declaration by non-resident payee, submitted on plain paper to the Indian payer, kept in the payer's file. From 16 July 2022 (CBDT Notification 03/2022), Form 10F became electronic &mdash; must be filed on the Indian Income Tax e-filing portal (incometax.gov.in).</p>"
         "<p>Initial relaxation (October 2022 - March 2023, extended to September 2023): non-residents without an Indian PAN could continue to file manual Form 10F. Post 1 October 2023: full electronic filing mandatory for all non-residents claiming DTAA benefit.</p>"
         "<p><strong>CBDT clarified</strong> (via Notification/Circular July 2024): non-residents without Indian PAN can obtain a temporary online account on the Indian e-filing portal using their foreign Tax Identification Number + country of residence &mdash; and file electronic Form 10F from that account.</p>"),
        ("/ When Form 10F is required", "The use cases.",
         "<ul>"
         "<li><strong>Any payment from India to non-resident claiming DTAA treaty rate</strong>: dividend, royalty, FTS, interest, capital gain, service fee. See our <a href='form-15ca-15cb-foreign-remittance-india.html'>Form 15CA/CB guide</a>.</li>"
         "<li><strong>NRI filing Indian ITR</strong>: when claiming reduced tax rate under DTAA (e.g., long-term capital gains at treaty rate).</li>"
         "<li><strong>NRI claiming lower TDS deduction</strong>: when seeking refund of excess Section 195 TDS deducted at 20% default when treaty rate was 10-15%.</li>"
         "<li><strong>Foreign company receiving India-source income</strong>: dividend from Indian subsidiary, royalty from Indian licensee, service fee from Indian customer.</li>"
         "</ul>"
         "<p>Without Form 10F + TRC, Indian payer must apply Section 195 default rate (20%) or Section 206AA PAN-absent rate (20%+). No treaty relief.</p>"),
        ("/ What Form 10F contains", "The nine items.",
         "<ul>"
         "<li>Status of the taxpayer (individual / company / firm / other).</li>"
         "<li>Nationality / country of incorporation / registration.</li>"
         "<li>Taxpayer's Identification Number in home country (TIN / SSN / NIN / foreign PAN equivalent).</li>"
         "<li>Period for which residential status (per TRC) applies.</li>"
         "<li>Address in home country.</li>"
         "<li>Indian PAN (if available) or foreign TIN as substitute.</li>"
         "<li>Confirmation that the person is a tax resident of home country.</li>"
         "<li>Confirmation that beneficial ownership of income is with the declarant (anti-treaty-shopping provision).</li>"
         "<li>Signature of declarant (or authorised signatory for companies).</li>"
         "</ul>"
         "<p>Validity: Form 10F declaration is tied to the TRC date range &mdash; typically 1 year (TRCs are usually annual).</p>"),
        ("/ Non-PAN NRI route - step-by-step", "e-Filing without Indian PAN.",
         "<ol>"
         "<li>Visit India e-filing portal: <code style='font:400 12px Inter,system-ui,sans-serif;background:#f8f3e8;padding:1px 6px;border-radius:3px'>incometax.gov.in</code>.</li>"
         "<li>Click 'Register' as 'Taxpayer' &rarr; select 'Non-Resident Not Holding and Not Required to Have PAN'.</li>"
         "<li>Enter: name + date of birth + foreign TIN (passport number acceptable where no formal TIN) + country of residence + email + mobile.</li>"
         "<li>OTP verification on email + mobile.</li>"
         "<li>Login credentials created; account linked to foreign TIN.</li>"
         "<li>Navigate to 'e-File &rarr; Income Tax Forms &rarr; File Income Tax Forms &rarr; Form 10F'.</li>"
         "<li>Complete the 9 fields.</li>"
         "<li>Upload TRC from home country tax authority (scanned PDF).</li>"
         "<li>Submit with Aadhaar OTP (not required for non-residents) OR using the account-level digital signature if available.</li>"
         "<li>Acknowledgement number generated &mdash; retain + share with Indian payer.</li>"
         "</ol>"
         "<p>Form 10F now visible to Indian payer when they look up the non-resident's Indian tax profile for Form 15CB signing.</p>"),
        ("/ Common Form 10F mistakes", "Where NRIs trip.",
         "<ul>"
         "<li><strong>Missing TRC</strong>: Form 10F cannot substitute TRC. Both are needed. TRC = tax authority of home country confirms residence; Form 10F = non-resident's own declaration about residence + treaty eligibility + beneficial ownership.</li>"
         "<li><strong>Stale TRC/Form 10F</strong>: validity is calendar year (or TRC's stated period). Must be renewed annually. Common for Indian payer to use last year's Form 10F in the new FY &rarr; invalid.</li>"
         "<li><strong>Beneficial ownership issue</strong>: NRI claiming treaty benefit but income actually flows to someone else (treaty shopping). GAAR / principal purpose test may deny treaty benefit even with TRC + Form 10F.</li>"
         "<li><strong>Wrong country of residence</strong>: NRI has moved countries but TRC + Form 10F reflect old country. Must match current residence as of income accrual period.</li>"
         "<li><strong>Form 10F filed too late</strong>: Form 10F must be in place BEFORE Indian payer makes payment / files Form 15CB. Late filing = payer deducts at non-treaty rate; NRI must claim refund later.</li>"
         "<li><strong>Account not accessible</strong>: non-resident forgot login or lost email access. CBDT support slow; prevention via proper credential management.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Is Form 10F mandatory for NRIs in 2026?",
         "Yes - mandatory in electronic form on India's income tax e-filing portal for every non-resident claiming DTAA treaty rate on India-source income (dividend, royalty, FTS, interest, capital gain, service fee). Post 1 October 2023, no manual filing permitted. Non-residents without Indian PAN can register online as 'Non-Resident Not Holding and Not Required to Have PAN' and file Form 10F from that account."),
        ("Can an NRI file Form 10F without an Indian PAN?",
         "Yes. Register on India's e-filing portal (incometax.gov.in) using foreign TIN (or passport number where no TIN exists) + country of residence + email + mobile. OTP verification creates account. File Form 10F from that account. CBDT clarified this specific route in Notification/Circular July 2024."),
        ("What is the validity of Form 10F?",
         "Tied to the associated TRC - typically 1 year. Both must be refreshed annually. Form 10F stays filed on the portal; new one must be filed for each new FY where DTAA benefit continues to be claimed."),
        ("What happens if an NRI doesn't file Form 10F?",
         "DTAA treaty rate denied. Indian payer must apply Section 195 default rate (20%) or Section 206AA rate (20%+) where applicable. NRI can later claim refund by filing Indian ITR + Form 10F + TRC, but immediate TDS deduction is at higher rate."),
        ("Does Form 10F need to be in English?",
         "The India e-filing portal is in English. Form 10F is filled in English. Supporting TRC (from home country) can be in any language but English translation (certified) recommended for Indian payer / tax officer reference."),
        ("Does BQP help NRIs with Form 10F + TRC + DTAA claim?",
         "Yes - standard NRI advisory service. Form 10F e-filing (via NRI's own portal account or via BQP as authorised representative where applicable), TRC coordination from home country, DTAA treaty rate analysis, Form 15CB for Indian payer, refund claim via Indian ITR where applicable. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("form-15ca-15cb-foreign-remittance-india.html", "Guide", "Form 15CA/CB"),
        ("nri-dtaa-claim-practical-trc-form-10f.html", "Guide", "DTAA Practical"),
    ],
    cta_headline="NRI claiming DTAA treaty rate on India-source income?",
    cta_body="Form 10F electronic filing is mandatory post Oct 2023. BQP: Form 10F e-filing + TRC coordination + Form 15CB coordination with Indian payer + Indian ITR refund where applicable. Scope-based engagement.",
))

# 2. NRI Inheritance Indian Property
write_page("nri-inheritance-indian-property-tax-fema-2026", page(
    slug="nri-inheritance-indian-property-tax-fema-2026",
    title="NRI Inheritance of Indian Property 2026 | Tax, FEMA, Mutation Guide - BQP",
    description="NRI inheriting Indian property / assets from Indian parents or relatives: no inheritance tax, Section 56(2)(x) exemption, FEMA repatriation route (USD 1M/year limit), mutation + probate / succession certificate, capital gains on later sale (indexation + Section 54 reinvestment). Complete 2026 guide. CA Durgesh Chavda.",
    keywords="NRI inheritance Indian property tax, NRI inherited property India sale, FEMA repatriation inherited property, succession certificate NRI India, probate for NRI inherited property",
    hero_kicker="/ NRI Guide &middot; Inheritance &middot; Updated 2026-10-15",
    hero_title_html="NRI inheriting Indian property, <em>tax + FEMA + mutation in one guide.</em>",
    hero_lead="NRI inheriting immovable property / Indian financial assets / Indian bank balance from Indian parents or relatives &mdash; the sequence of actions, tax position, FEMA treatment, mutation / succession formalities, and eventual sale / repatriation. India has no inheritance tax, but mishandled succession formalities can block sale or repatriation for years. Here's the complete framework.",
    sections=[
        ("/ Tax treatment of inheritance", "No inheritance tax.",
         "<ul>"
         "<li><strong>India abolished estate duty in 1985</strong>. No inheritance tax / estate tax on Indian assets.</li>"
         "<li><strong>Section 56(2)(x) specifically exempts</strong> gifts under will or by way of inheritance &mdash; inherited property is not treated as 'Income from Other Sources' in NRI's hands.</li>"
         "<li><strong>No immediate tax liability</strong> at the time of inheritance. The property / asset moves into NRI's hands at its historical cost (for later capital gains purposes under Section 49(1): cost = cost in previous owner's hands + period held by previous owner counted for holding-period calculation).</li>"
         "<li><strong>Income from inherited property is taxable</strong> in NRI's hands post-inheritance: rental income, interest on inherited FD, dividend on inherited shares.</li>"
         "<li><strong>US estate tax</strong>: if NRI is US tax person, inherited Indian assets may be included in US estate for US estate tax purposes on NRI's own death &mdash; separate planning needed. See our <a href='nri-us-estate-tax-indian-assets.html'>US estate tax guide</a>.</li>"
         "</ul>"),
        ("/ Mutation + legal transfer", "What NRI must do.",
         "<ol>"
         "<li><strong>Death certificate</strong>: obtain from Municipal Corporation / Panchayat.</li>"
         "<li><strong>If deceased left a Will (testamentary succession)</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Original Will + witness confirmation.</li>"
         "<li>&nbsp;&nbsp;&mdash; Probate from Indian High Court if (a) deceased was Christian / Parsi / Jew, or (b) immovable property in Mumbai / Chennai / Kolkata (mandatory jurisdictional probate requirement). Elsewhere, probate optional for Hindu / Muslim / Sikh / Jain testators but strengthens title.</li>"
         "<li>&nbsp;&nbsp;&mdash; Timeline: 6-24 months for probate.</li>"
         "<li><strong>If no Will (intestate succession)</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Hindu Succession Act 1956 for Hindu / Buddhist / Jain / Sikh.</li>"
         "<li>&nbsp;&nbsp;&mdash; Indian Succession Act 1925 for Christian / Parsi / Jew.</li>"
         "<li>&nbsp;&nbsp;&mdash; Muslim Personal Law for Muslim.</li>"
         "<li>&nbsp;&nbsp;&mdash; Succession Certificate from District Court (for movable assets &mdash; bank balance, shares).</li>"
         "<li>&nbsp;&nbsp;&mdash; Legal Heir Certificate from Revenue Authority (for immovable property mutation).</li>"
         "<li>&nbsp;&nbsp;&mdash; Timeline: 6-18 months.</li>"
         "<li><strong>Mutation (immovable property)</strong>: application to Municipal Corporation / Revenue Department with death certificate + Will / Succession Certificate / Legal Heir Certificate + NOC from co-heirs + property documents. Mutation updates municipal records to NRI's name.</li>"
         "<li><strong>Bank / demat / MF transfer</strong>: with Succession Certificate + ID documents.</li>"
         "<li><strong>NRO account</strong>: NRI should have NRO account to hold inherited Indian funds. Operations limited to local use + repatriation under FEMA.</li>"
         "</ol>"),
        ("/ FEMA + repatriation", "Taking inherited money out of India.",
         "<ul>"
         "<li><strong>Inherited property / funds held in NRO account</strong>: fully permissible under FEMA.</li>"
         "<li><strong>Repatriation of inherited funds abroad</strong>: NRI can repatriate up to <strong>USD 1 million per FY</strong> (combined limit for all remittances from NRO / inheritance / sale proceeds) under FEMA Current Account Rules + Schedule III. Requires Form A2 declaration + Form 15CA + 15CB (CA certificate).</li>"
         "<li><strong>Documents for repatriation</strong>: proof of inheritance (Will / probate / succession certificate), source documentation (bank statements showing credit), tax clearance (ITR / assessment order where income involved).</li>"
         "<li><strong>Beyond USD 1M/year</strong>: requires RBI prior approval under FEMA Current Account Rules.</li>"
         "<li><strong>Inherited immovable property</strong>: can be held by NRI indefinitely. Sale proceeds repatriable up to USD 1M/year.</li>"
         "<li><strong>Agricultural land / plantation / farmhouse</strong>: NRI can INHERIT but cannot BUY. Can hold inherited agricultural land but with restrictions on sale (sale only to Indian resident).</li>"
         "</ul>"),
        ("/ Sale of inherited property + capital gains", "Later disposal.",
         "<ul>"
         "<li><strong>Capital gain calculation</strong>: sale price - indexed cost (indexation from original acquisition date by previous owner per Section 49(1) + Section 48).</li>"
         "<li><strong>Holding period</strong>: period held by previous owner + period held by NRI (combined). If combined &gt; 24 months (property), gain is Long-Term Capital Gain (LTCG).</li>"
         "<li><strong>LTCG tax rate</strong>: Finance Act 2024 changed - 12.5% without indexation OR 20% with indexation (whichever lower) for property acquired before 23 July 2024; 12.5% without indexation for property acquired after 23 July 2024.</li>"
         "<li><strong>STCG</strong>: at slab rate.</li>"
         "<li><strong>TDS under Section 195</strong>: buyer deducts 20% LTCG / 30% STCG from sale proceeds. Lower Deduction Certificate (LDC) available under Section 197. See our <a href='nri-india-property-ldc-lower-deduction-certificate.html'>LDC guide</a>.</li>"
         "<li><strong>Section 54 reinvestment exemption</strong>: if NRI reinvests LTCG in another residential property in India within 1 year back / 2 years forward (purchase) / 3 years forward (construction), LTCG exempt subject to limits.</li>"
         "<li><strong>Section 54EC bonds</strong>: INR 50 lakh in REC / NHAI / PFC / IRFC bonds within 6 months.</li>"
         "<li><strong>Section 54F</strong>: full LTCG exemption on sale of any long-term asset (not residential property) if NRI invests net consideration in one residential property in India.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Is there inheritance tax on Indian property for NRI heir?",
         "No - India abolished estate duty in 1985 and has no inheritance tax. Section 56(2)(x) Income Tax Act specifically exempts inheritance from being treated as 'Income from Other Sources'. NRI inheriting Indian property faces no immediate tax liability at inheritance; only future income from the property (rent, interest, dividend) + capital gains on later sale are taxable."),
        ("How does an NRI legally transfer inherited Indian property to their name?",
         "Depends on whether a Will exists. With Will: obtain probate from Indian High Court (mandatory for Mumbai/Chennai/Kolkata immovable; optional elsewhere for Hindu/Muslim/Sikh/Jain). Without Will: Succession Certificate from District Court (for movable) + Legal Heir Certificate from Revenue Authority (for immovable mutation). Timeline: 6-24 months. Then mutation with Municipal Corporation/Revenue Department updates records to NRI's name."),
        ("Can an NRI repatriate inherited Indian funds abroad?",
         "Yes - up to USD 1 million per FY (combined limit for all remittances from NRO account / inheritance / property sale proceeds) under FEMA Current Account Rules + Schedule III. Requires Form A2 declaration + Form 15CA + 15CB (CA certificate). Beyond USD 1M/year requires RBI prior approval. Inheritance documentation (Will/probate/succession certificate) must support the repatriation."),
        ("Can an NRI inherit agricultural land in India?",
         "Yes - NRI can inherit agricultural land/plantation/farmhouse. Cannot BUY new agricultural land (FEMA restriction). Can hold inherited agricultural land but sale restricted to Indian resident buyer (cannot sell to another NRI). This is a specific FEMA restriction - plan the sale accordingly."),
        ("What's the capital gain tax when NRI later sells inherited property?",
         "Under Section 49(1) + Section 48: cost = cost in previous owner's hands (indexed if applicable). Holding period = combined (previous owner + NRI). If > 24 months: LTCG. Post Finance Act 2024, LTCG rate: 12.5% without indexation OR 20% with indexation (whichever lower) for property acquired before 23 July 2024; 12.5% without indexation thereafter. Section 54 / 54F / 54EC reinvestment exemptions available."),
        ("Does BQP handle NRI inheritance of Indian property?",
         "Yes - end-to-end service: probate / succession certificate coordination, mutation with Municipal Corporation, Section 56(2)(x) tax position confirmation, NRO account setup if needed, Form 15CA/CB for repatriation up to USD 1M/year, capital gain calculation + Lower Deduction Certificate (Section 197) + Section 54 reinvestment planning if sale planned. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-selling-indian-property-capital-gains.html", "Guide", "NRI Property Sale"),
        ("nri-us-estate-tax-indian-assets.html", "Guide", "US Estate Tax"),
    ],
    cta_headline="Inherited Indian property as an NRI? Act in the right sequence.",
    cta_body="Probate / mutation / NRO account / FEMA repatriation / capital gain planning. BQP end-to-end for NRIs in US / UK / UAE / Singapore / EU. Scope-based engagement.",
))

# 3. NRI Gift to/from Indian relatives
write_page("nri-gift-indian-relatives-section-56-fema-2026", page(
    slug="nri-gift-indian-relatives-section-56-fema-2026",
    title="NRI Gift to / from Indian Relatives 2026 | Section 56 + FEMA Rules - BQP",
    description="NRI gift to Indian relatives and NRI receiving gift from Indian relatives: Section 56(2)(x) relative exemption, FEMA current / capital account treatment, LRS limit USD 250K/year outbound, NRO account treatment, documentation (gift deed), capital gains later. Complete 2026 practical guide. CA Durgesh Chavda.",
    keywords="NRI gift Indian relatives tax, NRI gift Section 56 India FEMA, NRI gift to parents, NRI gift deed India, gift to NRI from India FEMA",
    hero_kicker="/ NRI Guide &middot; Gifts &middot; Updated 2026-10-15",
    hero_title_html="NRI gifts, <em>both directions, Section 56 and FEMA.</em>",
    hero_lead="NRI gifting money / property to Indian parents or siblings &mdash; or receiving gift from Indian relatives &mdash; is governed by both Income Tax Section 56(2)(x) and FEMA. Properly structured: fully tax-exempt + FEMA-compliant. Mishandled: Section 56(2)(x) 'Income from Other Sources' at slab rate, or FEMA breach with compounding. Here's the complete practical framework.",
    sections=[
        ("/ Section 56(2)(x) - the tax layer", "The relative exemption.",
         "<p>Section 56(2)(x) of Income Tax Act taxes gifts (money / property / specified movable property) received by an individual above INR 50,000 aggregate in FY as 'Income from Other Sources' at slab rate. EXCEPT gifts from 'relatives' as defined.</p>"
         "<p><strong>'Relative' under Explanation to Section 56(2)(x) for an individual</strong>:</p>"
         "<ul>"
         "<li>Spouse</li>"
         "<li>Brother or sister (own)</li>"
         "<li>Brother or sister of spouse</li>"
         "<li>Brother or sister of either parent</li>"
         "<li>Any lineal ascendant or descendant (parents, grandparents, children, grandchildren)</li>"
         "<li>Any lineal ascendant or descendant of spouse (in-laws)</li>"
         "<li>Spouse of any of the above persons</li>"
         "</ul>"
         "<p><strong>Standard NRI scenarios</strong>:</p>"
         "<ul>"
         "<li>NRI son gifts to Indian parent &mdash; parent is 'relative', fully exempt.</li>"
         "<li>Indian parent gifts to NRI daughter &mdash; daughter's parent is 'relative', fully exempt.</li>"
         "<li>NRI sibling gift / inheritance &mdash; sibling is 'relative', fully exempt.</li>"
         "<li>NRI uncle / aunt / cousin / niece / nephew &mdash; uncle / aunt via blood (parent's sibling) is 'relative'; via marriage is NOT; cousin / niece / nephew is NOT 'relative'; taxable above INR 50K.</li>"
         "<li>NRI friend gift &mdash; NOT 'relative'; taxable above INR 50K.</li>"
         "</ul>"
         "<p>See our comprehensive <a href='section-56-2-x-gift-tax-india-2026.html'>Section 56(2)(x) guide</a>.</p>"),
        ("/ FEMA layer - outbound (NRI to Indian relative)", "Resident recipient.",
         "<ul>"
         "<li><strong>NRI remits money to Indian relative</strong>: foreign-source inflow. Credited to recipient's NRE / regular savings / NRO account depending on recipient's status.</li>"
         "<li><strong>For Indian resident recipient</strong>: cash gift credited to regular savings account. No FEMA restriction on receipt by resident Indian. Form A2 + supporting documentation (gift deed / affidavit) completed at AD bank.</li>"
         "<li><strong>Gift deed recommended</strong>: notarised gift deed from NRI donor to Indian recipient describing: donor's details + recipient details + amount + relationship + stamp duty on gift deed (varies by state, typically INR 500-5,000 for cash gift documentation).</li>"
         "<li><strong>For gifts above INR 2 lakh to resident Indian in cash</strong>: Section 269ST violation if cash; strongly prefer bank transfer. NRI gifting via wire = compliant.</li>"
         "<li><strong>Multiple remittances in a year</strong>: aggregate matters. Standard practice: gift via one or two consolidated remittances with clear gift deed documentation.</li>"
         "<li><strong>Immovable property gift from NRI to resident</strong>: via registered gift deed in India + stamp duty + registration. FEMA permits (gift of property to resident family member allowed).</li>"
         "</ul>"),
        ("/ FEMA layer - inbound (NRI receiving from Indian relative)", "Resident donor.",
         "<ul>"
         "<li><strong>Indian relative gifts money to NRI</strong>: outbound remittance from India. Governed by FEMA Current Account Rules + LRS (Liberalised Remittance Scheme).</li>"
         "<li><strong>LRS limit</strong>: USD 2,50,000 per Indian resident per FY. Covers all permitted current + capital account transactions.</li>"
         "<li><strong>LRS use for gift to NRI relative</strong>: specifically permitted under FEMA Master Direction on LRS &mdash; included in 'maintenance of close relatives abroad' + 'gift' as permitted purposes.</li>"
         "<li><strong>Documentation</strong>: Form A2 declaration + PAN + purpose code (CRG - current remittance for gift). Gift deed strengthens case.</li>"
         "<li><strong>TCS under Section 206C(1G)</strong>: 20% TCS on LRS remittance above INR 7 lakh in FY (post Finance Act 2024). See our <a href='tcs-20-foreign-remittance-lrs-india-2026.html'>TCS LRS guide</a>. Collected by remitting bank, creditable against Indian donor's income tax.</li>"
         "<li><strong>Immovable property gift from resident to NRI</strong>: Indian resident can gift immovable property (not agricultural land) to NRI relative via registered gift deed + stamp duty.</li>"
         "<li><strong>Shares / securities gift</strong>: resident can gift Indian securities to NRI relative via FC-TRS filing (shares transferred to NRI's NRO/NRE demat).</li>"
         "</ul>"),
        ("/ Documentation + best practice", "The paper trail.",
         "<ul>"
         "<li><strong>Written gift deed</strong>: for all material gifts, not just immovable property. Notarised at least; registered if immovable property.</li>"
         "<li>Content: donor name + address, recipient name + address, nature of gift (money / property / securities), amount or description, date, acceptance by recipient, witness signatures, consideration clause (voluntary / without consideration), relationship statement (critical for Section 56(2)(x) relative exemption).</li>"
         "<li><strong>Bank route</strong>: wire transfer / NEFT / RTGS / SWIFT. No cash for gifts above INR 2 lakh (Section 269ST).</li>"
         "<li><strong>Form 15CA + 15CB</strong>: for remittance out of India above INR 5 lakh in FY (though for gift from Indian relative to NRI, often not required because gift is not 'chargeable to tax' under Section 195 - but AD bank practice varies).</li>"
         "<li><strong>ITR disclosure</strong>: both donor and recipient should disclose material gifts in their respective ITR (Schedule EI for exempt gifts; Schedule OS if taxable).</li>"
         "<li><strong>5-year retention</strong>: all documentation preserved for 5+ years to support tax position if questioned.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Is NRI gift to Indian parents tax-free?",
         "Yes - parents are 'relatives' under Explanation to Section 56(2)(x). Gift from NRI son/daughter to Indian parent is fully exempt in parent's hands, any amount, under Section 56(2)(x). On FEMA side: outbound remittance from abroad to India is inbound into Indian resident's bank account - no FEMA restriction on receipt. Gift deed documentation recommended."),
        ("Can Indian parents gift money to NRI daughter / son abroad?",
         "Yes - via LRS (Liberalised Remittance Scheme) up to USD 250,000 per Indian resident per FY (combined for all current + capital account purposes). Documented with Form A2 + gift purpose code + PAN. Gift deed strengthens the case. Section 56(2)(x) exempts the recipient NRI (parent is 'relative'). TCS 20% under Section 206C(1G) on LRS above INR 7 lakh/FY applies on remitting side."),
        ("Can Indian resident gift Indian property to NRI son / daughter?",
         "Yes - via registered gift deed in India with stamp duty + registration (state-specific; varies 2-7% of circle rate / market value). Permitted under FEMA (gift of immovable property to NRI relative allowed; agricultural land excluded). NRI holds the property with NRO-linked income; eventual sale subject to Section 195 TDS + USD 1M/year repatriation."),
        ("Can an NRI give gift of Indian shares / securities to an Indian relative?",
         "Yes - via FC-TRS filing (transfer of shares between non-resident and resident). Transfer at nil consideration (gift) permitted between relatives. Stamp duty on share transfer applicable. Section 56(2)(x) exempts recipient (donor is relative). Capital gain for NRI = nil (gift, no consideration). Cost of acquisition for Indian recipient = original cost in NRI's hands (Section 49(1))."),
        ("Does TCS apply to gift from Indian parent to NRI child?",
         "Yes - under Section 206C(1G), 20% TCS on LRS remittance exceeding INR 7 lakh in FY (post Finance Act 2024). Collected by Indian remitting bank on Indian donor's side. Donor can claim TCS credit against own income tax or claim refund in own ITR. Does not affect recipient NRI's position."),
        ("Does BQP help NRIs with gift transactions in / out of India?",
         "Yes - standard NRI advisory service. Gift structuring, gift deed drafting, Section 56(2)(x) relative-status verification, FEMA compliance (LRS or inbound remittance), stamp duty + registration coordination for property gifts, FC-TRS filing for share gifts, Form 15CA/CB for outbound where applicable, ITR disclosure. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("section-56-2-x-gift-tax-india-2026.html", "Guide", "Section 56(2)(x)"),
        ("tcs-20-foreign-remittance-lrs-india-2026.html", "Guide", "LRS TCS"),
    ],
    cta_headline="Gifting to or from India across borders?",
    cta_body="Section 56 'relative' structuring + FEMA LRS compliance + gift deed + stamp duty + ITR disclosure. BQP end-to-end for NRI cross-border gift transactions.",
))

# 4. OCI cardholder tax India
write_page("oci-cardholder-tax-india-complete-2026", page(
    slug="oci-cardholder-tax-india-complete-2026",
    title="OCI Cardholder Tax India 2026 | Complete Residence + Income Guide - BQP",
    description="OCI (Overseas Citizen of India) cardholder tax in India 2026: residential status (NRI / RNOR / Resident) determination, Section 6 physical presence tests, taxability of global income vs India-source only, PAN requirement, bank accounts, property purchase, voting rights ineligibility. Complete practitioner's guide. CA Durgesh Chavda.",
    keywords="OCI cardholder tax India, OCI tax resident India, OCI NRI tax difference, OCI PAN Aadhaar India, OCI property purchase India tax",
    hero_kicker="/ NRI Guide &middot; OCI Tax &middot; Updated 2026-10-15",
    hero_title_html="OCI cardholder tax, <em>what residence status really means.</em>",
    hero_lead="OCI (Overseas Citizen of India) card gives Indian-origin persons lifetime multi-entry visa + near-citizen rights. But OCI status does NOT change your Indian tax residence &mdash; tax residence is determined only by Section 6 physical presence in India. OCI holder can be NRI (most common), RNOR, or Resident for a given FY. Here's the complete 2026 tax framework for OCI cardholders.",
    sections=[
        ("/ OCI card vs tax residence", "They are separate.",
         "<p><strong>OCI card is an immigration/visa document</strong>:</p>"
         "<ul>"
         "<li>Issued by Government of India, Ministry of Home Affairs.</li>"
         "<li>Lifetime multi-entry Indian visa (no need for Indian visa before each trip).</li>"
         "<li>Near-equal civil rights with Indian citizens (except voting, government jobs, agricultural land purchase, political office).</li>"
         "<li>Does NOT confer Indian citizenship.</li>"
         "<li>Does NOT determine Indian tax residence.</li>"
         "</ul>"
         "<p><strong>Indian tax residence is determined by Section 6 Income Tax Act</strong>:</p>"
         "<ul>"
         "<li>Resident: physically in India for 182+ days in FY, OR 60+ days in FY plus 365+ days in preceding 4 FYs.</li>"
         "<li>Non-Resident (NRI): neither test satisfied.</li>"
         "<li>RNOR (Resident but Not Ordinarily Resident): resident this FY but non-resident for 9+ of 10 preceding FYs, OR physically in India &lt;= 729 days in 7 preceding FYs. See our <a href='nri-residential-status-rnor-india.html'>RNOR guide</a>.</li>"
         "</ul>"
         "<p>So an OCI holder physically present in India for most of the FY = Resident; one who visits briefly = NRI. OCI card itself is tax-neutral.</p>"),
        ("/ Taxability depends on status", "Three different regimes.",
         "<ul>"
         "<li><strong>OCI = Resident</strong>: global income taxable in India. World-wide investment income, overseas rental, foreign employment salary, foreign capital gain &mdash; all taxable at slab rate (foreign tax credit under Section 90/91 for DTAA).</li>"
         "<li><strong>OCI = RNOR</strong>: India-source + foreign-source income from business controlled from India + professional set up in India. Foreign-source investment / overseas employment / foreign capital gain remain exempt. See <a href='nri-residential-status-rnor-india.html'>RNOR guide</a>. RNOR status typically available for 2-3 years post-return to India.</li>"
         "<li><strong>OCI = NRI</strong>: only India-source income taxable &mdash; Indian employment, Indian business, Indian property rental, India-source capital gain, Indian bank interest. Foreign income / foreign investment income not taxable in India.</li>"
         "</ul>"
         "<p>Many OCI holders maintain NRI status throughout life (short Indian visits only) &rarr; only India-source income taxable. Significant tax planning benefit vs full-resident status.</p>"),
        ("/ Key tax touch-points for OCI holder", "What they typically own in India.",
         "<ul>"
         "<li><strong>Indian bank account</strong>: NRO (for Indian income - rent, dividend, interest), NRE (for foreign source - repatriable), FCNR (foreign currency fixed deposit, repatriable). Not regular savings (that's for residents).</li>"
         "<li><strong>Indian property</strong>: OCI can purchase residential / commercial property (not agricultural). Rental income taxable in India (standard deduction 30% + municipal tax + interest on home loan deduction).</li>"
         "<li><strong>Indian mutual fund / shares</strong>: via NRO or NRE demat. Capital gain on sale: LTCG 12.5% (post Finance Act 2024) or STCG 20% for listed equity. Interest / dividend taxable.</li>"
         "<li><strong>Indian ITR filing</strong>: mandatory if India-source income exceeds basic exemption (currently INR 3 lakh for NRIs). ITR-2 or ITR-3 depending on nature.</li>"
         "<li><strong>Form 10F + TRC</strong>: for DTAA treaty rate claim. See <a href='nri-form-10f-e-filing-mandatory-india-2026.html'>Form 10F guide</a>.</li>"
         "<li><strong>Section 54 reinvestment</strong>: available on sale of Indian property (same rules as resident).</li>"
         "<li><strong>Repatriation</strong>: up to USD 1M/year from NRO under FEMA; unlimited from NRE / FCNR.</li>"
         "</ul>"),
        ("/ Specific OCI complications in 2026", "Current traps.",
         "<ul>"
         "<li><strong>PAN requirement</strong>: OCI typically needs Indian PAN for ITR filing, property purchase, financial transactions above INR 2.5 lakh. Apply via Form 49AA (NRI PAN).</li>"
         "<li><strong>PAN-Aadhaar linking</strong>: NRIs are EXEMPT from mandatory PAN-Aadhaar linking (Notification 37/2017). OCI should ensure PAN is marked NRI in database. See our <a href='nri-pan-aadhaar-linking-exemption-rules.html'>PAN-Aadhaar guide</a>.</li>"
         "<li><strong>Deemed resident under Section 6(1A)</strong>: Indian citizen or OCI stay in India &gt; 120 days (if India income &gt; INR 15 lakh) treated as deemed resident but RNOR &mdash; narrow trap for high-income OCIs with substantial Indian income.</li>"
         "<li><strong>US estate tax</strong>: if OCI is US tax person, worldwide assets (including Indian) in US estate. See <a href='nri-us-estate-tax-indian-assets.html'>US estate tax guide</a>.</li>"
         "<li><strong>FBAR + Form 8938</strong>: US tax person with foreign financial accounts must report. India NRO / NRE / MF holdings disclosable.</li>"
         "<li><strong>LRS on Indian income</strong>: cannot use LRS as OCI (LRS is for Indian residents only). Repatriation of Indian income via NRO - USD 1M/year route instead.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Does OCI card make me an Indian tax resident?",
         "No - OCI is an immigration document, not a tax status. Indian tax residence is determined solely by Section 6 Income Tax Act physical presence tests (182+ days in FY, or 60+ days + 365+ days in preceding 4 FYs). Most OCI holders residing abroad maintain NRI status; only short visitors to India stay NRI by default."),
        ("What is deemed resident under Section 6(1A) for OCI holder?",
         "Finance Act 2020 inserted Section 6(1A): Indian citizen or OCI who stays in India for more than 120 days (if India-source income > INR 15 lakh) is treated as deemed resident but with Not Ordinarily Resident (RNOR) status. Applies only to high-India-income OCIs - most ordinary OCI holders unaffected. Benefit: can be in India longer without triggering full Resident status, but with RNOR tax treatment."),
        ("Can OCI holder buy agricultural land in India?",
         "No - OCI cannot buy agricultural / plantation / farmhouse. Can inherit (same as any NRI). Can purchase residential / commercial property freely. For agricultural land purchase, OCI must have RBI prior approval (rarely granted)."),
        ("Does OCI holder need to link PAN with Aadhaar?",
         "No - NRIs including OCI holders are EXEMPT from mandatory PAN-Aadhaar linking under CBDT Notification 37/2017. However, PAN database must correctly reflect NRI status; if PAN was issued when holder was resident and status changed to NRI, update required. Common issue - PAN marked as resident but holder is actually OCI/NRI results in PAN inoperative notice."),
        ("Does OCI holder need to file Indian ITR?",
         "Only if India-source income exceeds basic exemption limit (currently INR 3 lakh for NRIs under old regime; INR 7 lakh income under new regime with Section 87A rebate). Income types that typically trigger ITR: Indian property rent, Indian capital gains, Indian bank interest above INR 10K, India salary. Even where ITR not mandatory, filing often beneficial to claim Section 195 TDS refund."),
        ("Does BQP handle OCI cardholder tax matters?",
         "Yes - standard NRI advisory. Residential status determination, Section 6(1A) deemed resident analysis, Indian ITR filing, Section 195 TDS structuring, Form 10F + TRC, DTAA treaty rate, property purchase/sale coordination, FEMA repatriation, India-US estate tax integration. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-residential-status-rnor-india.html", "Guide", "NRI Residential Status"),
        ("nri-pan-aadhaar-linking-exemption-rules.html", "Guide", "PAN-Aadhaar Rules"),
    ],
    cta_headline="OCI card doesn't change tax residence &mdash; but Section 6(1A) can.",
    cta_body="Residential status + ITR filing + property / investment tax + FEMA repatriation. BQP: scope-based engagement for OCI holders in US / UK / UAE / Singapore / EU / Australia / Canada.",
))

# 5. US Green Card holder India tax
write_page("us-green-card-holder-india-tax-complete-2026", page(
    slug="us-green-card-holder-india-tax-complete-2026",
    title="US Green Card Holder India Tax 2026 | Dual Tax Residence + DTAA - BQP",
    description="US Green Card holder's India tax position 2026: US tax resident globally + Indian tax residence by Section 6, Form 1040 + Form 1116 + FBAR + Form 8938 + Indian ITR, India-US DTAA relief, Social Security no totalization, state tax issues, exit tax Section 877A. Complete practitioner's guide. CA Durgesh Chavda.",
    keywords="US green card holder India tax, lawful permanent resident India tax, green card India DTAA, FBAR Form 8938 India NRI, green card exit tax 877A India",
    hero_kicker="/ NRI Guide &middot; Green Card Holder &middot; Updated 2026-10-15",
    hero_title_html="US green card + Indian property, <em>the dual-residence puzzle.</em>",
    hero_lead="US green card holder (lawful permanent resident / LPR) is a US tax person on worldwide income. If also physically present in India &gt; 182 days or qualifying under Section 6 Indian tests, becomes dual tax resident. Form 1040 US + ITR India both. India-US DTAA + Foreign Tax Credit (FTC) prevent double tax but require careful execution. Plus FBAR, Form 8938, Section 877A exit tax. Here's the complete 2026 framework.",
    sections=[
        ("/ The dual-residence problem", "US + India both.",
         "<p><strong>US tax residence for green card holder</strong>:</p>"
         "<ul>"
         "<li>LPR is 'US person' per IRC Section 7701(b) &mdash; taxed on worldwide income regardless of physical location.</li>"
         "<li>Must file Form 1040 reporting global income.</li>"
         "<li>Must file FBAR (FinCEN Form 114) if aggregate foreign financial accounts &gt; USD 10,000 at any time in year.</li>"
         "<li>Must file Form 8938 (FATCA) if foreign financial assets &gt; USD 50,000 (single) / 100,000 (joint) at year-end OR 75K / 150K any time.</li>"
         "<li>State tax: if domiciled in a state (CA, NY, NJ), state income tax on worldwide income unless state residency broken.</li>"
         "</ul>"
         "<p><strong>Indian tax residence for green card holder</strong>:</p>"
         "<ul>"
         "<li>Section 6: physically in India 182+ days in FY, OR 60+ days plus 365+ days in preceding 4 FYs.</li>"
         "<li>If resident: global income taxable in India (subject to FTC and DTAA).</li>"
         "<li>If RNOR: India-source + foreign business controlled from India + professional set up in India.</li>"
         "<li>If NRI: India-source only.</li>"
         "</ul>"
         "<p><strong>Dual resident</strong>: possible to be US tax person (LPR) AND Indian tax resident (182+ days India) in same year. India-US DTAA Article 4 tie-breaker applies.</p>"),
        ("/ India-US DTAA tie-breaker + relief", "The treaty framework.",
         "<p><strong>Article 4 India-US DTAA tie-breaker rules</strong> (for individuals resident of both):</p>"
         "<ol>"
         "<li>Permanent home: where available &mdash; that country is residence.</li>"
         "<li>Centre of vital interests: closer personal / economic relations &mdash; that country is residence.</li>"
         "<li>Habitual abode: country where person habitually resides &mdash; that country is residence.</li>"
         "<li>National: country of citizenship.</li>"
         "<li>Mutual agreement: competent authorities of two countries decide.</li>"
         "</ol>"
         "<p>Green card holder physically settled in India after moving back: likely Indian treaty residence under centre of vital interests + habitual abode.</p>"
         "<p><strong>Foreign Tax Credit (FTC)</strong>:</p>"
         "<ul>"
         "<li>Form 1116 US: credit for Indian income tax paid on same income.</li>"
         "<li>Section 90 India: credit for US tax paid on US-source income (for Indian ITR).</li>"
         "<li>Example: Green card holder in India sells US stock. US capital gain tax at long-term rate (0/15/20%). India also taxes under Section 48 (post-2024 LTCG 12.5% + reinvestment exemptions). FTC in each ITR for other country's tax.</li>"
         "</ul>"),
        ("/ Common cross-tax scenarios", "What to plan.",
         "<ul>"
         "<li><strong>Green card holder returning to live in India</strong>: becomes Indian tax resident. Form 1040 + Indian ITR both required. Prior-year RNOR relief possible for 2-3 years. See <a href='nri-returning-india-rnor-complete-planning.html'>RNOR returning guide</a>.</li>"
         "<li><strong>Green card holder with Indian rental income</strong>: taxable both countries. Indian ITR with Section 24 standard deduction (30%) + interest on home loan (full deduction if let-out). US Schedule E with GAAP depreciation. FTC claim.</li>"
         "<li><strong>Green card holder with India mutual fund</strong>: Indian LTCG 12.5% post Finance Act 2024. US treats as PFIC (Passive Foreign Investment Company) &mdash; complex taxation (QEF election or Mark-to-market). FTC available but PFIC rules may erode benefit.</li>"
         "<li><strong>Indian employer salary + US green card</strong>: Indian employer withholds Section 192 TDS. US treats as US-source foreign wages (requires separate reporting). FTC relief under DTAA.</li>"
         "<li><strong>Indian dividend to green card holder</strong>: Section 195 TDS at 20% (10-15% under DTAA with TRC + Form 10F). US taxes as ordinary dividend (unless qualifying for lower rate). FTC relief.</li>"
         "</ul>"),
        ("/ Social Security - no totalization", "The gap.",
         "<ul>"
         "<li>India and US have NOT signed a Social Security Totalization Agreement (both have pending negotiations &mdash; no agreement as of 2026-10-15).</li>"
         "<li><strong>Green card holder working for Indian employer in India</strong>: contributes to Indian PF/EPF. No US Social Security contribution. Years do NOT count toward US SS eligibility.</li>"
         "<li><strong>Green card holder working for US employer in India (secondment)</strong>: US SS withheld (W-2) + Indian PF obligation on Indian company. Double contribution.</li>"
         "<li><strong>Planning</strong>: for dual residents / returning green card holders, structure employment to avoid double social security where possible.</li>"
         "</ul>"),
        ("/ Section 877A exit tax", "If giving up green card.",
         "<ul>"
         "<li><strong>Section 877A</strong>: expatriation tax applies if LPR &quot;covered expatriate&quot; &mdash; defined as LPR who:</li>"
         "<li>&nbsp;&nbsp;&mdash; Average net income tax for 5 years &gt; USD 206,000 (2026 threshold), OR</li>"
         "<li>&nbsp;&nbsp;&mdash; Net worth &gt; USD 2 million, OR</li>"
         "<li>&nbsp;&nbsp;&mdash; Fails to certify 5-year tax compliance.</li>"
         "<li><strong>Mark-to-market tax</strong>: all worldwide assets treated as sold at fair value on day before expatriation. Deemed gain / loss subject to tax (with USD 866,000 exclusion in 2026).</li>"
         "<li><strong>Specific IRA / 401k / deferred compensation</strong>: special rules.</li>"
         "<li><strong>Indian property + Indian company shares</strong>: deemed sold &mdash; US capital gains tax on built-in gain.</li>"
         "<li><strong>Planning</strong>: pre-expatriation review of worldwide assets, Section 1014 step-up planning, Indian legal / tax structuring.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Does a US green card holder need to file Indian ITR?",
         "Only if (a) physically Indian tax resident (182+ days in FY, or 60+/365+ test), OR (b) India-source income exceeds basic exemption limit (currently INR 3 lakh for NRIs). Most green card holders residing in US are Indian NRIs - file Indian ITR only if India rental / Indian capital gains / Indian bank interest triggers filing threshold. Green card holders physically in India for extended periods become Indian residents - full worldwide income disclosure in Indian ITR."),
        ("How does the India-US DTAA help a green card holder?",
         "Prevents double taxation via Foreign Tax Credit (FTC) + reduced treaty rates on specific income types. Article 4 tie-breaker determines treaty residence if dual resident. Treaty rates: dividend 15% (25% ownership) / 25% (otherwise); royalty 10-15%; FTS 10-15%. Both India and US must honour treaty rates per their domestic law. TRC + Form 10F required for Indian treaty claim."),
        ("Is Indian PF (Provident Fund) taxable to a US green card holder?",
         "Complex. US generally treats Indian PF as foreign pension - taxable in US on contributions + growth + distributions unless specific DTAA treatment applies. India-US DTAA has no specific PF article - US tax applies. Needs year-by-year reporting (Form 8938, FBAR). Specialised cross-border tax advice essential; many green card holders unknowingly misreport Indian PF."),
        ("Can I keep US green card while living in India long-term?",
         "Technically yes - LPR status maintained if you don't abandon residence. But: (a) physical absence from US > 1 year without re-entry permit creates presumption of abandonment; (b) USCIS may question continued LPR status at port of entry if India stay prolonged; (c) US tax obligations continue regardless of physical location. Many long-term India residents either surrender green card (triggering Section 877A exit tax if covered expatriate) or obtain re-entry permit periodically."),
        ("What is Section 877A exit tax for giving up US green card?",
         "If covered expatriate (net worth > USD 2M, or 5-year avg tax > USD 206K in 2026, or fails 5-year certification), worldwide assets deemed sold at fair value on day before expatriation. Capital gains tax applies on built-in gain (above USD 866K exclusion in 2026). Specific rules for IRA / 401k / deferred compensation. Pre-planning essential: step-up strategies, gifting out assets before trigger date, Indian legal / tax integration."),
        ("Does BQP handle green card holder cross-border tax matters?",
         "Yes - coordinated India + US cross-border advisory for green card holders. Indian residential status + ITR filing + Section 195 TDS structuring + Form 10F + TRC + DTAA FTC claim + repatriation + property / investment tax. Co-ordinate with US CPA / tax advisor for Form 1040 + Form 1116 + FBAR + Form 8938 integration. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-returning-india-tax-rnor-transition.html", "Guide", "NRI Returning"),
        ("india-us-tax-treaty-dtaa.html", "Guide", "India-US DTAA"),
    ],
    cta_headline="US green card + India income or Indian stay? Dual tax doesn't have to mean double tax.",
    cta_body="BQP cross-border: Indian ITR + Form 10F + TRC + Section 195 + DTAA FTC + exit tax planning. Co-ordinates with US CPA for Form 1040 / FBAR / Form 8938 integration.",
))

# 6. NRI PAN-Aadhaar
write_page("nri-pan-aadhaar-linking-exemption-rules", page(
    slug="nri-pan-aadhaar-linking-exemption-rules",
    title="NRI PAN-Aadhaar Linking Rules 2026 | Exemption + How to Fix - BQP",
    description="NRI PAN-Aadhaar linking exemption rules 2026: Notification 37/2017 exempts NRIs, but PAN marked 'resident' in database becomes inoperative - how to update PAN status to NRI, Form 49AA correction, Aadhaar enrolment for NRIs who want it, consequences of inoperative PAN. Complete 2026 guide. CA Durgesh Chavda.",
    keywords="NRI PAN Aadhaar linking exemption, NRI PAN inoperative fix, update PAN status NRI, Form 49AA NRI, Aadhaar for NRI India",
    hero_kicker="/ NRI Guide &middot; PAN-Aadhaar &middot; Updated 2026-10-15",
    hero_title_html="NRI PAN-Aadhaar, <em>you're exempt &mdash; but check your PAN status.</em>",
    hero_lead="Mandatory PAN-Aadhaar linking (Section 139AA) does NOT apply to NRIs. CBDT Notification 37/2017 specifically exempts non-residents. BUT: if NRI's PAN was issued when they were a resident, the PAN database still shows them as 'resident' &mdash; and PAN gets marked inoperative when linking deadline passes. Fix: update PAN status to NRI. Here's the complete 2026 playbook.",
    sections=[
        ("/ The exemption rule", "Who's exempt.",
         "<ul>"
         "<li><strong>Section 139AA + Rule 114AAA</strong>: PAN must be linked with Aadhaar; non-linking makes PAN inoperative.</li>"
         "<li><strong>CBDT Notification 37/2017 (dated 11 May 2017, as amended)</strong>: exempts specific categories from mandatory linking:</li>"
         "<li>&nbsp;&nbsp;&mdash; Non-residents as per Income Tax Act (NRIs).</li>"
         "<li>&nbsp;&nbsp;&mdash; Residents of the states of Assam, Jammu &amp; Kashmir, and Meghalaya.</li>"
         "<li>&nbsp;&nbsp;&mdash; Persons aged 80+ (super senior citizens).</li>"
         "<li>&nbsp;&nbsp;&mdash; Non-citizens of India.</li>"
         "</ul>"
         "<p>NRI's PAN therefore does NOT need to be linked with Aadhaar. In practice, many NRIs don't have Aadhaar anyway (Aadhaar enrolment requires residence in India for 182+ days in preceding 12 months - uncommon for NRIs).</p>"),
        ("/ The practical trap", "PAN database vs actual status.",
         "<p>Here's where NRIs trip:</p>"
         "<ul>"
         "<li>Person obtained PAN when they were Indian resident (say, 2010).</li>"
         "<li>Moved abroad in 2015, became NRI.</li>"
         "<li>PAN database still shows them as 'resident' because PAN was issued under resident Form 49A.</li>"
         "<li>Income Tax Department applies 'resident' status to PAN for Section 139AA purposes.</li>"
         "<li>Linking deadline passes (currently 30 June 2023 was last extension).</li>"
         "<li>PAN marked 'inoperative' because of non-linking.</li>"
         "<li>NRI discovers it when: Section 195 TDS deducted at 20% (PAN-absent rate), bank KYC refresh fails, mutual fund KYC fails, Form 15CB signing fails, Indian ITR cannot be filed online.</li>"
         "</ul>"
         "<p>Materially &mdash; the exemption EXISTS but it's not automatically applied. Must proactively update PAN status to NRI in database.</p>"),
        ("/ How to update PAN status to NRI", "The fix.",
         "<ol>"
         "<li><strong>File Form 49AA</strong>: 'Request for Changes or Correction in PAN Data' &mdash; specifically the version for non-residents.</li>"
         "<li><strong>Online route</strong>: NSDL (now Protean) e-governance portal: tin-nsdl.com &rarr; PAN services &rarr; Changes or Correction &rarr; select 'Non-resident' category.</li>"
         "<li><strong>Documents to upload</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Proof of NRI status: foreign passport + visa / residence card / green card / OCI card.</li>"
         "<li>&nbsp;&nbsp;&mdash; Address proof (foreign address): utility bill / bank statement / lease agreement.</li>"
         "<li>&nbsp;&nbsp;&mdash; Existing PAN card copy.</li>"
         "<li>&nbsp;&nbsp;&mdash; Passport-size photo.</li>"
         "<li><strong>Fee</strong>: ~INR 100-200 for correction + courier (varies).</li>"
         "<li><strong>Processing</strong>: 15-30 days.</li>"
         "<li><strong>Updated PAN</strong>: database status changes to 'Non-Resident'. Section 139AA exemption applies.</li>"
         "<li><strong>If PAN already inoperative</strong>: filing Form 49AA simultaneously + requesting restoration. May require Jurisdictional AO contact.</li>"
         "</ol>"),
        ("/ What happens if NRI's PAN becomes inoperative", "The downstream.",
         "<ul>"
         "<li><strong>Section 206AA kicks in</strong>: all TDS on NRI's India-source income at higher of applicable rate or 20%.</li>"
         "<li><strong>Section 206CC</strong>: higher TCS rate.</li>"
         "<li><strong>Section 195 TDS without PAN</strong>: 20% rate applies (treaty rate blocked by Section 206AA).</li>"
         "<li><strong>Indian ITR cannot be e-filed</strong>: PAN required for e-filing; inoperative PAN blocks.</li>"
         "<li><strong>Form 10F e-filing fails</strong>: without operative PAN, cannot login to Indian e-filing portal.</li>"
         "<li><strong>Bank KYC refresh fails</strong>: Indian banks block NRO / NRE operations.</li>"
         "<li><strong>Mutual fund + demat KYC fails</strong>: cannot redeem / sell holdings.</li>"
         "<li><strong>Form 15CB signing blocked</strong>: Indian payer cannot complete Form 15CA + 15CB for foreign remittance to NRI.</li>"
         "</ul>"
         "<p>Materially: inoperative PAN cascades into blocking most financial operations. Fix PAN status to NRI first, then normal operations resume.</p>"),
        ("/ Can NRI get Aadhaar", "The eligibility.",
         "<ul>"
         "<li><strong>Aadhaar enrolment eligibility</strong>: resident of India for 182+ days in preceding 12 months (per UIDAI). NRI residing abroad typically does NOT qualify.</li>"
         "<li><strong>NRI on long India visit (182+ days)</strong>: becomes eligible.</li>"
         "<li><strong>Returning NRI (settled in India)</strong>: becomes eligible.</li>"
         "<li><strong>If NRI has Aadhaar</strong> (obtained during past India residence): PAN-Aadhaar linking still not mandatory under Notification 37/2017 exemption. But can voluntarily link if useful.</li>"
         "<li><strong>Aadhaar enrolment procedure</strong>: visit nearest Aadhaar Enrolment Centre with ID + address proof + biometrics capture. Takes 2-4 weeks.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Do NRIs need to link PAN with Aadhaar?",
         "No - NRIs are EXEMPT from mandatory PAN-Aadhaar linking under CBDT Notification 37/2017. The exemption extends to non-residents, residents of Assam/J&K/Meghalaya, persons aged 80+, and non-citizens of India. However, PAN database must correctly reflect NRI status for the exemption to apply - if PAN was issued when holder was resident, status update required."),
        ("Why has my (NRI) PAN become inoperative?",
         "Likely because: (a) PAN database still shows you as 'resident' from original Form 49A issuance even though you are now NRI, (b) PAN-Aadhaar linking deadline passed and database treated you as resident, (c) PAN was issued without proper residency status flag. Fix: file Form 49AA to update PAN to NRI status with supporting documents (foreign passport, visa, address). 15-30 day processing."),
        ("How do I update my PAN status from Resident to NRI?",
         "File Form 49AA ('Request for Changes or Correction in PAN Data' - non-resident version) via NSDL/Protean portal (tin-nsdl.com). Upload foreign passport + visa / residence card / OCI card + foreign address proof + existing PAN card + photo. Fee ~INR 100-200 + courier. Processing 15-30 days. PAN database updated to 'Non-Resident'; Section 139AA exemption applies."),
        ("What happens if my PAN stays inoperative?",
         "Multiple cascading issues: (a) Section 206AA higher TDS at 20% on India-source income; (b) Indian ITR cannot be e-filed; (c) Form 10F e-filing blocked (cannot login to income tax portal); (d) Bank/mutual fund/demat KYC refresh fails; (e) Form 15CB signing blocked for foreign remittance. Most Indian financial operations stall. Fix is urgent."),
        ("Can NRIs enrol for Aadhaar?",
         "Only if resident in India for 182+ days in preceding 12 months per UIDAI. Most NRIs abroad do not qualify. Returning NRIs who settle in India qualify after 6 months. If NRI already has Aadhaar from prior India residence, that's fine - still not mandatory to link with PAN under Notification 37/2017 exemption."),
        ("Does BQP help NRIs with PAN-Aadhaar / PAN status update?",
         "Yes - standard NRI advisory. PAN status review, Form 49AA filing for NRI status update, PAN restoration if inoperative, Jurisdictional AO coordination where required, Section 206AA mitigation, Form 10F e-filing. Fast turnaround to unblock Indian financial operations. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-form-10f-e-filing-mandatory-india-2026.html", "Guide", "Form 10F"),
        ("pan-aadhaar-linking-status-fix-india-2026.html", "Guide", "PAN-Aadhaar General"),
    ],
    cta_headline="NRI PAN marked inoperative or showing resident status?",
    cta_body="File Form 49AA to update PAN to NRI. 15-30 day resolution. Unblocks Section 195 TDS at treaty rate, Form 10F e-filing, bank KYC. BQP end-to-end for NRIs globally.",
))

# 7. NRI LDC property sale
write_page("nri-india-property-ldc-lower-deduction-certificate", page(
    slug="nri-india-property-ldc-lower-deduction-certificate",
    title="NRI Property Sale India LDC (Lower Deduction Certificate) 2026 - BQP",
    description="NRI selling Indian property - obtain Lower Deduction Certificate (LDC) under Section 197 to reduce 20% Section 195 TDS to actual tax liability: online application via TRACES, documents, timeline 4-8 weeks, buyer coordination. Avoid locking up INR lakhs in TDS pool. Working CA guide by Durgesh Chavda.",
    keywords="NRI property sale LDC lower deduction certificate, Section 197 LDC NRI property, TRACES LDC application NRI, Section 195 TDS reduction property NRI, LDC online NRI",
    hero_kicker="/ NRI Guide &middot; LDC &middot; Updated 2026-10-15",
    hero_title_html="NRI property sale, <em>LDC saves you from a 20% TDS trap.</em>",
    hero_lead="NRI selling Indian property: Section 195 requires buyer to deduct 20% TDS on sale consideration (not just gain). On INR 3 crore sale, that's INR 60 lakh locked up as TDS even if actual capital gain tax is INR 5 lakh. Lower Deduction Certificate (LDC) under Section 197 fixes this &mdash; apply to Indian Tax Officer, get a certificate specifying actual tax amount, buyer deducts only that amount. 4-8 week process. Here's the complete LDC playbook.",
    sections=[
        ("/ The 20% TDS problem", "Why LDC exists.",
         "<p><strong>Section 195 default</strong>: when buyer pays NRI seller for Indian property, buyer must deduct TDS at:</p>"
         "<ul>"
         "<li><strong>20% + applicable surcharge + 4% cess</strong> on LTCG (property held &gt; 24 months).</li>"
         "<li><strong>30% + applicable surcharge + 4% cess</strong> on STCG (property held &lt;= 24 months).</li>"
         "<li><strong>TDS applies on gross sale consideration</strong> &mdash; not on gain. So even if your gain is modest or nil, 20% of sale amount withheld.</li>"
         "<li>TDS deposited by buyer with Indian government; NRI claims refund later in Indian ITR.</li>"
         "</ul>"
         "<p><strong>The problem</strong>: on INR 3 crore property with INR 50 lakh gain, actual tax under Section 112 (LTCG) at 12.5% without indexation = INR 6.25 lakh. But Section 195 TDS = 20% of INR 3 crore = INR 60 lakh. INR 54 lakh overpaid; locked in TDS pool until Indian ITR refund (6-18 months). Huge cash flow trap.</p>"
         "<p><strong>Section 197 LDC solution</strong>: NRI applies to Indian Tax Officer for certificate specifying lower TDS rate matching actual tax liability. Buyer then deducts the lower amount.</p>"),
        ("/ When LDC is worth the effort", "Decision criteria.",
         "<ul>"
         "<li><strong>Property sale value &gt; INR 50 lakh</strong>: 20% TDS = INR 10 lakh. Worth 4-8 weeks of application effort.</li>"
         "<li><strong>Gain is less than sale value</strong>: standard for property sold with indexed cost or Section 54 reinvestment planned. Material TDS saving.</li>"
         "<li><strong>Timing allows 4-8 weeks</strong>: LDC takes typically 4-8 weeks (sometimes faster, sometimes longer). If buyer wants to close within 2 weeks, LDC may not be ready.</li>"
         "<li><strong>Section 54 / 54F reinvestment planned</strong>: capital gain will be fully / partially exempt &rarr; actual tax very low &rarr; LDC essentially zero rate &rarr; massive TDS saving.</li>"
         "</ul>"
         "<p>For sale under INR 50 lakh or urgent closing (no LDC time), accept 20% TDS and claim refund in Indian ITR.</p>"),
        ("/ LDC application workflow", "Step by step.",
         "<ol>"
         "<li><strong>Pre-requisite documentation</strong>:</li>"
         "<li>&nbsp;&nbsp;&mdash; Property purchase deed (showing cost + date).</li>"
         "<li>&nbsp;&nbsp;&mdash; Property sale agreement / draft (showing sale value + buyer details).</li>"
         "<li>&nbsp;&nbsp;&mdash; NRI's PAN + proof of NRI status (passport + visa / OCI).</li>"
         "<li>&nbsp;&nbsp;&mdash; Capital gain calculation with indexation + Section 54 reinvestment plan if applicable.</li>"
         "<li>&nbsp;&nbsp;&mdash; Last 2-3 years Indian ITR of NRI (shows capital gain treatment history).</li>"
         "<li><strong>File Form 13 on TRACES portal</strong> (traces.tdscpc.gov.in):</li>"
         "<li>&nbsp;&nbsp;&mdash; NRI logs in with PAN + password.</li>"
         "<li>&nbsp;&nbsp;&mdash; Navigate to 'Statement/Payment &rarr; Request for Lower / No Deduction Certificate'.</li>"
         "<li>&nbsp;&nbsp;&mdash; Fill Form 13 online: Section 195, nature of payment (immovable property sale), payer details (buyer PAN), amount, requested TDS rate.</li>"
         "<li>&nbsp;&nbsp;&mdash; Upload supporting documents.</li>"
         "<li>&nbsp;&nbsp;&mdash; Submit with DSC or Aadhaar OTP (if NRI has either).</li>"
         "<li><strong>Assigned to Jurisdictional AO</strong>: application moves to Assessing Officer having jurisdiction over NRI's PAN.</li>"
         "<li><strong>AO review</strong>: may ask for clarifications, additional documents. Response via portal.</li>"
         "<li><strong>LDC issued</strong>: specifies the applicable TDS rate (e.g., 1% of sale consideration vs 20% default). Valid for the specific transaction.</li>"
         "<li><strong>Share LDC with buyer</strong>: buyer deducts the lower rate; deposits reduced TDS with government; files Form 27Q showing LDC reference.</li>"
         "<li><strong>Final tax reconciliation</strong>: NRI files Indian ITR; any residual tax paid/refunded.</li>"
         "</ol>"),
        ("/ What LDC rate the AO typically approves", "Realistic expectations.",
         "<ul>"
         "<li><strong>LTCG on property held long term with indexation</strong>: AO calculates actual tax on indexed capital gain + applicable surcharge + cess, then LDC specifies that amount as % of sale consideration. Typically 2-5% of sale value for modest gain.</li>"
         "<li><strong>LTCG with Section 54 reinvestment plan</strong>: if NRI commits to buy new residential property within 2 years (or construct within 3 years), capital gain exempt &rarr; LDC may specify very low rate (0.1-1% of sale).</li>"
         "<li><strong>Section 54EC bonds</strong>: INR 50 lakh in REC / NHAI / PFC / IRFC bonds within 6 months of sale &rarr; INR 50 lakh of gain exempt &rarr; LDC reflects remaining tax.</li>"
         "<li><strong>Section 54F</strong>: full LTCG exemption on sale of long-term asset (non-residential) if net consideration invested in one residential property &rarr; LDC near zero.</li>"
         "<li><strong>No reinvestment, substantial gain</strong>: LDC rate close to actual tax rate (12.5% on indexed gain).</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("What is Lower Deduction Certificate (LDC) for NRI property sale?",
         "A certificate issued by Indian Tax Officer under Section 197 Income Tax Act, specifying a TDS rate lower than Section 195 default (20% on LTCG / 30% on STCG), based on NRI's actual tax liability on the sale. Issued via Form 13 application on TRACES portal. Buyer deducts the LDC-specified rate instead of default - saves significant cash flow for NRI."),
        ("How long does LDC take?",
         "4-8 weeks typically from Form 13 submission to LDC issuance. Can be faster (2-4 weeks) if application is well-documented + AO is responsive, or slower (8-12 weeks) if AO raises queries or jurisdictional transfer required. Plan the property sale timeline accordingly; LDC should be in hand before closing."),
        ("What's the typical LDC rate approved by AO?",
         "Varies: 2-5% of sale consideration for property with modest LTCG; 0.1-1% if Section 54 reinvestment planned; close to 0% if full Section 54F exemption; close to 12.5% if large gain with no reinvestment. AO calculates actual tax under Section 112 (post Finance Act 2024 LTCG rules) and expresses as % of sale value for LDC."),
        ("Can I apply for LDC after the sale is done?",
         "No - LDC must be in place BEFORE buyer makes payment / deducts TDS. Once 20% default TDS is deducted and deposited, the only remedy is refund via Indian ITR filing (6-18 month wait). LDC is prospective - apply well in advance."),
        ("Does the buyer need to do anything special with LDC?",
         "Buyer references the LDC in Form 27Q TDS return + mentions it in the TDS challan. Buyer deducts the lower rate specified in LDC, deposits only that amount, files Form 27Q quarterly, issues Form 16A to NRI showing LDC rate. Standard procedure for buyer; most Indian buyers are familiar if advised at execution."),
        ("Does BQP handle LDC applications for NRI property sellers?",
         "Yes - standard NRI service. Capital gain calculation with indexation + Section 54/54F/54EC planning + Form 13 preparation + TRACES filing + AO follow-up + LDC issuance + buyer coordination. 4-8 week turnaround. Scope-based engagement. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-selling-indian-property-capital-gains.html", "Guide", "NRI Property Sale"),
        ("nri-property-tds-ldc-calculator.html", "Tool", "NRI Property TDS Calculator"),
    ],
    cta_headline="Selling Indian property as NRI? Don't lose 20% to TDS pool.",
    cta_body="LDC under Section 197 reduces TDS from 20% default to your actual tax rate. 4-8 week application via Form 13 on TRACES. BQP: capital gain calc + Form 13 + AO follow-up + buyer coordination.",
))

# 8. NRI DTAA practical
write_page("nri-dtaa-claim-practical-trc-form-10f", page(
    slug="nri-dtaa-claim-practical-trc-form-10f",
    title="NRI DTAA Claim Practical Guide 2026 | TRC + Form 10F + Rates - BQP",
    description="NRI practical guide to claiming DTAA treaty rate on India-source income 2026: TRC (Tax Residency Certificate) from home country, Form 10F electronic filing, Section 195 TDS reduction, Section 90(4) Act compliance, no-PE declaration, beneficial ownership. Country-wise rates. CA Durgesh Chavda.",
    keywords="NRI DTAA claim practical, TRC Form 10F DTAA, Section 90(4) DTAA, DTAA treaty rate NRI India, DTAA no PE declaration NRI",
    hero_kicker="/ NRI Guide &middot; DTAA Practical &middot; Updated 2026-10-15",
    hero_title_html="DTAA claim as NRI, <em>the three-document shortcut.</em>",
    hero_lead="India has Double Taxation Avoidance Agreements (DTAAs) with 90+ countries. If you're an NRI resident of a treaty country, your India-source income can be taxed at reduced treaty rate instead of Section 195 default (20%+). But claiming the treaty rate requires three documents in sequence: TRC from your country, Form 10F on Indian e-filing portal, and (sometimes) no-PE declaration. Here's exactly how to execute each.",
    sections=[
        ("/ The three documents - what each proves", "The chain.",
         "<ul>"
         "<li><strong>1. TRC (Tax Residency Certificate)</strong> &mdash; issued by home country tax authority. Confirms: NRI is tax resident of that country during the specified period. Required under Section 90(4) Income Tax Act. Without TRC, DTAA benefit denied.</li>"
         "<li><strong>2. Form 10F</strong> &mdash; declaration by NRI on India's e-filing portal. Confirms: status, nationality, TIN, residence country, beneficial ownership of income, treaty eligibility. Required under Rule 21AB. Mandatory electronic post Oct 2023. See <a href='nri-form-10f-e-filing-mandatory-india-2026.html'>Form 10F guide</a>.</li>"
         "<li><strong>3. No-PE declaration</strong> &mdash; required for business income claim under Article 7 of most DTAAs. NRI confirms they don't have a Permanent Establishment in India. If NRI has Indian PE (fixed place / dependent agent / service PE), business income taxable in India (treaty doesn't exempt).</li>"
         "</ul>"
         "<p>These three together give the Indian payer / Indian Tax Officer confidence to apply reduced treaty rate.</p>"),
        ("/ TRC - country-wise mechanics", "How to get TRC.",
         "<p><strong>United States</strong>: Form 6166 from IRS. Apply via Form 8802 at least 45 days before needed. Fee USD 85. Can get up to 3 years at once. User account at IRS website.</p>"
         "<p><strong>United Kingdom</strong>: HMRC Certificate of Residence. Request online via Government Gateway or by letter. Typically 2-6 weeks turnaround.</p>"
         "<p><strong>UAE</strong>: FTA (Federal Tax Authority) Tax Residency Certificate. Apply via FTA portal. AED 500 individual / AED 1,750 commercial. 2-4 week processing.</p>"
         "<p><strong>Singapore</strong>: IRAS Certificate of Residence. Request via mytax.iras.gov.sg. 1-2 week processing.</p>"
         "<p><strong>Canada</strong>: CRA Certificate of Residency. Request by letter to CRA. 4-8 week processing.</p>"
         "<p><strong>Australia</strong>: ATO Certificate of Residency. Request via online MyGov or by letter. 2-4 week processing.</p>"
         "<p><strong>Germany / Netherlands / France / other EU</strong>: respective tax authority. Request via national tax portal; forms vary.</p>"
         "<p>TRC validity: typically 1 year (calendar or fiscal). Must be renewed annually for continued DTAA claim.</p>"),
        ("/ Country-wise DTAA rates for NRI", "Common income types.",
         "<table style='width:100%;border-collapse:collapse;margin:12px 0;font:400 12px Inter,system-ui,sans-serif'>"
         "<tr style='background:#f8f3e8'><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Country</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Dividend</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Interest</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Royalty</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>FTS</th><th style='padding:6px;border:1px solid #ece4d5;text-align:left'>Capital gain</th></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>USA</strong></td><td style='padding:6px;border:1px solid #ece4d5'>15/25%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>UK</strong></td><td style='padding:6px;border:1px solid #ece4d5'>10/15%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Singapore</strong></td><td style='padding:6px;border:1px solid #ece4d5'>10/15%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>Shares exempt if long-term</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>UAE</strong></td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>12.5%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Mauritius</strong></td><td style='padding:6px;border:1px solid #ece4d5'>5/15%</td><td style='padding:6px;border:1px solid #ece4d5'>7.5%</td><td style='padding:6px;border:1px solid #ece4d5'>15%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>Grandfathered pre-April 2017</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Canada</strong></td><td style='padding:6px;border:1px solid #ece4d5'>15/25%</td><td style='padding:6px;border:1px solid #ece4d5'>15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-20%</td><td style='padding:6px;border:1px solid #ece4d5'>10-20%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Australia</strong></td><td style='padding:6px;border:1px solid #ece4d5'>15%</td><td style='padding:6px;border:1px solid #ece4d5'>15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>10-15%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Germany</strong></td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "<tr><td style='padding:6px;border:1px solid #ece4d5'><strong>Netherlands</strong></td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>10%</td><td style='padding:6px;border:1px solid #ece4d5'>Taxed per IT Act</td></tr>"
         "</table>"
         "<p><em>Rates indicative; verify specific DTAA article + beneficial ownership + GAAR implications before relying. Treaty rate requires TRC + Form 10F + sometimes no-PE declaration.</em></p>"),
        ("/ Section 90(4) + GAAR considerations", "The anti-abuse layer.",
         "<ul>"
         "<li><strong>Section 90(4) Income Tax Act</strong>: TRC mandatory for DTAA benefit claim. Without TRC, Section 90 relief denied.</li>"
         "<li><strong>Section 90(5)</strong>: additional information prescribed in Form 10F must be furnished. Hence electronic Form 10F.</li>"
         "<li><strong>GAAR (Section 95-102)</strong>: General Anti-Avoidance Rules can deny treaty benefit if arrangement is primarily tax-driven without commercial substance.</li>"
         "<li><strong>Principal Purpose Test (PPT) under MLI</strong>: India's Multilateral Instrument notifications include PPT &mdash; treaty benefit denied if obtaining benefit is one of principal purposes of arrangement.</li>"
         "<li><strong>Beneficial ownership</strong>: Form 10F requires declaration. If actual beneficial owner is different (e.g., NRI is nominee for another person), treaty benefit may be denied under GAAR / PPT.</li>"
         "</ul>"
         "<p>For routine NRI DTAA claims (own residence country, direct ownership, no treaty shopping), TRC + Form 10F + no-PE sufficient. For complex structures or Mauritius/Singapore holding routes, GAAR / PPT review critical.</p>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("How does an NRI claim DTAA treaty rate on India-source income?",
         "Three documents in sequence: (1) TRC (Tax Residency Certificate) from home country tax authority confirming residence. (2) Form 10F filed electronically on India's income tax portal confirming status + treaty eligibility + beneficial ownership. (3) No-PE declaration for business income claims. Share all three with Indian payer; payer applies treaty rate under Section 195 instead of default 20%+."),
        ("How long is TRC valid?",
         "Typically 1 year (calendar or fiscal year as specified by issuing authority). Must be renewed annually for continued DTAA claim. Form 10F validity is tied to TRC period. Plan ahead: TRC application timelines vary 2-8 weeks by country; US takes 45 days minimum."),
        ("What if NRI doesn't have TRC when payment is due?",
         "Indian payer applies Section 195 default rate (20% + surcharge + cess). NRI pays higher tax upfront. Can obtain TRC later and claim refund via Indian ITR filing - 6-18 month wait. Plan ahead: obtain TRC + file Form 10F before major India-source income event (property sale, dividend declaration, royalty payment)."),
        ("What is a no-PE declaration and when is it required?",
         "Declaration by NRI confirming they do NOT have a Permanent Establishment in India (fixed place of business, dependent agent, construction site over 6 months, service PE based on days threshold). Required for Article 7 business income exemption under DTAA. If NRI has Indian PE, business income taxable in India - treaty doesn't exempt."),
        ("Does DTAA apply to NRI capital gain on Indian securities?",
         "Mostly no - most DTAAs allow source country (India) to tax capital gain per domestic law. Specific exception: India-Singapore DTAA grandfathering of pre-April 2017 shares (zero tax); India-Mauritius DTAA grandfathering of pre-April 2017 shares (zero tax). Post-April 2017 investments: taxed per Indian Section 112A / 115AD rates (12.5% LTCG, 20% STCG for listed equity post Finance Act 2024)."),
        ("Does BQP handle DTAA claims end-to-end?",
         "Yes - standard NRI advisory. TRC coordination from home country tax authority (US / UK / Singapore / UAE / Canada / Australia / EU), Form 10F e-filing on Indian portal, no-PE declaration drafting, DTAA treaty rate analysis per income type, Form 15CA/CB coordination with Indian payer, refund claim via Indian ITR if excess TDS. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-form-10f-e-filing-mandatory-india-2026.html", "Guide", "Form 10F"),
        ("india-us-tax-treaty-dtaa.html", "Guide", "India-US DTAA"),
    ],
    cta_headline="NRI with India-source income - the treaty rate is your right.",
    cta_body="TRC + Form 10F + no-PE = reduced TDS from 20% default to 10-15% treaty. BQP: full DTAA claim stack for NRIs globally. WhatsApp +91 78018 87130.",
))

# 9. NRE/NRO conversion returning
write_page("nri-nre-nro-conversion-returning-india-2026", page(
    slug="nri-nre-nro-conversion-returning-india-2026",
    title="NRE / NRO Account Conversion When Returning to India 2026 - BQP",
    description="NRI returning to India - convert NRE / NRO / FCNR accounts to resident accounts (Regular Savings / RFC / FCNR-B). Timing (within reasonable time of becoming resident), FEMA rules, RFC account benefits, interest tax treatment transition. Complete 2026 practitioner's guide. CA Durgesh Chavda.",
    keywords="NRE NRO conversion returning India, RFC account NRI returning, FEMA account conversion NRI resident, NRE to savings account conversion",
    hero_kicker="/ NRI Guide &middot; Account Conversion &middot; Updated 2026-10-15",
    hero_title_html="NRE / NRO / FCNR accounts, <em>converting when you return.</em>",
    hero_lead="NRI returning to settle in India must convert NRE / NRO / FCNR accounts to resident accounts within reasonable time of becoming resident under FEMA. Options: Regular Savings, RFC (Resident Foreign Currency) account, FCNR-B conversion to RFC at maturity. Each has different tax + repatriation implications. Mishandled: FEMA breach + continuing to use NRE as resident risks compounding. Here's the complete transition framework.",
    sections=[
        ("/ The trigger - when must conversion happen", "FEMA residence shift.",
         "<ul>"
         "<li><strong>FEMA residence</strong>: distinct from Income Tax residence. FEMA Section 2(v) defines 'person resident in India' broadly &mdash; stays in India for more than 182 days during preceding FY OR intends to come to India for employment / business / stay for uncertain period.</li>"
         "<li><strong>Trigger of residence</strong>: once NRI's intention to stay in India for uncertain period crystallises (job in India, settlement plan, bringing family), FEMA residence may trigger even before 182 days physical presence.</li>"
         "<li><strong>Conversion obligation</strong>: 'within reasonable time' of becoming resident, NRE / NRO / FCNR accounts must be converted / designated as resident. 'Reasonable time' interpreted by banks as 60-90 days typical but not strictly defined.</li>"
         "<li><strong>Continuing to operate NRE / NRO as resident</strong> = FEMA breach. Prolonged breach can trigger compounding under Section 13.</li>"
         "</ul>"),
        ("/ Account options post-return", "What to convert to.",
         "<p><strong>1. Regular Savings Account</strong></p>"
         "<ul>"
         "<li>Standard rupee-denominated resident account.</li>"
         "<li>NRO account typically re-designated as regular savings. Same account number, different flag.</li>"
         "<li>Interest fully taxable at slab rate.</li>"
         "<li>Form 15G / 15H can be submitted to avoid TDS where applicable.</li>"
         "</ul>"
         "<p><strong>2. RFC (Resident Foreign Currency) Account</strong></p>"
         "<ul>"
         "<li>Available only to Indian residents who were previously NRIs for a continuous period of 1+ year.</li>"
         "<li>Denominated in: USD, GBP, EUR, JPY, CAD, AUD + others.</li>"
         "<li>Fully repatriable &mdash; funds can be remitted abroad freely for any permissible purpose.</li>"
         "<li>Interest taxable in India at slab rate (foreign-source but received in India).</li>"
         "<li>No cap on balance.</li>"
         "<li>Typically used by returning NRIs who may re-expatriate; preserves foreign currency.</li>"
         "<li>Source of funds: NRE / FCNR maturity proceeds (transferable); foreign currency brought into India during return move; pension / superannuation from foreign employer.</li>"
         "</ul>"
         "<p><strong>3. FCNR-B account (maturity)</strong></p>"
         "<ul>"
         "<li>Existing FCNR-B deposit (foreign currency fixed deposit opened as NRI) can continue until maturity.</li>"
         "<li>At maturity, must be transferred to RFC account (not auto-renewable as FCNR-B once resident).</li>"
         "<li>Interest tax-exempt until maturity (per earlier NRI status rules).</li>"
         "</ul>"
         "<p><strong>4. RFC(D) Deposit (Resident Foreign Currency Domestic)</strong></p>"
         "<ul>"
         "<li>For Indian residents who weren't previously NRI (e.g., forex gift receipt, pension from foreign source).</li>"
         "<li>Non-repatriable.</li>"
         "<li>Different from RFC &mdash; chosen by never-NRI residents.</li>"
         "</ul>"),
        ("/ Transition workflow", "Step by step.",
         "<ol>"
         "<li><strong>Determine FEMA residence trigger date</strong>: when did you become resident under FEMA? Typically arrival + settled intention date.</li>"
         "<li><strong>Notify bank</strong>: visit NRE / NRO / FCNR bank with change-of-status declaration + supporting documents (Indian address proof, employment letter, flight ticket).</li>"
         "<li><strong>NRO account</strong>: typically re-designated as regular savings. Same account number. Interest from NRO continues; TDS at resident rate (10% without Form 15G/H).</li>"
         "<li><strong>NRE account</strong>: must be closed or converted. Options:</li>"
         "<li>&nbsp;&nbsp;&mdash; Transfer balance to Regular Savings (if NRE funds are repatriable, they lose that status once converted).</li>"
         "<li>&nbsp;&nbsp;&mdash; Transfer to RFC (preserves foreign currency + repatriable status).</li>"
         "<li>&nbsp;&nbsp;&mdash; Early-close NRE and remit funds abroad before becoming resident.</li>"
         "<li><strong>FCNR deposit</strong>: continue until maturity; then transfer to RFC. Early-close is penalty-chargeable.</li>"
         "<li><strong>PIS (Portfolio Investment Scheme) account</strong>: close / transfer securities to resident demat.</li>"
         "<li><strong>Mutual fund + demat KYC</strong>: update to resident. Change of address + bank account linking.</li>"
         "<li><strong>Insurance policies</strong>: notify insurer of status change.</li>"
         "<li><strong>Credit card + loan accounts</strong>: notify of status change.</li>"
         "</ol>"),
        ("/ Tax treatment transition", "The RNOR optimisation.",
         "<ul>"
         "<li><strong>Returning NRI typically gets RNOR status</strong> for 2-3 years post-return (per Section 6(6) &mdash; see <a href='nri-residential-status-rnor-india.html'>RNOR guide</a>).</li>"
         "<li><strong>During RNOR</strong>: foreign-source investment income + overseas rental + foreign capital gain remain non-taxable in India. Only India-source + foreign business controlled from India + foreign profession set up in India are taxable.</li>"
         "<li><strong>RFC interest</strong>: taxable in India (received in India) &mdash; even during RNOR.</li>"
         "<li><strong>NRE interest</strong>: during RNOR, interest from NRE / FCNR period before residence trigger remains tax-exempt (as it accrued during NRI status). Interest on balance after FEMA residence trigger is taxable even if account is still technically NRE.</li>"
         "<li><strong>Full resident status</strong> (post RNOR, typically year 4): global income taxable. Foreign Tax Credit (Section 90/91) available.</li>"
         "<li><strong>Planning</strong>: during RNOR window, consolidate foreign assets, repatriate large amounts (while tax-free in India via RNOR exemption), structure holdings to minimise post-RNOR tax hit.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("When do I need to convert my NRE/NRO account after returning to India?",
         "Within reasonable time of becoming FEMA resident - typically 60-90 days post-arrival with settled intention to stay. FEMA residence (Section 2(v)) is distinct from Income Tax residence and can trigger even before 182 days physical presence if intention + employment / business set up suggests settlement. Prolonged operation of NRE/NRO as resident = FEMA breach + potential compounding under Section 13."),
        ("What is RFC account and should I open one?",
         "RFC (Resident Foreign Currency) account - foreign currency-denominated account for Indian residents who were NRI for 1+ year. Preserves foreign currency + fully repatriable + no balance limit. Interest taxable in India. Useful if you may re-expatriate, receive foreign pension, hold foreign currency savings. Alternative to converting NRE to Regular Savings (which loses foreign currency + repatriable status)."),
        ("What happens to my FCNR deposit when I return?",
         "FCNR-B deposit continues until maturity (interest tax-exempt during NRI status period preserved). At maturity, cannot renew as FCNR-B (only NRIs can hold). Transfer to RFC account to preserve foreign currency denomination. Early closure is penalty-chargeable - avoid unless urgent."),
        ("Will my NRE interest be taxable after I return to India?",
         "Interest accrued during NRI period (before FEMA residence trigger): tax-exempt. Interest accrued after becoming FEMA resident: taxable even if account is still technically NRE. Convert NRE promptly after returning; keeping NRE operational post-FEMA-residence doesn't give you tax exemption and risks FEMA breach."),
        ("Can I keep some money in NRE after I return?",
         "Technically no - FEMA requires NRE conversion within reasonable time of becoming resident. Practical workaround: convert NRE balance to RFC (preserves foreign currency + repatriable status). RFC is specifically designed for returning NRIs who want to retain foreign currency position."),
        ("Does BQP help with NRI account conversion on return?",
         "Yes - standard returning-NRI service. FEMA residence trigger analysis, bank conversion coordination, RFC account structuring, RNOR tax planning for 2-3 year transition, PIS / mutual fund / demat KYC update, insurance / loan status updates. Co-ordinated with Section 6 RNOR optimisation. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("nri-residential-status-rnor-india.html", "Guide", "RNOR Status"),
        ("nre-nro-fcnr-account-tax-rules.html", "Guide", "NRE/NRO/FCNR Tax"),
    ],
    cta_headline="Returning to India after NRI stint? Convert accounts within reasonable time.",
    cta_body="RFC + Regular Savings + FCNR maturity handling + RNOR tax optimisation during 2-3 year transition. BQP end-to-end for returning NRIs globally.",
))

# 10. NRI US Estate Tax
write_page("nri-us-estate-tax-indian-assets", page(
    slug="nri-us-estate-tax-indian-assets",
    title="NRI US Estate Tax on Indian Assets 2026 | Green Card + Citizen Planning - BQP",
    description="NRI / US green card holder / US citizen estate tax exposure on Indian assets 2026: USD 13.99M lifetime exemption (2026), Form 706, India-US no estate tax treaty, step-up basis, revocable trust structuring, QDOT for non-citizen spouse, gift tax annual exclusion USD 19K. Complete 2026 cross-border estate planning guide. CA Durgesh Chavda.",
    keywords="NRI US estate tax Indian assets, green card estate tax India, US citizen estate tax Indian property, Form 706 India, QDOT NRI spouse",
    hero_kicker="/ NRI Guide &middot; US Estate Tax &middot; Updated 2026-10-15",
    hero_title_html="US estate tax on Indian assets, <em>what NRIs often miss.</em>",
    hero_lead="US citizen or green card holder dies with Indian property / Indian company shares / Indian bank balance &mdash; those assets are included in US estate for US estate tax. USD 13.99M lifetime exemption (2026) is generous but TCJA sunset reduces it to ~USD 7M in 2026 if Congress doesn't act. No India-US estate tax treaty means potential double tax. Here's the complete 2026 planning framework.",
    sections=[
        ("/ The US estate tax reach", "Why it matters.",
         "<ul>"
         "<li><strong>US estate tax (IRC Section 2001-2210)</strong>: taxes worldwide gross estate of US citizen / US domiciliary at death at graduated rates up to 40%.</li>"
         "<li><strong>US citizens</strong>: worldwide assets taxed. No geographic limit.</li>"
         "<li><strong>US green card holders (LPR, domiciliaries)</strong>: worldwide assets taxed if domiciled in US. Domicile = physical presence + intent to remain permanently.</li>"
         "<li><strong>Non-US-domiciled aliens (NRIs without green card)</strong>: only US-situs assets taxed (US real estate, US company shares, US tangibles in US).</li>"
         "<li><strong>Lifetime exemption 2026</strong>: USD 13.99 million per person (indexed). TCJA provision &mdash; sunsets end of 2025 to ~USD 7 million (2026 inflation-adjusted ~USD 7-7.5M) unless Congress extends. Significant uncertainty.</li>"
         "<li><strong>Rate</strong>: 40% on amounts above exemption.</li>"
         "<li><strong>Form 706</strong>: US Estate Tax Return. Filed within 9 months of death (6-month extension possible).</li>"
         "</ul>"),
        ("/ Indian assets in US estate", "What's included.",
         "<ul>"
         "<li><strong>Indian real estate</strong>: residential + commercial property. Valued at fair market value on date of death.</li>"
         "<li><strong>Indian company shares</strong>: listed + unlisted. Listed at NSE/BSE closing price; unlisted at FMV (DCF or NAV).</li>"
         "<li><strong>Indian mutual fund + ETF holdings</strong>.</li>"
         "<li><strong>Indian bank balances</strong>: NRE, NRO, FCNR &mdash; all at date-of-death balance (converted at date-of-death FX rate).</li>"
         "<li><strong>Indian partnership + LLP interests</strong>.</li>"
         "<li><strong>Indian provident fund + superannuation</strong> balances (complex &mdash; depends on fund type).</li>"
         "<li><strong>Indian insurance policy proceeds payable to estate</strong> (not payable to named beneficiary &mdash; those bypass estate).</li>"
         "<li><strong>Indian jewellery / valuables</strong>: Indian location + Indian valuation.</li>"
         "</ul>"
         "<p>All added to US estate at FX-converted fair market value as of date of death.</p>"),
        ("/ No India-US estate tax treaty", "The double-tax risk.",
         "<ul>"
         "<li>India abolished estate duty in 1985 &mdash; no Indian estate tax.</li>"
         "<li>US estate tax does apply to US citizens / domiciliaries on worldwide assets including Indian.</li>"
         "<li>No India-US estate tax treaty means no formal mechanism to avoid double tax (though double tax is unlikely because India has no estate tax).</li>"
         "<li><strong>Transfer stamp duty in India</strong>: when Indian property transfers to heirs post-death, stamp duty + registration applicable in India (varies by state, typically 2-7% of circle rate). Not a 'tax' per se but a real cost.</li>"
         "<li><strong>Capital gain at future sale</strong>: Indian heirs who later sell inherited property pay Indian capital gain tax on sale. Cost of acquisition for them = cost in NRI's hands + indexation (not FMV at death). Important: no Indian step-up at death (unlike US).</li>"
         "</ul>"),
        ("/ Planning strategies", "Reducing exposure.",
         "<ul>"
         "<li><strong>Annual gift exclusion</strong>: USD 19,000 per donee per year (2026). Gift Indian assets gradually to US-citizen spouse or US-citizen children. Reduces estate while using annual exclusion.</li>"
         "<li><strong>Spousal unlimited marital deduction</strong>: unlimited for US-citizen spouse. Transfer all Indian assets to US-citizen spouse via Will &mdash; no estate tax on first death. Second-to-die planning needed.</li>"
         "<li><strong>QDOT (Qualified Domestic Trust)</strong>: for non-US-citizen spouse, standard marital deduction not available. QDOT structure (US trust with US trustee) qualifies for marital deduction. Specific IRC Section 2056A rules.</li>"
         "<li><strong>Credit shelter trust</strong>: at first death, apply USD 13.99M exemption to a trust that grows outside survivor's estate. Standard US estate planning.</li>"
         "<li><strong>Lifetime gifts of Indian assets</strong>: value appreciation after gift stays with donee &mdash; reduces estate growth. Caution: gift tax applies to gifts above annual exclusion; uses lifetime unified exemption.</li>"
         "<li><strong>Life insurance for liquidity</strong>: Irrevocable Life Insurance Trust (ILIT) holds policy &mdash; proceeds outside estate.</li>"
         "<li><strong>Charitable giving</strong>: unlimited charitable deduction. Charitable Remainder Trust (CRT) can defer / reduce tax.</li>"
         "<li><strong>Pre-mortem planning for Indian property</strong>: joint ownership with US-citizen spouse / children can shift fractional interests out of estate. Must comply with Indian stamp duty + mutation.</li>"
         "<li><strong>Non-resident alien route</strong>: if green card holder willing to expatriate (Section 877A exit tax applies), post-expatriation only US-situs assets in US estate. Indian assets outside US estate.</li>"
         "</ul>"),
        ("/ TCJA sunset risk", "What to watch.",
         "<ul>"
         "<li><strong>Current USD 13.99M exemption (2026) is temporary</strong> &mdash; set by TCJA 2017 to double the pre-2017 exemption. Scheduled to sunset end of 2025 (2026 fiscal year start) to roughly half (~USD 7M in 2026 inflation-adjusted terms).</li>"
         "<li><strong>Congress</strong> may extend / modify in 2025-2026 tax legislation. Significant political uncertainty.</li>"
         "<li><strong>Planning action</strong>: NRI with large estate (above ~USD 7M including Indian assets) should consider using current USD 13.99M exemption via lifetime gifting + trust structuring BEFORE potential sunset.</li>"
         "<li><strong>Clawback rule</strong>: IRS has stated that gifts using 2017-2025 doubled exemption will NOT be clawed back after 2025 sunset. 'Use it or lose it' planning advantageous.</li>"
         "</ul>"
         "<p><em>Last updated: 2026-10-15.</em></p>"),
    ],
    faqs=[
        ("Do my Indian assets face US estate tax if I'm a US citizen or green card holder?",
         "Yes. US citizens are taxed on worldwide gross estate at death; same for US-domiciled green card holders. Indian real estate, Indian company shares, Indian bank balances, Indian mutual funds all included in US estate at FX-converted fair market value on date of death. Lifetime exemption USD 13.99M (2026) - amount above exempted threshold taxed at up to 40%."),
        ("What happens when TCJA exemption sunsets in 2026?",
         "Current USD 13.99M lifetime exemption is scheduled to roughly halve to ~USD 7M in 2026 (TCJA sunset). Congress may extend / modify. If sunset occurs, estate tax exposure increases materially for mid-wealthy NRI estates. Planning action: use current USD 13.99M via lifetime gifting + trust structuring BEFORE sunset. IRS has confirmed no clawback for gifts made at higher exemption."),
        ("Is there an India-US estate tax treaty?",
         "No - India abolished estate duty in 1985 and has no estate tax. US estate tax applies to US citizens / domiciliaries on worldwide assets including Indian. No treaty mechanism exists but double tax is practically avoided because India has no estate tax. However: Indian stamp duty on heir mutation (2-7% of circle rate) applies; Indian capital gain on heir's later sale uses NRI's cost basis (no Indian step-up at death)."),
        ("Can I give my Indian property to my US-citizen spouse to avoid estate tax?",
         "Yes - unlimited marital deduction for US-citizen spouse. Transfer Indian property to US-citizen spouse via lifetime gift or Will - no US estate tax on first death. Second-to-die planning needed for ultimate exposure. If spouse is NOT US citizen, standard marital deduction unavailable - use QDOT (Qualified Domestic Trust) structure under IRC Section 2056A to qualify."),
        ("What is QDOT and when do I need one?",
         "Qualified Domestic Trust - US trust with US trustee holding assets for benefit of non-US-citizen spouse. Qualifies for US estate tax marital deduction (which is otherwise unavailable for non-citizen spouse under IRC Section 2056(d)). Specific rules: US trustee + distribution restrictions. Used by US citizen/green card holder who dies with non-US-citizen spouse, especially NRI couples where one has US status and other doesn't."),
        ("Does BQP coordinate cross-border estate planning?",
         "Yes - India-side coordination with US estate planning counsel. Indian asset valuation + Form 706 Indian-asset schedule preparation + Indian mutation / transfer coordination post-death + QDOT Indian-asset administration + Indian capital gain planning for heirs + Indian stamp duty optimisation. Co-ordinates with US estate attorney for Form 706 + lifetime gift strategy + trust funding. WhatsApp +91 78018 87130."),
    ],
    related=[
        ("us-green-card-holder-india-tax-complete-2026.html", "Guide", "Green Card India Tax"),
        ("nri-inheritance-indian-property-tax-fema-2026.html", "Guide", "NRI Inheritance"),
    ],
    cta_headline="US citizen or green card holder with Indian assets?",
    cta_body="USD 13.99M exemption + TCJA sunset risk + QDOT for non-citizen spouse + Indian mutation / stamp duty planning. BQP co-ordinates with US estate attorney for comprehensive India-US planning.",
))

print("Batch O part 1 complete: 10 NRI trending pages written")
