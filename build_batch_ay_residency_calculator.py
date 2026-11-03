# -*- coding: utf-8 -*-
"""Batch AY: Residential status calculator (Income-tax Act 1961 s.6 for FY 2025-26; Income-tax Act 2025 s.6 from tax year 2026-27).
Logic lives in tools/residential-status-logic.js and is tested by tools/residential-status-logic.test.js (node)."""
import json
import re
from build_lib import page, write_page

DOMAIN = "https://bharatquantumprospera.com"
CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "residential-status-calculator-india-nri-rnor-section-6"

_lrs = open("lrs-tcs-calculator.html", encoding="utf-8").read()
CALC_CSS = re.sub(r"\.calc-hero[^\n]*\n", "", re.search(r"<style>(.*?)</style>", _lrs, re.S).group(1))
CALC_CSS += """
  .calc-embed .calc-main{padding:0;max-width:none}
  .calc-embed .rtrace{margin:14px 0 0;padding-left:18px;font-size:13px;line-height:1.55}
  .calc-embed .rtrace li{margin:0 0 6px}
  .calc-embed .rerr{color:#C2312A;font-size:14px}
  .stays-row{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 8px}
  .stays-row input{flex:1 1 140px}
  .statute{font-size:14px;line-height:1.6}
  .statute details{border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:0 0 12px}
  .statute summary{cursor:pointer;font-weight:600}
  .statute p{margin:8px 0}
"""

LOGIC = open("tools/residential-status-logic.js", encoding="utf-8").read()
LOGIC = LOGIC.replace('if (typeof module !== "undefined") module.exports = { residency: residency, countDaysInYear: countDaysInYear };', "")


def field(fid, label, hint, ctrl):
    return f'<div class="field"><label for="{fid}">{label} <span class="hint">{hint}</span></label>{ctrl}</div>'


def sel(fid, opts):
    return f'<select id="{fid}">' + "".join(f'<option value="{v}">{t}</option>' for v, t in opts) + "</select>"


def numin(fid, val, mx):
    return f'<input id="{fid}" type="number" min="0" max="{mx}" step="1" value="{val}" inputmode="numeric" />'


INPUTS = (
    field("rAct", "Year", "The 1961 Act applies up to FY 2025-26; the 2025 Act from tax year 2026-27.",
          sel("rAct", [("2025", "Tax year 2026-27 onwards (Income-tax Act, 2025)"), ("1961", "FY 2025-26 or earlier, from FY 2020-21 (Income-tax Act, 1961)")]))
    + field("rDays", "Days in India in this year", "1 April to 31 March. Count the arrival and departure days.", numin("rDays", 120, 366))
    + '<details style="margin:-6px 0 14px"><summary style="cursor:pointer;font-size:13px">Count days from travel dates</summary>'
      '<div id="rStays" style="margin-top:10px"></div>'
      '<p style="font-size:12px;margin:4px 0 8px">Enter each stay in India (arrival and departure). Leave departure empty if you were still in India at 31 March. Financial year starting in April of: '
      '<input id="rFy" type="number" min="2015" max="2035" value="2026" style="width:90px" /></p>'
      '<button type="button" id="rAddStay" style="margin-right:8px">Add a stay</button><button type="button" id="rUseCount">Use the count</button> <span id="rCountOut" style="font-size:13px;margin-left:8px"></span></details>'
    + field("rDays4", "Days in India in the 4 preceding years", "Total for the four years before this year.", numin("rDays4", 400, 1461))
    + field("rCit", "Citizenship", "Person of Indian origin: you, a parent or a grandparent was born in undivided India (1961 Act: Explanation to section 115C(e)).",
            sel("rCit", [("citizen", "Citizen of India"), ("pio", "Person of Indian origin (not a citizen)"), ("foreign", "Neither")]))
    + field("rCat", "Your situation this year", "Pick the one that describes this year.",
            sel("rCat", [("visiting", "I live outside India and came to India on a visit"), ("leaving", "I left India this year for employment abroad, or as crew of an Indian ship"), ("other", "Neither of these")]))
    + field("rInc", "Total income other than income from foreign sources above INR 15 lakh?", "Income from foreign sources: income accruing or arising outside India, except from a business controlled in or a profession set up in India, and not deemed to accrue or arise in India.",
            sel("rInc", [("no", "No (INR 15 lakh or less)"), ("yes", "Yes (more than INR 15 lakh)")]))
    + field("rAbroad", "Liable to tax in another country or territory by reason of domicile, residence or similar criteria?", "Used only for the deemed-resident rule for citizens.",
            sel("rAbroad", [("yes", "Yes"), ("no", "No")]))
    + field("rNr10", "Of the 10 preceding years, how many were you a non-resident?", "Count only years of non-resident status (RNOR years are resident years).", numin("rNr10", 10, 10))
    + field("rDays7", "Days in India in the 7 preceding years", "Total for the seven years before this year.", numin("rDays7", 300, 2557))
)

