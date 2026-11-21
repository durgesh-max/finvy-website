# -*- coding: utf-8 -*-
"""Batch EX (21 Nov 2026): REPLACES two October 2026 pages from build_batch_q_news.py that had unverified or stale claims.
1. india-uk-ceta-implementation-operational-2026.html - the old page said 'concluded in 2024-2025', '95%+ trade lines'
   and 'whisky 150% to ~75% over 10 years', and described an investment-protection chapter.
   Facts (checked 21 Nov 2026): CETA signed 24 July 2025; entered into force 15 July 2026 after ratification by both
   sides, delayed from an expected May 2026 (HLC; KPMG GMS Flash Alert 2026-154); UK tariffs removed on 99% of Indian
   goods on entry into force; India cuts tariffs on 90% of tariff lines covering 92% of UK goods exports, 64% tariff-free
   immediately (Deloitte / UK Parliament report summaries); Scotch whisky duty 150% to 75% on entry into force, 40%
   after ten years (so around 2036); customs classification dispute on bulk whisky reported (The Core, opinion);
   Double Contributions Convention in force the same day, 60 months with a certificate of coverage (KPMG).
2. dpdp-rules-january-2025-operational-status-october-2026.html - the old page said the final rules were still awaited.
   Facts (checked 21 Nov 2026; MirvoLegal 'as at September 2026', Corpus Juris, Privy by IDfy, Wikipedia): Digital
   Personal Data Protection Rules, 2025 notified by MeitY on 13 November 2025 (Gazette 14 November 2025); phased:
   Data Protection Board provisions from notification; consent manager registration (rule 4) from about 13 November
   2026; main duties (notice, consent, security safeguards, breach reporting, children's data, data principal rights)
   from about 13 May 2027; Board members not reported as appointed as of September 2026 (applications invited 6 May
   2026) though another source says constituted; January 2026 proposal to shorten 18 months to 12 not notified as of
   September 2026; DPDP Act penalties up to INR 250 crore."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
CETA = "india-uk-ceta-implementation-operational-2026"
DPDP = "dpdp-rules-january-2025-operational-status-october-2026"
SSA = "india-social-security-agreements-list-2026-uk-double-contributions-convention-us-totalization-certificate-of-coverage"

C1 = contact("whether you are exporting from India to the UK or from the UK to India, your products or services, and whether you plan to set up or post staff in the other country")
C2 = contact("what personal data of people in India you handle, whether you are in India or abroad, and what you have in place today for consent, security and breach response")
PAGES = [dict(
    slug=CETA,
    title="India-UK CETA: In Force Since 15 July 2026 - Tariff Cuts, Whisky Duty, Social Security Relief and What Businesses Should Do",
    em="the trade agreement, in plain terms.",
    kicker="/ India-UK &middot; Trade agreement &middot; Updated 2026-11-21",
    lead=("The <strong>India-UK Comprehensive Economic and Trade Agreement (CETA)</strong> was signed on 24 July 2025 and <strong>entered into force on 15 July 2026</strong>. "
          "The UK removed tariffs on <strong>99% of Indian goods</strong> from that day. India is cutting tariffs on <strong>90% of its tariff lines</strong>, covering about 92% of UK goods exports, with 64% tariff-free immediately and the rest phased. "
          "Duty on <strong>Scotch whisky</strong> fell from 150% to <strong>75%</strong> on entry into force and falls to 40% over ten years. "
          "A separate <strong>Double Contributions Convention</strong> started the same day: employees posted between the two countries can stay in their home social security system for up to 60 months. "
          "To use a lower tariff, the goods must meet the agreement&rsquo;s <strong>rules of origin</strong> and the importer must claim the preference with proof of origin. "
          "<em>This page was corrected on 21 November 2026; an earlier version gave the wrong dates and tariff figures.</em>"),
    sections=[
        ("/ What is in force", "Key facts.",
         table(["Point", "Position"], [
             ["Signed", "24 July 2025"],
             ["In force", "15 July 2026, after ratification by both countries"],
             ["Indian goods entering the UK", "Tariffs removed on 99% of goods from entry into force"],
             ["UK goods entering India", "Tariff cuts on 90% of tariff lines (about 92% of UK goods exports); 64% tariff-free immediately, others phased"],
             ["Scotch whisky", "150% to 75% on entry into force; 40% after ten years. A customs classification question on bulk whisky has been reported"],
             ["Social security", "Double Contributions Convention from 15 July 2026: up to 60 months in the home system with a certificate of coverage"],
             ["Claiming the lower tariff", "Goods must meet the rules of origin; the preference is claimed with proof of origin at import"]])
         + call_box("Using the India-UK trade agreement", ["Whether your product qualifies under the rules of origin",
                                                          "Landed cost before and after the tariff cut",
                                                          "Setting up in India or the UK: entity, tax and FEMA",
                                                          "Posting staff: the 60-month social security relief",
                                                          "Income tax treaty relief on dividends, royalties and service fees"],
                    "your products and HS codes or services, trade volumes, and any plans for an entity or staff in the other country.")),
        ("/ What to do", "Exporters, importers and investors.",
         ul("<strong>Indian exporters to the UK:</strong> check that your goods meet the product-specific origin rule and keep the supplier and production records that prove it.",
            "<strong>UK exporters to India:</strong> look up the staging for your tariff line; many cuts are phased over several years.",
            "<strong>Customs in India:</strong> see <a href=\"india-iec-gst-customs-foreign-exporter-importer-2026.html\">IEC, GST and customs for foreign exporters and importers</a>.",
            "<strong>Posting employees:</strong> see <a href=\"" + SSA + ".html\">social security agreements and the UK convention</a>.",
            "<strong>Tax on cross-border payments:</strong> the trade agreement does not change the income tax treaty; see the <a href=\"india-uk-tax-treaty-dtaa.html\">India-UK tax treaty</a>.",
            "<strong>Setting up in India:</strong> see <a href=\"india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html\">the India entry structure chooser</a> and <a href=\"indian-ca-for-clients-in-uk.html\">Indian CA for UK clients</a>.")
         + sources("India-UK Comprehensive Economic and Trade Agreement (signed 24 July 2025; in force 15 July 2026) as reported by HLC, Deloitte and the UK Parliament's Business and Trade Committee report; KPMG GMS Flash Alert 2026-154 on the Double Contributions Convention; whisky classification report in The Core. Check the tariff schedule and origin rule for your own product before pricing. Corrected on 21 November 2026.")),
    ],
    faqs=[("When did the India-UK trade agreement come into force?", "The India-UK Comprehensive Economic and Trade Agreement was signed on 24 July 2025 and entered into force on 15 July 2026."),
          ("What tariffs does the UK charge on Indian goods under CETA?", "The UK removed tariffs on 99% of Indian goods from entry into force, provided the goods meet the agreement's rules of origin."),
          ("What happens to Indian tariffs on UK goods?", "India is cutting tariffs on 90% of its tariff lines, covering about 92% of UK goods exports; 64% became tariff-free immediately and the rest are phased."),
          ("What is the duty on Scotch whisky in India now?", "It fell from 150% to 75% when the agreement entered into force and reduces to 40% over ten years."),
          ("Does the agreement cover social security?", "A separate Double Contributions Convention began on 15 July 2026: employees posted between India and the UK can remain in their home social security system for up to 60 months with a certificate of coverage."),
          ("Can BQP help us use the agreement?", "Yes. " + C1)],
    related=[("india-uk-tax-treaty-dtaa.html", "India-UK tax treaty"), (SSA + ".html", "Social security agreements"), ("indian-ca-for-clients-in-uk.html", "Indian CA for UK clients")],
    cta_h="Trading between India and the UK?", cta_b=C1,
    keywords="India UK CETA in force 15 July 2026, India UK FTA tariffs, India UK trade agreement whisky duty 75%, India UK free trade agreement rules of origin, Double Contributions Convention India UK",
    desc="India-UK CETA: signed 24 July 2025, in force 15 July 2026. UK tariffs removed on 99% of Indian goods; India cuts 90% of tariff lines (64% immediately); Scotch whisky duty 150% to 75%, then 40% over ten years; social security relief for posted staff up to 60 months.",
    howto={"name": "How to use the India-UK trade agreement", "description": "Steps for exporters and importers.", "steps": [
        {"name": "Find your tariff line", "text": "Check the rate and the staging under the agreement."},
        {"name": "Check the origin rule", "text": "Confirm the product-specific rule and gather proof."},
        {"name": "Claim the preference", "text": "Provide proof of origin at import."},
        {"name": "Review people and structure", "text": "Social security relief for posted staff; entity and tax set-up."}]}),
    dict(
    slug=DPDP,
    title="DPDP Rules 2025: Notified, With Main Duties From May 2027 - Timeline and What Indian and Foreign Companies Should Do Now",
    em="India&rsquo;s data protection rules, where they stand in November 2026.",
    kicker="/ Data protection &middot; DPDP Act and Rules &middot; Updated 2026-11-21",
    lead=("The <strong>Digital Personal Data Protection Rules, 2025</strong> were notified on <strong>13 November 2025</strong> under the DPDP Act, 2023. They apply in phases. "
          "Provisions on the <strong>Data Protection Board</strong> applied from notification. <strong>Consent manager registration</strong> opens about a year later, around <strong>13 November 2026</strong>. "
          "The <strong>main duties</strong> on businesses apply around <strong>13 May 2027</strong>: notices, consent, security safeguards, breach reporting, children&rsquo;s data and the rights of individuals. "
          "The Act reaches <strong>foreign companies</strong> that process personal data in connection with offering goods or services to people in India. Penalties run up to <strong>INR 250 crore</strong>. "
          "A proposal to bring the main date forward by six months was floated in January 2026 but had not been notified as of September 2026. "
          "<em>This page was corrected on 21 November 2026; an earlier version said the final rules were still awaited.</em>"),
    sections=[
        ("/ Timeline", "What applies when.",
         table(["Date", "What starts", "Who is affected"], [
             ["13 November 2025", "Rules notified; Data Protection Board provisions apply", "Government; the Board"],
             ["About 13 November 2026", "Consent manager registration (rule 4)", "Entities that want to act as consent managers"],
             ["About 13 May 2027", "Main duties: notice, consent, security safeguards, breach reporting, children&rsquo;s data, individuals&rsquo; rights, significant data fiduciary duties", "Every business handling digital personal data of people in India, including foreign companies offering goods or services to them"],
             ["Not yet settled", "Board appointments were not reported as complete as of September 2026; a proposal to shorten the 18 months to 12 was not notified", "Watch for notifications"]])
         + call_box("DPDP readiness for our business", ["Whether and how the Act applies to you, including from outside India",
                                                        "A gap list against the May 2027 duties",
                                                        "Notices, consent records and vendor contracts",
                                                        "Breach response and record keeping",
                                                        "How this fits with GDPR or other regimes you already follow"],
                    "a short description of the personal data you hold on people in India, your systems and vendors, and any existing privacy programme.")),
        ("/ What to do before May 2027", "A practical order of work.",
         ul("<strong>Map the data:</strong> what personal data of people in India you collect, why, where it sits and who processes it for you.",
            "<strong>Notices and consent:</strong> rewrite notices in clear language and build a way to record and withdraw consent.",
            "<strong>Security and breach response:</strong> put reasonable safeguards in place and a process to notify the Board and affected people of a breach.",
            "<strong>Vendors:</strong> update contracts with processors so they follow your instructions and safeguards.",
            "<strong>Children&rsquo;s data:</strong> check whether you process data of under-18s; verifiable parental consent is required.",
            "<strong>Foreign companies:</strong> if you offer goods or services to people in India, the Act applies even without an Indian entity; see <a href=\"india-services-for-foreign-companies-complete-list.html\">India services for foreign companies</a>.",
            "Our own notice is here: <a href=\"privacy.html\">privacy and cookie notice</a>.")
         + sources("Digital Personal Data Protection Act, 2023; Digital Personal Data Protection Rules, 2025 (notified 13 November 2025, Gazette 14 November 2025); compliance timelines as summarised by MirvoLegal (as at September 2026), Corpus Juris and Privy by IDfy. We advise on readiness and controls; for legal opinions on the Act we work alongside your lawyers. Corrected on 21 November 2026.")),
    ],
    faqs=[("Have the DPDP Rules been notified?", "Yes. The Digital Personal Data Protection Rules, 2025 were notified on 13 November 2025 under the DPDP Act, 2023."),
          ("When do the DPDP duties apply to businesses?", "The main duties, including notice, consent, security safeguards and breach reporting, apply about 18 months after notification, around 13 May 2027. Consent manager registration starts around 13 November 2026."),
          ("Does the DPDP Act apply to foreign companies?", "Yes, where a company outside India processes digital personal data in connection with offering goods or services to people in India."),
          ("What is the penalty under the DPDP Act?", "Penalties depend on the breach and run up to INR 250 crore."),
          ("Has the May 2027 date been brought forward?", "A proposal to shorten the 18-month period to 12 months was floated in January 2026, but no notification had been reported as of September 2026."),
          ("Can BQP help with DPDP readiness?", "Yes. " + C2)],
    related=[("india-services-for-foreign-companies-complete-list.html", "India services for foreign companies"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Compliance calendar for foreign-owned subsidiaries"), ("privacy.html", "Our privacy notice")],
    cta_h="Handling personal data of people in India?", cta_b=C2,
    keywords="DPDP Rules 2025 notified, DPDP Rules timeline May 2027, DPDP Act compliance deadline, consent manager registration November 2026, DPDP Act foreign companies, Data Protection Board India status",
    desc="DPDP Rules 2025 were notified on 13 November 2025. Phases: Data Protection Board provisions immediately, consent manager registration from about 13 November 2026, main business duties from about 13 May 2027. Applies to foreign companies serving India; penalties up to INR 250 crore.",
    howto={"name": "How to prepare for the DPDP Rules", "description": "Before the main duties apply in May 2027.", "steps": [
        {"name": "Map personal data", "text": "What you collect on people in India, why and where."},
        {"name": "Fix notices and consent", "text": "Clear notices and a record of consent and withdrawal."},
        {"name": "Secure and plan for breaches", "text": "Safeguards and a notification process."},
        {"name": "Update vendor contracts", "text": "Processors must follow your instructions and safeguards."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EX complete:", len(PAGES))
