# -*- coding: utf-8 -*-
"""Batch JO (27 Nov 2026): income tax notice for property or land purchase - why buyers get notices and how to reply
with proof of the source of funds.
Demand: sweep ac125 (27 Nov 2026), all 7 markets: "income tax notice for property purchase", "income tax notice land
purchase" (+ online / pdf / form / format / hindi / kerala variants), "income tax notice for property sale"; no
existing page title targeted it.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - high-intent notice-reply service page.
Facts (verified 27 Nov 2026): registrars report property purchases / sales in the statement of financial transactions
(SFT) - Rs 30 lakh or more up to 31 March 2026 (rule 114E), Rs 45 lakh or more (price or stamp duty value; also gifts and
JDAs) from 1 April 2026 under rule 237 of the Income-tax Rules, 2026; the data shows in the buyer's AIS. Unexplained
investment (section 69, 1961 Act numbering) taxed at 60% + 25% surcharge + 4% cess (about 78%) under section 115BBE.
Section 56(2)(x): stamp duty value above the price by more than the higher of Rs 50,000 and 10% of the price - the
difference is the buyer's income (site page). Section 269SS: no cash of Rs 20,000 or more for an immovable property
transaction, penalty equal to the amount (271D). Buyer TDS 1% on Rs 50 lakh or more from a resident seller (194-IA, now
section 393), TDS on an NRI seller under section 393 (old 195) with TAN (site). Reassessment: 148A notice within 3 years
from the end of the AY, 5 years where escaped income is Rs 50 lakh or more (site). DIN check (CBDT Circular 19/2019).
No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "income-tax-notice-for-property-land-purchase-why-you-got-it-how-to-reply-source-of-funds-2026"

C = contact("the notice PDF (the password is your PAN in lower case followed by your date of birth as DDMMYYYY), the sale deed or agreement, the payment schedule, bank statements showing every payment, any home-loan sanction letter, gift deeds or earlier sale papers for the money used, and the returns you filed for that year")
PAGES = [dict(
    slug=SLUG,
    title="Income Tax Notice for Property or Land Purchase (2026): Why You Got It, How to Reply and What Proof of Source of Funds to Send",
    em="show where every rupee came from.",
    kicker="/ Property and land buyers, NRIs and joint owners &middot; Reply online &middot; Updated 2026-11-27",
    lead=("<strong>A buyer usually gets an income tax notice after a property or land purchase because the registrar reported the deal to the Income Tax Department and the price does not match the income in the buyer's returns - or no return was filed.</strong> "
          "The notice is really one question: where did the money come from? A clear reply traces every payment to a bank account, a home loan, a gift, an earlier sale or declared income. "
          "If the source is not explained, the amount can be taxed as unexplained investment at about 78% (60% tax plus surcharge and cess)."),
    sections=[
        ("/ Why buyers get notices", "The registrar reports the deal.",
         ul("<strong>SFT reporting:</strong> the registrar or sub-registrar reports property purchases and sales in the statement of financial transactions (SFT) - Rs 30 lakh or more up to 31 March 2026, and Rs 45 lakh or more (price or stamp duty value, including gifts and joint development agreements) from 1 April 2026 under rule 237 of the Income-tax Rules, 2026. The deal then shows in your Annual Information Statement (AIS).",
            "<strong>Income does not match:</strong> the price is high compared with the income in your returns, or you did not file a return for that year.",
            "<strong>Cash:</strong> cash payments raise a source-of-cash question. A seller cannot accept Rs 20,000 or more in cash for a property deal (section 269SS); the penalty is equal to the cash accepted.",
            "<strong>Stamp duty value above the price:</strong> if the stamp duty value is higher than the price by more than the higher of Rs 50,000 and 10% of the price, the difference is taxed as the buyer's income (section 56(2)(x)).",
            "<strong>Buyer TDS not deducted:</strong> 1% TDS on a purchase of Rs 50 lakh or more from a resident seller (Form 26QB), or full TDS with a TAN when the seller is an NRI. A missing or short deduction leads to a TDS default notice.",
            "<strong>Joint purchase:</strong> the AIS can show the full price against each buyer. Each co-owner should show their own share and where it came from.")),
        ("/ Which notice you have", "Read the heading and section first.",
         table(["Notice", "What it asks", "How to respond"], [
             ["E-campaign / significant transaction alert", "Confirm the purchase and its source", "Respond on the compliance portal: accept, or give feedback with the source"],
             ["Section 133(6) information request", "Details and documents about the purchase", "Reply with the payment trail within the time stated"],
             ["Section 142(1) during assessment", "Explain the investment for that year", "Reply on e-Proceedings with the source of funds"],
             ["Section 148A show cause notice", "Why the year should not be reopened for income that escaped tax", "Reply within the time stated; available within 3 years from the end of the assessment year, or 5 years where the amount is Rs 50 lakh or more"],
             ["TDS default (194-IA / NRI seller)", "Buyer TDS not deducted or not paid", "Pay the shortfall with interest and file the TDS statement, or show the seller paid the tax"]])),
        ("/ Reply format", "There is no prescribed format - this structure works.",
         ul("<strong>Header:</strong> name, PAN, assessment year, notice section, DIN and date.",
            "<strong>The purchase:</strong> property address, date of the deed, price, stamp duty value and your share if jointly bought.",
            "<strong>Source of funds table:</strong> each payment with date, amount, bank account and source - savings, home loan, gift from a relative, sale of an earlier asset, agricultural income, NRE / NRO funds.",
            "<strong>Proof for each line:</strong> bank statements, loan sanction and disbursement letter, gift deed with the donor's bank statement and PAN, earlier sale deed and capital gains working, land records for agricultural income, foreign remittance certificates for NRIs.",
            "<strong>Close:</strong> ask for the proceedings to be dropped, and request a personal hearing by video if the officer is not satisfied.",
            "Submit on e-Proceedings (or the compliance portal for e-campaigns). The reply cannot be edited once submitted, so check the figures first. Our " + '<a href="income-tax-gst-notice-reply-draft-letter-generator-free-tool-format-word.html">free notice reply generator</a>' + " builds a first draft.")
         + call_box("property purchase notices", ["Reading the notice, DIN and time limit",
                                                  "Building the source-of-funds trail for every payment",
                                                  "Joint owner shares and AIS feedback",
                                                  "Stamp duty value and section 56(2)(x) questions",
                                                  "Buyer TDS defaults and NRI-seller TDS"],
                    "the notice PDF, sale deed and bank statements.")
         + sources("Income-tax Act, 1961 (sections 56(2)(x), 69, 115BBE, 133(6), 142(1), 148A, 194-IA, 269SS, 271D) and Income-tax Act, 2025; Income-tax Rules, 1962 (rule 114E) and Income-tax Rules, 2026 (rule 237); CBDT Circular 19/2019 (DIN); site notice-reply, section 56(2)(x), AIS and TDS guides. Checked 27 November 2026.")),
    ],
    faqs=[("Why did I get an income tax notice after buying property or land?", "Because the registrar reported the purchase to the Income Tax Department in the statement of financial transactions and it appears in your AIS. If the price does not match the income in your returns, you paid cash, the stamp duty value is much higher than the price, or buyer TDS was missed, the department asks you to explain the source of the money."),
          ("What is the limit for property purchase reporting to income tax?", "Registrars report purchases and sales of Rs 30 lakh or more for deals up to 31 March 2026. From 1 April 2026, under rule 237 of the Income-tax Rules, 2026, the limit is Rs 45 lakh or more of price or stamp duty value, and gifts and joint development agreements are covered too. A purchase below the limit can still be questioned if it shows up in other information."),
          ("How do I reply to an income tax notice for a property purchase?", "Check the DIN, note the deadline, then reply on e-Proceedings (or the compliance portal for an e-campaign) with a table of every payment, its date, the bank account and the source, backed by bank statements, the loan sanction letter, gift deeds and earlier sale papers. There is no prescribed format, and the reply cannot be edited after submission."),
          ("What happens if I cannot explain the source of money used to buy property?", "The unexplained amount can be added to your income as unexplained investment and taxed at 60% plus a 25% surcharge and cess - about 78% - under section 115BBE, with penalty proceedings possible. That is why each payment should be traced to a documented source before replying."),
          ("I bought the property jointly. Do I explain the whole price?", "Explain your own share. The AIS may show the full price against each buyer, so give feedback in the AIS if the figure is wrong and show in the reply how much each co-owner paid and from which account."),
          ("What should I send to reply to a property purchase notice?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the notice PDF, the sale deed or agreement, the payment schedule, bank statements showing every payment, any home-loan sanction and disbursement letters, gift deeds with the donor's bank statement, earlier sale papers, and your returns for that year. We check the DIN and time limit, build the source-of-funds trail and draft the reply."),
          ("Can BQP reply to my income tax notice for a land or property purchase?", "Yes. CA Durgesh Chavda works online with property buyers in India and NRIs abroad. " + C)],
    related=[("income-tax-notice-reply-letter-format-sample-how-to-submit-e-proceedings-2026.html", "Income tax notice reply letter format"),
             ("how-to-respond-to-income-tax-notice-india.html", "How to respond to an income tax notice"),
             ("section-56-2-x-gift-tax-india-2026.html", "Section 56(2)(x): stamp duty value and gifts"),
             ("ais-mismatch-itr-what-to-do-feedback-revised-return-31-december-2026-e-campaign-nri.html", "AIS mismatch and e-campaigns"),
             ("how-to-respond-section-148a-show-cause-notice-india-step-by-step.html", "Section 148A show cause notice"),
             ("nri-income-tax-notice-india-why-nris-get-notices-how-to-reply-from-abroad-dubai-us-uk-2026.html", "NRI income tax notice")],
    cta_h="Got a notice after buying property?", cta_b=C,
    keywords="income tax notice for property purchase, income tax notice land purchase, income tax notice land purchase format, income tax notice after buying property, source of funds property purchase notice, sft property purchase limit, income tax notice for property sale",
    desc="Income tax notice for property or land purchase: why buyers get notices (registrar SFT report of Rs 30 lakh / Rs 45 lakh from April 2026, income mismatch, cash, stamp duty value, buyer TDS), the reply format, the source-of-funds proof to attach, and the 78% risk on unexplained investment.",
    howto={"name": "How to reply to an income tax notice for a property purchase", "description": "Trace every payment to a documented source.", "steps": [
        {"name": "Check the notice", "text": "Verify the DIN, the section and the time limit."},
        {"name": "List the payments", "text": "Every payment for the property with date, amount and bank account."},
        {"name": "Match each source", "text": "Savings, home loan, gift, earlier sale or declared income, with proof."},
        {"name": "Submit the reply", "text": "File on e-Proceedings or the compliance portal and keep the acknowledgement."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JO complete")
