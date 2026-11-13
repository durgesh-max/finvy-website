# -*- coding: utf-8 -*-
"""Batch BX (13 Nov 2026): setting up a Global Capability Centre (GCC) in India - checklist for US, UK and European
companies, with the 2026 safe harbour and the H-1B fee context.
Facts: from tax year 2026-27 a single transfer pricing safe harbour applies to software development, ITeS, KPO and
contract R&D services: 15.5% on operating expenses, for transactions up to INR 2,000 crore (previously 17-24% with an
INR 300 crore limit), with automated approval valid for five years; related-party data centre services have a 15% safe
harbour (Budget 2026). The USD 100,000 H-1B fee announced in September 2025 was extended by a September 2026 proclamation
and has been challenged in court with conflicting rulings. FDI in IT services is 100% automatic route; Form FC-GPR within
30 days of allotment; SEZ income-tax holiday is closed to units starting after 31 March 2020; export of services can be
zero-rated under GST with an LUT."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 13 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the parent's country, the functions planned for India and the expected headcount. "
           "We reply the same working day with the set-up plan, the transfer pricing approach and a fixed-scope quote.")
SLUG = "gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The 2026 safe harbour changes the maths for mid-size GCCs</p>'
       f'<p style="margin:0">A single 15.5% cost-plus margin for IT, ITeS, KPO and contract R&amp;D, now available up to INR 2,000 crore and approved for five years, removes most transfer pricing disputes for a new centre. We set up the entity, the intercompany agreement and the safe harbour filing: '
       f'<a href="{wa("Hi Durgesh, we are planning a GCC in India. Can you help with setup and transfer pricing?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Setting Up a Global Capability Centre (GCC) in India in 2026: Entity, 15.5% Safe Harbour and Compliance Checklist",
    em="a captive team with fewer tax arguments.",
    kicker="/ US, UK &amp; European companies &middot; GCC set-up &middot; Updated 2026-11-13",
    lead=("A Global Capability Centre is a company's own engineering, operations or analytics team in India, usually run as a wholly owned Indian subsidiary that charges the parent cost plus a margin. "
          "Two 2026 developments make it easier to justify: from tax year 2026-27 a single transfer pricing safe harbour of <strong>15.5% on operating expenses</strong> covers software, ITeS, KPO and contract R&amp;D for transactions up to INR 2,000 crore, approved for five years; and the uncertainty over the USD 100,000 H-1B fee has pushed more US companies to build teams in India instead. "
          "The set-up itself is a sequence: entity, bank and FDI reporting, intercompany agreement, safe harbour election, then payroll and ongoing compliance."),
    sections=[
        ("/ Set-up sequence", "From decision to first payroll.",
         ol("<strong>Choose the model:</strong> start with an employer of record or contractors for a pilot team, or go straight to a subsidiary; see <a href=\"foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html\">EOR vs contractor vs subsidiary</a>.",
            "<strong>Incorporate a private limited company:</strong> 100% foreign ownership is allowed under the automatic route for IT and IT-enabled services; see <a href=\"foreign-company-setup-indian-subsidiary-wos.html\">setting up a wholly owned subsidiary</a>.",
            "<strong>Capitalise and report:</strong> bring in share capital through banking channels at not less than fair value and file Form FC-GPR within 30 days of allotment.",
            "<strong>Intercompany agreement:</strong> a services agreement with the parent setting out the functions, cost base and mark-up, signed before invoicing starts.",
            "<strong>Elect the safe harbour</strong> where it fits, so the cost-plus margin is accepted for five years.",
            "<strong>Register and run:</strong> GST with a letter of undertaking for zero-rated exports, payroll registrations, and STPI or SEZ registration if the facilitation suits the business."))
        ,
        ("/ The 2026 safe harbour", "What changed in Budget 2026.",
         table(["Item", "Before", "From tax year 2026-27"], [
             ["Services covered", "Separate bands for software, ITeS, KPO, contract R&amp;D", "One category: software development, ITeS, KPO and contract R&amp;D"],
             ["Margin", "17% to 24% on cost depending on the service and size", "15.5% on operating expenses"],
             ["Size limit", "INR 300 crore", "INR 2,000 crore"],
             ["Approval", "Annual, discretionary", "Automated, valid for five years once elected"],
             ["Data centres", "Not covered", "15% for related-party data centre services"]])
         + BOX
         + '<p>Outside the safe harbour, the centre needs a transfer pricing study, an annual accountant&rsquo;s report and documentation; see <a href="transfer-pricing-india-foreign-mnc.html">transfer pricing for foreign MNCs</a> and <a href="delaware-c-corp-indian-engineering-center-transfer-pricing-ca.html">a US company&rsquo;s Indian engineering centre</a>.</p>'),
        ("/ Points that cause trouble later", "Plan them in.",
         ul("<strong>Permanent establishment:</strong> keep contract authority with the parent and the Indian company's role documented, so the parent does not create a taxable presence in India.",
            "<strong>GST classification:</strong> make sure the services qualify as exports and watch the intermediary question for support functions.",
            "<strong>SEZ:</strong> the old SEZ income-tax holiday is closed to units that began after 31 March 2020; SEZ and STPI still give customs and procedural benefits.",
            "<strong>Employee stock plans:</strong> parent RSUs granted to Indian employees create perquisite tax, withholding and cross-charge questions.",
            "<strong>Annual cycle:</strong> audit, corporate tax return, transfer pricing report, the FLA return by 15 July and ROC filings.")
         + '<p>Related: <a href="india-market-entry-foreign-company-guide.html">India market entry for foreign companies</a> &middot; <a href="fla-return-foreign-liabilities-assets-rbi-india.html">FLA return</a> &middot; <a href="ca-in-whitefield-bangalore-for-saas-gcc.html">GCC support in Bengaluru</a>.</p>'
         f'<p><strong>Sources:</strong> Union Budget 2026-27 and the Income-tax Rules, 2026 on safe harbour; FEMA (Non-debt Instruments) Rules, 2019 and the consolidated FDI policy; SEZ Act provisions on the income-tax deduction; US presidential proclamations of September 2025 and September 2026 on H-1B fees and related court rulings. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("What is the transfer pricing safe harbour for GCCs in India from 2026?", "From tax year 2026-27, a single safe harbour covers software development, ITeS, KPO and contract R&D: a 15.5% margin on operating expenses for transactions up to INR 2,000 crore, approved for five years once elected. It replaces the earlier 17-24% margins and INR 300 crore limit."),
          ("Can a US company own 100% of an Indian GCC?", "Yes. IT and IT-enabled services are under the automatic route for 100% foreign direct investment. The Indian company reports the investment on Form FC-GPR within 30 days of allotting shares."),
          ("Should we start with an employer of record or a subsidiary?", "An employer of record suits a small pilot team; a subsidiary suits a planned centre with a growing team. Many companies start with an EOR and move to a subsidiary once the team passes a handful of people."),
          ("Does the H-1B fee matter for an India GCC decision?", "It has added to the case for building teams in India. The USD 100,000 fee announced in September 2025 was extended in September 2026 and has faced conflicting court rulings, so check the current position with US immigration counsel."),
          ("Do GCCs still get SEZ tax holidays?", "Not for units that started after 31 March 2020. SEZ and STPI registration can still offer customs and procedural benefits."),
          ("Can BQP set up and run the GCC's finance and compliance?", "Yes. " + CONTACT)],
    related=[("foreign-company-remote-employee-india-pe-risk-eor-contractor-subsidiary-2026.html", "EOR vs contractor vs subsidiary"),
             ("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs"),
             ("foreign-company-setup-indian-subsidiary-wos.html", "Setting up an Indian subsidiary")],
    cta_h="Planning a GCC in India?", cta_b=CONTACT,
    keywords="GCC India setup, global capability centre India 2026, safe harbour 15.5% IT services, GCC transfer pricing India, US company GCC India, H-1B fee India GCC, Indian subsidiary cost plus, safe harbour 2000 crore",
    desc="Setting up a Global Capability Centre in India in 2026: entity and FDI steps, the new 15.5% transfer pricing safe harbour for software, ITeS, KPO and contract R&D (up to INR 2,000 crore, five-year approval), GST, SEZ and PE points, and the H-1B fee context for US companies.",
    howto={"name": "How to set up a GCC in India", "description": "Steps for a foreign company setting up its own centre in India.", "steps": [
        {"name": "Choose the model", "text": "Pilot with an EOR or go straight to a wholly owned subsidiary."},
        {"name": "Incorporate and capitalise", "text": "Form a private limited company and report the FDI on Form FC-GPR within 30 days."},
        {"name": "Sign the intercompany agreement", "text": "Set functions, cost base and mark-up before invoicing."},
        {"name": "Elect the safe harbour and register", "text": "Elect the 15.5% safe harbour where eligible; register for GST with an LUT and set up payroll."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BX complete")
