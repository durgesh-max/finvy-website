# -*- coding: utf-8 -*-
"""Batch DP (19 Nov 2026): India-Oman treaty as amended by the 2025 Protocol (effective in India from 1 April 2026) and
India-Saudi Arabia treaty basics, for Gulf NRIs and companies. Call-first pages.
Demand: Gulf sweep 19 Nov 2026 (ac17) - "saudi investment in india", "ksa investment in india", Oman/Saudi NRI tax;
news: India-Oman Protocol signed 27 Jan 2025, in force 28 May 2025, Notification No. 69/2025 (25 June 2025),
effective in India for income from 1 April 2026 (EY 30 Sep 2025, Taxmann, BDO).
Oman facts: royalties and fees for technical services cut from 15% to 10%; preamble against non-taxation and treaty
shopping; principal purpose test (Article 27B); exchange of information substituted (banking and ownership data cannot
be refused); new assistance-in-collection article; tie-breaker for non-individuals by mutual agreement (POEM,
incorporation); new non-discrimination article; corresponding transfer-pricing adjustments; tax-sparing credit deleted;
interest 10% (PwC); dividend article not changed by the protocol.
Saudi facts (secondary: CalcGuru, Beacon Filing, Income Tax Department rate charts): dividends 5%, interest 10%,
royalties 10% with TRC and Form 10F; no separate fees-for-technical-services article per most sources (one lists 10%)
- technical services without a PE generally fall under business profits; hedge and advise checking the treaty."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
OM = "india-oman-dtaa-protocol-2026-royalty-fts-10-percent-nri-oman-tax"
SA = "india-saudi-arabia-dtaa-tax-treaty-rates-nri-saudi-company-investment-india-2026"
QA = "india-qatar-dtaa-2026-new-tax-treaty-rates-nri-qatar-investment-india"

PAGES = []

C_OM = contact("whether you are an Oman-based individual or company, your Indian income or contracts, and your tax residency certificate status")
PAGES.append(dict(
    slug=OM,
    title="India-Oman Tax Treaty Amended from 1 April 2026: Royalty and Technical Fees Cut to 10%, Anti-Abuse Test and What Oman-Based NRIs and Companies Should Do",
    em="the 2025 Protocol explained.",
    kicker="/ Oman &middot; NRIs &middot; Gulf companies &middot; Tax treaty &middot; Updated 2026-11-19",
    lead=("India and Oman amended their tax treaty by a <strong>Protocol signed on 27 January 2025</strong>. It entered into force on 28 May 2025, was notified as <strong>Notification No. 69/2025</strong>, and applies in India to income from <strong>1 April 2026</strong>. "
          "The biggest practical change: <strong>royalties and fees for technical services</strong> paid from India to Oman residents are now taxed at <strong>10% instead of 15%</strong>. The Protocol also adds a <strong>principal purpose test</strong> that denies benefits to arrangements set up mainly to get them, broader <strong>exchange of information</strong> (banking and ownership data can no longer be refused), <strong>assistance in collecting tax</strong>, a mutual-agreement <strong>tie-breaker for dual-resident companies</strong>, and a non-discrimination article. "
          "Omani consultants and licensors billing Indian clients should update withholding from April 2026. Oman-based NRIs claiming treaty rates need an Omani tax residency certificate and Form 10F."),
    sections=[
        ("/ What the Protocol changes", "Old vs new.",
         table(["Item", "Before", "From 1 April 2026 (India)"], [
             ["Royalties", "15%", "10%"],
             ["Fees for technical services", "15%", "10%"],
             ["Interest", "10%", "Not changed by the Protocol"],
             ["Dividends", "Treaty rates by shareholding", "Not changed by the Protocol"],
             ["Anti-abuse", "No principal purpose test", "Principal purpose test and anti-treaty-shopping preamble"],
             ["Dual-resident companies", "Place of effective management", "Competent authorities decide by mutual agreement (management, incorporation and other factors)"],
             ["Exchange of information", "Older wording", "Substituted article; banking and ownership information cannot be refused; new assistance in collection"],
             ["Other", "Tax-sparing credit", "Tax-sparing deleted; corresponding transfer-pricing adjustments; non-discrimination article"]])
         + call_box("the India-Oman tax treaty", ["The withholding rate for your royalties or technical fees from April 2026",
                                                   "Whether your structure passes the principal purpose test",
                                                   "TRC, Form 10F and no-PE documents for Indian payers",
                                                   "Permanent establishment risk for projects in India",
                                                   "Refunds of excess tax withheld"],
                    "your Omani residency details, invoices or contracts with Indian clients, and any group structure.")),
        ("/ What to do now", "For individuals and companies.",
         ul("<strong>Omani service providers and licensors:</strong> ask Indian clients to withhold at 10% on royalties and technical fees for payments from April 2026, backed by a TRC, Form 10F (Form 41 under the new rules) and a no-PE declaration.",
            "<strong>Oman-based NRIs:</strong> NRO interest and other Indian income can get treaty rates with a TRC; NRE and FCNR interest stays exempt while non-resident; check India's deemed-residence rule if Indian income exceeds INR 15 lakh; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for Gulf NRIs</a>.",
            "<strong>Holding and financing structures:</strong> review against the principal purpose test before relying on treaty rates.",
            "<strong>Disputes:</strong> the mutual agreement procedure was updated; act within the treaty's time limit once you receive an adverse action.")
         + f'<p>Related: <a href="{QA}.html">new India-Qatar treaty</a> &middot; <a href="{SA}.html">India-Saudi Arabia treaty</a> &middot; <a href="indian-ca-for-clients-in-uae-gulf.html">Indian CA for Gulf clients</a> &middot; <a href="technology-licensing-royalty-payment-indian-company-to-foreign-company-fema-tds-gst-2026.html">royalty payments from India</a>.</p>'
         + sources("Protocol amending the India-Oman Convention (signed 27 January 2025, in force 28 May 2025); CBDT Notification No. 69/2025 dated 25 June 2025. Commentary checked 19 November 2026: EY (30 September 2025), Taxmann (27 June 2025), BDO India (3 July 2025), PwC Middle East (interest rate). Confirm rates against the notified text before applying.")),
    ],
    faqs=[("What changed in the India-Oman tax treaty?", "A 2025 Protocol cut the rate on royalties and fees for technical services from 15% to 10%, added a principal purpose test, broadened exchange of information and added assistance in collection, a mutual-agreement tie-breaker for dual-resident companies and a non-discrimination article."),
          ("When does the amended India-Oman treaty apply?", "The Protocol entered into force on 28 May 2025 and applies in India to income from 1 April 2026 (FY 2026-27)."),
          ("What is the withholding rate on technical fees paid to Oman?", "10% from 1 April 2026 (previously 15%), with a tax residency certificate and Form 10F, if no permanent establishment exists in India."),
          ("Did dividend or interest rates change?", "The Protocol did not change the dividend or interest articles; interest remains at 10% under the treaty."),
          ("What do Oman-based NRIs need for treaty rates?", "An Omani tax residency certificate and Form 10F (Form 41 under the new rules), given to the Indian payer."),
          ("Can BQP apply the amended treaty for us?", "Yes. " + C_OM)],
    related=[(QA + ".html", "New India-Qatar treaty"), (SA + ".html", "India-Saudi Arabia treaty"), ("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for Gulf clients")],
    cta_h="Living in Oman or billing Indian clients from Oman?", cta_b=C_OM,
    keywords="India Oman DTAA 2026, India Oman protocol 2025, India Oman DTAA royalty 10 percent, fees for technical services Oman India, Oman NRI tax India, India Oman treaty principal purpose test, Notification 69/2025",
    desc="India-Oman tax treaty amended from 1 April 2026 (Protocol signed 27 Jan 2025, Notification 69/2025): royalties and technical fees cut from 15% to 10%, principal purpose test, wider information exchange and collection assistance, tie-breaker for companies; actions for Oman-based NRIs and companies.",
    howto={"name": "How to apply the amended India-Oman treaty", "description": "Steps from April 2026.", "steps": [
        {"name": "Get an Omani TRC", "text": "Tax residency certificate for the relevant year."},
        {"name": "File Form 10F", "text": "Submit Form 10F (Form 41) and give it with the TRC to the Indian payer."},
        {"name": "Update withholding", "text": "10% on royalties and technical fees from 1 April 2026."},
        {"name": "Test structures", "text": "Check holding and financing arrangements against the principal purpose test."},
        {"name": "Recover excess tax", "text": "File an Indian return for refunds of over-withheld tax."}]}))

C_SA = contact("whether you are a Saudi-based individual or company, your Indian income or planned investment, and your residency certificate status")
PAGES.append(dict(
    slug=SA,
    title="India-Saudi Arabia Tax Treaty (2026): Rates on Dividends, Interest and Royalties, Technical Services, and What Saudi-Based NRIs and Saudi Companies Need",
    em="for Saudi-based NRIs and companies investing in or billing India.",
    kicker="/ Saudi Arabia &middot; NRIs &middot; Gulf companies &middot; Tax treaty &middot; Updated 2026-11-19",
    lead=("Under the India-Saudi Arabia tax treaty, Indian <strong>dividends</strong> paid to a Saudi resident are taxed in India at up to <strong>5%</strong>, and <strong>interest</strong> and <strong>royalties</strong> at up to <strong>10%</strong>, instead of the domestic 20% to 30% plus surcharge and cess. To get these rates the recipient needs a <strong>Saudi tax residency certificate</strong> and Form 10F. "
          "Most commentators read the treaty as having <strong>no separate article on fees for technical services</strong>. A Saudi firm's technical services to India, without a permanent establishment here, are then generally treated as business profits. Payments that transfer know-how can still be royalties. This point needs case-by-case review. "
          "Saudi-based NRIs mainly use the treaty for <strong>NRO interest and dividends</strong>. NRE and FCNR interest is already exempt in India while they are non-resident, and Saudi Arabia does not tax individuals on that income."),
    sections=[
        ("/ Rates at a glance", "Treaty vs Indian domestic law.",
         table(["Income from India", "Treaty rate (beneficial owner)", "Indian domestic rate (non-resident)", "Notes"], [
             ["Dividends", "5%", "20% plus surcharge and cess", "Needs TRC and Form 10F"],
             ["Interest (including NRO interest)", "10%", "Up to 30% for individuals (20% on certain foreign-currency loans) plus surcharge and cess", "Excess interest between related parties taxed under domestic law"],
             ["Royalties", "10%", "20% plus surcharge and cess", "Covers IP, copyrights, patents and know-how"],
             ["Fees for technical services", "No separate article per most sources (one source lists 10%)", "20% plus surcharge and cess", "Without a PE, often business profits; review each contract"],
             ["Capital gains on Indian shares and property", "Generally taxable in India", "Domestic rates", "Plan sales of Indian assets"]])
         + call_box("the India-Saudi Arabia tax treaty", ["The treaty rate on your dividends, interest, royalties or service fees",
                                                           "Whether your technical services are business profits or royalties",
                                                           "Permanent establishment risk for staff and projects in India",
                                                           "TRC, Form 10F and withholding documents",
                                                           "Investing in India from Saudi Arabia: entity, FDI route and repatriation"],
                    "your Saudi residency details, the type of Indian income or contract, and any planned investment.")),
        ("/ For Saudi-based NRIs and companies", "Practical points.",
         ul("<strong>NRIs:</strong> give the bank a Saudi TRC and Form 10F for NRO interest at 10%; claim refunds of excess TDS in an Indian return; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR for NRIs</a>. Watch India's deemed-residence rule if Indian income exceeds INR 15 lakh; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for Gulf NRIs</a>.",
            "<strong>Saudi companies investing in India:</strong> FDI route and sector caps apply; dividends from an Indian subsidiary can get 5%; see <a href=\"" + HUB + ".html\">working with an Indian CA as a foreign company</a>.",
            "<strong>Saudi service providers:</strong> confirm whether fees are business profits (no Indian tax without a PE) or royalties (10%), and give Indian clients a no-PE declaration where appropriate.",
            "<strong>Projects in India:</strong> track staff presence and project duration to manage permanent establishment risk.")
         + f'<p>Related: <a href="{QA}.html">new India-Qatar treaty</a> &middot; <a href="{OM}.html">amended India-Oman treaty</a> &middot; <a href="us-incorporation-for-saudi-founders.html">US incorporation for Saudi founders</a> &middot; <a href="indian-ca-for-clients-in-uae-gulf.html">Indian CA for Gulf clients</a>.</p>'
         + sources("Convention between India and the Kingdom of Saudi Arabia for the avoidance of double taxation; Income-tax Act, 2025; Income Tax Department treaty rate charts. Secondary sources checked 19 November 2026: CalcGuru, Beacon Filing, PwC Worldwide Tax Summaries. Sources differ on fees for technical services; confirm against the treaty text before applying.")),
    ],
    faqs=[("What is the dividend tax rate under the India-Saudi Arabia treaty?", "Up to 5% for a Saudi-resident beneficial owner with a tax residency certificate and Form 10F, compared with 20% plus surcharge and cess under Indian domestic law."),
          ("What tax applies on NRO interest for an NRI in Saudi Arabia?", "Up to 10% under the treaty with a Saudi TRC and Form 10F, instead of up to 30% plus surcharge and cess; excess TDS can be claimed back in an Indian return."),
          ("Does the India-Saudi treaty cover fees for technical services?", "Most sources say it has no separate article; such fees without a permanent establishment are generally business profits, unless they are really royalties for know-how. Review each contract."),
          ("Is NRE interest taxed for NRIs in Saudi Arabia?", "No. NRE and FCNR interest is exempt in India while you are non-resident, and Saudi Arabia does not tax individuals on it."),
          ("Can a Saudi company invest in India?", "Yes, through FDI subject to sector caps and approval routes; dividends from the Indian company can be taxed at the 5% treaty rate."),
          ("Can BQP apply the treaty for us?", "Yes. " + C_SA)],
    related=[(QA + ".html", "New India-Qatar treaty"), (OM + ".html", "Amended India-Oman treaty"), ("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for Gulf clients")],
    cta_h="Living in Saudi Arabia or investing from KSA?", cta_b=C_SA,
    keywords="India Saudi Arabia DTAA rates, India Saudi tax treaty dividend 5 percent, Saudi NRI tax India, NRO interest Saudi NRI TDS, Saudi company investment in India tax, fees for technical services India Saudi treaty, KSA investment in India",
    desc="India-Saudi Arabia tax treaty (2026): dividends 5%, interest and royalties 10% with TRC and Form 10F; fees for technical services generally business profits without a PE (sources differ); what Saudi-based NRIs and Saudi companies investing in or billing India should do.",
    howto={"name": "How to apply the India-Saudi treaty", "description": "Steps for NRIs and companies.", "steps": [
        {"name": "Get a Saudi TRC", "text": "Tax residency certificate for the relevant year."},
        {"name": "File Form 10F", "text": "Submit Form 10F (Form 41) and give both to the Indian payer."},
        {"name": "Classify the income", "text": "Dividend, interest, royalty or business profits from services."},
        {"name": "Check PE exposure", "text": "Staff presence and project duration in India."},
        {"name": "Recover excess tax", "text": "File an Indian return for refunds of over-withheld tax."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DP complete:", len(PAGES))
