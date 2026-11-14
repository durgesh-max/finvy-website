# -*- coding: utf-8 -*-
"""Batch CB (14 Nov 2026): significant economic presence (SEP) for foreign SaaS, app, ad-tech and online businesses
earning from India, under section 9 of the Income-tax Act, 2025 (from 1 April 2026), carried over from Explanation 2A
to section 9(1)(i) of the 1961 Act.
Facts: SEP = (a) transactions in goods, services or property with any person in India, including download of data or
software, with aggregate payments above the threshold (INR 2 crore), or (b) systematic and continuous soliciting of
business or interaction with users in India above the threshold (3 lakh users); thresholds first in rule 11UD (May 2021),
carried into the Income-tax Rules, 2026. Applies whether or not the agreement is made in India, the non-resident has a
residence or place of business in India, or services are rendered in India. Only income attributable to the
transactions/activities is taxed, including income from advertising targeting Indian customers or accessed via Indian
IP addresses, sale of data collected from India, and goods/services sold using such data. Purchase of goods in India
for export is excluded (Finance Act 2025). A more beneficial DTAA prevails: business profits taxable only with a PE;
treaty claim needs a TRC and Form 10F (Form 41 under the 2026 Rules), subject to the principal purpose test. Equalisation
levy: 2% on e-commerce supply abolished from 1 August 2024; 6% on online advertising abolished from 1 April 2025.
Foreign company rate 35% plus surcharge and cess (from AY 2025-26). GST: online services (OIDAR) to unregistered
recipients in India need simplified GST registration and IGST at 18%; B2B supplies under reverse charge.
Sources: Easevalue (section 9, Income-tax Act 2025), Accorp Partners, Patron Accounting (checked 14 Nov 2026)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 14 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your country of residence, annual India revenue, number of Indian users and whether you have any staff, contractors or servers in India. "
           "We reply the same working day with your exposure (income tax, withholding and GST) and a fixed-scope quote.")
SLUG = "significant-economic-presence-foreign-saas-app-company-india-2-crore-3-lakh-users-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The treaty is your shield, but only if you can show it.</p>'
       f'<p style="margin:0">Indian customers and the tax department will ask for a tax residency certificate and Form 10F (now Form 41) before applying treaty rates. Keep them ready every year, and keep India-facing staff and decision-making from creating a permanent establishment. '
       f'<a href="{wa("Hi Durgesh, we are a foreign SaaS / app company with customers in India. Can you check our significant economic presence and GST position?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Foreign SaaS, App and Online Companies Earning From India in 2026: Significant Economic Presence, the INR 2 Crore and 3 Lakh-User Tests, and Treaty Protection",
    em="no office in India needed to be taxed.",
    kicker="/ Foreign companies &middot; Digital tax &middot; Income-tax Act 2025 &middot; Updated 2026-11-14",
    lead=("A foreign company with no office, staff or server in India can still have a taxable <strong>business connection</strong> in India through <strong>significant economic presence (SEP)</strong>: "
          "either <strong>payments from India above INR 2 crore</strong> in a year for goods, services or property (including data and software downloads), or <strong>systematic and continuous dealings with 3 lakh or more users in India</strong>. "
          "The rule is in section 9 of the Income-tax Act, 2025 (in force from 1 April 2026), carried over from the 1961 Act. "
          "Only income attributable to India is taxed, and a company resident in a treaty country such as the US, UK, Singapore, UAE, Canada or Australia is usually protected by the treaty's permanent establishment test, provided it can produce a tax residency certificate and Form 10F (now Form 41)."),
    sections=[
        ("/ The two tests", "Either one creates SEP.",
         table(["Test", "Threshold", "What counts"], [
             ["Payment (revenue) test", "Aggregate payments above INR 2 crore in the tax year", "Transactions in goods, services or property with any person in India, including download of data or software"],
             ["User test", "3 lakh or more users in India", "Systematic and continuous soliciting of business or interaction with users in India through digital means"]])
         + "<p>SEP applies whether or not the contract is signed in India, the company has a place of business in India, or the services are rendered in India. The thresholds were first set in rule 11UD (May 2021) and continue under the Income-tax Rules, 2026. Buying goods in India only for export does not create SEP.</p>"),
        ("/ Are you actually taxable?", "Treaty country or not decides most cases.",
         table(["Your situation", "Usual position"], [
             ["Resident in a treaty country (US, UK, Singapore, UAE, Canada, Australia and others), no permanent establishment in India, TRC and Form 10F/41 available", "Treaty prevails where more beneficial: business profits taxed in India only if there is a PE, so SEP alone usually creates no Indian income tax"],
             ["Treaty country, but India-based staff, dependent agents or a fixed place in India", "PE risk: profits attributable to the PE are taxed in India (foreign company rate 35% plus surcharge and cess)"],
             ["Resident in a country with no tax treaty with India, or treaty benefit denied (no TRC, principal purpose test)", "SEP applies in full; income attributable to Indian revenue and users is taxable and a return is needed"],
             ["Below both thresholds", "No SEP; check other rules (royalty or fees for technical services, PE) separately"]])
         + BOX),
        ("/ What income is taxed", "Only the India-attributable part.",
         ul("Only income reasonably attributable to the Indian transactions or users is taxed, not global profit.",
            "This expressly includes income from <strong>advertising targeted at Indian customers</strong> or accessed through Indian IP addresses, <strong>sale of data collected from India</strong>, and goods or services sold using such data.",
            "The <strong>equalisation levy</strong> no longer shelters this income: the 2% levy on e-commerce supplies ended on 1 August 2024 and the 6% levy on online advertising ended on 1 April 2025, so these receipts are now tested under the income-tax rules instead.")),
        ("/ The other two Indian taxes on the same revenue", "Withholding and GST.",
         ul("<strong>Withholding by Indian business customers:</strong> an Indian payer must deduct tax on payments to a non-resident if the income is chargeable in India, and certify remittances (Forms 145/146, formerly 15CA/15CB). For standard software licences the Supreme Court held in <em>Engineering Analysis</em> (2 March 2021) that the payment is not royalty under the treaties, which many customers rely on with your TRC and Form 10F.",
            "<strong>GST on online services (OIDAR):</strong> selling digital services to consumers in India (B2C) requires simplified GST registration and IGST at 18%, even with no Indian presence; for B2B sales the Indian business pays GST under reverse charge. See <a href=\"oidar-gst-foreign-saas-ecommerce-india.html\">OIDAR GST for foreign SaaS</a>.",
            "<strong>Data rules:</strong> the DPDP Act applies to processing personal data of people in India; see <a href=\"dpdp-act-india-foreign-company-compliance-2026.html\">DPDP for foreign companies</a>.")
         + '<p>Related: <a href="foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html">PE risk from remote employees in India</a> &middot; <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">new form numbers (10F is now 41)</a> &middot; <a href="transfer-pricing.html">transfer pricing</a>.</p>'
         + f'<p><strong>Sources:</strong> Income-tax Act, 2025, section 9 (business connection and significant economic presence); Income-tax Act, 1961, section 9(1)(i) Explanations 2A and 3A and rule 11UD; Income-tax Rules, 2026; Finance (No. 2) Act, 2024 and Finance Act, 2025 (equalisation levy); <em>Engineering Analysis Centre of Excellence v CIT</em> (Supreme Court, 2 March 2021); IGST Act, 2017 (OIDAR). Secondary summaries checked 14 November 2026: Easevalue, Accorp Partners, Patron Accounting. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("What is significant economic presence in Indian tax?", "A rule under which a non-resident has a business connection in India, without any office or staff here, if payments from India for goods, services or property (including data or software downloads) exceed INR 2 crore in a year, or if it systematically and continuously deals with 3 lakh or more users in India."),
          ("Does SEP apply under the new Income-tax Act, 2025?", "Yes. The concept is in section 9 of the Income-tax Act, 2025, in force from 1 April 2026, with the INR 2 crore and 3 lakh user thresholds continued in the Income-tax Rules, 2026."),
          ("Our SaaS company is in the US with no Indian office. Do we pay Indian income tax?", "Usually not on business profits, if you are entitled to the India-US treaty and have no permanent establishment in India. The treaty prevails where it is more beneficial, but you need a tax residency certificate and Form 10F (now Form 41) to claim it."),
          ("Which companies are fully exposed to SEP?", "Companies resident in countries without a tax treaty with India, those that cannot show treaty residence, and those denied treaty benefits, for example under the principal purpose test."),
          ("Is the equalisation levy still charged?", "No. The 2% levy on e-commerce supplies ended on 1 August 2024 and the 6% levy on online advertising ended on 1 April 2025. Those receipts are now tested under the income-tax rules, including SEP."),
          ("Do we need GST registration in India?", "If you sell online services to consumers in India, yes: simplified OIDAR registration and IGST at 18%. For sales to Indian businesses, the customer pays GST under reverse charge."),
          ("Can BQP review our India exposure?", "Yes. " + CONTACT)],
    related=[("oidar-gst-foreign-saas-ecommerce-india.html", "OIDAR GST for foreign SaaS"),
             ("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "PE risk from remote employees"),
             ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "New income tax form numbers")],
    cta_h="Selling software or ads into India from abroad?", cta_b=CONTACT,
    keywords="significant economic presence India, SEP India 2 crore 3 lakh users, foreign SaaS company India tax, Income-tax Act 2025 section 9 SEP, digital company no PE India tax, equalisation levy abolished SEP, foreign app company India income tax, OIDAR GST foreign SaaS, US SaaS India treaty TRC Form 10F",
    desc="When a foreign SaaS, app or online company with no Indian office is taxable in India in 2026: significant economic presence under section 9 of the Income-tax Act, 2025 (INR 2 crore payments or 3 lakh users), treaty protection with TRC and Form 10F/41, end of the equalisation levy, withholding and OIDAR GST.",
    howto={"name": "How a foreign digital company checks its Indian tax exposure", "description": "Steps for SaaS, app and online businesses with Indian customers or users.", "steps": [
        {"name": "Measure India", "text": "Add up annual payments from customers in India and count users in India you deal with systematically."},
        {"name": "Test the thresholds", "text": "Above INR 2 crore in payments or 3 lakh users means significant economic presence under section 9."},
        {"name": "Check treaty protection", "text": "Confirm treaty residence, obtain the TRC and Form 10F (Form 41), and review any India staff, agents or fixed place for PE risk."},
        {"name": "Cover withholding and GST", "text": "Give Indian business customers your treaty documents, and register for OIDAR GST if you sell to consumers in India."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CB complete")