JS = LOGIC + r'''
(function(){
  function $(id){return document.getElementById(id);}
  function addStay(f,t){var d=document.createElement("div");d.className="stays-row";d.innerHTML='<input type="date" class="sFrom" aria-label="Arrival date"><input type="date" class="sTo" aria-label="Departure date">';d.querySelector(".sFrom").value=f||"";d.querySelector(".sTo").value=t||"";$("rStays").appendChild(d);}
  addStay();addStay();
  $("rAddStay").addEventListener("click",function(){addStay();});
  $("rUseCount").addEventListener("click",function(){
    var rows=[].slice.call(document.querySelectorAll("#rStays .stays-row")).map(function(r){return {from:r.querySelector(".sFrom").value,to:r.querySelector(".sTo").value};});
    var fy=parseInt($("rFy").value,10); if(!fy){$("rCountOut").textContent="Enter the year.";return;}
    var n=countDaysInYear(rows,fy); $("rDays").value=n; $("rCountOut").textContent=n+" days in FY "+fy+"-"+String(fy+1).slice(2)+"."; calc();
  });
  function intval(id){var v=$(id).value.trim();return v===""?NaN:Number(v);}
  function calc(){
    var cit=$("rCit").value;
    var r=residency({act:$("rAct").value,days:intval("rDays"),days4:intval("rDays4"),citizen:cit==="citizen",pio:cit==="pio",category:$("rCat").value,
      incomeOver15L:$("rInc").value==="yes",liableAbroad:$("rAbroad").value==="yes",nrYears10:intval("rNr10"),days7:intval("rDays7")});
    var out=$("rStatus"),hint=$("rStatusHint"),tr=$("rTrace");
    if(!r.ok){out.textContent="Check inputs";hint.textContent="";tr.innerHTML=r.errors.map(function(e){return '<li class="rerr">'+e+'</li>';}).join("");return;}
    out.textContent=r.status;hint.textContent=r.label;
    tr.innerHTML=r.trace.map(function(t){return "<li>"+t+"</li>";}).join("");
  }
  ["rAct","rDays","rDays4","rCit","rCat","rInc","rAbroad","rNr10","rDays7"].forEach(function(id){$(id).addEventListener("input",calc);$(id).addEventListener("change",calc);});
  calc();
})();'''

app = {"@context": "https://schema.org", "@type": "WebApplication", "name": "Residential Status Calculator (India, Section 6)",
       "url": f"{DOMAIN}/{SLUG}.html", "applicationCategory": "FinanceApplication", "operatingSystem": "Any",
       "description": "Determines whether an individual is Resident and Ordinarily Resident, Resident but Not Ordinarily Resident, or Non-resident under section 6 of the Income-tax Act, 1961 (FY 2025-26) and the Income-tax Act, 2025 (tax year 2026-27 onwards).",
       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "INR"},
       "author": {"@type": "Person", "name": "CA Durgesh Chavda", "url": f"{DOMAIN}/durgesh.html"},
       "publisher": {"@type": "AccountingService", "name": "Bharat Quantum Prospera", "url": DOMAIN}}

BLOCK = (f"<style>{CALC_CSS}</style>"
         f'<script type="application/ld+json">{json.dumps(app, separators=(",", ":"), ensure_ascii=False)}</script>'
         f'<div class="calc-embed"><div class="calc-main"><div class="calc-card"><h2>Inputs</h2><p class="sub">Days are whole days in India.</p>{INPUTS}</div>'
         '<div class="result-card"><div class="rlabel">Residential status</div><div class="rvalue red" id="rStatus">-</div><div class="rhint" id="rStatusHint"></div>'
         '<p style="font-size:13px;margin:14px 0 0;font-weight:600">How the law applies to your inputs</p><ol class="rtrace" id="rTrace"></ol></div></div></div>'
         f"<script>{JS}\n</script>")

