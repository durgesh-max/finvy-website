# -*- coding: utf-8 -*-
"""Batch DO (19 Nov 2026): the revised India-Qatar tax treaty, effective in India from 1 April 2026 - what changes for
Qatar-based NRIs and Qatari companies investing in India. Call-first page. Demand: Gulf sweep 19 Nov 2026 (ac17) -
"qatar investment in india", "qatari investment in india", "qatar investment authority india"; news: revised treaty
signed 18 Feb 2025, in force 10 Sep 2025, notified by CBDT Notification No. 154/2025 dated 24 Oct 2025 (G.S.R.
789(E)), effective in India for income from 1 April 2026 and in Qatar from 1 January 2026 (Taxmann, KPMG, AZB).
Facts (secondary commentary checked 19 Nov 2026): replaces the 1999 treaty; dividends 5% where the beneficial owner
holds at least 25% (previously 10%), otherwise 10%; dividends to the other state or its subdivisions exempt in source;
interest article covers Islamic finance instruments; sovereign interest exemption names RBI and EXIM Bank (India) and
Qatar Investment Authority and Qatar Holding LLC (Qatar); interest, royalties and fees for technical services reported
at 10% (single secondary source - hedged); capital gains on shares deriving more than 50% of value from immovable
property taxable in the source state; service PE where services exceed 90 days in any 12 months; installation PE,
closely-related enterprise and anti-fragmentation rules; principal purpose test (Article 28); mutual-agreement
tie-breaker for non-individuals; student employment cap removed."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
QA = "india-qatar-dtaa-2026-new-tax-treaty-rates-nri-qatar-investment-india"

C_QA = contact("whether you are a Qatar-based individual or company, your Indian income or planned investment, and your tax residency certificate status")
PAGES = [dict(
    slug=QA,
    title="New India-Qatar Tax Treaty from 1 April 2026: Rates, Capital Gains, PE and Anti-Abuse Rules for Qatar-Based NRIs and Qatari Investors",
    em="what changed from the 1999 treaty and who it affects.",
    kicker="/ Qatar &middot; NRIs &middot; Gulf investors &middot; Tax treaty &middot; Updated 2026-11-19",
    lead=("India and Qatar signed a <strong>new tax treaty on 18 February 2025</strong> to replace the 1999 treaty. It entered into force on 10 September 2025 and was notified by CBDT Notification No. 154/2025. It applies in India to income arising on or after <strong>1 April 2026</strong>, and in Qatar from 1 January 2026. "
          "The key changes: the <strong>5% dividend rate now needs a 25% shareholding</strong> (it was 10%), with 10% in other cases. Interest now expressly covers <strong>Islamic finance</strong>, and interest to the <strong>Qatar Investment Authority and Qatar Holding</strong> is exempt in India. India can tax gains on <strong>shares of property-rich companies</strong> (more than 50% of value from Indian immovable property). A <strong>service PE</strong> arises after 90 days of services in 12 months. A <strong>principal purpose test</strong> denies benefits to arrangements set up mainly for treaty access. "
          "Qatar-based NRIs claiming treaty rates on Indian income need a <strong>Qatari tax residency certificate</strong> and Form 10F (Form 41 under the new rules)."),
    sections=[
        ("/ What changed", "Old treaty vs new treaty.",
         table(["Item", "New treaty (from 1 April 2026 in India)", "Who it affects"], [
             ["Dividends", "5% if the beneficial owner holds at least 25% (previously 10%); 10% otherwise; dividends to the other state itself exempt in the source state", "Qatari parents of Indian companies; Qatar-based NRI shareholders"],
             ["Interest", "Covers Islamic finance instruments similar to loans; exemption for RBI and EXIM Bank (India) and Qatar Investment Authority and Qatar Holding (Qatar); other interest reported at 10%", "Lenders, sukuk-type financing, sovereign investors; NRIs with NRO interest"],
             ["Royalties and technical fees", "Reported at 10%; confirm against the notified text", "Licensors and service providers"],
             ["Capital gains", "Source state may tax gains on shares deriving more than 50% of value from immovable property there", "Investors in Indian real-estate-heavy companies"],
             ["Permanent establishment", "Service PE after more than 90 days in any 12 months; installation PE; closely-related enterprise and anti-fragmentation rules", "Qatari contractors and consultants working in India"],
             ["Anti-abuse", "Principal purpose test; tie-breaker for companies by mutual agreement", "Holding and treaty-planning structures"]])
         + call_box("the India-Qatar tax treaty", ["Which treaty rate applies to your dividends, interest or fees from April 2026",
                                                    "Whether your structure passes the principal purpose test",
                                                    "PE exposure for projects and staff in India",
                                                    "Capital gains on Indian investments under the new article",
                                                    "TRC, Form 10F and withholding documents"],
                    "your Qatari residency details, the type of Indian income or investment, and any existing structure.")),
        ("/ For Qatar-based NRIs", "Practical points.",
         ul("<strong>NRO interest and dividends:</strong> give your Indian bank or company a Qatari tax residency certificate and Form 10F to get treaty rates instead of 30% or 20% plus surcharge and cess; claim refunds of excess TDS in your Indian return; see <a href=\"which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html\">which ITR for NRIs</a>.",
            "<strong>NRE and FCNR interest:</strong> exempt in India while you are non-resident; Qatar has no personal income tax on it.",
            "<strong>Deemed residence:</strong> an Indian citizen with Indian income above INR 15 lakh who is not liable to tax in any country can be treated as resident in India; see <a href=\"dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html\">deemed residence for Gulf NRIs</a>.",
            "<strong>Property and shares in India:</strong> capital gains on Indian property and most Indian shares remain taxable in India; see <a href=\"nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html\">selling property from abroad</a>.")),
        ("/ For Qatari companies and investors", "Before investing or contracting.",
         ul("<strong>Investing in India:</strong> FDI route and sector caps apply as for any foreign investor; see <a href=\"" + HUB + ".html\">working with an Indian CA as a foreign company</a> and <a href=\"how-to-acquire-a-company-in-india-foreign-buyer-process-fema-cci-tax-2026.html\">acquiring an Indian company</a>.",
            "<strong>Holding structure:</strong> to get the 5% dividend rate, the Qatari company must beneficially own at least 25% and pass the principal purpose test.",
            "<strong>Projects in India:</strong> track staff days; more than 90 days of services in 12 months can create a PE and Indian tax on profits.",
            "<strong>Financing:</strong> Islamic finance structures now fit the interest article; check withholding on each payment.")
         + '<p>Related: <a href="indian-ca-for-clients-in-uae-gulf.html">Indian CA for UAE and Gulf clients</a> &middot; <a href="india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html">India-UAE treaty for NRIs</a> &middot; <a href="gift-city-for-nri-investment-fd-funds-insurance-tax-2026.html">GIFT City for NRIs</a>.</p>'
         + sources("Agreement between India and Qatar for the elimination of double taxation (signed 18 February 2025) and Protocol; CBDT Notification No. 154/2025 dated 24 October 2025; Income-tax Act, 2025. Secondary commentary checked 19 November 2026: Taxmann (28 October 2025), KPMG (3 December 2025), AZB &amp; Partners (December 2025). Royalty, technical-fee and general interest rates are from secondary sources; confirm against the notified text before applying.")),
    ],
    faqs=[("When does the new India-Qatar tax treaty apply?", "It entered into force on 10 September 2025 and applies in India to income arising on or after 1 April 2026 (in Qatar from 1 January 2026), replacing the 1999 treaty."),
          ("What is the dividend tax rate under the new India-Qatar treaty?", "5% where the beneficial owner holds at least 25% of the paying company (previously 10%), and 10% in other cases; dividends paid to the other state itself are exempt in the source state."),
          ("Does the new treaty change tax on Indian shares sold by Qatar residents?", "India can tax gains on shares that derive more than 50% of their value from Indian immovable property, and most other Indian share gains remain taxable in India under domestic law."),
          ("What documents does a Qatar-based NRI need for treaty rates?", "A Qatari tax residency certificate and Form 10F (Form 41 under the new rules), given to the Indian payer before payment; excess tax can be claimed back in the Indian return."),
          ("Is interest paid to Qatar Investment Authority taxed in India?", "No. The protocol lists Qatar Investment Authority and Qatar Holding LLC among the bodies whose interest is exempt in the source state."),
          ("Can BQP apply the new treaty for us?", "Yes. " + C_QA)],
    related=[("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for Gulf clients"), ("india-uae-dtaa-for-nris-dubai-nro-interest-mutual-funds-property-trc-2026.html", "India-UAE treaty for NRIs"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Living in Qatar or investing from Qatar?", cta_b=C_QA,
    keywords="India Qatar DTAA 2026, new India Qatar tax treaty, India Qatar DTAA rates, Qatar NRI tax India, Qatar investment in India tax, Qatar Investment Authority India interest exemption, India Qatar treaty capital gains, India Qatar service PE 90 days",
    desc="New India-Qatar tax treaty from 1 April 2026: signed 18 Feb 2025, Notification 154/2025; 5% dividends at 25% holding (10% otherwise), Islamic finance and QIA interest exemption, capital gains on property-rich shares, 90-day service PE, principal purpose test; what Qatar-based NRIs and investors should do.",
    howto={"name": "How to use the new India-Qatar treaty from April 2026", "description": "Steps for NRIs and investors.", "steps": [
        {"name": "Get a Qatari TRC", "text": "Obtain the tax residency certificate for the relevant year."},
        {"name": "File Form 10F", "text": "Submit Form 10F (Form 41 under the new rules) and give both to the Indian payer."},
        {"name": "Check the rate", "text": "Dividends 5% or 10% by shareholding; confirm interest, royalty and fee rates."},
        {"name": "Review structures", "text": "Test holding companies against the principal purpose test; track PE days."},
        {"name": "Claim refunds", "text": "File an Indian return to recover excess tax withheld."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DO complete:", len(PAGES))
