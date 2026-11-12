# -*- coding: utf-8 -*-
"""Batch BC (10 Nov 2026): demand-led pages.
1. FAST-DS payment: due date and interest calculator + how to pay (Form 2 -> ITNS 289 -> Form 3 -> Form 4).
   Facts: Finance Act 2026 s.135; e-Filing portal help on ITNS 289 (e-Pay Tax tile; post-login e-File > e-Pay Tax >
   Income Tax Act 1961 > New Payment > FAST-DS (ITNS 289)); one challan for the Form 2 amount; wrong ITNS 289 payments
   cannot be corrected or refunded; Form 3 intimation with proof; Form 4 certificate.
2. Form 40 (formerly Form 10-EE): relief for income from foreign retirement accounts, section 158 Income-tax Act 2025,
   rule 74 Income-tax Rules 2026; official Form 40 FAQ: notified countries USA, UK, Canada and Australia at present;
   option cannot be revoked and applies to all later tax years; file electronically by the return due date.
   Up to FY 2025-26: section 89A / Form 10-EE (US, UK, Canada notified).
Calculator logic: tools/fastds-payment-logic.js (tests: node tools/fastds-payment-logic.test.js)."""
import json, re
from urllib.parse import quote
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
UPDATED = "Last updated: 10 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">Message CA Durgesh Chavda on '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a> or email '
            f'<a href="mailto:durgesh@bharatquantumprospera.com">durgesh@bharatquantumprospera.com</a>.</p></div>')


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with a short note of your situation. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
PAGES = []

# ---------------------------------------------------------------- 1. FAST-DS payment calculator + steps
LOGIC = open("tools/fastds-payment-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { fastdsPayment: fastdsPayment, endOfMonthAfter: endOfMonthAfter };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")


def fld(fid, label, hint, kind, val=""):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="{kind}" value="{val}" {"min=\'0\' step=\'any\' inputmode=\'decimal\'" if kind == "number" else ""}/></div>')


