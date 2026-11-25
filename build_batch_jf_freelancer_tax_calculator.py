# -*- coding: utf-8 -*-
"""Batch JF (25 Nov 2026): Freelancer tax calculator India 2026-27 - resident freelancers / consultants: profit under
section 44ADA (section 58 of the Income-tax Act, 2025) at 50% of receipts (or higher), up to Rs 75 lakh receipts where
cash receipts are within 5% (Rs 50 lakh otherwise), or actual profit; new regime slabs with the section 87A rebate up to
Rs 12 lakh and marginal relief just above; old regime slabs (age-based basic exemption) with deductions and the Rs 12,500
rebate up to Rs 5 lakh; surcharge and 4% cess; TDS (194J) credit; advance tax - 44ADA pays all by 15 March, otherwise
15 June / 15 September / 15 December / 15 March when tax after TDS is Rs 10,000 or more.
Logic: tools/freelancer-tax-logic.js (node tools/freelancer-tax-logic.test.js, 10 tests).
Demand: sweep ac117 (25 Nov 2026), all 7 markets: "tax calculator for freelancers in india", "tax calculator for
freelancers", "tax for freelancers in india", "income tax for freelancers in india", "taxation for freelancers in india".
Facts (checked 25 Nov 2026): incometaxindia.gov.in (small businessmen benefits, 44ADA Rs 75 lakh with cash up to 5%);
site 87A / new-vs-old calculator (Rs 60,000 rebate + marginal relief), advance tax and freelancer guides."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 25 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/freelancer-tax-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { freelancerTax: freelancerTax, flSlabTax: flSlabTax };', "")
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


INPUTS = (sel("fRegime", "Tax regime", "New is the default; old allows 80C, 80D etc.", [("new", "New regime (default)"), ("old", "Old regime")])
          + sel("fMethod", "How profit is worked out", "44ADA: 50% of receipts treated as profit, no books needed.", [("44ada", "Presumptive, section 44ADA"), ("actual", "Actual profit (receipts minus expenses)")])
          + fld("fReceipts", "Gross professional receipts for the year (INR)", "Fees from Indian and foreign clients, Upwork / Fiverr payouts, before expenses.", "1800000")
          + sel("fCash", "Cash receipts", "The 44ADA limit is INR 75 lakh only if cash is 5% or less.", [("yes", "5% or less of receipts"), ("no", "More than 5%")])
          + fld("fPct", "Profit declared under 44ADA (%)", "Minimum 50%; declare more if actual profit is higher.", "50")
          + fld("fExp", "Business expenses (actual-profit method only, INR)", "Software, internet, rent, depreciation etc.; ignored under 44ADA.", "0")
          + fld("fOther", "Other income (INR)", "Savings / FD interest, rent after 30% etc.", "0")
          + sel("fAge", "Age (old regime only)", "Higher basic exemption at 60+ in the old regime.", [("below60", "Below 60"), ("60", "60 to 79"), ("80", "80 or more")])
          + fld("fDed", "Deductions (old regime only, INR)", "80C, 80D, NPS etc.; ignored in the new regime.", "0")
          + fld("fTds", "TDS already deducted (INR)", "Usually 10% under section 194J from Indian clients; see Form 26AS / AIS.", "0"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=freelancerTax({regime:$("fRegime").value,method:$("fMethod").value,receipts:$("fReceipts").value,lowCash:$("fCash").value,pct:$("fPct").value,expenses:$("fExp").value,other:$("fOther").value,age:$("fAge").value,deductions:$("fDed").value,tds:$("fTds").value});
    var out=$("fOut"), list=$("fList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent=r.tax>0?("About "+inr(r.tax)+" tax ("+r.effective+"% of receipts)"):"No tax payable";
    var items=r.notes.slice();
    items.push("Profit "+(r.method==="44ada"?"under section 44ADA":"(receipts minus expenses)")+": <strong>"+inr(r.profit)+"</strong>; taxable income: <strong>"+inr(r.taxableIncome)+"</strong>.");
    items.push("Slab tax ("+r.regime+" regime): <strong>"+inr(r.slabTax)+"</strong>"+(r.rebate>0?"; section 87A rebate / marginal relief: <strong>-"+inr(r.rebate)+"</strong>":"")+".");
    if(r.surcharge>0) items.push("Surcharge: <strong>"+inr(r.surcharge)+"</strong>.");
    items.push("Health and education cess at 4%: <strong>"+inr(r.cess)+"</strong>.");
    if(r.refund>0) items.push("TDS is higher than the tax: about <strong>"+inr(r.refund)+"</strong> comes back when you file your return.");
    else if(r.due>0) items.push("Tax payable after TDS: about <strong>"+inr(r.due)+"</strong>.");
    if(r.advance==="single") items.push("Advance tax: under 44ADA pay it all by <strong>15 March</strong> to avoid interest.");
    if(r.advance==="four") items.push("Advance tax: 15% by 15 June, 45% by 15 September, 75% by 15 December, 100% by 15 March.");
    items.push("Estimate only: surcharge marginal relief, losses and special-rate income are not applied.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["fRegime","fMethod","fReceipts","fCash","fPct","fExp","fOther","fAge","fDed","fTds"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "freelancer-tax-calculator-india-2026-27-section-44ada-new-old-regime-87a-advance-tax"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Freelancer Tax Calculator India 2026-27",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Estimates income tax for a resident freelancer or consultant in India for 2026-27 under section 44ADA or actual profit, in the new or old regime, with the 87A rebate, cess, TDS and advance tax.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I am a freelancer and want my tax worked out and my return filed.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your freelance income</h2><p class="sub">Enter yearly figures for 2026-27 (April 2026 to March 2027).</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="fOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="fList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Get it worked out and filed &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your receipts for the year, how clients pay you (Indian, foreign, platforms), Form 26AS / AIS and any GST registration. "
           "We reply the same working day with a fixed-scope quote to compute your tax, plan advance tax and file your return.")

PAGES = [dict(
    slug=SLUG,
    title="Freelancer Tax Calculator India 2026-27: Section 44ADA vs Actual Profit, New vs Old Regime, 87A Rebate, TDS and Advance Tax",
    em="up to INR 24 lakh of receipts can mean nil tax under 44ADA.",
    kicker="/ Calculator &middot; Freelancers and consultants &middot; Income tax &middot; Updated 2026-11-25",
    lead=("<strong>Most Indian freelancers and consultants can use section 44ADA, which treats 50% of gross receipts as profit with no books of account, for receipts up to &#8377;75 lakh where cash receipts are within 5%.</strong> "
          "Under the new regime a resident pays no tax on taxable income up to &#8377;12 lakh because of the section 87A rebate, so receipts of up to &#8377;24 lakh under 44ADA can mean nil tax if there is no other income. "
          "Enter your figures to estimate the tax, see TDS refunds and know your advance tax dates."),
    sections=[
        ("/ Calculator", "Estimate your tax as a freelancer.", CALC
         + call_box("my freelance tax", ["Exact tax on your figures, both regimes",
                                          "44ADA or books of account: which suits you",
                                          "ITR-4 / ITR-3 filing and TDS refunds",
                                          "Advance tax planning",
                                          "GST registration and LUT for foreign clients"],
                    "your receipts, client mix and Form 26AS / AIS.")),
        ("/ How freelancers are taxed", "The rules behind the numbers.",
         ul("<strong>Section 44ADA:</strong> 50% of gross receipts is treated as profit (declare more if actual profit is higher); available to specified professionals such as IT, design, consulting, legal, medical and engineering services, up to &#8377;75 lakh of receipts where cash receipts are within 5% (&#8377;50 lakh otherwise). It is section 58 of the Income-tax Act, 2025 from tax year 2026-27.",
            "<strong>Actual profit:</strong> receipts minus genuine business expenses, with books of account; a tax audit applies where receipts exceed &#8377;50 lakh without 44ADA.",
            "<strong>Slab rates:</strong> new regime nil to &#8377;4 lakh, then 5%, 10%, 15%, 20%, 25% and 30% above &#8377;24 lakh, with the 87A rebate making income up to &#8377;12 lakh tax-free for residents (marginal relief just above); old regime nil to &#8377;2.5 lakh (&#8377;3 lakh at 60, &#8377;5 lakh at 80), 5%, 20% and 30% above &#8377;10 lakh, with deductions. The &#8377;75,000 standard deduction is for salary only.",
            "<strong>TDS:</strong> Indian clients usually deduct 10% under section 194J on professional fees above &#8377;50,000 a year; it is credited against your tax, and any excess is refunded when you file.",
            "<strong>Advance tax:</strong> if tax after TDS is &#8377;10,000 or more, pay it in advance; under 44ADA the whole amount is due by 15 March, otherwise in instalments by 15 June, 15 September, 15 December and 15 March.",
            "<strong>GST:</strong> registration is needed once aggregate turnover crosses &#8377;20 lakh (&#8377;10 lakh in special category states); export receipts count, and exports go out zero-rated under a LUT.")
         + '<p>Read more: <a href="freelancer-consultant-tax-india-2026-complete.html">freelancer and consultant tax guide</a> &middot; <a href="best-ca-section-44ad-44ada-presumptive-scheme-india.html">sections 44AD and 44ADA</a> &middot; <a href="advance-tax-calculator-fy-2026-27-15-december-instalment.html">advance tax calculator</a> &middot; <a href="new-vs-old-tax-regime-calculator.html">new vs old regime calculator</a> &middot; <a href="gst-on-export-of-services-lut-without-lut-invoice-format-refund-freelancer-startup-2026.html">GST on export of services</a> &middot; <a href="youtube-instagram-influencer-tax-india-2026.html">YouTuber and influencer tax</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act, 1961 (section 44ADA, section 87A, sections 208-211) and Income-tax Act, 2025 (section 58, section 156); Income Tax Department, benefits for small businesses and professionals; Budget 2026 (no slab changes); CGST Act, section 22. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How is income tax calculated for freelancers in India?", "Profit is worked out either under section 44ADA (50% of gross receipts, no books) or as receipts minus expenses, other income is added, and tax is charged at new-regime or old-regime slab rates, less the 87A rebate for residents, plus 4% cess."),
          ("Is there a tax calculator for freelancers in India?", "Yes. The calculator on this page estimates a resident freelancer's tax for 2026-27 under section 44ADA or actual profit, in either regime, with the 87A rebate, TDS and advance tax dates."),
          ("How much can a freelancer earn tax-free in India?", "Under the new regime, taxable income up to Rs 12 lakh is tax-free for residents because of the 87A rebate. With section 44ADA at 50%, that means gross receipts up to about Rs 24 lakh if there is no other income."),
          ("What is the limit for section 44ADA in 2026-27?", "Rs 75 lakh of gross receipts where cash receipts are within 5% of the total, and Rs 50 lakh otherwise."),
          ("Do freelancers need to pay advance tax?", "Yes, if tax after TDS is Rs 10,000 or more. Under section 44ADA the full amount is due by 15 March; otherwise it is paid in four instalments by 15 June, 15 September, 15 December and 15 March."),
          ("Which ITR does a freelancer file?", "ITR-4 for resident individuals using section 44ADA (within its conditions), and ITR-3 for those declaring actual profit or with income that ITR-4 does not cover."),
          ("Can BQP handle my freelance tax?", "Yes. " + CONTACT)],
    related=[("freelancer-consultant-tax-india-2026-complete.html", "Freelancer and consultant tax guide"),
             ("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "Sections 44AD and 44ADA"),
             ("advance-tax-calculator-fy-2026-27-15-december-instalment.html", "Advance tax calculator")],
    cta_h="Want your freelance tax worked out exactly?", cta_b=CONTACT,
    keywords="tax calculator for freelancers in india, freelancer tax calculator, income tax for freelancers in india, 44ada calculator, freelancer tax 2026-27, presumptive tax calculator, freelancer advance tax",
    desc="Free freelancer tax calculator for India 2026-27: profit under section 44ADA (50%, up to Rs 75 lakh) or actual expenses, new vs old regime, 87A rebate to Rs 12 lakh, cess, TDS refund and advance tax dates.",
    howto={"name": "How to estimate a freelancer's income tax in India", "description": "Using the calculator.", "steps": [
        {"name": "Enter receipts", "text": "Gross fees for the year from all clients and platforms."},
        {"name": "Choose the method", "text": "Section 44ADA (50% profit) or actual profit."},
        {"name": "Pick the regime", "text": "New (default) or old with deductions."},
        {"name": "Enter TDS", "text": "From Form 26AS / AIS to see the refund or tax due."},
        {"name": "Plan advance tax", "text": "Pay by 15 March under 44ADA, or in four instalments."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JF complete")
