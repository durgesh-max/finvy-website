# -*- coding: utf-8 -*-
"""Batch KD (27 Nov 2026): Capital Gains Account Scheme, 1988 (CGAS) - what it is, when to use it, Account A vs Account B,
deposit before the return due date, forms, withdrawal and use within the period, unutilised amount, closure, NRIs.
Demand: sweep ac157 (27 Nov 2026), all 7 markets: "capital gains account scheme", "... time limit", "... sbi", "... hdfc
bank", "... 1988", "... india"; the site covered CGAS only inside the section 54 page.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - CGAS timing decides whether a section 54 / 54F exemption
survives, which sellers hand to a CA.
Facts (verified 27 Nov 2026 - scheme text on the Income Tax Department site and secondary sources): framed under sections
54(2), 54B(2), 54D(2), 54F(4) and related provisions (corresponding provisions of the Income-tax Act, 2025 from 1 April 2026;
section 54 is section 82 per the site's mapping); amount not invested before the due date of the return under section
139(1) must be deposited in the scheme by then to keep the exemption; two accounts - Deposit Account-A (savings type) and
Deposit Account-B (term deposit); withdrawal from Account-B by transfer to Account-A; Form A to open, Form C to withdraw,
Form D statement of use of the earlier withdrawal, Form G to close (depositor) and Form H (nominee / legal heir); amount
withdrawn to be used within 60 days; amount not used within the section's period (two years for purchase / three years for
construction under section 54) is taxed as capital gains of the year in which the period ends; closure needs the
Assessing Officer's approval; interest is taxable; offered by notified branches of authorised banks (no bank named).
No fees, no office claims, no statistics, no portal menu paths."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "capital-gains-account-scheme-cgas-1988-time-limit-account-a-b-withdrawal-closure-nri-2026"

C = contact("the sale deed and its date, the purchase or construction plan for the new house (agreement, builder schedule or plot papers), how much of the gain you have already reinvested, the due date of your return for the year and, if an account is already open, the bank's account statement")
PAGES = [dict(
    slug=SLUG,
    title="Capital Gains Account Scheme (CGAS) 1988: Time Limit, Account A vs Account B, Forms, Withdrawal, Closure and NRIs (2026)",
    em="deposit before your return is due.",
    kicker="/ Sellers of a house, land or other assets claiming section 54 / 54F / 54B &middot; Residents and NRIs &middot; Updated 2026-11-27",
    lead=("<strong>If you have sold a house or other asset and plan to claim a section 54, 54F or 54B exemption, but have not bought or built the new asset by the due date of your income tax return, the unused gain must be deposited in the Capital Gains Account Scheme before that due date - otherwise the exemption is lost for that amount.</strong> "
          "The money then has to be used for the new asset within the time the section allows; whatever is still unused at the end of that period is taxed as a capital gain in that year."),
    sections=[
        ("/ How the scheme works", "Two accounts, one deadline.",
         table(["Point", "Rule"], [
             ["Who uses it", "Anyone claiming exemption under sections 54, 54B, 54D, 54F and related provisions who has not reinvested the full amount by the return due date"],
             ["Deadline to deposit", "Before the due date of the return for the year of sale (section 139(1) due date)"],
             ["Account-A", "Savings-type account for money you expect to draw soon"],
             ["Account-B", "Term-deposit account for money not needed for a while; withdrawals go through Account-A"],
             ["Where", "Notified branches of authorised banks that offer the scheme"],
             ["Interest", "Taxable in the year it accrues"]])
         + ul("<strong>Forms:</strong> Form A to open the account; Form C to withdraw; Form D to show how the previous withdrawal was used; Form G to close (Form H for a nominee or legal heir).",
              "<strong>Use within 60 days:</strong> money withdrawn must be spent on the new asset within 60 days of withdrawal.",
              "<strong>Show it in the return:</strong> the deposit, with the account details, supports the exemption claimed in the return for the year of sale.")),
        ("/ Time limits", "What happens if the money is not used.",
         ul("<strong>Section 54 (house to house):</strong> buy within two years or build within three years of the sale; the deposit only keeps that window open.",
            "<strong>Unused balance:</strong> any amount not used by the end of the period is taxed as long-term capital gain of the year in which the period ends.",
            "<strong>Closing the account:</strong> closure needs the Assessing Officer's approval, and the unused amount is taxed as above.",
            "<strong>Late deposit:</strong> a deposit made after the return due date does not protect the exemption - check the date before you file.")),
        ("/ NRIs and special cases", "Where people get stuck.",
         ul("<strong>NRIs</strong> selling Indian property can use the scheme in the same way to keep a section 54 or 54F claim open; the buyer still deducts TDS on the price unless a Form 128 lower deduction certificate is obtained.",
            "<strong>Joint owners:</strong> each owner deposits and claims for their own share of the gain.",
            "<strong>Death of the depositor:</strong> the nominee or legal heir closes the account with Form H; the unused amount is not taxed in their hands as the depositor's capital gain.",
            "<strong>54EC bonds</strong> are a separate route with their own six-month deadline - the scheme does not replace them.")
         + call_box("CGAS and reinvestment planning", ["Section 54 / 54F / 54B exemption working",
                                                        "Deposit amount and deadline check",
                                                        "Withdrawal and use within the period",
                                                        "Closure and the tax on unused amounts",
                                                        "NRI property sales with Form 128"],
                    "Sale deed, reinvestment plan and return due date.")
         + sources("Capital Gains Accounts Scheme, 1988 (Income Tax Department); Income-tax Act, 1961, sections 54, 54B, 54D, 54F and 139(1), and the corresponding provisions of the Income-tax Act, 2025; site section 54, 54F, 54EC and NRI property guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is the Capital Gains Account Scheme?", "A deposit scheme under the Income-tax Act that lets you park the part of a capital gain you have not yet reinvested, so that a section 54, 54F or 54B exemption is not lost just because the return is due before the new house or asset is bought or built. The money must later be used for the new asset within the time the section allows."),
          ("What is the time limit to deposit in the Capital Gains Account Scheme?", "Before the due date of your income tax return for the year of the sale. A deposit made after that date does not protect the exemption for that amount."),
          ("What is the difference between Account A and Account B?", "Account-A works like a savings account for money you expect to draw soon; Account-B is a term deposit for money you will not need for some time. To withdraw from Account-B, the amount is first moved to Account-A."),
          ("Which banks offer the Capital Gains Account Scheme?", "Notified branches of authorised banks that run the scheme. Not every branch handles it, so check with the bank's branch before the deadline rather than on the last day."),
          ("What happens if I do not use the money in the capital gains account?", "Whatever is still unused when the section's period ends - two years for buying or three years for building under section 54 - is taxed as long-term capital gain in the year the period ends. Closing the account needs the Assessing Officer's approval."),
          ("Can an NRI open a Capital Gains Account Scheme account?", "Yes. An NRI selling Indian property can deposit the unused gain in the scheme to keep a section 54 or 54F claim open, on the same rules. TDS on the sale is separate and is deducted on the price unless a Form 128 lower deduction certificate is obtained."),
          ("What should I send to plan a CGAS deposit?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with " + "the sale deed and its date, the purchase or construction plan for the new house, how much you have already reinvested and the due date of your return. We work out the exemption, the amount to deposit and the deadline. You keep your own e-filing login.")],
    related=[("section-54-exemption-house-property-capital-gains-conditions-10-crore-limit-cgas-section-82-2026.html", "Section 54 exemption (now section 82)"),
             ("best-ca-section-54f-capital-gain-reinvestment-india.html", "Section 54F reinvestment"),
             ("54ec-bonds-section-85-capital-gains-bonds-lock-in-interest-rate-limit-nri-2026.html", "54EC bonds"),
             ("nri-selling-indian-property-capital-gains.html", "NRI property sale capital gains"),
             ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "Capital gains tax rates 2026")],
    cta_h="Gain not reinvested yet?", cta_b=C,
    keywords="capital gains account scheme, cgas, capital gains account scheme time limit, capital gains account scheme 1988, account a account b cgas, cgas withdrawal form c, cgas closure, capital gains account scheme nri, capital gains account scheme bank",
    desc="Capital Gains Account Scheme 1988 (CGAS): deposit the unused gain before the return due date to keep a section 54 / 54F / 54B exemption, Account A vs B, Forms A, C, D, G, H, use within 60 days, tax on unused amounts, closure and NRIs.",
    howto={"name": "How to use the Capital Gains Account Scheme", "description": "From sale to new asset.", "steps": [
        {"name": "Work out the exemption", "text": "Find the gain and how much you will reinvest under section 54, 54F or 54B."},
        {"name": "Deposit before the due date", "text": "Open Account-A or B with Form A at a branch that offers the scheme, before the return due date."},
        {"name": "Claim it in the return", "text": "Show the deposit and the exemption in the return for the year of sale."},
        {"name": "Withdraw and use", "text": "Withdraw with Form C and use the money within 60 days, within the section's time limit."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KD complete")
