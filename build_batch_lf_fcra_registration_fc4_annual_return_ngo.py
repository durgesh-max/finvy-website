# -*- coding: utf-8 -*-
"""Batch LF (28 Nov 2026): FCRA for NGOs - registration or prior permission, the SBI New Delhi FCRA account, the 20% cap on
administrative expenses, no transfer to other persons, FC-4 annual return by 31 December, renewal and consequences.
Demand: 'fcra registration', 'fc-4 annual return due date', 'fcra account sbi new delhi', 'fcra compliance ngo', 'fcra renewal' -
no page on the site (FCRA only mentioned on the section 8 and trust pages). Timely: FC-4 for FY 2025-26 is due 31 December 2026.
NGOs need a chartered accountant for FC-4 certification. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Foreign Contribution (Regulation) Act, 2010 as amended in 2020, and FCRA Rules, 2011): an association with a definite
cultural, economic, educational, religious or social programme needs FCRA registration (or prior permission for a specific
contribution) before accepting foreign contribution; foreign contribution must be received only in the FCRA account at the SBI
New Delhi Main Branch (Sansad Marg) and can be moved to utilisation accounts; administrative expenses out of foreign contribution
cannot exceed 20% of the foreign contribution received in the year (reduced from 50% in 2020); foreign contribution cannot be
transferred to any other person (2020 amendment); identification (Aadhaar) of office bearers is required; FC-4 annual return within
nine months of the year end, i.e. by 31 December, with income and expenditure account, receipts and payments account and balance
sheet certified by a chartered accountant; registration is valid for five years and must be renewed (Form FC-3C) before expiry;
non-compliance can lead to suspension or cancellation. Facts checked by web search 28 Nov 2026 (KPMG, Nishith Desai, practitioner
sources). Renewal lead time and registration eligibility thresholds are not stated (not verified). No fees, no portal menu paths.
advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "fcra-registration-ngo-fc-4-annual-return-31-december-sbi-new-delhi-account-20-percent-admin-renewal-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your organisation type (trust, society or section 8 "
     "company), FCRA registration number and validity (if any), foreign contributions received and spent in the year, and your "
     "FCRA and utilisation account statements. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="FCRA for NGOs (2026): Registration or Prior Permission, SBI New Delhi FCRA Account, 20% Admin Expense Cap, FC-4 Annual Return by 31 December and Renewal",
    em="foreign money, Indian rules - no exceptions.",
    kicker="/ Trusts, societies and section 8 companies &middot; Foreign Contribution (Regulation) Act &middot; Updated 2026-11-28",
    lead=("<strong>An NGO in India can accept foreign contribution only after FCRA registration or prior permission, and only into its FCRA account at the SBI New Delhi Main Branch. "
          "Administrative expenses from foreign funds are capped at 20%, foreign funds cannot be passed on to other organisations, and the FC-4 annual return - certified by a chartered accountant - is due by 31 December every year.</strong>"),
    sections=[
        ("/ The core rules", "FCRA 2010 as amended in 2020.",
         table(["Rule", "What it means"], [
             ["Registration or prior permission", "Needed before accepting any foreign contribution; prior permission is for a specific contribution from a specific donor"],
             ["FCRA account", "Foreign contribution must first be received only in the designated account at SBI New Delhi Main Branch"],
             ["Utilisation accounts", "Funds can be moved from the FCRA account to separate utilisation accounts for spending"],
             ["Administrative expenses", "Not more than 20% of the foreign contribution received in the year"],
             ["No onward transfer", "Foreign contribution cannot be transferred to any other person or organisation"],
             ["Office bearers", "Identification (Aadhaar, or passport / OCI for foreigners) required"],
             ["Annual return", "Form FC-4 within nine months of the year end - by 31 December - with CA-certified accounts"],
             ["Validity", "Registration valid for five years; renew in Form FC-3C before expiry"]])
         + ul("<strong>Mixing funds:</strong> foreign contribution must not be mixed with local funds; keep separate books and bank accounts.",
              "<strong>Changes:</strong> changes in key office bearers, address or bank details must be reported as the rules require.")),
        ("/ FC-4 and staying compliant", "Due 31 December 2026 for FY 2025-26.",
         ul("<strong>What goes into FC-4:</strong> foreign contribution received (donor-wise), utilisation by purpose, administrative expense percentage, assets created, and income and expenditure account, receipts and payments account and balance sheet for the foreign contribution, certified by a chartered accountant.",
            "<strong>Reconcile first:</strong> FCRA account and utilisation account statements, donor receipts, and the 20% administrative cap.",
            "<strong>Nil return:</strong> file FC-4 even if no foreign contribution was received in the year.",
            "<strong>Renewal:</strong> track the five-year validity and apply in good time; an expired registration means foreign funds cannot be received or used.",
            "<strong>Consequences:</strong> non-compliance can lead to suspension or cancellation of registration and freezing of foreign funds.")
         + call_box("FCRA compliance", ["FCRA registration or prior permission",
                                        "FC-4 annual return with CA certification",
                                        "20% administrative expense review",
                                        "Renewal in FC-3C",
                                        "Bank account and books set-up for foreign funds"],
                    "Organisation type, FCRA number and validity, foreign funds received and spent, account statements.")
         + sources("Foreign Contribution (Regulation) Act, 2010, as amended by the FCR (Amendment) Act, 2020; Foreign Contribution (Regulation) Rules, 2011, as amended; Ministry of Home Affairs FCRA notices; site section 8 company and trust registration (12AB / 80G) pages.")),
    ],
    faqs=[("Who needs FCRA registration?", "Any association, trust, society or section 8 company with a definite cultural, economic, educational, religious or social programme that wants to accept foreign contribution. Without registration or prior permission, foreign contribution cannot be accepted."),
          ("Where must foreign contribution be received?", "Only in the designated FCRA account at the SBI New Delhi Main Branch. From there it can be moved to utilisation accounts for spending, but it cannot be mixed with local funds."),
          ("What is the due date for the FC-4 annual return?", "Within nine months of the end of the financial year, that is by 31 December. For FY 2025-26 the due date is 31 December 2026. A nil return is needed even if no foreign contribution was received."),
          ("How much of foreign contribution can be spent on administration?", "Not more than 20% of the foreign contribution received in the financial year, after the 2020 amendment reduced the limit from 50%."),
          ("Can an NGO pass foreign contribution to another NGO?", "No. After the 2020 amendment, foreign contribution cannot be transferred to any other person or organisation, even one that is FCRA registered."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your organisation type, FCRA number and validity, foreign funds received and spent in the year, and your FCRA and utilisation account statements. Or book a call directly.")],
    related=[("section-8-company-registration-india-non-profit-licence-12a-80g-csr-1-compliance-2026.html", "Section 8 company registration"),
             ("trust-registration-12ab-section-332-80g-ngo-provisional-regular-renewal-form-104-105-2026.html", "Trust registration, 12AB and 80G"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar"),
             ("income-tax-notice-section-133-6-information-request-summons-section-131-how-to-reply-2026.html", "Income tax notice under section 133(6)")],
    cta_h="FC-4 due by 31 December, or need FCRA registration?", cta_b=C,
    keywords="fcra registration, fc-4 annual return due date, fcra account sbi new delhi, fcra compliance ngo, fcra renewal fc-3c, fcra administrative expenses 20 percent, fcra prior permission",
    desc="FCRA for NGOs: registration or prior permission before foreign contribution, FCRA account at SBI New Delhi Main Branch, utilisation accounts, 20% administrative expense cap, no transfer to other organisations, FC-4 by 31 December with CA-certified accounts, five-year validity and renewal.",
    howto={"name": "How to stay FCRA compliant", "description": "From receipt to FC-4.", "steps": [
        {"name": "Receive correctly", "text": "Only into the FCRA account at SBI New Delhi Main Branch."},
        {"name": "Spend within limits", "text": "Through utilisation accounts; administrative expenses within 20%; no onward transfer."},
        {"name": "File FC-4", "text": "By 31 December with CA-certified accounts; nil return if nothing received."},
        {"name": "Renew on time", "text": "Track five-year validity and file FC-3C before expiry."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LF complete")
