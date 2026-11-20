# -*- coding: utf-8 -*-
"""Batch EL (20 Nov 2026): RBI's reported proposal for an INR 50 lakh yearly sub-limit within the Liberalised Remittance
Scheme - what is reported, what is not changing, who may be affected, what to do now. Call-first news explainer.
Facts (checked 20 Nov 2026): first reported 27 October 2026 (Zee Business, citing sources), followed by Outlook Money,
Drishti IAS and others: a sub-limit of INR 50 lakh a year on certain LRS remittances, such as business travel and
pilgrimages, within the overall USD 250,000 per financial year; education and medical remittances reported to be kept
outside; overall USD 250,000 limit reported likely to stay; no RBI circular, notification or effective date as of
18 November 2026 (NCA Academy); stated rationale - curbing dollar outflows. LRS applies to resident individuals; NRIs
repatriate NRO funds under the separate USD 1 million facility. TCS from 1 April 2026 per the site's LRS pages: nil for
loan-funded education, 2% for self-funded education, 20% above INR 10 lakh for other purposes such as gifts and
investments; TCS is creditable against tax or refundable through the return."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "rbi-lrs-50-lakh-sub-limit-proposal-2026-overseas-remittance-what-it-means"

C = contact("what you send abroad and why (education, gifts to family, overseas property or investments, travel), approximate amounts this financial year and which family members remit")
PAGES = [dict(
    slug=SLUG,
    title="RBI's Proposed INR 50 Lakh LRS Sub-Limit (2026): What Is Reported, What Is Not Changing, and How to Plan Your Overseas Remittances",
    em="a proposal, not yet a rule - plan, do not panic.",
    kicker="/ LRS &middot; Remittances &middot; RBI &middot; News explainer &middot; Updated 2026-11-20",
    lead=("Since 27 October 2026, news reports citing sources have said the RBI has proposed a <strong>yearly sub-limit of INR 50 lakh</strong> on <strong>certain</strong> remittances under the Liberalised Remittance Scheme (LRS). Business travel and pilgrimages are the examples mentioned. The sub-limit would sit inside the overall <strong>USD 250,000 per person per financial year</strong>, and <strong>education and medical</strong> remittances are reported to be kept outside it. "
          "<strong>As of 20 November 2026 there is no RBI circular, notification or start date</strong>, so the current rules still apply. "
          "LRS covers <strong>resident individuals</strong>. NRIs moving their own NRO money abroad use the separate USD 1 million facility. "
          "If you plan to remit large amounts this year for an overseas property, investments or gifts to children abroad, review the timing, the purpose codes and TCS now, and watch for the final rule."),
    sections=[
        ("/ Reported vs confirmed", "What we know on 20 November 2026.",
         table(["Point", "Status", "Detail"], [
             ["INR 50 lakh yearly sub-limit", "Reported proposal", "On certain LRS purposes, e.g. business travel and pilgrimages"],
             ["Overall LRS limit", "Unchanged today", "USD 250,000 per resident individual per financial year"],
             ["Education and medical", "Reported to be outside the sub-limit", "Not confirmed until RBI issues the rule"],
             ["Effective date", "None announced", "No circular or notification as of 18-20 November 2026"],
             ["TCS", "Unchanged", "Nil for loan-funded education, 2% self-funded education, 20% above INR 10 lakh for other purposes; creditable in your return"],
             ["NRIs", "Not under LRS", "NRO repatriation uses the separate USD 1 million facility"]])
         + call_box("Planning our overseas remittances this year", ["How much each family member can remit and for what",
                                                                    "Purpose codes and documents for education, gifts, property and investments",
                                                                    "TCS cost, credit and refunds",
                                                                    "LRS vs ODI for overseas business investments",
                                                                    "What changes if the sub-limit is notified"],
                    "planned remittances by purpose and amount, family members involved and TCS already collected this year.")),
        ("/ What to do now", "Sensible steps while the rule is pending.",
         ul("<strong>Do not rush or split artificially:</strong> the overall limit is per person; remitting in another family member&rsquo;s name must reflect a genuine gift and their own limit.",
            "<strong>Use the right purpose code:</strong> education and medical payments should be coded and documented as such; reports suggest they may stay outside any sub-limit.",
            "<strong>Large planned transfers:</strong> for an overseas property or investment planned this financial year, review timing and documents with your bank now.",
            "<strong>TCS:</strong> 20% TCS above INR 10 lakh on gifts and investments is not a final cost; claim it against your tax or as a refund. See <a href=\"tcs-20-foreign-remittance-lrs-india-2026.html\">TCS on foreign remittances</a> and <a href=\"tcs-refund-foreign-remittance-lrs-how-to-claim-itr-employer-2026.html\">how to claim TCS back</a>.",
            "<strong>Students abroad:</strong> see <a href=\"parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html\">parents funding study abroad</a>.",
            "<strong>Business investments abroad:</strong> an overseas company or subsidiary may fall under ODI rather than LRS; see <a href=\"ca-for-fema-odi-compliance.html\">FEMA ODI compliance</a>.",
            "<strong>NRIs:</strong> money in NRO accounts goes abroad under the USD 1 million facility with Forms 145 and 146; see <a href=\"repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html\">repatriation from NRO</a>.")
         + '<p>Related: <a href="year-end-lrs-tcs-20-planning-october-march-2026-27.html">year-end LRS and TCS planning</a> &middot; <a href="lrs-tcs-calculator.html">LRS TCS calculator</a> &middot; <a href="india-tax-nri-cross-border-news-november-2026.html">November 2026 news roundup</a>.</p>'
         + sources("Reports of the proposal: Zee Business (27 October 2026, citing sources), Outlook Money, Drishti IAS, NCA Academy (status as of 18 November 2026). Current rules: RBI Master Direction on the Liberalised Remittance Scheme (USD 250,000 per financial year); Income-tax provisions on TCS on foreign remittances as summarised on this site. No RBI circular on the sub-limit had been issued when this page was written; we will update it when one is.")),
    ],
    faqs=[("Has the RBI capped LRS remittances at INR 50 lakh?", "Not yet. Reports since 27 October 2026 say the RBI has proposed a yearly INR 50 lakh sub-limit on certain remittances, but no circular, notification or effective date had been issued as of 20 November 2026."),
          ("Which remittances would the INR 50 lakh sub-limit cover?", "Reports mention business travel and pilgrimages as examples, with education and medical remittances kept outside; the final scope will depend on the RBI's rule."),
          ("Is the USD 250,000 LRS limit changing?", "Reports say the overall USD 250,000 per person per financial year limit is likely to stay; the INR 50 lakh figure is described as a sub-limit within it."),
          ("Does the LRS sub-limit affect NRIs?", "LRS applies to resident individuals. NRIs repatriating their own NRO funds use the separate USD 1 million per financial year facility."),
          ("Should I send money abroad now before the rule changes?", "Plan genuine needs sensibly rather than rushing: use the correct purpose codes, keep documents, and remember TCS above INR 10 lakh can be claimed back in your return."),
          ("Can BQP help plan our remittances?", "Yes. " + C)],
    related=[("tcs-20-foreign-remittance-lrs-india-2026.html", "TCS on foreign remittances"), ("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "Parents funding study abroad"),
             ("repatriate-money-from-india-to-abroad-nro-usd-1-million-15ca-15cb-2026.html", "NRO repatriation (USD 1 million)")],
    cta_h="Sending large amounts abroad this year?", cta_b=C,
    keywords="RBI LRS 50 lakh limit, LRS sub-limit proposal 2026, RBI overseas remittance cap, LRS USD 250000 limit 2026, TCS on foreign remittance 2026, LRS business travel pilgrimage limit, does LRS apply to NRI",
    desc="RBI's reported INR 50 lakh LRS sub-limit (proposal since 27 Oct 2026): certain purposes like business travel and pilgrimages, inside the USD 250,000 limit; education and medical reportedly outside; no circular yet. What it means for residents, NRIs and TCS, and how to plan.",
    howto={"name": "How to plan overseas remittances while the LRS sub-limit is pending", "description": "Practical steps.", "steps": [
        {"name": "List planned remittances", "text": "By purpose and family member for this financial year."},
        {"name": "Check purpose codes and documents", "text": "Education, medical, gifts, property, investments."},
        {"name": "Estimate TCS", "text": "And plan to claim it in your return."},
        {"name": "Consider ODI for business investments", "text": "Overseas companies may fall outside LRS."},
        {"name": "Watch for the RBI rule", "text": "Re-check plans once a circular is issued."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EL complete")
