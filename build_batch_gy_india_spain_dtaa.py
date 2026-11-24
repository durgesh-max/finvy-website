# -*- coding: utf-8 -*-
"""Batch GY (24 Nov 2026): India-Spain DTAA - royalties and fees for technical services cut to 10% by Notification
No. 33/2024 (19 March 2024) giving effect to the MFN clause (rate imported from the India-Germany treaty), applying from
tax year 2023-24, with refunds for excess withholding; royalties and FTS sit in Article 13 of this treaty; definitions
unchanged; dividends and interest at the treaty rates (reported as 15%); how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india spain dtaa", "india vs spain dtaa", "india spain dtaa income tax
website", "india spain dtaa pdf".
Facts (checked 24 Nov 2026): Notification No. 33/2024 dated 19 March 2024 (Deloitte, EY, KPMG, PwC, BDO, Taxmann, LiveLaw,
AZB, Khaitan, Mondaq, India Briefing): royalty and FTS rate under Article 13(2) reduced to 10% via MFN (India-Germany),
previously 10% for equipment royalties and 20% otherwise; applies from tax year 2023-24; definitions not changed; refunds
via Indian return. Dividends and interest stated as 15% as commonly reported (not re-verified this round; caveat on page)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-spain-dtaa-tax-treaty-royalty-fts-10-percent-mfn-notification-33-2024-rates"

C = contact("whether you are a Spanish company, a Spanish resident or an Indian resident, the income type (royalty, technical fees, dividend, interest or gains), the amounts and years, and whether tax above 10% was withheld")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-Spain DTAA (2026): Royalties and Technical Fees at 10% Under the MFN Notification, Dividend and Interest Rates, and How to Claim",
    em="royalties and technical fees fell to 10%, and past excess withholding can be refunded.",
    kicker="/ Spanish companies and NRIs in Spain &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>Under Notification No. 33/2024 of 19 March 2024, India gave effect to the most-favoured-nation clause in its treaty with Spain and cut the rate on royalties and fees for technical services paid to a Spanish resident to 10%, importing the rate from the India-Germany treaty.</strong> "
          "Before that, the treaty allowed 10% only on equipment royalties and 20% on other royalties and technical fees. The lower rate applies from tax year 2023-24, so Spanish recipients who suffered more than 10% can claim the excess by filing an Indian return. "
          "In this treaty royalties and technical fees sit in Article 13, and their definitions were not changed by the notification. Dividends and interest stay at the treaty rates, commonly reported as 15%."),
    sections=[
        ("/ Quick answers", "What Spanish companies and NRIs ask.",
         ul("<strong>What is the rate on royalties and technical fees?</strong> 10% of the gross amount for a Spanish resident beneficial owner, from tax year 2023-24 under Notification No. 33/2024.",
            "<strong>Why did it change?</strong> The treaty's MFN clause, which India now applies only after a separate notification following the Supreme Court's 2023 ruling, was given effect for Spain in March 2024.",
            "<strong>Did the definitions change?</strong> No. Only the rate was reduced; what counts as royalty or technical fees under the Spain treaty stays the same.",
            "<strong>Can I get a refund for earlier withholding?</strong> Yes, for years from 2023-24 where tax above 10% was withheld, by filing an Indian return and claiming the treaty rate.",
            "<strong>What about dividends and interest?</strong> Treaty rates, commonly reported as 15%; compare with the domestic rate and check the treaty text.")),
        ("/ Rates at a glance", "Indian tax on payments to a Spanish resident.",
         table(["Income", "India-Spain DTAA now", "Before the 2024 notification"], [
             ["Royalties", "10% (Article 13, MFN notification)", "10% for equipment royalties, 20% for others"],
             ["Fees for technical services", "10% (Article 13, MFN notification)", "20%"],
             ["Dividends", "Treaty rate, commonly reported as 15%", "Same"],
             ["Interest", "Treaty rate, commonly reported as 15%", "Same"],
             ["Business profits", "Taxable in India only with a permanent establishment", "Same"]])
         + '<p>Related: ' + L("india-switzerland-dtaa-tax-treaty-rates-mfn-suspended-2025-nestle-dividend-10-percent.html", "India-Switzerland DTAA and the MFN suspension") + ', ' + L("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and the Nestle ruling") + ' and ' + L("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA") + '.</p>'),
        ("/ Claiming and refunds", "Documents and next steps.",
         ul("<strong>Documents:</strong> a Spanish tax residency certificate, Form 41 (formerly Form 10F) and a PAN or the documents allowed instead; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>Indian payers</strong> can deduct TDS at 10% on royalties and technical fees once the documents are in place.",
            "<strong>Refunds:</strong> file an Indian return for each year from 2023-24 where tax above 10% was withheld, with the TRC and Form 41.",
            "<strong>Scope check:</strong> because definitions did not change, confirm the payment is royalty or technical fees under the Spain treaty, not business profits taxable only with a PE.",
            "<strong>Credit in Spain:</strong> Indian tax at the treaty rate is generally creditable against Spanish tax on the same income.")
         + call_box("India-Spain treaty questions", ["10% rate on royalties and technical fees",
                                                       "Refunds for 2023-24 onwards",
                                                       "TRC, Form 41 and PAN",
                                                       "Royalty vs business profits",
                                                       "Dividend and interest planning"],
                    "the recipient, the payment type, the amounts and the years.")
         + sources("Agreement between India and Spain for the avoidance of double taxation (1993); Notification No. 33/2024 dated 19 March 2024 (CBDT); analysis from Deloitte, EY, KPMG, PwC, BDO, Taxmann, LiveLaw, AZB &amp; Partners, Khaitan &amp; Co, Mondaq and India Briefing (2024). Dividend and interest rates as commonly reported; check the treaty text. Checked 24 November 2026.")),
    ],
    faqs=[("What is the India-Spain DTAA rate on royalties and fees for technical services?", "10% of the gross amount for a Spanish resident, under Notification No. 33/2024 of 19 March 2024, which gave effect to the treaty's MFN clause using the India-Germany rate. It applies from tax year 2023-24."),
          ("What was the rate before the 2024 notification?", "10% for royalties for industrial, commercial or scientific equipment and 20% for other royalties and fees for technical services."),
          ("Can Spanish companies get a refund of excess Indian tax?", "Yes. For years from 2023-24 where tax above 10% was withheld on royalties or technical fees, file an Indian income tax return claiming the treaty rate, with a Spanish TRC and Form 41."),
          ("Did the notification change the definitions of royalty and technical fees?", "No. It only reduced the rate. The definitions in the India-Spain treaty, where royalties and technical fees are covered in Article 13, stay as they were."),
          ("Can BQP advise on the India-Spain DTAA?", "Yes. " + C)],
    related=[("india-switzerland-dtaa-tax-treaty-rates-mfn-suspended-2025-nestle-dividend-10-percent.html", "India-Switzerland DTAA"),
             ("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and MFN"),
             ("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA"),
             ("india-italy-dtaa-tax-treaty-rates-dividend-15-interest-royalty-fts-20-article-13-2026.html", "India-Italy DTAA"),
             ("what-is-dtaa.html", "What is a DTAA")],
    cta_h="Paying or receiving royalties or fees between India and Spain?", cta_b=C,
    keywords="India Spain DTAA, India Spain tax treaty, India Spain DTAA royalty rate, India Spain DTAA fees for technical services, Notification 33/2024, India Spain MFN, India vs Spain DTAA",
    desc="India-Spain DTAA (2026): royalties and fees for technical services cut to 10% by Notification No. 33/2024 under the MFN clause (from tax year 2023-24, refunds for excess withholding); definitions unchanged in Article 13; dividends and interest at treaty rates; how to claim with TRC, Form 41 and PAN.",
    howto={"name": "How to apply the India-Spain treaty", "description": "For royalties and technical fees paid to a Spanish resident.", "steps": [
        {"name": "Confirm the payment type", "text": "Royalty or technical fees under the Spain treaty definitions."},
        {"name": "Apply 10%", "text": "Under Notification No. 33/2024, from tax year 2023-24."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Claim refunds", "text": "Through an Indian return for years with excess withholding."},
        {"name": "Claim credit in Spain", "text": "For Indian tax at the treaty rate."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GY complete")
