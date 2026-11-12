# -*- coding: utf-8 -*-
"""Batch AZ: FAST-DS 2026 cluster built from the Finance Act, 2026, Chapter IV (sections 130-144), as published on incometaxindia.gov.in.
Eligibility logic: tools/fastds-eligibility-logic.js (tests: node tools/fastds-eligibility-logic.test.js)."""
import json
import re
from urllib.parse import quote
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
WA = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I need help with FAST-DS 2026. My situation: ")
CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with a short note of your foreign accounts or assets and the years you were resident. "
           "Fixed-scope quote within 48 hours.")
UPDATED = "Last updated: 4 November 2026."
DEADLINE = "Declarations close on 31 December 2026."
LAW = "https://wm.incometaxindia.gov.in/w/section-133-93"
SRC_LAW = f'<p><strong>Source:</strong> Finance Act, 2026, Chapter IV (sections 130 to 144), the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026, as published by the <a href="{LAW}" rel="nofollow noopener" target="_blank">Income Tax Department</a>. Forms, valuation and payment mechanics are in the FAST-DS Rules. <em>{UPDATED}</em></p>'


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def cta_box(text="Not sure which category applies to you?"):
    return (f'<div style="border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{text}</p>'
            f'<p style="margin:0">Send us your situation on <a href="{WA}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a> or use the <a href="fast-ds-2026-eligibility-checker.html">FAST-DS eligibility checker</a>. {DEADLINE}</p></div>')


RELATED_ALL = [("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help"), ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"),
               ("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS amount calculator")]

CATS = ("<table><thead><tr><th></th><th>Category 1</th><th>Category 2</th></tr></thead><tbody>"
        "<tr><td>What</td><td>Undisclosed asset located outside India (no satisfactory explanation of the source of investment), or undisclosed foreign income (chargeable to tax in India but not offered to tax)</td><td>Asset outside India bought (a) from foreign income earned while non-resident, or (b) from income already offered to tax in India, but not shown in the foreign-assets schedule of the return</td></tr>"
        "<tr><td>Amount payable</td><td>30% tax on the asset value as on 31 March 2026 and on the income, plus an equal amount: 60% in all</td><td>A fee of INR 1 lakh</td></tr>"
        "<tr><td>Limit</td><td>Aggregate of such assets and income up to INR 1 crore</td><td>Value of the asset up to INR 5 crore</td></tr>"
        "<tr><td>Law</td><td>Section 133, Table, item 1</td><td>Section 133, Table, item 2</td></tr></tbody></table>")

TIMELINE = ul("<strong>Declaration (Form 1)</strong>: filed electronically on the e-filing portal by <strong>31 December 2026</strong> (sections 132 and 134).",
              "<strong>Order of amount payable</strong>: issued within one month from the end of the month in which you declare (section 135(1)).",
              "<strong>Payment</strong>: within two months from the end of the month in which you receive the order; or within a further two months with simple interest of 1% a month or part of a month (section 135(2) and (3)).",
              "<strong>Intimation of payment</strong>: within the extended period (section 135(4)).",
              "<strong>Certificate</strong>: an order certifying payment within one month from the end of the month of the intimation, conclusive as to the matters stated (section 135(5) and (6)).")

PAGES = []

