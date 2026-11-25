# -*- coding: utf-8 -*-
"""Batch IZ (25 Nov 2026): NRI income tax calculator India 2026-27 - tax on Indian income for a non-resident: slab income
under the new regime (nil to Rs 4 lakh ... 30% above Rs 24 lakh) or old regime (nil to Rs 2.5 lakh at any age, less
deductions), no section 87A rebate, equity STCG 20%, equity LTCG 12.5% above Rs 1.25 lakh, other LTCG 12.5%, surcharge
10/15/25% (37% old regime above Rs 5 crore) capped at 15% on gains, 4% cess; compares with TDS to show refund or tax due.
Logic: tools/nri-income-tax-logic.js (node tools/nri-income-tax-logic.test.js, 8 tests).
Demand: sweep ac115 (25 Nov 2026), all 7 markets: "nri tax calculator india", "nri tax calculator", "nri income tax
calculator", "nri tax slab in india 2026"."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 25 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/nri-income-tax-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { nriIncomeTax: nriIncomeTax, nriSlabTax: nriSlabTax };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed select{width:100%;padding:10px;border-radius:8px;border:1px solid #ccc;font-size:15px}\n")


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = ('<div class="field"><label for="nRegime">Tax regime <span class="hint">New is the default; old allows 80C, 80D etc.</span></label>'
          '<select id="nRegime"><option value="new">New regime (default)</option><option value="old">Old regime</option></select></div>'
          + fld("nSlab", "Indian income taxed at slab rates (INR)", "Rent after the 30% deduction, NRO interest, Indian salary, short-term gains on property etc.", "600000")
          + fld("nStcg", "Short-term gains on listed shares / equity funds (INR)", "Held 12 months or less; taxed at 20%.", "0")
          + fld("nLtcgEq", "Long-term gains on listed shares / equity funds (INR)", "Held over 12 months; 12.5% above INR 1.25 lakh.", "0")
          + fld("nLtcgOther", "Other long-term gains (INR)", "Property, unlisted shares, gold etc.; 12.5%.", "0")
          + fld("nDed", "Deductions (old regime only, INR)", "80C, 80D, home-loan interest etc.; ignored in the new regime.", "0")
          + fld("nTds", "TDS already deducted (INR)", "From Form 26AS / AIS; 0 if unknown.", "0"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=nriIncomeTax({regime:$("nRegime").value,slab:$("nSlab").value,stcg:$("nStcg").value,ltcgEq:$("nLtcgEq").value,ltcgOther:$("nLtcgOther").value,deductions:$("nDed").value,tds:$("nTds").value});
    var out=$("nOut"), list=$("nList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent="About "+inr(r.tax)+" tax ("+r.effective+"% of Indian income)";
    var items=["Tax on slab income ("+(r.regime==="old"?"old":"new")+" regime, no 87A rebate for NRIs): <strong>"+inr(r.slabTax)+"</strong>.",
      "Tax on capital gains at special rates: <strong>"+inr(r.cgTax)+"</strong>.",
      "Surcharge: <strong>"+inr(r.surcharge)+"</strong>; health and education cess at 4%: <strong>"+inr(r.cess)+"</strong>."];
    if(r.refund>0) items.push("TDS is higher than the tax: about <strong>"+inr(r.refund)+"</strong> can be claimed back by filing ITR-2 or ITR-3.");
    else if(r.due>0) items.push("Tax still payable after TDS: about <strong>"+inr(r.due)+"</strong> (advance tax or self-assessment tax).");
    items.push("Estimate only: marginal relief, treaty rates and set-off of losses are not applied.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["nRegime","nSlab","nStcg","nLtcgEq","nLtcgOther","nDed","nTds"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "nri-income-tax-calculator-india-2026-27-new-old-regime-capital-gains-tds-refund"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "NRI Income Tax Calculator India 2026-27",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Estimates an NRI's Indian income tax for 2026-27 under the new or old regime, with capital gains, surcharge, cess and the refund or tax due after TDS.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I am an NRI and want my Indian tax computed and my return filed.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your Indian income</h2><p class="sub">Enter yearly figures for 2026-27 (or 2025-26 to check a refund).</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="nOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="nList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Get it computed and filed &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your country of residence, days in India, Form 26AS / AIS and a list of your Indian income. "
           "We reply the same working day with a fixed-scope quote to compute your tax, claim refunds and file your return.")

PAGES = [dict(
    slug=SLUG,
    title="NRI Income Tax Calculator India 2026-27: New vs Old Regime, Capital Gains, Surcharge and Your Refund After TDS",
    em="no 87A rebate for NRIs, so check before you assume nil tax.",
    kicker="/ Calculator &middot; NRIs &middot; Indian income tax &middot; Updated 2026-11-25",
    lead=("<strong>NRIs pay Indian tax at the same slab rates as residents but without the section 87A rebate</strong>, so the &#8377;12 lakh tax-free limit does not apply: under the new regime tax starts above &#8377;4 lakh, and under the old regime above &#8377;2.5 lakh at any age. "
          "Capital gains are taxed at their own rates (20% on short-term equity gains, 12.5% on long-term gains), and TDS on NRI income is often higher than the final tax. "
          "Enter your Indian income to estimate the tax and see whether you are due a refund."),
    sections=[
        ("/ Calculator", "Estimate your Indian tax.", CALC
         + call_box("my NRI tax", ["Exact tax on your figures, both regimes",
                                    "ITR-2 / ITR-3 filing and TDS refunds",
                                    "Treaty rates with a tax residency certificate",
                                    "Lower TDS certificates for rent and property sales",
                                    "Residential status check"],
                    "Form 26AS / AIS, country of residence, days in India and income details.")),
        ("/ How it works", "The rules behind the numbers.",
         ul("<strong>Slab rates:</strong> new regime nil to &#8377;4 lakh, then 5%, 10%, 15%, 20%, 25% and 30% above &#8377;24 lakh; old regime nil to &#8377;2.5 lakh, 5%, 20% and 30% above &#8377;10 lakh.",
            "<strong>No 87A rebate</strong> for non-residents, and no higher senior-citizen exemption in the old regime.",
            "<strong>Capital gains:</strong> 20% on short-term gains on listed shares and equity funds; 12.5% on long-term equity gains above &#8377;1.25 lakh; 12.5% on other long-term gains such as property. NRIs cannot use unused basic exemption against these gains.",
            "<strong>Surcharge:</strong> 10% above &#8377;50 lakh, 15% above &#8377;1 crore, 25% above &#8377;2 crore (old regime 37% above &#8377;5 crore), capped at 15% on capital gains; plus 4% cess.",
            "<strong>TDS and refunds:</strong> TDS on payments to NRIs is often above the final tax; the excess comes back when you file ITR-2 or ITR-3.")
         + '<p>Read more: <a href="nri-income-tax-slab-india-2026-27-new-old-regime-no-87a-rebate-basic-exemption-surcharge-tds.html">NRI tax slab 2026-27</a> &middot; <a href="which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html">NRI ITR filing</a> &middot; <a href="nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html">NRI rent TDS refund calculator</a> &middot; <a href="nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html">NRO interest refund calculator</a> &middot; <a href="residential-status-calculator-india-nri-rnor-section-6.html">residential status calculator</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 2025 and Income-tax Act, 1961 (slab rates, section 87A / 156 rebate for residents, capital gains rates, surcharge and cess); Budget 2026 (no slab changes); site tax-rates 2026-27 guide. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How is income tax calculated for an NRI in India?", "Indian income taxed at slab rates is charged at the new-regime rates (nil to Rs 4 lakh) or old-regime rates (nil to Rs 2.5 lakh), without the 87A rebate; capital gains are added at their own rates, then surcharge and 4% cess."),
          ("Is there a tax calculator for NRIs?", "Yes, the calculator on this page estimates an NRI's Indian tax for 2026-27 under either regime, including equity and other capital gains, surcharge, cess and the refund or tax due after TDS."),
          ("Do NRIs get the Rs 12 lakh tax-free limit?", "No. That limit comes from the section 87A rebate, which is for resident individuals only."),
          ("How much tax does an NRI pay on Rs 10 lakh of Indian income?", "Under the new regime about Rs 41,600 including cess on Rs 10 lakh of slab income, because there is no 87A rebate; under the old regime more, unless deductions reduce it."),
          ("How can an NRI get a refund of excess TDS?", "By filing ITR-2 or ITR-3 for the year and claiming credit for the TDS shown in Form 26AS / AIS; the excess over the actual tax is refunded."),
          ("Can BQP compute and file my NRI tax?", "Yes. " + CONTACT)],
    related=[("nri-income-tax-slab-india-2026-27-new-old-regime-no-87a-rebate-basic-exemption-surcharge-tds.html", "NRI tax slab 2026-27"),
             ("which-itr-to-file-for-nri-ay-2026-27-itr-2-itr-3-refund-80c-deductions.html", "NRI ITR filing"),
             ("nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026.html", "NRI rent TDS refund calculator")],
    cta_h="Want your NRI tax worked out exactly?", cta_b=CONTACT,
    keywords="nri tax calculator india, nri income tax calculator, nri tax calculator 2026-27, nri tax slab calculator, nri capital gains tax calculator, nri tds refund calculator, nri new vs old regime",
    desc="Free NRI income tax calculator for India 2026-27: slab tax under the new or old regime without the 87A rebate, capital gains at 20% / 12.5%, surcharge and cess, and the refund or tax due after TDS.",
    howto={"name": "How to estimate an NRI's Indian income tax", "description": "Using the calculator.", "steps": [
        {"name": "Pick the regime", "text": "New (default) or old with deductions."},
        {"name": "Enter slab income", "text": "Rent after the 30% deduction, NRO interest, Indian salary."},
        {"name": "Enter capital gains", "text": "Short-term and long-term equity gains, other long-term gains."},
        {"name": "Enter TDS", "text": "From Form 26AS / AIS to see the refund or tax due."},
        {"name": "File the return", "text": "ITR-2 or ITR-3 to settle the tax and claim refunds."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IZ complete")
