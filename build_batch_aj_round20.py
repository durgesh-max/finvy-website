# -*- coding: utf-8 -*-
"""Batch AJ: Round 20 - four calculators for what people are searching (gratuity, advance tax, belated ITR fee, FAST-DS)."""
import json
import re
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."

_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += "\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .result-row .val{white-space:nowrap}\n"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


def field(fid, label, hint, kind="number", value="", options=None, step="1000"):
    if options:
        opts = "".join(f'<option value="{v}">{t}</option>' for v, t in options)
        ctrl = f'<select id="{fid}">{opts}</select>'
    else:
        ctrl = f'<input id="{fid}" type="{kind}" min="0" step="{step}" value="{value}" />'
    return f'<div class="field"><label>{label} <span class="hint">{hint}</span></label>{ctrl}</div>'


def result_rows(rows):
    return "".join(f'<div class="result-row"><span class="lbl">{l}</span><span class="val" id="{i}">INR 0</span></div>' for i, l in rows)


def calc_block(slug, name, desc, inputs_html, main_id, main_label, rows, js):
    app = {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "url": f"{DOMAIN}/{slug}.html",
           "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "description": desc,
           "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
           "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"},
           "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN}}
    return (f"<style>{CALC_CSS}</style>"
            f'<script type="application/ld+json">{json.dumps(app, separators=(",", ":"), ensure_ascii=False)}</script>'
            f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Inputs</h2><p class="sub">All amounts in INR.</p>{inputs_html}</div>'
            f'<div class="result-card"><div class="rlabel">{main_label}</div><div class="rvalue red" id="{main_id}">INR 0</div><div class="rhint" id="{main_id}Hint"></div>'
            f'{result_rows(rows)}</div></div></div>'
            f"<script>\n{js}\n</script>")


FMT = 'function fmt(n){n=Math.round(n||0);if(n<0)n=0;return "INR "+n.toLocaleString("en-IN");}\nfunction v(id){var e=document.getElementById(id);return e.tagName==="SELECT"?e.value:(parseFloat(e.value)||0);}\nfunction set(id,x){document.getElementById(id).textContent=(typeof x==="number")?fmt(x):x;}\nfunction wire(ids,f){ids.forEach(function(id){var e=document.getElementById(id);e.addEventListener("input",f);e.addEventListener("change",f);});f();}'

# ------------------------------------------------------------------ gratuity
GRAT_JS = FMT + r'''
function gratuity(o){
  var wages=Math.max(o.basicDa, 0.5*o.total);
  var totalMonths=o.years*12+o.months;
  var eligible = o.type==="fixed" ? totalMonths>=12 : (totalMonths>=60 || o.exitReason==="death");
  var serviceYears = o.type==="fixed" ? totalMonths/12 : o.years + (o.months>6?1:0);
  var amt = eligible ? wages*15/26*serviceYears : 0;
  var exempt = o.employer==="govt" ? amt : Math.min(amt, 2000000);
  return {wages:wages, uplift:Math.max(0,wages-o.basicDa), serviceYears:serviceYears, eligible:eligible, amount:amt, exempt:exempt, taxable:Math.max(0,amt-exempt)};
}
function calc(){
  var r=gratuity({type:v("gType"),exitReason:v("gExit"),employer:v("gEmployer"),basicDa:v("gBasic"),total:v("gTotal"),years:v("gYears"),months:v("gMonths")});
  set("gAmount",r.amount); set("gWages",r.wages); set("gUplift",r.uplift); set("gService",r.serviceYears.toFixed(2)+" years"); set("gExempt",r.exempt); set("gTaxable",r.taxable);
  set("gAmountHint", r.eligible ? "15/26 x monthly wages x years of service" : (v("gType")==="fixed" ? "Not yet eligible: fixed-term employees need 1 year of service" : "Not yet eligible: permanent employees need 5 years (except on death or disablement)"));
}
wire(["gType","gExit","gEmployer","gBasic","gTotal","gYears","gMonths"],calc);'''

