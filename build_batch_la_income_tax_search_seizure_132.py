# -*- coding: utf-8 -*-
"""Batch LA (28 Nov 2026): Income tax search and seizure under section 132 (an income tax raid) - powers, rights, statements on
oath, jewellery not seized, restraint orders, and the block assessment that follows.
Demand: 'income tax raid what to do', 'income tax search and seizure section 132', 'it raid rights', 'block assessment after
search' - only mentioned in the survey page (PR #921). Highest hire intent: a searched person needs a CA immediately. User steer
26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: search under section 132 of the 1961 Act (corresponding provisions in the Income-tax Act, 2025) needs a warrant of
authorisation; officers may enter any building or place, break open locks, search persons, seize books, documents, money,
bullion, jewellery and other valuables, and place a restraint (prohibitory) order on items that cannot be seized; statements
recorded under section 132(4) are on oath and can be used as evidence; the search is recorded in a panchnama with two witnesses
and an inventory; CBDT Instruction 1916 (1994): jewellery up to 500 g per married woman, 250 g per unmarried woman and 100 g per
male member is normally not seized; block assessment reintroduced by the Finance (No. 2) Act, 2024 for searches on or after
1 September 2024 (section 158BA onwards): block period of six assessment years before the year of search plus the current year up
to the search; undisclosed income taxed at 60% under section 113 (verified by web search, incometaxindia.gov.in and Taxmann,
28 Nov 2026). No fees, no penalty amounts, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "income-tax-search-seizure-section-132-raid-what-to-do-rights-statement-jewellery-block-assessment-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com as soon as possible after a search, with the date and "
     "places searched, the panchnama and inventory of items seized, copies of statements recorded, any restraint order, and "
     "your returns for the last six years. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Search and Seizure Under Section 132 (2026): What Happens in an Income Tax Raid, Your Rights, Statements on Oath, Jewellery Limits and Block Assessment",
    em="what you sign now decides the next six years.",
    kicker="/ Business owners, professionals, families and companies &middot; Income tax search (raid) and block assessment &middot; Updated 2026-11-28",
    lead=("<strong>An income tax search under section 132 - often called a raid - is carried out under a warrant of authorisation. "
          "Officers can enter homes and offices, open lockers, seize books, cash and jewellery, and record statements on oath that can be used as evidence. "
          "For searches from 1 September 2024, a block assessment covers the six earlier years plus the current year, with undisclosed income taxed at 60%.</strong>"),
    sections=[
        ("/ During the search", "Powers and rights.",
         table(["Point", "What the law allows"], [
             ["Authority", "A warrant of authorisation; ask to see it and note the names on it"],
             ["Where", "Any building, place, vehicle or locker named or connected, including the residence"],
             ["What can be seized", "Books, documents, money, bullion, jewellery and other valuables not explained"],
             ["Items not seized", "Can be placed under a restraint (prohibitory) order"],
             ["Statements", "Recorded on oath under section 132(4); usable as evidence"],
             ["Record", "Panchnama signed in the presence of two witnesses, with an inventory of items seized"],
             ["Jewellery", "Under CBDT instructions, up to 500 g per married woman, 250 g per unmarried woman and 100 g per male member is normally not seized"]])
         + ul("<strong>Stay calm and cooperative:</strong> do not destroy or hide anything, and do not obstruct the team.",
              "<strong>Read before you sign:</strong> check the panchnama and inventory against what was actually taken, and ask for copies.",
              "<strong>Answer only what you know:</strong> a statement on oath carries weight; say that records will be produced rather than guessing figures or offering income on the spot.")),
        ("/ After the search", "Block assessment and what to do.",
         ul("<strong>Block assessment:</strong> for searches on or after 1 September 2024, the officer assesses a block period of six assessment years before the year of search plus the current year up to the search; undisclosed income is taxed at 60% under section 113.",
            "<strong>Statements:</strong> a statement made under pressure or by mistake should be retracted promptly with reasons and evidence; delay weakens a retraction.",
            "<strong>Seized cash and assets:</strong> explain the source with records - books, bank statements, gift deeds, sale deeds, earlier returns - and apply for release where they are explained.",
            "<strong>Restraint orders:</strong> track their validity and seek release of items that are explained.",
            "<strong>Plan the return for the block period:</strong> the figures you file and the explanations you give will be tested against seized material.")
         + call_box("an income tax search", ["Guidance right after the search",
                                              "Review and retraction of statements",
                                              "Explaining seized cash, jewellery and documents",
                                              "Block period return and assessment",
                                              "Release of seized assets and appeals"],
                    "Search date, panchnama and inventory, statements, restraint orders, last six years of returns.")
         + sources("Income-tax Act, 1961 (sections 132, 113 and 158BA to 158BI as reintroduced by the Finance (No. 2) Act, 2024) and the corresponding provisions of the Income-tax Act, 2025; CBDT Instruction No. 1916 on seizure of jewellery; site survey, notice reply and reassessment pages.")),
    ],
    faqs=[("What happens during an income tax raid?", "Officers arrive with a warrant of authorisation, search the premises named (homes, offices, lockers, vehicles), seize unexplained books, cash, jewellery and other valuables, record statements on oath and prepare a panchnama with an inventory signed in front of two witnesses."),
          ("What is the difference between an income tax survey and a search?", "A survey under section 133A is limited to business premises, allows no seizure of cash, jewellery or stock, and statements are not on oath. A search under section 132 needs a warrant, can cover a residence, allows seizure, and statements are on oath."),
          ("How much jewellery can be kept during an income tax search?", "Under CBDT instructions, jewellery up to 500 g per married woman, 250 g per unmarried woman and 100 g per male member of the family is normally not seized, even without proof. More can be left if its source is explained."),
          ("What is block assessment after a search?", "For searches on or after 1 September 2024, the officer assesses a block period of six assessment years before the year of search plus the current year up to the date of search. Undisclosed income found is taxed at 60%."),
          ("Can I retract a statement given during a search?", "Yes, but it must be done promptly, in writing, with reasons and evidence. A statement on oath is strong evidence, so a late or unsupported retraction carries little weight."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the search date and places, the panchnama and inventory, copies of statements, any restraint order and your last six years of returns. Or book a call directly.")],
    related=[("income-tax-survey-section-133a-what-officers-can-do-statement-impounding-books-survey-vs-search-2026.html", "Income tax survey under section 133A"),
             ("section-148-148a-reassessment-notice-response-india.html", "Reassessment notice under section 148"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("income-tax-appeal-cit-appeals-form-35-form-99-time-limit-30-days-fee-20-percent-pre-deposit-2026.html", "Appeal to CIT(A)")],
    cta_h="Income tax search at your home or office?", cta_b=C,
    keywords="income tax raid what to do, income tax search and seizure section 132, rights during income tax raid, jewellery limit income tax search, block assessment after search 2024, statement on oath 132(4), panchnama income tax",
    desc="Income tax search and seizure under section 132: warrant, what can be seized, restraint orders, statements on oath, panchnama, jewellery not seized (500 g / 250 g / 100 g), and block assessment for searches from 1 September 2024 with undisclosed income taxed at 60%.",
    howto={"name": "How to handle an income tax search", "description": "During and after.", "steps": [
        {"name": "See the warrant", "text": "Note the authorisation and the names on it; cooperate."},
        {"name": "Check what you sign", "text": "Match the panchnama and inventory with what is taken; get copies."},
        {"name": "Review statements", "text": "Retract promptly in writing if a statement was wrong."},
        {"name": "Prepare the block return", "text": "Explain seized assets with records; plan the block period return."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LA complete")
