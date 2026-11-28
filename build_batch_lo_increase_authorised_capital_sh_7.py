# -*- coding: utf-8 -*-
"""Batch LO (28 Nov 2026): Increase of authorised share capital - section 61(1)(a), articles permission, ordinary resolution in a
general meeting, alteration of the capital clause of the memorandum, Form SH-7 within 30 days under section 64, and why it must
come before a fundraise or bonus issue.
Demand: 'increase authorised capital', 'sh-7 form', 'how to increase authorised share capital private limited company', 'sh-7
due date', 'authorised vs paid up capital' - 0 dedicated pages (mentioned on about twelve pages). A routine step before every round
that founders need done correctly. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 sections 13, 61, 64 and 117): a company can increase its authorised share capital under section 61(1)(a)
if its articles authorise it; the increase is approved by an ordinary resolution in a general meeting unless the articles require a
special resolution (then MGT-14 is also filed within 30 days); the capital clause of the memorandum is altered accordingly; notice of
the alteration in Form SH-7 is filed with the Registrar within 30 days of the resolution, with the altered memorandum (and articles
if changed); an extraordinary general meeting needs 21 clear days notice, or shorter notice with the consent of members as the Act
requires; the authorised capital must cover any allotment, conversion or bonus issue before it is made; stamp duty and Registrar fees
apply and vary (not stated). Authorised capital is the ceiling; issued / paid-up capital is what has actually been allotted and paid.
No fees, no stamp duty amounts, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "increase-authorised-share-capital-sh-7-section-61-64-ordinary-resolution-30-days-before-fundraise-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the current memorandum and articles, the present "
     "authorised and paid-up capital, the planned allotment, conversion or bonus issue, and the date you need it done by. Or book "
     "a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Increase Authorised Share Capital (2026): Section 61, Ordinary Resolution, Altering the Memorandum, Form SH-7 Within 30 Days and Doing It Before a Fundraise",
    em="raise the ceiling before you issue shares.",
    kicker="/ Private and public companies &middot; Companies Act sections 61 and 64 &middot; Updated 2026-11-28",
    lead=("<strong>Authorised capital is the ceiling on the shares a company can issue. Before an allotment, conversion of notes or preference shares, or a bonus issue that would cross that ceiling, the company must increase its authorised capital under section 61. "
          "That needs permission in the articles, an ordinary resolution in a general meeting (special, if the articles say so), a change to the capital clause of the memorandum, and Form SH-7 filed with the Registrar within 30 days.</strong>"),
    sections=[
        ("/ The steps", "Sections 61 and 64.",
         table(["Step", "Rule"], [
             ["Check the articles", "They must authorise an increase; amend them first if they do not"],
             ["Board meeting", "Approve the proposal and call a general meeting"],
             ["General meeting", "Ordinary resolution, unless the articles require a special resolution; 21 clear days notice or shorter notice with members&rsquo; consent as the Act allows"],
             ["Alter the memorandum", "Replace the capital clause with the new authorised capital"],
             ["Form SH-7", "File with the Registrar within 30 days of the resolution, with the altered memorandum (and articles if changed)"],
             ["MGT-14", "Also within 30 days if a special resolution was passed"],
             ["Then allot", "Only after the increase is effective, issue shares within the new limit"]])
         + ul("<strong>Authorised vs paid-up:</strong> authorised capital is the maximum; paid-up capital is what investors and founders have actually subscribed and paid.",
              "<strong>Stamp duty and fees:</strong> the increase attracts stamp duty and Registrar fees that depend on the amount and the state - plan the size of the increase with that in mind.")),
        ("/ Timing it with a round", "Where founders get stuck.",
         ul("<strong>Sequence:</strong> increase authorised capital, then pass the private placement resolutions, receive the money and allot - in that order.",
            "<strong>Convertibles and CCPS:</strong> keep enough headroom for conversion of notes, CCPS and the ESOP pool, so a later conversion does not stall.",
            "<strong>Bonus issues:</strong> the authorised capital must cover the bonus shares before the board allots them.",
            "<strong>Classes of shares:</strong> if adding preference shares or a new class, the memorandum and articles must reflect it.",
            "<strong>Late SH-7:</strong> filing after 30 days attracts additional fees and keeps the allotment exposed - file promptly.")
         + call_box("an increase in authorised capital", ["Checking the articles and memorandum",
                                                          "Board and general meeting resolutions",
                                                          "Altered capital clause",
                                                          "SH-7 (and MGT-14) within 30 days",
                                                          "Sequencing with the fundraise or bonus issue"],
                    "Memorandum, articles, current capital, planned issue, timeline.")
         + sources("Companies Act, 2013 (sections 13, 61, 64 and 117); Companies (Share Capital and Debentures) Rules, 2014; Form SH-7; site private placement, MGT-14 and ROC compliance pages.")),
    ],
    faqs=[("How do I increase the authorised share capital of a private limited company?", "Check that the articles allow it, hold a board meeting to call a general meeting, pass an ordinary resolution (or a special resolution if the articles require), alter the capital clause of the memorandum, and file Form SH-7 with the Registrar within 30 days of the resolution."),
          ("What is the due date for Form SH-7?", "Within 30 days of the shareholders' resolution approving the increase. If a special resolution was passed, MGT-14 is also due within 30 days."),
          ("Is a special resolution needed to increase authorised capital?", "Not usually. An ordinary resolution in a general meeting is enough, unless the company's articles require a special resolution."),
          ("What is the difference between authorised and paid-up capital?", "Authorised capital is the maximum share capital the company can issue under its memorandum. Paid-up capital is the part actually allotted to and paid for by shareholders."),
          ("Do I need to increase authorised capital before a funding round?", "Yes, if the new shares, conversions or ESOP pool would take total issued capital above the current authorised capital. The increase must be effective before allotment."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the memorandum and articles, current authorised and paid-up capital, the planned issue and your timeline. Or book a call directly.")],
    related=[("private-placement-shares-section-42-pas-4-pas-3-60-days-allotment-200-persons-startup-fundraise-2026.html", "Private placement under section 42"),
             ("form-mgt-14-board-shareholder-resolution-filing-india-2026.html", "Form MGT-14 resolution filing"),
             ("form-sh-4-share-transfer-form-india-2026.html", "Form SH-4 share transfer"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar")],
    cta_h="Need more authorised capital before your next issue?", cta_b=C,
    keywords="increase authorised capital, sh-7 form, how to increase authorised share capital private limited company, sh-7 due date 30 days, authorised vs paid up capital, section 61 companies act",
    desc="Increase authorised share capital: articles permission, board meeting, ordinary resolution in a general meeting (special if articles require), altered capital clause, Form SH-7 within 30 days under section 64, MGT-14 if special resolution, and doing it before a fundraise, conversion or bonus issue.",
    howto={"name": "How to increase authorised share capital", "description": "Before the next allotment.", "steps": [
        {"name": "Check articles", "text": "Confirm they authorise an increase; amend if needed."},
        {"name": "Pass resolutions", "text": "Board meeting, then ordinary (or special) resolution in a general meeting."},
        {"name": "Alter memorandum", "text": "Update the capital clause."},
        {"name": "File SH-7", "text": "Within 30 days, with altered memorandum; MGT-14 if special resolution."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LO complete")