# Official text, as published by the Income Tax Department (incometaxindia.gov.in), individual-related provisions.
S2025 = [
    "6. (1) For the purposes of this Act, residential status in India in a tax year of a person shall be determined as per the provisions of this section.",
    "(2) An individual shall be resident in India in a tax year, if he— (a) is in India for a total period of one hundred and eighty-two days or more in that tax year; or (b) is in India cumulatively for sixty days or more during that year and has been in India cumulatively for three hundred and sixty-five days or more in the four years preceding such tax year.",
    "(3) The provisions of sub-section (2)(b) shall not apply in the case of an individual who is a citizen of India and leaves India in any tax year— (a) as a member of the crew of an Indian ship, as defined in section 3(18) of the Merchant Shipping Act, 1958 (44 of 1958); or (b) for the purposes of employment outside India.",
    "(4) The provisions of sub-section (2)(b) shall not apply, subject to the provisions of sub-section (5), in the case of an individual— (a) who is a citizen of India or a person of Indian origin; and (b) who being outside India, comes on a visit to India in any tax year.",
    "(5) Where the person referred to in sub-section (4) has a total income exceeding fifteen lakh rupees during the tax year referred therein (other than the income from foreign sources), sub-section (2)(b) shall apply as if the words “sixty days” had been substituted with “one hundred and twenty days”.",
    "(6) For the purposes of sub-section (2), if the individual is— (a) a citizen of India; and (b) a member of the crew of a foreign-bound ship leaving India, the total number of days in India, in respect of that voyage, shall be determined in such manner and subject to such conditions, as may be prescribed.",
    "(7) Irrespective of the provisions of sub-sections (2) to (6), an individual shall be deemed to be resident in India for a tax year, if he— (a) is a citizen of India; (b) is not liable to tax in any other country or territory due to his domicile, residence, or similar criteria; and (c) has total income exceeding fifteen lakh rupees during such tax year (other than the income from foreign sources).",
    "(8) Sub-section (7) shall not apply to an individual, who is resident in India for a tax year under sub-sections (2) to (6).",
    "(12) If a person is resident in India in a tax year for any source of income, he shall be deemed to be resident in India in that tax year for each of his other sources of income.",
    "(13) A person is not ordinarily resident in India in any tax year, if that person is— (a) an individual who has been, or a Hindu undivided family, whose manager has been— (i) a non-resident in India in nine out of the ten tax years preceding that year; or (ii) in India cumulatively for seven hundred and twenty-nine days or less in seven tax years preceding that year; or (b) a citizen of India or a person of Indian origin,— (i) whose total income excluding income from foreign sources exceeds fifteen lakh rupees during the tax year, as mentioned in sub-section (5); and (ii) who has been in India cumulatively for one hundred and twenty days or more but less than one hundred and eighty-two days during the tax year; or (c) a citizen of India who is deemed to be resident in India under sub-section (7).",
    "(14) For the purposes of this section, “income from foreign sources” means the income, which accrues or arises outside India (except income derived from a business controlled in or a profession set up in India) and which is not deemed to accrue or arise in India.",
]
S1961 = [
    "6. For the purposes of this Act,— (1) An individual is said to be resident in India in any previous year, if he— (a) is in India in that year for a period or periods amounting in all to one hundred and eighty-two days or more; or (b) [***] (c) having within the four years preceding that year been in India for a period or periods amounting in all to three hundred and sixty-five days or more, is in India for a period or periods amounting in all to sixty days or more in that year.",
    "Explanation 1.—In the case of an individual,— (a) being a citizen of India, who leaves India in any previous year as a member of the crew of an Indian ship as defined in clause (18) of section 3 of the Merchant Shipping Act, 1958 (44 of 1958), or for the purposes of employment outside India, the provisions of sub-clause (c) shall apply in relation to that year as if for the words \"sixty days\", occurring therein, the words \"one hundred and eighty-two days\" had been substituted; (b) being a citizen of India, or a person of Indian origin within the meaning of Explanation to clause (e) of section 115C, who, being outside India, comes on a visit to India in any previous year, the provisions of sub-clause (c) shall apply in relation to that year as if for the words \"sixty days\", occurring therein, the words \"one hundred and eighty-two days\" had been substituted and in case of such person having total income, other than the income from foreign sources, exceeding fifteen lakh rupees during the previous year, for the words \"sixty days\" occurring therein, the words \"one hundred and twenty days\" had been substituted.",
    "Explanation 2.—For the purposes of this clause, in the case of an individual, being a citizen of India and a member of the crew of a foreign bound ship leaving India, the period or periods of stay in India shall, in respect of such voyage, be determined in the manner and subject to such conditions as may be prescribed.",
    "(1A) Notwithstanding anything contained in clause (1), an individual, being a citizen of India, having total income, other than the income from foreign sources, exceeding fifteen lakh rupees during the previous year shall be deemed to be resident in India in that previous year, if he is not liable to tax in any other country or territory by reason of his domicile or residence or any other criteria of similar nature.",
    "Explanation.—For the removal of doubts, it is hereby declared that this clause shall not apply in case of an individual who is said to be resident in India in the previous year under clause (1).",
    "(6) A person is said to be \"not ordinarily resident\" in India in any previous year if such person is— (a) an individual who has been a non-resident in India in nine out of the ten previous years preceding that year, or has during the seven previous years preceding that year been in India for a period of, or periods amounting in all to, seven hundred and twenty-nine days or less; or (b) a Hindu undivided family whose manager has been a non-resident in India in nine out of the ten previous years preceding that year, or has during the seven previous years preceding that year been in India for a period of, or periods amounting in all to, seven hundred and twenty-nine days or less; or (c) a citizen of India, or a person of Indian origin, having total income, other than the income from foreign sources, exceeding fifteen lakh rupees during the previous year, as referred to in clause (b) of Explanation1 to clause (1), who has been in India for a period or periods amounting in all to one hundred and twenty days or more but less than one hundred and eighty-two days; or (d) a citizen of India who is deemed to be resident in India under clause (1A).",
    "Explanation.—For the purposes of this section, the expression \"income from foreign sources\" means income which accrues or arises outside India (except income derived from a business controlled in or a profession set up in India) and which is not deemed to accrue or arise in India.",
]


