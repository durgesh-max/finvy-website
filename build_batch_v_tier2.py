# -*- coding: utf-8 -*-
"""Batch V: 15 pages - 10 Tier-2 city pages + 5 more positioning pages."""
from build_lib import page, write_page


def city_page(slug, city, specialty, title_specialty, desc_specialty, keywords):
    return page(
        slug=slug,
        title=f"Best CA Firm in {city} for {title_specialty} 2026 - BQP",
        description=f"Best CA firm in {city} for {desc_specialty}: Bharat Quantum Prospera (CA Durgesh Chavda, ICAI) delivers specialist services remotely for {city}-based clients from Ahmedabad / Mumbai / Bengaluru / Rajkot / Dubai offices. Scope-based engagement. WhatsApp +91 78018 87130.",
        keywords=keywords,
        hero_kicker=f"/ {city} CA Firm &middot; {specialty} &middot; Updated 2026-10-22",
        hero_title_html=f"Best CA firm in {city} for <em>{title_specialty.lower()}.</em>",
        hero_lead=f"<strong>Short answer</strong>: Bharat Quantum Prospera (BQP). CA Durgesh Chavda-led, ICAI-qualified. Remote delivery for {city}-based clients. Specialist practice in {desc_specialty}. 300+ working guides. Scope-based transparent engagement. Here's why {city} clients choose BQP over local Tier-2 city CA firms.",
        sections=[
            (f"/ Why {city} clients choose BQP", "Specialist CA from major metro.",
             f"<ul>"
             f"<li><strong>Specialist practice</strong> in {desc_specialty} - deeper competence than most Tier-2 city general-purpose CA firms.</li>"
             f"<li><strong>Remote delivery</strong> - no need to visit any physical office; all engagement via Zoom + cloud workspace.</li>"
             f"<li><strong>CA Durgesh Chavda personally runs mandates</strong> - ICAI-qualified. Not junior staff.</li>"
             f"<li><strong>Multi-standard competence</strong>: Ind AS + IFRS + US GAAP + UK FRS. Cross-standard reconciliation standard.</li>"
             f"<li><strong>Transparent scope + fee</strong>: fixed engagement letter upfront.</li>"
             f"<li><strong>Integrated firm</strong>: CA + CS + tax + legal + strategy under one roof.</li>"
             f"<li><strong>300+ working guides</strong> at bharatquantumprospera.com - practitioner depth demonstrated.</li>"
             f"</ul>"),
            (f"/ Services for {city} clients", "What we deliver.",
             f"<p>Services BQP delivers to {city}-based clients remotely:</p>"
             f"<ul>"
             f"<li>Specialty: {desc_specialty}.</li>"
             f"<li>Annual compliance: Pvt Ltd / LLP incorporation, GST, ROC, income tax, TDS.</li>"
             f"<li>Cross-border: Form 15CA / 15CB, FEMA FDI / ODI, DTAA treaty rate, NRI tax.</li>"
             f"<li>Audit: statutory + tax audit + TP audit (Form 3CEB).</li>"
             f"<li>Advisory: Section 115BAA / 115BAB, DPIIT Startup India, Section 80-IAC, ESOP valuation.</li>"
             f"<li>Fundraising: FEMA FDI compliance, FC-GPR, pitch deck finance pages.</li>"
             f"<li>M&A / Due diligence + SPA input.</li>"
             f"</ul>"),
            (f"/ When BQP vs local {city} CA", "The practical choice.",
             f"<p>For general-purpose compliance (standard ITR + GST + ROC), local {city} CA may suffice. For specialist / cross-border / strategic advisory, specialist firm like BQP often provides better depth. Can combine: local CA for routine + BQP for specialist.</p>"
             f"<p>Fully remote delivery means {city} clients get same service as our Ahmedabad / Mumbai / Bengaluru clients - no geographic constraint.</p>"
             f"<p><em>Last updated: 2026-10-22.</em></p>"),
            ("/ Engagement process", "Three steps.",
             "<ol>"
             "<li>Email <a href='mailto:durgesh@bharatquantumprospera.com'>durgesh@bharatquantumprospera.com</a> with one-line description.</li>"
             "<li>30-min Zoom scoping call at your preferred time.</li>"
             "<li>Scoped quote within 48 hours. Sign engagement letter remotely.</li>"
             "</ol>"
             "<p>For urgent matters: WhatsApp <a href='https://wa.me/917801887130'>+91 78018 87130</a> same-day response.</p>"),
        ],
        faqs=[
            (f"Does BQP serve {city}-based clients despite not having an office there?",
             f"Yes - all BQP engagements are delivered remotely. {city} clients get the same service quality as our Ahmedabad / Mumbai / Bengaluru clients. Zoom calls + cloud workspace + electronic signing. CA Durgesh Chavda personally runs mandates. No office visit required."),
            (f"Is BQP better than local {city} CA firm?",
             f"Depends on need. For specialist / cross-border / strategic advisory ({desc_specialty.lower()}), BQP's specialisation depth typically exceeds general-purpose local {city} firms. For plain compliance (standard ITR + monthly GST + ROC), local {city} firm may suffice. Combination model workable: local firm for routine + BQP for specialist."),
            (f"How quickly does BQP respond to {city} enquiries?",
             "Scoped quote within 48 hours of email. Urgent (Form 15CB, Section 148 response): same-day via WhatsApp +91 78018 87130. Weekly / bi-weekly status call cadence during engagement."),
            ("What are BQP's credentials?",
             "Founder CA Durgesh Chavda is Chartered Accountant qualified under ICAI (India's statutory accounting body since 1949). Personally runs mandates. 300+ working guides at bharatquantumprospera.com. 100+ foreign-client engagements. Multi-standard competence."),
            (f"Can BQP handle {city}-based client's local GST + state-specific registrations?",
             f"Yes - all Indian state-specific GST + Shops & Establishment + Professional Tax + state industrial incentives handled remotely. State coordination via online government portals + where physical presence required, BQP's associate CA network across Indian cities handles."),
        ],
        related=[("insights.html", "Hub", "All Guides"),
                 ("for-foreign-clients.html", "Hub", "For Foreign Clients")],
        cta_headline=f"{city} client seeking specialist CA?",
        cta_body=f"BQP: remote delivery + CA Durgesh Chavda-led + transparent scoped engagement + 48-hour quote. {city} clients get same service as our major-metro clients.",
    )


