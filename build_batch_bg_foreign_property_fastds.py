# -*- coding: utf-8 -*-
"""Batch BG (10 Nov 2026): a house or flat abroad missing from Schedule FA - FAST-DS route.
Facts: Schedule FA has a separate table for immovable property held outside India (calendar-year basis for residents and
ordinarily residents); the Black Money Act relief from the INR 10 lakh non-disclosure penalty (aggregate up to INR 20 lakh)
excludes immovable property at any value; FAST-DS Category 2 (INR 1 lakh, asset up to INR 5 crore) covers foreign assets
acquired from income taxed in India or while non-resident and not disclosed; untaxed income (e.g. rent never offered to
tax) is Category 1 at 60% within INR 1 crore; declarations close 31 December 2026; FEMA s.6(4) lets a resident hold
property abroad acquired while non-resident; residents can buy property abroad under the LRS."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 10 November 2026."
CK_NR = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=25000000"
CK_TX = "fast-ds-2026-eligibility-checker.html?kind=asset&then=yes&src=taxedIndia&fa=no&inc=yes&val=25000000"
CK_RENT = "fast-ds-2026-eligibility-checker.html?kind=income&then=yes&inc=no&val=600000"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the purchase deed, how it was paid for and the years you lived in India. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "house-flat-property-abroad-not-in-schedule-fa-fast-ds-returning-nri"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Why property is the riskiest asset to leave out</p>'
       f'<p style="margin:0">The Black Money Act spares small omissions from the INR 10 lakh penalty only for assets <em>other than</em> immovable property, up to INR 20 lakh in total. A house or flat abroad gets no such relief at any value. '
       f'Check your case: <a href="{CK_NR}"><strong>bought while you were an NRI</strong></a> &middot; <a href="{CK_TX}"><strong>bought from income taxed in India</strong></a> &middot; <a href="{CK_RENT}">rent never taxed</a>. '
       f'Or message CA Durgesh Chavda on <a href="{wa("Hi Durgesh, I own a property abroad that is not in my Schedule FA.")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Own a House or Flat Abroad That Is Not in Your Schedule FA? FAST-DS Before 31 December 2026",
    em="no small-asset relief for property.",
    kicker="/ Property abroad &middot; Schedule FA &middot; FAST-DS &middot; Updated 2026-11-10",
    lead=("If you are resident and ordinarily resident in India, a house, flat or plot you own outside India has to be shown in the immovable property table of Schedule FA every year, even if it earns nothing. "
          "Many returning NRIs keep the home they bought abroad and never list it. "
          "If it was bought while you were an NRI, or from income already taxed in India, FAST-DS Category 2 settles it for a flat INR 1 lakh (foreign assets up to INR 5 crore in total) if you declare by 31 December 2026. Rent that was never offered to tax is a separate Category 1 item at 60%."),
    sections=[
        ("/ Which route fits", "It depends on where the money came from.",
         table(["Your situation", "FAST-DS route", "Cost"], [
             ["Bought abroad while you were an NRI, from foreign earnings; not in Schedule FA after you became resident", "Category 2", "INR 1 lakh (foreign assets up to INR 5 crore in total)"],
             ["Bought under the LRS from income taxed in India; not in Schedule FA", "Category 2", "INR 1 lakh"],
             ["Rent from it earned while resident and never offered to tax in India", "Category 1 (income)", "60% of the income, within INR 1 crore"],
             ["Bought with money that was never taxed in India and cannot be explained", "Category 1 (asset)", "60% of the value, within INR 1 crore"],
             ["Shown in Schedule FA every year and rent offered to tax", "Not needed", "Nil"]])
         + BOX),
        ("/ What you still owe each year", "After the declaration.",
         ul("<strong>Schedule FA:</strong> list the property every year you are resident and ordinarily resident (calendar-year basis), with its cost and the income from it.",
            "<strong>Rent:</strong> taxable in India, with credit for tax paid abroad; file Form 67 before the return to claim it.",
            "<strong>Sale:</strong> the gain is taxable in India when you are resident and ordinarily resident, with credit for foreign tax under the treaty.",
            "<strong>FEMA:</strong> a property bought while you were non-resident can be kept after you return (section 6(4) of FEMA); residents can also buy property abroad under the Liberalised Remittance Scheme.",
            "<strong>RNOR years:</strong> in the first years back you may be resident but not ordinarily resident; Schedule FA does not apply then. Check with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="fast-ds-what-happens-if-i-do-not-declare-black-money-act.html">what happens if you do not declare</a> &middot; <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">FAST-DS calculator</a> &middot; <a href="fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html">payment dates</a>.</p>'),
        ("/ Before you declare", "Keep these ready.",
         ul("The purchase deed and proof of payment (foreign bank statements, or Form A2 and bank debit for an LRS remittance).",
            "Your residential status for each year from purchase to now.",
            "A value for the property as on 31 March 2026, the valuation date under FAST-DS, from a valuer in that country if you can.",
            "Rent received and tax paid abroad for each year you were resident in India, and whether it appeared in your returns.",
            "Any loan on the property: a mortgage does not remove the need to report the property.")
         + f'<p><strong>Sources:</strong> Income-tax return instructions for Schedule FA; Finance Act, 2026, Chapter IV (FAST-DS); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, sections 42 and 43; Foreign Exchange Management Act, 1999, section 6(4). <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Do I need to show a house abroad in Schedule FA if it earns no rent?", "Yes, if you are resident and ordinarily resident. Immovable property outside India has its own table in Schedule FA, whether or not it earns income."),
          ("Can FAST-DS cover a property abroad?", "Yes. A property bought while you were an NRI, or from income already taxed in India, and left out of Schedule FA usually falls in Category 2: a flat INR 1 lakh for foreign assets worth up to INR 5 crore in total, if you declare by 31 December 2026."),
          ("Does the INR 20 lakh relief under the Black Money Act cover property?", "No. The relief from the INR 10 lakh non-disclosure penalty applies only to assets other than immovable property. A property abroad gets no such relief at any value."),
          ("I never paid Indian tax on the rent. What then?", "Rent earned while you were resident and not offered to tax is undisclosed foreign income: Category 1 at 60%, within the INR 1 crore limit. The property itself may still be a Category 2 item."),
          ("Can I keep a property I bought abroad as an NRI after moving back?", "Yes. Section 6(4) of FEMA lets a resident hold property abroad that was acquired while non-resident. It still has to be in Schedule FA every year you are resident and ordinarily resident."),
          ("Can BQP handle the declaration?", "Yes. " + CONTACT)],
    related=[("fast-ds-returning-nri-foreign-accounts-not-reported.html", "FAST-DS for returning NRIs"),
             ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"),
             ("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "If you do not declare: Black Money Act")],
    cta_h="Property abroad missing from your return?", cta_b=CONTACT,
    keywords="foreign property Schedule FA, house abroad not disclosed India, FAST-DS immovable property, property abroad returning NRI tax, Black Money Act immovable property penalty, FEMA 6(4) property abroad, rent from foreign property India tax",
    desc="Resident in India with a house or flat abroad that is not in Schedule FA? Why property gets no small-asset relief under the Black Money Act, which FAST-DS category fits (INR 1 lakh or 60%), and what to report every year after. Declare by 31 December 2026.",
    howto={"name": "How to fix an undisclosed property abroad with FAST-DS", "description": "Steps for a resident of India with a foreign property missing from Schedule FA.", "steps": [
        {"name": "Trace how it was paid for", "text": "Foreign earnings while an NRI, or income taxed in India, points to Category 2; untaxed money points to Category 1."},
        {"name": "Value it as on 31 March 2026", "text": "Get a value as on the FAST-DS valuation date, ideally from a valuer in that country."},
        {"name": "Check rent for past years", "text": "Rent never offered to tax while resident is a separate Category 1 income item."},
        {"name": "File Form 1 by 31 December 2026", "text": "Declare on the e-Filing portal, pay after the Form 2 order, file Form 3, and report the property in Schedule FA from then on."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BG complete")