def statute(title, paras, url):
    return (f'<details><summary>{title}</summary>' + "".join(f"<p>{p}</p>" for p in paras)
            + f'<p><em>Source: <a href="{url}" rel="nofollow noopener" target="_blank">Income Tax Department, incometaxindia.gov.in</a>. Sub-sections on HUFs, firms and companies are omitted here.</em></p></details>')


TABLE = ("<table><thead><tr><th>Status</th><th>When (individuals)</th></tr></thead><tbody>"
         "<tr><td><strong>Resident</strong></td><td>182 days or more in India in the year; or 60 days or more in the year and 365 days or more in the 4 preceding years (the 60-day limit does not apply to a citizen leaving India for employment abroad, and to a citizen or person of Indian origin on a visit it does not apply unless income other than foreign-source income exceeds INR 15 lakh, when it becomes 120 days).</td></tr>"
         "<tr><td><strong>Deemed resident</strong></td><td>A citizen, not resident under the day tests, with income other than foreign-source income above INR 15 lakh, who is not liable to tax in any other country or territory by reason of domicile, residence or similar criteria. Always RNOR.</td></tr>"
         "<tr><td><strong>RNOR</strong></td><td>A resident who was a non-resident in 9 of the 10 preceding years, or was in India 729 days or less in the 7 preceding years; or a citizen/person of Indian origin on a visit with income above INR 15 lakh who is in India 120 to 181 days; or a deemed resident.</td></tr>"
         "<tr><td><strong>ROR</strong></td><td>A resident who is not RNOR.</td></tr>"
         "<tr><td><strong>Non-resident</strong></td><td>Anyone who is not resident or deemed resident.</td></tr></tbody></table>")

