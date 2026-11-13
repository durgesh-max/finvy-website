# -*- coding: utf-8 -*-
"""Batch BP (12 Nov 2026): returning to India from Australia - super, DASP, CGT on leaving, Australian property, India tax.
Facts (ATO): a Departing Australia Superannuation Payment (DASP) is available to former temporary visa holders who have
left Australia and whose visa has ended (not to citizens or permanent residents); DASP withholding: taxed element 35%,
untaxed element 45%, working holiday maker amounts 65%, tax-free component 0%. Ceasing Australian residency triggers CGT
event I1 for assets that are not taxable Australian property (e.g. most shares) unless the person elects to defer;
Australian real property stays in the Australian tax net; foreign residents generally cannot claim the main residence
exemption (from 1 July 2020, subject to the life events test). India: non-resident and RNOR years generally exclude foreign
income received outside India; Schedule FA once resident and ordinarily resident; Form 40 (Australia notified) defers Indian
tax on income accruing in specified foreign retirement accounts until withdrawal; FAST-DS Category 2 (INR 1 lakh) for assets
earned while NRI and missing from Schedule FA; declarations close 31 December 2026."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."
CK = "fast-ds-2026-eligibility-checker.html?kind=asset&then=no&since=yes&src=foreignWhileNR&fa=no&inc=yes&val=3000000"
F40 = "form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html"


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your visa status, leaving date, super fund and other Australian assets, and your stay in India for the last ten years. "
           "We reply the same working day with what is needed on the Indian side and a fixed-scope quote.")
SLUG = "returning-to-india-from-australia-super-dasp-cgt-property-india-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Back from Australia a few years and never listed the super or bank account?</p>'
       f'<p style="margin:0">Savings built from Australian salary while you were an NRI usually fit FAST-DS Category 2: a flat INR 1 lakh until 31 December 2026. '
       f'<a href="{CK}"><strong>Check it in the FAST-DS checker</strong></a> &middot; <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">super in Schedule FA</a> &middot; '
       f'<a href="{wa("Hi Durgesh, I moved back from Australia and want to check my super position in India.")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Returning to India From Australia: Super, DASP, CGT on Leaving and What India Taxes (2026)",
    em="your visa decides the super.",
    kicker="/ Returning NRIs &middot; Australia &middot; Updated 2026-11-12",
    lead=("What happens to your super depends on your visa. Former temporary visa holders can claim a Departing Australia Superannuation Payment (DASP) after leaving, with tax withheld at 35% on the taxed element; Australian citizens and permanent residents generally cannot, and their super stays until retirement age. "
          "Leaving Australia also triggers CGT event I1 on assets such as shares unless you elect to defer. "
          "In India, the first years back are usually non-resident or RNOR years; once you are resident and ordinarily resident, super and Australian accounts go in Schedule FA, and Form 40 can defer Indian tax on super until withdrawal."),
    sections=[
        ("/ Item by item", "Australian side and Indian side.",
         table(["Item", "When you leave Australia", "In India once resident and ordinarily resident"], [
             ["Super (temporary visa holder)", "DASP after departure once the visa ends: 35% on the taxed element, 45% untaxed, 65% for working holiday amounts", "If still held: Schedule FA; Form 40 can defer Indian tax on income inside"],
             ["Super (citizen or permanent resident)", "Generally preserved until retirement age; no DASP", "Schedule FA; Form 40 can defer Indian tax until withdrawal"],
             ["Shares and other non-property assets", "CGT event I1 on ceasing residency, unless you elect to defer", "Schedule FA; dividends and later gains taxed in India"],
             ["Australian home or investment property", "Stays in the Australian tax net; foreign residents generally lose the main residence exemption", "Schedule FA; rent and gains taxed in India with credit for Australian tax (Form 67)"],
             ["Bank accounts", "Can be kept", "Schedule FA; interest taxed in India with credit for any Australian tax"]])
         + '<p>More on deferral: <a href="' + F40 + '">Form 40 for Australian super and other foreign retirement accounts</a> (Australia is now notified).</p>'
         + BOX),
        ("/ Use the RNOR years well", "Planning points.",
         ul("<strong>Find your RNOR years</strong> with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>; foreign income and gains received outside India are generally not taxed in India then.",
            "<strong>DASP timing:</strong> a DASP paid into an account outside India in a non-resident or RNOR year is generally outside Indian tax; check the year before you claim.",
            "<strong>Selling Australian assets:</strong> plan sales around both the CGT event on leaving and your Indian RNOR window.",
            "<strong>NRE and FCNR accounts</strong> in India must be redesignated once you return for good; an RFC account can hold foreign currency. See <a href=\"nri-nre-nro-conversion-returning-india-2026.html\">NRE and NRO conversion on return</a>.",
            "<strong>Australian property you keep:</strong> rent is taxed in Australia as a foreign resident and, once you are resident and ordinarily resident, in India with credit for the Australian tax."))
        ,
        ("/ If you returned years ago", "Fix it before 31 December 2026.",
         ul("Super, accounts or shares built from salary earned while you were an NRI, not shown in Schedule FA after you became resident: <strong>FAST-DS Category 2, INR 1 lakh</strong> (foreign assets up to INR 5 crore in total).",
            "Australian rent, interest or dividends earned while resident and ordinarily resident and never offered to tax in India: <strong>Category 1, 60%</strong> within INR 1 crore.",
            "Declare by 31 December 2026, pay after the Form 2 order, and report every year after.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="indian-ca-for-clients-in-australia-new-zealand.html">Indian CA for clients in Australia and New Zealand</a> &middot; <a href="returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html">returning from the UK</a> &middot; <a href="returning-to-india-from-canada-rrsp-tfsa-departure-tax-india-tax-2026.html">returning from Canada</a>.</p>'
         f'<p><strong>Sources:</strong> Australian Taxation Office guidance on the Departing Australia Superannuation Payment and its tax rates, CGT event I1 on ceasing residency, and the main residence exemption for foreign residents; Income-tax return instructions for Schedule FA; Form 40 and the notification of Australia for foreign retirement accounts; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information. BQP advises on the Indian side; Australian filings need an Australian tax professional.</p>'),
    ],
    faqs=[("Can I withdraw my super when I leave Australia for India?", "Only if you were on a temporary visa: once you have left and the visa has ended you can claim a Departing Australia Superannuation Payment, with tax withheld at 35% on the taxed element (65% for working holiday amounts). Citizens and permanent residents generally have to wait until retirement age."),
          ("Is DASP taxable in India?", "Generally not if it is paid into an account outside India in a year you are non-resident or RNOR in India. Check your residential status for that year before claiming."),
          ("Is there an exit tax when leaving Australia?", "Ceasing Australian residency triggers CGT event I1 on assets such as shares that are not taxable Australian property, unless you elect to defer. Australian real property stays in the Australian tax net."),
          ("Do I report super in my Indian return?", "Yes, in Schedule FA once you are resident and ordinarily resident. Form 40 can defer Indian tax on income accruing in it until withdrawal, because Australia is a notified country."),
          ("I came back from Australia years ago and never reported my super. What now?", "If it was built from salary earned while you were an NRI, FAST-DS Category 2 settles it for a flat INR 1 lakh if you declare by 31 December 2026."),
          ("Can BQP help?", "On the Indian side, yes. " + CONTACT)],
    related=[(F40, "Form 40 for Australian super"),
             ("fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html", "Super in Schedule FA"),
             ("indian-ca-for-clients-in-australia-new-zealand.html", "Indian CA for clients in Australia")],
    cta_h="Moving back from Australia?", cta_b=CONTACT,
    keywords="returning to India from Australia tax, DASP India, super after moving to India, Australian super Schedule FA, CGT event I1 leaving Australia India, Australian property foreign resident India tax, moving back to India from Australia checklist",
    desc="Returning to India from Australia? Super and the Departing Australia Superannuation Payment (35% on the taxed element), CGT event I1 on leaving, Australian property as a foreign resident, how India taxes it all once you are resident and ordinarily resident, Form 40 for super, and FAST-DS (INR 1 lakh) before 31 December 2026.",
    howto={"name": "How to handle Australian assets when returning to India", "description": "Steps for NRIs moving back from Australia.", "steps": [
        {"name": "Check your super options", "text": "Temporary visa holders can claim DASP after leaving; citizens and permanent residents generally keep super until retirement age."},
        {"name": "Plan for CGT event I1", "text": "Decide whether to pay CGT on leaving or elect to defer for shares and similar assets."},
        {"name": "Map your Indian residential status", "text": "Find your non-resident and RNOR years with the residential status calculator."},
        {"name": "Report once resident and ordinarily resident", "text": "List super and Australian accounts in Schedule FA, use Form 40, and fix missed years through FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BP complete")
