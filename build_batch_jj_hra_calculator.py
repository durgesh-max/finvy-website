# -*- coding: utf-8 -*-
"""Batch JJ (25 Nov 2026): HRA exemption calculator 2026-27 - least of actual HRA, rent minus 10% of salary, and 50% of
salary in the eight listed cities (Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune, Ahmedabad - rule 279 of
the Income-tax Rules, 2026) or 40% elsewhere; salary = basic + DA forming part of retirement benefits + turnover-based
commission; old regime only (new regime: HRA fully taxable); shows which limit binds, taxable HRA and the rent needed
for full exemption. Logic: tools/hra-exemption-logic.js (node tools/hra-exemption-logic.test.js, 8 tests).
Demand: sweep ac119 (25 Nov 2026), all 7 markets: "hra exemption calculator", "hra exemption", "hra exemption rules",
"hra exemption formula", "hra exemption limit", "hra exemption in new tax regime", "hra exemption under which section".
Facts (checked 25 Nov 2026): site HRA exemption guide (section 10(13A), rule 2A -> rule 279, eight cities at 50% from
2026-27, old regime only, rent to parents)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 25 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/hra-exemption-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { hraExemption: hraExemption };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed select{width:100%;padding:10px;border-radius:8px;border:1px solid #ccc;font-size:15px}\n")


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


def sel(fid, label, hint, opts):
    o = "".join(f'<option value="{v}">{t}</option>' for v, t in opts)
    return f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><select id="{fid}">{o}</select></div>'


INPUTS = (sel("hRegime", "Tax regime", "HRA exemption is available only in the old regime.", [("old", "Old regime"), ("new", "New regime (no HRA exemption)")])
          + sel("hCity", "City where you rent", "50% for the eight listed cities from 2026-27, 40% elsewhere.", [("yes", "Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune or Ahmedabad"), ("no", "Any other city")])
          + fld("hBasic", "Basic salary for the year (INR)", "For the months you paid rent.", "600000")
          + fld("hDa", "DA forming part of retirement benefits (INR)", "0 if none.", "0")
          + fld("hComm", "Commission as a % of turnover (INR)", "0 if none.", "0")
          + fld("hHra", "HRA received for the year (INR)", "From your salary slips or Form 130 / Form 16.", "300000")
          + fld("hRent", "Rent paid for the year (INR)", "Actual rent for the same months.", "240000"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=hraExemption({regime:$("hRegime").value,metro:$("hCity").value,basic:$("hBasic").value,da:$("hDa").value,commission:$("hComm").value,hra:$("hHra").value,rent:$("hRent").value});
    var out=$("hOut"), list=$("hList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    if(r.regime==="new"){ out.textContent="No HRA exemption in the new regime"; list.innerHTML="<li>Under the new regime the full HRA of <strong>"+inr(r.taxable)+"</strong> is taxable. Compare regimes before choosing.</li>"; return; }
    out.textContent="HRA exempt: about "+inr(r.exempt)+" (taxable "+inr(r.taxable)+")";
    var lim={actual:"actual HRA received",rent:"rent paid minus 10% of salary",salary:r.pct+"% of salary"}[r.limit];
    var items=["Actual HRA received: <strong>"+inr(r.actual)+"</strong>.",
      "Rent paid minus 10% of salary ("+inr(r.salary)+"): <strong>"+inr(r.rentLess10)+"</strong>.",
      r.pct+"% of salary: <strong>"+inr(r.pctSalary)+"</strong>.",
      "The exemption is the lowest of the three; here it is set by the <strong>"+lim+"</strong>."];
    if(r.taxable>0 && r.limit==="rent") items.push("Rent of about <strong>"+inr(r.rentForFull)+"</strong> a year would be needed to exempt the HRA up to the other limits.");
    items.push("Estimate only: months without rent, changes in salary or city during the year and employer proofs can change the result.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["hRegime","hCity","hBasic","hDa","hComm","hHra","hRent"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "hra-exemption-calculator-2026-27-formula-metro-50-percent-8-cities-rent-old-regime"
GUIDE = "hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "HRA Exemption Calculator 2026-27",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Calculates the exempt and taxable part of house rent allowance for 2026-27: least of actual HRA, rent minus 10% of salary and 50% / 40% of salary, old regime only.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I want my HRA exemption and old vs new regime checked.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your salary and rent</h2><p class="sub">Enter yearly figures for 2026-27.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="hOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="hList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Get your HRA and regime checked &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your city, basic salary and DA, HRA received, rent paid and the tax year. "
           "We reply the same working day with a fixed-scope quote to check your HRA, compare regimes and fix your return.")

PAGES = [dict(
    slug=SLUG,
    title="HRA Exemption Calculator 2026-27: Formula, 50% for 8 Metro Cities, 40% Elsewhere, Rent Minus 10% of Salary and the Old Regime Rule",
    em="the lowest of three amounts is exempt.",
    kicker="/ Calculator &middot; Salaried employees &middot; HRA &middot; Updated 2026-11-25",
    lead=("<strong>HRA is exempt up to the least of three amounts: the HRA you actually receive, rent paid minus 10% of salary, and 50% of salary if you rent in Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune or Ahmedabad (40% elsewhere).</strong> "
          "From 2026-27 the 50% list has eight cities. The exemption is available only in the old tax regime; in the new regime the whole HRA is taxable. "
          "Enter your figures to see the exempt and taxable HRA."),
    sections=[
        ("/ Calculator", "Work out your HRA exemption.", CALC
         + call_box("my HRA and tax regime", ["HRA exemption on your actual figures",
                                               "Old vs new regime comparison",
                                               "Rent to parents and documentation",
                                               "Claiming missed HRA in the ITR",
                                               "Notices on HRA claims"],
                    "salary slips, rent receipts and the tax year.")),
        ("/ How HRA exemption works", "The rules behind the numbers.",
         ul("<strong>Three limits:</strong> actual HRA received; rent paid minus 10% of salary; 50% of salary in the eight listed cities or 40% elsewhere. The lowest is exempt and the rest is taxable.",
            "<strong>Salary for HRA:</strong> basic salary plus dearness allowance forming part of retirement benefits plus commission as a fixed percentage of turnover, for the period you paid rent.",
            "<strong>Eight cities at 50% from 2026-27:</strong> Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune and Ahmedabad, under rule 279 of the Income-tax Rules, 2026.",
            "<strong>Old regime only:</strong> the new regime does not allow the HRA exemption.",
            "<strong>Rent to parents:</strong> allowed if genuine, the parent owns the property, rent is actually paid and the parent reports it as income.")
         + f'<p>Full rules: <a href="{GUIDE}">HRA exemption 2026 guide</a> &middot; <a href="new-vs-old-tax-regime-calculator.html">new vs old regime calculator</a> &middot; <a href="tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html">TDS on salary and Form 130</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 1961, section 10(13A) and rule 2A; Income-tax Act, 2025 and rule 279 of the Income-tax Rules, 2026; site HRA guide. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How is HRA exemption calculated?", "HRA is exempt up to the least of the actual HRA received, rent paid minus 10% of salary, and 50% of salary in the eight listed cities or 40% elsewhere. The calculator on this page works it out from your figures."),
          ("Which cities get 50% HRA exemption in 2026-27?", "Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad, Pune and Ahmedabad. All other cities use 40% of salary."),
          ("Is HRA exemption available in the new tax regime?", "No. HRA exemption is allowed only in the old regime; under the new regime the full HRA is taxable."),
          ("What counts as salary for HRA?", "Basic salary plus dearness allowance forming part of retirement benefits plus commission as a fixed percentage of turnover, for the period the house was rented."),
          ("What if my rent is less than 10% of salary?", "Then rent minus 10% of salary is nil, so no HRA is exempt and the whole HRA is taxable."),
          ("Can BQP check my HRA claim?", "Yes. " + CONTACT)],
    related=[(GUIDE, "HRA exemption 2026 guide"),
             ("new-vs-old-tax-regime-calculator.html", "New vs old regime calculator"),
             ("tds-on-salary-section-392-old-192-rates-limit-calculation-form-130-2026-27.html", "TDS on salary and Form 130")],
    cta_h="Want your HRA and regime checked?", cta_b=CONTACT,
    keywords="hra exemption calculator, hra calculator, hra exemption calculation, hra exemption formula, hra exemption limit, hra exemption 2026-27, hra metro cities 50 percent, hra new regime",
    desc="Free HRA exemption calculator 2026-27: least of actual HRA, rent minus 10% of salary and 50% of salary (8 metro cities) or 40%; old regime only. See exempt and taxable HRA and the limit that applies.",
    howto={"name": "How to calculate HRA exemption", "description": "Using the calculator.", "steps": [
        {"name": "Pick the regime and city", "text": "Old regime; one of the eight cities or any other."},
        {"name": "Enter salary", "text": "Basic, DA forming part of retirement benefits, turnover commission."},
        {"name": "Enter HRA and rent", "text": "For the months you paid rent."},
        {"name": "Read the three limits", "text": "The lowest is exempt; the rest is taxable."},
        {"name": "Give proofs to your employer", "text": "Rent receipts and agreement, landlord PAN where required."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JJ complete")