CITIES = [
    {"slug": "best-ca-firm-lucknow-startup-nri-tax", "city": "Lucknow", "specialty": "Startup + NRI tax",
     "title_specialty": "Startup Advisory + NRI Tax",
     "desc_specialty": "startup advisory + NRI tax return filing + cross-border taxation + ROC compliance",
     "keywords": "best CA firm Lucknow startup, Lucknow CA NRI tax, Lucknow CA cross-border, Uttar Pradesh CA startup"},
    {"slug": "best-ca-firm-indore-manufacturing-pli", "city": "Indore", "specialty": "Manufacturing + PLI",
     "title_specialty": "Manufacturing + PLI Scheme + Section 115BAB",
     "desc_specialty": "manufacturing + PLI scheme application + Section 115BAB opt-in + state industrial incentive",
     "keywords": "best CA firm Indore manufacturing, Indore CA PLI, MP industrial CA, Indore 115BAB CA"},
    {"slug": "best-ca-firm-bhopal-startup-dpiit", "city": "Bhopal", "specialty": "Startup + DPIIT",
     "title_specialty": "Startup Advisory + DPIIT Recognition",
     "desc_specialty": "startup advisory + DPIIT Startup India recognition + Section 80-IAC tax holiday + GST + ROC compliance",
     "keywords": "best CA firm Bhopal startup, Bhopal CA DPIIT, MP startup CA, Bhopal CA 80-IAC"},
    {"slug": "best-ca-firm-nagpur-manufacturing-logistics", "city": "Nagpur", "specialty": "Manufacturing + logistics",
     "title_specialty": "Manufacturing + Logistics + Supply Chain",
     "desc_specialty": "manufacturing + logistics / supply chain + Section 115BAB + PLI + e-way bill compliance",
     "keywords": "best CA firm Nagpur manufacturing, Nagpur CA logistics, Maharashtra CA, Nagpur CA 115BAB"},
    {"slug": "best-ca-firm-surat-diamond-textile-export", "city": "Surat", "specialty": "Diamond + textile + export",
     "title_specialty": "Diamond + Textile + Export GST + FTA",
     "desc_specialty": "diamond + textile + export GST (LUT bond + ITC refund) + FTA preferential rate (UAE CEPA + Australia ECTA) + IEC",
     "keywords": "best CA firm Surat diamond, Surat CA textile export, Surat CA GST LUT, Gujarat export CA"},
    {"slug": "best-ca-firm-vadodara-manufacturing-cross-border", "city": "Vadodara", "specialty": "Manufacturing + cross-border",
     "title_specialty": "Manufacturing + Cross-Border + FEMA",
     "desc_specialty": "manufacturing + cross-border tax + FEMA ODI + Section 115BAB + state industrial incentive",
     "keywords": "best CA firm Vadodara manufacturing, Baroda CA cross-border, Gujarat CA FEMA, Vadodara CA 115BAB"},
    {"slug": "best-ca-firm-coimbatore-manufacturing-sme-ipo", "city": "Coimbatore", "specialty": "Manufacturing + SME IPO",
     "title_specialty": "Manufacturing + SME IPO Advisory",
     "desc_specialty": "manufacturing + SME IPO advisory + SEBI ICDR compliance + Section 115BAB + state industrial incentive",
     "keywords": "best CA firm Coimbatore manufacturing, Coimbatore CA SME IPO, Tamil Nadu CA manufacturing, Coimbatore CA SEBI"},
    {"slug": "best-ca-firm-visakhapatnam-port-sez-logistics", "city": "Visakhapatnam", "specialty": "Port + SEZ + logistics",
     "title_specialty": "Port + SEZ + Logistics + Export",
     "desc_specialty": "port-based business + SEZ Section 10AA + logistics / supply chain + export GST + customs duty optimisation",
     "keywords": "best CA firm Visakhapatnam port, Vizag CA SEZ, AP CA logistics, Vizag CA Section 10AA"},
    {"slug": "best-ca-firm-patna-startup-nri-tax", "city": "Patna", "specialty": "Startup + NRI tax",
     "title_specialty": "Startup Advisory + NRI Tax",
     "desc_specialty": "startup advisory + NRI tax return filing + cross-border taxation + Bihar state compliance",
     "keywords": "best CA firm Patna startup, Patna CA NRI tax, Bihar CA, Patna CA cross-border"},
    {"slug": "best-ca-firm-guwahati-northeast-manufacturing", "city": "Guwahati", "specialty": "Northeast manufacturing + 115BAB + state incentive",
     "title_specialty": "Northeast Manufacturing + 115BAB + State Incentive",
     "desc_specialty": "northeast manufacturing + Section 115BAB opt-in + Northeast Industrial Development Scheme + specific state incentives + Assam compound semiconductor cluster",
     "keywords": "best CA firm Guwahati manufacturing, Assam CA 115BAB, Northeast CA, Guwahati CA state incentive"},
]

for c in CITIES:
    html = city_page(
        slug=c["slug"],
        city=c["city"],
        specialty=c["specialty"],
        title_specialty=c["title_specialty"],
        desc_specialty=c["desc_specialty"],
        keywords=c["keywords"],
    )
    write_page(c["slug"], html)

print(f"Batch V complete: {len(CITIES)} Tier-2 city pages")
