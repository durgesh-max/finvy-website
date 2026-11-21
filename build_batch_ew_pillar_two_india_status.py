# -*- coding: utf-8 -*-
"""Batch EW (21 Nov 2026): REPLACES the page at beps-pillar-2-india-implementation-october-2026-update.html.
The earlier version (build_batch_q_news.py, 22 Oct 2026) said India's Pillar Two rules (QDMTT, IIR, UTPR) were
operational from FY 2025-26 and named Indian GloBE forms. That was wrong: India has not enacted Pillar Two legislation.
Facts (checked 21 Nov 2026):
- Beacon Filing, 'Has India Adopted Pillar 2?' (published 21 March 2026, last updated 7 September 2026): India has not
  yet enacted domestic Pillar Two legislation; a QDMTT is expected; India's 25.17% (115BAA) and 17.16% (115BAB) rates
  are above 15%, but incentives (SEZ, area-based, IFSC) can pull the effective rate below 15%. A second practitioner
  guide says India had not enacted a QDMTT as of May 2026. No source found reporting enactment since. The site's own
  transfer-pricing page already says India had not legislated GloBE rules as of November 2026.
- OECD side-by-side package, 5 January 2026 (RSM US, Grant Thornton alerts): US-parented groups can be exempt from the
  IIR and UTPR from 1 January 2026; qualified domestic top-up taxes still apply where a country has one; GloBE
  information return obligations continue.
- Pillar Two applies to groups with consolidated revenue of EUR 750 million or more in two of the four preceding years.
- Many jurisdictions have rules in force (UK and EU member states from accounting periods beginning on or after
  31 December 2023; others since). Existing Indian obligations: Form 3CEB, master file (Form 3CEAA), CbCR (Form 3CEAD)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 21 November 2026."
SLUG = "beps-pillar-2-india-implementation-october-2026-update"

C = contact("where your group is headquartered, group revenue, what the Indian entity does and which tax incentives it uses, and what your head office has asked for")
PAGES = [dict(
    slug=SLUG,
    title="BEPS Pillar Two in India (November 2026): India Has Not Enacted the 15% Global Minimum Tax - What Indian Subsidiaries of Foreign Groups Still Have to Do",
    em="status, who collects the top-up tax, and the data your head office will ask for.",
    kicker="/ Pillar Two &middot; Global minimum tax &middot; Foreign-owned subsidiaries &middot; Updated 2026-11-21",
    lead=("<strong>India has not enacted Pillar Two.</strong> As of November 2026 there is no Indian qualified domestic minimum top-up tax (QDMTT), income inclusion rule or undertaxed profits rule, and there is <strong>no Indian GloBE return or top-up tax to file</strong>. "
          "That does not take an Indian subsidiary out of the rules. If the group has consolidated revenue of <strong>EUR 750 million or more</strong> and its parent or other group countries have Pillar Two in force, the Indian entity is still a <strong>constituent entity</strong>. Any top-up tax on low-taxed Indian profits is collected <strong>abroad</strong>, usually by the parent&rsquo;s country. "
          "Most Indian companies pay <strong>25.17%</strong>, well above the 15% floor. The exposure sits with entities using incentives, such as SEZ or GIFT IFSC units and tax holidays. "
          "For <strong>US-parented groups</strong>, the OECD&rsquo;s side-by-side package of 5 January 2026 can switch off the income inclusion and undertaxed profits rules, though reporting continues. "
          "<em>An earlier version of this page said India&rsquo;s rules were already in force. That was incorrect and was corrected on 21 November 2026.</em>"),
    sections=[
        ("/ Where things stand", "India and the rest of the group.",
         table(["Question", "Position in November 2026"], [
             ["Has India enacted Pillar Two?", "No. No QDMTT, income inclusion rule or undertaxed profits rule has been legislated; a QDMTT is widely expected in a future Budget"],
             ["Is there an Indian GloBE return or form?", "No. Existing filings continue: Form 3CEB, the master file (Form 3CEAA) and country-by-country report (Form 3CEAD) where thresholds are met"],
             ["Which groups are in scope globally?", "Consolidated revenue of EUR 750 million or more in at least two of the four preceding years"],
             ["Who taxes low-taxed Indian profits?", "The parent&rsquo;s country under its income inclusion rule, or other group countries under the undertaxed profits rule, because India has no QDMTT to collect it first"],
             ["Which Indian entities are at risk of a rate below 15%?", "Those using incentives: SEZ and GIFT IFSC units, tax holidays and large deductions. Standard-rate companies (25.17%, or 17.16% for older new-manufacturing companies) are generally above the floor"],
             ["US-parented groups", "The side-by-side package (5 January 2026) allows an exemption from the income inclusion and undertaxed profits rules from 1 January 2026; domestic top-up taxes in other countries and information reporting still apply"],
             ["Indian-headquartered groups", "Foreign subsidiaries face domestic top-up taxes abroad; with no Indian income inclusion rule, other countries&rsquo; backstop rules can also apply"]])
         + call_box("Pillar Two and our Indian entity", ["Whether your group is in scope and where top-up tax would be collected",
                                                         "The Indian entity&rsquo;s effective tax rate under the GloBE method, incentive by incentive",
                                                         "Data your head office needs from India for its information return",
                                                         "SEZ, GIFT IFSC and tax-holiday planning with the 15% floor in mind",
                                                         "Transfer pricing, master file and country-by-country reporting alongside"],
                    "group structure and revenue, the Indian entity&rsquo;s financial statements and tax computation, and any head-office data request.")),
        ("/ What an Indian subsidiary should do now", "Practical steps.",
         ul("<strong>Confirm scope with head office:</strong> is the group above EUR 750 million, and which countries in the group have Pillar Two in force?",
            "<strong>Compute the Indian effective rate the GloBE way:</strong> covered taxes divided by GloBE income, after the substance-based exclusion for payroll and tangible assets. It will differ from the rate in your tax return.",
            "<strong>Review incentives:</strong> an incentive that takes the Indian rate below 15% may simply move the tax to the parent&rsquo;s country. Model this before choosing SEZ, GIFT IFSC or a holiday; see <a href=\"gift-city-section-10-4d-2026-update.html\">GIFT City section 10(4D)</a>.",
            "<strong>Get the data ready:</strong> deferred tax, payroll and asset figures in the form the group&rsquo;s information return needs; reconcile Ind AS numbers to the group&rsquo;s consolidated accounts.",
            "<strong>Keep Indian filings in order:</strong> <a href=\"form-3ceb-tp-audit-india-2026-30-november-checklist.html\">Form 3CEB</a>, master file and country-by-country report; see <a href=\"transfer-pricing-india-foreign-mnc.html\">transfer pricing for foreign groups in India</a>.",
            "<strong>Watch the Budget:</strong> if India introduces a QDMTT, the top-up tax would be paid in India instead of abroad, and Indian filings would follow.")
         + '<p>Related: <a href="pillar-2-global-minimum-tax-india-startups-2026.html">Pillar Two for Indian startups and groups</a> &middot; <a href="gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html">global capability centres in India</a> &middot; <a href="uae-corporate-tax-2026-qfzp-fta-update.html">UAE corporate tax and top-up tax</a> &middot; <a href="foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html">compliance calendar for foreign-owned subsidiaries</a>.</p>'
         + sources("OECD/G20 Inclusive Framework Pillar Two (GloBE) model rules and the side-by-side package of 5 January 2026 (as summarised by RSM US and Grant Thornton); India status per Beacon Filing, 'Has India Adopted Pillar 2?' (updated 7 September 2026) and other practitioner guides; no Indian Pillar Two legislation located as of 21 November 2026. Corrected on 21 November 2026: the earlier version of this page wrongly described Indian rules as in force. Check the Finance Act and CBDT notifications after each Budget.")),
    ],
    faqs=[("Has India implemented Pillar Two?", "No. As of November 2026 India has not enacted a qualified domestic minimum top-up tax, an income inclusion rule or an undertaxed profits rule. A QDMTT is widely expected in a future Budget."),
          ("Does an Indian subsidiary have to file a GloBE return in India?", "No. There is no Indian GloBE information return or top-up tax filing. The subsidiary still supplies data for the group's return filed abroad, and continues Indian filings such as Form 3CEB, the master file and the country-by-country report."),
          ("Who collects top-up tax on low-taxed Indian profits?", "Because India has no domestic top-up tax, it is collected abroad: by the parent's country under its income inclusion rule, or by other group countries under the undertaxed profits rule."),
          ("Is India's corporate tax rate above the 15% minimum?", "Usually yes. Most companies pay 25.17%. The risk is for entities using incentives such as SEZ or GIFT IFSC benefits or tax holidays, which can pull the GloBE effective rate below 15%."),
          ("How does the side-by-side package affect US groups with Indian subsidiaries?", "Under the OECD package of 5 January 2026, US-parented groups can be exempt from the income inclusion and undertaxed profits rules from 1 January 2026. Domestic top-up taxes in countries that have them, and information reporting, continue."),
          ("Can BQP support Pillar Two work for the Indian entity?", "Yes. " + C)],
    related=[("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign groups in India"),
             ("pillar-2-global-minimum-tax-india-startups-2026.html", "Pillar Two for Indian startups and groups"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Compliance calendar for foreign-owned subsidiaries")],
    cta_h="Head office asking for Pillar Two data from India?", cta_b=C,
    keywords="has India implemented Pillar Two, India Pillar 2 status 2026, India QDMTT, global minimum tax India subsidiary, GloBE India effective tax rate, side-by-side package US parent Indian subsidiary, Pillar Two SEZ GIFT IFSC",
    desc="Pillar Two in India (November 2026): India has not enacted the 15% global minimum tax - no QDMTT, IIR, UTPR or Indian GloBE return. Indian subsidiaries of groups above EUR 750 million are still in scope abroad; incentives below 15% shift tax to the parent's country.",
    howto={"name": "How an Indian subsidiary prepares for Pillar Two", "description": "While India has no domestic rules.", "steps": [
        {"name": "Confirm group scope", "text": "EUR 750 million revenue test and which group countries have rules in force."},
        {"name": "Compute the GloBE effective rate for India", "text": "Covered taxes over GloBE income, after the substance-based exclusion."},
        {"name": "Review incentives", "text": "Check whether SEZ, IFSC or holiday benefits take the rate below 15%."},
        {"name": "Prepare group data", "text": "Deferred tax, payroll and asset data reconciled to the consolidated accounts."},
        {"name": "Monitor Indian law", "text": "Watch each Budget for a domestic top-up tax."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EW complete")