# 1. Money page
PAGES.append(dict(
    slug="fast-ds-2026-filing-help-chartered-accountant",
    title="FAST-DS 2026 Filing Help From a Chartered Accountant: Category, Form 1 and Payment Before 31 December",
    em="declare foreign assets the right way, once.",
    kicker="/ FAST-DS 2026 &middot; Filing Help &middot; Updated 2026-11-04",
    lead=("FAST-DS 2026 lets eligible taxpayers declare foreign assets and income they left out of their Indian returns, pay either 60% (Category 1) or a flat INR 1 lakh (Category 2), and get immunity from tax, penalty and prosecution under the Black Money Act. Getting the category, residential status and valuation right matters: a declaration with a false material particular is invalid (section 134(3)) and nothing paid is refundable (section 138). "
          "Bharat Quantum Prospera, led by CA Durgesh Chavda, handles the whole process. " + DEADLINE),
    sections=[
        ("/ Who we help", "The situations we see most.",
         ul("Employees holding RSUs or ESPP shares of a foreign employer that were taxed through Indian payroll but never shown in the foreign-assets schedule.",
            "Returning NRIs with US 401(k)/IRA, UK pensions, foreign bank or brokerage accounts not reported after becoming resident and ordinarily resident.",
            "Students and professionals with old foreign bank accounts, deposits or crypto accounts left open after returning to India.",
            "Taxpayers who received the Income Tax Department's email about foreign assets in their AIS.",
            "Current NRIs who were resident when the foreign income arose or the asset was acquired (they are eligible under section 131(1)(a)(ii)).") + cta_box()),
        ("/ The two categories", "What you pay and when.", CATS),
        ("/ What we do", "End to end, fixed scope.",
         "<ol><li>Review your AIS (foreign assets information), past returns and residential status year by year.</li>"
         "<li>Classify each asset and income item: no action, revised or updated return, Category 1, or Category 2, and check the INR 1 crore and INR 5 crore limits and the exclusions in section 140.</li>"
         "<li>Value each asset as on 31 March 2026 in the prescribed manner.</li>"
         "<li>Prepare and file Form 1 on the e-filing portal and verify it electronically.</li>"
         "<li>Track the order of amount payable, arrange payment in time, file the payment intimation and obtain the certificate.</li></ol>"
         "<p><strong>What to send us</strong>: a list of foreign accounts and assets with opening dates, statements, the source of funds for each, your Indian returns for the relevant years, your AIS and the dates you lived abroad.</p>"),
        ("/ Timeline", "From declaration to certificate.", TIMELINE + SRC_LAW),
    ],
    faqs=[
        ("Can a chartered accountant file FAST-DS for me?", "Yes. We review your residential status and records, determine the category, value the assets, file Form 1, and manage payment and the final certificate. " + CONTACT),
        ("What is the last date for FAST-DS 2026?", "31 December 2026 for filing the declaration. Payment follows the order issued after the declaration."),
        ("How much does FAST-DS cost in tax?", "Category 1: 60% of the value of undisclosed foreign assets (as on 31 March 2026) and undisclosed foreign income, if the total is INR 1 crore or less. Category 2: a fee of INR 1 lakh for assets bought from explained income but not reported in the foreign-assets schedule, if the asset value is INR 5 crore or less."),
        ("Is the amount paid under FAST-DS refundable?", "No. Section 138 of the scheme says no amount paid is refundable, so check the category before filing."),
        ("What immunity does FAST-DS give?", "A valid declaration with payment gives immunity from further tax, penalty and prosecution under the Black Money Act for the declared income or asset, for years up to 2025-26 (section 139)."),
    ],
    related=RELATED_ALL[1:] + [("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS 2026 guide")],
    cta_h="Declare before 31 December 2026", cta_b=CONTACT,
    keywords="FAST-DS filing help, FAST-DS chartered accountant, FAST-DS consultant, FAST-DS 2026 CA, foreign asset disclosure scheme help, FAST-DS Form 1 filing, FAST-DS category 1 category 2, declare foreign assets India 2026",
    desc="FAST-DS 2026 filing by a Chartered Accountant: residential status review, Category 1 (60%) or Category 2 (INR 1 lakh), valuation as on 31 March 2026, Form 1, payment and certificate. Declarations close 31 December 2026.",
    howto=None))

