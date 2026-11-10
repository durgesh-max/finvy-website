# -*- coding: utf-8 -*-
"""Batch BD (10 Nov 2026): demand-led pages.
1. TCS on foreign remittance: how to get it back. Facts: TCS under LRS is a tax credit for the remitter (shows in Form 26AS /
   AIS), claimed in the income-tax return; excess refunded. Since 1 October 2024 a salaried person can give the employer a
   statement of TCS (Form 12BAA, Notification 112/2024) so it is taken into account for salary TDS. TCS rates from 1 April 2026:
   nil loan-funded education; 2% self-funded education/medical above INR 10 lakh; flat 2% tour packages; 20% other above INR 10 lakh.
2. Foreign life insurance policies for residents/returning NRIs: Schedule FA has a table for cash value insurance or annuity
   contracts (ROR only); unreported policy bought from income earned while non-resident -> FAST-DS Category 2 (INR 1 lakh, up to
   INR 5 crore) by 31 December 2026; INR 10 lakh Black Money Act penalty for non-disclosure where foreign assets other than
   immovable property exceed INR 20 lakh; maturity/surrender taxability depends on facts (section 10(10D) conditions)."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 10 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def box(title, msg):
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 8px;font-weight:600">{title}</p><p style="margin:0">Message CA Durgesh Chavda on '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp</strong></a> or email '
            f'<a href="mailto:durgesh@bharatquantumprospera.com">durgesh@bharatquantumprospera.com</a>.</p></div>')


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with a short note of your situation. "
           "We reply the same working day with what is needed and a fixed-scope quote.")
PAGES = []

TCS_SLUG = "tcs-refund-foreign-remittance-lrs-how-to-claim-itr-employer-2026"
PAGES.append(dict(
    slug=TCS_SLUG,
    title="TCS Refund on Foreign Remittance: How to Get Your LRS TCS Back (ITR or Employer), 2026",
    em="it is your tax, not the bank's fee.",
    kicker="/ LRS &middot; TCS refund &middot; Updated 2026-11-10",
    lead=("The TCS your bank collects when you send money abroad is not a charge: it is tax paid in your name. It shows in your Form 26AS and AIS, and you get it back in one of two ways. "
          "Claim it in your income-tax return, where it is set against your tax and any excess is refunded; or, if you are salaried, give your employer a statement of the TCS so it reduces the tax deducted from your salary for the rest of the year. "
          "From 1 April 2026 TCS is nil on education paid from a loan, 2% above INR 10 lakh for self-funded education or medical treatment, a flat 2% on overseas tour packages, and 20% above INR 10 lakh for other purposes such as gifts and investments."),
    sections=[
        ("/ Two ways back", "Pick the faster one.",
         table(["Route", "Who can use it", "When the money comes back", "How"], [
             ["Adjust against salary TDS", "Salaried employees", "Month by month, in the same year", "Give your employer a statement of TCS (Form 12BAA under the rules notified in October 2024) with the bank's TCS certificate; the employer must take it into account for TDS"],
             ["Claim in the income-tax return", "Everyone who paid TCS", "After the return is processed", "Report the TCS in the return (it is pre-filled from Form 26AS); excess over your tax is refunded with interest where due"],
             ["Advance tax adjustment", "Business owners and professionals", "When you pay advance tax", "TCS already collected counts towards your tax for the year, so later advance tax instalments are lower"]])
         + box("Paid a lot of TCS this year?", "Hi Durgesh, I paid TCS on foreign remittances this year and want it adjusted or refunded.")),
        ("/ Step by step", "Claiming it in the return.",
         ol("Download Form 26AS or the AIS and check every TCS entry against the bank's TCS certificate (the bank issues one each quarter).",
            "If an entry is missing or wrong, ask the bank to correct its TCS return before you file. The credit follows what the bank reports.",
            "File the return for the tax year in which TCS was collected. The TCS is pre-filled; confirm it matches.",
            "If TCS is more than your tax, the excess is refunded to your pre-validated bank account after processing.",
            "Keep the remittance documents (Form A2, invoices, admission letters) in case the purpose code is questioned.")
         + "<p><strong>Common reasons the refund is stuck:</strong> TCS collected under a different PAN (for example a parent's), the bank's TCS return not yet filed, an unvalidated refund bank account, or the return not verified.</p>"),
        ("/ Pay less TCS upfront", "Planning beats refunds.",
         ul("Code education payments as education (with the admission letter and fee invoice), not as gifts or maintenance: 2% instead of 20% above INR 10 lakh.",
            "Fund education through an education loan from a specified lender where it makes sense: nil TCS.",
            "The INR 10 lakh threshold is per person per financial year, so each family member sending from their own money has their own threshold.",
            "Watch the year-end: amounts sent in March and April fall in different financial years.")
         + f'<p>Tools: <a href="lrs-tcs-calculator.html">LRS TCS calculator</a> &middot; <a href="parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html">parents paying for study abroad</a> &middot; <a href="nri-send-money-to-from-india-checker.html">send-money checker</a>.</p>'
         f'<p><strong>Sources:</strong> Income-tax Act and rules on TCS for LRS remittances; Finance Act, 2026 (rates from 1 April 2026); CBDT Notification 112/2024 (statement to employer, from 1 October 2024). <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Is TCS on foreign remittance refundable?", "Yes. TCS is tax paid in your name. It is set off against your tax in the income-tax return, and any excess is refunded."),
          ("Can my employer adjust TCS against salary TDS?", "Yes. Since 1 October 2024 a salaried employee can give the employer a statement of TCS collected (Form 12BAA under the rules notified then), and the employer must take it into account when deducting tax from salary."),
          ("Where do I see the TCS collected on my remittances?", "In Form 26AS and the Annual Information Statement on the income-tax portal, and in the quarterly TCS certificate your bank issues."),
          ("Why is my TCS not showing in Form 26AS?", "Usually because the bank has not yet filed its quarterly TCS return or used a different PAN. Ask the bank to file or correct it before you file your return."),
          ("What is the TCS rate on foreign remittance in 2026?", "From 1 April 2026: nil for education paid from a loan, 2% above INR 10 lakh for self-funded education or medical treatment, a flat 2% on overseas tour packages, and 20% above INR 10 lakh for other purposes."),
          ("Can BQP help get my TCS back?", "Yes: checking Form 26AS, the employer statement and the return. " + CONTACT)],
    related=[("lrs-tcs-calculator.html", "LRS TCS calculator"), ("tcs-20-foreign-remittance-lrs-india-2026.html", "TCS 20% on foreign remittance"),
             ("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "Parents paying for study abroad")],
    cta_h="Get your TCS back faster", cta_b=CONTACT,
    keywords="TCS refund foreign remittance, how to claim TCS refund LRS, TCS on foreign remittance refundable, adjust TCS against salary TDS, Form 12BAA TCS, TCS not showing in 26AS, TCS rate foreign remittance 2026, LRS TCS credit ITR",
    desc="How to get back the TCS collected on foreign remittances under LRS: claim it in your ITR or adjust it against salary TDS through your employer. 2026 rates, Form 26AS checks and reasons refunds get stuck.",
    howto={"name": "How to claim back TCS on foreign remittance", "description": "Steps to recover TCS collected under the Liberalised Remittance Scheme.", "steps": [
        {"name": "Check Form 26AS", "text": "Match every TCS entry in Form 26AS or AIS with the bank's TCS certificate."},
        {"name": "Fix mismatches", "text": "Ask the bank to correct its TCS return if an entry is missing or wrong."},
        {"name": "Adjust through salary (optional)", "text": "Salaried employees can give the employer a statement of TCS so salary TDS is reduced."},
        {"name": "Claim in the return", "text": "File the income-tax return; the TCS is set off and any excess is refunded."}]}))

INS_SLUG = "foreign-life-insurance-policy-returning-nri-schedule-fa-fast-ds-tax-on-maturity"
PAGES.append(dict(
    slug=INS_SLUG,
    title="Foreign Life Insurance Policy After Moving Back to India: Schedule FA, FAST-DS and Tax on Maturity (Dubai, US, UK Policies)",
    em="the policy you forgot to report.",
    kicker="/ Returning NRIs &middot; Foreign insurance &middot; Updated 2026-11-10",
    lead=("A savings or investment-linked life policy bought from an insurer abroad (a Dubai endowment plan, a US whole-life policy, a UK investment bond) is a foreign asset for an Indian resident. "
          "Once you are resident and ordinarily resident it belongs in Schedule FA of your return every year, in the table for cash value insurance and annuity contracts, until it matures or is surrendered. "
          "If it was bought while you were a non-resident from money earned abroad and you never reported it, FAST-DS Category 2 can close the past for a flat INR 1 lakh, but only until 31 December 2026."),
    sections=[
        ("/ What applies", "Year by year.",
         table(["Your status", "Report in Schedule FA?", "Tax on growth and payouts in India"], [
             ["Non-resident", "No", "Foreign income generally not taxed in India"],
             ["Resident but not ordinarily resident (RNOR)", "No", "Foreign income generally not taxed unless received in India or from an Indian business"],
             ["Resident and ordinarily resident (ROR)", "Yes, every year until maturity or surrender", "Payouts may be taxable; whether the life-insurance exemption applies depends on the policy terms and facts"]])
         + box("Holding a policy from abroad?", "Hi Durgesh, I moved back to India and still hold a life insurance policy from abroad.")),
        ("/ If you missed it", "Before 31 December 2026.",
         ul("<strong>Bought while non-resident from foreign income, never in Schedule FA:</strong> usually FAST-DS Category 2, a flat INR 1 lakh for assets up to INR 5 crore.",
            "<strong>Premiums paid from income never taxed in India while resident:</strong> Category 1 at 60% may apply to that part. Get it reviewed.",
            "<strong>If found later instead:</strong> the Black Money Act allows a penalty of INR 10 lakh for not disclosing foreign assets in the return where foreign assets other than immovable property exceed INR 20 lakh, apart from tax on undisclosed income.")
         + f'<p>Work it out: <a href="fast-ds-2026-eligibility-checker.html">FAST-DS eligibility checker</a> &middot; <a href="fast-ds-2026-calculator-foreign-asset-disclosure-cost.html">FAST-DS cost calculator</a> &middot; <a href="fast-ds-payment-due-date-interest-calculator-itns-289-form-3-form-4.html">payment dates</a>.</p>'),
        ("/ Maturity and surrender", "Read before you cash it in.",
         ul("Report the value as the insurer shows it (surrender or cash value) and the amounts received during the year.",
            "Whether the payout is exempt depends on the policy meeting the conditions of the life-insurance exemption; these claims are examined closely for foreign policies, and tribunals have decided cases on their facts.",
            "Keep the policy document, premium history and proof of when and from what money it was bought (for example, salary while you lived abroad). Buying it while non-resident has helped taxpayers in disputes.",
            "Repatriating the proceeds to India or keeping them abroad does not change the reporting; both are visible to the tax department through information exchange.")
         + f'<p><strong>Sources:</strong> Income-tax return instructions for Schedule FA (cash value insurance contract or annuity contract); Finance Act, 2026, Chapter IV (FAST-DS); Black Money (Undisclosed Foreign Income and Assets) and Imposition of Tax Act, 2015, section 43. <em>{UPDATED}</em> General information, not advice for your situation.</p>'),
    ],
    faqs=[("Do I have to report a foreign life insurance policy in my Indian return?", "Yes, if you are resident and ordinarily resident and the policy has a cash or surrender value. It goes in Schedule FA every year until it matures or is surrendered."),
          ("Can FAST-DS cover an unreported foreign insurance policy?", "Usually yes. A policy bought while non-resident from foreign income and not shown in Schedule FA generally falls in Category 2, a flat INR 1 lakh for assets up to INR 5 crore. Declarations close on 31 December 2026."),
          ("Is the maturity amount of a Dubai or US life policy taxable in India?", "It depends on your residential status in the year of receipt and whether the policy meets the conditions of the life-insurance exemption. These claims are examined closely, so get the policy reviewed before filing."),
          ("Do I report a policy bought from an Indian insurer while I was abroad?", "No, a policy issued by an Indian insurer is not a foreign asset, even if you bought it while you were an NRI."),
          ("What if I am RNOR?", "In RNOR years Schedule FA is not required. Reporting starts in your first year as resident and ordinarily resident."),
          ("Can BQP review my foreign policy?", "Yes: residential status, Schedule FA, FAST-DS category and the tax position on maturity. " + CONTACT)],
    related=[("fast-ds-returning-nri-foreign-accounts-not-reported.html", "FAST-DS for returning NRIs"), ("fast-ds-2026-eligibility-checker.html", "FAST-DS eligibility checker"),
             ("residential-status-calculator-india-nri-rnor-section-6.html", "Residential status calculator")],
    cta_h="Moved back with a foreign policy?", cta_b=CONTACT,
    keywords="foreign life insurance policy Schedule FA, Dubai insurance policy tax India, US life insurance returning NRI India, cash value insurance contract Schedule FA, FAST-DS insurance policy, foreign ULIP tax India, maturity of foreign insurance policy taxable India",
    desc="Returning NRIs with a life policy from Dubai, the US or the UK: when it goes in Schedule FA, how FAST-DS Category 2 (INR 1 lakh) can cover a missed policy before 31 December 2026, and what to check before taking the maturity amount.",
    howto=None))

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BD complete:", len(PAGES), "pages")