GRAT_INPUTS = (field("gType", "Employment type", "Fixed-term employees qualify after 1 year; permanent after 5.", options=[("permanent", "Permanent"), ("fixed", "Fixed-term contract")])
               + field("gBasic", "Monthly basic pay + DA", "Last drawn.", value="40000")
               + field("gTotal", "Monthly total remuneration", "Gross monthly pay including all allowances.", value="100000")
               + field("gYears", "Completed years of service", "", value="6", step="1")
               + field("gMonths", "Additional months", "0-11.", value="7", step="1")
               + field("gExit", "Reason for leaving", "Death or disablement removes the 5-year condition.", options=[("normal", "Resignation, retirement or contract end"), ("death", "Death or disablement")])
               + field("gEmployer", "Employer", "Government employees' gratuity is fully tax-exempt.", options=[("private", "Private sector"), ("govt", "Government")]))

# ------------------------------------------------------------------ advance tax
ADV_JS = FMT + r'''
function r100(x){return Math.floor(Math.max(0,x)/100)*100;}
function advanceTax(o){
  var T=o.tax;
  if(T<10000) return {applies:false, i425:0, i424:0, due:[0,0,0,0], short:[0,0,0,0]};
  var paid=[o.p1, o.p1+o.p2, o.p1+o.p2+o.p3, o.p1+o.p2+o.p3+o.p4];
  var req = o.presumptive ? [0,0,0,1] : [0.15,0.45,0.75,1];
  var safe= o.presumptive ? [0,0,0,1] : [0.12,0.36,0.75,1];
  var months=[3,3,3,1], i425=0, short=[0,0,0,0], due=[0,0,0,0];
  for(var k=0;k<4;k++){ due[k]=T*req[k]; short[k]=Math.max(0,due[k]-paid[k]); if(paid[k]<T*safe[k]) i425+=r100(short[k])*0.01*months[k]; }
  var i424 = paid[3] < 0.9*T ? r100(T-paid[3])*0.01*o.monthsLate : 0;
  return {applies:true, i425:i425, i424:i424, due:due, short:short};
}
function calc(){
  var r=advanceTax({tax:v("aTax"),presumptive:v("aPres")==="yes",p1:v("aP1"),p2:v("aP2"),p3:v("aP3"),p4:v("aP4"),monthsLate:v("aLate")});
  set("aTotal", r.i425+r.i424); set("aDec", r.due[2]); set("aDecShort", r.short[2]); set("a425", r.i425); set("a424", r.i424);
  set("aTotalHint", r.applies ? "Interest for deferment (Section 425, earlier 234C) + shortfall (Section 424, earlier 234B)" : "No advance tax needed: liability after TDS is below INR 10,000");
}
wire(["aTax","aPres","aP1","aP2","aP3","aP4","aLate"],calc);'''

ADV_INPUTS = (field("aTax", "Estimated tax for FY 2026-27, after TDS/TCS", "Your full-year tax liability minus tax already deducted at source.", value="300000")
              + field("aPres", "Presumptive income (44AD/44ADA-type)?", "Presumptive taxpayers pay 100% by 15 March in one instalment.", options=[("no", "No"), ("yes", "Yes")])
              + field("aP1", "Paid by 15 June 2026", "", value="45000")
              + field("aP2", "Paid 16 June - 15 September 2026", "", value="60000")
              + field("aP3", "Paid / planned 16 September - 15 December 2026", "", value="50000")
              + field("aP4", "Planned 16 December 2026 - 15 March 2027", "", value="145000")
              + field("aLate", "Months from 1 April 2027 until the balance is paid", "If less than 90% was paid by 31 March, interest runs monthly; e.g. 4 if you pay with a July return.", value="0", step="1"))

