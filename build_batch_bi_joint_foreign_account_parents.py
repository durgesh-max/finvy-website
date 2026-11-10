# -*- coding: utf-8 -*-
"""Batch BI (11 Nov 2026): parents in India (or a spouse) named on a foreign account - Schedule FA.
Facts: the ITR asks residents and ordinarily residents whether they held any asset outside India as beneficial owner,
beneficiary or otherwise, or had signing authority in any account outside India; Schedule FA has a separate table for
accounts in which the taxpayer has signing authority. Black Money Act s.43: penalty INR 10 lakh for a resident who held a
foreign asset as beneficial owner or otherwise (or was a beneficiary) and did not disclose it in the return; no penalty
where foreign assets other than immovable property total up to INR 20 lakh (from 1 October 2024). Schedule FA is not
required in NRI or RNOR years. FAST-DS declarations close 31 December 2026; revised return for FY 2025-26 free until
31 December 2026."""
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


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the account statements, whose money is in the account and each holder's residential status. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
SLUG = "parents-joint-holder-nri-child-foreign-account-schedule-fa-india"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">&ldquo;It is my son&rsquo;s money&rdquo; is not the test</p>'
       f'<p style="margin:0">The Black Money Act penalty of INR 10 lakh reaches a resident who held a foreign asset &ldquo;as a beneficial owner or otherwise&rdquo; and left it out of the return, unless foreign assets other than property total INR 20 lakh or less. '
       f'A name on the account is enough to raise the question. If your parents&rsquo; returns do not show it, fix it before 31 December 2026: message CA Durgesh Chavda on '
       f'<a href="{wa("Hi Durgesh, my parents in India are joint holders on my foreign account. Do they need to report it?")}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Parents in India Added to Your Foreign Bank Account? Their Schedule FA Duty, Explained (2026)",
    em="your account can be their reporting problem.",
    kicker="/ Joint holders &middot; Signing authority &middot; Schedule FA &middot; Updated 2026-11-11",
    lead=("Many NRIs add a parent in India as a joint holder or signatory on a US, UK or other foreign account for emergencies. "
          "If that parent is resident and ordinarily resident in India, the income-tax return asks whether they held any asset outside India as beneficial owner, beneficiary <em>or otherwise</em>, or had signing authority in any account outside India. "
          "A joint holding or signing authority means the account has to appear in the parent's Schedule FA, even when every rupee in it belongs to the child. The same applies to spouses on joint accounts."),
    sections=[
        ("/ Who reports what", "Resident and ordinarily resident holders only.",
         table(["Situation", "Schedule FA for the person in India"], [
             ["Parent is a joint holder of the child's foreign account", "Yes: report the account (as legal holder, noting the funds are the child's)"],
             ["Parent is only an authorised signatory", "Yes: in the Schedule FA table for accounts with signing authority"],
             ["Parent is only a nominee or beneficiary on death", "Generally no holding during life; reporting starts if the account passes to them"],
             ["Spouses hold a foreign account jointly, both resident and ordinarily resident", "Each should report it; the income is taxed in the hands of the spouse whose money it is"],
             ["The holder in India is NRI or RNOR that year", "No Schedule FA for that year"]])
         + BOX),
        ("/ Tax on the interest", "Reporting is not the same as owning the income.",
         ul("<strong>Whose income:</strong> interest follows the person who funded the account. A parent who only lends a name usually has no Indian tax on the interest, but still reports the account.",
            "<strong>Keep proof:</strong> the child's salary credits, transfer records and the bank's account-opening papers show whose money it is.",
            "<strong>If the parent funded it:</strong> then it is the parent's own foreign asset, its income is taxable in India, and it may be an LRS remittance with its own records.",
            "<strong>Residential status:</strong> parents who spend long periods abroad may be NRI or RNOR in some years. Check with the <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>."))
        ,
        ("/ If it was never reported", "Options before 31 December 2026.",
         ul("<strong>Revised return:</strong> adds the account to the FY 2025-26 return (free until 31 December 2026, with a fee until 31 March 2027).",
            "<strong>FAST-DS:</strong> gives immunity for earlier years for what is declared. Whether it is worth using for an account a parent only lends a name to depends on the amounts and the years; the INR 20 lakh rule matters here.",
            "<strong>Going forward:</strong> report it every year the parent is resident and ordinarily resident, or remove the parent from the account if the role is no longer needed.")
         + '<p>Related: <a href="fast-ds-returning-nri-foreign-accounts-not-reported.html">FAST-DS for returning NRIs</a> &middot; <a href="fast-ds-vs-revised-return-vs-updated-return-itr-u.html">FAST-DS vs revised return vs ITR-U</a> &middot; <a href="fast-ds-what-happens-if-i-do-not-declare-black-money-act.html">what happens if you do not declare</a> &middot; <a href="fast-ds-2026-eligibility-checker.html">FAST-DS checker</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax return instructions for Schedule FA (assets held as beneficial owner, beneficiary or otherwise; accounts with signing authority); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, section 43 as amended from 1 October 2024; Finance Act, 2026, Chapter IV (FAST-DS). <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("My parents are joint holders on my US bank account. Do they need to report it in India?", "Yes, if they are resident and ordinarily resident. The return covers foreign assets held as beneficial owner, beneficiary or otherwise, and accounts with signing authority, so a joint holding belongs in their Schedule FA even if the money is yours."),
          ("Do my parents pay tax on the interest?", "Usually not, if you funded the account: income follows the person whose money it is. They still report the account. Keep records showing the funds are yours."),
          ("My father is only a signatory. Does that count?", "Yes. Schedule FA has a separate table for accounts outside India in which you have signing authority."),
          ("What if they never reported it?", "The Black Money Act penalty of INR 10 lakh can apply to an asset held as beneficial owner or otherwise, unless foreign assets other than property total INR 20 lakh or less. A revised return for FY 2025-26 or a FAST-DS declaration by 31 December 2026 can fix it."),
          ("Does a nominee need to report the account?", "A nominee or beneficiary on death generally does not hold the account during the owner's life. Reporting starts if the account passes to them."),
          ("Can BQP review both returns?", "Yes. " + CONTACT)],
    related=[("fast-ds-returning-nri-foreign-accounts-not-reported.html", "FAST-DS for returning NRIs"),
             ("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "If you do not declare: Black Money Act"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator")],
    cta_h="Your name on a foreign account?", cta_b=CONTACT,
    keywords="joint foreign bank account Schedule FA, parents joint holder NRI account India tax, signing authority foreign account Schedule FA, spouse joint account foreign asset India, Black Money Act joint holder, NRI child US account parents India",
    desc="Parents in India named as joint holders or signatories on an NRI child's foreign account must usually show it in Schedule FA, even when the money is the child's. Who reports what, who pays tax on the interest, and how to fix missed years before 31 December 2026.",
    howto={"name": "How parents in India should handle a child's foreign account", "description": "Steps for a resident parent named on a foreign account.", "steps": [
        {"name": "Check the role", "text": "Joint holder or signatory means Schedule FA; a nominee only does not hold the account during the owner's life."},
        {"name": "Check residential status", "text": "Schedule FA applies only in years the parent is resident and ordinarily resident."},
        {"name": "Document whose money it is", "text": "Keep the child's transfer records so the interest is taxed in the right hands."},
        {"name": "Fix missed years", "text": "Use a revised return for FY 2025-26 or FAST-DS by 31 December 2026."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BI complete")
