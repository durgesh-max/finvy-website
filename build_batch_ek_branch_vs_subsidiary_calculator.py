# -*- coding: utf-8 -*-
"""Batch EK (20 Nov 2026): Branch vs subsidiary India tax calculator for foreign companies - branch taxed as a foreign
company at 35% plus surcharge (2% above INR 1 crore, 5% above INR 10 crore) and 4% cess, no tax on remitting profits;
subsidiary under section 115BAA at 25.168% plus dividend withholding at the treaty rate (TRC and Form 10F) or 20% plus
surcharge and cess without a treaty. Treaty dividend rates as stated on the site's treaty pages (USA, Canada 15% with a
10% holding; Australia 15%; UK, Singapore (25% holding), UAE, Germany, Netherlands, Japan 10%; Mauritius (10% holding),
Saudi Arabia, Qatar (25% holding) 5%). Rates: Finance Act 2024 cut the foreign company rate from 40% to 35% (Deloitte
India highlights; PwC tax summaries). Logic: tools/branch-vs-subsidiary-logic.js (node tools/branch-vs-subsidiary-logic.test.js, 6 tests)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/branch-vs-subsidiary-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { branchVsSubsidiary: branchVsSubsidiary, BVS_TREATY: BVS_TREATY };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")

COUNTRIES = [("usa", "United States (15%, 10% holding)"), ("uk", "United Kingdom (10%)"), ("singapore", "Singapore (10%, 25% holding)"),
             ("uae", "UAE (10%)"), ("germany", "Germany (10%)"), ("netherlands", "Netherlands (10%)"), ("japan", "Japan (10%)"),
             ("canada", "Canada (15%, 10% holding)"), ("australia", "Australia (15%)"), ("mauritius", "Mauritius (5%, 10% holding)"),
             ("saudi", "Saudi Arabia (5%)"), ("qatar", "Qatar (5%, 25% holding)"), ("none", "Other / no treaty (20% plus cess)")]
OPTS = "".join(f'<option value="{v}">{l}</option>' for v, l in COUNTRIES)


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = (fld("bProfit", "Expected annual profit in India (INR)", "Taxable profit before tax.", "50000000")
          + f'<div class="field"><label for="bCountry">Parent company&rsquo;s country <span class="hint">Treaty dividend rate shown; needs a TRC and Form 10F.</span></label><select id="bCountry">{OPTS}</select></div>'
          + fld("bPayout", "Share of subsidiary profit paid as dividend (%)", "100 if all profit goes to the parent each year.", "100"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function pct(x){ return (x*100).toFixed(2) + "%"; }
  function show(){
    var r=branchVsSubsidiary({profit:$("bProfit").value,country:$("bCountry").value,payout:$("bPayout").value});
    var out=$("bOut"), list=$("bList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    var lower = r.saving > 0 ? "Subsidiary costs about "+inr(r.saving)+" less" : (r.saving < 0 ? "Branch costs about "+inr(-r.saving)+" less" : "About the same");
    out.textContent=lower;
    var items=["<strong>Branch:</strong> 35% plus surcharge and cess = <strong>"+inr(r.branchTax)+"</strong> ("+pct(r.branchRate)+"); remitting profits to head office has no further Indian tax.",
      "<strong>Subsidiary:</strong> corporate tax at 25.168% (section 115BAA) = <strong>"+inr(r.corpTax)+"</strong>.",
      "Dividend of "+inr(r.dividend)+" to the parent, withholding at "+pct(r.whtRate)+(r.treaty?" (treaty rate)":" (domestic rate, no treaty)")+" = <strong>"+inr(r.wht)+"</strong>.",
      "<strong>Subsidiary total:</strong> "+inr(r.subTax)+" ("+pct(r.subRate)+" of profit).",
      "Tax is only one factor: a branch needs RBI approval and can do only permitted activities; a subsidiary limits liability and permanent establishment exposure. Your home country may also tax and give credit.",
      "Estimate only: surcharge marginal relief, transfer pricing, MAT and home-country tax are not modelled."];
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["bProfit","bCountry","bPayout"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Branch vs Subsidiary India Tax Calculator",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Compares Indian tax on a foreign company's branch (35% plus surcharge and cess) with a subsidiary (25.168% plus dividend withholding at the treaty rate).",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, we are a foreign company comparing a branch and a subsidiary in India and would like a call.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your India numbers</h2><p class="sub">FY 2026-27 rates. Use a realistic steady-state profit.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="bOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="bList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="https://topmate.io/cadurgesh_chavda/741484" target="_blank" rel="noopener">Book a call to choose the structure &rarr;</a> &middot; <a href="{wa}" target="_blank" rel="noopener">WhatsApp</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Book a call at book-a-call.html, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your country, what you will do in India, "
           "expected revenue and profit, and how you plan to bring profits home.")

PAGES = [dict(
    slug=SLUG,
    title="Branch vs Subsidiary in India: Tax Calculator for Foreign Companies (2026) - 35% Branch Rate vs 25.17% Plus Dividend Withholding",
    em="see the total Indian tax on each structure for your country.",
    kicker="/ Calculator &middot; Foreign companies &middot; India entry &middot; Updated 2026-11-20",
    lead=("A foreign company&rsquo;s <strong>branch in India</strong> is taxed as a foreign company at <strong>35%</strong>, plus a 2% surcharge above INR 1 crore of profit or 5% above INR 10 crore, plus 4% cess. That is about <strong>36.4% to 38.2%</strong>, and profits sent back to head office carry no further Indian tax. "
          "An <strong>Indian subsidiary</strong> pays <strong>25.168%</strong> under section 115BAA. When it pays dividends to the parent, India withholds tax at the <strong>treaty rate</strong>, for example 15% for a US parent with a 10% holding, 10% for the UK, Singapore (25% holding), UAE, Germany, the Netherlands and Japan, and 5% for Mauritius, Saudi Arabia and Qatar. Without a treaty the rate is 20% plus surcharge and cess. "
          "For a US parent paying out all its profit, the two structures come out <strong>almost equal</strong>. For most treaty countries the subsidiary costs less, and it costs much less if profits are reinvested in India. "
          "Tax is only part of the decision: a branch needs RBI approval and can carry on only permitted activities, while a subsidiary limits liability. Enter your numbers below."),
    sections=[
        ("/ Calculator", "Branch vs subsidiary, total Indian tax.", CALC
         + call_box("Branch or subsidiary for our India business", ["Total tax under each structure on your projections",
                                                                    "RBI approval for a branch vs incorporating a subsidiary",
                                                                    "Dividends, buybacks and other ways to bring profits home",
                                                                    "Permanent establishment, transfer pricing and treaty documents",
                                                                    "Compliance calendar and costs of running each"],
                    "your country, planned activities in India, revenue and profit projections and how you plan to repatriate profits.")),
        ("/ How the numbers work", "Rates used and what is left out.",
         ul("<strong>Branch:</strong> 35% (cut from 40% by the Finance Act 2024), surcharge 2% above INR 1 crore and 5% above INR 10 crore, 4% cess; no tax on remitting branch profits.",
            "<strong>Subsidiary:</strong> 22% under section 115BAA plus 10% surcharge and 4% cess = 25.168%; no MAT under this regime.",
            "<strong>Dividends:</strong> treaty rate with a tax residency certificate and Form 10F (Form 41 from 1 April 2026); otherwise 20% plus surcharge and cess. See the <a href=\"india-us-dtaa-withholding-rates.html\">India-US withholding rates</a>.",
            "<strong>Reinvesting:</strong> profits kept in the subsidiary bear only the 25.168%; set the payout to see the effect.",
            "<strong>Home country:</strong> your country may tax branch profits or dividends and give credit for Indian tax; check both sides.",
            "<strong>Not modelled:</strong> surcharge marginal relief, transfer pricing adjustments, buyback or capital reduction routes, and state taxes.")
         + '<p>Related: <a href="india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html">India entry structure chooser</a> &middot; <a href="branch-office-vs-liaison-vs-wos-india-foreign.html">branch vs liaison vs subsidiary</a> &middot; <a href="permanent-establishment-risk-checker-india-foreign-company-2026.html">PE risk checker</a> &middot; <a href="get-capital-back-from-indian-subsidiary-dividend-buyback-capital-reduction-tax-2026.html">getting money back from a subsidiary</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax rates for foreign companies (35% from 1 April 2024, Finance Act 2024; Deloitte India tax highlights; PwC worldwide tax summaries) and section 115BAA; dividend articles of India&rsquo;s tax treaties as summarised on this site&rsquo;s treaty pages. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("What is the tax rate on a foreign company's branch in India?", "35% plus surcharge (2% above INR 1 crore, 5% above INR 10 crore) and 4% cess, about 36.4% to 38.2%; remitting branch profits has no further Indian tax."),
          ("What is the tax rate on an Indian subsidiary of a foreign company?", "25.168% under section 115BAA, plus withholding tax on dividends paid to the parent at the treaty rate or 20% plus surcharge and cess without a treaty."),
          ("Is a branch or a subsidiary cheaper for a US company in India?", "With all profits paid out as dividends at the 15% treaty rate, the total Indian tax is almost the same; a subsidiary is cheaper if profits are reinvested in India."),
          ("Which countries get a 5% or 10% dividend rate?", "Under the site's treaty summaries: 5% for Mauritius (10% holding), Saudi Arabia and Qatar (25% holding); 10% for the UK, Singapore (25% holding), UAE, Germany, the Netherlands and Japan; 15% for the US, Canada and Australia."),
          ("Is tax the only factor in choosing a branch?", "No. A branch needs RBI approval and can do only permitted activities; a subsidiary limits liability and permanent establishment exposure and is the usual route for operating businesses."),
          ("Can BQP model our structure?", "Yes. " + CONTACT)],
    related=[("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "India entry structure chooser"),
             ("branch-office-vs-liaison-vs-wos-india-foreign.html", "Branch vs liaison vs subsidiary"),
             ("permanent-establishment-risk-checker-india-foreign-company-2026.html", "PE risk checker")],
    cta_h="Choosing between a branch and a subsidiary?", cta_b=CONTACT,
    keywords="branch vs subsidiary India tax, foreign company branch tax rate India 35%, Indian subsidiary tax rate 25.17%, dividend withholding tax India treaty rate, branch office vs subsidiary India calculator, foreign company India tax calculator",
    desc="Calculator for foreign companies: Indian tax on a branch (35% plus surcharge and cess, no tax on remittance) vs a subsidiary (25.168% under 115BAA plus dividend withholding at treaty rates: US 15%, UK/Singapore/UAE 10%, Mauritius 5%). Payout and country inputs.",
    howto={"name": "How to compare a branch and a subsidiary in India", "description": "Use the calculator, then check non-tax factors.", "steps": [
        {"name": "Enter expected profit", "text": "A realistic steady-state annual profit in India."},
        {"name": "Choose the parent's country", "text": "The treaty dividend rate applies with a TRC and Form 10F."},
        {"name": "Set the payout", "text": "How much of the subsidiary's profit goes to the parent each year."},
        {"name": "Compare total tax", "text": "Branch at 35% plus surcharge and cess vs subsidiary 25.168% plus dividend tax."},
        {"name": "Check the non-tax factors", "text": "RBI approval, permitted activities, liability and PE exposure."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EK complete")
