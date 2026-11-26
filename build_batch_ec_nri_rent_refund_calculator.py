# -*- coding: utf-8 -*-
"""Batch EC (20 Nov 2026): NRI rental income TDS refund calculator - tenant TDS on gross rent (30% plus surcharge and
cess) vs tax on house-property income (rent less municipal taxes, 30% standard deduction, home-loan interest; new-regime
slabs FY 2025-26, no 87A for NRIs; house-property loss not set off under the new regime). Pushes belated / revised returns
by 31 December 2026 and lower deduction certificates. Logic: tools/nri-rent-refund-logic.js
(node tools/nri-rent-refund-logic.test.js, 5 tests)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/nri-rent-refund-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { nriRentRefund: nriRentRefund, rentSlabTax: rentSlabTax };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")


def fld(fid, label, hint, val):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="number" value="{val}" min="0" step="any" inputmode="decimal"/></div>')


INPUTS = (fld("rRent", "Annual rent received (INR)", "Gross rent for FY 2025-26.", "600000")
          + fld("rMuni", "Municipal / property tax paid (INR)", "Paid by you in the year.", "0")
          + fld("rInt", "Home-loan interest on this property (INR)", "0 if no loan.", "0")
          + fld("rOther", "Other Indian income (INR)", "NRO interest, gains at slab rates etc.; 0 if none.", "0"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=nriRentRefund({rent:$("rRent").value,municipal:$("rMuni").value,interest:$("rInt").value,other:$("rOther").value});
    var out=$("rOut"), list=$("rList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    out.textContent="About "+inr(r.refund)+" possible refund";
    var items=["Tenant TDS at 30% plus surcharge and cess on gross rent: about <strong>"+inr(r.tds)+"</strong>.",
      "Taxable house-property income after municipal tax, the 30% standard deduction and loan interest: <strong>"+inr(r.houseProperty)+"</strong>.",
      "Tax on it at FY 2025-26 slab rates (new regime, no 87A rebate for NRIs): <strong>"+inr(r.tax)+"</strong>.",
      "The difference can be claimed in a belated or revised return by <strong>31 December 2026</strong>; a lower deduction certificate cuts future TDS."];
    if(r.highIncome) items.push("Total income is above INR 50 lakh, so surcharge may apply; get it computed on your figures.");
    items.push("Estimate only: new regime assumed; a house-property loss is not set off against other income under it.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["rRent","rMuni","rInt","rOther"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "nri-rental-income-tds-refund-calculator-31-2-percent-vs-actual-tax-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "NRI Rental Income TDS Refund Calculator",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Compares tenant TDS on gross rent with tax on an NRI landlord's house-property income to estimate the refund.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I am an NRI landlord and want to claim my rent TDS refund before 31 December.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your rental income</h2><p class="sub">Use FY 2025-26 figures from your tenant&rsquo;s TDS certificates.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="rOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="rList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Claim it with us before 31 December &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the rent received, TDS certificates (Form 16A), Form 26AS / AIS, municipal tax and loan interest. "
           "We reply the same working day, file before 31 December 2026 and apply for a lower TDS certificate, with a fixed-scope quote.")

PAGES = [dict(
    slug=SLUG,
    title="TDS on Rent Paid to an NRI Landlord (2026): 31.2% Rate, Section 393 (Old 195), Tenant TAN and Form 144 (Old 27Q), and a Refund Calculator",
    em="most NRI landlords overpay; see how much you can claim back.",
    kicker="/ Calculator &middot; NRIs &middot; Rental income &middot; Updated 2026-11-20",
    lead=("A tenant paying rent to an NRI landlord deducts TDS at <strong>30% plus surcharge and cess (31.2% for most)</strong> on the <strong>gross rent</strong>. Tax, however, is due only on house-property income: rent less municipal taxes, less a <strong>30% standard deduction</strong>, less interest on a home loan for the property. That income is taxed at <strong>slab rates</strong>, and under the new regime for FY 2025-26 the first INR 4 lakh is nil. The gap is often most of the TDS. "
          "You get it back only by filing a return. For FY 2025-26 the last date is <strong>31 December 2026</strong> for a belated or revised return. A <strong>lower deduction certificate</strong> stops the over-deduction on future rent. Enter your figures to estimate the refund."),
    sections=[
        ("/ Calculator", "Tenant TDS vs your actual tax.", CALC
         + call_box("my rent TDS refund", ["Your exact refund on FY 2025-26 figures",
                                            "Filing the belated or revised return before 31 December 2026",
                                            "A lower deduction certificate so tenants deduct less from now on",
                                            "Tenant TAN, Form 16A and Form 26AS mismatches",
                                            "Repatriating rent from your NRO account"],
                    "rent agreement, Form 16A certificates, Form 26AS / AIS, municipal tax receipts and loan interest certificate.")),
        ("/ How it works", "The rules behind the numbers.",
         ul("<strong>Tenant TDS:</strong> 30% plus surcharge and cess on rent paid to a non-resident, deducted from the gross rent.",
            "<strong>Your taxable income:</strong> annual rent less municipal taxes paid, less a 30% standard deduction, less home-loan interest on the let-out property.",
            "<strong>Slab tax:</strong> FY 2025-26 new-regime slabs with 4% cess; NRIs do not get the section 87A rebate; under the new regime a house-property loss cannot reduce other income.",
            "<strong>Treaty:</strong> rental income from Indian property is taxable in India under tax treaties; your country of residence may also tax it and give credit.",
            "<strong>Lower deduction certificate:</strong> apply to the Income Tax Department so the tenant deducts at the certified rate.")
         + '<p>Next steps: <a href="nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html">TDS on rent to NRIs</a> &middot; <a href="nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html">NRI year-end checklist</a> &middot; <a href="nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html">NRO interest refund calculator</a> &middot; <a href="repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html">repatriating rent</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act provisions on income from house property (30% standard deduction, interest), TDS on payments to non-residents and FY 2025-26 slab rates; India&rsquo;s tax treaties (immovable property article). <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How much TDS does a tenant deduct on rent paid to an NRI?", "30% plus surcharge and cess on the gross rent, which is 31.2% for most NRIs, unless the NRI has a lower deduction certificate."),
        ("What does a tenant have to do when the landlord is an NRI?", "The tenant must deduct tax under section 393 of the Income-tax Act, 2025 (old section 195) from every rent payment, whatever the amount - the Rs 50,000 a month limit for resident landlords does not apply. The tenant needs a TAN, deposits the tax by challan, files the quarterly TDS return in Form 144 (old 27Q) and gives the landlord a TDS certificate in Form 131 (old 16A). The rate is 30% plus cess (31.2%, with surcharge on very large rents) unless the landlord gives the tenant a lower or nil TDS certificate in Form 128."),
        ("What should an NRI landlord send to cut TDS on rent or claim it back?", "WhatsApp us the rent agreement, the yearly rent and the municipal tax and loan interest you pay on the property, your PAN and Form 168 (old 26AS), and your country of residence. We work out the tax on your actual rental income, apply for a Form 128 lower TDS certificate if it is worth it, and file your ITR to claim back any excess TDS."),
          ("How is an NRI's rental income taxed?", "Rent less municipal taxes, less a 30% standard deduction and home-loan interest, taxed at slab rates; NRIs do not get the section 87A rebate."),
          ("Can an NRI get a refund of TDS on rent?", "Yes, by filing an Indian return. For FY 2025-26 a belated return can be filed until 31 December 2026 and a filed return revised until 31 March 2027 (fee after 31 December); an updated return cannot claim refunds."),
          ("How can an NRI landlord reduce TDS on rent?", "Apply for a lower deduction certificate so the tenant deducts at the rate the Income Tax Department certifies."),
          ("Does the tax treaty reduce tax on Indian rent?", "No. Rental income from Indian property is taxable in India; the country of residence may tax it too and give credit for Indian tax."),
          ("Can BQP claim my refund and certificate?", "Yes. " + CONTACT)],
    related=[("nri-rental-income-india-tenant-tds-31-2-percent-tan-form-144-2026.html", "TDS on rent to NRIs"),
             ("nri-nro-interest-tds-refund-calculator-treaty-rate-by-country-2026.html", "NRO interest refund calculator"),
             ("nri-year-end-tax-checklist-before-31-december-2026-refund-belated-itr-fast-ds-residency.html", "NRI year-end checklist")],
    cta_h="Rent from Indian property while living abroad?", cta_b=CONTACT,
    keywords="NRI rental income TDS refund calculator, TDS on rent paid to NRI 31.2 percent, NRI landlord tax India, NRI rent refund 31 December 2026, lower deduction certificate rent NRI, house property income NRI 30 percent deduction",
    desc="Calculator for NRI landlords: tenant TDS of 31.2% on gross rent vs tax on house-property income (30% standard deduction, municipal tax, loan interest, FY 2025-26 slabs, no 87A); estimate the refund, claim it by 31 December 2026 and cut future TDS with a lower deduction certificate.",
    howto={"name": "How an NRI landlord claims back excess TDS on rent", "description": "Estimate, file and reduce future TDS.", "steps": [
        {"name": "Enter your figures", "text": "Rent, municipal tax, loan interest and other Indian income."},
        {"name": "Compare TDS with tax", "text": "See tenant TDS against tax on your actual income."},
        {"name": "File by 31 December 2026", "text": "Belated or revised ITR-2 for FY 2025-26 to claim the refund."},
        {"name": "Get a lower deduction certificate", "text": "So tenants deduct less from the next payment."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EC complete")
