# -*- coding: utf-8 -*-
"""Batch BF (10 Nov 2026): US Social Security received by a resident of India.
Facts: India-US DTAA Article 20(2): social security benefits and other public pensions paid by a Contracting State to a
resident of the other Contracting State (or a US citizen) are taxable only in the paying State (subject to Article 19,
government service). So US Social Security of a resident of India is taxable only in the US.
SSA: for nonresident aliens, 30% withheld on 85% of the benefit (effective 25.5%) unless a treaty exempts; the India
treaty exempts only benefits based on US federal, state or local government employment, for a resident and national
of India; SSA issues Form SSA-1042S. US citizens and green card holders are US tax residents: no NRA withholding,
benefits taxed under normal US rules on Form 1040. No US-India totalization agreement."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 10 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with your SSA-1042S or SSA-1099, your US status "
           "and the year you moved back. We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "us-social-security-taxable-in-india-dtaa-article-20-returning-nri"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">The account it lands in still counts</p>'
       f'<p style="margin:0">India does not tax the benefit, but once you are resident and ordinarily resident the US bank account it is paid into belongs in Schedule FA, and the interest on it is taxable in India. '
       f'Missed that in past returns? See <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> (declarations close 31 December 2026), or message CA Durgesh Chavda on '
       f'<a href="{wa("Hi Durgesh, I receive US Social Security in India and want to check my tax position.")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Is US Social Security Taxable in India? Article 20(2) of the India-US Tax Treaty for Returning NRIs (2026)",
    em="the US taxes it; India does not.",
    kicker="/ US Social Security &middot; India-US DTAA &middot; Updated 2026-11-10",
    lead=("No. Under Article 20(2) of the India-US tax treaty, US Social Security paid to a resident of India is taxable only in the United States, even after you become resident and ordinarily resident in India. "
          "What changes is the US side: if you are no longer a US citizen or green card holder, the Social Security Administration usually withholds 30% on 85% of each payment, an effective 25.5%. "
          "In your Indian return you show it as exempt under the treaty, and the US bank account it is paid into still goes in Schedule FA."),
    sections=[
        ("/ Who taxes it", "Depends on your US status.",
         table(["Your US status while living in India", "US tax on Social Security", "Indian tax"], [
             ["Not a US citizen or green card holder (nonresident alien)", "30% withheld on 85% of the benefit (25.5% effective); Form SSA-1042S", "None (Article 20(2)); show as exempt"],
             ["Nonresident alien, benefit based on US federal, state or local government work, and you are a resident and national of India", "Exempt from the US withholding under the treaty", "Check Article 19 (government service) first"],
             ["US citizen or green card holder", "No nonresident withholding; taxed under normal US rules on Form 1040 (up to 85% of the benefit)", "None (Article 20(2)); show as exempt"]])
         + BOX),
        ("/ In your Indian return", "What to do every year.",
         ul("<strong>Show the benefit as exempt income</strong> under the India-US treaty; do not add it to taxable income. Keep the SSA-1042S or SSA-1099 for the year.",
            "<strong>No foreign tax credit for it in India:</strong> India does not tax the benefit, so there is nothing to set the US tax against. Form 67 is needed only for foreign income India does tax, such as US bank interest or dividends.",
            "<strong>Schedule FA:</strong> once you are resident and ordinarily resident, report the US bank account the benefit is credited to (calendar-year basis), along with any other US accounts, IRAs or 401(k)s.",
            "<strong>RNOR years:</strong> in your first years back you may be resident but not ordinarily resident; Schedule FA does not apply then, and foreign income outside India is generally not taxed. Check with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>.",
            "<strong>A refund of over-withheld US tax</strong> (for example on a government-work benefit) is claimed from the IRS on Form 1040-NR, not in India.")
         + '<p>Related: <a href="us-green-card-holder-india-tax-complete-2026.html">green card holders living in India</a> &middot; <a href="h1b-holders-returning-to-india-tax-rnor-401k-2026.html">returning H-1B holders: RNOR and 401(k)</a> &middot; <a href="form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html">Form 40 for 401(k) and IRA income</a>.</p>'),
        ("/ Points people miss", "Before you assume it is all simple.",
         ul("<strong>Social Security is not the same as a 401(k) or IRA.</strong> Withdrawals from a 401(k) or IRA are not covered by Article 20(2) and can be taxable in India once you are resident and ordinarily resident; Form 40 may defer it.",
            "<strong>There is no US-India totalization agreement,</strong> so work years in India do not count towards the 40 US credits, and Indian Provident Fund rules are separate.",
            "<strong>US state tax</strong> is a separate question from federal tax and the treaty.",
            "<strong>Interest earned on the benefit</strong> after it reaches a US or Indian bank account is ordinary income and taxable in India when you are resident.")
         + f'<p><strong>Sources:</strong> Convention between India and the United States for the avoidance of double taxation, Article 20(2) (and Article 19); US Social Security Administration, nonresident alien tax withholding guidance; IRS Publication 915. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is US Social Security taxable in India?", "No. Under Article 20(2) of the India-US tax treaty, Social Security paid by the US to a resident of India is taxable only in the US. Show it as exempt income in your Indian return."),
          ("How much US tax is withheld from Social Security if I live in India?", "If you are not a US citizen or green card holder, the SSA usually withholds 30% on 85% of the benefit, an effective 25.5%. US citizens and green card holders are taxed under normal US rules instead."),
          ("Can I claim the US tax as a credit in India?", "No credit is needed for the benefit itself, because India does not tax it. Form 67 and foreign tax credit apply to foreign income India does tax, such as US interest or dividends."),
          ("Do I report the US bank account in Schedule FA?", "Yes, once you are resident and ordinarily resident. Report the account the benefit is paid into, on a calendar-year basis. Missed accounts can be fixed through FAST-DS until 31 December 2026."),
          ("Is a 401(k) or IRA treated the same way?", "No. Article 20(2) covers Social Security and public pensions, not 401(k) or IRA withdrawals, which can be taxable in India once you are resident and ordinarily resident. Form 40 may defer the tax."),
          ("Can BQP review my return?", "Yes. " + CONTACT)],
    related=[("us-green-card-holder-india-tax-complete-2026.html", "Green card holders living in India"),
             ("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "Returning H-1B holders: RNOR and 401(k)"),
             ("form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india.html", "Form 40 for foreign retirement accounts")],
    cta_h="Receiving US Social Security in India?", cta_b=CONTACT,
    keywords="US Social Security taxable in India, social security India US DTAA article 20, US social security returning NRI, SSA-1042S India, 25.5% withholding social security India, social security exempt ITR India, green card holder social security India",
    desc="US Social Security paid to a resident of India is taxable only in the US under Article 20(2) of the India-US tax treaty. US withholding (25.5% for nonresident aliens), how to show it as exempt in your Indian return, and the Schedule FA point most returning NRIs miss.",
    howto={"name": "How to report US Social Security in your Indian return", "description": "Steps for a resident of India who receives US Social Security.", "steps": [
        {"name": "Check your US status", "text": "Nonresident aliens get 25.5% withheld; US citizens and green card holders are taxed on Form 1040."},
        {"name": "Keep the SSA-1042S or SSA-1099", "text": "It shows the benefit and the US tax withheld for the year."},
        {"name": "Show the benefit as exempt", "text": "Report it as income exempt under the India-US treaty, Article 20(2)."},
        {"name": "Report the US account in Schedule FA", "text": "Once resident and ordinarily resident, list the account it is paid into and offer the interest to tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BF complete")
