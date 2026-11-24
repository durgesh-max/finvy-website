# -*- coding: utf-8 -*-
"""Batch HE (25 Nov 2026): India-Hong Kong DTAA - signed 19 March 2018, in force 30 November 2018; 5% on dividends, 10% on
interest (government and specified bodies such as the RBI exempt), royalties and fees for technical services; an
anti-abuse article against treaty shopping and conduit companies; Hong Kong holding structures and Indian founders;
FDI overlay (Hong Kong investors still need approval under Press Note 3 as per the site's Press Note 2 (2026) page); how
to claim.
Demand: sweep ac95 (25 Nov 2026), all 7 markets: "india hong kong dtaa", "indian hong kong dtaa", "india hong kong dtaa
pdf".
Facts (checked 25 Nov 2026): EY Global Tax News (signed March 2018; entered into force, December 2018 alert), India
Briefing, KPMG, ClearTax, Beacon Filing, NoBroker, Dezan Shira: dividends 5%, interest/royalties/FTS 10% (one TaxGuru
summary shows dividends 10% - outlier noted), government/RBI interest exempt, anti-abuse article. Application date in India
stated as from the year after entry into force, to confirm against the notification."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "india-hong-kong-dtaa-tax-treaty-rates-dividend-5-interest-royalty-fts-10-press-note-2026"

C = contact("whether you are a Hong Kong company, a Hong Kong resident or an Indian founder with a Hong Kong entity, the income type (dividend, interest, royalty, technical fees or gains), the amounts, any Indian investment, and whether you have a TRC and PAN")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Hong Kong DTAA (2026): Tax Treaty Rates of 5% on Dividends and 10% on Interest, Royalties and Technical Fees, Anti-Abuse Rules and FDI Approval",
    em="low dividend tax, but substance and investment approval still decide the outcome.",
    kicker="/ Hong Kong companies and Indian founders &middot; DTAA &middot; Updated 2026-11-25",
    lead=("<strong>India and Hong Kong signed their first comprehensive double tax avoidance agreement on 19 March 2018, and it entered into force on 30 November 2018.</strong> "
          "It caps Indian tax on dividends paid to a Hong Kong resident at 5% and on interest, royalties and fees for technical services at 10%, against India&rsquo;s domestic 20% plus surcharge and cess; interest paid to the governments and specified bodies such as the Reserve Bank of India is exempt. "
          "The treaty has an anti-abuse article aimed at treaty shopping and conduit companies, so a Hong Kong entity needs real substance. Separately, investment into India with Hong Kong or Chinese beneficial ownership still needs government approval under Press Note 3. "
          "Hong Kong recipients claim the treaty rate with a Hong Kong tax residency certificate, Form 41 (formerly Form 10F) and a PAN."),
    sections=[
        ("/ Quick answers", "What Hong Kong companies and Indian founders ask.",
         ul("<strong>What is the dividend rate?</strong> 5% of the gross dividend for a Hong Kong resident beneficial owner; one summary shows 10%, so confirm against the treaty text.",
            "<strong>Interest, royalties and technical fees?</strong> 10% of the gross amount each, with interest to the governments and specified bodies exempt.",
            "<strong>Can I route Indian income through a Hong Kong company?</strong> Only with genuine substance; the anti-abuse article and India&rsquo;s general anti-avoidance rules can deny benefits to conduit structures.",
            "<strong>Does a Hong Kong investor need FDI approval?</strong> Yes, investment with Hong Kong or Chinese beneficial ownership needs prior approval; see " + L("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026) and land-border FDI") + ".",
            "<strong>From when does the treaty apply in India?</strong> It entered into force on 30 November 2018; confirm the first applicable year for withholding against the notification.")),
        ("/ Rates at a glance", "Indian tax on payments to a Hong Kong resident.",
         table(["Income", "India-Hong Kong DTAA", "Without treaty benefit"], [
             ["Dividends", "5% (confirm against the treaty text)", "20% plus surcharge and cess"],
             ["Interest", "10% (governments and specified bodies exempt)", "20% or other domestic rates plus surcharge and cess"],
             ["Royalties", "10%", "20% plus surcharge and cess"],
             ["Fees for technical services", "10%", "20% plus surcharge and cess"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Taxable if there is a business connection"]])
         + '<p>Related: ' + L("hong-kong-incorporation-indian-founder.html", "Hong Kong incorporation for Indian founders") + ', ' + L("india-china-dtaa-tax-treaty-rates-10-percent-dividend-royalty-fts-press-note-fdi-2026.html", "India-China DTAA") + ' and ' + L("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA") + '.</p>'),
        ("/ Claiming and structuring", "Documents, substance and approvals.",
         ul("<strong>Documents:</strong> a Hong Kong tax residency certificate from the Inland Revenue Department, Form 41 and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Substance:</strong> board decisions, staff and real activity in Hong Kong support treaty claims and reduce anti-abuse risk.",
            "<strong>Indian residents owning Hong Kong companies:</strong> overseas direct investment rules, Schedule FA reporting and place-of-effective-management risk apply.",
            "<strong>Investment approvals:</strong> share issues, transfers and downstream investment with Hong Kong beneficial ownership need approval before money moves.",
            "<strong>Credit in Hong Kong:</strong> check how Hong Kong treats Indian tax against its territorial system before assuming a credit.")
         + call_box("India-Hong Kong tax and investment questions", ["Treaty rate on dividends, royalties and FTS",
                                                                       "Hong Kong TRC, Form 41 and PAN",
                                                                       "Substance and anti-abuse review",
                                                                       "Press Note 3 approvals",
                                                                       "ODI and Schedule FA for Indian owners"],
                    "the recipient, the structure, the amounts and any investment plan.")
         + sources("Agreement between India and the Hong Kong Special Administrative Region for the avoidance of double taxation (signed 19 March 2018, in force 30 November 2018); EY Global Tax News (March and December 2018); India Briefing, KPMG, ClearTax, Beacon Filing, NoBroker and Dezan Shira guides; Hong Kong Inland Revenue Department treaty rate page; DPIIT Press Note 3 (2020) as summarised on the linked site page. Confirm the dividend rate and first applicable year against the treaty and notification. Checked 25 November 2026.")),
    ],
    faqs=[("What are the India-Hong Kong DTAA rates?", "Indian tax on payments to a Hong Kong resident is capped at 5% on dividends and 10% on interest, royalties and fees for technical services, with interest to the governments and specified bodies exempt. Confirm the dividend rate against the treaty text, as one summary shows 10%."),
          ("When did the India-Hong Kong DTAA come into force?", "It was signed on 19 March 2018 and entered into force on 30 November 2018. Check the notification for the first year its withholding rates apply in India."),
          ("Can a Hong Kong company invest in India without approval?", "No. Investment with Hong Kong or Chinese beneficial ownership needs prior government approval under Press Note 3 of 2020; the 2026 easing for non-controlling stakes does not cover China and Hong Kong investors."),
          ("How does a Hong Kong company claim the treaty rate in India?", "Give the Indian payer a Hong Kong tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead, and keep evidence of substance because the treaty has an anti-abuse article."),
          ("Can BQP advise on the India-Hong Kong DTAA?", "Yes. " + C)],
    related=[("hong-kong-incorporation-indian-founder.html", "Hong Kong incorporation for Indian founders"),
             ("india-china-dtaa-tax-treaty-rates-10-percent-dividend-royalty-fts-press-note-fdi-2026.html", "India-China DTAA"),
             ("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2 (2026): land-border FDI"),
             ("india-singapore-tax-treaty-dtaa.html", "India-Singapore DTAA"),
             ("what-is-dtaa.html", "What is a DTAA")],
    cta_h="Paying or receiving income between India and Hong Kong?", cta_b=C,
    keywords="India Hong Kong DTAA, India Hong Kong tax treaty, India Hong Kong DTAA rates, Hong Kong company India tax, India Hong Kong DTAA dividend, Press Note 3 Hong Kong, Hong Kong TRC India",
    desc="India-Hong Kong DTAA (2026): signed 19 March 2018, in force 30 November 2018; 5% on dividends and 10% on interest, royalties and fees for technical services; anti-abuse article; Hong Kong investment still needs Press Note 3 approval; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Hong Kong treaty", "description": "For payments to a Hong Kong resident.", "steps": [
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or business profits."},
        {"name": "Apply the treaty rate", "text": "5% on dividends, 10% on the rest, or the domestic rate if lower."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Document substance", "text": "To meet the anti-abuse article."},
        {"name": "Check investment approvals", "text": "Press Note 3 for any share issue or transfer."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch HE complete")