INPUTS = (fld("pDecl", "Date you filed Form 1 (declaration)", "Optional if you already have Form 2.", "date", "2026-11-20")
          + fld("pOrder", "Date you received Form 2 (order)", "Leave blank if not received yet.", "date")
          + fld("pAmt", "Amount payable in Form 2 (INR)", "", "number", "100000")
          + fld("pPay", "Date you plan to pay", "Optional: shows interest if late.", "date"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function fmt(d){ if(!d) return "-"; var p=d.split("-"); return new Date(Date.UTC(+p[0],+p[1]-1,+p[2])).toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric",timeZone:"UTC"}); }
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=fastdsPayment({declarationDate:$("pDecl").value,orderDate:$("pOrder").value,amount:$("pAmt").value,paymentDate:$("pPay").value});
    var out=$("pOut"), list=$("pList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent="Pay by "+fmt(r.dueDate);
    var li=[];
    if(r.orderBy) li.push("Form 2 (order of amount payable) should be issued by <strong>"+fmt(r.orderBy)+"</strong>.");
    if(r.orderAssumed) li.push("Dates below assume Form 2 arrives on that last day. Re-check once you receive it.");
    li.push("Pay without interest by <strong>"+fmt(r.dueDate)+"</strong> (two months from the end of the month you receive Form 2).");
    li.push("Last date with interest: <strong>"+fmt(r.extendedDate)+"</strong> (1% simple interest for every month or part of a month).");
    if(r.status==="on time") li.push("Your planned date is on time: pay "+inr(r.total)+".");
    if(r.status==="late, within the extended period") li.push("Your planned date is "+r.months+" month(s) late: interest "+inr(r.interest)+", total "+inr(r.total)+".");
    if(r.status==="after the extended period") li.push("<strong>Your planned date is after the extended period.</strong> Speak to a CA before then: the declaration and immunity depend on paying in time.");
    li.push("Then file Form 3 (intimation of payment) with the challan, and download Form 4 (certificate) once issued.");
    list.innerHTML=li.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["pDecl","pOrder","pAmt","pPay"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "FAST-DS 2026 Payment Due Date and Interest Calculator",
       "url": f"{DOMAIN}/fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html", "applicationCategory": "FinanceApplication",
       "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Works out when Form 2 is due, the last date to pay FAST-DS without interest, the extended date and the 1% monthly interest.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your FAST-DS dates</h2><p class="sub">Use the dates on your Form 1 acknowledgement and Form 2.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="pOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="pList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa("Hi Durgesh, I received FAST-DS Form 2 and need help with payment and Form 3.")}" target="_blank" rel="noopener">Get help with Form 2, payment and Form 3 &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
PAY_SLUG = "fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4"
PAGES.append(dict(
    slug=PAY_SLUG,
    title="FAST-DS Payment: Due Date and Interest Calculator, ITNS 289 Challan, Form 3 and Form 4 Certificate (Step by Step)",
    em="what to do after you file Form 1.",
    kicker="/ FAST-DS 2026 &middot; Payment &middot; Updated 2026-11-10",
    lead=("Filing Form 1 by 31 December 2026 is only the first step. The Department issues Form 2 (the order of the amount payable) within one month from the end of the month you declare. "
          "You then pay through challan ITNS 289 within two months from the end of the month you receive Form 2, or within a further two months with simple interest of 1% for every month or part of a month. "
          "After paying, you file Form 3 with the proof, and the Department issues Form 4, the certificate that gives you immunity. Use the calculator for your own dates."),
    sections=[
        ("/ Calculator", "Your due dates and interest.", CALC + '<p style="font-size:13px">General information based on section 135 of the Finance Act, 2026. Check the dates on your own Form 2.</p>'),
        ("/ Step by step", "From Form 2 to the certificate.",
         ol("<strong>Watch for Form 2.</strong> It arrives in your e-Filing account (and by email) within one month from the end of the month you filed Form 1. Check the amount against your own working.",
            "<strong>Create the ITNS 289 challan.</strong> Before login: incometax.gov.in &rarr; e-Pay Tax &rarr; the &ldquo;Foreign Assets of Small Taxpayers Disclosure Scheme, 2026 [Challan No. ITNS 289]&rdquo; tile. After login: e-File &rarr; e-Pay Tax &rarr; Income Tax Act, 1961 &rarr; New Payment &rarr; FAST-DS (ITNS 289).",
            "<strong>Pay the exact Form 2 amount</strong> by net banking, card or UPI through an authorised bank. One ITNS 289 challan can be used for the amount in Form 2.",
            "<strong>File Form 3</strong> (intimation of payment) electronically with the challan details as proof, within the time allowed.",
            "<strong>Download Form 4</strong>, the certificate, once the Department verifies the payment. Keep it with your Form 1 and Form 2.",
            "<strong>Fix Schedule FA from 2026-27 onwards</strong>, so the same assets are reported every year.")
         + table(["Stage", "Time limit"], [["Form 1 declaration", "By 31 December 2026"], ["Form 2 order", "Within 1 month from the end of the month of declaration"],
                                           ["Payment (ITNS 289)", "Within 2 months from the end of the month Form 2 is received"], ["Late payment", "A further 2 months, simple interest 1% per month or part"],
                                           ["Form 3 intimation", "After payment, with proof"], ["Form 4 certificate", "Issued after verification"]])
         + box("Received Form 2?", "Hi Durgesh, I received FAST-DS Form 2 and want it checked before I pay.")),
        ("/ Mistakes to avoid", "These cannot be undone.",
         ul("<strong>Wrong challan or minor head.</strong> The portal warns that an incorrect payment under ITNS 289 cannot be corrected or refunded. Double-check the challan type before paying.",
            "<strong>Paying before Form 2.</strong> ITNS 289 is for the amount determined in Form 2; wait for the order.",
            "<strong>Forgetting Form 3.</strong> Paying is not the end: without Form 3 the Department cannot issue the certificate.",
            "<strong>Missing the extended date.</strong> Interest stops being an option after the further two months.",
            "<strong>Assuming the amount is refundable.</strong> Amounts paid under the scheme are not refunded.")
         + f'<p>Related: <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">FAST-DS cost calculator</a> &middot; <a href="fast-ds-2026-eligibility-checker.html">eligibility checker</a> &middot; <a href="fast-ds-2026-filing-help-chartered-accountant.html">filing help</a>.</p>'
         f'<p><strong>Sources:</strong> Finance Act, 2026, Chapter IV, section 135; FAST-DS Rules, 2026; Income Tax Department e-Filing help on the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026 and challan ITNS 289. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("When do I pay under FAST-DS?", "After you receive Form 2, the order of the amount payable. Pay within two months from the end of the month in which you receive it, or within a further two months with simple interest of 1% for every month or part of a month."),
          ("Which challan is used for FAST-DS?", "Challan ITNS 289, available on the e-Filing portal under e-Pay Tax (the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026 tile) or after login under e-File > e-Pay Tax > New Payment."),
          ("What are Form 3 and Form 4 under FAST-DS?", "Form 3 is your intimation of payment, filed with proof after paying. Form 4 is the certificate the Department issues after verifying the payment."),
          ("Is the 31 December deadline for payment?", "No. 31 December 2026 is the last date to file the declaration (Form 1). Payment follows Form 2, which comes later."),
          ("Can a wrong ITNS 289 payment be refunded?", "The portal states that an incorrect payment made under ITNS 289 cannot be corrected or refunded, so check the challan and amount carefully."),
          ("Can BQP handle Form 2, payment and Form 3?", "Yes. " + CONTACT)],
    related=[("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS cost calculator"), ("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help"),
             ("fast-ds-what-happens-if-i-do-not-declare-black-money-act.html", "If you do not declare")],
    cta_h="Form 2 in hand?", cta_b=CONTACT,
    keywords="FAST-DS payment, ITNS 289 challan, FAST-DS Form 2 order, FAST-DS Form 3 intimation of payment, FAST-DS Form 4 certificate, FAST-DS payment due date, FAST-DS interest 1% per month, how to pay FAST-DS",
    desc="FAST-DS 2026 payment calculator and steps: Form 2 within a month, pay via challan ITNS 289 within two months (or two more with 1% monthly interest), then Form 3 and the Form 4 certificate.",
    howto={"name": "How to pay under FAST-DS 2026 and get the certificate", "description": "From the Form 2 order to the Form 4 certificate under the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026.", "steps": [
        {"name": "Receive Form 2", "text": "Form 2, the order of amount payable, is issued within one month from the end of the month of your Form 1 declaration."},
        {"name": "Generate challan ITNS 289", "text": "On the e-Filing portal choose e-Pay Tax and the FAST-DS 2026 (ITNS 289) tile, or after login e-File > e-Pay Tax > New Payment."},
        {"name": "Pay the Form 2 amount", "text": "Pay within two months from the end of the month you received Form 2, or within a further two months with 1% simple interest per month or part."},
        {"name": "File Form 3", "text": "Submit Form 3, the intimation of payment, with the challan as proof."},
        {"name": "Download Form 4", "text": "Download the Form 4 certificate after the Department verifies the payment."}]}))

# ---------------------------------------------------------------- 2. Form 40
F40_SLUG = "form-40-foreign-retirement-account-401k-ira-uk-pension-rrsp-super-defer-tax-india"
PAGES.append(dict(
    slug=F40_SLUG,
    title="Form 40 (Formerly Form 10-EE): Defer Indian Tax on Your 401(k), IRA, UK Pension, RRSP or Australian Super After Moving Back",
    em="section 158 of the Income-tax Act, 2025.",
    kicker="/ Returning NRIs &middot; Foreign retirement accounts &middot; Updated 2026-11-10",
    lead=("When you become resident in India, growth inside a foreign retirement account can be taxable in India every year, even though the US, UK, Canada or Australia taxes it only when you withdraw. "
          "The relief lets you align the two: income from the account is taxed in India when it is taxed abroad on withdrawal. From tax year 2026-27 it sits in section 158 of the Income-tax Act, 2025 and rule 74 of the Income-tax Rules, 2026, and you claim it by filing Form 40 electronically by the return due date. "
          "Up to FY 2025-26 the same relief was section 89A, claimed in Form 10-EE. The official Form 40 FAQ lists the USA, the UK, Canada and Australia as notified countries at present."),
    sections=[
        ("/ At a glance", "Old and new.",
         table(["", "Up to FY 2025-26", "From tax year 2026-27"], [
             ["Law", "Section 89A, Income-tax Act, 1961; rule 21AAA", "Section 158, Income-tax Act, 2025; rule 74, Income-tax Rules, 2026"],
             ["Form", "Form 10-EE", "Form 40"],
             ["Notified countries", "USA, UK, Canada", "USA, UK, Canada and Australia (per the official Form 40 FAQ, at present)"],
             ["When to file", "By the due date of the return", "Electronically by the due date of the return"],
             ["Can you withdraw the option?", "No, it continues for later years", "No; once exercised it applies to that year and all later years"]])
         + box("Moved back with a 401(k), IRA, pension, RRSP or super?", "Hi Durgesh, I moved back to India and have a foreign retirement account. Should I file Form 40?")),
        ("/ Who it helps", "Typical cases.",
         ul("Returning from the US with a <strong>401(k) or IRA</strong> that keeps growing while you live in India.",
            "Returning from the UK with a <strong>workplace pension or SIPP</strong>.",
            "Returning from Canada with an <strong>RRSP</strong>.",
            "Returning from Australia with <strong>superannuation</strong>: now listed as notified in the Form 40 FAQ, which matters because super was outside the old section 89A list.")
         + "<p>The relief is about <em>when</em> income is taxed, not whether. You still report the account every year in Schedule FA, and withdrawals are taxed in India in the year they are taxed abroad, with credit for foreign tax under the treaty.</p>"),
        ("/ Before you file", "Check these first.",
         ol("Your residential status for the year: in RNOR years foreign income is generally not taxed in India, so the relief may not be needed yet.",
            "That the account was opened while you were resident in the notified country.",
            "Every retirement account you hold in that country: the option covers all of them and cannot be revoked later.",
            "That the return due date has not passed: miss it and the relief is lost for that year.",
            "Whether earlier years were reported. If the account was never in Schedule FA, look at FAST-DS before 31 December 2026.")
         + f'<p>Related: <a href="fast-ds-rsu-espp-us-shares-401k-which-category.html">FAST-DS for RSUs and 401(k)</a> &middot; <a href="fast-ds-uk-pension-isa-canada-rrsp-australia-super-schedule-fa.html">FAST-DS for UK pensions, RRSP and super</a> &middot; <a href="h1b-holders-returning-to-india-tax-rnor-401k-2026.html">H-1B holders returning to India</a> &middot; <a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 2025, section 158; Income-tax Rules, 2026, rule 74 and Form 40; Income Tax Department FAQs on Form 40; Income-tax Act, 1961, section 89A and rule 21AAA (Form 10-EE). <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("What is Form 40 in the Income-tax Rules, 2026?", "The form to opt for relief on income from a retirement account in a notified country, under section 158 of the Income-tax Act, 2025 and rule 74. It replaces Form 10-EE, which was used under section 89A."),
          ("Is Form 10-EE still used?", "For income up to FY 2025-26 under the Income-tax Act, 1961, yes. From tax year 2026-27 the relief is claimed in Form 40."),
          ("Which countries are notified for the foreign retirement account relief?", "The official Form 40 FAQ lists the USA, the UK, Canada and Australia at present. Under the old section 89A, the notified countries were the USA, the UK and Canada."),
          ("When must Form 40 be filed?", "Electronically by the due date for filing the income-tax return for the year. Missing it means losing the relief for that year."),
          ("Can I withdraw the Form 40 option later?", "No. Once exercised it cannot be revoked for that tax year and applies to all subsequent tax years."),
          ("Does Form 40 mean my 401(k) is tax-free in India?", "No. It defers Indian tax so that income is taxed when it is taxed abroad on withdrawal. You still report the account in Schedule FA every year."),
          ("Can BQP file Form 40 and my return?", "Yes. " + CONTACT)],
    related=[("fast-ds-rsu-espp-us-shares-401k-which-category.html", "FAST-DS for RSUs and 401(k)"), ("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "H-1B holders returning to India"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator")],
    cta_h="Back in India with a foreign pension?", cta_b=CONTACT,
    keywords="Form 40 income tax, Form 10-EE replaced, section 158 Income-tax Act 2025, section 89A foreign retirement account, 401k tax India returning NRI, IRA tax India, UK pension tax India, RRSP tax India, Australian super tax India, defer tax foreign retirement account India",
    desc="Form 40 (formerly Form 10-EE): how returning NRIs defer Indian tax on a 401(k), IRA, UK pension, RRSP or Australian super under section 158 of the Income-tax Act, 2025. Notified countries, due date, and why the option is permanent.",
    howto={"name": "How to claim relief on a foreign retirement account with Form 40", "description": "Steps for a resident in India with a retirement account in the USA, UK, Canada or Australia.", "steps": [
        {"name": "Confirm residential status", "text": "Check whether you are resident and ordinarily resident for the tax year; in RNOR years the relief may not be needed."},
        {"name": "List all accounts in the country", "text": "The option covers every retirement account you hold in that notified country."},
        {"name": "File Form 40", "text": "File Form 40 electronically on the e-Filing portal by the due date of the return."},
        {"name": "Report in your return", "text": "Report the accounts in Schedule FA and tax withdrawals in the year they are taxed abroad."}]}))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BC complete:", len(PAGES), "pages")
