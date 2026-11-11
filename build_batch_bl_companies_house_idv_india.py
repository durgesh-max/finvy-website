# -*- coding: utf-8 -*-
"""Batch BL (11 Nov 2026): Companies House identity verification for directors and PSCs of UK companies who live in India.
Facts: identity verification under the Economic Crime and Corporate Transparency Act 2023 became mandatory on
18 November 2025; new directors verify before appointment; existing directors and PSCs have a 12-month transition ending
18 November 2026, generally tied to the company's next confirmation statement; verification is through GOV.UK One Login
(biometric passport from any country) or an Authorised Corporate Service Provider (ACSP), which can also handle
non-biometric documents; a personal code is issued and used across all roles. Indian side: a resident of India holding
shares in a UK company needs FEMA overseas investment compliance (Form ODI; Annual Performance Report by 31 December each
year) and Schedule FA in the ITR when resident and ordinarily resident."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 11 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the UK company number and how the shares were funded. "
           "We reply the same working day with what is needed on the Indian side (ODI, APR, Schedule FA) and a fixed-scope quote.")
SLUG = "companies-house-identity-verification-director-living-in-india-18-november-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The UK check has an Indian twin</p>'
       f'<p style="margin:0">If you live in India and own shares in the UK company, India expects its own paperwork: the FEMA overseas investment filings, an <strong>Annual Performance Report by 31 December</strong> each year, and the shares in <strong>Schedule FA</strong> of your return. '
       f'Missed Schedule FA? <a href="fast-ds-2026-eligibility-checker.html?kind=asset&amp;then=yes&amp;src=taxedIndia&amp;fa=no&amp;inc=yes&amp;val=1000000">Check the FAST-DS route</a> before 31 December 2026, or message CA Durgesh Chavda on '
       f'<a href="{wa("Hi Durgesh, I live in India and am a director/shareholder of a UK company. Can you check my Indian compliance?")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Director of a UK Company Living in India? Companies House ID Verification Transition Ends 18 November 2026",
    em="verify once, use the code everywhere.",
    kicker="/ UK companies &middot; Companies House &middot; Updated 2026-11-11",
    lead=("Every director and person with significant control (PSC) of a UK company now has to verify their identity with Companies House, wherever they live. "
          "Verification became mandatory on 18 November 2025; people already in post have a twelve-month transition that ends on 18 November 2026, usually met at the company's next confirmation statement. "
          "From India, the quickest route is GOV.UK One Login with a biometric Indian passport; otherwise a UK Authorised Corporate Service Provider (ACSP) can verify you. "
          "If you also hold shares while living in India, Indian FEMA and income-tax reporting apply too."),
    sections=[
        ("/ What applies to you", "By role and timing.",
         table(["You are", "When to verify"], [
             ["A new director appointed after 18 November 2025", "Before appointment; the personal code is needed on the appointment filing"],
             ["An existing director", "With the company's next confirmation statement, and in any case by the end of the transition on 18 November 2026"],
             ["An existing PSC", "Within the PSC timing set by Companies House around the confirmation statement; check the official guidance for your company"],
             ["A director of several companies", "Once; the same personal code is used for every role, so the earliest confirmation statement sets your real deadline"]])
         + BOX),
        ("/ How to verify from India", "Two routes.",
         ol("<strong>GOV.UK One Login:</strong> create a One Login, use the app to scan a biometric passport (an Indian e-passport qualifies) and a face check, then receive your Companies House personal code.",
            "<strong>Through an ACSP:</strong> a UK-registered Authorised Corporate Service Provider verifies you and passes the confirmation to Companies House. This route also handles documents that the app cannot read.",
            "<strong>Give the personal code to whoever files</strong> the confirmation statement or appointment for the company.")
         + '<p>Indian set-up guides: <a href="uk-incorporation-indian-founder.html">UK incorporation for Indian founders</a> &middot; <a href="uk-ltd-indian-subsidiary-psc-filing-ca.html">UK Ltd with an Indian subsidiary: PSC and filings</a>.</p>'),
        ("/ The Indian side", "Often the part that is missed.",
         ul("<strong>FEMA overseas investment:</strong> a resident of India who acquires shares in a UK company does so under the Overseas Investment rules, with Form ODI reporting through the bank.",
            "<strong>Annual Performance Report:</strong> due by 31 December every year for each foreign entity, based on its accounts.",
            "<strong>Schedule FA:</strong> the shares go in your return every year you are resident and ordinarily resident (calendar-year basis), with any dividend in Schedule FSI.",
            "<strong>Shares bought while you were an NRI</strong> can be kept after you return (section 6(4) of FEMA), but still belong in Schedule FA.",
            "<strong>Missed reporting:</strong> shares funded from income taxed in India and missing from Schedule FA usually fall in FAST-DS Category 2 (INR 1 lakh) until 31 December 2026; FEMA delays are handled through late submission fees.")
         + f'<p><strong>Sources:</strong> Companies House guidance on identity verification under the Economic Crime and Corporate Transparency Act 2023; Foreign Exchange Management (Overseas Investment) Rules and Regulations, 2022; Income-tax return instructions for Schedule FA; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information. BQP advises on the Indian side; UK identity verification is done through GOV.UK One Login or a UK ACSP.</p>'),
    ],
    faqs=[("Do directors living in India need Companies House identity verification?", "Yes. Verification applies to every director and PSC of a UK company, wherever they live. Existing directors have until the end of the transition on 18 November 2026, usually at the company's next confirmation statement."),
          ("Can I verify with an Indian passport?", "Yes, a biometric (e-)passport from any country can be used through the GOV.UK One Login app. Otherwise, a UK Authorised Corporate Service Provider can verify you."),
          ("I am a director of three UK companies. Do I verify three times?", "No. You verify once and receive one personal code for all your roles. The earliest confirmation statement among your companies sets your practical deadline."),
          ("What happens if I do not verify?", "Filings that depend on your verification, such as the confirmation statement, can be held up, and acting as a director without verifying can be an offence. Check the Companies House guidance for your situation."),
          ("I live in India and own the UK company's shares. What do I owe in India?", "FEMA overseas investment reporting (Form ODI) and an Annual Performance Report by 31 December each year, plus the shares in Schedule FA of your return when you are resident and ordinarily resident."),
          ("Can BQP help?", "On the Indian side, yes. " + CONTACT)],
    related=[("uk-incorporation-indian-founder.html", "UK incorporation for Indian founders"),
             ("uk-ltd-indian-subsidiary-psc-filing-ca.html", "UK Ltd with an Indian subsidiary"),
             ("ca-for-fema-odi-compliance.html", "FEMA ODI compliance")],
    cta_h="UK company, Indian resident?", cta_b=CONTACT,
    keywords="Companies House identity verification India, UK director living in India ID verification, Companies House verification 18 November 2026, GOV.UK One Login Indian passport, ACSP verification non-resident director, UK company Indian resident ODI APR, UK company shares Schedule FA",
    desc="Directors and PSCs of UK companies who live in India must verify their identity with Companies House; the transition for existing directors ends on 18 November 2026. How to verify with an Indian passport (GOV.UK One Login or an ACSP) and the Indian ODI, APR and Schedule FA duties that come with UK shares.",
    howto={"name": "How a director living in India verifies with Companies House", "description": "Steps for a director or PSC of a UK company resident in India.", "steps": [
        {"name": "Find your earliest deadline", "text": "Check the next confirmation statement date of each company you are a director of."},
        {"name": "Verify through One Login or an ACSP", "text": "Use the GOV.UK One Login app with a biometric passport, or a UK ACSP."},
        {"name": "Share the personal code", "text": "Give it to whoever files the confirmation statement or appointment."},
        {"name": "Check the Indian side", "text": "Confirm ODI reporting, the Annual Performance Report by 31 December and Schedule FA for the shares."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BL complete")
