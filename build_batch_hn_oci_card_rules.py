# -*- coding: utf-8 -*-
"""Batch HN (25 Nov 2026): OCI card rules 2026 - who is eligible, what OCI allows and restricts, reissue and passport
upload rules (age 20 / age 50, three months), children, August 2025 cancellation grounds (two-year sentence; chargesheet
for offence punishable with seven years or more), tax and money rules for OCIs.
Demand: sweep ac98 (25 Nov 2026), all 7 markets: "oci card rules and regulations", "oci card rules 2025", "oci card rules
tightened india", "oci card rules for kids", "oci application rules".
Facts (checked 25 Nov 2026): MHA notification of August 2025 under section 7D(da) of the Citizenship Act, 1955 as reported
by Business Today, The Print, The Wire and Tribune (cancellation for sentence of two years or more, or chargesheet for an
offence punishable with seven years or more, in India or abroad); Indian mission notices on the revised re-issuance
guidelines of 16 April 2021 (reissue only once if new passport issued after 20 for those registered before 20; upload new
passport and photo each time up to 20 and once after 50, within three months); MHA notification of March 2021 on OCI
activities needing permission; Citizenship Act section 7A eligibility."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "oci-card-rules-2026-eligibility-reissue-passport-age-20-50-children-cancellation-tightened"

C = contact("your citizenship, when you got the OCI card, your age at registration, any new passport, and the tax or money question you have in India")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="OCI Card Rules (2026): Eligibility, What OCIs Can and Cannot Do, Passport Reissue at 20 and 50, Children and the 2025 Cancellation Rules",
    em="a lifelong visa with conditions that tightened in 2025.",
    kicker="/ OCI cardholders and families &middot; Immigration and tax &middot; Updated 2026-11-25",
    lead=("<strong>An Overseas Citizen of India (OCI) card is a lifelong, multiple-entry visa for foreign citizens of Indian origin and foreign spouses of Indian citizens or OCIs; it is not dual citizenship.</strong> "
          "Rules that matter in 2026: since August 2025 an OCI registration can be cancelled if the holder is sentenced to two years or more, or charge-sheeted for an offence punishable with seven years or more, in India or abroad. "
          "Under the 2021 guidelines, a card needs reissuing only once, when a new passport is issued after age 20 to someone registered before 20; otherwise the new passport and a photo are uploaded online, each time up to age 20 and once after age 50, within three months."),
    sections=[
        ("/ Quick answers", "What OCI holders ask most.",
         ul("<strong>What changed in 2025?</strong> The government added cancellation grounds: a prison sentence of two years or more, or being named in a chargesheet for an offence punishable with seven years or more. It applies to offences in India or abroad that are recognised under Indian law.",
            "<strong>Do I need a new OCI card with every passport?</strong> No. If you registered before 20, the card is reissued once, when you get a new passport after turning 20. If you registered after 20, no reissue is needed; upload the new passport details online.",
            "<strong>What are the rules for children?</strong> Each time a child gets a new passport, up to age 20, upload the new passport and a recent photo on the OCI portal within three months. Reissue the card once after the child turns 20 and gets a new passport.",
            "<strong>What can&rsquo;t OCIs do?</strong> Vote, hold constitutional or most government posts, or buy agricultural land, plantation or farmhouse property. Research, missionary or journalism work and visits to protected areas need special permission.",
            "<strong>Who cannot get OCI?</strong> Applicants who, or whose parents or grandparents, have been citizens of Pakistan or Bangladesh, and serving or retired foreign military personnel.",
            "<strong>Does OCI decide my Indian tax?</strong> No. Tax residence depends on days spent in India, not on OCI status; see " + L("oci-cardholder-tax-india-complete-2026.html", "OCI cardholder tax")) + "."),
        ("/ Rules at a glance", "OCI in one table.",
         table(["Topic", "Rule"], [
             ["Eligibility", "Foreign citizens of Indian origin (and their children and grandchildren), and foreign spouses of Indian citizens or OCIs married for at least two years"],
             ["Visa", "Lifelong, multiple entry; no registration with the police or FRRO for any length of stay"],
             ["Reissue", "Once only, on a new passport after age 20, if registered before 20; none if registered after 20"],
             ["Passport upload", "Each new passport up to age 20 and once after 50, within three months of getting it"],
             ["Restricted activities", "Research, missionary or journalism work, mountaineering and protected areas need permission"],
             ["Property", "Can buy residential and commercial property; not agricultural land, plantation or farmhouse (inheritance allowed)"],
             ["Cancellation (2025)", "Sentence of two years or more, or chargesheet for an offence with seven years or more; also fraud or acts against India"]])),
        ("/ Money and tax for OCIs", "What the OCI card does not cover.",
         ul("<strong>Bank accounts:</strong> OCIs are treated like NRIs for accounts; see " + L("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "can an OCI open NRE / NRO accounts") + ".",
            "<strong>PAN:</strong> needed for investments and property; see " + L("nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund.html", "PAN for NRIs and OCIs") + ".",
            "<strong>Investing:</strong> demat, mutual funds and digital KYC from abroad; see " + L("nri-oci-demat-trading-account-digital-kyc-from-abroad-sebi-3-december-2026.html", "digital KYC for NRIs and OCIs") + ".",
            "<strong>Agricultural land:</strong> OCIs cannot buy it but can inherit it; see " + L("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "agricultural land rules") + ".",
            "<strong>Giving up Indian citizenship first:</strong> surrender and the renunciation certificate come before OCI; see " + L("renounce-indian-citizenship-surrender-certificate-bank-accounts-pan-property-tax-oci-2026.html", "renouncing Indian citizenship") + ".")
         + call_box("OCI tax and money questions", ["Tax residence and India income",
                                                    "NRE / NRO accounts and repatriation",
                                                    "Property purchase and sale",
                                                    "PAN and investments",
                                                    "Inherited assets in India"],
                    "your citizenship, days in India and the income or asset.")
         + sources("Citizenship Act, 1955, sections 7A to 7D; MHA notification of August 2025 adding cancellation grounds under section 7D(da), as reported by Business Today, The Print, The Wire and Tribune; Indian mission notices on the revised OCI re-issuance guidelines (16 April 2021); MHA notification of 4 March 2021 on OCI rights and permissions. Immigration questions should be confirmed on ociservices.gov.in or with the Indian mission. Checked 25 November 2026.")),
    ],
    faqs=[("What are the new OCI card rules from 2025?", "Since August 2025, OCI registration can be cancelled if the holder is sentenced to imprisonment of two years or more, or is charge-sheeted for an offence punishable with seven years or more, in India or abroad, where the offence is recognised under Indian law."),
          ("Do I need to renew my OCI card when I get a new passport?", "Only once, if you registered before age 20: the card is reissued when a new passport is issued after you turn 20. If you registered after 20, no reissue is needed. In other cases upload the new passport and a photo on the OCI portal within three months."),
          ("What are the OCI card rules for children?", "Each time a child gets a new passport up to age 20, the new passport and a recent photo must be uploaded on the OCI portal within three months, and the card is reissued once after the child turns 20 and gets a new passport."),
          ("Can an OCI cardholder buy property in India?", "Yes, residential and commercial property, but not agricultural land, plantation property or a farmhouse. Agricultural land can be inherited."),
          ("Does an OCI card make me an Indian tax resident?", "No. Tax residence depends on the days you spend in India in the tax year, not on OCI status. OCIs are generally taxed like NRIs on Indian income if they are non-resident."),
          ("Can BQP help OCI cardholders?", "Yes, on the tax and money side: residence, Indian income, NRE / NRO accounts, property and repatriation. Immigration questions should go to the Indian mission. " + C)],
    related=[("oci-cardholder-tax-india-complete-2026.html", "OCI cardholder tax"),
             ("can-oci-open-nre-nro-account-nri-bank-accounts-tax-repatriation-2026.html", "OCI bank accounts"),
             ("nri-oci-pan-card-2026-apply-from-abroad-form-93-95-inoperative-pan-fix-refund.html", "PAN for OCIs"),
             ("nri-oci-agricultural-land-india-buy-inherit-sell-tax-fema-2026.html", "Agricultural land"),
             ("renounce-indian-citizenship-surrender-certificate-bank-accounts-pan-property-tax-oci-2026.html", "Renouncing Indian citizenship")],
    cta_h="OCI cardholder with money or property in India?", cta_b=C,
    keywords="OCI card rules, OCI card rules 2025, OCI card rules 2026, OCI rules tightened, OCI card rules for kids, OCI reissue new passport, OCI card cancellation, OCI card rules and regulations, OCI application rules",
    desc="OCI card rules (2026): eligibility, lifelong visa, what OCIs cannot do, reissue only once after 20, passport uploads up to 20 and after 50, children, and the August 2025 cancellation rules (two-year sentence or seven-year chargesheet).",
    howto={"name": "How to keep your OCI card valid", "description": "When you get a new passport.", "steps": [
        {"name": "Check your age at registration", "text": "Before 20 or after 20."},
        {"name": "Reissue if required", "text": "Once, for a new passport after 20, if registered before 20."},
        {"name": "Otherwise upload", "text": "New passport and photo on the OCI portal within three months (up to 20, and once after 50)."},
        {"name": "Carry both documents", "text": "Travel with the OCI card and the current passport."},
        {"name": "Keep tax separate", "text": "Track days in India for tax residence."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HN complete")
