# -*- coding: utf-8 -*-
"""Batch AS: Round 30 - Press Note 2 (2026): FDI from land-border countries eased (10% non-controlling, 60-day track)."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


TABLE = ("<table><thead><tr><th>Situation</th><th>Route</th></tr></thead><tbody>"
         "<tr><td>Investor incorporated outside a land-border country; land-border beneficial ownership within 10% and non-controlling</td><td>Automatic route (sectoral caps still apply)</td></tr>"
         "<tr><td>Land-border beneficial ownership above the threshold, or any control</td><td>Government approval</td></tr>"
         "<tr><td>Investor incorporated or registered in China (including Hong Kong) or another land-border country</td><td>Government approval</td></tr>"
         "<tr><td>Approval cases in specified manufacturing sectors</td><td>Decision timeline of 60 days</td></tr>"
         "<tr><td>Other approval cases</td><td>Standard timeline (about 12 weeks)</td></tr></tbody></table>")

sections = [
    ("/ What changed", "Press Note 3 (2020) vs Press Note 2 (2026).",
     "<p>Since April 2020, Press Note 3 required government approval for any investment where the investor, or the beneficial owner of the investment, was from a country sharing a land border with India. Because no threshold was set, even a small indirect Chinese holding in a global fund could trigger approval. Press Note 2 (2026), approved by the Cabinet on 10 March 2026, keeps the rule but adds a threshold and defines beneficial ownership.</p>" + TABLE),
    ("/ The key changes", "In plain terms.",
     ul("<strong>Beneficial owner defined</strong>: by reference to the Prevention of Money-laundering Act, 2002 and Rule 9(3) of the PML (Maintenance of Records) Rules, 2005.",
        "<strong>10% non-controlling relief</strong>: where land-border beneficial ownership in the investor entity is within 10% and carries no control, the investment can use the automatic route, subject to sectoral caps.",
        "<strong>Tested at the investor level</strong>: the investor entity must itself be incorporated outside a land-border country.",
        "<strong>60-day decisions</strong>: approval proposals in specified manufacturing sectors, including capital goods, electronic capital goods, electronic components and polysilicon / ingot-wafers (and other items listed in the revised SOP), get a 60-day timeline.",
        "<strong>Procedure</strong>: a revised standard operating procedure (reported as dated 4 May 2026) moves applications to the National Single Window System; the corresponding NDI Rules amendment was reported as notified on 1 May 2026.",
        "<strong>Disclosure</strong>: investors declare beneficial ownership at the time of investment; banks may ask for an undertaking.")),
    ("/ What did not change", "Still needs approval.",
     ul("Direct investment by entities incorporated or registered in China, including Hong Kong, and other land-border countries.",
        "Land-border beneficial ownership above the threshold, or any control through board seats, veto rights or agreements.",
        "Routing through a Singapore, Mauritius or US holding company does not by itself remove the requirement; beneficial ownership is looked through.",
        "A later change in ownership that crosses the threshold needs approval.",
        "Prohibited sectors and sectoral caps.")),
    ("/ What foreign investors and Indian companies should do", "Practical checklist.",
     ul("Map the cap table and the investor's upstream ownership, including fund LPs, to identify land-border beneficial owners and control rights.",
        "Document the 10% test at the investor level and keep the beneficial-ownership declaration on file.",
        "Check sectoral caps and whether the 60-day sector track applies to an approval case.",
        "For past investments made without approval where it was needed, assess FEMA compounding before a fundraise or exit.",
        "Expect buyers in M&amp;A due diligence to ask for this analysis.") +
     '<p><strong>Sources:</strong> <a href="https://www.barandbench.com/law-firms/view-point/beyond-press-note-3-analysing-press-note-2-2026-and-the-new-fdi-framework-for-land-bordering-countries" rel="nofollow noopener" target="_blank">Bar &amp; Bench (18 June 2026)</a>; '
     '<a href="https://taxguru.in/rbi/investment-china-land-border-fdi-rule-2026.html" rel="nofollow noopener" target="_blank">TaxGuru (27 March 2026)</a>; '
     '<a href="https://ksandk.com/fdi/investing-in-india-from-hong-kong-fdi-rules/" rel="nofollow noopener" target="_blank">King Stubb &amp; Kasiva (27 October 2026)</a>.</p>'
     "<p><em>Last updated: 31 October 2026. Practitioner summaries differ on whether the threshold reads \"up to 10%\" or \"more than 10%\" and on the full sector list; check the DPIIT Press Note and SOP text for your case.</em></p>"),
]

faqs = [
    ("What is Press Note 2 (2026)?", "An amendment to India's FDI policy, approved on 10 March 2026, that eases Press Note 3 (2020) for investments with a land-border-country link: non-controlling beneficial ownership within 10% can use the automatic route, beneficial ownership is defined using PMLA rules, and approvals in specified manufacturing sectors get a 60-day timeline."),
    ("Is Press Note 3 still in force?", "Yes. Government approval is still needed for investors from China, Hong Kong and other land-border countries, and where land-border beneficial ownership is above the threshold or carries control."),
    ("Can a fund with a small Chinese LP invest in India without approval now?", "Generally yes, if the fund is incorporated outside a land-border country and the Chinese beneficial ownership is within 10% and non-controlling, subject to sectoral caps and disclosure."),
    ("Do Hong Kong companies still need approval to invest in India?", "Yes. Entities incorporated or registered in Hong Kong are treated with China and still need prior government approval."),
    ("Which sectors get 60-day approval?", "Specified manufacturing sectors such as capital goods, electronic capital goods, electronic components and polysilicon / ingot-wafers, with others listed in the revised SOP."),
    ("Can BQP do the Press Note 3 / Press Note 2 analysis?", "Yes: beneficial-ownership mapping, route assessment, approval filings, FC-GPR/FC-TRS and compounding of past breaches. " + CONTACT),
]

html = page(slug=SLUG,
            title="Press Note 2 (2026): FDI From China and Land-Border Countries Eased, 10% Non-Controlling Stakes Allowed",
            description="Press Note 2 (2026) eases Press Note 3: investments with non-controlling land-border beneficial ownership within 10% can use the automatic route; beneficial owner defined via PMLA rules; 60-day approvals for specified manufacturing sectors. China and Hong Kong investors still need approval.",
            keywords="Press Note 2 2026, Press Note 3 amendment 2026, FDI China India 10 percent, land border FDI automatic route, Hong Kong investment India approval, beneficial ownership Press Note 3, 60 day FDI approval India",
            hero_kicker="/ FDI &middot; Foreign Companies &middot; Updated 2026-10-31",
            hero_title_html="Press Note 2 (2026), <em>Press Note 3 eased for small stakes.</em>",
            hero_lead="India's FDI rule for investors linked to China and other land-border countries has been relaxed. Under Press Note 2 (2026), an investor incorporated outside those countries whose land-border beneficial ownership is within 10% and non-controlling can invest through the automatic route. Beneficial ownership is now defined using anti-money-laundering rules, and approvals in specified manufacturing sectors get a 60-day timeline. Direct investment from China and Hong Kong still needs government approval.",
            sections=sections, faqs=faqs,
            related=[("can-foreigner-own-100-percent-indian-company.html", "Related", "Can a foreigner own 100% of an Indian company?"),
                     ("best-ca-fema-compounding-voluntary-india.html", "Related", "FEMA compounding")],
            cta_headline="Investor with a land-border link?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AS complete")
