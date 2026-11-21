# -*- coding: utf-8 -*-
"""Batch FB (21 Nov 2026): Master file (Form 3CEAA) for Indian subsidiaries of foreign companies - Part A for every
constituent entity, Part B above the thresholds, due 30 November 2026 for FY 2025-26. Call-first page.
Demand: sweep 21 Nov 2026 (ac35), all 7 markets: "form 3ceaa", "form 3ceaa purpose", "who is required to file form
3ceaa", "form 3ceaa 3ceab 3ceac". Site mentioned the master file inside transfer-pricing pages (and only the Part B
thresholds) but had no page of its own.
Facts (checked 21 Nov 2026):
- India Briefing, 17 Nov 2026 ("Transfer Pricing Compliance in India: Key Filing Requirements for 30 November 2026"):
  FY 2025-26 / AY 2026-27 compliance continues under the Income-tax Act, 1961; master file under section 92D(4), Rule 10DA,
  Form 3CEAA; Part A for all constituent entities of an international group irrespective of the Part B thresholds; Part B
  where consolidated group revenue exceeds INR 500 crore and international transactions exceed INR 50 crore, or
  intangible-related transactions exceed INR 10 crore; due 30 November 2026 with the transfer-pricing return.
- Income Tax Department form page: Form 3CEAA is the master file report under section 92D(4) read with Rule 10DA;
  Form 3CEAC is the intimation under section 286(1) by a resident constituent entity whose parent is non-resident.
- Rule 10DA: Form 3CEAB designation of one Indian constituent entity at least 30 days before the due date; filings go
  to the Director General of Income-tax (Risk Assessment). Rule 10DB: country-by-country report threshold INR 6,400 crore
  consolidated group revenue; Form 3CEAC at least two months before the report's due date (12 months after the end of the
  reporting accounting year); Form 3CEAD only in the secondary-filing cases.
- Penalty: section 271AA(2), INR 5,00,000 for not furnishing the master file information (reasonable cause, section 273B).
- Income-tax Rules, 2026 (tax year 2026-27 onwards): Forms 56, 57, 58, 59 replace 3CEAA, 3CEAB, 3CEAC, 3CEAD
  (ICAI navigator, TaxGuru, CAclubindia tables)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "master-file-form-3ceaa-india-part-a-part-b-indian-subsidiary-foreign-company-due-30-november-2026"

C = contact("the parent company's country, the group's consolidated revenue, the value of the Indian entity's transactions with group companies in FY 2025-26, and how many group entities are in India")
PAGES = [dict(
    slug=SLUG,
    title="Master File in India (Form 3CEAA) for Subsidiaries of Foreign Companies: Part A, Part B, Thresholds and the 30 November 2026 Due Date",
    em="who files what, and what the parent must send.",
    kicker="/ Foreign companies &middot; Transfer pricing &middot; Master file &middot; Updated 2026-11-21",
    lead=("<strong>Every Indian entity that belongs to an international group files Part A of the master file (Form 3CEAA), whatever its size.</strong> "
          "For FY 2025-26 it is due on <strong>30 November 2026</strong>, the same day as the transfer-pricing income-tax return. "
          "<strong>Part B</strong>, the detailed group description, is needed only when the group&rsquo;s consolidated revenue is above <strong>INR 500 crore</strong> and the Indian entity&rsquo;s international transactions are above <strong>INR 50 crore</strong> (or above <strong>INR 10 crore</strong> for intangibles). "
          "Many small foreign-owned subsidiaries miss Part A because they assume the master file is only for large groups. The penalty for not filing is <strong>INR 5 lakh</strong>. "
          "The form is filed online by the Indian entity, but most of the information has to come from the parent, so ask for it now."),
    sections=[
        ("/ Who files what", "Part A, Part B and the country-by-country forms.",
         table(["Filing", "Who", "When for FY 2025-26"], [
             ["Form 3CEAA Part A (basic details of the Indian entity and the group)", "Every Indian constituent entity of an international group, with no size threshold", "30 November 2026"],
             ["Form 3CEAA Part B (the full master file)", "Group consolidated revenue above INR 500 crore, and the Indian entity&rsquo;s international transactions above INR 50 crore, or above INR 10 crore for intangibles", "30 November 2026"],
             ["Form 3CEAB (naming one Indian entity to file for all)", "Groups with more than one entity in India that want a single filing", "At least 30 days before the due date, so 31 October 2026 has passed; each entity now files its own"],
             ["Form 3CEAC (telling India which group entity files the country-by-country report)", "Indian entity of a foreign-parented group with consolidated revenue above INR 6,400 crore", "At least two months before the group&rsquo;s report is due, which is 12 months after its year end"],
             ["Form 3CEAD (the country-by-country report itself)", "Indian-parented groups above INR 6,400 crore; an Indian subsidiary only if India cannot get the report from the parent&rsquo;s country", "12 months after the group&rsquo;s year end"]])
         + '<p>A group is &ldquo;international&rdquo; when it has entities in more than one country. So an Indian private limited company owned by a US, UK, UAE or Singapore company is a constituent entity, even if the group is a start-up.</p>'
         + call_box("Master file and transfer-pricing filings due 30 November", ["Whether your Indian entity needs Part A only or Part A and Part B",
                                                                               "A list of what the parent company has to send, in one request",
                                                                               "Filing Form 3CEAA, and the transfer-pricing return that goes with it",
                                                                               "Country-by-country intimation (Form 3CEAC) where the group is large",
                                                                               "What to do if the date has already passed"],
                    "the parent&rsquo;s country, group consolidated revenue, the Indian entity&rsquo;s transactions with group companies and whether Form 3CEB has been filed.")),
        ("/ What goes in", "Part A is short. Part B is the group&rsquo;s story.",
         ul("<strong>Part A:</strong> name, address and PAN of the Indian entity; name and address of the international group; the accounting year; and the names, PANs and addresses of all group entities in India.",
            "<strong>Part B, structure:</strong> every group entity with its address, and an ownership chart.",
            "<strong>Part B, business:</strong> what drives profit, the supply chain for the main products and services, main markets, important service arrangements between group companies, and the functions, assets and risks of the entities that contribute most.",
            "<strong>Part B, intangibles:</strong> the group&rsquo;s strategy for developing and owning intangibles, the important ones and who owns them, and the agreements and pricing policies around them.",
            "<strong>Part B, financing:</strong> how the group is funded, the main lenders, and any group company that acts as a central financing entity.",
            "<strong>Part B, tax and accounts:</strong> consolidated financial statements, and existing advance pricing agreements and tax rulings.")
         + '<p>The master file is separate from the Indian entity&rsquo;s own transfer-pricing study and from the accountant&rsquo;s report in Form 3CEB, which was due on 31 October 2026. See <a href="form-3ceb-tp-audit-india-2026-30-november-checklist.html">Form 3CEB and the 30 November return</a>.</p>'),
        ("/ Practical points", "Before 30 November.",
         ul("<strong>Check Part A first:</strong> if the Indian company has a foreign parent or foreign subsidiaries, assume Part A applies and file it, even with small transactions.",
            "<strong>Use the group&rsquo;s existing master file:</strong> most large groups already prepare one under OECD rules for other countries. The Indian form asks for a few items in its own format, so it needs mapping, not rewriting.",
            "<strong>Test the thresholds on the right numbers:</strong> group revenue is the consolidated figure for the group&rsquo;s accounting year; the INR 50 crore and INR 10 crore tests use the Indian entity&rsquo;s own international transactions.",
            "<strong>One filing for several Indian entities:</strong> this needed Form 3CEAB by 31 October. Without it, each Indian entity files its own Form 3CEAA.",
            "<strong>Penalty:</strong> INR 5 lakh under section 271AA(2) for not furnishing the master file information. It can be contested where there was reasonable cause, so a late filing is still better than none.",
            "<strong>Which law:</strong> FY 2025-26 filings stay under the Income-tax Act, 1961 and the old form numbers. From tax year 2026-27 the same filings become Forms 56, 57, 58 and 59 under the Income-tax Rules, 2026.",
            "<strong>Return due the same day:</strong> the income-tax return for transfer-pricing cases is also due on 30 November 2026 and was not extended.")
         + '<p>Related: <a href="transfer-pricing-india-foreign-mnc.html">transfer pricing for foreign groups in India</a> &middot; <a href="foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html">annual compliance calendar for a foreign-owned subsidiary</a> &middot; <a href="tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html">TDS on payments to the parent: calculator</a> &middot; <a href="deadline-desk-20-november-2026-to-31-january-2027-income-tax-gst-roc-nri-foreign-companies.html">all deadlines to 31 January 2027</a>.</p>'
         + sources("Income-tax Act, 1961, sections 92D(4), 271AA(2), 273B and 286; Income-tax Rules, 1962, Rules 10DA and 10DB; Income Tax Department form pages for Forms 3CEAA and 3CEAC; India Briefing, &ldquo;Transfer Pricing Compliance in India: Key Filing Requirements for 30 November 2026&rdquo; (17 November 2026); Income-tax Rules, 2026 form tables (ICAI, TaxGuru). Checked 21 November 2026. Confirm the form version on the e-filing portal before filing.")),
    ],
    faqs=[("Does every Indian subsidiary of a foreign company have to file a master file?", "Yes for Part A. Every Indian constituent entity of an international group files Part A of Form 3CEAA whatever its size. Part B is needed only when group consolidated revenue is above INR 500 crore and the Indian entity's international transactions are above INR 50 crore, or above INR 10 crore for intangibles."),
          ("What is the due date for Form 3CEAA for FY 2025-26?", "30 November 2026, the due date of the income-tax return for transfer-pricing cases. It has not been extended."),
          ("What is the penalty for not filing the master file in India?", "INR 5 lakh under section 271AA(2) of the Income-tax Act, 1961. The penalty can be contested if there was reasonable cause for the failure."),
          ("What is Form 3CEAB?", "An intimation naming one Indian entity of the group to file the master file for all the group's Indian entities. It must be filed at least 30 days before the due date, which for FY 2025-26 was 31 October 2026."),
          ("When does an Indian subsidiary deal with country-by-country reporting?", "When the group's consolidated revenue is above INR 6,400 crore. The Indian entity files Form 3CEAC, naming the group entity that files the report, at least two months before the report is due. It files the report itself (Form 3CEAD) only if India cannot obtain it from the parent's country."),
          ("What are the new form numbers for the master file?", "From tax year 2026-27, under the Income-tax Rules, 2026, Form 56 replaces Form 3CEAA, Form 57 replaces 3CEAB, Form 58 replaces 3CEAC and Form 59 replaces 3CEAD. FY 2025-26 filings use the old numbers."),
          ("Can BQP prepare and file the master file for our Indian subsidiary?", "Yes. " + C)],
    related=[("form-3ceb-tp-audit-india-2026-30-november-checklist.html", "Form 3CEB and the 30 November return"),
             ("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign groups in India"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Annual compliance calendar for a foreign-owned subsidiary")],
    cta_h="Indian subsidiary with a master file due on 30 November?", cta_b=C,
    keywords="Form 3CEAA, master file India, who is required to file Form 3CEAA, Form 3CEAA Part A Part B, master file due date 30 November 2026, Form 3CEAB, Form 3CEAC, master file threshold 500 crore, Indian subsidiary foreign company transfer pricing",
    desc="Master file in India (Form 3CEAA): every Indian entity of an international group files Part A by 30 November 2026; Part B only above INR 500 crore group revenue and INR 50 crore transactions (INR 10 crore intangibles). Penalty INR 5 lakh. Forms 3CEAB, 3CEAC, 3CEAD explained.",
    howto={"name": "How an Indian subsidiary files the master file (Form 3CEAA)", "description": "Steps before 30 November.", "steps": [
        {"name": "Confirm group status", "text": "A foreign parent or foreign subsidiaries make the Indian company a constituent entity."},
        {"name": "Test the Part B thresholds", "text": "Group revenue above INR 500 crore and Indian international transactions above INR 50 crore, or INR 10 crore for intangibles."},
        {"name": "Collect group information", "text": "Ask the parent for the group master file, ownership chart and consolidated accounts."},
        {"name": "File Form 3CEAA online", "text": "Part A, and Part B if the thresholds are met, by 30 November 2026."},
        {"name": "File the return", "text": "The transfer-pricing income-tax return is due the same day."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FB complete")