# ------------------------------------------------------------------ belated ITR
BEL_JS = FMT + r'''
function belated(o){
  var fee = o.required==="no" ? 0 : (o.income<=500000 ? 1000 : 5000);
  var due=new Date(o.dueDate), filed=new Date(o.fileDate);
  var months=0;
  if(filed>due){ months=(filed.getFullYear()-due.getFullYear())*12+(filed.getMonth()-due.getMonth()); if(filed.getDate()>due.getDate()) months+=1; if(months<1) months=1; }
  var interest=Math.floor(Math.max(0,o.taxDue)/100)*100*0.01*months;
  var late = filed>new Date("2026-12-31");
  return {fee:fee, months:months, interest:interest, total:fee+interest+o.taxDue, late:late};
}
function calc(){
  var r=belated({income:v("bIncome"),taxDue:v("bTax"),required:v("bReq"),dueDate:v("bDue"),fileDate:document.getElementById("bFile").value});
  set("bTotal", r.total); set("bFee", r.fee); set("bMonths", r.months+" months"); set("bInt", r.interest); set("bTaxOut", v("bTax"));
  set("bTotalHint", r.late ? "After 31 December 2026 a belated return is no longer possible; only an updated return (ITR-U) with additional tax" : "Tax + Section 234F fee + Section 234A interest, payable before filing");
}
wire(["bIncome","bTax","bReq","bDue","bFile"],calc);'''

BEL_INPUTS = (field("bIncome", "Total income for FY 2025-26", "Decides the late fee: INR 1,000 if INR 5 lakh or less, otherwise INR 5,000.", value="1500000")
              + field("bTax", "Tax still unpaid (after TDS and advance tax)", "Self-assessment tax you will pay before filing.", value="40000")
              + field("bReq", "Were you required to file?", "No late fee if income was below the level at which filing is mandatory.", options=[("yes", "Yes"), ("no", "No, filing voluntarily")])
              + field("bDue", "Original due date", "", options=[("2026-07-31", "31 July 2026 (most individuals)"), ("2026-11-21", "21 November 2026 (audit cases)"), ("2026-11-30", "30 November 2026 (transfer pricing cases)")])
              + f'<div class="field"><label>Date you will file <span class="hint">Belated returns are allowed until 31 December 2026.</span></label><input id="bFile" type="date" value="2026-11-15" /></div>')

# ------------------------------------------------------------------ FAST-DS
FAST_JS = FMT + r'''
function fastds(o){
  if(o.cat==="1"){ var base=o.asset+o.income; var ok=base<=10000000; return {ok:ok, base:base, pay: ok? base*0.60 : 0, bma: base*1.20}; }
  var ok2=o.asset<=50000000; return {ok:ok2, base:o.asset, pay: ok2? 100000 : 0, bma: null};
}
function calc(){
  var r=fastds({cat:v("fCat"),asset:v("fAsset"),income:v("fIncome")});
  set("fPay", r.pay); set("fBase", r.base); set("fBma", r.bma===null ? "Tax already paid; reporting lapse only" : fmt(r.bma));
  set("fPayHint", !r.ok ? (v("fCat")==="1" ? "Above the INR 1 crore limit for Category 1: not eligible" : "Above the INR 5 crore limit for Category 2: not eligible") : (v("fCat")==="1" ? "60% of value (30% tax + equal additional amount). File by 31 December 2026." : "Flat fee of INR 1 lakh. File by 31 December 2026."));
}
wire(["fCat","fAsset","fIncome"],calc);'''

FAST_INPUTS = (field("fCat", "Category", "Category 1: never taxed in India. Category 2: taxed (or bought while non-resident) but not shown in Schedule FA.", options=[("1", "Category 1: untaxed foreign income or assets"), ("2", "Category 2: taxed but unreported assets")])
               + field("fAsset", "Fair market value of foreign assets on 31 March 2026", "Bank balances, shares, ESOPs/RSUs, retirement accounts, property.", value="6000000")
               + field("fIncome", "Undisclosed foreign income not already in those assets", "Category 1 only.", value="2000000"))

