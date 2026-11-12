# -*- coding: utf-8 -*-
"""Batch BS (12 Nov 2026): a foreign (US/UK/Singapore/UAE) company with one or a few remote employees in India.
Facts: salary for services rendered in India is taxable in India wherever it is paid; the payer's withholding (TDS on
salary) obligation extends to salary paid abroad for Indian services (Supreme Court, CIT v. Eli Lilly & Co., 2009);
permanent establishment risk depends on the treaty and facts: dependent-agent PE where a person in India habitually
concludes contracts, fixed-place PE where premises are at the enterprise's disposal; Indian tribunals have required
physical presence for service PE (Delhi ITAT, March 2024); the OECD's 2025 guidance on home-office PE is subject to
India's reservations. Options: employer of record (EOR), independent contractor (export of services, misclassification
risk), Indian subsidiary (FDI under the automatic route for most sectors, Form FC-GPR after share allotment)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your country, the roles you have or plan in India and what they do (engineering, sales, support). "
           "We reply the same working day with the options for your case and a fixed-scope quote.")
SLUG = "foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The role matters more than the headcount</p>'
       f'<p style="margin:0">One engineer writing code is a different risk from one salesperson signing contracts with Indian customers. Tell us what your India hires do and we will map the safest structure: '
       f'<a href="{wa("Hi Durgesh, we are a foreign company with remote employees in India. Which structure should we use?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a> or email durgesh@bharatquantumprospera.com.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Foreign Company With Remote Employees in India: PE Risk, Payroll Tax and EOR vs Contractor vs Subsidiary (2026)",
    em="one hire can create an Indian tax presence.",
    kicker="/ US, UK, Singapore &amp; UAE companies &middot; India hiring &middot; Updated 2026-11-12",
    lead=("A US, UK, Singapore or UAE company can hire people in India without an Indian entity, but it should choose the route deliberately. "
          "Salary for work done in India is taxable in India wherever it is paid, and the Supreme Court has held that the payer's duty to withhold tax extends to salary paid abroad for Indian services. "
          "The bigger risk is a permanent establishment (PE): if someone in India habitually concludes contracts for you, or works from premises at your disposal, India can tax part of your profits. "
          "The three common routes are an employer of record (EOR), independent contractors, and an Indian subsidiary."),
    sections=[
        ("/ The three routes", "Compared.",
         table(["Route", "Good for", "Watch out for"], [
             ["Employer of record (EOR)", "1-15 hires, fast start, no entity", "PE risk still depends on what the people do; EOR cost grows with headcount"],
             ["Independent contractor", "Genuine freelancers on defined projects", "Misclassification if they work like employees; sales roles concluding contracts create PE risk"],
             ["Indian subsidiary (private limited)", "Teams growing past a handful, sales in India, long-term presence", "Set-up and annual compliance, transfer pricing on cross-border charges, FDI reporting (Form FC-GPR)"]])
         + BOX),
        ("/ Where the PE risk comes from", "Treaty and facts decide it.",
         ul("<strong>Dependent agent:</strong> a person in India who habitually concludes contracts, or plays the principal role in concluding them, for the foreign company. Keep contract authority outside India.",
            "<strong>Fixed place:</strong> an office or premises at the company's disposal. An employee's home office is usually not at the company's disposal, but India has reservations on the OECD's 2025 home-office guidance, so document the arrangement.",
            "<strong>Service PE:</strong> under some treaties, services furnished through personnel in India beyond a period; Indian tribunals have required physical presence of personnel (Delhi ITAT, 2024).",
            "<strong>Senior management in India:</strong> if key decisions are taken from India, ask whether the company's place of effective management could shift.")
         + '<p>More: <a href="employer-of-record-india-hire-from-abroad.html">employer of record in India</a> &middot; <a href="transfer-pricing-india-foreign-mnc.html">transfer pricing for foreign MNCs</a> &middot; <a href="delaware-c-corp-indian-engineering-center-transfer-pricing-ca.html">US company with an Indian engineering centre</a>.</p>'),
        ("/ Moving to a subsidiary", "When and how.",
         ul("<strong>Triggers:</strong> a growing team, Indian customers, people in sales or management roles, or a fundraising or acquisition due diligence that will ask about India.",
            "<strong>Set-up:</strong> a private limited company with foreign shareholding under the automatic route for most sectors, share capital received through banking channels and Form FC-GPR reported after allotment.",
            "<strong>Ongoing:</strong> transfer pricing on the service fee charged to the parent, annual Form 3CEB, the annual return on foreign liabilities and assets (FLA), and payroll compliance.",
            "<strong>Moving staff over:</strong> transfer employees from the EOR or contractor arrangement with continuity of service terms agreed in writing.")
         + '<p>Related: <a href="repatriate-profits-india-foreign-parent.html">repatriating profits to the foreign parent</a> &middot; <a href="fla-return-foreign-liabilities-assets-rbi-india.html">FLA return</a> &middot; <a href="india-services-for-foreign-companies-complete-list.html">India services for foreign companies</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax provisions on salary for services rendered in India and withholding on salary; Supreme Court, CIT v. Eli Lilly &amp; Co. (India) (2009); OECD Model Tax Convention commentary on home-office PE (2025 update) and India&rsquo;s reservations; Delhi ITAT decision of March 2024 on service PE; FEMA (Non-debt Instruments) Rules, 2019 and Form FC-GPR. <em>{UPDATED}</em> General information, not advice for your situation; PE questions turn on the treaty and the facts.</p>'),
    ],
    faqs=[("Can a US company hire an employee in India without an Indian entity?", "Yes, through an employer of record or as an independent contractor, or directly with care. Salary for work done in India is taxable in India, and withholding obligations can extend to salary paid abroad, so the route should be chosen deliberately."),
          ("Does one remote employee in India create a permanent establishment?", "Not automatically. The risk depends on the treaty and what the person does: habitually concluding contracts for the company, or working from premises at the company's disposal, are the main triggers. Engineering roles carry less risk than sales roles."),
          ("Is an employer of record enough to avoid PE?", "An EOR handles employment and payroll, but PE risk still depends on the activities of the people in India. Keep contract authority outside India and document roles."),
          ("When should we set up an Indian subsidiary?", "Usually when the team grows past a handful, when you sell to Indian customers, when India staff hold sales or management roles, or before a fundraising or acquisition due diligence."),
          ("What compliance does an Indian subsidiary of a foreign company need?", "FDI reporting on share allotment (Form FC-GPR), transfer pricing on charges to the parent with an annual Form 3CEB, the FLA return, corporate tax and payroll compliance."),
          ("Can BQP advise our company?", "Yes. " + CONTACT)],
    related=[("employer-of-record-india-hire-from-abroad.html", "Employer of record in India"),
             ("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs"),
             ("india-services-for-foreign-companies-complete-list.html", "India services for foreign companies")],
    cta_h="Hiring in India from abroad?", cta_b=CONTACT,
    keywords="foreign company remote employee India, hire employee in India without entity, permanent establishment risk India remote worker, EOR vs subsidiary India, US company hiring in India tax, contractor vs employee India foreign company, India PE home office",
    desc="A US, UK, Singapore or UAE company with remote employees in India: when salary tax and withholding apply, where permanent establishment risk comes from (dependent agent, fixed place, service PE), and how to choose between an employer of record, contractors and an Indian subsidiary.",
    howto={"name": "How a foreign company should structure India hires", "description": "Steps for companies hiring people in India without an Indian entity.", "steps": [
        {"name": "List roles and activities", "text": "Separate engineering and support roles from sales and management roles."},
        {"name": "Check PE triggers", "text": "Keep contract authority outside India and avoid premises at the company's disposal."},
        {"name": "Pick the route", "text": "EOR or contractors for a small, low-risk team; an Indian subsidiary as the team or Indian sales grow."},
        {"name": "Plan the subsidiary step", "text": "Budget for FDI reporting, transfer pricing and payroll compliance when you move."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BS complete")
