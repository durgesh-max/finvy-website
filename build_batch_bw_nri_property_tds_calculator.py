# -*- coding: utf-8 -*-
"""Batch BW (12 Nov 2026): NRI property sale TDS calculator - TDS on the full price (no certificate) vs tax on the actual
long-term gain, and the amount a lower deduction certificate keeps out of the refund queue.
Facts: buyer deducts TDS under the non-resident provisions on the sale consideration unless a lower/nil certificate is
obtained; long-term gains on property transferred on or after 23 July 2024 at 12.5% without indexation, surcharge capped
at 15% for long-term gains (10% above INR 50 lakh, 15% above INR 1 crore), cess 4% (effective 14.95% at the top band);
short-term gains: TDS 30% plus surcharge and cess. Logic: tools/nri-property-tds-logic.js (node tools/nri-property-tds-logic.test.js)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


LOGIC = open("tools/nri-property-tds-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { nriPropertyTds: nriPropertyTds, nriSurcharge: nriSurcharge };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = (fld("tPrice", "Sale price (INR)", "Agreed consideration.", "12000000")
          + fld("tCost", "Purchase cost plus improvements (INR)", "From your purchase deed and bills.", "6000000")
          + '<div class="field"><label for="tTerm">How long have you held it?</label><select id="tTerm" style="width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;font:inherit">'
            '<option value="lt">More than 24 months (long-term)</option><option value="st">24 months or less (short-term)</option></select></div>')
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=nriPropertyTds({price:$("tPrice").value,cost:$("tCost").value,longTerm:$("tTerm").value==="lt"});
    var out=$("tOut"), list=$("tList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    if(!r.longTerm){ out.textContent="TDS at 30% plus surcharge and cess";
      list.innerHTML="<li>Short-term gains are taxed at your slab rates, but the buyer deducts TDS at 30% (plus surcharge and cess) on the price unless you hold a lower deduction certificate.</li><li>Send us the numbers and we will work out your actual tax and the certificate route.</li>"; return; }
    out.textContent=inr(r.excess)+" more TDS than tax";
    list.innerHTML=["Without a certificate, the buyer deducts about <strong>"+inr(r.tdsFull)+"</strong> (12.5% plus surcharge and cess on the full price).",
      "Estimated tax on your gain of "+inr(r.gain)+": <strong>"+inr(r.tax)+"</strong>.",
      "Difference waiting for a refund after you file your return: <strong>"+inr(r.excess)+"</strong>. A lower deduction certificate obtained before the sale aims to cut TDS to your actual tax.",
      "Estimate only: assumes this gain is your only Indian income and ignores exemptions (reinvestment, bonds) and marginal relief. Residents with property bought before 23 July 2024 may have a 20% with-indexation option; check whether it applies to you."]
      .map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["tPrice","tCost","tTerm"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "nri-property-sale-tds-calculator-lower-deduction-certificate-savings"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "NRI Property Sale TDS vs Actual Tax Calculator",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Compares the TDS a buyer deducts on the full sale price from an NRI with the estimated tax on the actual long-term gain.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your sale</h2><p class="sub">Use the agreed price and your documented cost.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="tOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="tList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa("Hi Durgesh, I am an NRI selling property in India. Can you apply for a lower TDS certificate?")}" target="_blank" rel="noopener">Apply for a lower TDS certificate with us &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the sale price, purchase cost and date, and your country. "
           "We reply the same working day with the lower-TDS route and a fixed-scope quote.")

PAGES = [dict(
    slug=SLUG,
    title="NRI Property Sale TDS Calculator: How Much Extra Tax the Buyer Withholds, and What a Lower TDS Certificate Saves",
    em="TDS on the price, tax on the gain.",
    kicker="/ Calculator &middot; NRI property sale &middot; Updated 2026-11-12",
    lead=("When an NRI sells property in India, the buyer deducts TDS on the <strong>full sale price</strong>, not on the profit: for a long-term sale that is 12.5% plus surcharge and cess, up to 14.95% of the price. "
          "Your actual tax is on the gain only, so the difference sits with the Income Tax Department until you file and get a refund. "
          "A lower or nil deduction certificate, obtained before the sale, aims to cut TDS to your real tax. Use the calculator to see the gap on your numbers."),
    sections=[
        ("/ Calculator", "TDS vs your actual tax.", CALC),
        ("/ How it works", "The rules behind the numbers.",
         ul("<strong>Rate:</strong> long-term gains on property (held more than 24 months) transferred on or after 23 July 2024 are taxed at 12.5% without indexation.",
            "<strong>Surcharge and cess:</strong> 10% surcharge above INR 50 lakh and 15% above INR 1 crore (capped at 15% for long-term gains), plus 4% cess.",
            "<strong>Base:</strong> without a certificate, the buyer applies these rates to the whole sale consideration.",
            "<strong>Short-term:</strong> TDS at 30% plus surcharge and cess on the price; your actual tax is at slab rates.",
            "<strong>Certificate:</strong> apply to the Income Tax Department with the sale details and your cost; the buyer then deducts at the certified rate.")
         + '<p>Next steps: <a href="nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html">selling from abroad with a power of attorney</a> &middot; <a href="nri-selling-indian-property-capital-gains.html">capital gains for NRIs</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating the proceeds</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax provisions on TDS on payments to non-residents, long-term capital gains on property after 23 July 2024 and lower deduction certificates; Finance (No. 2) Act, 2024. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How much TDS is deducted when an NRI sells property?", "For a long-term sale, 12.5% plus surcharge and cess on the full sale price unless the NRI has a lower deduction certificate; up to 14.95% of the price above INR 1 crore. For a short-term sale, 30% plus surcharge and cess."),
          ("Why is TDS more than my actual tax?", "Because the buyer applies the rate to the whole price, while your tax is only on the gain. The difference is refunded after you file your return."),
          ("What does a lower deduction certificate do?", "It authorises the buyer to deduct TDS at a lower or nil rate based on your estimated tax, so less money is locked up until the refund."),
          ("Can NRIs use indexation on property sales?", "Long-term gains on transfers from 23 July 2024 are taxed at 12.5% without indexation. The 20% with-indexation option for property bought before that date is framed for residents; check your case."),
          ("Is the calculator result exact?", "No. It assumes the gain is your only Indian income and ignores exemptions and marginal relief. Use it to size the gap, then get the certificate worked out on your documents."),
          ("Can BQP apply for the certificate?", "Yes. " + CONTACT)],
    related=[("nri-sell-property-in-india-from-abroad-power-of-attorney-tds-repatriation-2026.html", "Selling from abroad: POA, TDS, repatriation"),
             ("nri-selling-indian-property-capital-gains.html", "Capital gains for NRIs selling property"),
             ("buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", "Buying from an NRI: no TAN needed")],
    cta_h="Selling property in India as an NRI?", cta_b=CONTACT,
    keywords="NRI property sale TDS calculator, TDS on sale of property by NRI, lower deduction certificate NRI property, NRI TDS 12.5 percent property, NRI capital gains tax calculator India, TDS refund NRI property sale",
    desc="Calculator for NRIs selling property in India: the buyer deducts TDS on the full sale price (12.5% plus surcharge and cess, up to 14.95%), while tax is due only on the gain. See the gap on your numbers and how a lower deduction certificate keeps it out of the refund queue.",
    howto={"name": "How to reduce TDS on an NRI property sale", "description": "Steps to size and cut excess TDS.", "steps": [
        {"name": "Enter price and cost", "text": "Use the agreed price and documented purchase cost."},
        {"name": "Compare TDS with tax", "text": "See how much more the buyer would deduct than your estimated tax."},
        {"name": "Apply for a certificate", "text": "Apply for a lower or nil deduction certificate before the sale."},
        {"name": "File and claim the balance", "text": "File your return for the year of sale to claim any remaining refund."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    # consolidate with the older calculator page (same intent)
    CANON_OLD = "nri-property-tds-ldc-calculator"
    html = html.replace(f'<link rel="canonical" href="{DOMAIN}/{p["slug"]}.html"', f'<link rel="canonical" href="{DOMAIN}/{CANON_OLD}.html"', 1)
    write_page(p["slug"], html)
print("Batch BW complete")
