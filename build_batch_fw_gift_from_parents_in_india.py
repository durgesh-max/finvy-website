# -*- coding: utf-8 -*-
"""Batch FW (24 Nov 2026): gift money from parents in India to a child living abroad - tax and reporting in India and in
the US, UK, Canada, Australia, Singapore and UAE. Call-first page for NRIs and their parents.
Demand: sweep ac49 (24 Nov 2026), all 7 markets: "do i pay tax on gift money from parents overseas", "can i receive money
from my parents tax free". The site covered the India side (nri-gift-indian-relatives...) but not the home-country side.
Facts (checked 24 Nov 2026):
- India: gift from a relative (parents included) is not taxed in the recipient's hands (section 56(2)(x) of the 1961 Act,
  carried into the 2025 Act; site page). Parents remit under LRS up to USD 250,000 per person per financial year; TCS
  20% on gift remittances above INR 10 lakh in a financial year (aggregate LRS), creditable/refundable in the parent's
  return (Budget 2025 threshold; bank FAQs). An NRI can also receive a rupee gift into an NRO account.
- US: gifts are not income for the recipient; a US person must file Form 3520 if gifts from a nonresident alien
  individual exceed USD 100,000 in the year; penalty for not filing up to 25% of the gift (5% a month). US gift tax is on
  the giver; non-US-person parents giving from outside the US are generally outside it.
- UK, Canada, Australia, Singapore, UAE: no tax on the recipient for a gift; income later earned on it is taxable where the
  recipient lives (UAE: no personal income tax). UK inheritance tax concerns the giver; parents who are not UK residents
  and give non-UK assets are generally outside it. Banks may ask for proof of source for large transfers."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "gift-money-from-parents-in-india-tax-usa-uk-canada-australia-form-3520-lrs-tcs-2026"

C = contact("where you live, the amount, whether your parents send it from India under LRS or from your NRO account, and what you plan to do with the money")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Gift Money From Parents in India While Living Abroad (2026): Is It Taxable in the USA, UK, Canada or Australia? Form 3520, LRS and TCS",
    em="usually tax-free, but not paperwork-free.",
    kicker="/ NRIs &middot; Gifts from family &middot; Updated 2026-11-24",
    lead=("<strong>Money your parents in India give you is not taxed as income in India, the US, the UK, Canada, Australia, Singapore or the UAE.</strong> "
          "India exempts gifts from relatives, and none of these countries taxes the person receiving a gift. The catches are paperwork and cash flow: "
          "a <strong>US person</strong> must file <strong>Form 3520</strong> if gifts from non-US parents exceed <strong>USD 100,000</strong> in a year, with penalties of up to 25% for missing it; "
          "your parents can send up to <strong>USD 250,000 each per year</strong> under the Liberalised Remittance Scheme, but the bank collects <strong>20% TCS</strong> on gift remittances above <strong>INR 10 lakh</strong> a year, which they get back through their Indian return. "
          "Income you later earn on the money is taxed where you live."),
    sections=[
        ("/ Quick answers", "What children abroad and their parents ask.",
         ul("<strong>Do I pay tax on gift money from my parents in India?</strong> No, as income: India exempts gifts from parents and other relatives, and the US, UK, Canada, Australia, Singapore and UAE do not tax the recipient of a gift.",
            "<strong>Do I have to report it?</strong> In the US, yes, on Form 3520 if gifts from non-US persons exceed USD 100,000 in the year. The UK, Canada, Australia, Singapore and UAE have no gift-reporting form for the recipient, but banks may ask where large sums came from.",
            "<strong>How much can my parents send?</strong> Up to USD 250,000 per parent per financial year (April to March) under the Liberalised Remittance Scheme.",
            "<strong>Why did the bank deduct 20%?</strong> That is TCS on gift remittances above INR 10 lakh in a year. It is not a final tax: your parents claim it against their tax or as a refund in their Indian return.",
            "<strong>Is there a cheaper route?</strong> A rupee gift into your NRO account in India attracts no TCS; moving it abroad from the NRO account then needs Forms 145 and 146 within the USD 1 million a year limit.")),
        ("/ Country by country", "The recipient's side.",
         table(["You live in", "Tax on the gift", "Reporting", "Watch out for"], [
             ["USA", "None for the recipient", "Form 3520 if gifts from non-US persons exceed USD 100,000 in the year", "Penalty up to 25% of the gift for not filing; income on the money is taxable; Indian accounts in your name go on FBAR"],
             ["UK", "None for the recipient", "No form", "Inheritance tax concerns the giver; parents who are not UK residents and give non-UK assets are generally outside it"],
             ["Canada", "None", "No form for the gift itself", "Foreign property above CAD 100,000 (such as an Indian account in your name) goes on Form T1135"],
             ["Australia", "None; a gift is not income", "No form", "Banks report large international transfers; keep the gift letter and bank records"],
             ["Singapore", "None", "No form", "Keep proof of source for the bank"],
             ["UAE", "None (no personal income tax)", "No form", "Keep proof of source for the bank"]])
         + '<p>A short <strong>gift letter</strong> from your parents (amount, date, that it is a gift with no repayment) and the bank remittance advice answer most questions from banks or tax authorities.</p>'),
        ("/ India side", "What your parents need to know.",
         ul("<strong>LRS limit:</strong> USD 250,000 per resident individual per financial year, so two parents can send up to USD 500,000 between them.",
            "<strong>TCS:</strong> 20% on the amount of gift remittances above INR 10 lakh in a financial year (counting all their LRS remittances). It shows in their Form 26AS and is adjusted in their return; it is not an extra tax.",
            "<strong>No gift tax in India</strong> for a gift to a child, and no tax for the child as a relative. Income on the money while it sits in India in the parent&rsquo;s name stays taxable in the parent&rsquo;s hands.",
            "<strong>Rupee route:</strong> parents can gift into your NRO account in India; see " + L("nri-gift-indian-relatives-section-56-fema-2026.html", "gifts to NRI relatives") + ".",
            "<strong>Students:</strong> money for a child&rsquo;s education abroad has different TCS rules; see " + L("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "parents paying for study abroad") + ".")
         + call_box("a gift from parents in India", ["The cheapest route: LRS from India or via your NRO account",
                                                     "TCS and how your parents get it back",
                                                     "Form 3520 or other home-country reporting",
                                                     "Gift letter and records",
                                                     "Tax on what you do with the money next"],
                    "your country, the amount and the route.")
         + sources("Income-tax Act, 1961, section 56(2)(x) (gifts from relatives), carried into the Income-tax Act, 2025; RBI Liberalised Remittance Scheme (USD 250,000 per financial year); Finance Act, 2025 (TCS threshold of INR 10 lakh; 20% above it for gifts and other purposes), as summarised by bank TCS FAQs; US Internal Revenue Code section 6039F and IRS Form 3520 instructions (foreign gifts above USD 100,000 from a nonresident alien individual); Canada Revenue Agency Form T1135; general position on gifts in the UK, Australia, Singapore and UAE. Checked 24 November 2026.")),
    ],
    faqs=[("Do I pay tax on gift money from my parents overseas?", "Not as income. India exempts gifts from parents and other relatives, and the US, UK, Canada, Australia, Singapore and UAE do not tax the person receiving a gift. Income you later earn on the money is taxable where you live."),
          ("Do I need to file Form 3520 for money from my parents in India?", "Yes, if you are a US person and gifts from non-US persons, including your parents, exceed USD 100,000 in the calendar year. There is no tax, but the penalty for not filing can reach 25% of the gift."),
          ("How much money can parents in India send to their child abroad?", "Up to USD 250,000 per parent per financial year under the Liberalised Remittance Scheme. The bank collects 20% TCS on gift remittances above INR 10 lakh in the year, which the parent claims back in their Indian return."),
          ("Can I receive money from my parents tax free in the UK?", "Yes. The UK does not tax the recipient of a gift, and inheritance tax concerns the giver; parents who are not UK residents giving non-UK assets are generally outside it."),
          ("Is a gift from parents taxable in Canada or Australia?", "No. Neither country taxes the recipient of a gift. In Canada, an Indian account in your name above CAD 100,000 goes on Form T1135; in Australia, keep records of the source."),
          ("Can BQP help with a gift from parents in India?", "Yes. " + C)],
    related=[("nri-gift-indian-relatives-section-56-fema-2026.html", "Gifts to NRI relatives"),
             ("inherit-money-property-from-india-living-in-uk-usa-canada-australia-2026.html", "Inheriting from India while living abroad"),
             ("tcs-20-foreign-remittance-lrs-india-2026.html", "TCS on foreign remittances"),
             ("parents-send-money-child-studying-abroad-uk-usa-canada-australia-lrs-tcs-2026.html", "Parents paying for study abroad"),
             ("how-to-file-fbar.html", "How to file the FBAR")],
    cta_h="Parents sending you money?", cta_b=C,
    keywords="gift money from parents in India tax, do I pay tax on gift money from parents overseas, Form 3520 gift from parents India, can I receive money from my parents tax free, LRS gift TCS 20%, NRI gift from parents USA UK Canada Australia",
    desc="Gift money from parents in India is not taxed as income in India, the USA, UK, Canada, Australia, Singapore or UAE. US persons file Form 3520 above USD 100,000; parents can send USD 250,000 each a year under LRS with 20% TCS above INR 10 lakh, refundable in their return. Country table and routes.",
    howto={"name": "How parents in India can send a gift to a child abroad", "description": "Steps with the least cost and paperwork.", "steps": [
        {"name": "Pick the route", "text": "LRS remittance from India, or a rupee gift into the child's NRO account."},
        {"name": "Write a gift letter", "text": "Amount, date, no repayment expected."},
        {"name": "Remit through the bank", "text": "Up to USD 250,000 per parent per year; TCS 20% above INR 10 lakh."},
        {"name": "Claim the TCS back", "text": "In the parent's Indian return for the year."},
        {"name": "Report abroad if required", "text": "Form 3520 for a US person above USD 100,000."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FW complete")
