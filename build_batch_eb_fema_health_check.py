# -*- coding: utf-8 -*-
"""Batch EB (20 Nov 2026): FEMA health check for foreign-owned Indian companies - eight yes / no / not applicable
questions (allotment within 60 days, FC-GPR 30 days, valuation, FC-TRS 60 days, FLA 15 July, Form DI 30 days, ECB LRN
and ECB 2, sector cap and Press Note 3) with fix routes (late submission fee within three years of the due date,
otherwise compounding). Call-first tool. Logic: tools/fema-health-logic.js (node tools/fema-health-logic.test.js, 6 tests).
Facts: NDI Rules and reporting regulations - allot within 60 days of receipt or refund within 15 days; FC-GPR within 30
days of allotment; FC-TRS within 60 days; FLA by 15 July; Form DI within 30 days; ECB LRN before drawdown and ECB 2
returns; late submission fee INR 7,500 plus 0.025% of the amount per year of delay for reporting delays within three years
of the due date, otherwise compounding (site pages)."""
import re, json
from urllib.parse import quote
from build_lib import page, write_page, DOMAIN
import advisory_lib as A
from advisory_lib import ul, call_box

A.UPDATED = "Last updated: 20 November 2026."
UPDATED = A.UPDATED

LOGIC = open("tools/fema-health-logic.js", encoding="utf-8").read().replace(
    'if (typeof module !== "undefined") module.exports = { femaHealth: femaHealth, FEMA_CHECKS: FEMA_CHECKS };', "")
_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += ("\n  .calc-embed .calc-main{padding:0;max-width:none}\n  .calc-embed .rtrace{margin:8px 0 0;padding-left:18px;font-size:13px;line-height:1.55}\n"
             "  .calc-embed .rtrace li{margin:0 0 6px}\n  .calc-embed .result-card .rtrace strong,.calc-embed .result-card .rtrace b{color:#fff}\n"
             "  .calc-embed .fq{margin:0 0 14px;font-size:14px;line-height:1.45}\n  .calc-embed .fq select{display:block;margin-top:6px;width:100%;padding:8px;border:1px solid var(--line);border-radius:8px;font:inherit}\n")
SLUG = "fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026"
wa = "https://wa.me/917801887130?text=" + quote("Hi Durgesh, I ran your FEMA health check for our Indian company and want to fix the gaps.")
JS = LOGIC + r'''
(function(){
  var box=document.getElementById("fQs");
  box.innerHTML=FEMA_CHECKS.map(function(c){return '<div class="fq"><label for="f_'+c.id+'">'+c.text+'</label><select id="f_'+c.id+'"><option value="">Choose</option><option value="yes">Yes</option><option value="no">No / not sure</option><option value="na">Not applicable</option></select></div>';}).join("");
  function show(){
    var a={}; FEMA_CHECKS.forEach(function(c){a[c.id]=document.getElementById("f_"+c.id).value;});
    var r=femaHealth(a), out=document.getElementById("fOut"), list=document.getElementById("fList");
    var label={unanswered:"Answer the questions",clean:"No gaps on these answers",fixable:r.count+" gap(s): usually fixable with late fees",serious:r.count+" gap(s), including ones that need compounding or approval"}[r.status];
    out.textContent=label;
    var items=[];
    if(r.status==="clean") items.push("Keep the filings calendar going: FLA every year by 15 July, FC-GPR within 30 days of each allotment.");
    r.gaps.forEach(function(g){items.push(g.fix);});
    if(r.count) items.push("Fix gaps before a fundraise, sale, dividend or audit: buyers and banks check FEMA history.");
    items.push("Screening only; the fix route depends on dates and amounts.");
    list.innerHTML=items.map(function(e){return "<li>"+e+"</li>";}).join("");
  }
  FEMA_CHECKS.forEach(function(c){document.getElementById("f_"+c.id).addEventListener("change",show);});
  show();
})();'''
app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "FEMA Health Check for Foreign-Owned Indian Companies",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "BusinessApplication", "operatingSystem": "Any",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "description": "Eight-question check of FEMA filings (FC-GPR, FC-TRS, FLA, Form DI, ECB, valuation, sector caps) with fix routes.",
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"}}
CALC = (f"<style>{CALC_CSS}</style><script type=\"application/ld+json\">{json.dumps(app, separators=(',', ':'))}</script>"
        '<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Your company&rsquo;s FEMA record</h2><p class="sub">Answer for every foreign investment since incorporation.</p><div id="fQs"></div></div>'
        '<div class="result-card"><div class="rlabel">Result</div><div class="rvalue red" id="fOut" style="font-size:22px;line-height:1.3">-</div>'
        '<ul class="rtrace" id="fList"></ul>'
        f'<p style="font-size:13px;margin:14px 0 0"><a href="{wa}" target="_blank" rel="noopener">Fix the gaps with CA Durgesh Chavda &rarr;</a></p></div></div></div>'
        f"<script>{JS}\n</script>")
CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with the company name, a list of foreign investments and transfers with dates, and what was filed. "
           "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")

