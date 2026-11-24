# -*- coding: utf-8 -*-
"""Batch GV (24 Nov 2026): India-France DTAA and the amending protocol signed 23 February 2026 - current treaty rates
(10% on dividends, interest, royalties and fees for technical services), what the protocol changes once in force
(dividends 5% for holdings of at least 10% held 365 days and 15% otherwise; full taxing rights on share gains for the
company's country; MFN clause deleted; service PE; FTS aligned with the India-US make-available standard; MLI-style
anti-abuse), status (enters into force the day after the later notification; check whether notified), and how to claim.
Demand: sweep ac94 (24 Nov 2026), all 7 markets: "india france dtaa", "india france dtaa amendment effective date",
"india france dtaa article 13", "india france dtaa income tax".
Facts (checked 24 Nov 2026): Ministry of Finance / News On AIR (signed 23 February 2026 by CBDT chairperson and the French
ambassador, amending the 1992 convention); Business Today, Free Press Journal, India Briefing, KPMG, EY, Khaitan, BDO,
Forvis Mazars, CMS: dividend split 5%/15% with 10% holding for 365 days, full source taxing rights on share gains, MFN
deleted, service PE, FTS aligned with the India-US treaty; entry into force the day after the later notification of
completion of procedures; one note says ratification and notification pending. Pre-protocol rates 10%."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "india-france-dtaa-2026-amending-protocol-dividend-5-15-capital-gains-mfn-removed-rates"

C = contact("whether you are a French company, a French resident or an Indian resident, the income type (dividend, interest, royalty, technical fees, share sale), the holding and amounts, and the payment dates")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="India-France DTAA (2026): The Amending Protocol, New Dividend Rates of 5% and 15%, Capital Gains on Shares and MFN Removal",
    em="the 1992 treaty is being rewritten: check which version applies to each payment.",
    kicker="/ French companies and NRIs in France &middot; DTAA &middot; Updated 2026-11-24",
    lead=("<strong>India and France signed a protocol on 23 February 2026 to amend their 1992 double tax avoidance convention.</strong> "
          "Once in force it replaces the flat 10% dividend rate with 5% for a company holding at least 10% of the capital (for 365 days) and 15% in other cases, gives the country where a company is resident full rights to tax gains on its shares, deletes the most-favoured-nation clause, adds a service permanent establishment rule and aligns fees for technical services with the India-US &ldquo;make available&rdquo; standard. "
          "The protocol enters into force the day after the later of the two countries&rsquo; notifications, so until it is notified the existing rates apply: 10% on dividends, interest, royalties and fees for technical services. Check the status before applying a new rate."),
    sections=[
        ("/ Quick answers", "What French investors and NRIs ask.",
         ul("<strong>When does the amendment take effect?</strong> On the day after the later notification that both countries have completed their procedures; its provisions then apply from the dates set in the protocol, so confirm notification before relying on it.",
            "<strong>What happens to dividends?</strong> 5% for a company holding at least 10% of the capital for 365 days including the payment date, and 15% in all other cases, instead of 10%.",
            "<strong>What about capital gains on shares (Article 14)?</strong> India gets full taxing rights on gains from shares of Indian companies, whatever the size of the holding, once the protocol applies; earlier the source country's right depended on the size of the participation.",
            "<strong>Is the MFN clause gone?</strong> Yes. The protocol deletes it, after the Supreme Court held in 2023 that MFN benefits need a separate notification.",
            "<strong>What about technical fees?</strong> The definition moves closer to the India-US treaty, which covers services only if they make available technical knowledge, and a service PE rule is added.")),
        ("/ Old and new rules", "Indian tax on payments to a French resident.",
         table(["Item", "1992 treaty (until the protocol applies)", "After the 2026 protocol applies"], [
             ["Dividends", "10%", "5% (holding of 10% or more for 365 days) or 15%"],
             ["Interest", "10%", "No change reported in the headline terms"],
             ["Royalties and FTS", "10%", "FTS definition aligned with the India-US make-available standard"],
             ["Gains on shares", "Source taxation depended on the participation", "Full taxing rights for the company's country"],
             ["MFN clause", "In the protocol to the treaty", "Deleted"],
             ["Permanent establishment", "Standard PE rules", "Service PE added"]])
         + '<p>Related: ' + L("what-is-dtaa.html", "what a DTAA is") + ', ' + L("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA") + ' and ' + L("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and the MFN issue") + '.</p>'),
        ("/ What to do now", "Practical steps.",
         ul("<strong>Payments before entry into force:</strong> claim the 10% treaty rate with a French tax residency certificate, Form 41 (formerly Form 10F) and a PAN; see " + L("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "tax residency certificates") + ".",
            "<strong>French parent companies:</strong> check whether the 10% holding and 365-day conditions will be met to plan dividends under the 5% rate.",
            "<strong>Portfolio investors and share sales:</strong> model the loss of treaty protection on gains from Indian shares once the protocol applies.",
            "<strong>Service providers:</strong> review days in India and service contracts against the new service PE rule and the revised FTS definition.",
            "<strong>MFN claims:</strong> stop relying on MFN-based lower rates for French payments.")
         + call_box("India-France treaty questions", ["Which treaty version applies to a payment",
                                                        "Dividend planning for French parents",
                                                        "Capital gains on Indian shares",
                                                        "Service PE and FTS review",
                                                        "TRC, Form 41 and PAN"],
                    "the recipient, the payment type, the holding and the dates.")
         + sources("Convention between India and France for the avoidance of double taxation (1992) and the Amending Protocol signed 23 February 2026 (Ministry of Finance press release; News On AIR); analysis from Business Today, Free Press Journal, India Briefing, KPMG, EY, Khaitan &amp; Co, BDO, Forvis Mazars and CMS (February to June 2026). The protocol text and its notification should be checked for exact dates. Checked 24 November 2026.")),
    ],
    faqs=[("What does the India-France DTAA amending protocol change?", "Signed on 23 February 2026, it replaces the 10% dividend rate with 5% for a company holding at least 10% of the capital for 365 days and 15% otherwise, gives the company's country full rights to tax gains on its shares, deletes the MFN clause, adds a service PE rule and aligns fees for technical services with the India-US make-available standard."),
          ("When is the India-France DTAA amendment effective?", "The protocol enters into force on the day after the later of the notifications by India and France that their procedures are complete, and applies from the dates set in it. Until it is notified, the 1992 treaty rates apply, so check the status for each payment."),
          ("What are the current India-France DTAA rates?", "Under the 1992 treaty, Indian tax on dividends, interest, royalties and fees for technical services paid to a French resident is capped at 10%, claimed with a French TRC, Form 41 and a PAN."),
          ("How does the protocol affect capital gains on Indian shares?", "Once it applies, India can tax gains made by French residents on shares of Indian companies regardless of the size of the holding; earlier the source country's right depended on the participation."),
          ("Can BQP advise on the India-France DTAA?", "Yes. " + C)],
    related=[("what-is-dtaa.html", "What is a DTAA"),
             ("india-netherlands-dtaa-tax-treaty-nri-company-rates-mfn-nestle-2026.html", "India-Netherlands DTAA and MFN"),
             ("india-germany-dtaa-tax-treaty-nri-company-rates-10-percent-2026.html", "India-Germany DTAA"),
             ("india-japan-dtaa-tax-treaty-rates-dividend-interest-royalty-fts-article-12-2026.html", "India-Japan DTAA"),
             ("tax-residency-certificate-india-form-42-43-10fa-10fb-freelancer-youtube-2026.html", "Tax residency certificates")],
    cta_h="Investing or paying between India and France?", cta_b=C,
    keywords="India France DTAA, India France DTAA amendment, India France tax treaty protocol 2026, India France DTAA dividend rate, India France DTAA capital gains, India France MFN clause, India France DTAA effective date",
    desc="India-France DTAA (2026): the amending protocol signed 23 February 2026 sets dividends at 5% (10% holding for 365 days) or 15%, gives full taxing rights on share gains to the company's country, deletes the MFN clause, adds service PE and aligns FTS with the India-US treaty; until notified, 10% rates apply.",
    howto={"name": "How to apply the India-France treaty in 2026", "description": "For payments to a French resident.", "steps": [
        {"name": "Check the protocol status", "text": "Whether it has been notified and from when it applies."},
        {"name": "Identify the income type", "text": "Dividend, interest, royalty, FTS or share gain."},
        {"name": "Test the dividend conditions", "text": "10% holding for 365 days for the 5% rate."},
        {"name": "Collect TRC, Form 41 and PAN", "text": "Before the Indian payer deducts tax."},
        {"name": "Review PE and FTS", "text": "Service PE and the make-available definition."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GV complete")
