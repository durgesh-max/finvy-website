# -*- coding: utf-8 -*-
"""Batch LR (28 Nov 2026): Rights issue and bonus issue of shares in a private company - section 62(1)(a) rights (proportionate
offer, 15 to 30 day window, renunciation, private company shorter period), section 63 bonus (sources, conditions, two-month
implementation), PAS-3, and the tax and FEMA side.
Demand: 'rights issue private company', 'bonus issue of shares procedure', 'section 63 bonus shares', 'rights issue section 62 1 a',
'bonus shares tax' - 0 dedicated pages. Common way for founders to bring in more money from existing shareholders or capitalise
reserves. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 sections 39, 62(1)(a) and 63; Companies (Share Capital and Debentures) Rules, 2014 rule 14; MCA private
company exemption notification of 5 June 2015 as amended): rights issue - offered to existing equity shareholders in proportion to
their holdings by a letter of offer, open for at least 15 and not more than 30 days, with a right to renounce in favour of others
unless the articles provide otherwise; a private company can have a shorter period if 90% of members consent; approved by the board;
bonus issue - out of free reserves, the securities premium account or the capital redemption reserve (not revaluation reserves);
authorised by the articles; recommended by the board and approved in a general meeting; partly paid shares must be fully paid; no
default on deposits, debt securities or statutory employee dues; not in lieu of dividend; once announced, cannot be withdrawn;
implemented within two months of board approval (or of shareholder approval where needed); return of allotment PAS-3 within 30 days
of allotment; authorised capital must cover the new shares. Tax: bonus shares have nil cost and their holding period runs from
allotment. FEMA: rights to non-residents at a price not lower than that offered to residents; FC-GPR within 30 days. No fees, no
stamp duty amounts. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "rights-issue-bonus-issue-shares-private-company-section-62-1-a-section-63-procedure-pas-3-tax-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current shareholding, the articles, the latest "
     "balance sheet (reserves and securities premium), the amount or ratio you have in mind, and whether any shareholder is a "
     "non-resident. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Rights Issue and Bonus Issue of Shares (2026): Section 62(1)(a) and Section 63 Procedure, Timelines, PAS-3, Tax and Foreign Shareholders",
    em="new money from existing owners, or reserves turned into shares.",
    kicker="/ Private companies and their shareholders &middot; Companies Act sections 62 and 63 &middot; Updated 2026-11-28",
    lead=("<strong>A rights issue offers new shares to existing shareholders in proportion to what they hold - the simplest way to raise money from the current owners. "
          "A bonus issue gives free shares by converting free reserves or securities premium into share capital. "
          "Both need the authorised capital to cover the new shares and a PAS-3 return within 30 days of allotment.</strong>"),
    sections=[
        ("/ Rights issue vs bonus issue", "Sections 62(1)(a) and 63.",
         table(["Point", "Rights issue (s.62(1)(a))", "Bonus issue (s.63)"], [
             ["Money in", "Yes - shareholders pay for the shares", "No - reserves are capitalised"],
             ["Who gets it", "Existing equity shareholders, in proportion", "Existing shareholders, in proportion"],
             ["Approval", "Board resolution", "Board recommendation and general meeting approval; articles must allow"],
             ["Offer window", "15 to 30 days; shorter in a private company with 90% members&rsquo; consent", "Not applicable"],
             ["Renunciation", "Allowed unless the articles say otherwise", "Not applicable"],
             ["Source", "Fresh subscription money", "Free reserves, securities premium or capital redemption reserve - not revaluation reserves"],
             ["Conditions", "Authorised capital headroom", "Partly paid shares fully paid; no default on deposits, debt or statutory employee dues; not in lieu of dividend"],
             ["Timeline", "Allot after the offer closes", "Implement within two months of approval; cannot be withdrawn once announced"],
             ["Filing", "PAS-3 within 30 days of allotment", "PAS-3 within 30 days of allotment"]])
         + ul("<strong>Check authorised capital first:</strong> increase it (and file SH-7) before the allotment if the new shares would exceed it.",
              "<strong>Rights vs private placement:</strong> offering shares to someone other than existing shareholders in proportion is a private placement under section 42, with its own process.")),
        ("/ Tax and foreign shareholders", "Before you price it.",
         ul("<strong>Bonus shares:</strong> no tax on receipt for ordinary shareholders; cost is nil and the holding period runs from allotment, which matters on a later sale.",
            "<strong>Rights at a low price:</strong> a proportionate rights issue is generally neutral, but disproportionate subscription or renunciation at below fair value can raise tax questions - plan the pricing.",
            "<strong>Non-resident shareholders:</strong> rights shares to non-residents cannot be priced below the price offered to residents, the sector must allow foreign investment, and FC-GPR is filed within 30 days.",
            "<strong>Renounced rights:</strong> a renouncee who is new to the company should be checked for FEMA and KYC before allotment.",
            "<strong>Records:</strong> update the register of members, issue share certificates or credit demat accounts, and keep board and meeting minutes.")
         + call_box("a rights or bonus issue", ["Choosing rights, bonus or private placement",
                                                "Authorised capital and articles check",
                                                "Letter of offer or bonus resolutions",
                                                "PAS-3 and share certificates / demat",
                                                "FEMA pricing and FC-GPR for non-residents"],
                    "Shareholding, articles, balance sheet, proposed amount or ratio, residency of shareholders.")
         + sources("Companies Act, 2013 (sections 39, 61, 62(1)(a) and 63); Companies (Share Capital and Debentures) Rules, 2014 (rule 14); MCA private company exemption notification, 5 June 2015 as amended; FEMA (Non-debt Instruments) Rules, 2019; site private placement, authorised capital and FC-GPR pages.")),
    ],
    faqs=[("What is a rights issue in a private company?", "An offer of new shares to existing equity shareholders in proportion to their holdings, made by a letter of offer open for 15 to 30 days, approved by the board. Shareholders can renounce their entitlement unless the articles prohibit it."),
          ("Can a private company keep the rights issue open for less than 15 days?", "Yes, if at least 90% of the members consent in writing or electronically, under the exemption available to private companies."),
          ("From which reserves can bonus shares be issued?", "From free reserves, the securities premium account or the capital redemption reserve. Bonus shares cannot be issued out of revaluation reserves."),
          ("What is the time limit to complete a bonus issue?", "The bonus issue must be implemented within two months of the board approval, or of shareholder approval where that is required, and once announced it cannot be withdrawn."),
          ("Are bonus shares taxable?", "Receiving bonus shares is generally not taxed for ordinary shareholders. Their cost is treated as nil and the holding period runs from the date of allotment, which affects capital gains on a later sale."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the shareholding, articles, latest balance sheet, proposed amount or ratio and residency of shareholders. Or book a call directly.")],
    related=[("increase-authorised-share-capital-sh-7-section-61-64-ordinary-resolution-30-days-before-fundraise-2026.html", "Increase authorised share capital (SH-7)"),
             ("private-placement-shares-section-42-pas-4-pas-3-60-days-allotment-200-persons-startup-fundraise-2026.html", "Private placement under section 42"),
             ("form-fc-gpr-filing-checklist-india-2026.html", "Form FC-GPR filing checklist"),
             ("form-sh-4-share-transfer-form-india-2026.html", "Form SH-4 share transfer")],
    cta_h="Planning a rights or bonus issue?", cta_b=C,
    keywords="rights issue private company, bonus issue of shares procedure, section 63 bonus shares, rights issue section 62 1 a, bonus shares tax india, rights issue 15 days private company, pas-3 30 days",
    desc="Rights issue and bonus issue of shares: section 62(1)(a) proportionate offer open 15-30 days (shorter with 90% consent in private companies), renunciation; section 63 bonus from free reserves, securities premium or CRR, two-month implementation; PAS-3 within 30 days; tax on bonus shares; FEMA for non-residents.",
    howto={"name": "How to do a rights or bonus issue", "description": "Check, approve, allot, file.", "steps": [
        {"name": "Check capital and articles", "text": "Authorised capital headroom; articles permit the issue."},
        {"name": "Approve", "text": "Board resolution for rights; board recommendation and general meeting for bonus."},
        {"name": "Offer or capitalise", "text": "Letter of offer for 15-30 days, or capitalise reserves within two months."},
        {"name": "Allot and file", "text": "PAS-3 within 30 days; update registers; FC-GPR for non-residents."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LR complete")
