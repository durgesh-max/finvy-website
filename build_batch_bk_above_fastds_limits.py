# -*- coding: utf-8 -*-
"""Batch BK (11 Nov 2026): above the FAST-DS limits - options when undisclosed foreign income/assets exceed INR 1 crore
(Category 1) or an asset exceeds INR 5 crore (Category 2).
Facts: FAST-DS Category 1: 60% (30% tax + equal additional amount) for undisclosed foreign income/assets up to INR 1 crore
aggregate; Category 2: INR 1 lakh for assets from taxed income or NRI earnings up to INR 5 crore; declarations close
31 December 2026. Black Money Act: 30% tax on undisclosed foreign income/asset (s.3), penalty three times the tax (s.41),
INR 10 lakh for not furnishing return / not disclosing in return (ss.42, 43; relief up to INR 20 lakh for assets other than
immovable property), prosecution 6 months to 7 years for failure to furnish return or information (ss.49, 50).
Updated return: up to 48 months from the end of the assessment year (Finance Act 2025), with additional tax of 25%/50%/60%/70%
of tax and interest by year; only where it increases tax, not after search/survey or certain notices. Revised return for
FY 2025-26: free until 31 December 2026, fee until 31 March 2027."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 11 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with a short note of the assets, their values and the years involved. "
           "Discussions are confidential. We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "fast-ds-not-eligible-above-1-crore-5-crore-limit-what-are-the-options"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">First, check you are really over the limit</p>'
       f'<p style="margin:0">The limits apply per category, value is taken as on 31 March 2026, and assets bought from taxed income or NRI earnings fall in Category 2 (up to INR 5 crore), not the INR 1 crore Category 1 pool. '
       f'Split your items in the <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html"><strong>FAST-DS calculator</strong></a> before concluding the scheme is closed to you, or message CA Durgesh Chavda on '
       f'<a href="{wa("Hi Durgesh, my foreign assets may be above the FAST-DS limits. Can we discuss confidentially?")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Above the FAST-DS Limit? Options When Foreign Assets Exceed INR 5 Crore or Undisclosed Income Exceeds INR 1 Crore",
    em="the scheme is small; the exposure is not.",
    kicker="/ FAST-DS limits &middot; Regular route &middot; Updated 2026-11-11",
    lead=("FAST-DS is built for small taxpayers: Category 1 (60%) covers undisclosed foreign income or assets up to INR 1 crore in aggregate, and Category 2 (INR 1 lakh) covers assets from taxed income or NRI earnings worth up to INR 5 crore. "
          "Above those limits the scheme cannot be used, and the Black Money Act remains: 30% tax, a penalty of three times that tax, an INR 10 lakh penalty for non-disclosure, and possible prosecution. "
          "There is no equivalent amnesty, but acting before the department does still changes the outcome. This page sets out what is left, and why to get advice before 31 December 2026."),
    sections=[
        ("/ The limits, precisely", "Measured as on 31 March 2026.",
         table(["Category", "Who it is for", "Limit", "Cost under FAST-DS"], [
             ["Category 1", "Undisclosed foreign income, or assets bought from it", "Aggregate up to INR 1 crore", "60% (30% tax + equal additional amount)"],
             ["Category 2", "Assets from income taxed in India or earned abroad while NRI, missing from Schedule FA", "Asset value up to INR 5 crore", "INR 1 lakh"],
             ["Above either limit", "-", "-", "Not available; regular law applies"]])
         + BOX),
        ("/ What is left above the limit", "Each has limits of its own.",
         ul("<strong>Revised return (FY 2025-26 only):</strong> add the asset and any income to the latest return; free until 31 December 2026, with a fee until 31 March 2027. It does not cover earlier years.",
            "<strong>Updated return for earlier years:</strong> available up to 48 months from the end of the assessment year, with additional tax of 25% to 70% of the tax and interest depending on the delay. It needs additional income to report, so it cannot be used just to add an asset, and it is barred after a search, survey or certain notices.",
            "<strong>Paying tax on the income now:</strong> offering foreign interest, dividends, rent or gains to tax through the routes above narrows what can later be called undisclosed income.",
            "<strong>Documenting the source:</strong> for assets bought from taxed income or NRI earnings, the issue may be a reporting failure rather than undisclosed income, which changes the exposure. Bank trails, LRS records and past returns matter.",
            "<strong>Reporting every year from now on:</strong> Schedule FA from the next return, so the omission does not continue."))
        ,
        ("/ If nothing is done", "The Black Money Act route.",
         ul("<strong>Tax:</strong> 30% on the value of an undisclosed foreign asset or income, charged in the year it comes to the department's notice.",
            "<strong>Penalty:</strong> three times the tax, in addition to the tax.",
            "<strong>Non-disclosure penalty:</strong> INR 10 lakh for not disclosing a foreign asset in the return (no relief for immovable property, or once assets other than property exceed INR 20 lakh).",
            "<strong>Prosecution:</strong> failure to furnish a return or information about a foreign asset can lead to rigorous imprisonment of six months to seven years.",
            "<strong>Information is already flowing:</strong> CRS and FATCA data from partner countries, and targeted nudges such as those reported for UAE property owners in October 2026.")
         + '<p>Related: <a href="fast-ds-what-happens-if-i-do-not-declare-black-money-act.html">what happens if you do not declare</a> &middot; <a href="fast-ds-vs-revised-return-vs-updated-return-itr-u.html">FAST-DS vs revised return vs ITR-U</a> &middot; <a href="dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026.html">UAE property nudge</a> &middot; <a href="fast-ds-2026-eligibility-checker.html">FAST-DS checker</a>.</p>'
         f'<p><strong>Sources:</strong> Finance Act, 2026, Chapter IV (FAST-DS); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, sections 3, 41, 42, 43, 49 and 50; Finance Act, 2025 (updated return period). <em>{UPDATED}</em> General information, not advice for your situation; cases above the limits need individual advice.</p>'),
    ],
    faqs=[("What if my foreign assets are above the FAST-DS limit?", "FAST-DS cannot be used above INR 1 crore (Category 1) or INR 5 crore (Category 2). What remains is the revised return for FY 2025-26, updated returns for earlier years where additional income is involved, documenting the source of the money, and reporting correctly from now on."),
          ("Is the INR 5 crore limit per asset or in total?", "Check your items against the scheme's rules with an adviser; values are taken as on 31 March 2026, and Category 1 and Category 2 items are counted separately. Use the FAST-DS calculator to split your items first."),
          ("Can I use an updated return just to add a foreign asset?", "No. An updated return has to report additional income and increase tax. It cannot be used only to add an asset to Schedule FA, and it is barred after a search, survey or certain notices."),
          ("What does the Black Money Act charge if I do nothing?", "30% tax on the undisclosed foreign income or asset, a penalty of three times that tax, an INR 10 lakh penalty for non-disclosure in the return, and possible prosecution with imprisonment of six months to seven years."),
          ("Does it help to act before 31 December 2026 even if I cannot use FAST-DS?", "Yes. Correcting the latest return, paying tax on income through an updated return where allowed, and documenting the source of funds all narrow the exposure before the department acts."),
          ("Can BQP advise on a case above the limits?", "Yes. " + CONTACT)],
    related=[("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "If you do not declare: Black Money Act"),
             ("fast-ds-vs-revised-return-vs-updated-return-itr-u.html", "FAST-DS vs revised return vs ITR-U"),
             ("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS calculator")],
    cta_h="Above the FAST-DS limits?", cta_b=CONTACT,
    keywords="FAST-DS not eligible, FAST-DS above 5 crore, FAST-DS limit 1 crore, foreign assets above FAST-DS limit options, Black Money Act penalty 30% tax three times, undisclosed foreign assets large value India, updated return foreign income",
    desc="Foreign assets above INR 5 crore or undisclosed foreign income above INR 1 crore cannot use FAST-DS. What is left (revised return, updated return, source documentation), what the Black Money Act charges if nothing is done, and why to act before 31 December 2026.",
    howto={"name": "What to do if you are above the FAST-DS limits", "description": "Steps for residents whose undisclosed foreign assets exceed the FAST-DS limits.", "steps": [
        {"name": "Split items by category", "text": "Separate taxed-income and NRI-earnings assets (Category 2) from untaxed income (Category 1) and value them as on 31 March 2026."},
        {"name": "Confirm the limit is crossed", "text": "Check each category against its limit before ruling out FAST-DS."},
        {"name": "Correct the latest return", "text": "File a revised return for FY 2025-26; consider updated returns for earlier years where additional income is involved."},
        {"name": "Document the source and report going forward", "text": "Assemble bank, LRS and return records, and show every foreign asset in Schedule FA from the next return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BK complete")