CALCS = [
    dict(slug="gratuity-calculator-new-labour-codes-2026",
         title="Gratuity Calculator 2026 Under the New Labour Codes (50% Wage Rule, 1-Year Fixed-Term)",
         em="what you are owed, and how much is tax-free.",
         kicker="/ Free Tool &middot; Gratuity &middot; Updated 2026-10-29",
         lead="Calculate gratuity under the Code on Social Security, 2020: 15 days' wages for each year of service, with wages now at least 50% of total pay and fixed-term employees eligible after one year instead of five. Shows the tax-exempt and taxable parts.",
         block=lambda: calc_block("gratuity-calculator-new-labour-codes-2026", "Gratuity Calculator 2026 (New Labour Codes)", "Gratuity under the Code on Social Security, 2020 with the 50% wage rule and 1-year eligibility for fixed-term employees.",
                                  GRAT_INPUTS, "gAmount", "Estimated gratuity",
                                  [("gWages", "Monthly wages used (after 50% rule)"), ("gUplift", "Added to wages by the 50% rule"), ("gService", "Service counted"), ("gExempt", "Tax-exempt (estimate)"), ("gTaxable", "Taxable (estimate)")], GRAT_JS),
         sections=[
             ("/ How it is calculated", "The rules behind the numbers.",
              ul("<strong>Formula</strong>: monthly wages &times; 15 &divide; 26 &times; years of service.",
                 "<strong>50% wage rule</strong>: from 21 November 2025, basic pay plus DA must be at least 50% of total remuneration. If allowances exceed 50%, the excess is added back to wages for gratuity, PF and other statutory benefits.",
                 "<strong>Eligibility</strong>: permanent employees after 5 years of continuous service (not needed on death or disablement); fixed-term employees after 1 year, paid pro rata.",
                 "<strong>Rounding</strong>: for permanent employees, a part-year of more than six months counts as a full year.",
                 "<strong>Tax</strong>: gratuity of government employees is fully exempt; for others, exemption is limited to INR 20 lakh over the employee's lifetime.",
                 "The calculator gives an estimate; employer policies can be more generous.")),
             ("/ For employers", "What the codes change.",
              ul("Salary structures with low basic pay now cost more in gratuity and PF; review CTC structures and provisions.",
                 "Fixed-term contracts of one year or more now carry a gratuity liability.",
                 "Foreign companies with Indian subsidiaries or employer-of-record arrangements should re-run actuarial provisions under Ind AS 19.") +
              src(("Aditya Birla Capital", "https://lifeinsurance.adityabirlacapital.com/articles/retirement-insurance/gratuity-after-one-year-under-new-labour-law/"), ("Outlook Money", "https://www.outlookmoney.com/retirement/pension/gratuity-under-new-labour-codes-rules-eligibility-and-impact-explained")) +
              "<p><em>Last updated: 29 October 2026. Check the Code text and Ministry of Labour notifications for your case.</em></p>"),
         ],
         faqs=[("How is gratuity calculated under the new labour codes?", "Monthly wages x 15/26 x years of service, where wages must be at least 50% of total remuneration. Fixed-term employees qualify after one year, permanent employees after five."),
               ("What is the 50% wage rule for gratuity?", "Basic pay plus DA must be at least half of total pay. If allowances are more than 50%, the excess is treated as wages for gratuity and PF, which raises the gratuity amount."),
               ("Do fixed-term employees get gratuity after one year?", "Yes. Under the Code on Social Security, a fixed-term employee becomes eligible after one year of service, paid pro rata."),
               ("How much gratuity is tax-free?", "All of it for government employees. For others, up to INR 20 lakh over the employee's lifetime."),
               ("Can BQP review our payroll for the labour codes?", "Yes: salary restructuring, gratuity and PF exposure, and Ind AS 19 provisions for Indian companies and foreign-owned subsidiaries. " + CONTACT)],
         related=[("employer-of-record-india-hire-from-abroad.html", "Hiring in India from abroad"), ("foreign-company-setup-indian-subsidiary-wos.html", "Setting up an Indian subsidiary")],
         keywords="gratuity calculator 2026, gratuity calculator new labour code, gratuity 50% wage rule calculator, fixed term employee gratuity 1 year, gratuity tax exemption 20 lakh",
         desc="Free gratuity calculator 2026 under the new labour codes: 15/26 formula, 50% wage rule from 21 November 2025, 1-year eligibility for fixed-term employees, and the tax-exempt and taxable parts."),
    dict(slug="advance-tax-calculator-fy-2026-27-15-december-instalment",
         title="Advance Tax Calculator FY 2026-27: 15 December Instalment and Interest",
         em="what to pay by 15 December 2026.",
         kicker="/ Free Tool &middot; Advance Tax &middot; Updated 2026-10-29",
         lead="By 15 December 2026, 75% of your FY 2026-27 tax (after TDS) should be paid as advance tax. Enter your estimate and what you have paid; the calculator shows the December shortfall and the interest under Sections 425 and 424 of the Income-tax Act, 2025 (earlier Sections 234C and 234B).",
         block=lambda: calc_block("advance-tax-calculator-fy-2026-27-15-december-instalment", "Advance Tax Calculator FY 2026-27", "Advance tax instalments and interest for deferment and shortfall for tax year 2026-27.",
                                  ADV_INPUTS, "aTotal", "Estimated interest",
                                  [("aDec", "Cumulative due by 15 December (75%)"), ("aDecShort", "Shortfall at 15 December"), ("a425", "Interest for deferment (Sec. 425 / earlier 234C)"), ("a424", "Interest for shortfall (Sec. 424 / earlier 234B)")], ADV_JS),
         sections=[
             ("/ The schedule", "Cumulative instalments.",
              "<table><thead><tr><th>By</th><th>Cumulative</th><th>No interest if at least</th></tr></thead><tbody>"
              "<tr><td>15 June 2026</td><td>15%</td><td>12%</td></tr><tr><td>15 September 2026</td><td>45%</td><td>36%</td></tr>"
              "<tr><td>15 December 2026</td><td>75%</td><td>75%</td></tr><tr><td>15 March 2027</td><td>100%</td><td>100%</td></tr></tbody></table>"
              + ul("Advance tax applies if tax after TDS is INR 10,000 or more; resident senior citizens without business income are exempt.",
                   "Interest for deferment: 1% a month on the shortfall, for three months for each of the first three instalments and one month for the last.",
                   "Interest for shortfall: 1% a month from 1 April 2027 if less than 90% was paid by 31 March 2027.",
                   "Interest is computed on amounts rounded down to the nearest INR 100.")),
             ("/ What counts", "Getting the estimate right.",
              ul("Include capital gains, interest, rent and freelance or business income, not just salary.",
                 "Foreign income is taxable if you are resident and ordinarily resident; claim credit for foreign tax in the return.",
                 "Gains arising after an instalment date can be paid in the next instalment without deferment interest for that part.") +
              src(("India Briefing: advance tax under the Income-tax Act, 2025", "https://india-briefing.com/news/indias-advance-tax-due-dates-tax-year-2026-27-45178.html/")) +
              "<p><em>Last updated: 29 October 2026. Assumes the 2025 Act keeps the same rates and schedule as the 1961 Act's Sections 234B and 234C.</em></p>"),
         ],
         faqs=[("When is the third advance tax instalment for FY 2026-27?", "15 December 2026, by which 75% of the year's tax (after TDS) should be paid."),
               ("What is the interest for missing the 15 December instalment?", "1% a month for three months on the shortfall against 75% of the tax, under Section 425 of the Income-tax Act, 2025 (earlier Section 234C)."),
               ("Who has to pay advance tax?", "Anyone whose tax after TDS is INR 10,000 or more, except resident senior citizens without business income."),
               ("When does Section 424 (earlier 234B) interest apply?", "If less than 90% of the tax was paid as advance tax by 31 March, at 1% a month from 1 April until the balance is paid."),
               ("Can BQP compute and pay my advance tax?", "Yes, including capital gains, foreign income and NRI cases. " + CONTACT)],
         related=[("advance-tax-q3-december-15-2026-india.html", "15 December 2026 advance tax guide"), ("income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", "Income-tax Act 2025 section changes")],
         keywords="advance tax calculator FY 2026-27, advance tax 15 December 2026, 234C interest calculator, section 425 interest advance tax, advance tax due dates 2026-27",
         desc="Free advance tax calculator for FY 2026-27: 15 December 2026 instalment (75%), shortfall, and interest under Sections 425 and 424 of the Income-tax Act, 2025 (earlier 234C and 234B)."),
    dict(slug="belated-itr-late-fee-interest-calculator-234f-234a-2026",
         title="Belated ITR Late Fee and Interest Calculator: Section 234F and 234A (File by 31 December 2026)",
         em="the cost of filing late.",
         kicker="/ Free Tool &middot; Belated ITR &middot; Updated 2026-10-29",
         lead="Missed the ITR due date for FY 2025-26? A belated return can still be filed until 31 December 2026. This calculator shows the Section 234F late fee (INR 1,000 or INR 5,000) and Section 234A interest of 1% a month on unpaid tax, so you know the total to pay before filing.",
         block=lambda: calc_block("belated-itr-late-fee-interest-calculator-234f-234a-2026", "Belated ITR Late Fee and Interest Calculator", "Section 234F late fee and Section 234A interest for belated FY 2025-26 income tax returns.",
                                  BEL_INPUTS, "bTotal", "Total to pay before filing",
                                  [("bTaxOut", "Unpaid tax"), ("bFee", "Late fee (Section 234F)"), ("bMonths", "Months of delay"), ("bInt", "Interest (Section 234A)")], BEL_JS),
         sections=[
             ("/ The rules", "FY 2025-26 returns (1961 Act).",
              ul("<strong>Late fee, Section 234F</strong>: INR 5,000; INR 1,000 if total income is INR 5 lakh or less.",
                 "<strong>Interest, Section 234A</strong>: 1% for every month or part of a month from the day after the due date until filing, on tax unpaid, rounded down to the nearest INR 100.",
                 "<strong>Last date</strong>: 31 December 2026 for belated and revised returns.",
                 "<strong>Losses</strong>: business and capital losses cannot be carried forward from a belated return.",
                 "<strong>After 31 December</strong>: only an updated return (ITR-U) with 25% to 70% additional tax, and no refunds.")),
             ("/ Next step", "File, or let us file.",
              f'<p>See <a href="belated-itr-31-december-2026-section-139-4-india.html">the belated return guide</a> or, for NRIs, <a href="nri-missed-itr-deadline-what-to-do-india.html">what to do if you missed the ITR deadline</a>.</p>'
              "<p><em>Last updated: 29 October 2026.</em></p>"),
         ],
         faqs=[("What is the late fee for filing ITR after the due date?", "INR 5,000 under Section 234F, or INR 1,000 if total income is INR 5 lakh or less."),
               ("How is Section 234A interest calculated?", "1% for each month or part month from the day after the due date until the return is filed, on the tax still unpaid."),
               ("What is the last date for a belated return for FY 2025-26?", "31 December 2026."),
               ("Is there a late fee if my income is below the taxable limit?", "No late fee applies if you were not required to file and are filing voluntarily."),
               ("Can BQP file my belated return?", "Yes, for residents and NRIs. " + CONTACT)],
         related=[("belated-itr-31-december-2026-section-139-4-india.html", "Belated ITR guide"), ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)")],
         keywords="belated ITR late fee calculator, 234F late fee calculator, 234A interest calculator, belated return 31 December 2026, ITR late filing penalty calculator",
         desc="Free calculator for belated FY 2025-26 income tax returns: Section 234F late fee (INR 1,000 or 5,000) and Section 234A interest at 1% a month. Belated returns allowed until 31 December 2026."),
    dict(slug="fast-ds-2026-calculator-foreign-asset-disclosure-cost",
         title="FAST-DS 2026 Calculator: What It Costs to Declare Undisclosed Foreign Assets",
         em="before the 31 December 2026 deadline.",
         kicker="/ Free Tool &middot; FAST-DS &middot; Updated 2026-10-29",
         lead="Estimate the amount payable under FAST-DS 2026, the one-time foreign asset disclosure scheme for small taxpayers: 60% of the value for untaxed foreign income or assets up to INR 1 crore, or a flat INR 1 lakh for taxed-but-unreported assets up to INR 5 crore. Declarations close on 31 December 2026.",
         block=lambda: calc_block("fast-ds-2026-calculator-foreign-asset-disclosure-cost", "FAST-DS 2026 Calculator", "Amount payable under the Foreign Assets of Small Taxpayers Disclosure Scheme 2026.",
                                  FAST_INPUTS, "fPay", "Amount payable under FAST-DS",
                                  [("fBase", "Value declared"), ("fBma", "Black Money Act if found later (30% tax + 90% penalty)")], FAST_JS),
         sections=[
             ("/ How it works", "Two categories.",
              ul("<strong>Category 1</strong>: foreign income or assets never taxed in India, up to INR 1 crore in aggregate. Pay 30% tax plus an equal additional amount: 60% of the value.",
                 "<strong>Category 2</strong>: assets already taxed, or acquired while non-resident, but not shown in Schedule FA, up to INR 5 crore. Flat fee of INR 1 lakh.",
                 "Assets are valued at fair market value as on 31 March 2026.",
                 "A valid declaration gives immunity from tax, penalty and prosecution under the Black Money Act for the declared items.",
                 "For comparison, the Black Money Act charges 30% tax and a penalty of up to three times that tax if undisclosed assets are found, and prosecution is possible.")),
             ("/ Next step", "Declare before 31 December.",
              '<p>Read the <a href="fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html">full FAST-DS 2026 guide</a>.</p>' +
              src(("Outlook Money", "https://www.outlookmoney.com/personal-finance/fast-ds-2026-goes-live-small-taxpayers-get-window-to-declare-foreign-assets-income")) +
              "<p><em>Last updated: 29 October 2026. Estimate only; eligibility depends on your facts.</em></p>"),
         ],
         faqs=[("How much do I pay under FAST-DS 2026?", "Category 1 (untaxed foreign income or assets up to INR 1 crore): 60% of the value. Category 2 (taxed-but-unreported assets up to INR 5 crore): a flat INR 1 lakh."),
               ("What is the last date for FAST-DS 2026?", "31 December 2026."),
               ("Which date is used to value foreign assets?", "Fair market value as on 31 March 2026."),
               ("What happens if I don't declare?", "If found later, undisclosed foreign assets are taxed under the Black Money Act at 30% plus a penalty of up to three times the tax, and prosecution is possible."),
               ("Can BQP file my FAST-DS declaration?", "Yes. " + CONTACT)],
         related=[("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS 2026 guide"), ("nri-returning-india-tax-rnor-transition.html", "Returning to India: RNOR")],
         keywords="FAST-DS calculator, FAST-DS 2026 calculator, foreign asset disclosure scheme calculator, undisclosed foreign assets tax calculator India, FAST-DS 60 percent",
         desc="Free FAST-DS 2026 calculator: amount payable to declare undisclosed foreign assets (60% for Category 1 up to INR 1 crore, INR 1 lakh for Category 2 up to INR 5 crore) before 31 December 2026, compared with Black Money Act exposure."),
]

for c in CALCS:
    H2 = {"gratuity": "Calculate your gratuity.", "advance-tax": "Check your 15 December payment.", "belated": "Calculate fee and interest.", "fast-ds": "Estimate your FAST-DS amount."}
    h2 = next(t for k, t in H2.items() if c["slug"].startswith(k))
    sections = [("/ Calculator", h2, c["block"]())] + c["sections"]
    html = page(slug=c["slug"], title=c["title"], description=c["desc"], keywords=c["keywords"],
                hero_kicker=c["kicker"], hero_title_html=f'{c["title"]}, <em>{c["em"]}</em>',
                hero_lead=c["lead"], sections=sections, faqs=c["faqs"],
                related=[(h, "Related", t) for h, t in c["related"]],
                cta_headline="Want a CA to check the numbers?", cta_body=CONTACT)
    write_page(c["slug"], html)

print(f"Batch AJ complete: {len(CALCS)} calculators")
