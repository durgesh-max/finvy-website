# -*- coding: utf-8 -*-
"""Batch Y: Round 9 - 10 pages Oct 23. State registrations + forms + today-anchored timely."""
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


PAGES = [
    {
        "slug": "best-ca-west-bengal-state-registration-kolkata",
        "title": "Best CA for West Bengal State Registration (Kolkata + State-wide)",
        "hero_em": "Kolkata + Siliguri + state-wide compliance.",
        "lead": "West Bengal state registrations: Shops & Establishment Act (WB S&E) + Professional Tax + Labour Welfare Fund + specific KMDA / HMDA regulations + specific WBIDC industrial policies + jute + tea + specific sectoral regulations. For Pvt Ltd / LLP operating in Kolkata + Howrah + Siliguri + Durgapur + Asansol. Here's the complete 2026 West Bengal framework.",
        "kicker": "/ West Bengal Registration Specialist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Core West Bengal state registrations", "Mandatory.",
             "<ul>"
             "<li>West Bengal Shops & Establishments Act: within 30 days of commencement. Online via WB Labour Department.</li>"
             "<li>WB Professional Tax: employer registration + monthly deduction + annual return.</li>"
             "<li>WB Labour Welfare Fund.</li>"
             "<li>WB Factories Act for establishments meeting worker + power thresholds.</li>"
             "<li>WBPCB (West Bengal Pollution Control Board): CTE / CTO.</li>"
             "<li>Kolkata Municipal Corporation Trade Licence (for Kolkata-based specific categories).</li>"
             "</ul>"),
            ("/ West Bengal industrial advantages", "What WB offers.",
             "<ul>"
             "<li><strong>Industrial Policy 2017-22 + 2022+</strong>: specific state support for manufacturing + specific sectors.</li>"
             "<li><strong>WBIDC (West Bengal Industrial Development Corporation)</strong>: land allocation + specific industrial parks.</li>"
             "<li><strong>Specific sectors</strong>: jute (traditional), tea (specific regulatory), leather (Bantala Leather Complex), engineering + IT (Kolkata Salt Lake Sector V), specific manufacturing clusters.</li>"
             "<li><strong>Kolkata IT ecosystem</strong>: Salt Lake Sector V + New Town + specific IT parks. Specific state IT policy support.</li>"
             "<li><strong>Haldia port + Kolkata port</strong>: specific port + logistics advantages for East India + Southeast Asia trade.</li>"
             "</ul>"),
            ("/ Our scope for WB clients", "Complete offering.",
             "<ul>"
             "<li>WB state registrations (S&E + PT + LWF + Factory + WBPCB).</li>"
             "<li>WBIDC land + Industrial Policy incentive application.</li>"
             "<li>Kolkata Municipal Corporation Trade Licence.</li>"
             "<li>Specific sectoral regulatory: jute / tea / leather / IT.</li>"
             "<li>Haldia / Kolkata port + customs integration.</li>"
             "<li>Related central compliance.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's WB S&E deadline?",
             "Within 30 days of commencement. Online via WB Labour Department. Covers all employers in West Bengal. Renewal periodicity based on employee count."),
            ("Can BQP help with WBIDC land allocation?",
             "Yes - BQP coordinates WBIDC application for specific industrial land + capex subsidy incentive. For strategic investments in Kolkata / Howrah / Durgapur / Siliguri / Asansol clusters."),
            ("Does BQP handle WB + central integrated compliance?",
             "Yes - integrated engagement. WB state (S&E + PT + LWF + WBPCB + KMC) + specific sectoral (jute / tea / leather / IT) + central (GST + PF + ESI + Income Tax + ROC + FEMA). Remote delivery for WB clients. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-kolkata-m-and-a-transactions.html", "Related", "Best CA Firm Kolkata"),
                          ("company-secretarial-services-india-remote.html", "Related", "CS Services")],
        "cta_h": "West Bengal-based company? S&E + PT + WBIDC + central integrated.",
        "cta_b": "Kolkata + Howrah + Siliguri + Durgapur + Asansol state + central compliance. BQP WB specialist practice.",
        "keywords": "best CA West Bengal state registration, Kolkata S&E CA, WBIDC CA, WB PT CA India",
        "desc": "Best CA for West Bengal state registration (Kolkata + Howrah + Siliguri + Durgapur + Asansol): S&E + PT + LWF + WBPCB + WBIDC + Industrial Policy + Haldia port. Specific sectoral (jute / tea / leather / IT). CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-telangana-state-registration-hyderabad-ranga-reddy",
        "title": "Best CA for Telangana State Registration (Hyderabad + Ranga Reddy)",
        "hero_em": "pharma + IT + biotech cluster.",
        "lead": "Telangana state registrations for Hyderabad + Ranga Reddy + Medchal + state-wide: S&E + PT + LWF + Factory + TSPCB + GHMC (Greater Hyderabad Municipal Corporation) specifics. Specific advantages: TS-iPASS single-window + pharma cluster (Hyderabad Pharma City) + biotech (Genome Valley) + IT (HITEC City + Pocharam). Here's the complete 2026 Telangana framework.",
        "kicker": "/ Telangana Registration Specialist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Core Telangana state registrations", "Mandatory.",
             "<ul>"
             "<li>Telangana Shops & Establishments Act.</li>"
             "<li>Telangana Professional Tax: employer registration + monthly deduction.</li>"
             "<li>Telangana Labour Welfare Fund.</li>"
             "<li>Telangana Factories Act.</li>"
             "<li>TSPCB (Telangana State Pollution Control Board).</li>"
             "<li>GHMC Trade Licence for Hyderabad metropolitan specific categories.</li>"
             "</ul>"),
            ("/ Telangana industrial advantages", "What Telangana offers.",
             "<ul>"
             "<li><strong>TS-iPASS (Single Window)</strong>: specific industrial clearance framework. Fast-track approvals + deemed approval if not responded within specified timeline.</li>"
             "<li><strong>Hyderabad Pharma City</strong>: 19,000 acres dedicated pharma cluster. Specific regulatory + sector-specific support.</li>"
             "<li><strong>Genome Valley (Shamirpet)</strong>: biotech + biopharma cluster.</li>"
             "<li><strong>HITEC City (Madhapur) + Pocharam</strong>: IT corridors. Specific IT Policy benefits.</li>"
             "<li><strong>TSIIC (Telangana State Industrial Infrastructure Corporation)</strong>: industrial land + specific parks.</li>"
             "<li><strong>Telangana Industrial Policy</strong>: capex + SGST + electricity + specific state benefits.</li>"
             "</ul>"),
            ("/ Our scope for Telangana clients", "Complete offering.",
             "<ul>"
             "<li>Telangana state (S&E + PT + LWF + Factory + TSPCB).</li>"
             "<li>TS-iPASS single-window co-ordination.</li>"
             "<li>TSIIC land allocation.</li>"
             "<li>Pharma City / Genome Valley / HITEC City specific co-ordination.</li>"
             "<li>GHMC Trade Licence.</li>"
             "<li>Related central compliance.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's TS-iPASS?",
             "Telangana State Industrial Project Approval Self-Certification System - single-window industrial clearance framework. Fast-track approvals (deemed approval if not responded within statutory timeline). Online application + specific industrial sector priority."),
            ("Does BQP cover Hyderabad Pharma City?",
             "Yes - BQP has specific experience with Hyderabad Pharma City (19,000 acres dedicated pharma cluster). Co-ordination with TSIIC + specific sectoral regulatory authorities. For pharma + biotech + CDMO investments."),
            ("Does BQP handle TS + central integrated compliance?",
             "Yes - integrated engagement. TS state + specific industrial clusters + central compliance. Remote delivery for TS clients. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("best-ca-firm-hyderabad-us-incorporation.html", "Related", "Best CA Firm Hyderabad"),
                          ("best-ca-healthtech-india-2026.html", "Related", "Best CA for Healthtech")],
        "cta_h": "Telangana-based company? Hyderabad / Pharma City / Genome Valley?",
        "cta_b": "State + specific clusters + central compliance. BQP TS specialist practice.",
        "keywords": "best CA Telangana state registration, Hyderabad GHMC CA, TS-iPASS CA, TSIIC CA, Hyderabad Pharma City CA",
        "desc": "Best CA for Telangana state registration (Hyderabad + Ranga Reddy + Medchal + state-wide): S&E + PT + LWF + TSPCB + GHMC + TS-iPASS + TSIIC + Hyderabad Pharma City + Genome Valley + HITEC City. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-haryana-state-registration-gurgaon-faridabad-manesar",
        "title": "Best CA for Haryana State Registration (Gurgaon + Faridabad + Manesar)",
        "hero_em": "NCR auto + IT + manufacturing.",
        "lead": "Haryana state registrations for Gurgaon + Faridabad + Manesar + Panipat + state-wide: S&E + PT (recent re-introduction) + LWF + Factory + HSPCB. Specific advantages: HSIIDC industrial parks + Enterprise Promotion Policy + specific auto cluster (Manesar) + IT corridor (Gurgaon Cyber City + Udyog Vihar). Here's the complete 2026 Haryana framework.",
        "kicker": "/ Haryana Registration Specialist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Core Haryana state registrations", "Mandatory.",
             "<ul>"
             "<li>Haryana Shops & Establishments Act.</li>"
             "<li>Haryana Professional Tax: re-introduced in recent years - employer registration + employee deduction.</li>"
             "<li>Haryana Labour Welfare Fund.</li>"
             "<li>Haryana Factories Act.</li>"
             "<li>HSPCB (Haryana State Pollution Control Board).</li>"
             "<li>MCG / FMC specific Trade Licence (Gurgaon / Faridabad corporations).</li>"
             "</ul>"),
            ("/ Haryana industrial advantages", "What Haryana offers.",
             "<ul>"
             "<li><strong>Enterprise Promotion Policy 2020-25 + 2025+</strong>: comprehensive state support for manufacturing + specific sectors.</li>"
             "<li><strong>HSIIDC (Haryana State Industrial & Infrastructure Development Corporation)</strong>: industrial parks (IMT Manesar + IMT Faridabad + others).</li>"
             "<li><strong>Auto cluster (Manesar)</strong>: Maruti Suzuki + specific auto OEMs + supply chain depth.</li>"
             "<li><strong>Gurgaon IT corridor</strong>: Cyber City + Udyog Vihar + Golf Course Road - specific IT / ITES ecosystem.</li>"
             "<li><strong>NCR advantages</strong>: proximity to Delhi + specific inter-state logistics + capital markets access.</li>"
             "<li><strong>Specific sectors</strong>: automobile (Manesar), IT / BPO (Gurgaon), textile (Panipat), engineering + specific manufacturing.</li>"
             "</ul>"),
            ("/ Gurgaon-specific attention", "The NCR hub.",
             "<ul>"
             "<li>MCG (Municipal Corporation of Gurgaon) Trade Licence for specific categories.</li>"
             "<li>DHBVN electricity + specific infrastructure co-ordination.</li>"
             "<li>HUDA / GMDA specific zoning + building approvals.</li>"
             "<li>Specific Cyber City + Udyog Vihar + Golf Course + Sohna Road zones + specific industrial park governance.</li>"
             "</ul>"),
            ("/ Our scope for Haryana clients", "Complete offering.",
             "<ul>"
             "<li>Haryana state (S&E + PT + LWF + Factory + HSPCB).</li>"
             "<li>HSIIDC land + Enterprise Promotion Policy incentive.</li>"
             "<li>Gurgaon / Faridabad specific MCG / FMC Trade Licence.</li>"
             "<li>Related central compliance.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("Was Haryana PT recently re-introduced?",
             "Yes - Haryana Professional Tax was re-introduced in recent years (specific statutory re-introduction). Employer registration + monthly deduction + annual return applicable. Fresh compliance for employers who may not have Haryana PT in historical records."),
            ("Does BQP cover Manesar auto cluster?",
             "Yes - Manesar is specific auto cluster with Maruti Suzuki + supply chain. BQP specific experience with auto OEM + Tier-1 + Tier-2 suppliers + specific HSIIDC + Enterprise Promotion Policy + specific inter-state logistics."),
            ("Does BQP handle Haryana + central integrated?",
             "Yes - integrated engagement. Haryana state + specific industrial clusters + central compliance. For Gurgaon + Faridabad + Manesar + Panipat + state-wide operations. Remote delivery. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("company-secretarial-services-india-remote.html", "Related", "CS Services"),
                          ("india-pli-scheme-foreign-manufacturer-2026.html", "Related", "PLI Scheme")],
        "cta_h": "Haryana-based company? Gurgaon / Manesar / Faridabad / Panipat?",
        "cta_b": "State + HSIIDC + specific clusters + central compliance. BQP Haryana specialist practice.",
        "keywords": "best CA Haryana state registration, Gurgaon MCG CA, Manesar auto CA, HSIIDC CA, Haryana PT CA",
        "desc": "Best CA for Haryana state registration (Gurgaon + Faridabad + Manesar + Panipat + state-wide): S&E + PT + LWF + Factory + HSPCB + HSIIDC + Enterprise Promotion Policy + MCG / FMC. Specific auto (Manesar) + IT (Gurgaon) + textile (Panipat). CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "best-ca-uttar-pradesh-state-registration-noida-lucknow",
        "title": "Best CA for Uttar Pradesh State Registration (Noida + Lucknow + Kanpur)",
        "hero_em": "largest state + specific electronics + food processing.",
        "lead": "Uttar Pradesh state registrations for Noida + Greater Noida + Lucknow + Kanpur + Varanasi + state-wide: S&E + UP Professional Tax (post re-introduction) + LWF + Factory + UPPCB + specific UPSIDA + NOIDA Authority (if NOIDA-based). Specific advantages: Yamuna Expressway Industrial Development Authority + Jewar Airport + specific electronics manufacturing cluster. Here's the complete 2026 UP framework.",
        "kicker": "/ UP Registration Specialist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Core UP state registrations", "Mandatory.",
             "<ul>"
             "<li>UP Shops & Establishments Act.</li>"
             "<li>UP Professional Tax: re-introduced in recent years.</li>"
             "<li>UP Labour Welfare Fund.</li>"
             "<li>UP Factories Act.</li>"
             "<li>UPPCB (Uttar Pradesh Pollution Control Board).</li>"
             "<li>NOIDA / Greater Noida / YEIDA Authority specific if based in these areas.</li>"
             "<li>Specific Nagar Nigam Trade Licence (Lucknow Nagar Nigam, Kanpur Nagar Nigam, Varanasi Nagar Nigam).</li>"
             "</ul>"),
            ("/ UP industrial advantages", "What UP offers.",
             "<ul>"
             "<li><strong>UP Industrial Investment & Employment Promotion Policy</strong>: comprehensive support.</li>"
             "<li><strong>UPSIDA (UP State Industrial Development Authority)</strong>: industrial parks across state.</li>"
             "<li><strong>Yamuna Expressway Industrial Development Authority (YEIDA)</strong>: dedicated industrial development near Jewar Airport (Noida International Airport, operational 2024+).</li>"
             "<li><strong>Jewar Airport ecosystem</strong>: specific logistics + manufacturing + supply chain for aviation + export-oriented.</li>"
             "<li><strong>Specific sectors</strong>: electronics manufacturing (Noida IT corridor), food processing (specific clusters), leather (Kanpur / Agra), textile (Varanasi silk + others).</li>"
             "<li><strong>UP Electronics Manufacturing Cluster (EMC)</strong>: specific electronics focus.</li>"
             "</ul>"),
            ("/ Noida-specific attention", "The NCR hub.",
             "<ul>"
             "<li>NOIDA Authority specific regulations + trade licence + specific allotment framework.</li>"
             "<li>Greater Noida Authority similar + specific SMART City initiatives.</li>"
             "<li>YEIDA specific framework.</li>"
             "<li>Specific IT parks + specific sector clusters.</li>"
             "<li>Delhi NCR / Noida inter-state logistics + specific capital markets access.</li>"
             "</ul>"),
            ("/ Our scope for UP clients", "Complete offering.",
             "<ul>"
             "<li>UP state registrations (S&E + PT + LWF + Factory + UPPCB).</li>"
             "<li>UPSIDA / NOIDA / YEIDA land + policy incentive.</li>"
             "<li>Jewar Airport ecosystem + specific aviation logistics.</li>"
             "<li>Specific sectoral: electronics / food processing / leather / textile.</li>"
             "<li>Nagar Nigam Trade Licence.</li>"
             "<li>Related central compliance.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's YEIDA and why is it important?",
             "Yamuna Expressway Industrial Development Authority - dedicated industrial development authority near Jewar Airport (Noida International Airport, operational 2024+). Specific industrial park allocation + aviation-adjacent logistics + manufacturing + export-oriented operations. Jewar Airport is expected to become India's largest airport."),
            ("Does BQP handle UP state + central integrated?",
             "Yes - integrated engagement. UP state + specific industrial clusters (NOIDA / YEIDA / UPSIDA) + central compliance. For Noida + Greater Noida + Lucknow + Kanpur + Varanasi + state-wide operations. Remote delivery. WhatsApp +91 78018 87130."),
            ("Which UP cities does BQP serve?",
             "All UP cities with remote delivery. Specific concentration in Noida + Greater Noida (NCR adjacency), Lucknow (state capital), Kanpur (industrial), Varanasi (specific cultural + commercial), Agra (leather + specific). Remote delivery + associate network for specific site visits."),
        ],
        "related_pairs": [("best-ca-firm-lucknow-startup-nri-tax.html", "Related", "Best CA Firm Lucknow"),
                          ("company-secretarial-services-india-remote.html", "Related", "CS Services")],
        "cta_h": "UP-based company? Noida / Lucknow / Kanpur / YEIDA?",
        "cta_b": "State + UPSIDA + YEIDA + Jewar Airport ecosystem + central compliance. BQP UP specialist practice.",
        "keywords": "best CA Uttar Pradesh state registration, Noida NOIDA CA, YEIDA CA, Jewar Airport ecosystem CA, UP PT CA",
        "desc": "Best CA for Uttar Pradesh state registration (Noida + Greater Noida + Lucknow + Kanpur + Varanasi + Agra + state-wide): S&E + PT + LWF + UPPCB + UPSIDA + NOIDA / Greater Noida / YEIDA Authority + Industrial Investment & Employment Promotion Policy. Jewar Airport ecosystem. CA Durgesh Chavda specialist practice.",
    },
    {
        "slug": "form-aoc-5-registered-office-location-filing-india-2026",
        "title": "Form AOC-5 Registered Office Location India 2026",
        "hero_em": "mandatory for maintaining books outside registered office.",
        "lead": "Form AOC-5 is mandatory ROC filing when company's books of accounts are kept at a location DIFFERENT from registered office. Section 128 Companies Act 2013 + Rule 2A of Companies (Accounts) Rules 2014. Must be filed within 7 days of board resolution. Non-filing attracts Section 450 default penalty. Here's the complete 2026 Form AOC-5 framework.",
        "kicker": "/ ROC Form Checklist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ When Form AOC-5 is needed", "Core trigger.",
             "<ul>"
             "<li>Section 128 Companies Act requires books of accounts to be kept at REGISTERED OFFICE of the company by default.</li>"
             "<li>If company chooses to keep books at a DIFFERENT location (branch office, head office different from registered office, back-office location): must file Form AOC-5.</li>"
             "<li>Rule 2A: file Form AOC-5 within 7 days of board resolution authorising books location change.</li>"
             "<li>Section 450 default penalty if not filed.</li>"
             "</ul>"),
            ("/ Common AOC-5 scenarios", "When companies trigger.",
             "<ul>"
             "<li>Registered office in Ahmedabad but books at corporate office in Mumbai: file AOC-5.</li>"
             "<li>Registered office at CA / professional office + actual books at company's own office elsewhere: file AOC-5.</li>"
             "<li>Multi-location business with centralised back-office / accounting hub.</li>"
             "<li>Outsourced accounting to third-party service provider's location (BQP's office may be the books location for client).</li>"
             "<li>Virtual registered office with physical books at different location.</li>"
             "</ul>"),
            ("/ Form AOC-5 structure + filing", "The compliance.",
             "<ul>"
             "<li>Board resolution: company's board must pass resolution authorising keeping books at specific different location.</li>"
             "<li>Form AOC-5 content: company CIN + PAN + registered office + different books location address + period from when books kept there.</li>"
             "<li>Attach: certified board resolution.</li>"
             "<li>DSC + file via MCA v3 portal within 7 days.</li>"
             "<li>Fee: minimal MCA fee + late fee if filed beyond 7 days.</li>"
             "<li>Section 450 default penalty: INR 10,000 + INR 1,000 per day continuing default + officer penalty.</li>"
             "</ul>"),
            ("/ Our scope + related compliances", "Integrated engagement.",
             "<ul>"
             "<li>Books location strategy: when to file AOC-5 vs maintain at registered office.</li>"
             "<li>Board resolution drafting.</li>"
             "<li>Form AOC-5 preparation + MCA filing.</li>"
             "<li>Related: Section 134 Board Report disclosure, Section 177 Audit Committee specific consideration.</li>"
             "<li>Section 143 statutory audit interaction: auditor's access to books location.</li>"
             "<li>GST books at different location + specific GST location rules.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("When is Form AOC-5 due?",
             "Within 7 days of board resolution authorising keeping books at location different from registered office. Section 128 + Rule 2A Companies (Accounts) Rules 2014. Late filing attracts Section 450 default penalty."),
            ("What if books are at registered office?",
             "No AOC-5 required - default rule. Company's books kept at registered office. AOC-5 ONLY needed when books location is different from registered office."),
            ("Does outsourcing accounting to CA firm trigger AOC-5?",
             "Depends on physical location of books. If physical books / data kept at CA firm's office (common for outsourced accounting): yes - file AOC-5. If CA firm has only soft access to company's cloud accounting (QBO / Zoho / Tally cloud) with physical books at company's own office: not strictly triggered. Specific analysis needed."),
            ("Does BQP file AOC-5 for client companies?",
             "Yes - integrated with standard CS services. Board resolution drafting + AOC-5 preparation + MCA filing within 7-day deadline. Standard for mid-size + large companies with specific books location arrangements. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("company-secretarial-services-india-remote.html", "Related", "CS Services"),
                          ("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Related", "Form MGT-14")],
        "cta_h": "Books of accounts at different location than registered office?",
        "cta_b": "Board resolution + Form AOC-5 within 7 days + MCA filing + related compliance. BQP integrated CS services.",
        "keywords": "Form AOC-5 India 2026, Section 128 books location ROC filing CA, AOC-5 7 days deadline CA",
        "desc": "Form AOC-5 registered office location filing India 2026: Section 128 Companies Act 2013 + Rule 2A Companies (Accounts) Rules 2014. 7-day deadline from board resolution. Common scenarios: multi-location business, outsourced accounting location, virtual registered office. CA Durgesh Chavda guide.",
    },
    {
        "slug": "form-sh-4-share-transfer-form-india-2026",
        "title": "Form SH-4 Share Transfer Form India 2026 Complete Checklist",
        "hero_em": "stamp duty + proper execution.",
        "lead": "Form SH-4 is the share transfer form under Section 56 Companies Act 2013 + Rule 11 Companies (Share Capital and Debentures) Rules 2014. Prescribed form for every share transfer between members. Stamp duty payable per Indian Stamp Act (0.015% in most states; vary). Signed by both transferor + transferee + witness. Here's the complete 2026 SH-4 framework.",
        "kicker": "/ Share Transfer Checklist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Form SH-4 core", "The prescribed form.",
             "<ul>"
             "<li>Form SH-4: statutory share transfer deed under Section 56 Companies Act 2013.</li>"
             "<li>Mandatory for every share transfer between members (physical shares; demat transfer is depository-based without SH-4).</li>"
             "<li>Signed by: transferor + transferee + witness.</li>"
             "<li>Stamp duty payable per Indian Stamp Act (central / state-specific).</li>"
             "<li>Standard stamp duty: 0.015% of consideration (or face value if higher) in most states.</li>"
             "<li>Specific state variations (Maharashtra, Karnataka, Tamil Nadu, etc.).</li>"
             "</ul>"),
            ("/ Post Rule 9B demat regime", "Reduced SH-4 use.",
             "<ul>"
             "<li>Post Rule 9B mandatory dematerialisation of unlisted shares (October 2024 for private companies), most share transfers are now in demat form - depository-based transfer without SH-4.</li>"
             "<li>SH-4 still relevant for: companies not yet Rule 9B compliant (unresponsive shareholders in physical form), small companies exempt from Rule 9B, specific legacy / inheritance share transfers.</li>"
             "<li>Buy-back / specific restructuring may still use SH-4 for specific share class.</li>"
             "</ul>"),
            ("/ SH-4 + FC-TRS integration (foreign shareholder)", "FEMA angle.",
             "<ul>"
             "<li>Share transfer between resident + non-resident OR between two non-residents requires Form FC-TRS filing within 60 days.</li>"
             "<li>SH-4 is the share transfer deed; FC-TRS is the FEMA reporting.</li>"
             "<li>Both required for share transfer involving foreign shareholder.</li>"
             "<li>Rule 21 pricing guidelines verification + CA / Merchant Banker certificate.</li>"
             "<li>See our FC-TRS filing checklist for details.</li>"
             "</ul>"),
            ("/ Common SH-4 execution issues", "Where companies trip.",
             "<ul>"
             "<li>Stamp duty under-paid (wrong state rate applied, wrong consideration basis).</li>"
             "<li>Missing witness signature.</li>"
             "<li>SH-4 lodged with company > 2 months after execution (Rule 11 time limit).</li>"
             "<li>Company's refusal to register transfer (specific grounds under Section 58).</li>"
             "<li>Lost share certificates - must issue duplicate under Rule 6 before transfer.</li>"
             "<li>Non-compliance with Rule 9B demat requirement for Rule 9B companies - transfer in physical form invalid post Rule 9B date.</li>"
             "<li>Section 56(2)(x) buyer-side gift tax if transfer at below fair value.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("When is Form SH-4 needed?",
             "For every share transfer between members in physical form. Post Rule 9B mandatory demat (October 2024 for private companies), most transfers are depository-based without SH-4. SH-4 still relevant for Rule 9B-exempt entities + legacy physical shares + specific restructuring."),
            ("What's the stamp duty on SH-4?",
             "Per Indian Stamp Act + state-specific adjustments. Standard: 0.015% of consideration or face value whichever higher. Maharashtra, Karnataka, Tamil Nadu, Gujarat have specific state-level rates. Payable via physical stamp paper or e-stamping (preferred)."),
            ("Can share transfer be rejected by company?",
             "Section 58 Companies Act: company can refuse to register transfer only on specific grounds (not frivolous). Refusal: within 30 days + reasoned order + specific appeal mechanism to NCLT. Rare in practice for standard transfers."),
            ("Does BQP handle SH-4 + FC-TRS integrated for foreign-shareholder transfers?",
             "Yes - integrated service. SH-4 preparation + stamp duty computation + CA/Merchant Banker pricing certificate + FC-TRS filing within 60 days + MCA records update + related compliance. For M&A transactions + angel exits + specific secondary + Rule 9B demat transfers. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("form-fc-trs-filing-checklist-india-2026.html", "Related", "FC-TRS Checklist"),
                          ("dematerialisation-unlisted-shares-india-mandatory.html", "Related", "Rule 9B Demat")],
        "cta_h": "Share transfer involving physical shares or foreign shareholder?",
        "cta_b": "SH-4 + stamp duty + FC-TRS (foreign) + Rule 9B demat compliance + related. BQP integrated engagement.",
        "keywords": "Form SH-4 India 2026, share transfer form India CA, Section 56 share transfer CA India, stamp duty SH-4",
        "desc": "Form SH-4 share transfer form India 2026 complete checklist: Section 56 Companies Act 2013 + Rule 11 Companies (Share Capital) Rules 2014. Stamp duty 0.015% (varies by state). Post Rule 9B demat regime reduced SH-4 use. SH-4 + FC-TRS integration for foreign shareholder transfers. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "form-mr-1-managerial-personnel-appointment-india-2026",
        "title": "Form MR-1 Managerial Personnel Appointment India 2026",
        "hero_em": "MD + WTD + Manager appointment ROC filing.",
        "lead": "Form MR-1 is mandatory ROC filing for appointment of Managing Director (MD) / Whole-Time Director (WTD) / Manager under Section 196 + 197 Companies Act 2013. Filed within 60 days of appointment. Includes remuneration disclosure + Schedule V compliance. Here's the complete 2026 Form MR-1 framework.",
        "kicker": "/ Managerial Appointment Checklist &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Form MR-1 core", "Who files when.",
             "<ul>"
             "<li>Form MR-1: filed by company within 60 days of appointment of MD / WTD / Manager.</li>"
             "<li>Section 196 Companies Act 2013 + Section 197 (managerial remuneration limits).</li>"
             "<li>Covers: appointment, re-appointment, variation in terms, remuneration change.</li>"
             "<li>MCA v3 portal filing.</li>"
             "<li>Section 450 default penalty for late / non-filing.</li>"
             "</ul>"),
            ("/ Section 197 managerial remuneration limits", "The ceilings.",
             "<ul>"
             "<li>Public company: aggregate remuneration to all directors including MD/WTD/Manager - maximum 11% of net profit (Section 197(1)).</li>"
             "<li>Specific sub-limits: single MD/WTD max 5% of net profit; multiple MDs/WTDs max 10% aggregate; non-executive directors max 1% (with MD/WTD) or 3% (without).</li>"
             "<li>Private company: no Section 197 limits (except specific exemptions carved out).</li>"
             "<li>Loss / inadequate profit: Schedule V Part II provisions apply with specific slab-wise maximum.</li>"
             "<li>Shareholder special resolution required for exceeding Section 197 limits.</li>"
             "</ul>"),
            ("/ Schedule V compliance", "The specific framework.",
             "<ul>"
             "<li>Schedule V Companies Act: part I (eligibility conditions for appointment) + Part II (remuneration ceiling for loss / inadequate profit years).</li>"
             "<li>Eligibility conditions: minimum age 21 + maximum age 70 (specific special resolution if above 70) + specific qualifications.</li>"
             "<li>Prohibition on managerial appointment: specific disqualifications (undischarged insolvent, convicted of specific offences, specific IRDA/SEBI debarment).</li>"
             "<li>Loss / inadequate profit remuneration limit: slab-wise maximum based on effective capital of company.</li>"
             "<li>Approval sequence: Board → Nomination & Remuneration Committee (if applicable) → Shareholders (if Section 197 limits exceeded or Schedule V applicable).</li>"
             "</ul>"),
            ("/ Form MR-1 + related compliances", "Integrated.",
             "<ul>"
             "<li>Form MR-1: within 60 days of appointment.</li>"
             "<li>Form DIR-12: appointment of director (within 30 days).</li>"
             "<li>Form MGT-14: for specific resolutions (Section 179(3) board resolutions for appointment of KMP including MD / CEO / CFO).</li>"
             "<li>Section 134 Board Report: disclosure of managerial remuneration.</li>"
             "<li>Section 197 details in financial statements + notes.</li>"
             "<li>Separate CSR Committee / Audit Committee / Nomination & Remuneration Committee if applicable.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("When is Form MR-1 due?",
             "Within 60 days of appointment of MD / WTD / Manager. Also for re-appointment, variation in terms, remuneration change. Section 196 Companies Act 2013 + Section 197 managerial remuneration limits."),
            ("Does Section 197 limit apply to Pvt Ltd?",
             "No - Section 197 managerial remuneration limits (11% of net profit, etc.) apply only to public companies. Private companies are exempt from Section 197 limits (except specific carved-out scenarios). But Form MR-1 filing is still mandatory for private company MD/WTD/Manager appointment."),
            ("What's Schedule V compliance?",
             "Companies Act Schedule V: Part I (eligibility conditions - age 21-70, qualifications, no specific disqualification) + Part II (remuneration ceiling for loss / inadequate profit years - slab-wise maximum based on effective capital). Applicable to public companies in loss years + specific private company scenarios."),
            ("Does BQP handle Form MR-1 + related compliance?",
             "Yes - integrated. MD/WTD/Manager appointment advisory + Section 197 limits analysis + Schedule V compliance + Form MR-1 + DIR-12 + MGT-14 (if applicable) + Board Report disclosure + ongoing managerial remuneration tracking. Standard for mid-size + large companies. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("company-secretarial-services-india-remote.html", "Related", "CS Services"),
                          ("dir-3-kyc-director-annual-compliance-india.html", "Related", "DIR-3 KYC")],
        "cta_h": "MD / WTD / Manager appointment or remuneration change?",
        "cta_b": "Form MR-1 + Section 197 + Schedule V + related filings. BQP integrated engagement for managerial appointments.",
        "keywords": "Form MR-1 India 2026, MD WTD Manager appointment ROC CA, Section 197 managerial remuneration CA, Schedule V CA India",
        "desc": "Form MR-1 Managing Director / Whole-Time Director / Manager appointment ROC filing India 2026: Section 196 + 197 Companies Act 2013 + Schedule V compliance (eligibility + remuneration ceiling). 60-day deadline + Section 197 limits (public company 11% of net profit) + Schedule V Part II slab-wise maximum. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "diwali-2026-festive-season-year-end-tax-planning-india",
        "title": "Diwali 2026 Festive Season Year-End Tax Planning India",
        "hero_em": "Diwali to March 31 - the 5-month tax planning window.",
        "lead": "Diwali 2026 (10 November) marks the start of India's intensive year-end tax planning window: 5 months until 31 March 2027 FY end. Capital gain reinvestment (Section 54 / 54F / 54EC) + Section 80C/80D/80G exhaustion + Section 44AD/ADA presumptive + donation deadlines + specific exemption claims. Here's the complete BQP festive-season planning framework.",
        "kicker": "/ Diwali-March Planning &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ The 5-month planning window", "November to March.",
             "<ul>"
             "<li><strong>November 2026</strong>: Diwali 10 Nov. Form 29B MAT verification. Form 3CEB TP audit (30 November). MGT-7 (29 November). PAS-6 (29 November). MSME Form I (29 November). AOC-4 (if not already Oct 30).</li>"
             "<li><strong>December 2026</strong>: Q3 advance tax (15 Dec, 75% cumulative). Form ODI APR (31 Dec). GSTR-9 FY 2024-25 (31 Dec). Belated / revised ITR (31 Dec).</li>"
             "<li><strong>January 2027</strong>: Q3 TDS returns (31 Jan). Specific sector returns.</li>"
             "<li><strong>February 2027</strong>: Union Budget 2026-27 (expected 1 Feb). Pre-Budget investment / capital gain timing decisions.</li>"
             "<li><strong>March 2027</strong>: Q4 advance tax (15 Mar, 100% cumulative). Section 80C/80D/80G last-minute investment. Section 54 reinvestment completion. 31 Mar FY end.</li>"
             "</ul>"),
            ("/ Capital gain reinvestment planning", "Section 54 / 54F / 54EC.",
             "<ul>"
             "<li><strong>Section 54 (residential-to-residential)</strong>: LTCG on residential property reinvested in residential property - exempt. 2-year purchase OR 3-year construction window.</li>"
             "<li><strong>Section 54F (any long-term asset-to-residential)</strong>: LTCG on non-residential asset reinvested in ONE residential property - exempt. Net consideration (not just gain) must be invested.</li>"
             "<li><strong>Section 54EC (bonds)</strong>: LTCG invested in REC / NHAI / PFC / IRFC bonds within 6 months - INR 50 lakh limit. Simple + lower-risk.</li>"
             "<li>Finance Act 2024 LTCG 12.5% framework interaction - optimise choice.</li>"
             "<li>Capital Gain Account Scheme (CGAS) deposit before 31 July 2027 ITR deadline if actual investment delayed.</li>"
             "</ul>"),
            ("/ Section 80C / 80D / 80G last-mile", "The deduction optimisation.",
             "<ul>"
             "<li>Section 80C INR 1.5 lakh: ELSS mutual fund, PPF, EPF, NPS, Life Insurance Premium, Tuition Fees. Deadline 31 March 2027.</li>"
             "<li>Section 80CCD(1B) NPS additional INR 50K: for NPS Tier-I.</li>"
             "<li>Section 80D health insurance: self (INR 25K / 50K senior) + parents (INR 25K / 50K senior).</li>"
             "<li>Section 80G donations: specific NGOs with 80G certificate + 100%/50% deduction. Document transfer before 31 March.</li>"
             "<li>Section 80TTA / 80TTB savings interest exemption.</li>"
             "<li>Section 80E education loan interest - no upper limit on amount, 8 years.</li>"
             "</ul>"),
            ("/ New vs Old regime decision", "AY 2027-28 planning.",
             "<ul>"
             "<li>New regime (default): INR 7 lakh exemption + rebate. Lower rates. No most deductions except Section 80CCD(2) employer NPS + standard deduction INR 75K.</li>"
             "<li>Old regime: higher rates + full deduction suite (80C, 80D, 80G, HRA, home loan interest, etc.).</li>"
             "<li>Decision varies by individual deduction profile.</li>"
             "<li>Can switch each year for non-business income; business income has specific lock-in.</li>"
             "<li>Use BQP's new vs old regime calculator at bharatquantumprospera.com/new-vs-old-tax-regime-calculator.html.</li>"
             "</ul>"),
            ("/ Startup / company specific year-end", "Beyond individual.",
             "<ul>"
             "<li>Form 10-IC Section 115BAA opt-in (if desired).</li>"
             "<li>Form 10-ID Section 115BAB opt-in for new manufacturing.</li>"
             "<li>Pre-FY-end bonus + ESOP exercise + related perquisite tax planning.</li>"
             "<li>MSE supplier payment before 45-day Section 43B(h) trigger.</li>"
             "<li>Section 194R business perquisite TDS year-end reconciliation.</li>"
             "<li>Form 3CEB TP + Master File + CbCR for in-scope groups.</li>"
             "<li>GSTR-9 + GSTR-9C pre-filing audit (31 December 2026 deadline).</li>"
             "<li><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("What's the Diwali to March 31 tax planning window?",
             "5 months of intensive year-end planning. November-December: compliance deadlines (TP audit, MGT-7, PAS-6, MSME-1, Q3 advance tax, GSTR-9, Form ODI APR). February: pre-Budget. March: last-mile Section 80C/80D/80G + Section 54 reinvestment + Q4 advance tax. Final decisions before FY ends 31 March 2027."),
            ("Should I buy ELSS before Diwali or in March?",
             "Both work. Diwali-based ELSS SIP spreads cost. March-based lump-sum optimises timing based on actual annual tax position. For most individuals: SIP throughout year + top-up in March to hit INR 1.5 lakh Section 80C limit."),
            ("How to time Section 54 reinvestment?",
             "If LTCG realised in current FY: reinvestment window is 2 years forward (purchase) / 3 years forward (construction). Deposit in Capital Gain Account Scheme (CGAS) by 31 July 2027 if actual investment delayed. Must complete investment within 2/3 year window from original sale date."),
            ("New or Old regime for AY 2027-28?",
             "Varies by deduction profile. For individuals with substantial deductions (HRA + home loan interest + Section 80C + 80D + 80G), old regime typically better. For simpler profile (minimum deductions), new regime often better due to lower rates + INR 7 lakh rebate. Use BQP calculator at bharatquantumprospera.com/new-vs-old-tax-regime-calculator.html."),
            ("What's the biggest Diwali-season compliance miss BQP sees?",
             "Director DIR-3 KYC catch-up (missed 30 September deadline, deactivated DIN blocking all MCA filings). Fix urgently with INR 5,000 late fee + 24-72 hour reactivation. Also: PAS-6 half-year (29 November) + MSME Form I (29 November) often missed."),
            ("Does BQP offer year-end tax planning engagement?",
             "Yes - November-March intensive engagement: Q3 advance tax + GSTR-9 + Form ODI APR + Form 3CEB + managerial compliance + Section 54 reinvestment + Section 80C/D/G optimisation + regime decision + ESOP/bonus timing + Section 148 response + 2027 Budget planning. For individuals + startups + mid-market companies. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("advance-tax-q3-december-15-2026-india.html", "Related", "Q3 Advance Tax Dec 15"),
                          ("india-tax-compliance-calendar-fy-2026-27-complete.html", "Related", "FY 2026-27 Calendar")],
        "cta_h": "Diwali to March 31 = 5 months of year-end tax planning window.",
        "cta_b": "Capital gain reinvestment + Section 80C/D/G exhaustion + regime decision + ESOP timing + compliance deadlines. BQP year-end intensive engagement.",
        "keywords": "Diwali 2026 tax planning, year-end tax planning India 2026-27, 31 March 2027 FY end tax planning CA, festive season tax CA",
        "desc": "Diwali 2026 festive season to 31 March 2027 year-end tax planning India: 5-month intensive window covering capital gain reinvestment (Section 54 / 54F / 54EC), Section 80C/80D/80G exhaustion, Q3 advance tax, GSTR-9, Form ODI APR, new vs old regime decision, Section 115BAA opt-in, pre-Budget planning. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "pre-budget-2026-startup-foreign-company-actions-window",
        "title": "Pre-Budget 2026 Startup + Foreign Company Actions Window",
        "hero_em": "October 2026 - February 2027 window.",
        "lead": "Pre-Budget 2026 (expected 1 February 2027) window from October 2026 to February 2027 is critical planning period for startups + foreign companies. Historical pattern: material tax changes announced in Budget often take effect from FY 2027-28; some retrospective. Specific actions to execute now before Budget rather than wait. Here's the complete BQP pre-Budget action framework.",
        "kicker": "/ Pre-Budget 2026 Window &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ Why pre-Budget planning matters", "The timing play.",
             "<ul>"
             "<li>Historical pattern: Finance Act (post-Budget) often introduces changes with effect from FY 2027-28 (next year).</li>"
             "<li>Some changes retrospective (specific areas - usually clarificatory).</li>"
             "<li>Pre-Budget action enables locking-in favourable position before any potential tightening.</li>"
             "<li>Investment / transaction / election timing decisions have specific pre-Budget vs post-Budget trade-offs.</li>"
             "<li>October 2026 - early February 2027 is the planning + execution window.</li>"
             "</ul>"),
            ("/ Startup pre-Budget actions", "Before Budget 2026.",
             "<ul>"
             "<li><strong>Section 115BAA opt-in via Form 10-IC</strong>: if planned, do before 31 October 2026 ITR for FY 2025-26. Irrevocable; locks 22% rate.</li>"
             "<li><strong>Section 115BAB opt-in via Form 10-ID</strong>: for new manufacturing - Form 10-ID with first-year ITR. Lock 15% rate.</li>"
             "<li><strong>DPIIT Startup India + Section 80-IAC application</strong>: before DPIIT policy changes in Budget.</li>"
             "<li><strong>ESOP grants pre-Budget</strong>: at current 409A/11UA valuation; before any potential Section 17(2) perquisite rule changes.</li>"
             "<li><strong>Section 56(2)(viib) legacy clean-up</strong>: for pre-abolition rounds - defend / regularise before any tightening clarification in Budget.</li>"
             "<li><strong>Section 54GB reinvestment</strong>: use current startup-friendly provisions.</li>"
             "<li><strong>Capital raise / M&A timing</strong>: completed transactions crystallise current tax position.</li>"
             "</ul>"),
            ("/ Foreign company pre-Budget actions", "Before Budget 2026.",
             "<ul>"
             "<li><strong>DPDP Act compliance readiness</strong>: Rules expected to finalise by Budget 2026. Prepare now vs scramble post-Rules.</li>"
             "<li><strong>FEMA voluntary compounding</strong>: historical breaches regularised before any Budget / policy tightening. Materially cheaper than reactive.</li>"
             "<li><strong>Rule 9B demat completion</strong>: 2-year post-mandate - complete remediation before any strict enforcement.</li>"
             "<li><strong>Transfer pricing documentation refresh</strong>: Form 3CEB benchmarking study updated for FY 2025-26. Potential Pillar 2 integration.</li>"
             "<li><strong>BEPS Pillar 2 preparation</strong>: for in-scope groups - operational now, GIR filing June 2027. Pre-Budget data readiness.</li>"
             "<li><strong>Section 115BAB opt-in via Form 10-ID</strong>: for new manufacturing - lock 15% rate before any potential future change.</li>"
             "<li><strong>FDI reform consultation feedback</strong>: engage with pre-Budget consultation if sectoral FDI expansion planned.</li>"
             "</ul>"),
            ("/ Individual + NRI pre-Budget actions", "Specific moves.",
             "<ul>"
             "<li><strong>Capital gain reinvestment</strong>: Section 54 / 54F / 54EC within windows. Current LTCG 12.5% framework (post Finance Act 2024).</li>"
             "<li><strong>Section 80C/D/G exhaustion</strong>: current limits + current rules.</li>"
             "<li><strong>NRI returning to India - RNOR optimisation</strong>: 2-3 year window + current treatment.</li>"
             "<li><strong>LRS planning Oct-March</strong>: current TCS 20% rate + specific exemptions (education loan, medical).</li>"
             "<li><strong>Section 139(8A) updated return</strong>: for prior AYs under current 24-month window.</li>"
             "</ul>"),
            ("/ Specific risks of waiting post-Budget", "Why act now.",
             "<ul>"
             "<li><strong>Rate changes</strong>: Budget may change 115BAA 22%, 115BAB 15%, LTCG 12.5%, or specific sector rates.</li>"
             "<li><strong>DTAA treaty renegotiations</strong>: US-India / Mauritius-India specific. Pre-Budget position may be grandfathered.</li>"
             "<li><strong>DPDP Rules notification</strong>: compliance obligations crystallise. Preparation required.</li>"
             "<li><strong>FDI sector reforms</strong>: specific sector may open or tighten; current rules apply to pre-reform transactions.</li>"
             "<li><strong>Specific anti-avoidance clarifications</strong>: GAAR / PPT / specific sector rules may tighten.</li>"
             "</ul>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("When is Union Budget 2026-27 expected?",
             "Early February 2027 - typically 1 February. Finance Act 2027 provisions typically effective from FY 2027-28 (next year). Some clarificatory changes retrospective. Pre-Budget planning window: October 2026 - early February 2027."),
            ("Should I opt into Section 115BAA before Budget 2026?",
             "Yes if 115BAA is the right choice based on current analysis. Budget 2026 may change concessional corporate tax rate framework (unlikely but possible). Form 10-IC filing is irrevocable - once opted in, locked at 22% rate (effective 25.17%) regardless of future changes. Lock-in protective."),
            ("What's the biggest pre-Budget action for foreign companies?",
             "FEMA voluntary compounding for historical breaches - under Section 13. Materially cheaper than being caught in RBI inspection + any potential policy tightening. 90-180 day window. Should be completed before Budget 2026."),
            ("Is DPDP Act compliance Budget-dependent?",
             "DPDP Act is already enacted (August 2023). Rules expected to be notified around Budget 2026 timeframe. Pre-Budget compliance readiness means being prepared when Rules notify. 90-180 day window post-Rules notification for enforcement typically."),
            ("Does BQP offer pre-Budget 2026 planning engagement?",
             "Yes - October 2026 to February 2027 intensive engagement. Startup: 115BAA/115BAB opt-in + DPIIT + ESOP + 56(2)(viib) legacy. Foreign company: DPDP readiness + FEMA compounding + Rule 9B demat + Pillar 2 preparation + Form 3CEB refresh. Individuals: capital gain reinvestment + Section 80C/D/G + regime decision + LRS planning. WhatsApp +91 78018 87130."),
        ],
        "related_pairs": [("budget-2026-expectations-startups-nri-foreign-companies.html", "Related", "Budget 2026 Expectations"),
                          ("diwali-2026-festive-season-year-end-tax-planning-india.html", "Related", "Diwali-March Planning")],
        "cta_h": "Pre-Budget 2026 window: October 2026 to February 2027.",
        "cta_b": "Startup + foreign company + individual + NRI specific pre-Budget actions. BQP intensive engagement + 48-hour quote.",
        "keywords": "pre-Budget 2026 planning India, Union Budget 2027 preparation CA, pre-Budget startup foreign company India, FY 2026-27 pre-Budget actions",
        "desc": "Pre-Budget 2026 (expected 1 Feb 2027) startup + foreign company + individual action window October 2026 - February 2027: Section 115BAA/BAB opt-in, DPIIT + 80-IAC, ESOP timing, 56(2)(viib) legacy clean-up, DPDP readiness, FEMA compounding, Rule 9B demat, Pillar 2 preparation, capital gain reinvestment, regime decision. Working CA guide by Durgesh Chavda.",
    },
    {
        "slug": "rbi-mpc-gst-council-sebi-update-tracker-oct-2026",
        "title": "RBI MPC + GST Council + SEBI Update Tracker October 2026",
        "hero_em": "monthly regulatory update digest for CFOs.",
        "lead": "October 2026 regulatory update tracker: RBI Monetary Policy Committee outcomes + GST Council meeting clarifications + SEBI consultation papers + MeitY DPDP Rules status + CBDT notifications. Compiled for CFOs + finance teams + Indian subsidiary CFOs of foreign parents to track what's changing. BQP monthly digest. Here's the Oct 2026 edition.",
        "kicker": "/ Regulatory Update Digest &middot; Updated 2026-10-23",
        "sections_pairs": [
            ("/ RBI Monetary Policy update", "Interest rate + liquidity framework.",
             "<ul>"
             "<li>RBI MPC continues data-dependent monetary policy stance.</li>"
             "<li>Repo rate decisions impact: borrowing cost, bond yields, FX hedging cost, deposit rates.</li>"
             "<li>Specific liquidity management framework changes impact banking sector + corporate treasury operations.</li>"
             "<li>External Commercial Borrowings (ECB) framework: specific sector allocations + hedging mandates.</li>"
             "<li>FEMA LRS + Form A2 updates track RBI master directions.</li>"
             "<li>Scale-Based Regulation (SBR) framework for NBFCs continues implementation.</li>"
             "</ul>"),
            ("/ GST Council updates", "Rate + clarification framework.",
             "<ul>"
             "<li>Periodic GST Council meetings issue rate clarifications + sector-specific guidance.</li>"
             "<li>Recent focus areas: online gaming 28% framework fine-tuning, specific export of service clarifications, OIDAR classification, specific HSN rate rationalisation.</li>"
             "<li>GSTR-9 + GSTR-9C FY 2024-25 deadline 31 December 2026 - any extension / amendment announcements tracked.</li>"
             "<li>Section 43B(h) MSE payment year 2 impact clarifications.</li>"
             "<li>GST Appellate Tribunal (GSTAT) operationalisation + specific procedure updates.</li>"
             "</ul>"),
            ("/ SEBI consultation papers", "Capital markets regulation.",
             "<ul>"
             "<li>Periodic SEBI consultation papers on specific capital markets reforms.</li>"
             "<li>Recent focus: SME IPO framework refinements, LODR Regulations updates, specific disclosure requirements, SBEB (ESOP) Regulations.</li>"
             "<li>SEBI AIF Regulations: periodic updates on fund structuring, LP-GP agreements, specific disclosure.</li>"
             "<li>SEBI research analyst / investment adviser regulation.</li>"
             "<li>GIFT City IFSCA interface + specific cross-regulatory framework.</li>"
             "</ul>"),
            ("/ MeitY + DPDP + AI regulation", "Technology sector.",
             "<ul>"
             "<li>DPDP Rules expected to finalise around Budget 2026 timeframe.</li>"
             "<li>MeitY periodic AI advisories: deepfake labelling, large model deployment, intermediary rules refinement.</li>"
             "<li>Digital India Act (DIA) draft under consultation - comprehensive digital governance framework.</li>"
             "<li>IndiaAI Mission continues implementation + specific compute + model development support.</li>"
             "<li>Section 69A IT Act specific content takedown framework updates.</li>"
             "</ul>"),
            ("/ CBDT notifications + clarifications", "Direct tax specifics.",
             "<ul>"
             "<li>Periodic CBDT notifications on specific interpretations.</li>"
             "<li>Recent focus: Form 10F electronic filing clarifications, Section 115BBH VDA (crypto) specific interpretations, Section 194R (business perquisite) industry-specific CBDT circulars, Section 194S (crypto TDS) clarifications.</li>"
             "<li>Rule 11UA valuation framework updates.</li>"
             "<li>Section 148 reassessment procedural clarifications.</li>"
             "<li>DGIT Investigation specific framework.</li>"
             "<li>Form 3CEB TP audit specific clarifications.</li>"
             "</ul>"),
            ("/ What CFOs should track", "The action list.",
             "<ol>"
             "<li>RBI repo rate + liquidity framework for ECB + domestic borrowing + treasury.</li>"
             "<li>GST Council rate + classification changes for specific products / services.</li>"
             "<li>SEBI consultation papers for listed / pre-IPO + AIF / fund structuring.</li>"
             "<li>MeitY DPDP Rules notification timing.</li>"
             "<li>CBDT specific sector / section clarifications.</li>"
             "<li>MCA specific amendments (Companies Act Rules, LLP Act Rules).</li>"
             "<li>Supreme Court / High Court rulings on specific tax / corporate / regulatory matters.</li>"
             "<li>Union Budget 2026-27 (February 2027) proposal + Finance Act 2027.</li>"
             "</ol>"
             "<p><em>Last updated: 2026-10-23.</em></p>"),
        ],
        "faqs": [
            ("How often does BQP publish regulatory update tracker?",
             "Monthly update digest + ad-hoc for material changes. Covers RBI + GST Council + SEBI + MeitY + CBDT + MCA + Supreme Court / High Court rulings. For CFOs + finance teams + Indian subsidiary CFOs of foreign parents. Subscribe via newsletter or follow bharatquantumprospera.com/insights.html for ongoing updates."),
            ("What's the biggest October 2026 regulatory watch?",
             "DPDP Rules notification (expected around Budget 2026 timeframe), BEPS Pillar 2 India operational implementation (FY 2025-26 live), GST Council sector-specific rate clarifications, SEBI SME IPO framework refinements, CBDT Form 10F + Section 194R + Section 115BBH clarifications."),
            ("Does BQP help interpret specific regulatory changes for client companies?",
             "Yes - standard advisory. When RBI MPC / GST Council / SEBI / MeitY / CBDT issues material update, BQP analyses impact on client's business + provides specific action memo. Standard annual engagement includes regulatory tracking + impact assessment for client portfolio. WhatsApp +91 78018 87130."),
            ("What should pre-IPO companies track specifically?",
             "SEBI consultation papers on SME IPO framework + LODR Regulations + SBEB (ESOP) Regulations. SEBI ICDR Regulations amendments. GSTAT operationalisation. CBDT Form 3CEB TP audit specifics. Any Supreme Court / High Court capital markets rulings. BQP pre-IPO roadmap includes regulatory tracking."),
            ("Does BQP track Supreme Court / High Court rulings?",
             "Yes - major rulings on tax (Section 148, Section 56, Section 115BBH, TP, FEMA), corporate (Companies Act, SEBI, LODR), regulatory (RBI, DPDP, specific sector) tracked. Specific case impact analysis + client-specific advisory. For material matters affecting client's position."),
            ("Does BQP coordinate with foreign counsel on cross-border regulatory updates?",
             "Yes - standard for foreign-shareholder subsidiary clients. BEPS Pillar 2 global coordination, Pillar 1 Equalisation Levy sunset, OECD CARF for crypto, specific DTAA renegotiations (US-India, Mauritius-India, Cyprus-India), FATCA/CRS reporting updates. BQP + foreign counsel + Big-4 global network coordinated advisory for cross-border matters."),
        ],
        "related_pairs": [("budget-2026-expectations-startups-nri-foreign-companies.html", "Related", "Budget 2026 Expectations"),
                          ("india-tax-compliance-calendar-fy-2026-27-complete.html", "Related", "FY 2026-27 Calendar")],
        "cta_h": "Monthly regulatory update tracker for CFOs?",
        "cta_b": "RBI + GST Council + SEBI + MeitY + CBDT + MCA + courts. BQP monthly digest + client-specific impact advisory. Scope-based.",
        "keywords": "RBI GST Council SEBI update tracker India CA 2026, India regulatory update CFO digest, India tax compliance monthly update CA, India regulatory news October 2026",
        "desc": "October 2026 India regulatory update tracker: RBI MPC + GST Council + SEBI consultation + MeitY DPDP + CBDT notifications + MCA + Supreme Court / High Court. For CFOs + finance teams + Indian subsidiary CFOs of foreign parents. Monthly digest + client-specific impact advisory. CA Durgesh Chavda.",
    },
]

for p in PAGES:
    html = quick_page(
        slug=p["slug"], title=p["title"], hero_em=p["hero_em"], lead=p["lead"],
        kicker=p["kicker"], sections_pairs=p["sections_pairs"],
        faqs=p["faqs"], related_pairs=p["related_pairs"],
        cta_h=p["cta_h"], cta_b=p["cta_b"],
        keywords=p["keywords"], desc=p["desc"],
    )
    write_page(p["slug"], html)

print(f"Batch Y complete: {len(PAGES)} pages")
