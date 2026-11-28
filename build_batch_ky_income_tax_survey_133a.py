# -*- coding: utf-8 -*-
"""Batch KY (28 Nov 2026): Income tax survey under section 133A - what officers can and cannot do, statements, impounding of
books, survey vs search, and what happens after.
Demand: 'income tax survey', 'income tax survey under section 133a', 'it survey at business premises what to do', 'difference
between survey and search income tax' - no page on the site (grep for 133A / survey: none). High hire intent: a business owner
facing or just after a survey needs a CA immediately. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (section 133A of the 1961 Act; corresponding provisions in the Income-tax Act, 2025): authorities may enter a place where
business or profession is carried on (or where books, cash or stock are kept) - business premises during business hours, other
places between sunrise and sunset; inspect books, verify cash and stock, place marks of identification, take extracts or copies,
and record statements; books can be impounded with reasons recorded, and retained beyond fifteen days (excluding holidays) only
with higher approval; a survey cannot seize cash, jewellery or stock (that is a search under section 132); a statement recorded
in a survey is not on oath and courts have held it is not conclusive evidence on its own; undisclosed income admitted can be taxed
at the special rate under section 115BBE. No fees, no penalty amounts, no portal menu paths. advisory_lib.contact() not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "income-tax-survey-section-133a-what-officers-can-do-statement-impounding-books-survey-vs-search-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com as soon as a survey starts or ends, with the survey "
     "date and premises, the inventory or list of books impounded, copies of any statements recorded, and your last two "
     "years' returns and books. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Survey Under Section 133A (2026): What Officers Can and Cannot Do, Statements, Impounding of Books, Survey vs Search and What Happens Next",
    em="stay calm, stay accurate.",
    kicker="/ Business owners, professionals and companies &middot; Income tax survey at business premises &middot; Updated 2026-11-28",
    lead=("<strong>A survey under section 133A lets income tax officers visit your business premises to inspect books, verify cash and stock, and record statements. "
          "Unlike a search, a survey cannot seize cash, jewellery or stock - but books can be impounded, and what you say and sign during the survey shapes the assessment that follows.</strong>"),
    sections=[
        ("/ What officers can and cannot do", "Survey under section 133A.",
         table(["Point", "Survey (section 133A)", "Search (section 132)"], [
             ["Where", "Place where business or profession is carried on, or where books, cash or stock are kept", "Any place, including residence, under a warrant of authorisation"],
             ["When", "Business premises during business hours; other places between sunrise and sunset", "Any time under the warrant"],
             ["Books and documents", "Inspect, mark, copy; impound with reasons recorded", "Seize"],
             ["Cash, jewellery, stock", "Verify and inventory only - no seizure", "Can be seized"],
             ["Statements", "Recorded, not on oath", "Recorded on oath"],
             ["Retaining impounded books", "Beyond fifteen days (excluding holidays) only with higher approval", "As the law on seized material allows"]])
         + ul("<strong>Cooperate, but read before you sign:</strong> answers recorded in the statement are used later; give facts you can support, and ask for a copy of the statement and of any inventory.",
              "<strong>Say when you do not know:</strong> it is better to state that records will be produced than to guess figures for income, stock or cash.")),
        ("/ After the survey", "Where most of the tax is decided.",
         ul("<strong>Statements are not the last word:</strong> courts have held that a statement recorded in a survey is not conclusive evidence by itself; a statement made under pressure or in error can be retracted promptly, with reasons and evidence.",
            "<strong>Admitted undisclosed income:</strong> income offered during or after a survey that falls under the unexplained income sections can be taxed at the special rate under section 115BBE - decide on any disclosure with advice, not on the spot.",
            "<strong>What usually follows:</strong> a scrutiny or reassessment notice for the years covered, with the impounded books and survey findings as the starting point.",
            "<strong>Reconcile quickly:</strong> stock and cash differences found in the survey can often be explained from books, purchase and sale records, and returns - prepare that reconciliation early.",
            "<strong>Get impounded books back:</strong> ask for return of books once the purpose is served, and keep copies of what you need for compliance.")
         + call_box("an income tax survey", ["Guidance during and right after the survey",
                                              "Review and retraction of statements",
                                              "Stock and cash difference reconciliation",
                                              "Decisions on any disclosure",
                                              "Scrutiny and reassessment that follow"],
                    "Survey date, premises, inventory, statements recorded, returns and books.")
         + sources("Income-tax Act, 1961 (sections 132, 133A and 115BBE) and the corresponding provisions of the Income-tax Act, 2025; Supreme Court and High Court decisions on the evidentiary value of survey statements; site notice reply, scrutiny and reassessment pages.")),
    ],
    faqs=[("What is an income tax survey under section 133A?", "A visit by income tax officers to a place where business or profession is carried on, or where books, cash or stock are kept, to inspect books, verify cash and stock, mark and copy documents and record statements. It is narrower than a search: cash, jewellery and stock cannot be seized."),
          ("What is the difference between an income tax survey and a search?", "A survey is limited to business premises (and places where books, cash or stock are kept) during set hours, with no seizure and statements not on oath. A search under section 132 needs a warrant, can cover a residence, and allows seizure of books, cash, jewellery and other assets."),
          ("Can officers take my books during a survey?", "They can impound books and documents after recording reasons. Keeping them beyond fifteen days, excluding holidays, needs approval from a higher authority. Ask for an inventory of what is taken."),
          ("Is a statement given during a survey binding?", "It is recorded without oath, and courts have held that it is not conclusive evidence by itself. A statement made under pressure or by mistake should be retracted promptly with reasons and supporting records."),
          ("What happens after an income tax survey?", "Usually a scrutiny or reassessment notice for the years covered, using the survey findings and impounded books. Reconcile stock and cash differences, review any statements, and get advice before offering additional income."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the survey date and premises, the inventory of books impounded, copies of statements recorded, and your recent returns and books. Or book a call directly.")],
    related=[("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-143-2-scrutiny-notice-response-india.html", "Scrutiny notice under section 143(2)"),
             ("section-148-148a-reassessment-notice-response-india.html", "Reassessment notice under section 148"),
             ("income-tax-outstanding-demand-what-to-do-section-245-refund-adjustment-disagree-rectification-2026.html", "Income tax outstanding demand")],
    cta_h="Income tax survey at your premises?", cta_b=C,
    keywords="income tax survey, income tax survey section 133a, it survey business premises, difference between survey and search income tax, statement recorded in survey, impounding of books 133a, what to do in income tax survey",
    desc="Income tax survey under section 133A: where and when officers can visit, inspecting books and verifying cash and stock, impounding books (beyond fifteen days only with approval), no seizure unlike a search, statements not on oath, 115BBE on admitted income, and what follows.",
    howto={"name": "How to handle an income tax survey", "description": "During and after.", "steps": [
        {"name": "Cooperate and stay accurate", "text": "Give facts you can support; say records will be produced where unsure."},
        {"name": "Get copies", "text": "Ask for copies of statements and the inventory of books impounded."},
        {"name": "Review and reconcile", "text": "Check statements; reconcile stock and cash differences from books."},
        {"name": "Prepare for assessment", "text": "Retract wrong statements promptly; plan replies to notices that follow."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KY complete")
