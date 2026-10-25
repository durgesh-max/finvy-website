# -*- coding: utf-8 -*-
"""Batch AE: Round 15 - 10 hyper-local city+locality CA pages."""
from build_lib import page, write_page


def quick_page(slug, title, hero_em, lead, kicker, sections_pairs, faqs, related_pairs, cta_h, cta_b, keywords, desc):
    return page(
        slug=slug, title=title, description=desc, keywords=keywords,
        hero_kicker=kicker,
        hero_title_html=f"{title.split(' | ')[0]}, <em>{hero_em}</em>",
        hero_lead=lead,
        sections=sections_pairs, faqs=faqs,
        related=[(h, "Related", l) for h, _, l in related_pairs],
        cta_headline=cta_h, cta_body=cta_b,
    )


def make_page(city, locality, industry_focus, metro_desc, specific_services, slug):
    return {
        "slug": slug,
        "title": f"CA in {locality} {city} for {industry_focus}",
        "hero_em": f"specialist CA for {industry_focus} businesses in {locality}.",
        "lead": f"{locality} in {city} is {metro_desc}. Businesses based in {locality} benefit from a specialist CA firm that understands {industry_focus} needs + cross-border matters + ICAI-grade compliance. BQP serves {locality} + {city} with remote-first delivery (Google Drive + video + 24-48h turnaround) + on-site visits by appointment. CA Durgesh Chavda ICAI leads practice.",
        "kicker": f"/ CA in {locality} &middot; Updated 2026-10-25",
        "sections_pairs": [
            (f"/ Why {locality} needs specialist CA", f"The {industry_focus} concentration.",
             f"<ul>"
             f"<li>{locality} is {metro_desc}.</li>"
             f"<li>{industry_focus} businesses dominate the micro-market.</li>"
             f"<li>Specific client profile: {specific_services[0]} + {specific_services[1]} + {specific_services[2]}.</li>"
             f"<li>Generalist CAs often lack specialist capability for {industry_focus}.</li>"
             f"<li>Specialist CA = materially better outcomes + specific risk mitigation + specific tax optimisation.</li>"
             f"</ul>"),
            (f"/ Services BQP delivers for {locality} businesses", "The scope.",
             "<ul>" + "".join(f"<li><strong>{s}</strong>: specific scope + specific deliverables + specific timing.</li>" for s in specific_services) + "</ul>"),
            (f"/ Remote-first delivery for {locality} + {city}", "Technology-driven.",
             "<ul>"
             "<li>Google Drive / Dropbox / shared workspace for all engagements.</li>"
             "<li>Video consultations (Zoom / Google Meet / Microsoft Teams).</li>"
             "<li>E-signing (DocuSign / specific) for engagement letters + specific deliverables.</li>"
             "<li>24-48 hour standard turnaround for routine matters (Form 15CB, specific advisory).</li>"
             "<li>On-site visit by appointment: Ahmedabad principal office + specific city coverage.</li>"
             "<li>WhatsApp +91 78018 87130 for urgent matters + specific client support.</li>"
             "<li>Email durgesh@bharatquantumprospera.com for structured engagement.</li>"
             "</ul>"),
            ("/ BQP engagement model", "Scope-based.",
             "<ul>"
             "<li>Scope-based fixed-fee engagement (not hourly).</li>"
             "<li>48-hour quote: free initial consultation + specific scope + specific deliverables + specific timing + fixed fee.</li>"
             "<li>Specific engagement letter: scope + timing + fee + specific scope boundaries.</li>"
             "<li>Unlimited email + WhatsApp within scope.</li>"
             "<li>Specific scope creep: written change order + specific additional fee quoted + agreed before work.</li>"
             "<li>Preferred by clients vs hourly billing of generalist firms.</li>"
             "</ul>"),
            ("/ Why BQP", "The firm's qualifications.",
             "<ul>"
             "<li>CA Durgesh Chavda ICAI qualified + 15+ years specialist practice.</li>"
             "<li>1,500+ clients across Indian + foreign jurisdictions.</li>"
             "<li>Specialist cross-border + domestic tax + GST + MCA + FEMA + specific sector expertise.</li>"
             "<li>Partner network: US CPAs + UK ACAs + UAE accountants + Singapore CPAs + Canada CPAs + Australia CPAs for integrated advisory.</li>"
             "<li>Technology-driven delivery + specific client portal + specific document management.</li>"
             "<li>ICAI-grade compliance + specific professional standards.</li>"
             "<li><em>Last updated: 2026-10-25.</em></li>"
             "</ul>"),
        ],
        "faqs": [
            (f"Does BQP serve {locality} + {city}?",
             f"Yes - BQP serves {locality} + entire {city} metro area with remote-first delivery + on-site visits by appointment. Specialist CA practice for {industry_focus} + cross-border + domestic matters. Scope-based engagement + 48-hour quote. durgesh@bharatquantumprospera.com | WhatsApp +91 78018 87130."),
            (f"What's typical {industry_focus} CA engagement in {locality}?",
             f"Specific scope: {', '.join(specific_services)}. Each engagement: scope-based fixed-fee + specific deliverables + specific timing. BQP's specialist practice covers {industry_focus} end-to-end: incorporation + annual compliance + specific sector-specific regulatory + specific tax optimisation + cross-border advisory."),
            ("Can engagement be fully remote?",
             "Yes - BQP delivers 100% remote via Google Drive + video + e-signing + e-filing + specific portal. On-site visits by appointment for specific scenarios (closing + specific document execution + specific board meetings). Materially faster + more cost-effective + specific time-zone flexibility."),
            ("How fast is standard turnaround?",
             "24-48 hours for routine matters (Form 15CB + specific advisory + specific quick deliverables). 2-4 weeks for ITR / audit / annual compliance. 4-6 weeks for incorporation. Scope-specific timing in engagement letter. BQP tracks delivery via specific project management + specific client visibility."),
            ("Does BQP engage with foreign-origin businesses in Indian cities?",
             "Yes - specialist cross-border practice. 500+ foreign subsidiary engagements across Indian cities. For US / UK / EU / Singapore / UAE / HK / Canada / Australia / Mauritius / Netherlands parents with Indian subsidiaries + specific city operations. Integrated with foreign CPA partners for integrated advisory. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("ca-in-" + city.lower().replace(" ", "-") + "-india.html", "Related", f"CA in {city} Full"),
                          ("for-foreign-clients.html", "Related", "Foreign Clients Hub")],
        "cta_h": f"Need CA in {locality} {city}?",
        "cta_b": f"BQP specialist {industry_focus} practice + scope-based engagement + 48-hour quote. durgesh@bharatquantumprospera.com | WhatsApp +91 78018 87130.",
        "keywords": f"CA in {locality} {city} for {industry_focus}, {locality} {city} CA specialist, best CA {locality} {industry_focus}",
        "desc": f"CA in {locality} {city} for {industry_focus}: specialist CA practice for {industry_focus} businesses in {locality} ({metro_desc}), services ({', '.join(specific_services)}), remote-first delivery with 24-48h turnaround + on-site visits by appointment, scope-based fixed-fee engagement + 48-hour quote. CA Durgesh Chavda ICAI 1,500+ clients.",
    }


LOCATIONS = [
    ("Ahmedabad", "SG Highway", "startups + mid-market + jewelry",
     "Ahmedabad's primary growth corridor connecting Sarkhej, Vastrapur, Thaltej, Bopal with 500+ corporate offices + specific tech + jewelry + textiles + specific manufacturing concentration",
     ["Startup incorporation + DPIIT 80-IAC + MCA + GST", "Jewelry sector + specific gold stock + specific state registrations", "Mid-market audit + tax + MCA annual compliance", "ESOP + fundraising + specific VC due diligence"],
     "ca-in-sg-highway-ahmedabad-for-startups-mid-market"),
    ("Mumbai", "Bandra Kurla Complex", "banking + finance + MNC Indian HQ",
     "Mumbai's primary business district hosting most Indian banks + MNC Indian headquarters + specific fintech + specific legal + specific consulting firms",
     ["MNC Indian HQ compliance + specific transfer pricing + specific FEMA", "Banking + NBFC + specific RBI compliance", "ESOP + fundraising + specific VC due diligence", "Cross-border tax + Section 195 + Form 15CB + specific DTAA"],
     "ca-in-bandra-kurla-complex-mumbai-for-mnc-finance"),
    ("Bangalore", "Whitefield", "SaaS + IT services + GCC",
     "Bangalore's primary tech corridor concentration of SaaS startups + IT services companies + Global Capability Centers (GCC) of foreign MNCs",
     ["SaaS tax optimisation + Section 115BAA + specific export of services + LUT", "GCC transfer pricing + Safe Harbour Rules + Form 3CEB", "Software captive setup + FEMA FC-GPR + specific advisory", "US LLC Indian employee + ESOP + specific advisory"],
     "ca-in-whitefield-bangalore-for-saas-gcc"),
    ("Gurugram", "Cyber City", "MNC + consulting + fintech",
     "Gurugram's primary business district adjacent to Delhi airport with 300+ MNC offices + specific consulting + fintech + specific legal + specific IT services",
     ["MNC Indian subsidiary compliance + specific transfer pricing + specific FEMA", "Fintech + specific RBI compliance + specific state regulatory", "Consulting firm + specific partnership + LLP structuring", "Cross-border + specific DTAA + specific repatriation advisory"],
     "ca-in-cyber-city-gurugram-for-mnc-fintech"),
    ("Hyderabad", "Hitech City", "biopharma + IT services + specific tech",
     "Hyderabad's primary tech hub with concentration of biopharma + IT services + specific SaaS + specific pharma specific state advantages",
     ["Biopharma + specific R&D + Section 35 + specific IP structuring", "IT services + export of services + LUT + specific state incentives", "GCC + transfer pricing + specific Form 3CEB", "Specific state registrations + Telangana specific advisory"],
     "ca-in-hitech-city-hyderabad-for-biopharma-it"),
    ("Noida", "Sector 62", "IT services + mid-market + specific sector",
     "Noida's primary IT corridor adjacent to Delhi with concentration of IT services + specific manufacturing + specific state advantages + specific UP registrations",
     ["IT services + export + LUT + specific state advantages", "Mid-market audit + tax + MCA annual compliance", "Specific UP state registrations + specific sector", "Cross-border + specific DTAA + specific advisory"],
     "ca-in-sector-62-noida-for-it-mid-market"),
    ("Pune", "Hinjewadi", "IT + automotive + specific manufacturing",
     "Pune's primary tech corridor combining IT park concentration + specific automotive supplier concentration + specific manufacturing specific state advantages",
     ["IT services + export + LUT + specific state advantages", "Automotive supplier + specific GST + specific state advisory", "Manufacturing + specific Section 115BAB + specific capital subsidy", "Specific Maharashtra state registrations + specific sector"],
     "ca-in-hinjewadi-pune-for-it-automotive"),
    ("Chennai", "OMR", "automotive + IT services + specific manufacturing",
     "Chennai's primary IT + automotive corridor (Old Mahabalipuram Road / IT Expressway) with specific state advantages + specific Tamil Nadu registrations",
     ["Automotive + specific supplier compliance + specific GST", "IT services + export + LUT + specific state advantages", "Manufacturing + specific Section 115BAB + specific state advisory", "Specific Tamil Nadu state registrations + specific sector"],
     "ca-in-omr-chennai-for-automotive-it"),
    ("Kolkata", "Salt Lake", "trading + BPO + specific sector",
     "Kolkata's primary business district (Bidhannagar / Sector V) with specific trading + BPO + specific IT services + specific state advantages",
     ["Trading + specific GST + specific state advisory", "BPO + specific export + specific transfer pricing", "IT services + export + LUT + specific state advantages", "Specific West Bengal state registrations + specific sector"],
     "ca-in-salt-lake-kolkata-for-trading-bpo"),
    ("Jaipur", "Mansarovar", "gems + textiles + specific mid-market",
     "Jaipur's primary growth area with specific gems/jewelry + textiles + specific tourism + specific mid-market concentration + specific Rajasthan registrations",
     ["Gems/jewelry + specific export + specific GST advisory", "Textiles + specific sector advisory", "Mid-market audit + tax + MCA annual compliance", "Specific Rajasthan state registrations + specific sector"],
     "ca-in-mansarovar-jaipur-for-gems-textiles"),
]

PAGES = [make_page(*loc) for loc in LOCATIONS]

for p in PAGES:
    html = quick_page(
        slug=p["slug"], title=p["title"], hero_em=p["hero_em"], lead=p["lead"],
        kicker=p["kicker"], sections_pairs=p["sections_pairs"],
        faqs=p["faqs"], related_pairs=p["related_pairs"],
        cta_h=p["cta_h"], cta_b=p["cta_b"],
        keywords=p["keywords"], desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch AE complete: {len(PAGES)} hyper-local city+locality CA pages")
