# -*- coding: utf-8 -*-
"""Batch LN (28 Nov 2026): Private placement of shares under section 42 of the Companies Act - who can be offered, the 200-person
limit, special resolution, PAS-4 offer letter, PAS-5 record, separate bank account, 60-day allotment and refund rule, PAS-3 return,
valuation, and the FEMA / tax side for startups raising money.
Demand: 'private placement section 42', 'pas-4 private placement offer letter', 'pas-3 return of allotment due date', 'how to issue
shares to investors private limited company', 'allotment within 60 days' - PAS-4 / private placement mentioned on about ten pages
but no dedicated page. Startups raising angel, VC or foreign money need this done correctly. User steer 26 Nov 2026: more calls.
Facts (Companies Act, 2013 sections 42 and 62(1)(c); Companies (Prospectus and Allotment of Securities) Rules, 2014 rules 13 and 14;
Companies (Share Capital and Debentures) Rules): an offer to identified persons whose names are recorded before the invitation;
not more than 200 persons in a financial year (excluding qualified institutional buyers and employees under an ESOP scheme); a
special resolution approves the offer (filed in MGT-14); the offer letter is in Form PAS-4 and a record of offers is kept in PAS-5;
subscription money only from the subscriber's bank account, not in cash, into a separate bank account; the company cannot use the
money until allotment; allotment within 60 days of receiving the money, otherwise refund within 15 days after that, failing which
interest at 12% a year is payable from the 60th day; return of allotment in PAS-3 within 15 days of allotment; no public
advertisement or general marketing of the offer; the issue price is backed by a registered valuer's report; for foreign investors
the FEMA pricing guidelines and FC-GPR within 30 days of allotment apply (site FC-GPR page). The angel tax provision (section
56(2)(viib)) was abolished from assessment year 2025-26 (site page). No fees, no penalty amounts. advisory_lib.contact() not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "private-placement-shares-section-42-pas-4-pas-3-60-days-allotment-200-persons-startup-fundraise-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the term sheet or investment agreement, the list of "
     "investors (Indian and foreign), the proposed price and valuation report, the current shareholding and articles, and the "
     "expected date money will arrive. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Private Placement of Shares Under Section 42 (2026): Identified Investors, the 200-Person Limit, PAS-4, Separate Bank Account, 60-Day Allotment and PAS-3",
    em="money in, shares out, inside 60 days.",
    kicker="/ Startups and private companies raising money &middot; Companies Act section 42 &middot; Updated 2026-11-28",
    lead=("<strong>When a private company issues shares to new investors, it usually does so by private placement under section 42 of the Companies Act. "
          "The offer goes only to identified investors (not more than 200 in a year), is approved by special resolution, is made through a PAS-4 offer letter, and the money must come from the investor&rsquo;s bank account into a separate bank account. "
          "Shares must be allotted within 60 days of receiving the money, and the return of allotment (PAS-3) filed within 15 days of allotment.</strong>"),
    sections=[
        ("/ The section 42 process", "Step by step.",
         table(["Step", "Rule"], [
             ["Identify investors", "Names recorded before the invitation; not more than 200 persons in a year (excluding QIBs and ESOP employees)"],
             ["Valuation", "Issue price supported by a registered valuer&rsquo;s report"],
             ["Approval", "Board approval and a special resolution of shareholders (MGT-14 filed)"],
             ["Offer letter", "Form PAS-4 to each identified investor; record of offers in PAS-5"],
             ["Money", "From the investor&rsquo;s own bank account, never cash, into a separate bank account; not usable before allotment"],
             ["Allotment", "Within 60 days of receiving the money"],
             ["If not allotted", "Refund within 15 days after the 60 days, or interest at 12% a year from the 60th day"],
             ["Return of allotment", "Form PAS-3 within 15 days of allotment"]])
         + ul("<strong>No public marketing:</strong> the offer cannot be advertised or marketed to the public, and it cannot be renounced to someone else.",
              "<strong>Shareholder agreement:</strong> investor rights (board seats, vetoes, anti-dilution) need matching changes in the articles.")),
        ("/ Foreign investors, tax and common mistakes", "Where rounds get stuck.",
         ul("<strong>Foreign investors:</strong> the price must meet FEMA pricing guidelines, the sector must permit foreign investment, and FC-GPR must be filed within 30 days of allotment.",
            "<strong>Angel tax:</strong> the section 56(2)(viib) charge on premium was abolished from assessment year 2025-26, but valuation still matters for FEMA and company law.",
            "<strong>Money before paperwork:</strong> receiving funds before the special resolution and PAS-4 is a common breach - sequence the steps.",
            "<strong>Missed 60 days:</strong> refund with interest, or regularise with advice - do not simply allot late.",
            "<strong>Convertible notes and CCPS:</strong> convertible instruments follow the same private placement route, with conversion terms fixed upfront.")
         + call_box("a private placement", ["Sequencing the round from term sheet to allotment",
                                            "Valuation and board / special resolutions",
                                            "PAS-4, PAS-5 and separate bank account",
                                            "Allotment and PAS-3 within the deadlines",
                                            "FEMA pricing and FC-GPR for foreign investors"],
                    "Term sheet, investor list, valuation, shareholding, articles, funding date.")
         + sources("Companies Act, 2013 (sections 42 and 62(1)(c)); Companies (Prospectus and Allotment of Securities) Rules, 2014 (rules 13 and 14; Forms PAS-3, PAS-4, PAS-5); FEMA (Non-debt Instruments) Rules, 2019; site FC-GPR, angel tax and MGT-14 pages.")),
    ],
    faqs=[("What is private placement under section 42?", "An offer of shares or other securities by a company to a select group of identified persons, not more than 200 in a financial year (excluding QIBs and ESOP employees), made through a PAS-4 offer letter after a special resolution, without public advertisement."),
          ("What is the time limit for allotment in a private placement?", "Shares must be allotted within 60 days of receiving the application money. If not, the money must be refunded within the next 15 days, failing which interest at 12% a year is payable from the 60th day."),
          ("When is PAS-3 due?", "The return of allotment in Form PAS-3 must be filed with the Registrar within 15 days of allotment."),
          ("Can investors pay in cash or into the normal company account?", "No. Subscription money must come from the investor's own bank account, by cheque, draft or other banking channel, into a separate bank account opened for the issue. It cannot be used until shares are allotted."),
          ("What extra steps apply to foreign investors?", "The issue price must meet FEMA pricing guidelines, the sector must allow foreign investment under the automatic or approval route, and FC-GPR must be filed within 30 days of allotment."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the term sheet, investor list, proposed price and valuation report, current shareholding and articles, and the expected funding date. Or book a call directly.")],
    related=[("form-fc-gpr-filing-checklist-india-2026.html", "Form FC-GPR filing checklist"),
             ("angel-tax-abolished-effective-date-which-year-startups-section-56-2-viib-2026.html", "Angel tax abolished: which year"),
             ("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Form MGT-14 resolution filing"),
             ("raise-money-from-foreign-or-nri-investor-india-startup-issue-shares-non-resident-fema-valuation-fc-gpr-2026.html", "Raise money from a foreign or NRI investor")],
    cta_h="Raising a round and issuing shares?", cta_b=C,
    keywords="private placement section 42, pas-4 private placement offer letter, pas-3 return of allotment, allotment within 60 days, how to issue shares to investors private limited company, 200 persons private placement",
    desc="Private placement under section 42: identified investors (max 200 a year), registered valuer price, special resolution, PAS-4 offer letter, PAS-5 record, separate bank account, allotment within 60 days or refund with 12% interest, PAS-3 within 15 days, FEMA and FC-GPR for foreign investors.",
    howto={"name": "How to issue shares by private placement", "description": "From term sheet to PAS-3.", "steps": [
        {"name": "Value and approve", "text": "Registered valuer report; board approval and special resolution."},
        {"name": "Offer", "text": "PAS-4 to identified investors; record in PAS-5; open a separate bank account."},
        {"name": "Receive money", "text": "From investors' bank accounts only; do not use before allotment."},
        {"name": "Allot and file", "text": "Allot within 60 days; PAS-3 within 15 days; FC-GPR for foreign investors."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LN complete")
