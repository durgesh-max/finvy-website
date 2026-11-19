# -*- coding: utf-8 -*-
"""Batch DN (19 Nov 2026): GIFT City (IFSC) for NRIs - accounts, FDs, funds, insurance, tax and when it helps. Call-first.
Demand: autocomplete sweep 19 Nov 2026 (ac17), all 7 markets: "can nri invest in gift city", "gift city for nri
investment", "gift city fd for nri", "gift city account for nri", "gift city funds for nri", "gift city taxation for
nri", "nri investment through gift city"; existing GIFT City pages are fund-setup oriented.
Facts (checked 19 Nov 2026): products for NRIs - foreign-currency deposits with IFSC Banking Units, IFSC mutual funds /
retail schemes and AIFs (AIF minimums around USD 150,000), securities on India INX / NSE IX, bonds, insurance (Business
Today, 18 Apr 2026); interest on deposits with an offshore banking unit received by a non-resident or not-ordinarily-
resident person exempt under the old section 10(15)(viii), carried into the Income-tax Act, 2025 schedules; Income-tax
Act, 2025 Schedule VI holds IFSC exemptions, e.g. specified funds' income attributable to non-resident unit holders
(Bhatt & Joshi, 21 Oct 2026); Finance Act, 2025 removed the premium cap for exemption of life policies issued by IFSC
insurance offices (BDO, Feb 2025 on the proposal); residents invest only through LRS rules; Indian exemption does not
stop the home country (US, UK, Canada, Australia) taxing the income; UAE has no personal income tax."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

GC = "gift-city-for-nri-investment-fd-funds-insurance-tax-2026"

C_GC = contact("your country of residence, citizenship, the amount and currency, your goal (deposit, fund, insurance, listed securities) and time horizon")
PAGES = [dict(
    slug=GC,
    title="GIFT City for NRIs (2026): Dollar FDs, IFSC Funds, Insurance and Listed Securities - What Is Tax-Free in India and When It Actually Helps",
    em="for NRIs in the UAE, US, UK, Singapore, Canada and Australia.",
    kicker="/ NRIs &middot; GIFT City IFSC &middot; Tax &middot; Updated 2026-11-19",
    lead=("Yes, NRIs can invest through <strong>GIFT City</strong>, India's International Financial Services Centre (IFSC) in Gujarat. Everything there is held in <strong>foreign currency</strong>, usually US dollars. "
          "The main options are <strong>foreign-currency fixed deposits</strong> with the IFSC banking units of Indian and foreign banks, <strong>IFSC mutual funds, retail schemes and AIFs</strong> (AIFs typically need around USD 150,000), securities on the IFSC exchanges, and <strong>life insurance</strong> from IFSC insurance offices. "
          "Several of these are <strong>exempt from Indian tax for non-residents</strong>. Interest on IFSC banking unit deposits has long been exempt for non-residents and not-ordinarily-resident individuals, and the Income-tax Act, 2025 groups the IFSC exemptions in a schedule. But <strong>your home country may still tax the income</strong>: the US, UK, Canada and Australia tax residents on worldwide income. GIFT City is therefore most attractive for NRIs in the <strong>UAE and other no-tax countries</strong>, for returning NRIs in their RNOR years, and for anyone who wants dollar exposure with an Indian bank."),
    sections=[
        ("/ What NRIs can use in GIFT City", "Products at a glance.",
         table(["Product", "What it is", "Indian tax for non-residents", "Watch"], [
             ["Foreign-currency deposits (IBU FDs)", "USD and other currency deposits with IFSC banking units of banks", "Interest exempt for non-residents and RNORs (old section 10(15)(viii), carried into the 2025 Act)", "Bank's own minimums and KYC; currency risk versus INR goals"],
             ["IFSC mutual funds and retail schemes", "Funds registered with IFSCA, investing in India or abroad", "Income of specified funds attributable to non-resident unit holders exempt, subject to conditions", "Check the scheme is a 'specified fund' and its minimum"],
             ["AIFs in GIFT City", "Category I-III funds, often with higher minimums (around USD 150,000)", "Depends on category and structure", "Lock-ins, fees, accredited-investor rules"],
             ["Listed securities on India INX / NSE IX", "Global stocks, derivatives, bonds, depository receipts", "Certain transfers on IFSC exchanges exempt; conditions apply", "Product-by-product rules"],
             ["Life insurance from IFSC insurance offices", "Dollar policies", "Finance Act, 2025 relaxed the premium cap for exemption of proceeds", "Policy terms; home-country tax on gains"]])
         + call_box("investing through GIFT City", ["Which GIFT City products fit your goal and country of residence",
                                                     "Indian tax position product by product, including RNOR years after return",
                                                     "How your home country taxes the same income",
                                                     "Funding from abroad or from NRE/FCNR accounts, and repatriation",
                                                     "Reporting in your Indian and overseas returns"],
                    "your country of residence, the amount, the products you are considering and your plans to return to India (if any).")),
        ("/ When GIFT City helps, and when it does not", "Home country decides.",
         table(["Where you live", "Indian exemption useful?", "Why"], [
             ["UAE, Qatar, Saudi Arabia, Oman, Bahrain, Kuwait", "Usually yes", "No personal income tax at home, so India's exemption means no tax overall (watch India's deemed-residence rule)"],
             ["USA", "Limited", "US citizens and residents are taxed on worldwide income; foreign funds can be PFICs with punitive US treatment"],
             ["UK, Canada, Australia", "Limited", "Residents taxed on worldwide income (UK new arrivals may have four-year FIG relief; Australian temporary residents are generally exempt on foreign investment income)"],
             ["Singapore", "Often yes", "Foreign-sourced investment income received by individuals is generally not taxed"],
             ["Returning to India (RNOR years)", "Yes, while RNOR", "IBU deposit interest exemption extends to not-ordinarily-resident individuals"]])),
        ("/ Practical points", "Before you invest.",
         ul("<strong>KYC:</strong> passport, overseas address proof, PAN or tax residency details; banks may onboard you remotely.",
            "<strong>Funding:</strong> transfer from abroad, or from NRE/FCNR accounts where the bank permits; money stays in foreign currency.",
            "<strong>Compare with FCNR deposits:</strong> FCNR(B) interest is also exempt for non-residents and RNORs; compare rates, tenure and flexibility; see <a href=\"nre-nro-fcnr-account-tax-rules.html\">NRE, NRO and FCNR</a>.",
            "<strong>Returning to India:</strong> once you become resident and ordinarily resident, exemptions tied to non-resident status stop, and residents can only invest within the LRS rules.",
            "<strong>US persons:</strong> check PFIC and reporting rules before buying any non-US fund.",
            "<strong>Home-country reporting:</strong> declare accounts and income where required (for example FBAR or T1135).")
         + '<p>Related: <a href="gift-city.html">GIFT City advisory</a> &middot; <a href="what-is-gift-city.html">what is GIFT City</a> &middot; <a href="is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026.html">is NRE interest taxed abroad</a> &middot; <a href="dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html">deemed residence for UAE NRIs</a> &middot; <a href="nri-returning-india-tax-rnor-transition.html">returning NRIs and RNOR</a>.</p>'
         + sources("International Financial Services Centres Authority Act, 2019 and IFSCA fund management and banking regulations; Income-tax Act, 1961 (section 10(15)(viii), 10(4D), 10(23FBC), 10(10D) as amended by the Finance Act, 2025) and the Income-tax Act, 2025 (IFSC exemptions in Schedule VI). Secondary sources checked 19 November 2026: Business Today (18 April 2026), Bhatt &amp; Joshi Associates (21 October 2026), BDO India (February 2025). Product availability and exemptions are conditional; confirm for each product.")),
    ],
    faqs=[("Can NRIs invest in GIFT City?", "Yes. NRIs can open foreign-currency deposits with IFSC banking units and invest in IFSC mutual funds, retail schemes, AIFs, exchange-traded products and insurance, all in foreign currency."),
          ("Is GIFT City FD interest tax-free for NRIs?", "Interest on deposits with IFSC banking units is exempt in India for non-residents and not-ordinarily-resident individuals, but your country of residence may still tax it."),
          ("Are GIFT City funds tax-free for NRIs?", "Income of specified IFSC funds attributable to non-resident unit holders is exempt in India subject to conditions; check that the scheme qualifies and how your home country taxes it."),
          ("Is GIFT City worth it for NRIs in the US or UK?", "Often less so: US and UK residents are taxed on worldwide income, and US persons face PFIC rules on foreign funds. It is most useful for NRIs in the UAE and other no-tax countries, and for returning NRIs in RNOR years."),
          ("What is the minimum investment in GIFT City?", "It depends on the product and provider; AIFs typically need around USD 150,000, while bank deposits and some retail schemes have lower minimums."),
          ("Can BQP advise on GIFT City investments?", "Yes, on the tax and regulatory side. " + C_GC)],
    related=[("gift-city.html", "GIFT City advisory"), ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR"),
             ("dubai-uae-nri-indian-income-above-15-lakh-deemed-resident-india-tax-2026.html", "Deemed residence for UAE NRIs")],
    cta_h="Considering GIFT City as an NRI?", cta_b=C_GC,
    keywords="can NRI invest in GIFT City, GIFT City for NRI investment, GIFT City FD for NRI, GIFT City account for NRI, GIFT City funds for NRI, GIFT City taxation for NRI, IFSC banking unit deposit NRI tax free, GIFT City UAE NRI",
    desc="GIFT City for NRIs (2026): dollar FDs with IFSC banking units, IFSC funds, AIFs, IFSC-exchange securities and insurance; what is exempt in India for non-residents and RNORs; why home-country tax decides the benefit (UAE vs US, UK, Canada, Australia); practical points.",
    howto={"name": "How an NRI evaluates GIFT City investments", "description": "Steps before investing.", "steps": [
        {"name": "Set the goal", "text": "Dollar deposit, fund exposure, insurance or listed securities."},
        {"name": "Check Indian tax", "text": "Confirm the product's exemption for non-residents and RNORs."},
        {"name": "Check home-country tax", "text": "Worldwide taxation, PFIC or foreign-fund rules where you live."},
        {"name": "Complete KYC and fund", "text": "Open the account with the IFSC unit; fund from abroad or NRE/FCNR."},
        {"name": "Report", "text": "Declare in your overseas return and, when resident in India, in Schedule FA."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch DN complete:", len(PAGES))
