# -*- coding: utf-8 -*-
"""Batch LM (28 Nov 2026): Loans between a company and its directors - section 185 restrictions on loans to directors, the
private company exemption, section 185(2) loans to interested entities, director loans to the company (not a deposit with a
declaration), deemed dividend under section 2(22)(e), and cash limits.
Demand: 'loan to director from company', 'section 185 companies act', 'can director take loan from private limited company',
'loan from director to company', 'deemed dividend 2(22)(e)' - section 185 mentioned on 3 pages, no dedicated page. Small company
owners regularly need help. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 section 185 as substituted in 2017; MCA exemption notification of 5 June 2015 as amended in 2017;
Companies (Acceptance of Deposits) Rules, 2014 rule 2(1)(c)(viii); Income-tax Act section 2(22)(e), sections 269SS and 269T):
a company cannot give a loan, guarantee or security to its directors, directors of its holding company, their partners or
relatives, or a firm in which such a director or relative is a partner; under section 185(2) it may lend to other persons in whom
a director is interested after a special resolution, if the loan is used for the borrower's principal business; exceptions include
loans to a managing or whole-time director under conditions of service applicable to all employees or a scheme approved by special
resolution, lending companies in the ordinary course at not less than the bank rate, and holding-company loans, guarantees or
security for wholly owned subsidiaries used for their principal business; section 185 does not apply to a private company in which
no other body corporate has invested, whose borrowings from banks, financial institutions or bodies corporate are below twice its
paid-up capital or INR 50 crore (whichever is lower), and which has no subsisting repayment default; money from a director is not a
deposit if the director declares it is not out of borrowed funds (for private companies, also a director's relative), and it is
reported as such; a loan by a closely held company to a shareholder with at least 10% voting power (or a concern in which such a
shareholder has a substantial interest) is a deemed dividend to the extent of accumulated profits, taxable in the recipient's hands;
loans of INR 20,000 or more cannot be taken or repaid in cash. No penalty amounts, no fees. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "loan-to-director-from-company-section-185-private-company-exemption-director-loan-deemed-dividend-2-22-e-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the company&rsquo;s shareholding (any body corporate "
     "investor?), its bank and other borrowings, the loans to or from directors and relatives with dates and amounts, any board or "
     "special resolutions, and the latest balance sheet. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Loan to Director From a Company (2026): Section 185 Restrictions, the Private Company Exemption, Director Loans to the Company and Deemed Dividend Under 2(22)(e)",
    em="the company is not the founder&rsquo;s wallet.",
    kicker="/ Private limited company founders and directors &middot; Companies Act section 185 and Income-tax section 2(22)(e) &middot; Updated 2026-11-28",
    lead=("<strong>A company generally cannot lend to its directors or their relatives under section 185 of the Companies Act - but many private companies qualify for an exemption, and loans to entities in which a director is interested are allowed with a special resolution. "
          "Even where company law allows it, a loan from a closely held company to a 10% shareholder can be taxed as a deemed dividend. "
          "Money a director lends to the company is fine, if the paperwork shows it is not from borrowed funds.</strong>"),
    sections=[
        ("/ Company to director: section 185", "What is barred, what is allowed.",
         table(["Situation", "Position"], [
             ["Loan, guarantee or security to a director, a director of the holding company, their partners or relatives, or their firms", "Prohibited, unless an exception or exemption applies"],
             ["Loan to a company or body in which a director is interested", "Allowed with a special resolution, if used for the borrower&rsquo;s principal business (section 185(2))"],
             ["Loan to a managing or whole-time director", "Allowed under conditions of service for all employees, or a scheme approved by special resolution"],
             ["Holding company to its wholly owned subsidiary", "Allowed if used for the subsidiary&rsquo;s principal business"],
             ["Lending company in ordinary course", "Allowed at not less than the bank rate"],
             ["Private company exemption", "No body corporate shareholder; borrowings from banks, FIs and bodies corporate below twice paid-up capital or INR 50 crore (lower); no repayment default"]])
         + ul("<strong>Check the exemption every time:</strong> a new corporate investor, more borrowing or a default can take away the private company exemption.",
              "<strong>Consequences:</strong> breaching section 185 exposes the company, the officers in default and the director who received the loan to penalties.")),
        ("/ Director to company, and the tax side", "Deposits, deemed dividend and cash.",
         ul("<strong>Director lending to the company:</strong> not a deposit if the director gives a written declaration that the money is not from borrowed funds (for private companies, a director&rsquo;s relative too); disclose it and report it in the annual return of money not treated as deposits.",
            "<strong>Deemed dividend:</strong> a loan or advance from a closely held company to a shareholder with at least 10% voting power, or to a concern in which that shareholder has a substantial interest, is taxed as dividend in the recipient&rsquo;s hands to the extent of accumulated profits.",
            "<strong>Repaying does not undo it:</strong> deemed dividend is triggered when the loan is given, even if repaid later.",
            "<strong>No cash:</strong> loans of INR 20,000 or more cannot be accepted or repaid in cash.",
            "<strong>Founder salary instead?</strong> Salary, dividend or a properly approved loan each have different tax results - plan before money moves.")
         + call_box("director loans", ["Section 185 and exemption check",
                                       "Special resolutions under section 185(2)",
                                       "Director loan declarations and annual return",
                                       "Deemed dividend exposure",
                                       "Cleaning up past loans"],
                    "Shareholding, borrowings, director loans, resolutions, balance sheet.")
         + sources("Companies Act, 2013 (section 185 as substituted in 2017); MCA notification of 5 June 2015 on private company exemptions, as amended; Companies (Acceptance of Deposits) Rules, 2014 (rule 2(1)(c)(viii)); Income-tax Act, 1961 (sections 2(22)(e), 269SS and 269T) and the corresponding provisions of the Income-tax Act, 2025; site founder salary vs dividend and ROC compliance pages.")),
    ],
    faqs=[("Can a director take a loan from a private limited company?", "Generally not under section 185, unless the company qualifies for the private company exemption - no body corporate shareholder, borrowings from banks, financial institutions and bodies corporate below twice paid-up capital or INR 50 crore (whichever is lower), and no repayment default - or another exception applies."),
          ("Can a company give a loan to another company in which a director is interested?", "Yes, under section 185(2), after a special resolution of the lending company, provided the loan is used by the borrower for its principal business activities."),
          ("Can a director lend money to the company?", "Yes. The money is not treated as a deposit if the director gives a written declaration that it is not out of borrowed funds. In a private company, a director's relative can also lend on the same basis."),
          ("What is deemed dividend under section 2(22)(e)?", "A loan or advance by a closely held company to a shareholder with at least 10% voting power, or to a concern in which that shareholder has a substantial interest, is taxed as dividend in the recipient's hands to the extent of the company's accumulated profits, even if it is later repaid."),
          ("What happens if section 185 is breached?", "The company, its officers in default and the director who received the loan face penalties. The loan should be reviewed and regularised with advice."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the shareholding, borrowings, director loans with dates and amounts, resolutions and the latest balance sheet. Or book a call directly.")],
    related=[("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "Founder salary vs dividend"),
             ("related-party-transactions-section-188-companies-act-approval-arms-length-aoc-2-wholly-owned-subsidiary-2026.html", "Related party transactions (section 188)"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar"),
             ("company-secretarial-services-india-remote.html", "Company secretarial services")],
    cta_h="Money moving between you and your company?", cta_b=C,
    keywords="loan to director from company, section 185 companies act, can director take loan from private limited company, loan from director to company, deemed dividend 2(22)(e), private company exemption section 185, director loan declaration",
    desc="Loan to director from a company: section 185 prohibition, exceptions, private company exemption (no body corporate shareholder, borrowings below 2x paid-up capital or INR 50 crore, no default), section 185(2) special resolution, director loans to the company, deemed dividend under 2(22)(e), cash limits.",
    howto={"name": "How to handle loans between a company and its directors", "description": "Check, approve, document.", "steps": [
        {"name": "Check section 185", "text": "Is the borrower a director, relative or linked firm? Does an exemption apply?"},
        {"name": "Approve where allowed", "text": "Special resolution for interested entities under section 185(2)."},
        {"name": "Document director loans", "text": "Declaration that funds are not borrowed; annual reporting."},
        {"name": "Test the tax", "text": "Deemed dividend for 10% shareholders; no cash of INR 20,000 or more."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LM complete")
