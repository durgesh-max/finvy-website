# -*- coding: utf-8 -*-
"""Batch BJ (11 Nov 2026): Income Tax Department nudging owners of undisclosed UAE (Dubai) property - FAST-DS.
Facts: Business Standard, 26 Oct 2026 (Finance Ministry sources): about 1,100 FAST-DS declarations so far; the department
has begun selectively contacting taxpayers who may hold undisclosed UAE residential or commercial property; regional
committees under Principal Chief Commissioners handle queries; outreach through companies, institutions and professional
bodies planned. A nudge is not a demand. FAST-DS: Category 2 INR 1 lakh (asset up to INR 5 crore, from taxed income or while
non-resident); Category 1 60% (aggregate up to INR 1 crore); declarations close 31 December 2026. The UAE levies no personal
income tax, so rent is taxable in India for residents and ordinarily residents with no foreign tax to credit. Black Money Act
small-asset relief excludes immovable property."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 11 November 2026."
CK_NR = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=30000000"
CK_TX = "fast-ds-2026-eligibility-checker.html?kind=asset&then=yes&src=taxedIndia&fa=no&inc=yes&val=30000000"
CK_RENT = "fast-ds-2026-eligibility-checker.html?kind=income&then=yes&inc=no&val=900000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the title deed or Oqood, how it was paid for and the years you lived in India. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "dubai-uae-property-not-disclosed-india-income-tax-nudge-fast-ds-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Got a message about UAE property, or expecting one?</p>'
       f'<p style="margin:0">A nudge is not a demand, but it shows the department is looking. Check your route in the FAST-DS checker: '
       f'<a href="{CK_NR}"><strong>bought while you were an NRI</strong></a> &middot; <a href="{CK_TX}"><strong>bought from income taxed in India</strong></a> &middot; <a href="{CK_RENT}">rent never taxed in India</a>. '
       f'Or message CA Durgesh Chavda on <a href="{wa("Hi Durgesh, I own property in Dubai/UAE that is not in my Indian return.")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Dubai or UAE Property Not in Your Indian Tax Return? The Income Tax Department Has Started Asking (FAST-DS 2026)",
    em="seven weeks left to fix it cheaply.",
    kicker="/ UAE property &middot; FAST-DS nudge &middot; Updated 2026-11-11",
    lead=("Business Standard reported on 26 October 2026, citing Finance Ministry sources, that the Income Tax Department has begun selectively contacting taxpayers who may hold undisclosed residential or commercial property in the UAE, as FAST-DS declarations reached about 1,100. "
          "If you are resident and ordinarily resident in India and own a flat, villa or off-plan unit in Dubai or elsewhere in the UAE that is not in Schedule FA, the cheapest fix closes on 31 December 2026: "
          "a flat INR 1 lakh under FAST-DS Category 2 if it was bought from income taxed in India or while you were an NRI, and the property is worth up to INR 5 crore."),
    sections=[
        ("/ Which route fits", "Source of money and value decide it.",
         table(["Your situation", "Route", "Cost"], [
             ["Bought while you were an NRI from UAE or other foreign earnings; not shown after you became resident", "FAST-DS Category 2", "INR 1 lakh (value up to INR 5 crore)"],
             ["Bought under the LRS from income taxed in India; not in Schedule FA", "FAST-DS Category 2", "INR 1 lakh"],
             ["Rent earned while resident and never offered to tax in India", "FAST-DS Category 1 (income)", "60%, within INR 1 crore in total"],
             ["Bought with money never taxed in India", "FAST-DS Category 1 (asset)", "60% of value, within INR 1 crore"],
             ["Above the INR 5 crore or INR 1 crore limits", "Not eligible for FAST-DS", "Regular route: revised or updated return where possible, advice on Black Money Act exposure"]])
         + BOX),
        ("/ UAE-specific points", "Where people go wrong.",
         ul("<strong>No UAE income tax means no credit in India.</strong> Rent from a UAE property is fully taxable in India for a resident and ordinarily resident, at slab rates, with no foreign tax to set off.",
            "<strong>Property gets no small-asset relief.</strong> The Black Money Act spares assets other than immovable property up to INR 20 lakh in total from the INR 10 lakh non-disclosure penalty; a UAE property gets no such relief at any value.",
            "<strong>Off-plan and instalment purchases</strong> still count once you hold rights in the unit; keep the developer's payment schedule and the remittance records.",
            "<strong>Value matters for eligibility:</strong> many Dubai properties are worth more than INR 5 crore. Value is taken as on 31 March 2026; check this before assuming Category 2 applies.",
            "<strong>Residential status:</strong> years spent working in the UAE as an NRI, and the first RNOR years after return, need no Schedule FA. Check with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>."))
        ,
        ("/ What to do this month", "Before 31 December 2026.",
         ul("Collect the title deed (or Oqood for off-plan), the payment trail and your returns for the years since purchase.",
            "Work out the value as on 31 March 2026 and whether rent was ever shown in India.",
            "File FAST-DS Form 1 on the e-Filing portal by 31 December 2026, pay after the Form 2 order, file Form 3, and receive Form 4.",
            "From then on, show the property in Schedule FA and the rent in your return every year you are resident and ordinarily resident.")
         + '<p>Related: <a href="house-flat-property-abroad-not-in-schedule-fa-fast-ds-returning-nri.html">property abroad and FAST-DS</a> &middot; <a href="income-tax-email-foreign-assets-fast-ds-what-to-do.html">received an income tax email about foreign assets?</a> &middot; <a href="fast-ds-what-happens-if-i-do-not-declare-black-money-act.html">what happens if you do not declare</a> &middot; <a href="fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html">payment dates</a>.</p>'
         f'<p><strong>Sources:</strong> Business Standard, &ldquo;I-T dept nudges UAE property owners as FAST-DS gets 1,100 declarations&rdquo;, 26 October 2026; Finance Act, 2026, Chapter IV (FAST-DS); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, sections 42 and 43. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is the Income Tax Department contacting people with property in Dubai?", "Yes. Business Standard reported on 26 October 2026, citing Finance Ministry sources, that the department has begun selectively nudging taxpayers who may hold undisclosed UAE residential or commercial property to use FAST-DS before 31 December 2026."),
          ("Is a nudge a tax demand?", "No. It is a prompt to review your return. But it shows the department has information, and after 31 December 2026 the FAST-DS route closes."),
          ("How much does FAST-DS cost for a Dubai flat?", "INR 1 lakh under Category 2 if it was bought from income taxed in India or while you were an NRI and is worth up to INR 5 crore as on 31 March 2026. Property bought with untaxed money, or rent never taxed, is Category 1 at 60% within INR 1 crore."),
          ("Is rent from a Dubai property taxable in India?", "Yes, for a resident and ordinarily resident. The UAE has no personal income tax, so there is no foreign tax credit to claim; the rent is taxed in India at slab rates."),
          ("My Dubai property is worth more than INR 5 crore. Can I use FAST-DS?", "Not under Category 2, which is limited to INR 5 crore. You need advice on the regular route, including revised or updated returns where they are still allowed."),
          ("Can BQP handle the declaration?", "Yes. " + CONTACT)],
    related=[("house-flat-property-abroad-not-in-schedule-fa-fast-ds-returning-nri.html", "Property abroad and FAST-DS"),
             ("income-tax-email-foreign-assets-fast-ds-what-to-do.html", "Income tax email about foreign assets"),
             ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker")],
    cta_h="Property in the UAE not in your return?", cta_b=CONTACT,
    keywords="Dubai property not disclosed India, UAE property income tax notice India, FAST-DS Dubai property, income tax nudge UAE property, Dubai flat Schedule FA, rent from Dubai property tax India, undisclosed foreign property India 2026",
    desc="The Income Tax Department has started nudging Indians with undisclosed UAE property (reported 26 October 2026). Which FAST-DS route fits a Dubai flat (INR 1 lakh or 60%), why UAE rent is fully taxable in India, the INR 5 crore limit, and what to do before 31 December 2026.",
    howto={"name": "How to regularise an undisclosed UAE property", "description": "Steps for a resident of India with UAE property missing from Schedule FA.", "steps": [
        {"name": "Collect documents", "text": "Title deed or Oqood, payment trail and returns since purchase."},
        {"name": "Value it as on 31 March 2026", "text": "Check it against the INR 5 crore Category 2 limit."},
        {"name": "Pick the category", "text": "Taxed income or NRI earnings: Category 2. Untaxed money or untaxed rent: Category 1."},
        {"name": "File Form 1 by 31 December 2026", "text": "Pay after Form 2, file Form 3, then report the property every year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BJ complete")
