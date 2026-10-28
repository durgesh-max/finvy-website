# -*- coding: utf-8 -*-
"""Batch AI: Round 19 - verified news 28 Oct 2026: GST 1 Nov changes, Rule 96(10), FEMA foreign individuals, UAE CT/top-up tax, H-1B returnees."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours; work delivered remotely."


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def src(*pairs):
    return "<p><strong>Sources:</strong> " + "; ".join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in pairs) + ".</p>"


def updated(note=""):
    return f"<p><em>Last updated: 28 October 2026.{(' ' + note) if note else ''} Confirm against the official circular or notification before acting.</em></p>"


def steps(*pairs):
    return [{"name": n, "text": t} for n, t in pairs]


S_GST = [("TaxO: CBIC circulars after 57th GST Council", "https://taxo.online/latest-news/27-10-2026-cbic-issued-various-circulars-following-recommendations-of-57th-gst-council-meeting-covering-smoother-registration-fairer-adjudication-and-major-relief-on-itc-and-export-refunds/"),
         ("CAclubindia: notifications from 1 Nov 2026", "https://www.caclubindia.com/news/cbic-issues-new-gst-notifications-rcm-registration-and-tds-changes-from-1st-nov-2026-26905.asp"),
         ("India.com: changes from 1 Nov 2026", "https://www.india.com/business/attention-traders-modi-govt-issues-notification-for-first-set-of-gst-changes-to-kick-in-on-nov-1-check-details-here-8539796/")]
S_9610 = [("TaxGuru: Circular 264/10/2026", "https://taxguru.in/goods-and-service-tax/rule-96-10-beginning-cbic-accepts-goodluck-india-circular-264-10-2026.html")]
S_FEMA = [("India Briefing: NDI amendment for foreign individuals", "https://www.india-briefing.com/news/fema-non-debt-amendment-foreign-individuals-45618.html/"),
          ("TaxGuru: NDI Third Amendment Rules 2026", "https://taxguru.in/rbi/fema-ndi-amendment-rules-2026-foreign-individual-investment-liberalised.html")]
S_UAE = [("OPS: UAE corporate tax deadline 30 October", "https://ops.ae/blog/uae-corporate-tax-deadline-january-year-end/"),
         ("Crowe UAE: top-up tax registration", "https://www.crowe.com/ae/news/uae-top-up-tax"),
         ("Kelmer: DMTT registration deadlines", "https://kelmer.com/uae-dmtt-registration-deadlines-2026/")]
S_H1B = [("Forbes, 1 Oct 2026", "https://www.forbes.com/sites/stuartanderson/2026/10/01/judge-strikes-down-latest-version-of-100000-h-1b-immigration-fee/")]

PAGES = [
    dict(
        slug="gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars",
        title="GST Changes From 1 November 2026: What the 57th GST Council and CBIC's 8 Circulars Mean for You",
        em="refunds, registration, scrap and discounts.",
        kicker="/ News &middot; GST &middot; Updated 2026-10-28",
        lead="Following the 57th GST Council meeting on 8 October 2026, CBIC issued eight circulars dated 26 October 2026 and a set of notifications that mostly take effect on 1 November 2026. The headline changes: 90% provisional refunds for inverted duty structures, no INR 1,000 minimum for courier and postal export refunds, simpler handling of post-sale discounts, tighter rules for scrap trades, and limits on what officers can ask for at registration.",
        sections=[
            ("/ From 1 November 2026", "Notifications.",
             ul("<strong>Inverted duty refunds</strong>: businesses whose input tax exceeds output tax can get 90% of the refund provisionally, subject to risk assessment.",
                "<strong>Small exporters</strong>: the INR 1,000 minimum for refunds of tax paid on exports through courier or post is removed.",
                "<strong>Post-sale discounts</strong>: simplified credit-note provisions for discounts given by manufacturers to distributors and retailers.",
                "<strong>Reverse charge on scrap</strong>: used cooking oil, plastic waste and scrap, tyre waste and scrap, and electrical and electronic waste supplied by unregistered persons to registered persons now fall under reverse charge (Notification 04/2026-Central Tax (Rate)).",
                "<strong>Scrap dealers must register</strong>: suppliers of those items and of metal scrap (Chapters 72-81) lose the small-supplier registration exemption (Notification 06/2026-Central Tax).",
                "<strong>GST TDS on scrap</strong>: registered buyers of those items from registered suppliers must deduct GST TDS (Notification 07/2026-Central Tax).",
                "<strong>Rates</strong>: retreaded tractor tyres get a separate lower-rate entry; isabgol (psyllium seed) is exempt.")),
            ("/ The eight circulars (26 October 2026)", "What each one settles.",
             "<table><thead><tr><th>Circular</th><th>Subject</th><th>Key point</th></tr></thead><tbody>"
             "<tr><td>257/03/2026</td><td>Registration</td><td>Officers cannot seek unwarranted documents; queries only through REG-03 with a 7-working-day reply; missed timelines mean deemed approval.</td></tr>"
             "<tr><td>258/04/2026</td><td>Demand and adjudication</td><td>Show cause notices must be specific and quantified; fraud allegations need concrete evidence; demand cannot exceed the notice.</td></tr>"
             "<tr><td>259/05/2026</td><td>Pre-deposit for appeals</td><td>10% of disputed tax; refund through RFD-01 after a favourable order, even if the department appeals.</td></tr>"
             "<tr><td>260/06/2026</td><td>Input Service Distributor</td><td>Multiple ISD registrations allowed within a state for distinct verticals.</td></tr>"
             "<tr><td>261/07/2026</td><td>Banks and NBFCs</td><td>Clarifies the 50% ITC option under Section 17(4).</td></tr>"
             "<tr><td>262/08/2026</td><td>Demo vehicles</td><td>ITC on demo vehicles not blocked for dealer-agency models.</td></tr>"
             "<tr><td>263/09/2026</td><td>Export of services</td><td>Payment received into a repatriable INR account (such as SNRR) counts as foreign-exchange receipt for export of services.</td></tr>"
             "<tr><td>264/10/2026</td><td>Rule 96(10)</td><td>Omission applies retrospectively from 23 October 2017; demands based on it cannot be sustained.</td></tr>"
             "</tbody></table>"),
            ("/ What to do this week", "Action list.",
             ul("Exporters with Rule 96(10) or Rule 89(4A)/(4B) disputes: file supplementary submissions citing Circular 264/10/2026 and claim refunds of amounts paid under protest.",
                "Businesses with inverted duty structures: line up refund applications for the faster 90% provisional route.",
                "Buyers of scrap and e-waste: update purchase processes for reverse charge and GST TDS from 1 November.",
                "Service exporters paid into SNRR or similar rupee accounts: check refunds or demands that turned on the foreign-exchange condition.",
                "Pending registration applications stuck on queries: cite Circular 257/03/2026.") + src(*S_GST) + updated("Some notification numbers are as reported by secondary sources.")),
        ],
        howto=None,
        faqs=[
            ("What GST changes apply from 1 November 2026?", "90% provisional refunds for inverted duty structures, no INR 1,000 minimum for courier/postal export refunds, simpler post-sale discount credit notes, reverse charge and GST TDS on specified scrap and e-waste, compulsory registration for scrap suppliers, and minor rate changes."),
            ("When was the 57th GST Council meeting?", "8 October 2026, in New Delhi. CBIC issued eight implementing circulars (257 to 264) on 26 October 2026."),
            ("Can a GST officer ask for any document during registration?", "No. Circular 257/03/2026 bars unwarranted document requests; deficiencies must be raised in FORM GST REG-03 and missed timelines result in deemed approval."),
            ("What is the pre-deposit for a GST appeal?", "10% of the disputed tax. Circular 259/05/2026 says the refund after a favourable order is claimed through RFD-01, even if the department files a further appeal."),
            ("Can BQP help with GST refunds and disputes under these changes?", "Yes: inverted duty and export refunds, Rule 96(10) relief, show cause notice replies and appeals. " + CONTACT),
        ],
        related=[("rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026.html", "Rule 96(10) relief for exporters"), ("gst-notice-response-india-asmt-drc-gstr.html", "Responding to GST notices")],
        cta_h="GST refund or dispute affected by these changes?",
        cta_b=CONTACT,
        keywords="GST changes 1 November 2026, 57th GST Council, CBIC circular 257 to 264 2026, GST inverted duty refund 90 percent provisional, reverse charge scrap e-waste GST, GST registration circular 257/03/2026",
        desc="GST changes from 1 November 2026 after the 57th GST Council: 90% provisional inverted duty refunds, no INR 1,000 minimum on courier export refunds, reverse charge and TDS on scrap, eight CBIC circulars (257-264) on registration, adjudication, pre-deposit, ISD and export refunds.",
    ),
    dict(
        slug="rule-96-10-omitted-retrospectively-exporters-igst-refund-circular-264-2026",
        title="Rule 96(10) Omitted Retrospectively: Exporters Can Fight Old IGST Refund Demands (Circular 264/10/2026)",
        em="relief back to October 2017.",
        kicker="/ News &middot; GST Exports &middot; Updated 2026-10-28",
        lead="CBIC Circular 264/10/2026, dated 26 October 2026, accepts the Supreme Court's 6 August 2026 judgment in Goodluck India Limited and treats the omission of Rule 96(10) of the CGST Rules as effective from 23 October 2017. Show cause notices and demands that relied on Rule 96(10) cannot be sustained, and the same treatment extends to Rules 89(4A) and 89(4B).",
        sections=[
            ("/ What Rule 96(10) did", "Background.",
             ul("Rule 96(10), inserted from 23 October 2017, stopped exporters from claiming a refund of IGST paid on exports if they had bought inputs under certain concessional schemes, such as advance authorisation or EOU benefits.",
                "Thousands of exporters received demands to repay IGST refunds, often with interest and penalty.",
                "The rule was omitted from 8 October 2024 without a saving clause, and the dispute was whether pending cases survived.")),
            ("/ What changed", "Judgment and circular.",
             ul("The Supreme Court held that, without a saving clause, the omission applies to all proceedings pending on the date of omission.",
                "CBIC accepted the judgment without reservation and directed field officers to apply it: notices and demands founded on Rule 96(10) cannot be sustained at notice, adjudication or appeal stage.",
                "The circular applies the same treatment to Rules 89(4A) and 89(4B), which reduced refund amounts in similar situations.")),
            ("/ Who benefits and how", "By stage of your case.",
             "<table><thead><tr><th>Your situation</th><th>What to do</th></tr></thead><tbody>"
             "<tr><td>Show cause notice pending</td><td>Reply citing the judgment and Circular 264/10/2026; ask for the notice to be dropped.</td></tr>"
             "<tr><td>Order passed, appeal pending</td><td>File an additional submission with the circular; the demand should be set aside.</td></tr>"
             "<tr><td>Paid under protest during pending proceedings</td><td>Claim a refund of the amount paid.</td></tr>"
             "<tr><td>Refunds reduced under Rule 89(4A)/(4B), still in dispute</td><td>Seek recomputation.</td></tr>"
             "<tr><td>Matter closed without contest, or final</td><td>Not automatically reopened; whether relief is available depends on whether proceedings were pending on 8 October 2024. Needs case review.</td></tr>"
             "</tbody></table>"
             "<p>The time limit for refund claims arising from the circular is not settled; act promptly.</p>" + src(*S_9610) + updated("Based on published analysis of the circular and judgment.")),
        ],
        howto=dict(name="How an exporter uses Circular 264/10/2026", description="Steps to obtain relief from Rule 96(10) demands.",
                   steps=steps(("List affected cases", "Every notice, order, appeal and payment linked to Rule 96(10) or Rules 89(4A)/(4B) since 2017."),
                               ("Check the stage", "Was each matter pending on 8 October 2024?"),
                               ("File submissions", "Cite the Supreme Court judgment of 6 August 2026 and Circular 264/10/2026."),
                               ("Claim refunds", "For amounts paid under protest or recovered during pending proceedings."))),
        faqs=[
            ("What does Circular 264/10/2026 say?", "That the omission of Rule 96(10) applies retrospectively from 23 October 2017, following the Supreme Court's Goodluck India judgment of 6 August 2026, and that demands based on the rule cannot be sustained. The same applies to Rules 89(4A) and 89(4B)."),
            ("Can exporters get back IGST they repaid under Rule 96(10)?", "Amounts paid under protest or recovered while proceedings were pending can be claimed as refunds. Cases that were closed or became final are not automatically reopened."),
            ("Does it apply to cases in appeal?", "Yes. Appellate authorities should set aside demands based on Rule 96(10); a short additional submission with the circular and judgment is usually enough."),
            ("Is there a deadline to claim?", "The limitation period for refund claims arising from the circular is not settled, so claims should be filed promptly."),
            ("Can BQP review our Rule 96(10) exposure?", "Yes: case review, submissions, appeals and refund claims for exporters. " + CONTACT),
        ],
        related=[("gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html", "All GST changes from 1 November 2026"), ("india-iec-gst-customs-foreign-exporter-importer-2026.html", "Exporter and importer compliance")],
        cta_h="Exporter with a Rule 96(10) demand?",
        cta_b="Old demands may now be unsustainable. " + CONTACT,
        keywords="Rule 96(10) omitted retrospectively, Circular 264/10/2026, Goodluck India Supreme Court Rule 96(10), IGST refund exporters advance authorisation, Rule 89(4A) 89(4B) relief",
        desc="CBIC Circular 264/10/2026 (26 October 2026) applies the omission of Rule 96(10) retrospectively from 23 October 2017 after the Supreme Court's Goodluck India ruling. Demands cannot be sustained; Rules 89(4A)/(4B) treated the same. What exporters should do.",
    ),
    dict(
        slug="foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026",
        title="Any Foreign Individual Can Now Buy Listed Indian Shares: FEMA Schedule III Opened Beyond NRIs and OCIs",
        em="10% per person, 24% in aggregate.",
        kicker="/ News &middot; FEMA &middot; Updated 2026-10-28",
        lead="Amendments to India's Non-Debt Instruments Rules in 2026 opened the repatriable Schedule III route for listed Indian equity to any individual resident outside India, not just NRIs and OCIs. Each individual can hold less than 10% of a company's paid-up equity, and all such investors together up to 24%. Banks report the investments on Form LEC (Individual Foreign Investor).",
        sections=[
            ("/ What changed", "In plain terms.",
             ul("<strong>Who</strong>: any individual resident outside India, including NRIs and OCIs. A US, UK, Japanese or Singaporean individual can now invest directly through an Indian broker on a repatriable basis.",
                "<strong>What</strong>: equity and eligible instruments of listed Indian companies bought on recognised stock exchanges.",
                "<strong>Limits</strong>: below 10% of paid-up equity per individual; 24% aggregate for all Schedule III individual investors in a company.",
                "<strong>Breach</strong>: an individual crossing 10% must sell the excess within five trading days of settlement, or the whole holding is treated as FDI.",
                "<strong>Money</strong>: funds come by inward remittance or from repatriable accounts, through a designated repatriable rupee account used only for these investments; sale proceeds can be sent abroad.",
                "<strong>Reporting</strong>: the bank reports purchases and transfers on Form LEC (IFI).")),
            ("/ What did not change", "Restrictions that remain.",
             ul("Prior government approval is still needed where ownership or control would pass to entities or citizens of countries sharing a land border with India.",
                "Sectors that need prior approval for foreign investment still need it.",
                "Unlisted companies are outside this route; investment there follows the FDI rules.")),
            ("/ Tax for foreign individual investors", "What to plan for.",
             ul("Capital gains on listed Indian shares are taxed in India: 12.5% on long-term gains above the annual exemption and 20% on short-term gains, plus surcharge and cess, subject to treaty relief.",
                "Dividends are taxed in India, with treaty rates available on a Tax Residency Certificate and Form 10F.",
                "An Indian PAN is needed; Indian returns may be required to claim refunds of excess tax withheld.") + src(*S_FEMA) + updated("The amendment dates from mid-2026; RBI has also published draft FEMA (Foreign Investment) Rules, 2026 that may replace the NDI Rules.")),
        ],
        howto=None,
        faqs=[
            ("Can a foreigner buy shares of listed Indian companies directly?", "Yes. After the 2026 amendments, any individual resident outside India can invest in listed Indian equity on a repatriable basis under Schedule III, within the limits."),
            ("What are the investment limits?", "Below 10% of paid-up equity per individual, and 24% for all such individual foreign investors in a company combined."),
            ("What happens if I cross 10%?", "You must sell the excess within five trading days of settlement; otherwise the entire holding is treated as foreign direct investment."),
            ("How is the investment reported?", "The authorised dealer bank reports it on Form LEC (Individual Foreign Investor)."),
            ("Can BQP help a foreign individual set up and file Indian taxes?", "Yes: PAN, treaty documentation, capital gains computation, Indian returns and repatriation. " + CONTACT),
        ],
        related=[("fdi-vs-fpi-india-startup-investment.html", "FDI vs FPI in India"), ("india-us-tax-treaty-dtaa.html", "India-US tax treaty")],
        cta_h="Foreign individual investing in Indian shares?",
        cta_b=CONTACT,
        keywords="foreign individual invest Indian stock market 2026, FEMA NDI third amendment 2026, Schedule III foreign individual investor, Form LEC IFI, NRI OCI 10% 24% limit",
        desc="2026 FEMA NDI amendments let any individual resident outside India invest in listed Indian shares on a repatriable basis: under 10% per individual, 24% aggregate, Form LEC (IFI) reporting, land-border approval still required. Tax points for foreign investors.",
    ),
    dict(
        slug="uae-corporate-tax-deadline-30-october-2026-top-up-tax-registration-30-november",
        title="UAE Corporate Tax: Returns Due 30 October 2026 for January Year-Ends; Top-up Tax Registration by 30 November",
        em="two UAE deadlines this month.",
        kicker="/ News &middot; UAE &middot; Updated 2026-10-28",
        lead="UAE companies with a financial year ending 31 January 2026 must file their corporate tax return and pay within nine months, and because 31 October 2026 is a Saturday, the practical deadline is Friday 30 October. Separately, entities of multinational groups subject to the UAE's 15% Domestic Minimum Top-up Tax whose first in-scope year ended before 30 April 2026, which covers most calendar-year groups, must register with the FTA by 30 November 2026.",
        sections=[
            ("/ Corporate tax returns", "Nine months after year-end.",
             ul("Returns and payment are due nine months after the end of the tax period.",
                "31 January 2026 year-end: due 31 October 2026, a Saturday, so file and pay by Friday 30 October.",
                "31 December 2025 year-end: was due 30 September 2026; late-filing penalties have already started for those who missed it.",
                "Indian-owned UAE companies should also check how UAE profits and dividends are treated under the India-UAE DTAA and Indian FEMA overseas investment reporting.")),
            ("/ Domestic Minimum Top-up Tax registration", "For large multinational groups.",
             ul("Applies to UAE entities of multinational groups with consolidated revenue of EUR 750 million or more in at least two of the four preceding years.",
                "Entities whose first in-scope fiscal year ended before 30 April 2026 must register by 30 November 2026 (FTA Decision No. 12 of 2026); others have seven months from year-end.",
                "Late registration can attract a penalty of AED 10,000 per entity.",
                "India has its own Pillar Two rules; groups with Indian and UAE entities should coordinate both.") + src(*S_UAE) + updated("Confirm your tax period and obligations on the FTA portal.")),
        ],
        howto=None,
        faqs=[
            ("When is UAE corporate tax due for a 31 January 2026 year-end?", "Nine months later, on 31 October 2026. As that is a Saturday, file and pay by Friday 30 October 2026."),
            ("Who must register for the UAE top-up tax by 30 November 2026?", "UAE entities of multinational groups with consolidated revenue of EUR 750 million or more whose first in-scope fiscal year ended before 30 April 2026, which includes most calendar-year groups."),
            ("What is the penalty for late top-up tax registration?", "Reported as AED 10,000 per entity."),
            ("Does BQP work with UAE companies?", "Yes, on the India side: Indian subsidiaries and branches of UAE companies, India-UAE treaty planning, FEMA overseas investment reporting and repatriation, with UAE filings coordinated with UAE-registered partners. " + CONTACT),
        ],
        related=[("indian-ca-for-clients-in-uae-gulf.html", "Indian CA for clients in the UAE and Gulf"), ("uae-corporate-tax-2026-qfzp-fta-update.html", "UAE corporate tax and free zones")],
        cta_h="UAE company with Indian owners or operations?",
        cta_b=CONTACT,
        keywords="UAE corporate tax deadline 30 October 2026, UAE corporate tax return 31 January year end, UAE DMTT registration 30 November 2026, FTA Decision 12 of 2026, UAE top-up tax penalty",
        desc="UAE corporate tax returns for 31 January 2026 year-ends are due by Friday 30 October 2026. Multinational groups under the UAE 15% Domestic Minimum Top-up Tax must register by 30 November 2026 (FTA Decision 12 of 2026).",
    ),
    dict(
        slug="h1b-holders-returning-to-india-tax-rnor-401k-2026",
        title="H-1B Holders Returning to India in 2026: Tax Residency, RNOR and Your US Retirement Accounts",
        em="plan the move before you book the flight.",
        kicker="/ News &middot; NRI &middot; Updated 2026-10-28",
        lead="With the US$100,000 H-1B fee caught in litigation and new fee proposals pending, many Indian professionals in the US are weighing a move home. The Indian tax outcome depends heavily on timing: the RNOR (resident but not ordinarily resident) status can keep foreign income outside Indian tax for a period, and US retirement accounts have a special Indian tax option that must be chosen on time.",
        sections=[
            ("/ Where the H-1B fee stands", "As of October 2026.",
             ul("A federal court vacated the guidance implementing the US$100,000 fee in June 2026, and an appeals court refused to pause that order in July; the fee was not being collected in early October 2026.",
                "A further proclamation and a separate proposed filing fee mean the position is unsettled; confirm with US immigration counsel.",
                "The fee applied to new petitions for workers outside the US, not to extensions or changes of status inside the US.")),
            ("/ Indian tax residency on return", "Why the arrival date matters.",
             ul("You become resident in India for a financial year (April-March) mainly based on days spent in India in that year and earlier years.",
                "Returning NRIs are usually RNOR for a period if they were non-resident in 9 of the previous 10 years, or spent 729 days or fewer in India in the previous 7 years.",
                "As RNOR, foreign income such as US salary for the period before return, US interest or US investment gains is generally not taxed in India unless received in India or derived from a business controlled from India.",
                "Once ordinarily resident, worldwide income and foreign assets must be reported in Indian returns, including Schedule FA. Missed reporting can now be regularised under FAST-DS until 31 December 2026.")),
            ("/ 401(k), IRA and US accounts", "Decisions to make early.",
             ul("India allows income accruing in retirement accounts in notified countries, including the US, to be taxed in India on withdrawal rather than year by year, if you opt in on time with the prescribed form.",
                "US withholding and early-withdrawal penalties apply to distributions; plan with a US tax adviser before cashing out.",
                "Convert NRE and FCNR deposits to resident accounts after return and keep track of when the FCNR rate protection ends.",
                "US brokerage accounts may restrict Indian residents; plan transfers before your address changes.") + src(*S_H1B) + updated("Immigration status is outside BQP's scope; consult US immigration counsel.")),
        ],
        howto=dict(name="Tax steps for an H-1B holder returning to India", description="What to do before and after moving back.",
                   steps=steps(("Pick the arrival date", "Model your Indian residential status for this and the next two financial years."),
                               ("List US assets", "401(k), IRA, brokerage, bank accounts, RSUs and ESOPs."),
                               ("Decide on retirement-account taxation", "Opt in to tax-on-withdrawal in India before the deadline if it suits you."),
                               ("Convert accounts", "NRE/NRO to resident accounts; plan FCNR maturities."),
                               ("File both countries", "US final-year return as dual-status or non-resident; Indian return with correct status."))),
        faqs=[
            ("Is the US$100,000 H-1B fee being charged?", "As of early October 2026 it was not being collected after court rulings, but appeals and new proposals mean it may change. Check with US immigration counsel."),
            ("Will my US income be taxed in India when I move back?", "Not while you are RNOR, unless it is received in India or from a business controlled from India. Once you become ordinarily resident, worldwide income is taxable in India with credit for US tax."),
            ("How long does RNOR status last?", "It depends on your history; returning NRIs commonly qualify for one to three financial years. It is tested each year."),
            ("How is my 401(k) taxed in India?", "You can opt to have income accruing in a US retirement account taxed in India on withdrawal rather than annually, by filing the prescribed form on time; otherwise accrual can be taxable once you are ordinarily resident."),
            ("Can BQP plan my return to India?", "Yes: residency modelling, RNOR planning, retirement accounts, foreign asset reporting and coordination with a US tax adviser. " + CONTACT),
        ],
        related=[("nri-returning-india-tax-rnor-transition.html", "Returning to India: RNOR"), ("fast-ds-2026-foreign-asset-disclosure-scheme-31-december-deadline.html", "FAST-DS: fix unreported foreign assets")],
        cta_h="Moving back to India from the US?",
        cta_b="Plan residency and US accounts before you move. " + CONTACT,
        keywords="H-1B returning to India tax 2026, H-1B $100000 fee status October 2026, RNOR status returning NRI, 401k taxation India returning NRI, move back to India from US tax planning",
        desc="H-1B holders returning to India in 2026: status of the US$100,000 H-1B fee, how RNOR status keeps foreign income outside Indian tax, how 401(k)/IRA accounts are taxed in India, and the steps to take before moving.",
    ),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)

print(f"Batch AI complete: {len(PAGES)} news pages")
