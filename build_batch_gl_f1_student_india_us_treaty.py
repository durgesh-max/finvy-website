# -*- coding: utf-8 -*-
"""Batch GL (24 Nov 2026): Indian students on F-1 visas in the US - India-US treaty Article 21 (standard deduction on
Form 1040-NR, payments from abroad), Form 8843, FICA exemption, and the Indian side (residence in the year of leaving,
Indian income, parents' remittances and TCS, NRE/NRO accounts). Call-first page for students and parents.
Demand: sweeps ac51 (24 Nov 2026), all 7 markets: "f1 student india tax treaty", "do f1 students pay taxes".
Facts (checked 24 Nov 2026): Article 21(2) of the India-US treaty lets Indian students and business apprentices claim
the standard deduction allowed to US residents on Form 1040-NR (Publication 519 carve-out); there is no USD 5,000 wage
exemption under the India treaty; Article 21(1) exempts payments from abroad for maintenance, education or training;
FICA exemption for nonresident alien F-1 students comes from IRC 3121(b)(19), not the treaty, generally for the first five
calendar years; Form 8843 filed each year by exempt individuals (f1jobs.io, Sprintax, UCOP treaty table, MIT GSC).
Indian side from site pages: TCS on education remittances nil if paid from an education loan by a specified financial
institution, 2% above INR 10 lakh a year if self-funded (from 1 April 2026)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "f1-student-india-us-tax-treaty-article-21-standard-deduction-form-8843-fica-indian-tax-2026"

C = contact("the student's visa, year of arrival, US income (scholarship, assistantship, OPT wages), any Indian income or accounts, and how the parents send money")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Indian F-1 Students in the US (2026): India-US Tax Treaty Article 21, Standard Deduction, Form 8843, FICA and the Indian Side",
    em="the treaty gives a deduction, not a blanket exemption.",
    kicker="/ Students abroad &middot; USA &middot; Updated 2026-11-24",
    lead=("<strong>Indian students on F-1 visas usually file as US nonresident aliens, and Article 21 of the India-US tax treaty gives them something most other nonresidents do not get: the US standard deduction on Form 1040-NR.</strong> "
          "There is <strong>no USD 5,000 wage exemption</strong> under the India treaty, despite what many forums say. Money sent from India for maintenance and studies is not US income. "
          "F-1 students who are nonresident aliens are generally <strong>exempt from Social Security and Medicare (FICA)</strong> on campus and OPT wages, under US law rather than the treaty, and every F-1 student files <strong>Form 8843</strong> each year, even with no income. "
          "On the Indian side, check your residence in the year you leave, keep Indian income in an NRO account, and note that parents pay <strong>no TCS</strong> on education remittances funded by an education loan and <strong>2%</strong> above INR 10 lakh a year if self-funded."),
    sections=[
        ("/ Quick answers", "What Indian students and parents ask.",
         ul("<strong>Do F-1 students pay taxes in the US?</strong> Yes on US income such as on-campus wages, assistantships, taxable scholarships and OPT pay, usually as nonresident aliens on Form 1040-NR. Money from home is not US income.",
            "<strong>What does the India-US treaty give F-1 students?</strong> Article 21(2) lets Indian students claim the standard deduction allowed to US residents on Form 1040-NR, and Article 21(1) keeps payments from abroad for maintenance and education tax-free.",
            "<strong>Is there a USD 5,000 exemption for Indian students?</strong> No. That exemption exists in some other countries&rsquo; treaties, not India&rsquo;s.",
            "<strong>Do F-1 students pay FICA?</strong> Generally not while they are nonresident aliens (typically the first five calendar years); the exemption comes from US tax law, not the treaty. Ask the employer to stop withholding if they deducted it.",
            "<strong>What is Form 8843?</strong> A statement every F-1 student files each year to exclude days from the US residence test, even with no income.")),
        ("/ US side", "Filing as a nonresident alien student.",
         table(["Item", "Position for an Indian F-1 student"], [
             ["Filing status", "Nonresident alien (Form 1040-NR) while days are exempt, typically for the first five calendar years"],
             ["Standard deduction", "Allowed under Article 21(2) of the India-US treaty, unlike most nonresidents"],
             ["Wage exemption", "None under the India treaty"],
             ["Payments from India", "Not taxable under Article 21(1)"],
             ["FICA (Social Security, Medicare)", "Generally exempt as a nonresident alien student; not a treaty benefit"],
             ["Form 8843", "File every year, even with no income"],
             ["State tax", "Depends on the state; the federal treaty may not be followed"]])
         + '<p>US rules change yearly; confirm amounts with IRS Publication 519 or a US tax preparer. Once you become a US resident for tax (for example on H-1B after the student years), see ' + L("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "H-1B and returning to India") + '.</p>'),
        ("/ Indian side", "What the student and parents should check in India.",
         ul("<strong>Residence in the year you leave:</strong> leaving for studies (unlike employment) does not get the relaxed 182-day rule, so a student who spent 60 days or more in India in that year and 365 days in the previous four may still be resident for that Indian tax year.",
            "<strong>Indian income:</strong> interest, rent or investments in your name stay taxable in India; switch savings accounts to NRO once non-resident and file an Indian return if needed.",
            "<strong>Parents sending money:</strong> education remittances funded by an education loan from a specified financial institution carry no TCS; self-funded education carries 2% TCS above INR 10 lakh a year, claimable in the parent&rsquo;s return. See " + L("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "parents paying for study abroad") + ".",
            "<strong>Gifts from parents</strong> are not taxed in India; see " + L("gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026.html", "gift money from parents") + " (Form 3520 applies only to US persons).",
            "<strong>Coming back:</strong> foreign accounts go into Schedule FA once you are resident and ordinarily resident in India again.")
         + call_box("tax for an Indian student in the US", ["Indian residence in the year of leaving",
                                                             "NRO accounts and Indian income",
                                                             "TCS on parents' remittances",
                                                             "Coordinating with a US preparer on Form 1040-NR",
                                                             "Moving to OPT or H-1B"],
                    "the student's dates, US income, Indian income and how money is sent.")
         + sources("India-US Double Taxation Avoidance Agreement, Article 21; IRS Publication 519 (standard deduction exception for students from India); IRS Form 8843 instructions; Internal Revenue Code section 3121(b)(19) (FICA exemption for nonresident alien students); university treaty tables (University of California Office of the President) and student tax guides (Sprintax, f1jobs.io); Income-tax Act residence rules; Finance Act provisions on TCS for education remittances. Checked 24 November 2026.")),
    ],
    faqs=[("Do F-1 students pay taxes in the US?", "Yes, on US income such as on-campus wages, assistantships, taxable scholarships and OPT pay, usually as nonresident aliens on Form 1040-NR. Money sent from India for living and study costs is not US income."),
          ("What does the India-US tax treaty give F-1 students?", "Under Article 21(2), Indian students can claim the standard deduction allowed to US residents on Form 1040-NR, which most nonresidents cannot. Article 21(1) keeps payments from abroad for maintenance and education tax-free."),
          ("Is there a USD 5,000 tax exemption for Indian F-1 students?", "No. The India-US treaty does not have a USD 5,000 wage exemption; that appears in some other countries' treaties."),
          ("Do F-1 students pay Social Security and Medicare tax?", "Generally not while they are nonresident aliens, typically for the first five calendar years, under US tax law rather than the treaty. If FICA was withheld by mistake, ask the employer to refund it."),
          ("Is Form 8843 required if I had no income?", "Yes. Every F-1 student who is excluding days from the US residence test files Form 8843 each year, even with no income."),
          ("Can BQP help with the Indian side for a student abroad?", "Yes. " + C)],
    related=[("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "Parents paying for study abroad"),
             ("gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026.html", "Gift money from parents"),
             ("nri-residential-status-rnor-india.html", "NRI residential status"),
             ("india-us-dtaa-withholding-rates.html", "India-US treaty rates"),
             ("h1b-holders-returning-to-india-tax-rnor-401k-2026.html", "H-1B holders and returning to India")],
    cta_h="Student in the US, family in India?", cta_b=C,
    keywords="F1 student India tax treaty, do F1 students pay taxes, India US tax treaty Article 21 students, standard deduction Indian students 1040-NR, Form 8843 F1, FICA exemption F1 students, TCS education remittance 2026, Indian student US tax",
    desc="Indian F-1 students in the US (2026): India-US treaty Article 21 gives the standard deduction on Form 1040-NR and exempts payments from home (no USD 5,000 wage exemption), FICA exemption for nonresident students, Form 8843, and the Indian side: residence when leaving, NRO, TCS on parents' remittances.",
    howto={"name": "How an Indian F-1 student handles taxes", "description": "US and Indian steps each year.", "steps": [
        {"name": "File Form 8843", "text": "Every year, even with no income."},
        {"name": "File Form 1040-NR if you had US income", "text": "Claim the Article 21(2) standard deduction."},
        {"name": "Check FICA", "text": "Nonresident alien students are generally exempt; ask for a refund if withheld."},
        {"name": "Check Indian residence", "text": "For the year you left India; switch accounts to NRO once non-resident."},
        {"name": "Plan parents' remittances", "text": "Education loan route means no TCS; self-funded 2% above INR 10 lakh."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GL complete")
