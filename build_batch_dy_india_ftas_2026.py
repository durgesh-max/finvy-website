# -*- coding: utf-8 -*-
"""Batch DY (20 Nov 2026): India's trade agreements in 2026 and what they mean for foreign companies setting up,
sourcing or selling in India. Call-first page.
Demand: sweep 20 Nov 2026 (ac19), all 7 markets: "india oman cepa", "india new zealand fta", "india eu fta 2026",
"india australia ecta", "india efta tepa investment", "which countries have free trade agreements with india".
Facts (checked 20 Nov 2026; PIB year-end review, India Briefing FTA tracker, Wikipedia, ATB Legal): India-EFTA TEPA in
force October 2025 (EFTA states' USD 100 billion investment and 1 million jobs aspiration over 15 years); India-UK CETA
signed July 2025, in force July 2026 (15 July per Wikipedia), with a double contribution convention on social security;
India-Oman CEPA signed December 2025 (in force reported June 2026 - single source); India-New Zealand FTA announced 22
December 2025, signed 27 April 2026, reported in force 20 October 2026 (Wikipedia); India-EU FTA concluded 27 January
2026, signature and ratification pending; India-UAE CEPA in force 1 May 2022; India-Australia ECTA in force 29 December
2022. Benefits need rules-of-origin compliance and certificates of origin."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
FTA = "india-free-trade-agreements-2026-uk-eu-efta-uae-oman-australia-new-zealand-foreign-companies"
HUB = "foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026"
CP1 = "china-plus-one-india-moving-sourcing-manufacturing-to-india-foreign-company-2026"

C_FTA = contact("your country, product or service, and whether you want to source from India, manufacture in India, or sell into India")
PAGES = [dict(
    slug=FTA,
    title="India's Trade Agreements in 2026 (UK, EU, EFTA, UAE, Oman, Australia, New Zealand): What They Mean for Foreign Companies Sourcing, Manufacturing or Selling in India",
    em="status, benefits and the compliance that unlocks them.",
    kicker="/ Foreign companies &middot; Trade agreements &middot; Updated 2026-11-20",
    lead=("India's trade-agreement network expanded quickly in 2025-26. The <strong>India-EFTA TEPA</strong> (Switzerland, Norway, Iceland, Liechtenstein) took effect in <strong>October 2025</strong>, with an aspiration of <strong>USD 100 billion of EFTA investment</strong> over 15 years. The <strong>India-UK CETA</strong>, signed in July 2025, took effect in <strong>July 2026</strong>, alongside a social security convention for posted workers. The <strong>India-Oman CEPA</strong> was signed in December 2025. The <strong>India-New Zealand FTA</strong> was signed in April 2026. The <strong>India-EU FTA</strong> was concluded on 27 January 2026 and is awaiting signature and ratification. These sit alongside the <strong>India-UAE CEPA</strong> (since May 2022) and the <strong>India-Australia ECTA</strong> (since December 2022). "
          "For a foreign company, the value is lower duties on goods moving between India and the partner country, easier services and mobility terms, and a stronger case for <strong>manufacturing or sourcing in India for export</strong>. The duty benefit only applies if the goods meet the <strong>rules of origin</strong> and carry a valid certificate of origin, which is where most claims fail."),
    sections=[
        ("/ Where each agreement stands", "As reported on 20 November 2026; confirm before relying on a date.",
         table(["Agreement", "Status", "What foreign companies notice"], [
             ["India-UAE CEPA", "In force since 1 May 2022", "Tariff cuts both ways; UAE as a hub for India trade"],
             ["India-Australia ECTA", "In force since 29 December 2022", "Tariff cuts; broader agreement under negotiation"],
             ["India-EFTA TEPA", "In force since October 2025", "Investment and jobs commitment; tariff cuts for Swiss, Norwegian and other EFTA goods"],
             ["India-UK CETA", "Signed July 2025; in force July 2026", "Tariff cuts; services and mobility terms; social security convention for posted workers"],
             ["India-Oman CEPA", "Signed December 2025 (reported in force mid-2026)", "Tariff cuts; Gulf manufacturing and logistics links"],
             ["India-New Zealand FTA", "Signed April 2026 (reported in force October 2026)", "Tariff cuts and services commitments"],
             ["India-EU FTA", "Concluded 27 January 2026; signature and ratification pending", "Large tariff cuts expected once in force; plan supply chains now"]])
         + call_box("India's trade agreements", ["Whether your product qualifies under the rules of origin",
                                                  "Sourcing vs contract manufacturing vs your own plant in India for export",
                                                  "Customs, GST and certificate-of-origin compliance",
                                                  "Entity, tax and transfer pricing if you set up in India",
                                                  "Posting staff to India and social security"],
                    "your country, the products or services, current supply route and target volumes.")),
        ("/ Making the benefit real", "Where companies go wrong.",
         ul("<strong>Rules of origin:</strong> each agreement sets value-addition or tariff-shift tests; keep cost and bill-of-materials records that prove origin.",
            "<strong>Certificates of origin:</strong> issued through the designated agencies; errors lead to duty demands and penalties on audit.",
            "<strong>Customs and GST in India:</strong> concessional duty on imports needs correct classification and documentation; GST still applies; see <a href=\"india-iec-gst-customs-foreign-exporter-importer-2026.html\">IEC, GST and customs</a>.",
            "<strong>Manufacturing in India for export:</strong> combine agreement benefits with India's manufacturing incentives; see <a href=\"" + CP1 + ".html\">China plus one: moving to India</a>.",
            "<strong>Services and people:</strong> mobility chapters and social security conventions reduce cost for posted staff; see <a href=\"expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html\">expat tax in India</a>.",
            "<strong>Tax treaties are separate:</strong> trade agreements do not change income-tax treaty rates; see the <a href=\"india-qatar-dtaa-2026-new-tax-treaty-rates-nri-qatar-investment-india.html\">Qatar</a> and <a href=\"india-oman-dtaa-protocol-2026-royalty-fts-10-percent-nri-oman-tax.html\">Oman</a> treaty updates.")
         + f'<p>Related: <a href="{HUB}.html">working with an Indian CA as a foreign company</a> &middot; <a href="find-distributor-business-partner-in-india-foreign-company-agreement-checks-2026.html">finding a partner in India</a>.</p>'
         + sources("Ministry of Commerce and Industry, PIB year-end review of India&rsquo;s FTAs for 2025-26; India Briefing FTA tracker; ATB Legal FTA tracker; agreement texts (India-UAE CEPA, India-Australia ECTA, India-EFTA TEPA, India-UK CETA, India-Oman CEPA, India-New Zealand FTA). Dates are as reported on 20 November 2026; some in-force dates come from single sources, so confirm with the latest notifications.")),
    ],
    faqs=[("Which countries have free trade agreements with India in 2026?", "In force: UAE (CEPA), Australia (ECTA), EFTA states (TEPA), the UK (CETA, from July 2026), and reportedly Oman and New Zealand; plus older agreements such as those with ASEAN, Japan and South Korea. The India-EU FTA was concluded in January 2026 and awaits signature."),
          ("Is the India-EU FTA in force?", "Not yet. It was concluded on 27 January 2026; signature and ratification were pending as of November 2026."),
          ("What does the India-UK trade agreement change for UK companies?", "Lower tariffs on many goods, services and mobility commitments, and a social security convention that helps posted workers avoid double contributions."),
          ("How do companies claim lower duty under an FTA?", "By meeting the agreement's rules of origin and presenting a valid certificate of origin, with records that prove origin if customs audits the claim."),
          ("Do trade agreements change income-tax rates?", "No. Income-tax treaty rates on dividends, interest and royalties are set by separate tax treaties."),
          ("Can BQP help us use India's trade agreements?", "Yes, on structure, tax, customs and GST compliance. " + C_FTA)],
    related=[(CP1 + ".html", "China plus one: moving to India"), ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "IEC, GST and customs"),
             (HUB + ".html", "Working with an Indian CA")],
    cta_h="Using India's trade agreements?", cta_b=C_FTA,
    keywords="India free trade agreements 2026, India UK CETA in force, India EU FTA status, India EFTA TEPA investment, India Oman CEPA, India New Zealand FTA, India Australia ECTA, India UAE CEPA, rules of origin India FTA",
    desc="India's trade agreements in 2026: EFTA TEPA (Oct 2025), UK CETA (in force July 2026), Oman CEPA (signed Dec 2025), New Zealand FTA (signed Apr 2026), EU FTA (concluded Jan 2026, pending), UAE CEPA and Australia ECTA; what they mean for foreign companies, rules of origin and compliance.",
    howto={"name": "How a foreign company uses India's trade agreements", "description": "From product check to compliant claims.", "steps": [
        {"name": "Check the agreement", "text": "Status and tariff schedule for your product and country."},
        {"name": "Test rules of origin", "text": "Value-addition or tariff-shift test with cost records."},
        {"name": "Choose the India model", "text": "Sourcing, contract manufacturing or own plant."},
        {"name": "Set up compliance", "text": "Classification, certificates of origin, customs and GST records."},
        {"name": "Review yearly", "text": "Agreements phase in tariff cuts; update sourcing and pricing."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DY complete:", len(PAGES))
