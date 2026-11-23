# -*- coding: utf-8 -*-
"""Batch GD (24 Nov 2026): buying and selling unlisted (pre-IPO) shares in India - legality, SEBI's June 2026 caution on
unauthorised platforms, demat transfer, tax for buyer and seller (12.5% after 24 months, FMV rules), NRI / FEMA rules,
post-IPO lock-in. Call-first page for investors, ESOP holders and NRIs.
Demand: sweep ac52 (24 Nov 2026), all 7 markets: "is it legal to buy unlisted shares in india", "can you sell unlisted
shares". The site had demat and FC-TRS pages but no buy/sell guide.
Facts (checked 24 Nov 2026):
- SEBI press release 32/2026 (17 June 2026): caution against dealing in unlisted public company securities through
  unauthorised platforms; such deals are outside SEBI oversight with no exchange grievance redressal; earlier advisories
  in December 2024 and August 2016; some companies penalised by the ROC for allowing dealings on such platforms
  (Business Today, Taxmann, LiveLaw). Buying unlisted shares as a private transfer is not itself banned.
- Unlisted public companies' shares must be in demat for transfer (site demat page); private company shares usually have
  transfer restrictions in the articles.
- Tax: unlisted shares long-term after 24 months, 12.5% without indexation (from 23 July 2024); short-term at slab rates.
  Buyer paying less than fair market value is taxed on the difference above INR 50,000 (section 56(2)(x) of the 1961 Act,
  carried into the 2025 Act); seller's consideration is deemed to be FMV if lower (section 50CA). Rule 11UA valuation.
- NRIs / foreign buyers: transfer from a resident to a non-resident needs pricing at or above fair value and Form FC-TRS
  within 60 days (site FC-TRS page); TDS when buying from a non-resident (site page).
- After an IPO, pre-issue shares of non-promoter shareholders are generally locked in for six months (SEBI ICDR)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 24 November 2026."
SLUG = "buy-sell-unlisted-pre-ipo-shares-india-legal-sebi-caution-tax-nri-fema-2026"

C = contact("whether you are buying or selling, the company, how many shares and at what price, whether you are resident or NRI, and how the shares are held")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Is It Legal to Buy or Sell Unlisted (Pre-IPO) Shares in India? (2026): SEBI Caution, Demat Transfer, Tax and NRI Rules",
    em="legal as a private deal, risky on the wrong platform.",
    kicker="/ Investors &middot; Unlisted shares &middot; Updated 2026-11-24",
    lead=("<strong>Buying or selling unlisted shares in India is legal as a private transfer between buyer and seller, but SEBI warned on 17 June 2026 that dealing through unauthorised online platforms is outside its oversight, with no exchange grievance redressal if shares are not delivered.</strong> "
          "Shares of unlisted public companies move only in demat form; private company shares usually need board approval under the articles. "
          "For tax, a sale after <strong>24 months</strong> is a long-term gain taxed at <strong>12.5%</strong> without indexation; earlier, at your slab rate. Price matters both ways: a buyer paying below fair market value is taxed on the shortfall, and a seller is taxed as if paid fair value. "
          "An <strong>NRI or foreign buyer</strong> buying from a resident must pay at least fair value and file <strong>Form FC-TRS</strong> within 60 days. If the company lists, pre-IPO shares are usually locked in for six months."),
    sections=[
        ("/ Quick answers", "What investors and ESOP holders ask.",
         ul("<strong>Is it legal to buy unlisted shares in India?</strong> Yes, as a private transfer. What SEBI warns against is buying through platforms it has not authorised: those deals are outside its supervision, and some companies have been penalised for allowing them.",
            "<strong>Can you sell unlisted shares?</strong> Yes, to a willing buyer, subject to the company&rsquo;s articles (private companies usually restrict transfers) and, for unlisted public companies, through demat.",
            "<strong>How are gains on unlisted shares taxed?</strong> Long-term after 24 months: 12.5% without indexation. Short-term: at your slab rate.",
            "<strong>Can NRIs buy unlisted shares?</strong> Yes, subject to FEMA: on a repatriable basis the price must be at least fair value, and Form FC-TRS is filed within 60 days of the transfer.",
            "<strong>What happens if the company lists?</strong> Pre-IPO shares of non-promoter shareholders are generally locked in for six months after listing, so you cannot sell immediately.")),
        ("/ Buyer vs seller", "What each side must watch.",
         table(["", "Buyer", "Seller"], [
             ["Price", "Paying below fair market value: the shortfall above INR 50,000 is taxed as your income", "Selling below fair market value: your sale price is taken as fair value for tax"],
             ["Valuation", "Ask for a Rule 11UA valuation or recent funding round price", "Get a valuation report to support the price"],
             ["Tax on sale", "Your holding period starts on transfer to you", "12.5% long-term after 24 months; slab rate if shorter"],
             ["Transfer", "Demat credit for unlisted public companies; share transfer form and board approval for private companies", "Same; stamp duty on transfer"],
             ["Non-resident side", "Buying from a non-resident: deduct TDS on the seller&rsquo;s gain", "Selling to a non-resident: fair value pricing and FC-TRS"]])
         + '<p>See ' + L("dematerialisation-unlisted-shares-india-mandatory.html", "demat rules for unlisted shares") + ', ' + L("form-fc-trs-filing-checklist-india-2026.html", "the FC-TRS checklist") + ' and ' + L("tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026.html", "TDS when buying shares from a non-resident") + '.</p>'),
        ("/ Safer way to deal", "If you go ahead.",
         ul("<strong>Deal directly or through a SEBI-registered intermediary</strong>, not an app or website offering &lsquo;exclusive&rsquo; pre-IPO access or guaranteed returns.",
            "<strong>Check the company:</strong> latest financials on the MCA portal, share capital, any pending IPO filing (DRHP), and transfer restrictions in the articles.",
            "<strong>Use documented transfers:</strong> demat instruction slips or a share transfer deed, with stamp duty paid, and keep the valuation report.",
            "<strong>Plan liquidity:</strong> there is no ready market; selling may take time, and post-IPO lock-in applies if the company lists.",
            "<strong>ESOP holders selling to investors:</strong> your cost is the exercise-date value; see " + L("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback and secondary sale tax") + ".")
         + call_box("buying or selling unlisted shares", ["Valuation and pricing for tax and FEMA",
                                                           "Capital gains on the sale",
                                                           "NRI purchase: pricing, FC-TRS, TDS",
                                                           "Transfer documents and demat",
                                                           "Section 54F reinvestment of the gain"],
                    "the company, number of shares, price, residence of both sides and how the shares are held.")
         + sources("SEBI press release No. 32/2026 (17 June 2026) cautioning investors against dealing in unlisted securities on unauthorised platforms, as reported by Business Today, Taxmann and LiveLaw; Companies (Prospectus and Allotment of Securities) Rules on dematerialisation for unlisted public companies; SEBI ICDR Regulations on lock-in of pre-issue capital; Income-tax Act provisions on capital gains for unlisted shares (12.5% long-term from 23 July 2024), section 56(2)(x), section 50CA and Rule 11UA (carried into the Income-tax Act, 2025); FEMA (Non-debt Instruments) Rules, 2019 on pricing and Form FC-TRS. Checked 24 November 2026.")),
    ],
    faqs=[("Is it legal to buy unlisted shares in India?", "Yes, as a private transfer between buyer and seller. SEBI's June 2026 caution is about unauthorised online platforms, where deals fall outside its oversight and there is no exchange grievance redressal."),
          ("Can you sell unlisted shares in India?", "Yes, to a willing buyer, subject to transfer restrictions in the company's articles and, for unlisted public companies, through demat. There is no ready market, so finding a buyer can take time."),
          ("How is the sale of unlisted shares taxed in India?", "Held over 24 months: long-term capital gain at 12.5% without indexation. Held 24 months or less: short-term, taxed at your slab rate. If you sell below fair market value, fair value is taken as your sale price."),
          ("Can an NRI buy unlisted shares from a resident in India?", "Yes. On a repatriable basis the price must be at least fair value under FEMA, and Form FC-TRS must be filed within 60 days of the transfer."),
          ("Are pre-IPO shares locked in after listing?", "Generally yes: pre-issue shares held by non-promoter shareholders are locked in for six months after the IPO under SEBI rules."),
          ("Can BQP help with an unlisted share deal?", "Yes. " + C)],
    related=[("dematerialisation-unlisted-shares-india-mandatory.html", "Demat rules for unlisted shares"),
             ("form-fc-trs-filing-checklist-india-2026.html", "FC-TRS checklist"),
             ("tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026.html", "TDS when buying from a non-resident"),
             ("esop-buyback-taxation-india-2026-capital-gains-vested-options-salary-employees-founders.html", "ESOP buyback taxation"),
             ("ltcg-12-5-percent-new-capital-gains-india-2026.html", "LTCG at 12.5%")],
    cta_h="Buying or selling unlisted shares?", cta_b=C,
    keywords="is it legal to buy unlisted shares in India, can you sell unlisted shares, pre-IPO shares India, SEBI unlisted shares caution 2026, unlisted shares tax India 12.5%, NRI buy unlisted shares FC-TRS, section 56(2)(x) shares below FMV, unlisted shares demat",
    desc="Buying or selling unlisted (pre-IPO) shares in India (2026): legal as a private transfer, but SEBI's 17 June 2026 caution on unauthorised platforms; demat and transfer rules; tax at 12.5% after 24 months and FMV rules for buyer and seller; NRI pricing and FC-TRS; six-month post-IPO lock-in.",
    howto={"name": "How to buy unlisted shares in India safely", "description": "Steps for a documented transfer.", "steps": [
        {"name": "Check the company", "text": "MCA filings, share capital, transfer restrictions, any IPO filing."},
        {"name": "Agree price with a valuation", "text": "At or above fair market value to avoid tax on the shortfall."},
        {"name": "Use a documented transfer", "text": "Demat instruction or share transfer deed, stamp duty paid."},
        {"name": "Handle non-resident rules", "text": "FC-TRS within 60 days and TDS where a non-resident sells."},
        {"name": "Keep records for tax", "text": "Purchase date and cost for the 24-month holding test."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch GD complete")
