# -*- coding: utf-8 -*-
"""Batch FD (21 Nov 2026): FEMA late submission fee (LSF) calculator - FC-GPR, FC-TRS, Form DI, Form FC, ECB 2, FLA, APR.
Demand: sweep 21 Nov 2026 (ac38), all 7 markets: "late submission fee under fema", "fc gpr filing due date",
"fc trs due date". The site stated the formula on compounding pages but had no calculator.
Facts (checked 21 Nov 2026):
- RBI A.P. (DIR Series) Circular No. 16 dated 30 September 2022 (RBI/2022-23/122), late submission fee for reporting
  delays under FEMA: returns that capture flows (FC-GPR, FC-TRS, Form ESOP, LLP(I), LLP(II), CN, DI, InVi, ODI Part I
  and III / Form FC, ECB, ECB 2): INR 7,500 + (0.025% x A x n); returns that do not capture flows (FLA, APR / ODI Part II,
  FC-GPR(B), OPI, evidence of investment): INR 7,500. n = years of delay rounded up to the nearest month, to two
  decimals; A = amount involved in the delayed reporting; maximum 100% of A; rounded up to the nearest hundred; payable
  within 30 days of the advice, else the advice lapses and a fresh application date is the reference date; LSF available
  up to three years from the due date, after which compounding applies.
- A.P. (DIR Series) Circular No. 25 dated 30 March 2026 on ECB returns: Form ECB 1 treated as a return without flows
  (flat fee) from 1 April 2026 (FemaOnline index; practitioner summaries). Stated on the page as reported.
Logic: tools/fema-lsf-logic.js (node tools/fema-lsf-logic.test.js, 9 tests)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, table, call_box

A.UPDATED = "Last updated: 21 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/fema-lsf-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { femaLsf: femaLsf, LSF_FORMS: LSF_FORMS };', "")
assert "module.exports" not in LOGIC
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed input[type=date]{width:100%}\n")

FORMS = [("fcgpr", "FC-GPR (shares issued to a non-resident)"), ("fctrs", "FC-TRS (transfer of shares)"), ("di", "Form DI (downstream investment)"),
         ("cn", "Form CN (convertible notes)"), ("esop", "Form ESOP"), ("llp", "Form LLP(I) or LLP(II)"), ("invi", "Form InVi"),
         ("fc", "Form FC (overseas investment or disinvestment)"), ("ecb2", "Form ECB 2"), ("fla", "FLA return (flat fee)"),
         ("apr", "Annual Performance Report, overseas investment (flat fee)"), ("opi", "Form OPI (flat fee)"), ("ecb1", "Form ECB 1 (flat fee)")]


def sel(fid, label, hint, opts):
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label><select id="{fid}">'
            + "".join(f'<option value="{v}">{l}</option>' for v, l in opts) + "</select></div>")


def fld(fid, label, hint, val, typ="number"):
    extra = ' min="0" step="any" inputmode="decimal"' if typ == "number" else ""
    return (f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>'
            f'<input id="{fid}" type="{typ}" value="{val}"{extra}/></div>')


INPUTS = (sel("lForm", "Which filing is late?", "Flat-fee returns ignore the amount.", FORMS)
          + fld("lAmount", "Amount reported in the form (INR)", "For FC-GPR, the amount received for the shares.", "10000000")
          + fld("lDue", "Due date", "FC-GPR: 30 days from allotment. FC-TRS: 60 days from transfer or payment.", "2026-06-10", "date")
          + fld("lFiled", "Date you will file", "Today by default.", "2026-11-21", "date"))
JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function inr(n){ return "INR " + Math.round(n).toLocaleString("en-IN"); }
  try { var d=new Date(); $("lFiled").value = d.getFullYear()+"-"+("0"+(d.getMonth()+1)).slice(-2)+"-"+("0"+d.getDate()).slice(-2); } catch(e){}
  function show(){
    var r=femaLsf({form:$("lForm").value,amount:$("lAmount").value,due:$("lDue").value,filed:$("lFiled").value});
    var out=$("lOut"), list=$("lList"), items=[];
    if(!r.ok){ out.textContent="Check inputs"; list.innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join(""); return; }
    if(!r.late){ out.textContent="Not late: no fee"; list.innerHTML="<li>The filing date is on or before the due date.</li>"; return; }
    if(!r.available){
      out.textContent="More than three years late: compounding";
      items.push("The late submission fee is available only for three years from the due date. This filing is about "+r.months+" months late.");
      items.push("Older delays are regularised by a compounding application to the RBI. The amount is set under the RBI&rsquo;s compounding guidelines, not this formula.");
      items.push("Book a call before filing anything: the order of filing and the compounding application matters.");
      list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join(""); return;
    }
    out.textContent="Estimated fee: "+inr(r.fee);
    items.push("Delay: <strong>"+r.months+" month"+(r.months>1?"s":"")+"</strong> (part months count as full), so n = "+r.n.toFixed(2)+" years.");
    if(r.flow){
      items.push("INR 7,500 + 0.025% &times; "+inr(r.amount)+" &times; "+r.n.toFixed(2)+" = "+inr(7500+r.variable)+(r.capped?", limited to 100% of the amount":"")+", rounded up to the nearest INR 100: <strong>"+inr(r.fee)+"</strong>.");
    } else {
      items.push("This return does not report a flow of money, so the fee is a flat <strong>INR 7,500</strong>.");
    }
    items.push("The fee is per form. Three late forms mean three fees.");
    items.push("Pay within 30 days of the fee advice. If it lapses, the delay is counted up to the new application date.");
    items.push("Estimate only: the bank or the RBI works out the final figure, and a wrong valuation or missing approval is not cured by the fee.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  ["lForm","lAmount","lDue","lFiled"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  show();
})();'''
SLUG = "fema-late-submission-fee-calculator-fc-gpr-fc-trs-form-di-fla-apr-lsf-rbi-2026"
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "FEMA Late Submission Fee Calculator (India)",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Estimates the RBI late submission fee for a delayed FEMA filing such as FC-GPR, FC-TRS, Form DI, Form FC, ECB 2, FLA or APR: INR 7,500 plus 0.025% of the amount per year of delay, or a flat INR 7,500.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, we have a late FEMA filing (FC-GPR / FC-TRS / FLA) and need help to regularise it.")
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>The late filing</h2><p class="sub">One form at a time. The fee is charged per form.</p>{INPUTS}</div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="lOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="lList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="https://topmate.io/cadurgesh_chavda/741484" target="_blank" rel="noopener">Book a call to regularise it &rarr;</a> &middot; <a href="{wa}" target="_blank" rel="noopener">WhatsApp</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Book a call at book-a-call.html, WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the form that is late, "
           "the transaction date and amount, the investor's country and your bank.")

PAGES = [dict(
    slug=SLUG,
    title="FEMA Late Submission Fee Calculator (2026): FC-GPR, FC-TRS, Form DI, Form FC, ECB 2, FLA and APR - INR 7,500 Plus 0.025% a Year",
    em="what a late RBI filing costs, and when it becomes compounding.",
    kicker="/ Calculator &middot; FEMA &middot; Foreign investment &middot; Updated 2026-11-21",
    lead=("<strong>A late FEMA filing can usually be regularised by paying a late submission fee, if it is filed within three years of the due date.</strong> "
          "For forms that report money moving, such as <strong>FC-GPR, FC-TRS, Form DI, Form FC and ECB 2</strong>, the fee is <strong>INR 7,500 plus 0.025% of the amount for each year of delay</strong>. "
          "For returns that report no flow, such as the <strong>FLA return and the Annual Performance Report</strong>, it is a flat <strong>INR 7,500</strong>. "
          "The delay is counted in months, with part months rounded up. The fee cannot exceed the amount reported and is rounded up to the nearest INR 100. "
          "<strong>After three years the fee route closes</strong> and the delay has to be compounded with the RBI. "
          "The fee is small next to what a pending filing blocks: the next funding round, a share transfer, an exit or a remittance to the parent. Enter the form, amount and dates below."),
    sections=[
        ("/ Calculator", "Fee for one late form.", CALC
         + call_box("A late FEMA filing in our Indian company", ["Which filings are late and which are simply missing",
                                                                "Whether each one fits the fee route or needs compounding",
                                                                "Filing the forms on the RBI portal with the bank",
                                                                "Valuation, KYC and board papers the bank will ask for",
                                                                "Clearing it before a funding round, share transfer or exit"],
                    "the forms that are late, transaction dates and amounts, the investor&rsquo;s country and your authorised dealer bank.")),
        ("/ How the fee works", "Formula, limits and due dates.",
         table(["Filing", "Normal due date", "Late fee"], [
             ["FC-GPR (shares issued to a non-resident)", "30 days from allotment", "INR 7,500 + 0.025% &times; amount &times; years"],
             ["FC-TRS (transfer between resident and non-resident)", "60 days from the transfer or payment, whichever is earlier", "INR 7,500 + 0.025% &times; amount &times; years"],
             ["Form DI (downstream investment)", "30 days from allotment", "INR 7,500 + 0.025% &times; amount &times; years"],
             ["Form FC (overseas investment)", "With the remittance, through the bank", "INR 7,500 + 0.025% &times; amount &times; years"],
             ["FLA return", "15 July each year", "INR 7,500 flat"],
             ["Annual Performance Report (overseas investment)", "31 December each year", "INR 7,500 flat"]])
         + ul("<strong>Years of delay:</strong> counted in months, part months rounded up, then divided by 12 to two decimals. Five months and three days is six months, or 0.50 years.",
              "<strong>Ceiling:</strong> the fee cannot be more than the amount reported in the form.",
              "<strong>Per form:</strong> each late form has its own fee.",
              "<strong>Payment:</strong> within 30 days of the fee advice. If it lapses, the delay runs to the date of the fresh application.",
              "<strong>Three years:</strong> beyond three years from the due date the fee route is not available; see <a href=\"fema-compounding-foreign-subsidiary-india.html\">FEMA compounding for foreign-owned companies</a>.",
              "<strong>What the fee does not cure:</strong> shares issued below fair value, a sector that needed approval, or money received in the wrong account. Those are separate contraventions.",
              "<strong>ECB forms:</strong> Form ECB 2 uses the formula. Form ECB 1 is reported to be a flat-fee return from 1 April 2026; confirm with the bank.")
         + '<p>Related: <a href="fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html">FEMA health check for a foreign-owned company</a> &middot; <a href="form-fc-gpr-filing-checklist-india-2026.html">FC-GPR checklist</a> &middot; <a href="form-fc-trs-filing-checklist-india-2026.html">FC-TRS checklist</a> &middot; <a href="fla-return-foreign-liabilities-assets-rbi-india.html">FLA return</a> &middot; <a href="form-odi-apr-annual-performance-report-india-2026.html">Annual Performance Report</a> &middot; <a href="downstream-investment-india-foreign-owned-company-fema-form-di-funding-rules-2026.html">downstream investment and Form DI</a>.</p>'
         f'<p><strong>Sources:</strong> Reserve Bank of India, A.P. (DIR Series) Circular No. 16 dated 30 September 2022, &ldquo;Late Submission Fee for reporting delays under FEMA&rdquo;; RBI Master Direction on Reporting under FEMA; FEMA (Mode of Payment and Reporting of Non-Debt Instruments) Regulations, 2019; FEMA (Overseas Investment) Regulations, 2022; A.P. (DIR Series) Circular No. 25 dated 30 March 2026 on ECB returns, as reported. <em>{UPDATED}</em> Estimates only; the bank or the RBI sets the final fee.</p>'),
    ],
    faqs=[("What is the late submission fee under FEMA?", "For returns that report a flow of money, such as FC-GPR, FC-TRS, Form DI, Form FC and ECB 2, it is INR 7,500 plus 0.025% of the amount for each year of delay. For returns that report no flow, such as the FLA return and the Annual Performance Report, it is a flat INR 7,500."),
          ("How is the delay counted for the FEMA late submission fee?", "In years, with the delay rounded up to the nearest month and expressed to two decimals. The fee is capped at 100% of the amount reported and rounded up to the nearest INR 100."),
          ("What is the late fee for FC-GPR?", "INR 7,500 plus 0.025% of the amount received for the shares for each year of delay. For INR 1 crore filed five months late, the fee is about INR 8,600."),
          ("What if a FEMA filing is more than three years late?", "The late submission fee is available only for three years from the due date. After that the delay must be compounded through an application to the RBI."),
          ("How soon must the late submission fee be paid?", "Within 30 days of the fee advice. If it is not paid in time the advice lapses, and the delay is then counted up to the date of the fresh application."),
          ("Can BQP regularise our late FEMA filings?", "Yes. " + CONTACT)],
    related=[("fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html", "FEMA health check for a foreign-owned company"),
             ("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding for foreign-owned companies"),
             ("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR filing checklist")],
    cta_h="Late with an RBI filing?", cta_b=CONTACT,
    keywords="late submission fee under FEMA, FEMA LSF calculator, FC-GPR late fee, FC-TRS late fee, FLA return late fee, LSF 7500 0.025%, FC-GPR filing due date, FC-TRS due date, FEMA compounding three years",
    desc="Calculator: RBI late submission fee for a delayed FEMA filing. FC-GPR, FC-TRS, Form DI, Form FC, ECB 2: INR 7,500 plus 0.025% of the amount per year of delay; FLA and APR: flat INR 7,500. Available for three years from the due date, then compounding.",
    howto={"name": "How to regularise a late FEMA filing", "description": "Fee route within three years.", "steps": [
        {"name": "List what is late", "text": "Each form, its transaction date, amount and due date."},
        {"name": "Check the three-year window", "text": "Within three years: late submission fee. Beyond: compounding."},
        {"name": "File the form", "text": "On the RBI portal through the authorised dealer bank, with valuation and KYC."},
        {"name": "Pay the fee", "text": "Within 30 days of the fee advice."},
        {"name": "Keep the acknowledgment", "text": "Investors and buyers ask for it in due diligence."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FD complete")