PAGES = [dict(
    slug=SLUG,
    title="FEMA Health Check for Foreign-Owned Indian Companies (2026): FC-GPR, FC-TRS, FLA, Form DI, ECB and Valuation Gaps, and How to Fix Them",
    em="find missed FEMA filings before a buyer, investor or bank does.",
    kicker="/ Tool &middot; Foreign-owned companies &middot; FEMA &middot; Updated 2026-11-20",
    lead=("Every Indian company with foreign investment carries a FEMA filing history, and gaps surface at the worst moments: a fundraise, a sale, a dividend or a bank's KYC review. The core obligations are to allot shares within <strong>60 days</strong> of receiving foreign money, file <strong>FC-GPR within 30 days</strong> of allotment and <strong>FC-TRS within 60 days</strong> of a transfer, file the <strong>FLA return by 15 July every year</strong>, file <strong>Form DI within 30 days</strong> of a downstream investment, register foreign loans (<strong>ECB</strong>) before drawdown, and keep a <strong>fair-value report</strong> for every issue or transfer. "
          "Reporting delays within three years of the due date are usually settled with a <strong>late submission fee</strong> (INR 7,500 plus 0.025% of the amount for each year). Older delays and substantive breaches go to <strong>compounding</strong> with the RBI. Run the check below, then book a call to plan the clean-up."),
    sections=[
        ("/ Health check", "Eight questions.", CALC
         + call_box("our company's FEMA compliance", ["Which gaps exist, by investment and date",
                                                      "Late submission fee or compounding for each, and the order to fix them",
                                                      "Documents the bank and RBI will ask for",
                                                      "Timing against a fundraise, sale or dividend",
                                                      "A filing calendar so it does not recur"],
                    "a list of foreign investments, transfers and loans with dates, and copies of filings made.")),
        ("/ What each check covers", "And why it matters.",
         ul("<strong>Allotment within 60 days:</strong> money not allotted or refunded in time is a contravention.",
            "<strong>FC-GPR and FC-TRS:</strong> reporting of issues and transfers on the RBI FIRMS portal; see <a href=\"form-fc-gpr-filing-checklist-india-2026.html\">FC-GPR checklist</a> and <a href=\"form-fc-trs-filing-checklist-india-2026.html\">FC-TRS checklist</a>.",
            "<strong>Valuation:</strong> fair-value report for every issue or transfer with a non-resident; see <a href=\"fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html\">FEMA valuation report</a>.",
            "<strong>FLA return:</strong> annual, by 15 July, for every company with foreign investment; see <a href=\"fla-return-foreign-liabilities-assets-rbi-india.html\">FLA return</a>.",
            "<strong>Form DI:</strong> for downstream investment by a foreign-owned company; see <a href=\"downstream-investment-india-foreign-owned-company-fema-form-di-funding-rules-2026.html\">downstream investment</a>.",
            "<strong>ECB:</strong> LRN before drawdown and ECB 2 returns; see <a href=\"loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules.html\">loans from foreign shareholders</a>.",
            "<strong>Sector caps and approvals:</strong> including Press Note 3 for land-border investors; see <a href=\"press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html\">Press Note 2 (2026)</a>.")
         + '<p>Read more: <a href="fema-compounding-foreign-subsidiary-india.html">FEMA compounding</a> &middot; <a href="foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html">subsidiary compliance calendar</a> &middot; <a href="sell-side-due-diligence-india-selling-indian-company-to-foreign-buyer-2026.html">sell-side due diligence</a>.</p>'
         f'<p><strong>Sources:</strong> Foreign Exchange Management (Non-Debt Instruments) Rules, 2019; Mode of Payment and Reporting of Non-Debt Instruments Regulations; Borrowing and Lending Regulations as amended in 2026; RBI Master Directions on foreign investment, reporting and compounding. <em>{UPDATED}</em> Screening tool only, not advice for your situation.</p>'),
    ],
    faqs=[("What FEMA filings does a foreign-owned Indian company need?", "FC-GPR within 30 days of each allotment, FC-TRS within 60 days of transfers with residents, the FLA return by 15 July every year, Form DI for downstream investment, ECB registration and returns for foreign loans, and a fair-value report for each issue or transfer."),
          ("What happens if FC-GPR was filed late?", "Delays within three years of the due date are usually regularised with a late submission fee of INR 7,500 plus 0.025% of the amount per year; longer delays go to compounding."),
          ("What if shares were not allotted within 60 days?", "Holding foreign money beyond 60 days without allotment or refund within 15 days is a contravention, generally regularised through compounding with the RBI."),
          ("Is the FLA return needed every year?", "Yes, by 15 July each year for every company that has received foreign direct investment or made overseas investment, even if nothing new happened."),
          ("When should FEMA gaps be fixed?", "Before a fundraise, sale, dividend repatriation or bank review, because buyers and banks check the FEMA history."),
          ("Can BQP clean up our FEMA record?", "Yes. " + CONTACT)],
    related=[("fema-compounding-foreign-subsidiary-india.html", "FEMA compounding"), ("form-fc-gpr-filing-checklist-india-2026.html", "FC-GPR checklist"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar")],
    cta_h="Not sure your FEMA record is clean?", cta_b=CONTACT,
    keywords="FEMA health check, FEMA compliance check foreign subsidiary India, FC-GPR late filing fee, late submission fee FEMA 7500, FLA return 15 July missed, FEMA compounding foreign owned company, Form DI late, allotment 60 days FEMA",
    desc="FEMA health check for foreign-owned Indian companies (2026): eight questions on allotment within 60 days, FC-GPR, valuation, FC-TRS, FLA, Form DI, ECB and sector caps, with fix routes (late submission fee within three years, otherwise compounding).",
    howto={"name": "How a foreign-owned Indian company checks and fixes its FEMA record", "description": "Screen, then regularise.", "steps": [
        {"name": "List every foreign transaction", "text": "Issues, transfers, loans and downstream investments with dates."},
        {"name": "Run the health check", "text": "Answer the eight questions for each transaction."},
        {"name": "Classify the gaps", "text": "Late submission fee within three years, otherwise compounding or approval."},
        {"name": "File and regularise", "text": "Through the AD bank and RBI, in the right order."},
        {"name": "Set a calendar", "text": "FLA every 15 July and event-based filings within their windows."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EB complete")
