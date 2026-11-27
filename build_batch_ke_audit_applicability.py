# -*- coding: utf-8 -*-
"""Batch KE (27 Nov 2026): Audit applicability in India by entity - company, LLP, partnership firm, proprietorship and
trust; statutory audit vs tax audit vs trust audit, limits, deadlines and what happens if an audit is missed.
Demand: sweep ac158 (27 Nov 2026), all 7 markets: "audit applicability", "... for llp", "... for company", "... for trust",
"... under llp act", "... for proprietorship"; the site had a tax audit limit page but nothing that answered audit
applicability by type of entity.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - an audit can only be done by a CA, so every reader of this
page who needs one has to hire one.
Facts (verified 27 Nov 2026 - web search and the site's own tax audit page): every company needs a statutory audit under the
Companies Act whatever its size; LLP audit under rule 24(8) of the LLP Rules where turnover exceeds Rs 40 lakh or
contribution exceeds Rs 25 lakh (exempt below both); partnership firms and proprietorships have no statutory audit, only a
tax audit under section 44AB (business turnover above Rs 1 crore, Rs 10 crore where cash receipts and payments are each
within 5%; professionals above Rs 50 lakh, as on the site's tax audit page) and the presumptive-scheme triggers; trusts
registered for exemption get accounts audited when income before exemption exceeds the maximum amount not chargeable to tax,
with the report in the prescribed form (Form 10B / 10BB under the 1961 rules) before the return; corresponding provisions of
the Income-tax Act, 2025 apply from 1 April 2026 (section numbers of the 1961 Act used as most readers search them).
No fees, no office claims, no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "audit-applicability-india-company-llp-partnership-proprietorship-trust-statutory-tax-audit-limits-2026"

C = contact("the type of entity, last year's turnover or gross receipts and partner contribution, how much of the year's receipts and payments were in cash, whether you use the presumptive scheme, the last audited accounts or return filed, and any notice received")
PAGES = [dict(
    slug=SLUG,
    title="Audit Applicability in India (2026): Company, LLP, Partnership Firm, Proprietorship and Trust - Statutory Audit vs Tax Audit Limits",
    em="which audit, and from what turnover.",
    kicker="/ Founders, partners, proprietors and trustees &middot; Statutory, tax and trust audits &middot; Updated 2026-11-27",
    lead=("<strong>A company always needs a statutory audit, whatever its size. An LLP needs one only when its turnover exceeds Rs 40 lakh or partners' contribution exceeds Rs 25 lakh. Partnership firms and proprietors have no statutory audit, but any business crossing the income tax limits - Rs 1 crore turnover, or Rs 10 crore when cash dealings are within 5%, and Rs 50 lakh for professionals - needs a tax audit.</strong> "
          "Trusts claiming exemption need their accounts audited once their income before exemption crosses the basic exemption limit. Only a chartered accountant can sign any of these audits."),
    sections=[
        ("/ Audit applicability by entity", "One table, five entity types.",
         table(["Entity", "Statutory audit", "Tax audit (section 44AB)"], [
             ["Private or public company", "Always, under the Companies Act - even with no turnover", "Also needed if turnover crosses the 44AB limit"],
             ["LLP", "When turnover exceeds Rs 40 lakh or contribution exceeds Rs 25 lakh (rule 24(8) of the LLP Rules)", "When turnover crosses the 44AB limit; LLPs cannot use the 44AD presumptive scheme"],
             ["Partnership firm", "None under the Partnership Act", "When turnover or receipts cross the 44AB limits, or presumptive income is declared below the scheme rate"],
             ["Proprietorship", "None", "Same as a firm - on the proprietor's business turnover or professional receipts"],
             ["Trust or institution claiming exemption", "Accounts audited when income before exemption exceeds the basic exemption limit (Form 10B / 10BB under the 1961 rules)", "Covered by the trust audit report instead"]])
         + ul("<strong>Tax audit limits:</strong> business turnover above Rs 1 crore, or above Rs 10 crore where cash receipts and cash payments are each within 5% of the total; professional gross receipts above Rs 50 lakh.",
              "<strong>Presumptive scheme:</strong> businesses under section 44AD and professionals under section 44ADA who declare at least the scheme rate do not need a tax audit; declaring less, with income above the basic exemption limit, brings it in.",
              "<strong>GST:</strong> there is no separate GST audit by a CA now - the annual return GSTR-9 and the self-certified reconciliation GSTR-9C are filed by the taxpayer.")),
        ("/ Deadlines and what goes wrong", "Dates and the cost of missing them.",
         ul("<strong>Company:</strong> the auditor is appointed within 30 days of incorporation for the first auditor and at the AGM after that (Form ADT-1); audited accounts are filed in AOC-4 within 30 days of the AGM.",
            "<strong>LLP:</strong> audited accounts go into Form 8 by 30 October; the annual return Form 11 is due by 30 May.",
            "<strong>Tax audit:</strong> the audit report is due one month before the return due date for audit cases - check the year's dates, which are sometimes extended by CBDT circular.",
            "<strong>Missing a tax audit</strong> can draw a penalty under section 271B (0.5% of turnover, capped), and a late company or LLP filing runs up additional fees for each day of delay.",
            "<strong>Trust audit missed</strong> can cost the exemption for that year, so the report must be filed before the return.")
         + call_box("Audits and audit applicability", ["Statutory audit of companies and LLPs",
                                                      "Tax audit under section 44AB (Form 3CA / 3CB / 3CD)",
                                                      "Trust and NGO audits",
                                                      "Applicability check from your turnover and cash mix",
                                                      "Catch-up for missed audits and filings"],
                    "Entity type, turnover, cash mix and last filed return.")
         + sources("Companies Act, 2013 (sections 139 and 143); Limited Liability Partnership Rules, 2009 (rule 24(8)); Income-tax Act, 1961 (sections 12A, 44AB, 44AD, 44ADA, 271B) and the corresponding provisions of the Income-tax Act, 2025; site tax audit, ADT-1, LLP Form 8 / 11 and annual filing guides. Checked 27 November 2026.")),
    ],
    faqs=[("Is audit compulsory for every company in India?", "Yes. Every company - private or public, with or without turnover - must have its accounts audited by a chartered accountant under the Companies Act every year. A tax audit is needed in addition when turnover crosses the income tax limits."),
          ("What is the audit applicability for an LLP?", "An LLP needs a statutory audit when its turnover in the year exceeds Rs 40 lakh or its partners' contribution exceeds Rs 25 lakh, under rule 24(8) of the LLP Rules. Below both, the accounts can be signed by the designated partners without audit. A separate tax audit applies if turnover crosses the section 44AB limit; LLPs cannot use the 44AD presumptive scheme."),
          ("Is audit required for a proprietorship or partnership firm?", "There is no statutory audit for a proprietorship or a partnership firm. A tax audit under section 44AB is needed when business turnover exceeds Rs 1 crore (Rs 10 crore where cash receipts and payments are each within 5%) or professional receipts exceed Rs 50 lakh, or where presumptive income is declared below the scheme rate and total income is above the basic exemption limit."),
          ("When does a trust need an audit?", "A trust or institution registered for exemption must get its accounts audited when its income, before claiming the exemption, exceeds the basic exemption limit, and file the audit report in the prescribed form (Form 10B or 10BB under the 1961 rules) before the return. Missing it can cost the exemption for the year."),
          ("What is the penalty for not getting a tax audit done?", "Section 271B allows a penalty of 0.5% of turnover or gross receipts, subject to a cap, unless there was reasonable cause. Getting the audit done and filed as soon as possible limits the damage."),
          ("Can a tax audit and a statutory audit be done by the same CA?", "Yes, usually. A company's statutory auditor can also do its tax audit, subject to the professional rules on how many tax audits one CA may sign in a year."),
          ("What should I send to check if my business needs an audit?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the type of entity, last year's turnover or receipts and partner contribution, how much of the receipts and payments were in cash, whether you use the presumptive scheme, and the last return filed. We tell you which audits apply and the due dates.")],
    related=[("form-3ca-3cb-3cd-tax-audit-india-2026-checklist.html", "Tax audit limits and Form 3CD"),
             ("form-adt-1-auditor-appointment-15-days-first-auditor-rotation-adt-3-india-2026.html", "Form ADT-1 auditor appointment"),
             ("llp-form-8-due-30-october-2026-no-extension-late-fee.html", "LLP Form 8 due 30 October"),
             ("company-annual-filing-india-2026-aoc-4-mgt-7-due-date-fee-waiver-circular-05-2026-ccfs-status-check.html", "Company annual filing (AOC-4 / MGT-7)"),
             ("best-ca-section-44ad-44ada-presumptive-scheme-india.html", "Presumptive scheme (44AD / 44ADA)")],
    cta_h="Not sure which audit applies?", cta_b=C,
    keywords="audit applicability, audit applicability for llp, audit applicability for company, audit applicability for trust, audit applicability for proprietorship, llp audit limit 40 lakh, tax audit limit 44ab, statutory audit vs tax audit, partnership firm audit",
    desc="Audit applicability in India by entity: companies always need a statutory audit; LLPs above Rs 40 lakh turnover or Rs 25 lakh contribution; firms and proprietors only a tax audit above the 44AB limits; trusts above the basic exemption limit. Deadlines and penalties.",
    howto={"name": "How to check which audit your business needs", "description": "Four questions.", "steps": [
        {"name": "Identify the entity", "text": "Company, LLP, partnership firm, proprietorship or trust."},
        {"name": "Check the statutory audit rule", "text": "Always for companies; LLPs above Rs 40 lakh turnover or Rs 25 lakh contribution."},
        {"name": "Check the tax audit limits", "text": "Turnover, cash mix and presumptive scheme decide section 44AB."},
        {"name": "Diary the deadlines", "text": "Audit reports before the return; company and LLP filings by their due dates."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KE complete")
