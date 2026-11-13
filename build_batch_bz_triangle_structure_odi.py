# -*- coding: utf-8 -*-
"""Batch BZ (13 Nov 2026): the "triangular" structure (Indian resident founders -> US/Delaware parent -> Indian
subsidiary) under the FEMA Overseas Investment Rules, 2022.
Facts: Schedule III general permission lets a resident individual make ODI only in an operating foreign entity not
engaged in financial services and which does not have a subsidiary or step-down subsidiary where the resident individual
has control in the foreign entity; control (rule 2(1)(c)) includes 10% or more of voting rights, the right to appoint a
majority of directors or control of management or policy decisions; outside the general permission, approval is needed.
Rule 19(3): no financial commitment in a foreign entity that has invested or invests into India resulting in more than two
layers of subsidiaries. An Indian company can make ODI under Schedule I subject to the two-layer limit. Resident
individuals' ODI counts within the LRS limit of USD 250,000 per financial year; annual performance report by 31 December;
foreign shares go in Schedule FA. Share swaps in a flip are taxable for Indian shareholders (12.5% LTCG on unlisted shares
transferred from 23 July 2024 if held over 24 months). Angel tax (section 56(2)(viib)) does not apply from AY 2025-26."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 13 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the cap table of both companies and the dates shares were issued. "
           "We reply the same working day with what the structure needs and a fixed-scope quote.")
SLUG = "triangular-structure-indian-founders-us-parent-indian-subsidiary-odi-schedule-iii-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Already set up this way?</p>'
       f'<p style="margin:0">Many founders discover the issue during fundraising or acquisition due diligence. Fixing it earlier, with the bank and RBI, is far cheaper than fixing it with an investor waiting. '
       f'<a href="{wa("Hi Durgesh, we are Indian resident founders with a US parent and an Indian subsidiary. Can you check our ODI position?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="The Triangular Structure: Indian Founders, a US Parent and an Indian Subsidiary Under FEMA's Overseas Investment Rules (2026)",
    em="the rule most founder diagrams leave out.",
    kicker="/ Indian founders &middot; US incorporation &middot; FEMA ODI &middot; Updated 2026-11-13",
    lead=("The structure most Indian startups copy is a triangle: founders living in India own a Delaware (or other US) parent, and the parent owns the Indian operating company. "
          "Under the FEMA Overseas Investment Rules, 2022, a resident individual's general permission covers only an operating foreign company <strong>that has no subsidiary or step-down subsidiary where the individual has control</strong>, and control starts at 10% of the votes, board control or control of management. "
          "So a founder-controlled US parent that owns an Indian company usually falls outside the automatic route and needs approval. Separately, the round-tripping rule allows no more than two layers of subsidiaries."),
    sections=[
        ("/ The three legs of the triangle", "And the rule on each.",
         table(["Leg", "What it is", "FEMA position"], [
             ["Founders (resident in India) &rarr; US parent", "Overseas direct investment (ODI) by a resident individual, within the LRS limit of USD 250,000 a year", "General permission only if the US company has no subsidiary or step-down subsidiary in which the founder has control; otherwise approval"],
             ["US parent &rarr; Indian subsidiary", "Foreign direct investment (FDI) into India", "Automatic route for most sectors; Form FC-GPR within 30 days of allotment"],
             ["The whole structure", "Money from India going out and coming back", "Round-tripping test: no more than two layers of subsidiaries (rule 19(3))"]])
         + BOX),
        ("/ What founders can do", "Options, in order of simplicity.",
         ul("<strong>Seek approval up front:</strong> where the founders will hold control in the US parent that owns the Indian company, apply for approval through the authorised dealer bank before investing or swapping shares.",
            "<strong>Indian company as the parent:</strong> an Indian company can set up a US subsidiary under the general route for Indian entities (Schedule I), within the two-layer limit, which avoids the individual-control restriction.",
            "<strong>Build in India first, flip later if investors insist:</strong> many founders now keep the Indian company as the parent and only flip when a lead investor requires it, with the FEMA and tax costs priced in.",
            "<strong>Already in a triangle?</strong> Map every share issue and transfer, check what was reported, and regularise with the bank and RBI (late submission fees or compounding) before a fundraise or exit.")
         + '<p>Related: <a href="fema-odi-us-entity-indian-founder.html">FEMA ODI for Indian founders</a> &middot; <a href="form-odi-apr-annual-performance-report-india-2026.html">annual performance report</a> &middot; <a href="reverse-flip-india-fast-track-inbound-merger-section-233-rbi-tax-2026.html">reverse flip by fast-track merger</a>.</p>'),
        ("/ Other points in the same structure", "Founders ask about these too.",
         ul("<strong>Flip share swap:</strong> taxable for Indian shareholders (12.5% on long-term gains on unlisted shares held over 24 months, at fair value); see the <a href=\"flip-tax-impact-calculator.html\">flip tax calculator</a>.",
            "<strong>Place of effective management:</strong> if the US company is run entirely from India, it can be treated as resident in India.",
            "<strong>Transfer pricing:</strong> the Indian subsidiary charges the US parent cost plus a margin; from tax year 2026-27 a 15.5% safe harbour can apply. See <a href=\"gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html\">the 2026 safe harbour</a>.",
            "<strong>Angel tax:</strong> no longer applies to share issues from assessment year 2025-26 onwards.",
            "<strong>Founders' own returns:</strong> the US shares go in Schedule FA every year, and the annual performance report is due by 31 December.")
         + f'<p><strong>Sources:</strong> Foreign Exchange Management (Overseas Investment) Rules, 2022, rule 2(1)(c), rule 19(3) and Schedule III; Overseas Investment Directions, 2022; FEMA (Non-debt Instruments) Rules, 2019; Finance (No. 2) Act, 2024. <em>{UPDATED}</em> General information, not advice for your situation; confirm your case with the authorised dealer bank.</p>'),
    ],
    faqs=[("Can Indian resident founders own a US company that owns an Indian subsidiary?", "Not under the general permission if the founders have control in the US company. Schedule III of the Overseas Investment Rules lets a resident individual invest only in a foreign company that has no subsidiary or step-down subsidiary where the individual has control; otherwise approval is needed."),
          ("What counts as control for this rule?", "10% or more of the voting rights, the right to appoint a majority of directors, or control of management or policy decisions."),
          ("What is the two-layer round-tripping rule?", "Rule 19(3) bars a financial commitment in a foreign entity that has invested or invests into India where it results in more than two layers of subsidiaries."),
          ("Can an Indian company set up the US subsidiary instead?", "Yes. An Indian company invests under the general route for Indian entities (Schedule I), subject to the two-layer limit, which avoids the individual-control restriction."),
          ("We already have a triangle. What now?", "Map every share issue and transfer, check what was reported to the bank and RBI, and regularise through late submission fees or compounding before a fundraise or exit."),
          ("Can BQP fix our structure?", "Yes. " + CONTACT)],
    related=[("fema-odi-us-entity-indian-founder.html", "FEMA ODI for Indian founders"),
             ("how-to-structure-india-us-flip-f-reorganization-step-by-step.html", "India-US flip step by step"),
             ("reverse-flip-india-fast-track-inbound-merger-section-233-rbi-tax-2026.html", "Reverse flip by fast-track merger")],
    cta_h="Founders with a US parent and an Indian company?", cta_b=CONTACT,
    keywords="triangular structure Indian startup, Indian founders US parent Indian subsidiary FEMA, ODI Schedule III control step down subsidiary, round tripping two layers ODI, Delaware flip FEMA approval, resident individual ODI control 10 percent, Indian founder US company RBI approval",
    desc="Indian resident founders owning a US parent that owns their Indian company: why Schedule III of the FEMA Overseas Investment Rules, 2022 usually takes this triangle outside the automatic route (control from 10%), the two-layer round-tripping rule, options, and how to regularise an existing structure.",
    howto={"name": "How to check a founder triangle under FEMA", "description": "Steps for Indian founders with a US parent and an Indian subsidiary.", "steps": [
        {"name": "Map the holdings", "text": "List each founder's stake and rights in the US parent and the US parent's stake in the Indian company."},
        {"name": "Test control", "text": "10% or more of votes, board control or management control means the Schedule III restriction applies."},
        {"name": "Count the layers", "text": "Check the structure does not exceed two layers of subsidiaries."},
        {"name": "Seek approval or restructure", "text": "Apply through the AD bank, use an Indian parent, or regularise past steps before a fundraise."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BZ complete")
