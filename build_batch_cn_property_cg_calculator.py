# -*- coding: utf-8 -*-
"""Batch CN (15 Nov 2026): property capital gains calculator for residents, NRIs and inherited property: 12.5% without
indexation vs 20% with indexation (residents, land or buildings acquired before 23 July 2024), 1 April 2001 value for
older property, sections 54 (up to INR 10 crore) and 54EC (up to INR 50 lakh). CII up to 384 for 2026-27 (CBDT
Notification 85/2026, 15 July 2026; 376 for 2025-26). Logic: tools/property-capital-gains-logic.js
(node tools/property-capital-gains-logic.test.js, 8 tests)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN

UPDATED = "Last updated: 15 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


LOGIC = open("tools/property-capital-gains-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { propertyCapitalGains: propertyCapitalGains, CII: CII, fyOf: fyOf };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n")
SEL = "width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;font:inherit"


def fld(fid, label, hint, val, typ="number"):
    extra = ' min="0" step="any" inputmode="decimal"' if typ == "number" else ""
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="{typ}" value="{val}"{extra}/></div>')


INPUTS = ('<div class="field"><label for="gRes">Seller</label><select id="gRes" style="' + SEL + '">'
          '<option value="r">Resident individual or HUF</option><option value="n">NRI (non-resident)</option></select></div>'
          + fld("gBuy", "Purchase date", "For inherited or gifted property, the previous owner's purchase date.", "2010-06-01", "date")
          + fld("gCost", "Purchase cost (INR)", "If bought before 1 April 2001, the value on that date (not above the stamp duty value).", "4000000")
          + fld("gSale", "Sale date", "Up to 31 March 2027.", "2026-09-01", "date")
          + fld("gPrice", "Sale price (INR)", "Full consideration.", "16000000")
          + fld("gExp", "Transfer expenses (INR)", "Brokerage, legal fees.", "0")
          + fld("g54", "Reinvested in a new house, section 54 (INR)", "Optional; capped at INR 10 crore.", "0")
          + fld("g54ec", "Capital gain bonds, section 54EC (INR)", "Optional; capped at INR 50 lakh.", "0"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  function show(){
    var r=propertyCapitalGains({resident:$("gRes").value==="r",buyDate:$("gBuy").value,saleDate:$("gSale").value,cost:$("gCost").value,
      price:$("gPrice").value,expenses:$("gExp").value,reinvest54:$("g54").value,bonds54EC:$("g54ec").value});
    var out=$("gOut"), list=$("gList");
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    if(!r.longTerm){ out.textContent="Short-term: taxed at slab rates";
      list.innerHTML="<li>Held 24 months or less, so the gain of <strong>"+inr(r.gainNoIndex)+"</strong> is added to your income and taxed at slab rates.</li><li>For inherited property, use the previous owner's purchase date; most inherited property is long-term.</li>"; return; }
    var items=[];
    items.push("Without indexation: gain <strong>"+inr(r.gainNoIndex)+"</strong>, tax at 12.5% plus 4% cess <strong>"+inr(r.taxA)+"</strong>.");
    if(r.canIndex){
      items.push("With indexation: indexed cost "+inr(r.indexedCost)+", gain <strong>"+inr(r.gainIndexed)+"</strong>, tax at 20% plus 4% cess <strong>"+inr(r.taxB)+"</strong>.");
      out.textContent=(r.best==="indexed"? "Choose 20% with indexation: ":"Choose 12.5% without indexation: ")+inr(Math.min(r.taxA,r.taxB));
    } else {
      out.textContent="Tax: "+inr(r.taxA)+" at 12.5%";
      items.push($("gRes").value==="n" ? "NRIs pay 12.5% without indexation; the buyer also deducts TDS on the price unless you get a lower deduction certificate." : "No indexation option: the property was acquired on or after 23 July 2024, or the seller is non-resident.");
    }
    if(r.pre2001) items.push("Bought before 1 April 2001: the value on that date is used as cost and indexed from 2001-02.");
    if(r.exemptApplied>0) items.push("Exemptions applied (sections 54 and 54EC, within their limits): "+inr(r.exemptApplied)+".");
    items.push("Estimate only: before surcharge and any unused basic exemption; one property and no other gains. Check the 20% option for your inheritance date with a CA.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["gRes","gBuy","gCost","gSale","gPrice","gExp","g54","g54ec"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "property-capital-gains-tax-calculator-india-indexation-12-5-vs-20-inherited-nri-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Property Capital Gains Tax Calculator India (12.5% vs 20% with indexation)",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Compares 12.5% without indexation with 20% with indexation on the sale of land or buildings in India, including inherited property and the 1 April 2001 value, with CII up to 384 for 2026-27.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your property</h2><p class="sub">Use dates and amounts from the deeds.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="gOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="gList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa("Hi Durgesh, I am selling a property in India. Can you check my capital gains working?")}" target="_blank" rel="noopener">Get your working checked by CA Durgesh Chavda &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the purchase and sale deeds (or the previous owner's for inherited property) and your residence status. "
           "We reply the same working day with the tax working and ways to reduce it.")
CII_ROWS = "".join(f"<tr><td>{y}-{str(y+1)[2:]}</td><td>{v}</td></tr>" for y, v in [(2001, 100), (2005, 117), (2010, 167), (2015, 254), (2020, 301), (2022, 331), (2023, 348), (2024, 363), (2025, 376), (2026, 384)])

PAGES = [dict(
    slug=SLUG,
    title="Property Capital Gains Tax Calculator India (2026): 12.5% vs 20% With Indexation, Inherited Property, Sale Within 2 Years, 1 April 2001 Value and NRIs",
    em="see which rate costs you less.",
    kicker="/ Calculator &middot; Property &middot; Capital gains &middot; Updated 2026-11-15",
    lead=("Long-term gains on land and buildings sold in India are taxed at <strong>12.5% without indexation</strong>. A <strong>resident individual or HUF</strong> can instead choose <strong>20% with indexation</strong> for property acquired before 23 July 2024, and pays whichever is lower; <strong>NRIs pay 12.5%</strong>. "
          "For inherited property, use the <strong>previous owner's purchase date and cost</strong>; for property bought before 1 April 2001, use its value on that date. "
          "The calculator uses the cost inflation index up to <strong>384 for 2026-27</strong> (CBDT Notification 85/2026, 15 July 2026) and applies section 54 and 54EC reinvestment if you enter it."),
    sections=[
        ("/ Calculator", "12.5% vs 20% with indexation.", CALC),
        ("/ The rules behind it", "And the index values.",
         ul("<strong>Long-term:</strong> held more than 24 months; for inherited or gifted property, the previous owner's holding counts.",
            "<strong>Rates:</strong> 12.5% without indexation; resident individuals and HUFs may opt for 20% with indexation on land or buildings acquired before 23 July 2024; plus 4% cess and any surcharge.",
            "<strong>Indexed cost:</strong> cost x CII of the year of sale / CII of the year of purchase (2001-02 for property acquired earlier).",
            "<strong>1 April 2001:</strong> the fair market value on that date, not above the stamp duty value, can be used as cost.",
            "<strong>Reliefs:</strong> section 54 (new residential house, up to INR 10 crore) and section 54EC (specified bonds within six months, up to INR 50 lakh).")
         + f"<table><thead><tr><th>Financial year</th><th>Cost inflation index</th></tr></thead><tbody>{CII_ROWS}</tbody></table>"
         + '<p>Related: <a href="inherited-property-india-rules-rights-sale-tax-nri-resident-2026.html">inherited property in India</a> &middot; <a href="nri-property-tds-ldc-calculator.html">NRI property TDS calculator</a> &middot; <a href="nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html">lower TDS certificate (Form 128)</a> &middot; <a href="best-ca-nri-property-sale-section-54-reinvestment.html">section 54 reinvestment</a>.</p>'
         + f'<p><strong>Sources:</strong> Finance (No. 2) Act, 2024 (rates from 23 July 2024 and the indexation option); Income-tax Act provisions on cost of acquisition for inherited property and the 1 April 2001 value; CBDT Notification No. 85/2026 dated 15 July 2026 (CII 384 for 2026-27) and No. 70/2025 (376 for 2025-26); sections 54 and 54EC. <em>{UPDATED}</em> Estimates only, not advice for your situation.</p>'),
    ],
    faqs=[("How is capital gains tax on property calculated in India?", "Long-term gains (held over 24 months) are taxed at 12.5% without indexation. Resident individuals and HUFs can choose 20% with indexation for land or buildings acquired before 23 July 2024, paying whichever is lower. Cess and any surcharge are added."),
        ("How is tax calculated if I sell a house within 2 years of buying it?", "A house or land held for 24 months or less is a short-term capital asset, so the gain - sale price (or the stamp duty value, if that is more than 10% higher) minus purchase cost, improvement cost and transfer expenses such as brokerage - is added to your other income and taxed at your normal slab rate, with no indexation. The reinvestment exemptions under sections 54, 54EC and 54F apply only to long-term gains, so they cannot reduce a short-term gain; a short-term loss can be set off against other capital gains and carried forward for eight years. For an NRI seller the buyer deducts TDS on the price at non-resident rates (30% plus surcharge and cess on short-term gains) unless a lower deduction certificate is obtained, and any excess comes back through the return. Selling within five years of possession also reverses home loan principal claimed under 80C. WhatsApp +91 78018 87130 with the purchase and sale deeds, dates and costs, or book a call."),
          ("What is the cost inflation index for 2026-27?", "384, notified by CBDT Notification No. 85/2026 dated 15 July 2026. It was 376 for 2025-26."),
          ("How do I calculate capital gains on inherited property?", "Use the previous owner's purchase cost and date (or the 1 April 2001 value for older property). The holding period includes the previous owner's, so it is usually long-term."),
          ("Can NRIs use indexation?", "No. NRIs pay 12.5% without indexation on long-term property gains; the 20% with-indexation option is for resident individuals and HUFs."),
          ("Does the calculator include surcharge?", "No. It shows tax plus 4% cess before surcharge and any unused basic exemption, which depend on your total income."),
          ("Can BQP check my working?", "Yes. " + CONTACT)],
    related=[("inherited-property-india-rules-rights-sale-tax-nri-resident-2026.html", "Inherited property in India"), ("nri-property-tds-ldc-calculator.html", "NRI property TDS calculator"),
             ("best-ca-nri-property-sale-section-54-reinvestment.html", "Section 54 reinvestment")],
    cta_h="Selling property in India?", cta_b=CONTACT,
    keywords="property capital gains tax calculator India, capital gains calculator indexation 2026, 12.5% vs 20% indexation calculator, inherited property capital gains calculator, cost inflation index 2026-27 384, CII 2026-27, NRI property capital gains calculator, 1 April 2001 fair market value",
    desc="Free calculator for capital gains on land and buildings in India (2026): 12.5% without indexation vs 20% with indexation for residents (property acquired before 23 July 2024), inherited property, 1 April 2001 value, NRIs, sections 54 and 54EC, CII 384 for 2026-27.",
    howto={"name": "How to calculate capital gains on property in India", "description": "Steps for residents, NRIs and heirs.", "steps": [
        {"name": "Find the dates and cost", "text": "Use your purchase date and cost, or the previous owner's for inherited property, or the 1 April 2001 value for older property."},
        {"name": "Compute both options", "text": "12.5% on the plain gain; for residents with pre-23 July 2024 property, 20% on the indexed gain."},
        {"name": "Apply reliefs", "text": "Reduce the gain by section 54 or 54EC reinvestment within the limits and time allowed."},
        {"name": "Pay the lower tax", "text": "Residents choose the lower; NRIs pay 12.5% and can get a lower TDS certificate for the buyer."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch CN complete")
