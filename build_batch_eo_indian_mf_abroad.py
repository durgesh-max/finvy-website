# -*- coding: utf-8 -*-
"""Batch EO (20 Nov 2026): Indian mutual funds held by residents of the UK (non-reporting offshore funds; HMRC
one-to-many letters of October 2026), US (PFIC), Canada (T1135), Australia (CGT, FITO), Singapore, UAE. Call-first.
Demand: sweep 20 Nov 2026 (ac30): "do i need to declare indian income in uk", "can uk citizen invest in indian mutual
funds" (all 7 markets); site had no page on UK offshore fund rules for Indian funds.
Facts (checked 20 Nov 2026): ICAEW 12 Oct 2026 - HMRC one-to-many letters asking investors in offshore funds to check
income and gains are on their Self Assessment returns, 'not a compliance check'; ISA holdings excluded; check reporting
status on GOV.UK list of approved offshore reporting funds. HMRC IFM12300: non-reporting fund = offshore fund without
reporting status; gains on disposal are offshore income gains taxed as income at marginal rates, capital losses cannot
be set against them; distributions taxed as dividends. Indian funds generally do not appear on the reporting funds list
(adviser commentary; HMRC forum replies) - check each fund. From 6 April 2025 the remittance basis is abolished; qualifying
new residents may claim the 4-year FIG exemption. India taxes NRI gains with TDS; UK credit for Indian tax under the
treaty, subject to UK rules. US: Indian mutual funds generally PFICs (site page). Canada: T1135 if specified foreign
property cost exceeds CAD 100,000; offshore investment fund property rules (s.94.1) need case review. Australia: Indian
tax credited via FITO; CGT discount depends on residency history (foreign/temporary residents restricted for assets
acquired after 8 May 2012). Singapore: no capital gains tax; foreign-sourced income received by individuals generally
exempt. UAE: no personal income tax."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 20 November 2026."
SLUG = "indian-mutual-funds-uk-resident-non-reporting-offshore-fund-hmrc-letter-2026-us-pfic-canada-australia"

C = contact("your country of residence, when you became resident there, the Indian funds you hold (names, cost, dates), any redemptions and whether you have received an HMRC letter")
PAGES = [dict(
    slug=SLUG,
    title="Indian Mutual Funds While Living Abroad (2026): UK Non-Reporting Offshore Fund Rules and HMRC's October 2026 Letters, US PFIC, Canada T1135, Australia, Singapore, UAE",
    em="the tax in your country can be far higher than the Indian tax.",
    kicker="/ NRI &middot; Mutual funds &middot; UK offshore funds &middot; HMRC &middot; Updated 2026-11-20",
    lead=("<strong>For UK residents</strong>, Indian mutual funds are usually <strong>non-reporting offshore funds</strong>. Indian funds generally do not appear on HMRC&rsquo;s list of reporting funds, but check each fund. "
          "When you sell, the gain is an <strong>offshore income gain</strong> taxed as <strong>income at your marginal rate</strong>, up to 45%, not as a capital gain. The capital gains allowance does not apply and capital losses cannot be set off. Distributions are taxed as dividends. "
          "In <strong>October 2026 HMRC began writing to investors in offshore funds</strong>, asking them to check that past and current returns include this income and these gains. HMRC says it is not a compliance check, but errors found should be corrected. "
          "Since 6 April 2025 the remittance basis has gone, although qualifying new arrivals may use the 4-year FIG exemption. "
          "<strong>US persons</strong> face the <strong>PFIC</strong> rules on Indian funds. <strong>Canadians</strong> report them on <strong>T1135</strong> once the cost of foreign property exceeds CAD 100,000. <strong>Australians</strong> pay CGT with a credit for Indian tax. <strong>Singapore and UAE</strong> residents generally pay no tax there on the gains. India also taxes NRI gains, with TDS."),
    sections=[
        ("/ Country by country", "How your Indian funds are taxed where you live.",
         table(["Country", "How Indian mutual funds are taxed there", "Watch out for"], [
             ["United Kingdom", "Usually non-reporting offshore funds: gains taxed as income at marginal rates; distributions as dividends", "HMRC letters (Oct 2026); no CGT allowance or loss relief; FIG exemption for qualifying new residents"],
             ["United States", "Generally PFICs: excess-distribution regime unless an election applies; Form 8621", "Punitive tax and interest; FBAR and Form 8938"],
             ["Canada", "Gains taxed as capital gains; distributions as income", "T1135 above CAD 100,000 cost; offshore investment fund property rules need review"],
             ["Australia", "Gains under CGT; Indian tax credited via the foreign income tax offset", "CGT discount depends on residency history; offset can be reduced if the discount applies"],
             ["Singapore", "Generally no capital gains tax; foreign-sourced income received by individuals generally exempt", "Indian tax remains"],
             ["UAE", "No personal income tax", "India taxes gains; see the India-UAE treaty position"]])
         + call_box("My Indian mutual funds and my country's tax", ["Whether your funds are reporting or non-reporting (UK) or PFICs (US)",
                                                                    "What to do if you have received an HMRC offshore funds letter",
                                                                    "Indian TDS on redemptions and claiming treaty credit abroad",
                                                                    "Whether to hold, switch or redeem, and the order of steps",
                                                                    "Correcting past returns in India and abroad"],
                    "fund statements (CAS), redemption details, Indian TDS certificates, your residence history and any letter received.")),
        ("/ If you are UK resident", "Practical steps.",
         ul("<strong>Check status:</strong> look up each fund on GOV.UK&rsquo;s list of approved offshore reporting funds; assume non-reporting if it is not listed.",
            "<strong>Report correctly:</strong> offshore income gains go on the Self Assessment return as income; distributions as foreign dividends.",
            "<strong>Past years:</strong> if gains or income were missed, consider correcting them; your UK adviser can advise on HMRC&rsquo;s disclosure routes.",
            "<strong>Indian side:</strong> the fund house deducts TDS on NRI redemptions; file an Indian return to reconcile and claim any excess; see <a href=\"nri-mutual-funds-india-tax.html\">NRI mutual fund tax in India</a>.",
            "<strong>Credit:</strong> the UK generally gives credit for Indian tax on the same gain under the India-UK treaty, subject to UK rules; see the <a href=\"india-uk-tax-treaty-dtaa.html\">India-UK treaty guide</a>.",
            "<strong>Status changes:</strong> see <a href=\"change-nri-status-mutual-funds-demat-resident-to-nri-nri-to-resident-kyc-2026.html\">changing NRI status in funds</a>; US persons see <a href=\"what-is-pfic.html\">PFIC explained</a>.")
         + '<p>Related: <a href="returning-to-india-from-uk-isa-uk-pension-property-split-year-india-tax-2026.html">returning from the UK</a> &middot; <a href="indian-ca-for-clients-in-uk.html">Indian CA for UK clients</a> &middot; <a href="is-nre-fd-interest-taxable-in-uk-usa-canada-australia-singapore-uae-2026.html">is NRE FD interest taxable abroad</a>.</p>'
         + sources("ICAEW, 'HMRC contacts UK investors in offshore funds' (12 October 2026) and the HMRC letter text; HMRC Investment Funds Manual IFM12300 and IFM13414 (non-reporting funds, offshore income gains); GOV.UK list of approved offshore reporting funds; HMRC guidance on the FIG regime from 6 April 2025; CRA guidance on Form T1135; ATO guidance on the foreign income tax offset and CGT discount for foreign residents. Checked 20 November 2026. We advise on the Indian side and coordinate with your adviser abroad.")),
    ],
    faqs=[("Are Indian mutual funds reporting funds for UK tax?", "Generally not; Indian funds do not usually appear on HMRC's list of approved offshore reporting funds, so they are treated as non-reporting funds. Check each fund on the GOV.UK list."),
          ("How are gains on Indian mutual funds taxed in the UK?", "For non-reporting funds, gains on disposal are offshore income gains taxed as income at your marginal rate, without the capital gains allowance or loss relief; distributions are taxed as dividends."),
          ("What is HMRC's October 2026 offshore funds letter?", "An educational one-to-many letter asking investors in offshore funds to check that income and gains are included in their Self Assessment returns for current and past years; HMRC says it is not a compliance check."),
          ("Do UK residents pay Indian tax on Indian mutual fund gains too?", "Yes, India taxes the gains of non-residents with TDS; the UK generally gives credit for the Indian tax under the treaty, subject to UK rules."),
          ("How are Indian mutual funds taxed for US, Canada and Australia residents?", "US persons face PFIC rules; Canadians report on T1135 above CAD 100,000 and pay tax on gains; Australians pay CGT with a foreign income tax offset for Indian tax."),
          ("Can BQP help with the Indian side?", "Yes. " + C)],
    related=[("nri-mutual-funds-india-tax.html", "NRI mutual fund tax in India"), ("what-is-pfic.html", "PFIC explained"), ("indian-ca-for-clients-in-uk.html", "Indian CA for UK clients")],
    cta_h="Holding Indian mutual funds while living abroad?", cta_b=C,
    keywords="Indian mutual funds UK tax, non-reporting offshore fund Indian mutual fund, HMRC offshore funds letter October 2026, do I need to declare Indian income in UK, Indian mutual funds PFIC, Indian mutual funds Canada T1135, Indian mutual funds Australia tax",
    desc="Indian mutual funds for residents abroad (2026): UK - usually non-reporting offshore funds, gains taxed as income; HMRC's October 2026 letters ask investors to check returns. US PFIC, Canada T1135, Australia CGT and FITO, Singapore and UAE. Indian TDS and treaty credit.",
    howto={"name": "How a UK resident deals with Indian mutual funds", "description": "From checking fund status to correcting returns.", "steps": [
        {"name": "Check reporting status", "text": "Look up each fund on GOV.UK's reporting funds list."},
        {"name": "Work out the UK tax", "text": "Non-reporting: gains as income at marginal rates; distributions as dividends."},
        {"name": "Review past returns", "text": "Correct missed income or gains with your UK adviser."},
        {"name": "Reconcile Indian TDS", "text": "File the Indian return; claim excess TDS and use treaty credit."},
        {"name": "Decide the plan", "text": "Hold, switch or redeem in the right order."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch EO complete")
