# -*- coding: utf-8 -*-
"""Batch AL: Round 22 - rewrite gaming page for the Online Gaming Act, 2025 (real-money games banned from 1 May 2026)."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


p = dict(
    slug="best-ca-gaming-esports-india-2026",
    title="CA for Gaming and Esports Companies in India After the Online Gaming Act, 2025",
    em="esports, free-to-play, and winding down real-money games.",
    kicker="/ Sector &middot; Gaming &amp; Esports &middot; Updated 2026-10-29",
    lead="The Promotion and Regulation of Online Gaming Act, 2025 (assent 22 August 2025, fully in force from 1 May 2026 with the Online Gaming Rules, 2026) bans offering, advertising or processing payments for online money games, including paid fantasy sports, rummy and poker. Esports and free-to-play or social games remain legal. Bharat Quantum Prospera, led by CA Durgesh Chavda (ICAI), advises gaming companies on both sides of that line.",
    sections=[
        ("/ What the law now allows", "The new map.",
         "<table><thead><tr><th>Activity</th><th>Status from 1 May 2026</th></tr></thead><tbody>"
         "<tr><td>Online money games (stakes or fees with expectation of winnings), including paid fantasy, rummy, poker, betting</td><td>Banned: offering, advertising and payment processing</td></tr>"
         "<tr><td>Esports</td><td>Legal and recognised</td></tr>"
         "<tr><td>Free-to-play, casual and social games without money stakes</td><td>Legal</td></tr></tbody></table>"
         "<p>Banks and payment providers may not process payments for online money games, and penalties apply to operators and advertisers.</p>"),
        ("/ For esports and free-to-play companies", "Tax and compliance that still applies.",
         ul("GST on in-app purchases, subscriptions and advertising; registration for foreign platforms supplying to Indian users under the online services (OIDAR) rules.",
            "Tax and TDS on prize money paid to players and teams, depending on how prizes are structured.",
            "Transfer pricing and permanent establishment questions for Indian studios working for foreign publishers.",
            "FEMA and foreign investment reporting for Indian gaming studios raising money from abroad.",
            "Data protection under the DPDP Act, including children's data in games aimed at younger players.")),
        ("/ For former real-money operators", "Winding down cleanly.",
         ul("Pending GST disputes on earlier periods, including the valuation of deposits and contest entry amounts.",
            "TDS returns and certificates on player winnings for past years, and reconciling player balances being returned.",
            "Employee settlements, contract terminations and investor reporting.",
            "Pivot planning: moving to esports or free-to-play without carrying over prohibited features.",
            "Closing or restructuring the company: strike-off, merger or sale.") +
         '<p><strong>Sources:</strong> <a href="https://www.mondaq.com/india/gaming/1676566/summary-promotion-and-regulation-of-online-gaming-act-2025" rel="nofollow noopener" target="_blank">Mondaq: summary of the Act</a>; '
         '<a href="https://www.sansalegal.com/post/online-gaming-act-2025-india-bans-real-money-gaming-with-effect-from-may-2026" rel="nofollow noopener" target="_blank">Sansa Legal: ban effective May 2026</a>.</p>'
         "<p><em>Last updated: 29 October 2026. Legal questions on whether a game is an online money game should go to counsel.</em></p>"),
    ],
    faqs=[
        ("Are real-money online games legal in India in 2026?", "No. Under the Promotion and Regulation of Online Gaming Act, 2025, in full force from 1 May 2026, offering, advertising or processing payments for online money games is banned, including paid fantasy sports, rummy and poker."),
        ("Is esports legal in India?", "Yes. The Act recognises esports, and free-to-play or social games without money stakes remain legal."),
        ("What should a former real-money gaming company do now?", "Settle past GST and TDS positions, return player balances, handle employees and contracts, and either pivot to permitted formats or close or restructure the company."),
        ("Does BQP work with esports and game studios?", "Yes: GST, TDS on prizes, transfer pricing for studios serving foreign publishers, FEMA for foreign funding, and wind-down work for former real-money operators. " + CONTACT),
    ],
    related=[("dpdp-act-india-foreign-company-compliance-2026.html", "DPDP Act compliance"), ("company-struck-off-section-248-notice-revival-india.html", "Closing or reviving a company")],
    keywords="online gaming act 2025 CA, real money gaming ban India 2026, esports CA India, gaming company GST India 2026, fantasy sports ban wind down",
    desc="Tax and compliance for gaming companies after the Promotion and Regulation of Online Gaming Act, 2025: real-money games banned from 1 May 2026, esports and free-to-play legal, and wind-down work for former real-money operators.",
)

html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
            hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
            hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
            related=[(h, "Related", t) for h, t in p["related"]],
            cta_headline="Gaming or esports company?", cta_body=CONTACT)
write_page(p["slug"], html)
print("Batch AL complete: gaming page rewritten")
