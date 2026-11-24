# -*- coding: utf-8 -*-
"""Batch GN (24 Nov 2026): India business visa for foreign founders, executives and staff - what the e-Business visa
allows and does not allow (no employment), validity and stay, how to apply on the official portal, and the tax and
company-law side a business visitor creates: salary tax for days in India (short-stay and treaty exemptions), permanent
establishment risk, directors' DIN and resident director, paying visitors. Call-first page for foreign companies.
Demand: sweep ac63 (24 Nov 2026): "india business visa", "india business visa requirements / application / cost /
for us citizens" in all 7 markets.
Facts (checked 24 Nov 2026): e-Business visa valid one year from grant, multiple entry, each stay capped at 180 days,
FRRO registration if business stay exceeds 180 days; apply on the official Indian visa portal; fees vary by
nationality; using a tourist visa for business can lead to deportation and re-entry bans (Wise, BAL, Fragomen,
visa-requirements.io). Tax points match the site's expat page: 90-day short-stay exemption for employees of a foreign
enterprise with no business in India (section 10(6)(vi) of the 1961 Act, carried forward) and treaty exemption for
stays under 183 days where a non-resident employer pays and bears the salary."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-business-visa-2026-e-business-visa-rules-what-you-can-do-tax-pe-risk-foreign-visitors"

C = contact("your nationality, who is travelling and for how long, what they will do in India, who pays them, and whether you have or plan an Indian entity")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India Business Visa (2026): e-Business Visa Rules, What You Can and Cannot Do, and the Tax Side for Foreign Visitors",
    em="meetings yes, a job in India no.",
    kicker="/ Foreign companies &middot; Visiting India &middot; Updated 2026-11-24",
    lead=("<strong>Foreign founders, executives and staff visiting India for meetings, sales, site visits, setting up a company or hiring usually travel on an e-Business visa, applied for online on the official Indian visa portal.</strong> "
          "It is generally valid for one year with multiple entries, each stay capped at 180 days; fees depend on nationality. "
          "A business visa does <strong>not</strong> allow employment in India: someone who will work for an Indian entity or be paid in India needs an employment visa. Using a tourist visa for business can lead to deportation and a re-entry ban. "
          "The tax side matters too: salary for days worked in India can be taxable in India unless a short-stay or treaty exemption applies, long or frequent visits can create a <strong>permanent establishment</strong> for the foreign company, and foreign directors of an Indian company need a DIN."),
    sections=[
        ("/ Quick answers", "What foreign visitors ask.",
         ul("<strong>What can I do on an India business visa?</strong> Attend meetings and trade fairs, negotiate and sign contracts, explore or set up a business, recruit staff, inspect suppliers and give technical support to an Indian business you deal with.",
            "<strong>What can I not do?</strong> Take up employment with an Indian entity or draw a salary in India; that needs an employment visa.",
            "<strong>How long is it valid?</strong> The e-Business visa is generally valid for one year from grant with multiple entries, and each stay can last up to 180 days.",
            "<strong>How do I apply?</strong> Online on the official Indian government visa portal, with a passport valid for at least six months, a photo and usually a business card and details of the Indian company you will visit. Avoid unofficial sites that charge extra.",
            "<strong>How much does it cost?</strong> The fee depends on your nationality and is shown on the official portal when you apply.")),
        ("/ Visa and tax at a glance", "What changes with the length and nature of the visit.",
         table(["Situation", "Visa", "Tax and compliance point"], [
             ["Short visits for meetings, sales, setting up", "e-Business or regular business visa", "Salary usually stays taxable only at home if a short-stay or treaty exemption applies"],
             ["Employee of a foreign company, 90 days or less, foreign company has no business in India", "Business visa", "Indian law exempts the salary if it is not charged to an Indian business"],
             ["Longer visits, salary paid and borne by the foreign employer", "Business visa", "Most treaties exempt the salary for stays under 183 days, if no Indian entity or PE bears it"],
             ["Working for the Indian subsidiary or paid in India", "Employment visa", "Indian payroll tax and, usually, provident fund"],
             ["Staff spending long periods in India negotiating or delivering services", "Business visa", "Permanent establishment risk for the foreign company: Indian tax on profits linked to that work"],
             ["Director of an Indian company", "Business visa for board meetings", "DIN needed; sitting fees taxed in India; the company needs one director resident in India"]])),
        ("/ How we help", "Keep the visit simple and the tax clean.",
         ul("<strong>Before travel:</strong> check what the visitor will actually do, the likely days in India, and whether an Indian entity or a permanent establishment is in play.",
            "<strong>Salary and days:</strong> track days, apply the short-stay or treaty exemption correctly, or set up Indian payroll if needed; see " + L("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "expat tax in India") + ".",
            "<strong>Permanent establishment:</strong> review contracts, secondments and remote staff; see " + L("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "PE risk from staff in India") + ".",
            "<strong>Setting up:</strong> company, LLP, branch or employer of record; see " + L("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "India entry structure chooser") + ".",
            "<strong>Directors:</strong> DIN, PAN and the resident director; see " + L("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "foreign nationals registering a company") + ".")
         + call_box("business visits to India", ["Visa type versus what the visitor will do",
                                                  "Salary tax for days in India",
                                                  "Permanent establishment review",
                                                  "Indian entity, payroll or employer of record",
                                                  "Foreign directors: DIN, PAN, resident director"],
                    "nationality, travel plans, duties in India and who pays the visitor.")
         + sources("Government of India e-Visa portal and Bureau of Immigration guidance on e-Business visas (one year, multiple entry, 180 days per stay, FRRO registration beyond 180 days), as summarised by BAL, Fragomen, Wise and visa-requirements.io; Income-tax Act short-stay exemption for employees of foreign enterprises and tax treaty dependent personal services articles; Companies Act, 2013 (DIN, resident director). Visa rules are set by the Ministry of Home Affairs and can change; BQP advises on tax and company law, not immigration. Checked 24 November 2026.")),
    ],
    faqs=[("What can I do in India on a business visa?", "Attend meetings and trade fairs, negotiate and sign contracts, explore or set up a business, recruit staff, inspect suppliers and give technical support to an Indian business you deal with. You cannot take up employment in India or be paid by an Indian entity; that needs an employment visa."),
          ("How long is an India e-Business visa valid?", "Generally one year from grant, with multiple entries, and each stay can last up to 180 days. Registration with the Foreigners Regional Registration Office is needed if a business stay goes beyond 180 days."),
          ("How do I apply for an India business visa?", "Online on the official Indian government e-Visa portal, with a passport valid for at least six months, a photo, and usually a business card and details of the Indian company you will visit. The fee depends on your nationality; avoid unofficial sites that add charges."),
          ("Can I visit India on a tourist visa for business meetings?", "No. Business activity needs a business visa; using a tourist visa for business can lead to deportation and a ban on re-entry."),
          ("Will I pay Indian tax on my salary during a business trip?", "Often not for short trips: Indian law exempts employees of a foreign company that has no business in India for stays of 90 days or less, and most tax treaties exempt stays under 183 days when a foreign employer pays and bears the salary. Longer stays, work for an Indian entity or a permanent establishment change that."),
          ("Can BQP help with the tax side of business visits?", "Yes. " + C)],
    related=[("doing-business-in-india-2026-guide-for-foreign-companies-entity-tax-fdi-compliance-repatriation.html", "Doing business in India"),
             ("expat-tax-india-foreign-employee-residency-rnor-salary-pf-dtaa-2026.html", "Expat tax in India"),
             ("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "PE risk from staff in India"),
             ("employer-of-record-india-hire-from-abroad.html", "Employer of record in India"),
             ("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Foreign nationals registering a company")],
    cta_h="Sending people to India?", cta_b=C,
    keywords="India business visa, India e-business visa 2026, India business visa requirements, India business visa for US citizens, India business visa validity 180 days, business visa vs employment visa India, tax on business visitors India, permanent establishment business travel India",
    desc="India business visa (2026): e-Business visa generally one year, multiple entry, 180 days per stay, apply on the official portal; allows meetings, sales, setting up and hiring but not employment; tax side: salary exemptions for short stays (90 days / treaty 183 days), PE risk, foreign directors' DIN.",
    howto={"name": "How a foreign company plans a business visit to India", "description": "Visa and tax steps.", "steps": [
        {"name": "Define the activity", "text": "Meetings, sales and setting up fit a business visa; working for an Indian entity needs an employment visa."},
        {"name": "Apply on the official portal", "text": "Passport valid six months, photo, business card and host company details."},
        {"name": "Track days in India", "text": "Short-stay and treaty exemptions depend on days and who pays the salary."},
        {"name": "Check permanent establishment risk", "text": "Long or repeated stays delivering work can create Indian tax on profits."},
        {"name": "Plan the entity and directors", "text": "Subsidiary, LLP, branch or employer of record; DIN and a resident director."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GN complete")