# 2. Eligibility checker (tool)
LOGIC = open("tools/fastds-eligibility-logic.js", encoding="utf-8").read().replace('if (typeof module !== "undefined") module.exports = { fastds: fastds };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += "\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:14px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n  .calc-embed .rtrace li{margin:0 0 6px}\n"


def fld(fid, label, hint, opts=None, num=None):
    if opts:
        ctrl = f'<select id="{fid}">' + "".join(f'<option value="{v}">{t}</option>' for v, t in opts) + "</select>"
    else:
        ctrl = f'<input id="{fid}" type="number" min="0" step="1000" value="{num}" inputmode="numeric" />'
    return f'<div class="field" id="w_{fid}"><label for="{fid}">{label} <span class="hint">{hint}</span></label>{ctrl}</div>'


YN = [("no", "No"), ("yes", "Yes")]
INPUTS = (fld("fKind", "What are you checking?", "Check one asset or income item at a time.", [("asset", "A foreign asset (bank account, shares, RSUs, 401(k), property, crypto)"), ("income", "Foreign income (interest, dividends, rent, salary) not shown in my return")])
          + fld("fResThen", "Were you resident in India when you acquired it / earned it?", "Resident under section 6 in that year.", [("yes", "Yes, resident"), ("no", "No, I was a non-resident (or RNOR)")])
          + fld("fResSince", "Have you been resident and ordinarily resident in India in any later year up to 2025-26?", "Only asked if you were non-resident at the time.", YN)
          + fld("fSource", "Where did the money to buy it come from?", "", [("taxedIndia", "Income already taxed in India (salary, RSU/ESPP taxed via payroll, savings)"), ("foreignWhileNR", "Foreign income earned while I was a non-resident"), ("untaxed", "Income never taxed in India / I cannot explain the source")])
          + fld("fFA", "Was it shown in the foreign-assets schedule (Schedule FA) of every return where required?", "Required in years you were resident and ordinarily resident.", YN)
          + fld("fInc", "Was all income from it (interest, dividends, gains) offered to tax in India in resident years?", "", [("yes", "Yes"), ("no", "No")])
          + fld("fVal", "Value in INR", "Asset: value as on 31 March 2026. Income: amount of the income.", num=2000000)
          + fld("fOther", "Other Category 1 items you are also declaring (INR)", "For the INR 1 crore aggregate limit. Leave 0 if none.", num=0)
          + fld("fPmla", "Any proceedings under the Prevention of Money-laundering Act on this income or asset?", "", YN)
          + fld("fBma", "Has a Black Money Act assessment already been completed for the year?", "", YN))
CHECK_JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  var LABEL={CAT1:"Category 1 (60%)",CAT2:"Category 2 (INR 1 lakh fee)",NOT_NEEDED:"No FAST-DS needed",INCOME_ONLY:"Declare the income only",NOT_ELIGIBLE:"Not eligible for FAST-DS",EXCLUDED:"Excluded from FAST-DS"};
  function show(){
    var kind=$("fKind").value, resThen=$("fResThen").value==="yes";
    $("w_fResSince").style.display=resThen?"none":""; ["w_fSource","w_fFA"].forEach(function(w){$(w).style.display=kind==="asset"?"":"none";});
    var r=fastds({kind:kind,residentThen:resThen,residentSince:resThen||$("fResSince").value==="yes",source:$("fSource").value,reportedFA:$("fFA").value==="yes",incomeReported:$("fInc").value==="yes",
      value:Number($("fVal").value),otherCat1:Number($("fOther").value||0),pmla:$("fPmla").value==="yes",bmaDone:$("fBma").value==="yes"});
    if(!r.ok){$("fOut").textContent="Check inputs";$("fAmt").textContent="";$("fWhy").innerHTML=r.errors.map(function(e){return "<li>"+e+"</li>";}).join("");return;}
    $("fOut").textContent=LABEL[r.result];
    $("fAmt").textContent=r.amount?("Amount payable on this item: INR "+r.amount.toLocaleString("en-IN")):"";
    $("fWhy").innerHTML=r.why.map(function(t){return "<li>"+t+"</li>";}).join("");
  }
  ["fKind","fResThen","fResSince","fSource","fFA","fInc","fVal","fOther","fPmla","fBma"].forEach(function(id){$(id).addEventListener("input",show);$(id).addEventListener("change",show);});
  // Prefill from a link (used by the FAST-DS self-check newsletter): ?kind=&then=&since=&src=&fa=&inc=&val=
  try {
    var q=new URLSearchParams(location.search), MAP={kind:"fKind",then:"fResThen",since:"fResSince",src:"fSource",fa:"fFA",inc:"fInc",val:"fVal"}, hit=false;
    Object.keys(MAP).forEach(function(k){ var v=q.get(k), el=$(MAP[k]); if(v===null||!el) return;
      if(el.tagName==="SELECT"){ if([].some.call(el.options,function(o){return o.value===v;})){ el.value=v; hit=true; } }
      else if(/^\d+(\.\d+)?$/.test(v)){ el.value=v; hit=true; } });
    if(hit){ var go=function(){ var c=document.querySelector(".calc-embed"); if(c){ window.scrollTo(0, c.getBoundingClientRect().top + window.pageYOffset - 80); } }; if(document.readyState==="complete") setTimeout(go,150); else window.addEventListener("load", function(){ setTimeout(go,150); }); }
  } catch(e) {}
  show();
})();'''
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "FAST-DS 2026 Eligibility Checker", "url": f"{DOMAIN}/fast-ds-2026-eligibility-checker.html",
       "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "description": "Checks whether a foreign asset or income falls under Category 1, Category 2, or neither, under the Foreign Assets of Small Taxpayers Disclosure Scheme, 2026.",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"}, "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"},
       "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN}}
BLOCK = (f"<style>{CALC_CSS}</style>"
         f'<script type="application/ld+json">{json.dumps(app, separators=(",", ":"), ensure_ascii=False)}</script>'
         f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your item</h2><p class="sub">Answer for one asset or income item.</p>{INPUTS}</div>'
         '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="fOut" style="font-size:26px">-</div><div class="rhint" id="fAmt"></div>'
         '<p style="font-size:13px;margin:14px 0 0;font-weight:600">Why</p><ol class="rtrace" id="fWhy"></ol>'
         f'<p style="font-size:13px;margin:12px 0 0"><a href="{WA}" target="_blank" rel="noopener">Get this checked by a CA on WhatsApp &rarr;</a></p></div></div></div>'
         f"<script>{CHECK_JS}\n</script>")
PAGES.append(dict(
    slug="fast-ds-2026-eligibility-checker",
    title="FAST-DS 2026 Eligibility Checker: Category 1, Category 2 or Not Needed?",
    em="answer a few questions per asset.",
    kicker="/ Free Tool &middot; FAST-DS 2026 &middot; Updated 2026-11-04",
    lead="Check each foreign asset or income item against the scheme's own tests: whether you were resident when you acquired or earned it, where the money came from, whether it was shown in the foreign-assets schedule, and the INR 1 crore and INR 5 crore limits. The checker cites the section of the Finance Act, 2026 behind each answer. " + DEADLINE,
    sections=[("/ Checker", "Check an asset or income item.", BLOCK),
              ("/ How the checker decides", "The scheme's tests.",
               ul("<strong>Eligible person</strong> (section 131(1)(a)): resident in the year; or a non-resident/RNOR who was resident in the year the income arose or the asset was acquired.",
                  "<strong>Undisclosed foreign asset</strong> (section 131(1)(j)): an asset outside India whose source of investment you cannot satisfactorily explain. Category 1.",
                  "<strong>Undisclosed foreign income</strong> (section 131(1)(k)): foreign-source income chargeable to tax in India but not offered to tax. Category 1.",
                  "<strong>Category 2</strong> (section 133, item 2): asset bought from foreign income while non-resident, or from income taxed in India, not shown in the foreign-assets schedule.",
                  "<strong>Exclusions</strong> (section 140): proceeds of crime with PMLA proceedings initiated or pending; years where a Black Money Act assessment is completed.") + SRC_LAW)],
    faqs=[("How do I know if I am eligible for FAST-DS?", "You are eligible if you were resident in India in the year, or are now non-resident but were resident when the foreign income arose or the asset was acquired, and the item is an undisclosed foreign asset or income (Category 1, total up to INR 1 crore) or an asset bought from explained income but missing from the foreign-assets schedule (Category 2, up to INR 5 crore)."),
          ("Can an NRI use FAST-DS?", "Yes, if he or she was resident in India in the year the income arose or the asset was acquired (section 131(1)(a)(ii))."),
          ("Do I need FAST-DS if I reported everything?", "No. If the asset was bought from explained funds, shown in the foreign-assets schedule and its income was taxed, nothing is undisclosed."),
          ("Can BQP confirm the checker's result?", "Yes. " + CONTACT)],
    related=[("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help"), ("fast-ds-2026-calculator-foreign-asset-disclosure-cost.html", "FAST-DS amount calculator")],
    cta_h="Want a CA to confirm your category?", cta_b=CONTACT,
    keywords="FAST-DS eligibility, FAST-DS eligibility checker, am I eligible for FAST-DS, FAST-DS category 1 or 2, FAST-DS NRI eligible, FAST-DS 2026 who can apply",
    desc="Free FAST-DS 2026 eligibility checker: Category 1 (60%, up to INR 1 crore), Category 2 (INR 1 lakh fee, up to INR 5 crore) or not needed, per asset, citing sections 131, 133 and 140 of the Finance Act, 2026.",
    howto=None))

# 3. RSUs / ESPP / 401(k)
PAGES.append(dict(
    slug="fast-ds-rsu-espp-us-shares-401k-which-category",
    title="FAST-DS for RSUs, ESPP Shares and 401(k): Which Category Applies?",
    em="most tech employees fall in Category 2.",
    kicker="/ FAST-DS 2026 &middot; Employees &middot; Updated 2026-11-04",
    lead="If your foreign employer's RSUs or ESPP shares were taxed through Indian payroll, the shares were bought from income already offered to tax. If they were never shown in the foreign-assets schedule of your return, they fall in Category 2: a fee of INR 1 lakh, if the value is INR 5 crore or less. A 401(k) or IRA built while you were non-resident is also Category 2 if you did not report it after becoming resident and ordinarily resident. Unreported dividends or sale gains are separate: they are undisclosed foreign income under Category 1 (60%). " + DEADLINE,
    sections=[("/ Common holdings", "How each is treated.",
               "<table><thead><tr><th>Holding</th><th>Usual category</th><th>Why</th></tr></thead><tbody>"
               "<tr><td>RSUs vested and taxed as a perquisite through Indian payroll, not in Schedule FA</td><td>Category 2</td><td>Bought from income offered to tax (section 133, item 2(b))</td></tr>"
               "<tr><td>ESPP shares bought from Indian salary, not in Schedule FA</td><td>Category 2</td><td>Same reason</td></tr>"
               "<tr><td>401(k), IRA or foreign pension built while non-resident, not reported after becoming resident and ordinarily resident</td><td>Category 2</td><td>Foreign income earned while non-resident (section 133, item 2(a))</td></tr>"
               "<tr><td>Dividends or sale gains on these, not offered to tax in resident years</td><td>Category 1</td><td>Undisclosed foreign income (section 131(1)(k))</td></tr>"
               "<tr><td>Shares bought from money never taxed in India</td><td>Category 1</td><td>Undisclosed asset (section 131(1)(j))</td></tr></tbody></table>"
               + cta_box("Holding RSUs, ESPP or a 401(k)?")),
              ("/ Before you file", "Check these first.",
               ul("Your residential status for each year: the foreign-assets schedule is required in years you are resident and ordinarily resident, not in RNOR years.",
                  "Whether the dividends and gains were reported; for 2025-26, a revised return (free until 31 December 2026, or with a fee until 31 March 2027) can fix the return itself.",
                  "Whether the total of Category 2 assets is within INR 5 crore, and any Category 1 items within INR 1 crore.") + SRC_LAW)],
    faqs=[("Do RSUs need FAST-DS?", "If the RSU shares were taxed through Indian payroll but never shown in the foreign-assets schedule, they usually fall under Category 2: a fee of INR 1 lakh, if the value is INR 5 crore or less."),
          ("Is a US 401(k) covered by FAST-DS?", "A 401(k) built while you were non-resident and not reported after you became resident and ordinarily resident usually falls in Category 2 (asset bought from foreign income earned while non-resident)."),
          ("What about unreported dividends on RSUs?", "Dividends or gains not offered to tax in resident years are undisclosed foreign income, declared under Category 1 at 60%, unless corrected through a return that can still be revised."),
          ("Can BQP handle FAST-DS for RSUs and 401(k)?", "Yes. " + CONTACT)],
    related=[("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"), ("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help")],
    cta_h="RSUs, ESPP or 401(k) not in your return?", cta_b=CONTACT,
    keywords="FAST-DS RSU, FAST-DS ESPP, FAST-DS 401k, RSU not declared in Schedule FA, foreign shares not reported ITR, FAST-DS category 2 RSU, US stocks Schedule FA missed",
    desc="FAST-DS 2026 for RSUs, ESPP shares and 401(k): shares taxed through Indian payroll but missing from Schedule FA are usually Category 2 (INR 1 lakh fee, up to INR 5 crore); unreported dividends and gains are Category 1 (60%).",
    howto=None))

# 4. Returning NRIs / current NRIs
PAGES.append(dict(
    slug="fast-ds-returning-nri-foreign-accounts-not-reported",
    title="FAST-DS for Returning NRIs: Foreign Accounts and Pensions Not Reported After Coming Back",
    em="and whether current NRIs can use it.",
    kicker="/ FAST-DS 2026 &middot; NRIs &middot; Updated 2026-11-04",
    lead="Many returning NRIs kept foreign bank accounts, brokerage accounts, pensions or property but did not list them in the foreign-assets schedule once they became resident and ordinarily resident. Assets built from foreign income earned while non-resident fall in Category 2 of FAST-DS (fee INR 1 lakh, value up to INR 5 crore). Interest, dividends or rent on them that were not offered to tax in resident years are Category 1 (60%). A current NRI can also use the scheme if he or she was resident when the income arose or the asset was acquired. " + DEADLINE,
    sections=[("/ Where returning NRIs stand", "Year by year.",
               ul("<strong>RNOR years</strong>: foreign income is generally not taxable and the foreign-assets schedule is not required, so there is usually nothing undisclosed for those years.",
                  "<strong>First resident and ordinarily resident year onwards</strong>: foreign assets must be listed in the schedule and worldwide income taxed. Missing these is what FAST-DS cures.",
                  "<strong>Eligibility</strong>: a person resident in the year, or a non-resident/RNOR who was resident when the income arose or the asset was acquired (section 131(1)(a)).") + cta_box("Returned to India with foreign accounts?")),
              ("/ Steps", "What to do now.",
               "<ol><li>Work out your residential status for each year since you returned (use our <a href=\"residential-status-calculator-india-nri-rnor-section-6.html\">residential status calculator</a>).</li>"
               "<li>List each foreign asset with its value as on 31 March 2026 and the source of funds.</li>"
               "<li>Check the AIS foreign-assets information on the e-filing portal.</li>"
               "<li>Classify each item (<a href=\"fast-ds-2026-eligibility-checker.html\">eligibility checker</a>) and file Form 1 by 31 December 2026.</li></ol>" + SRC_LAW)],
    faqs=[("I returned to India and kept my US accounts. Do I need FAST-DS?", "If you have been resident and ordinarily resident and did not list them in the foreign-assets schedule, yes, usually under Category 2 for assets built while non-resident (INR 1 lakh fee), with any untaxed income from them under Category 1."),
          ("Can a current NRI file FAST-DS?", "Yes, if he or she was resident in India in the year the income arose or the asset was acquired (section 131(1)(a)(ii))."),
          ("Did I need to report foreign assets in RNOR years?", "No. The foreign-assets schedule is for residents who are ordinarily resident; RNOR years are generally outside it."),
          ("Can BQP help returning NRIs with FAST-DS?", "Yes. " + CONTACT)],
    related=[("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator"), ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker")],
    cta_h="Returned NRI with foreign assets?", cta_b=CONTACT,
    keywords="FAST-DS returning NRI, FAST-DS NRI eligibility, foreign bank account not declared after returning India, 401k not reported ITR returning NRI, can NRI file FAST-DS, Schedule FA returning NRI",
    desc="FAST-DS 2026 for returning NRIs: foreign accounts, pensions and property built while non-resident but not reported after becoming resident and ordinarily resident are usually Category 2 (INR 1 lakh); current NRIs are eligible if they were resident when the asset was acquired.",
    howto=None))

# 5. FAST-DS vs revised return vs ITR-U
PAGES.append(dict(
    slug="fast-ds-vs-revised-return-vs-updated-return-itr-u",
    title="FAST-DS vs Revised Return vs Updated Return (ITR-U): Which Route for Foreign Assets?",
    em="the answer depends on the year and the category.",
    kicker="/ FAST-DS 2026 &middot; Comparison &middot; Updated 2026-11-04",
    lead="For FY 2025-26, a revised return can be filed free until 31 December 2026 (and with a section 234-I fee until 31 March 2027) and can add a missed foreign asset or income to that return. An updated return (ITR-U) lets you offer more income for earlier years with additional tax, but it does not grant immunity under the Black Money Act. FAST-DS 2026 does: a valid declaration with payment gives immunity from further tax, penalty and prosecution under the Black Money Act for the declared items, for years up to 2025-26 (section 139). " + DEADLINE,
    sections=[("/ Side by side", "Choosing the route.",
               "<table><thead><tr><th></th><th>Revised return</th><th>Updated return (ITR-U)</th><th>FAST-DS 2026</th></tr></thead><tbody>"
               "<tr><td>Years covered</td><td>FY 2025-26 (free until 31 December 2026; with a fee until 31 March 2027)</td><td>Earlier years within the time allowed</td><td>Any year up to 2025-26</td></tr>"
               "<tr><td>Cost</td><td>Normal tax and interest</td><td>Tax, interest and additional tax that rises with delay</td><td>60% (Category 1) or INR 1 lakh (Category 2)</td></tr>"
               "<tr><td>Black Money Act immunity</td><td>Not by itself</td><td>No</td><td>Yes, for declared items (section 139)</td></tr>"
               "<tr><td>Refund of amount paid</td><td>As per return</td><td>As per return</td><td>Not refundable (section 138)</td></tr></tbody></table>"
               + cta_box("Not sure which route is cheaper for you?")),
              ("/ How to decide", "Practical rule of thumb.",
               ul("Only FY 2025-26 affected, and the schedule omission is the only issue: a revised return may be enough.",
                  "Earlier years affected, especially with assets above INR 20 lakh (other than immovable property) where Black Money Act penalties of INR 10 lakh per year can apply: FAST-DS gives certainty.",
                  "Untaxed money abroad: compare 60% under Category 1 with tax at 30% plus penalty under the Black Money Act if it is found later.") + SRC_LAW)],
    faqs=[("Is a revised return enough instead of FAST-DS?", "Only for FY 2025-26 and only for that return. It does not cover earlier years or give Black Money Act immunity for them."),
          ("Does ITR-U give immunity for foreign assets?", "No. An updated return adds income with additional tax but does not grant immunity under the Black Money Act; FAST-DS does for declared items."),
          ("Which is cheaper, ITR-U or FAST-DS?", "It depends on the category and years. For an asset bought from taxed income but missing from the schedule, FAST-DS Category 2 is a flat INR 1 lakh."),
          ("Can BQP compare the routes for me?", "Yes. " + CONTACT)],
    related=[("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"), ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised return: free until 31 December 2026, fee until 31 March 2027")],
    cta_h="Pick the right route before 31 December", cta_b=CONTACT,
    keywords="FAST-DS vs ITR-U, FAST-DS vs revised return, updated return foreign assets, revised return Schedule FA missed, which is better FAST-DS or ITR-U, Black Money Act immunity FAST-DS",
    desc="FAST-DS 2026 vs revised return vs updated return (ITR-U) for missed foreign assets: years covered, cost, Black Money Act immunity (only FAST-DS, section 139) and when each route makes sense.",
    howto=None))

# 6. If you do not declare
PAGES.append(dict(
    slug="fast-ds-what-happens-if-i-do-not-declare-black-money-act",
    title="What Happens If I Do Not Declare Foreign Assets Under FAST-DS? Black Money Act Exposure",
    em="tax, penalty and prosecution risk.",
    kicker="/ FAST-DS 2026 &middot; Risk &middot; Updated 2026-11-04",
    lead="If undisclosed foreign assets or income are found later, the Black Money Act applies: tax at 30% on the value of the undisclosed asset or income, a penalty equal to three times that tax, a separate penalty of INR 10 lakh for failing to disclose a foreign asset in the return (for assets other than immovable property, only where the aggregate value exceeds INR 20 lakh), and possible prosecution. The Department already receives foreign account data and has been emailing taxpayers. FAST-DS 2026 costs 60% or INR 1 lakh and gives immunity. " + DEADLINE,
    sections=[("/ Compare", "Declare now or risk later.",
               "<table><thead><tr><th></th><th>FAST-DS 2026</th><th>If found later (Black Money Act)</th></tr></thead><tbody>"
               "<tr><td>Untaxed foreign asset</td><td>60% of value (Category 1, up to INR 1 crore)</td><td>30% tax + penalty of three times the tax, and possible prosecution</td></tr>"
               "<tr><td>Asset from taxed income, not in the schedule</td><td>INR 1 lakh (Category 2, up to INR 5 crore)</td><td>Penalty of INR 10 lakh for non-disclosure in the return, where the INR 20 lakh threshold is crossed</td></tr></tbody></table>"
               + cta_box("Received the Department's foreign assets email?")),
              ("/ Notes", "Read before deciding.",
               ul("Penalties under the Black Money Act are imposed by order and can be contested; tribunals have taken different views on the INR 10 lakh penalty for genuine omissions.",
                  "The INR 20 lakh threshold for the non-disclosure penalty applies from 1 October 2024 and excludes immovable property.",
                  "FAST-DS immunity covers declared items for years up to 2025-26 only; anything not declared stays exposed.") + SRC_LAW +
               '<p>See also: <a href="income-tax-email-foreign-assets-fast-ds-what-to-do.html">what the Department\'s FAST-DS email means</a>.</p>')],
    faqs=[("What if I ignore FAST-DS?", "Undisclosed foreign assets or income found later can attract 30% tax, a penalty of three times that tax and possible prosecution under the Black Money Act; non-disclosure in the return can attract a separate INR 10 lakh penalty where the threshold is crossed."),
          ("Is there a penalty for small foreign accounts?", "The INR 10 lakh non-disclosure penalty does not apply where the aggregate value of foreign assets, other than immovable property, is INR 20 lakh or less (from 1 October 2024). Tax on undisclosed income still applies."),
          ("Can BQP advise whether to declare?", "Yes. " + CONTACT)],
    related=[("income-tax-email-foreign-assets-fast-ds-what-to-do.html", "FAST-DS email: what to do"), ("fast-ds-2026-filing-help-chartered-accountant.html", "FAST-DS filing help")],
    cta_h="Decide before 31 December 2026", cta_b=CONTACT,
    keywords="what if I do not declare FAST-DS, Black Money Act penalty foreign assets, 10 lakh penalty Schedule FA, undisclosed foreign assets penalty India, FAST-DS not filed consequences",
    desc="Not declaring under FAST-DS 2026: if found later, the Black Money Act applies (30% tax, penalty of three times the tax, INR 10 lakh non-disclosure penalty above the INR 20 lakh threshold, prosecution). FAST-DS costs 60% or INR 1 lakh with immunity.",
    howto=None))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print(f"Batch AZ complete: {len(PAGES)} FAST-DS pages")
