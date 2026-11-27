# -*- coding: utf-8 -*-
"""Batch FT (23 Nov 2026): Transfer pricing safe harbour vs advance pricing agreement (APA) in India under the
Income-tax Act, 2025 and Income-tax Rules, 2026. Call-first page for foreign parents of Indian subsidiaries (captives, GCCs).
Demand: sweep ac47 (23 Nov 2026), all 7 markets: "transfer pricing safe harbour rules india", "advance pricing agreement
india", "what is advance pricing agreement", "bilateral advance pricing agreement india", "types of advance pricing
agreement". Site had safe harbour mentions on GCC and TP pages but no page on safe harbour vs APA.
Facts (checked 23 Nov 2026):
- Safe harbour: section 167 of the Income-tax Act, 2025; Rules 86-102 of the Income-tax Rules, 2026 (86-93 international
  transactions); option in Form 49 (TaxGuru, Safe Harbour Rules under the 2025 Act and 2026 Rules, Part I, 28 Apr 2026;
  TaxGuru, Safe Harbour Rules 2026 for Indian subsidiaries of foreign parents, 12 Nov 2026).
- IT services (software development, ITeS, KPO, software contract R&D merged): operating profit at least 15.5% of
  operating expenses from tax year 2026-27; limit INR 2,000 crore (was INR 300 crore; earlier margins 17%-24%);
  one Form 49 covers five consecutive tax years; filed electronically, system-driven acceptance by DGIT (Systems)
  (Budget 2026; TaxGuru Part I; KPMG flash on the draft rules). Sources differ on how the INR 2,000 crore limit is tested.
- Other categories: data centre services 15% of operating cost; core auto components 12%, non-core 8.5%; corporate
  guarantee commission at least 1% a year (explicit guarantee to a wholly owned subsidiary); intra-group loans at a
  benchmark (SBI one-year MCLR for rupee loans; term reference rates such as SOFR for foreign currency) plus a
  credit-rating spread (TaxGuru Part I).
- Exclusions: associated enterprises in notified jurisdictions or no/low-tax territories; MAP not available for
  transactions accepted under safe harbour; documentation and the accountant's report (Form 48) still required.
- APA: section 168 (agreement) and 169 (returns of the taxpayer and associated enterprises); Rules 103-120; Form 50
  pre-filing, Form 51 application including rollback, Form 52 annual compliance report, Form 53 relief, Form 54 renewal;
  up to five future tax years plus rollback of up to four years; flat fee of INR 20 lakh (CBDT summary reproduced by
  TaxGuru, 9 Aug 2026); unilateral APA for IT services fast-tracked: deemed closed if not concluded within two years from
  the end of the quarter of application, extendable by six months; associated enterprises can file modified returns for
  APAs entered on or after 1 April 2026.
- CBDT signed 219 APAs in FY 2025-26 (84 bilateral), cumulative 1,034 (750 unilateral, 284 bilateral); first bilateral
  APAs with France, Ireland, Indonesia and Sweden (Income Tax Department press release, 31 March 2026)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "transfer-pricing-safe-harbour-vs-apa-india-2026-15-5-percent-it-services-form-49-advance-pricing-agreement"

C = contact("the Indian entity's activity (software, ITeS, R&amp;D, distribution, manufacturing), last year's revenue and operating costs, the related-party transactions and the parent's country")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Transfer Pricing Safe Harbour vs APA in India (2026): 15.5% IT Services Margin, Form 49 and Advance Pricing Agreements",
    em="certainty for your Indian subsidiary, two ways.",
    kicker="/ Foreign companies &middot; Transfer pricing &middot; Safe harbour and APA &middot; Updated 2026-11-23",
    lead=("<strong>An Indian subsidiary can lock in its transfer pricing in two ways: opt for the safe harbour, or sign an advance pricing agreement (APA) with the tax department.</strong> "
          "From tax year 2026-27, a single <strong>IT services safe harbour</strong> (software development, ITeS, KPO and software contract R&amp;D) accepts an operating profit of <strong>at least 15.5% of operating expenses</strong>, "
          "for eligible companies up to <strong>INR 2,000 crore</strong>, chosen once in <strong>Form 49</strong> for five tax years. It is cheap and quick, but one-sided: the parent&rsquo;s country is not bound and treaty dispute resolution is not available. "
          "An <strong>APA</strong> covers up to five future years plus four years back, can be <strong>bilateral</strong> with the parent&rsquo;s country, and suits larger or complex transactions; the filing fee is now a single prescribed amount and unilateral IT services APAs now have a two-year timeline. "
          "CBDT signed a record 219 APAs in FY 2025-26."),
    sections=[
        ("/ Quick answers", "The questions foreign parents ask first.",
         ul("<strong>What is the transfer pricing safe harbour in India?</strong> A set of margins and rates the tax department must accept for specified related-party transactions if the company opts in (section 167 of the Income-tax Act, 2025; Rules 86 to 102 of the Income-tax Rules, 2026).",
            "<strong>What is the safe harbour margin for IT services in 2026?</strong> 15.5% of operating expenses, for software development, ITeS, KPO and software contract R&amp;D together. Earlier margins were 17% to 24% with a INR 300 crore limit.",
            "<strong>What is an advance pricing agreement?</strong> A binding agreement with the Central Board of Direct Taxes on the pricing method (and often the margin) for future years, and optionally past years (section 168).",
            "<strong>Which is better?</strong> Safe harbour for a cost-plus captive whose margin is already at or above 15.5% and whose parent&rsquo;s country will accept that price. APA for bigger, unusual or two-country problems: royalties, distribution, intangibles, or where double tax is the real risk.",
            "<strong>When must Form 49 be filed?</strong> On or before the due date of the return for the first year of the option (for companies with transfer pricing reports, 30 November after the tax year).")),
        ("/ Safe harbour categories", "What the rules accept from tax year 2026-27.",
         table(["Transaction", "Safe harbour", "Key condition"], [
             ["IT services: software development, ITeS, KPO, software contract R&amp;D", "Operating profit at least 15.5% of operating expenses", "Up to INR 2,000 crore (raised from INR 300 crore); one Form 49 for five consecutive tax years; filed electronically and accepted through a system-driven process"],
             ["Data centre services to a foreign related party", "15% of operating cost", "Related-party data centre on cost-plus"],
             ["Core auto components (engine, transmission, steering, suspension, braking, EV and hybrid batteries)", "12% of operating expenses", "Manufacture and export to related parties"],
             ["Non-core auto components", "8.5% of operating expenses", "Manufacture and export to related parties"],
             ["Corporate guarantee", "Commission at least 1% a year of the amount guaranteed", "Explicit guarantee for a wholly owned subsidiary abroad"],
             ["Intra-group loan to a foreign subsidiary", "Interest at least a benchmark plus a credit spread", "Rupee loans: SBI one-year MCLR; foreign currency loans: term reference rates such as SOFR; spread by credit rating and loan size"]])
         + ul("<strong>Operating expenses</strong> include salaries, ESOP costs, reimbursements and depreciation, and exclude interest, exchange losses and income tax. Cost reimbursed by the parent without mark-up still counts in the base.",
              "<strong>Not available</strong> where the associated enterprise is in a notified jurisdiction or a territory with no or low tax.",
              "<strong>No treaty relief:</strong> a transaction accepted under safe harbour cannot go to the mutual agreement procedure, so if the parent&rsquo;s tax authority says 15.5% is too high, India will not adjust.",
              "<strong>Paperwork continues:</strong> transfer pricing documentation and the accountant&rsquo;s report (Form 48, formerly Form 3CEB) are still required.",
              "<strong>Check the rule text</strong> for your facts: commentators differ on how the INR 2,000 crore limit is measured, and the non-IT categories have their own procedure before the Assessing Officer.")
         + call_box("transfer pricing safe harbour or an APA", ["Whether your Indian entity qualifies for the IT services safe harbour",
                                                               "Your operating margin on the rules&rsquo; cost base",
                                                               "Safe harbour vs APA vs annual benchmarking for your case",
                                                               "Form 49, Form 48 and the master file",
                                                               "The parent&rsquo;s side: will the home country accept the price?"],
                    "last year&rsquo;s financials of the Indian entity, the intercompany agreement and the parent&rsquo;s country.")),
        ("/ Advance pricing agreements", "How APAs work under the 2025 Act.",
         table(["Point", "Rule"], [
             ["Types", "Unilateral (India only), bilateral or multilateral (India and the other country&rsquo;s competent authority)"],
             ["Period", "Up to five future tax years, plus rollback to up to four earlier years"],
             ["Forms", "Form 50 pre-filing consultation; Form 51 application, including rollback; Form 52 annual compliance report; Form 53 claim of relief; Form 54 renewal"],
             ["Fee", "A single prescribed fee, the same whatever the transaction value (earlier it varied with transaction value)"],
             ["IT services fast track", "A unilateral APA application for IT services is treated as closed if not concluded within two years from the end of the quarter in which it was filed, extendable by six months on request"],
             ["Associated enterprises", "For APAs entered on or after 1 April 2026, the associated enterprise can also file a return or modified return in line with the APA"],
             ["Annual compliance report", "Form 52, within 30 days of the return due date or 90 days of signing, whichever is later"],
             ["Track record", "219 APAs signed in FY 2025-26, including 84 bilateral; 1,034 since the programme began (750 unilateral, 284 bilateral)"]])
         + '<p>Bilateral APAs give protection on both sides of the transaction. India signed its first bilateral APAs with France, Ireland, Indonesia and Sweden in FY 2025-26, alongside agreements with the US, the UK, Japan and Singapore. See ' + L("transfer-pricing-india-foreign-mnc.html", "transfer pricing for foreign MNCs in India") + ' for the wider rules.</p>'),
        ("/ Which to choose", "Safe harbour, APA or annual benchmarking.",
         table(["", "Safe harbour", "APA", "Annual benchmarking (TNMM)"], [
             ["Best for", "Cost-plus IT, ITeS, R&amp;D captives and GCCs within the limit", "Large, complex or two-country risk; royalties, distribution, intangibles", "Entities whose arm&rsquo;s length margin is below the safe harbour rate"],
             ["Certainty", "India only, for the option period", "India, and the other country if bilateral", "None until assessment"],
             ["Cost and time", "Low; a form with the return", "Prescribed filing fee plus advisory; months to years", "Yearly study and possible audit"],
             ["Margin", "Fixed (15.5% for IT services)", "Negotiated", "Comparables, often 12% to 20% for captives"],
             ["Double tax protection", "No (no MAP)", "Yes if bilateral", "MAP available after an adjustment"]])
         + ul("If your captive already earns 15.5% or more on cost and the parent&rsquo;s country accepts that mark-up, the safe harbour removes Indian audit risk for five years at almost no cost.",
              "If your benchmark supports less than 15.5%, safe harbour means paying tax on a higher profit than needed; compare the extra tax with the cost of defending a lower margin.",
              "A US parent should check the US side: a higher Indian mark-up is a higher US deduction, which the IRS can question. A bilateral APA solves both sides.",
              "Groups near the global minimum tax threshold should model the effect on the Indian effective rate; see " + L("pillar-2-global-minimum-tax-india-startups-2026.html", "Pillar Two in India") + ".")),
        ("/ Steps", "Electing the IT services safe harbour.",
         ul("<strong>1. Check eligibility:</strong> activity within the IT services definition, associated enterprise not in an excluded territory, within the INR 2,000 crore limit.",
            "<strong>2. Compute the margin</strong> on the rules&rsquo; operating expense base for the current year and forecast the next four.",
            "<strong>3. Align the intercompany agreement</strong> so the parent pays cost plus at least 15.5%, with year-end true-ups.",
            "<strong>4. File Form 49</strong> electronically by the return due date of the first year, certified as the rules require.",
            "<strong>5. Keep documentation</strong> and file Form 48 and, where applicable, the " + L("master-file-form-3ceaa-india-part-a-part-b-indian-subsidiary-foreign-company-due-30-november-2026.html", "master file") + " each year.")
         + sources("Income-tax Act, 2025, sections 167 to 169; Income-tax Rules, 2026, Rules 86 to 120 and Forms 49 to 54; TaxGuru, Safe Harbour Rules under the Income Tax Act, 2025 and Rules, 2026 (Part I, 28 April 2026); TaxGuru, Safe Harbour Rules 2026 and transfer pricing for Indian subsidiaries of foreign parents (12 November 2026); TaxGuru, Income Tax Rules 2026: key changes in advance pricing agreements (9 August 2026, reproducing CBDT material); KPMG Flash News on safe harbour reforms in the draft Income-tax Rules, 2026; Union Budget 2026 safe harbour and fast-track APA announcements; Income Tax Department press release on 219 APAs signed in FY 2025-26 (31 March 2026). Checked 23 November 2026.")),
    ],
    faqs=[("What is the safe harbour margin for IT services in India from 2026?", "At least 15.5% of operating expenses for software development, ITeS, KPO and software contract R&D, from tax year 2026-27, for eligible companies up to INR 2,000 crore. One Form 49 covers five consecutive tax years."),
          ("What is an advance pricing agreement in India?", "A binding agreement between the taxpayer and the Central Board of Direct Taxes on the transfer pricing method for up to five future tax years, with an option to roll it back to four earlier years. It can be unilateral, bilateral or multilateral."),
          ("Is there a government fee for an APA in India?", "Yes. A single fee prescribed in the Income-tax Rules, 2026 is paid with the application, the same whatever the transaction value. Book a call to weigh an APA against safe harbour for the entity before applying."),
          ("How long does an APA take in India?", "Unilateral APAs for IT services are now on a fast track: if not concluded within two years from the end of the quarter of application (extendable by six months), the application is treated as closed. Other APAs have historically taken several years."),
          ("Can we use the mutual agreement procedure if we opt for safe harbour?", "No. Transactions accepted under safe harbour cannot be taken to the mutual agreement procedure, so the parent&#39;s country is not bound by the Indian price. A bilateral APA gives two-country certainty."),
        ("How does the thin capitalisation rule work, and is there a safe harbour for it?", "India's thin capitalisation rule (section 94B of the 1961 Act, now section 177 of the Income-tax Act, 2025) limits the interest an Indian company, or the Indian permanent establishment of a foreign company, can deduct on borrowings from a non-resident associated enterprise, including third-party loans the group guarantees. Where such interest is more than INR 1 crore in a year, the part above 30% of EBITDA is disallowed; the disallowed interest can be carried forward for up to eight years and deducted within the 30% room of later years. Banks and insurance companies are outside the rule. There is no safe harbour that lifts the 30% limit: India's transfer pricing safe harbour rules cover the interest rate on certain intra-group loans and the commission on corporate guarantees, which is a separate arm's length question. A subsidiary funded mostly by parent debt should model both before drawing the loan, or look at equity or compulsorily convertible instruments instead. WhatsApp +91 78018 87130 with the loan amount, interest rate, lender and last year's EBITDA, or book a call."),
          ("Is safe harbour or APA better for a GCC in India?", "For a cost-plus captive already earning 15.5% or more on cost, safe harbour is usually simplest. For large captives, mixed functions, intangibles or where double tax is the concern, an APA is usually better."),
          ("Can BQP help with safe harbour or an APA?", "Yes. " + C)],
    related=[("transfer-pricing-india-foreign-mnc.html", "Transfer pricing for foreign MNCs"),
             ("gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html", "Setting up a GCC in India"),
             ("form-3ceb-tp-audit-india-2026-30-november-checklist.html", "Transfer pricing audit checklist"),
             ("master-file-form-3ceaa-india-part-a-part-b-indian-subsidiary-foreign-company-due-30-november-2026.html", "Master file"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Subsidiary compliance calendar")],
    cta_h="Pricing your Indian subsidiary?", cta_b=C,
    keywords="transfer pricing safe harbour India 2026, safe harbour rules India IT services 15.5%, Form 49 safe harbour, advance pricing agreement India, APA India fee, bilateral APA India, types of advance pricing agreement, safe harbour vs APA, GCC transfer pricing India",
    desc="Transfer pricing safe harbour vs APA in India (2026): IT services safe harbour at 15.5% of operating expenses up to INR 2,000 crore via Form 49 for five years; other categories; APAs (Forms 50-54, single filing fee, two-year IT fast track, rollback); which to choose.",
    howto={"name": "How an Indian subsidiary opts for the IT services safe harbour", "description": "Steps under the Income-tax Rules, 2026.", "steps": [
        {"name": "Check eligibility", "text": "IT services activity, associated enterprise not in an excluded territory, within INR 2,000 crore."},
        {"name": "Compute the margin", "text": "Operating profit on operating expenses, at least 15.5%."},
        {"name": "Align the intercompany agreement", "text": "Cost plus at least 15.5% with year-end true-ups."},
        {"name": "File Form 49", "text": "Electronically by the return due date of the first year; covers five tax years."},
        {"name": "Keep documentation", "text": "Form 48 and, where applicable, the master file each year."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FT complete")