sections = [
    ("/ Calculator", "Find your residential status.", BLOCK),
    ("/ The rules in one table", "Section 6, individuals.", TABLE +
     "<p>The 1961 Act (section 6) and the 2025 Act (section 6) apply the same tests with different numbering; the calculator cites the provisions of the Act you select.</p>"),
    ("/ Counting days", "Get the inputs right.",
     "<ul><li>Count every day you were in India in the year (1 April to 31 March), including the day of arrival and the day of departure. Use your passport stamps or travel records.</li>"
     "<li>\"Preceding years\" means the 4, 7 or 10 financial years immediately before the year being tested.</li>"
     "<li>For a citizen who is a crew member of a foreign-bound ship, the days are determined in the manner prescribed by the rules (Explanation 2 to section 6(1) of the 1961 Act; section 6(6) of the 2025 Act); enter the days after applying them.</li>"
     "<li>\"Income from foreign sources\" is income accruing or arising outside India, except income from a business controlled in or a profession set up in India, and not deemed to accrue or arise in India.</li></ul>"),
    ("/ The law, word for word", "Official text of section 6 for individuals.",
     '<div class="statute">'
     + statute("Income-tax Act, 2025, section 6 (tax year 2026-27 onwards)", S2025, "https://wm.incometaxindia.gov.in/w/section-6-1")
     + statute("Income-tax Act, 1961, section 6 (as applicable to FY 2025-26)", S1961, "https://wm.incometaxindia.gov.in/w/section-6-66")
     + "</div><p><em>Last updated: 3 November 2026. This calculator applies section 6 only. Where you are also resident in another country, the tie-breaker in the relevant tax treaty decides treaty residence; that needs separate analysis.</em></p>"),
]

faqs = [
    ("How is residential status determined for an individual in India?", "Under section 6, you are resident if you are in India for 182 days or more in the year, or for 60 days or more in the year and 365 days or more in the 4 preceding years. The 60-day limit is replaced for citizens leaving India for employment abroad and for citizens or persons of Indian origin visiting India. A resident is RNOR if non-resident in 9 of the 10 preceding years or in India 729 days or less in the 7 preceding years."),
    ("What is the 120-day rule for NRIs?", "A citizen of India or person of Indian origin who lives outside India and visits India is resident under the 60-day test only if income other than foreign-source income exceeds INR 15 lakh, and then the 60 days become 120 days (with 365 days in the 4 preceding years). Such a person in India for 120 to 181 days is RNOR."),
    ("What is a deemed resident?", "A citizen of India with income other than foreign-source income above INR 15 lakh who is not liable to tax in any other country or territory by reason of domicile, residence or similar criteria, and who is not resident under the day tests. A deemed resident is always RNOR."),
    ("Does the 2025 Act change residential status rules?", "The tests are the same; the provisions are renumbered. Section 6(2) to (8) and 6(13) of the Income-tax Act, 2025 correspond to section 6(1), its Explanations, 6(1A) and 6(6) of the 1961 Act, and apply from tax year 2026-27."),
    ("Are the arrival and departure days counted?", "Count both as days in India; the calculator's travel-date counter does this."),
    ("Can BQP confirm my residential status?", "Yes, including treaty tie-breaker analysis and the effect on your return. " + CONTACT),
]

html = page(slug=SLUG,
            title="Residential Status Calculator India: NRI, RNOR or Resident Under Section 6 (1961 and 2025 Acts)",
            description="Free residential status calculator for individuals under section 6 of the Income-tax Act, 1961 (FY 2025-26) and the Income-tax Act, 2025 (tax year 2026-27): 182-day, 60/120-day and 365-day tests, deemed resident, RNOR. Built from the official statutory text, with a travel-date day counter.",
            keywords="residential status calculator, NRI status calculator India, RNOR calculator, section 6 residential status, 182 days rule calculator, 120 days rule NRI, deemed resident calculator, residential status income tax act 2025",
            hero_kicker="/ Free Tool &middot; Residential Status &middot; Updated 2026-11-03",
            hero_title_html="Residential Status Calculator, <em>NRI, RNOR or resident under section 6.</em>",
            hero_lead="Enter your days in India and a few facts, and the calculator applies section 6 of the Income-tax Act, 1961 (FY 2025-26) or the Income-tax Act, 2025 (tax year 2026-27 onwards) exactly as written: the 182-day test, the 60-day test with the 120-day and 182-day substitutions, deemed residence for citizens, and the RNOR tests. It shows which provision decided each step, and the official text is reproduced below.",
            sections=sections, faqs=faqs,
            related=[("nri-residential-status-rnor-india.html", "Related", "NRI residential status and RNOR"),
                     ("nri-returning-india-tax-rnor-transition.html", "Related", "Returning to India: RNOR planning")],
            cta_headline="Want your residential status confirmed?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AY complete")
