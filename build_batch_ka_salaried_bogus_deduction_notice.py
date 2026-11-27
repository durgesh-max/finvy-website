# -*- coding: utf-8 -*-
"""Batch KA (27 Nov 2026): Income tax notices and nudges to salaried employees over bogus or unsupported deductions -
HRA, 80C / 80D, 80G and 80GGC political donations - the CBDT NUDGE campaign, and how to correct or reply.
Demand: sweep ac147 (27 Nov 2026), all 7 markets: "fake deduction notice", "income tax notice salaried employees",
"income tax notices for salaried employees (sample pdf / hindi / last date)", "income tax notification for salaried
employees", plus seeds 'bogus deduction notice', 'hra fake rent notice', 'income tax notice for donation 80g'; no page
covered deduction-misuse notices to salaried people.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - correcting or defending deduction claims needs a CA.
Facts (verified 27 Nov 2026): CBDT press releases of 13 and 23 December 2025 - data analytics flagged high-risk claims,
notably under sections 80G and 80GGC and the HRA exemption (section 10(13A)); a NUDGE campaign of SMS / email / portal
messages asked taxpayers to review claims and correct them through a revised return or, for earlier years, an updated
return with additional tax; employees of MNCs, PSUs, government bodies and academic institutions were among those
flagged. Site facts: revised ITR for AY 2026-27 free until 31 December 2026, fee (old 234-I) up to 31 March 2027; ITR-U
within 48 months with additional tax; penalty under section 270A - 50% of tax for under-reporting, 200% for
misreporting; HRA needs rent receipts and the landlord's PAN where annual rent exceeds Rs 1 lakh; HRA, 80C, 80G and 80GGC
are old-regime deductions; 80GGC donations only to registered political parties and not in cash. No fees, no office
claims, no statistics beyond the CBDT releases."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "income-tax-notice-salaried-employees-bogus-deduction-hra-80g-80ggc-nudge-campaign-revised-return-2026"

C = contact("the notice, SMS or e-mail, your ITR and Form 130 (old Form 16) for the year, your AIS, and the proof behind each deduction questioned - rent receipts and rent agreement with the landlord's PAN, donation receipts with the donee's details and payment proof, insurance, loan or investment statements")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Notice for Salaried Employees on Bogus Deductions (2026): HRA, 80C, 80G and 80GGC Claims, the CBDT NUDGE Campaign and How to Correct or Reply",
    em="fix the claim before it becomes a penalty.",
    kicker="/ Salaried employees, including NRIs and returning residents &middot; Deduction and exemption claims &middot; Updated 2026-11-27",
    lead=("<strong>Since December 2025 the Income Tax Department has been using data analytics to flag salaried taxpayers whose deductions look unsupported - especially donations under sections 80G and 80GGC and HRA exemptions - and has sent SMS, e-mail and portal messages asking them to review and correct their returns.</strong> "
          "A claim you can prove is safe; a claim you cannot support should be withdrawn through a revised or updated return before a notice turns into a demand with penalty. "
          "Ignoring the message can lead to scrutiny or reassessment."),
    sections=[
        ("/ What is being flagged", "The claims the department is checking.",
         table(["Claim", "What gets questioned", "What proves it"], [
             ["HRA (section 10(13A))", "Rent paid to relatives without real payment, rent receipts without the landlord's PAN, inflated rent", "Rent agreement, receipts, bank transfers, landlord's PAN where annual rent exceeds Rs 1 lakh, and the landlord showing the rent as income"],
             ["Donations (80G, 80GGC)", "Donations to entities or political parties linked to cash-back arrangements, or paid in cash", "Receipt from an eligible donee or registered political party, payment through banking channels, donee reporting"],
             ["80C, 80D, 80E and similar", "Claims with no matching premium, investment or loan record", "Statements, premium receipts, loan certificates"],
             ["Regime", "Old-regime deductions claimed while on the new regime", "The regime chosen for the year"]])
         + ul("<strong>How you hear:</strong> an SMS, e-mail or message on the e-filing portal under the NUDGE campaign, an e-campaign or compliance query, or a formal notice under section 143(2), 133(6) or 148A.",
              "<strong>Employers too:</strong> the CBDT said employees of multinationals, PSUs, government bodies and academic institutions were among those flagged, so claims passed through payroll are not immune.")),
        ("/ How to respond", "Correct, or defend with papers.",
         ul("<strong>If the claim is genuine:</strong> keep it, collect the proof, and reply to any query or notice with the documents.",
            "<strong>If it cannot be supported:</strong> withdraw it - a revised return for AY 2026-27 is free until 31 December 2026 (with a fee up to 31 March 2027); for earlier years an updated return (ITR-U) within 48 months, paying the additional tax.",
            "<strong>If a notice has already come:</strong> reply within the time given; correcting voluntarily before an addition is made generally reduces exposure.",
            "<strong>Do not argue a claim you cannot document:</strong> under-reporting attracts a penalty of 50% of the tax under section 270A, and misreporting such as fake receipts 200%.")),
        ("/ For NRIs and returning residents", "Common traps.",
         ul("HRA and most deductions are available only under the old regime, and many NRIs have no Indian salary to claim HRA against.",
            "NRIs cannot claim the section 87A rebate or some resident-only deductions; a refund claimed on that basis is likely to be questioned.",
            "Returning residents should check that Form 130 from an Indian employer matches the return and the AIS.")
         + call_box("Deduction notices for salaried people", ["Reviewing HRA, 80C, 80G and 80GGC claims",
                                                              "Revised and updated returns to withdraw claims",
                                                              "Replies to 143(2), 133(6) and 148A notices",
                                                              "Penalty exposure under section 270A",
                                                              "NRI and returning-resident returns"],
                    "The message or notice, ITR and proof of each claim.")
         + sources("CBDT press releases of 13 and 23 December 2025 on bogus deduction and exemption claims and the NUDGE campaign; Income-tax Act (sections 10(13A), 80C, 80D, 80G, 80GGC, 139(5), 139(8A), 143(2), 148A, 270A) and the corresponding provisions of the Income-tax Act, 2025; site revised return, ITR-U, HRA and notice reply guides. Checked 27 November 2026.")),
    ],
    faqs=[("Why are salaried employees getting income tax notices for deductions?", "The department's data analytics has flagged returns where deductions look unsupported - especially donations under sections 80G and 80GGC and HRA exemptions - and since December 2025 it has sent SMS, e-mail and portal messages under a NUDGE campaign asking taxpayers to review and correct them, followed by queries or notices where needed."),
          ("What should I do if I claimed a deduction I cannot prove?", "Withdraw it before the department makes an addition: file a revised return for AY 2026-27 (free until 31 December 2026, with a fee up to 31 March 2027) or, for earlier years, an updated return (ITR-U) within 48 months, paying the additional tax. Correcting voluntarily generally reduces penalty exposure."),
          ("Can I get a notice for HRA claimed on rent paid to my parents?", "Rent paid to a parent can be valid if the rent is actually paid, there is an agreement and receipts, payments go through the bank, and the parent shows the rent as income in their return. Claims without real payment, or without the landlord's PAN where annual rent exceeds Rs 1 lakh, are the ones being questioned."),
          ("Why are donations under 80GGC being checked?", "The CBDT has flagged claims for donations to political parties linked to cash-back arrangements. The deduction is available only for contributions to registered political parties made other than in cash, backed by a proper receipt."),
          ("What is the penalty for a bogus deduction claim?", "If income is under-reported the penalty under section 270A is 50% of the tax on it; if it is misreported - for example through fake rent or donation receipts - the penalty is 200% of the tax, in addition to the tax and interest."),
          ("What should I send to respond to a deduction notice or nudge message?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice, SMS or e-mail, your ITR and Form 130 (old Form 16), your AIS, and the proof behind each claim questioned - rent agreement and receipts with the landlord's PAN, donation receipts and payment proof, insurance, loan or investment statements. We review each claim, then either defend it or file the revised or updated return. You keep your own e-filing login."),
          ("Can BQP help salaried employees and NRIs with these notices?", "Yes. CA Durgesh Chavda works online with salaried employees, NRIs and returning residents on deduction reviews, corrections and notice replies. " + C)],
    related=[("section-143-2-scrutiny-notice-response-india.html", "Section 143(2) scrutiny"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("revised-itr-section-139-5-deadline-31-december-2026-india.html", "Revised ITR by 31 December 2026"),
             ("itr-u-updated-return-48-months-section-139-8a-india.html", "Updated return (ITR-U)"),
             ("hra-exemption-2026-formula-calculation-8-metro-cities-50-percent-new-regime-section-10-13a.html", "HRA exemption rules")],
    cta_h="Got a deduction notice or nudge message?", cta_b=C,
    keywords="income tax notice salaried employees, fake deduction notice, bogus deduction income tax, hra notice income tax, 80ggc political donation notice, 80g donation notice, cbdt nudge campaign deductions, withdraw wrong deduction revised return",
    desc="Income tax notices and nudge messages to salaried employees over bogus or unsupported deductions - HRA, 80C, 80G and 80GGC - what the CBDT is flagging, how to correct through a revised or updated return, the section 270A penalty, and what to send.",
    howto={"name": "How to respond to a deduction nudge or notice", "description": "From the message to a corrected or defended return.", "steps": [
        {"name": "Read the message", "text": "Note which deduction and year it questions, and any deadline."},
        {"name": "Check the proof", "text": "Collect rent, donation, insurance or loan documents for each claim."},
        {"name": "Correct or defend", "text": "Withdraw unsupported claims by revised or updated return; defend genuine ones with papers."},
        {"name": "Reply on time", "text": "Respond to any query or notice within the time given."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KA complete")
