# -*- coding: utf-8 -*-
"""Batch LV (28 Nov 2026): Converting a loan into equity shares - section 62(3) conversion option approved by special resolution
before the loan, converting an existing loan without such an option through a fresh issue (preferential / private placement),
valuation, PAS-3, and FEMA for loans from foreign parents, NRI directors or ECB lenders.
Demand: 'convert loan into equity', 'conversion of loan into shares section 62(3)', 'convert director loan to equity', 'ecb
conversion into equity', 'loan to share capital private company' - mentioned on two pages, no dedicated page. Founders, parent
companies and foreign lenders often convert. User steer 26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts (Companies Act, 2013 sections 42, 62(1)(c) and 62(3); Companies (Share Capital and Debentures) Rules, 2014; Companies
(Prospectus and Allotment of Securities) Rules, 2014): section 62(3) allows conversion of a loan or debentures into shares where the
terms of the loan include an option to convert and that option was approved by a special resolution before the loan was raised;
where there was no such option, the company issues shares afresh (preferential allotment under section 62(1)(c) read with section
42) against the outstanding loan, with a special resolution, a registered valuer's price and the usual private placement steps;
the allotment is reported in PAS-3; authorised capital must cover the shares. FEMA: conversion of an ECB or other amounts owed to a
non-resident into equity is permitted subject to sector rules and pricing guidelines, with FC-GPR reporting; an existing loan from an
NRI director or foreign parent must have been taken in line with FEMA in the first place (site ECB page). Tax: angel tax on premium
abolished from AY 2025-26 (site page). No fees, no thresholds invented. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "convert-loan-into-equity-shares-section-62-3-director-loan-foreign-parent-ecb-conversion-pas-3-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the loan agreement (does it have a conversion option?), "
     "the lender (director, parent, NRI, foreign company, bank), the outstanding amount and interest, the proposed price and "
     "valuation, and the current shareholding. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Convert a Loan Into Equity Shares (2026): Section 62(3) Conversion Option, Converting Director or Parent Loans Without It, Valuation, PAS-3 and FEMA for Foreign Lenders",
    em="the loan agreement decides the route.",
    kicker="/ Private companies, founders, foreign parents and NRI directors &middot; Companies Act section 62(3) &middot; Updated 2026-11-28",
    lead=("<strong>A company can turn a loan into shares in two ways. If the loan was taken with a conversion option approved by special resolution before the loan, section 62(3) allows conversion on those terms. "
          "If not, the company issues new shares against the loan through a preferential allotment, with a special resolution, a registered valuer&rsquo;s price and private placement steps. "
          "Loans from foreign parents, NRI directors or ECB lenders also need FEMA pricing and FC-GPR reporting.</strong>"),
    sections=[
        ("/ The two routes", "With or without a conversion option.",
         table(["Point", "Conversion option (s.62(3))", "No option - fresh issue (s.62(1)(c) + s.42)"], [
             ["When", "Loan terms included an option to convert", "Ordinary loan with no conversion term"],
             ["Approval", "Special resolution before the loan was raised", "Special resolution now, approving the allotment"],
             ["Price", "As set in the loan terms", "Registered valuer&rsquo;s report"],
             ["Process", "Exercise the option per the terms", "Offer letter, allotment against the outstanding loan"],
             ["Filing", "PAS-3 within the time allowed", "PAS-3 within 15 days of allotment (private placement)"],
             ["Authorised capital", "Must cover the new shares", "Must cover the new shares"]])
         + ul("<strong>Plan it at the start:</strong> building a conversion option into a founder or parent loan, approved by special resolution, makes later conversion much simpler.",
              "<strong>Interest:</strong> decide whether accrued interest is converted too, and deduct TDS on interest as applicable before conversion.")),
        ("/ Foreign lenders and tax", "Where conversions stall.",
         ul("<strong>Foreign parent or NRI director loans:</strong> the loan itself must have been taken in line with FEMA (for example under the ECB framework); converting an irregular loan does not cure it.",
            "<strong>ECB conversion:</strong> converting an ECB into equity is allowed subject to sector rules, pricing guidelines and lender consent, with FC-GPR and ECB reporting updated.",
            "<strong>Pricing:</strong> for non-residents, the issue price must meet FEMA pricing guidelines.",
            "<strong>Angel tax:</strong> the section 56(2)(viib) charge on premium was abolished from assessment year 2025-26; valuation still matters for company law and FEMA.",
            "<strong>Books:</strong> the loan account is closed and share capital and premium credited; update the register of members and issue certificates or credit demat.")
         + call_box("a loan-to-equity conversion", ["Checking the loan terms and route",
                                                    "Special resolutions and valuation",
                                                    "Allotment and PAS-3",
                                                    "FEMA pricing, ECB and FC-GPR for foreign lenders",
                                                    "Authorised capital and records"],
                    "Loan agreement, lender, outstanding amount, price, shareholding.")
         + sources("Companies Act, 2013 (sections 42, 61, 62(1)(c) and 62(3)); Companies (Share Capital and Debentures) Rules, 2014; Companies (Prospectus and Allotment of Securities) Rules, 2014; FEMA (Non-debt Instruments) Rules, 2019 and the RBI ECB framework; site ECB, private placement, FC-GPR and director loan pages.")),
    ],
    faqs=[("Can a private company convert a loan into equity shares?", "Yes. If the loan terms had a conversion option approved by special resolution before the loan, conversion follows section 62(3). Otherwise, the company issues new shares against the loan through a preferential allotment with a special resolution and a registered valuer's price."),
          ("What does section 62(3) of the Companies Act allow?", "It allows a company to convert loans or debentures into shares where the terms of the loan or debentures include an option to convert, approved by a special resolution passed before the loan was raised."),
          ("How do I convert a director's loan into shares?", "If the loan had no conversion option, treat it as a fresh issue: special resolution, registered valuer's report, offer letter, allotment against the outstanding loan and PAS-3. Check authorised capital first."),
          ("Can a foreign parent's loan or ECB be converted into equity?", "Yes, subject to the sector allowing foreign investment, FEMA pricing guidelines and lender consent, with FC-GPR filed and ECB reporting updated. The loan must have been taken in line with FEMA in the first place."),
          ("Is there tax on converting a loan into shares at a premium?", "The angel tax provision on share premium was abolished from assessment year 2025-26. Interest accrued up to conversion is still taxable for the lender, with TDS where applicable."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the loan agreement, lender details, outstanding amount and interest, proposed price and current shareholding. Or book a call directly.")],
    related=[("loan-from-nri-director-shareholder-to-indian-company-ecb-2026-rules.html", "Loan from NRI director or shareholder (ECB)"),
             ("private-placement-shares-section-42-pas-4-pas-3-60-days-allotment-200-persons-startup-fundraise-2026.html", "Private placement under section 42"),
             ("loan-to-director-from-company-section-185-private-company-exemption-director-loan-deemed-dividend-2-22-e-2026.html", "Loan to director (section 185)"),
             ("form-fc-gpr-filing-checklist-india-2026.html", "Form FC-GPR filing checklist")],
    cta_h="Turning a loan into shares?", cta_b=C,
    keywords="convert loan into equity, conversion of loan into shares section 62(3), convert director loan to equity, ecb conversion into equity, loan to share capital private company, special resolution conversion option",
    desc="Convert a loan into equity: section 62(3) where a conversion option was approved by special resolution before the loan; otherwise a fresh preferential issue with special resolution, registered valuer price and PAS-3; FEMA pricing, ECB conversion and FC-GPR for foreign lenders.",
    howto={"name": "How to convert a loan into equity", "description": "Pick the route, then allot.", "steps": [
        {"name": "Read the loan terms", "text": "Conversion option approved by special resolution before the loan?"},
        {"name": "Approve and value", "text": "Special resolution; registered valuer price for a fresh issue."},
        {"name": "Allot and file", "text": "Allot against the outstanding loan; PAS-3; check authorised capital."},
        {"name": "Foreign lenders", "text": "FEMA pricing, ECB reporting and FC-GPR."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LV complete")
