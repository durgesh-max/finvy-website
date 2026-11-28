# -*- coding: utf-8 -*-
"""Batch KT (28 Nov 2026): Can an NRI work in India - FEMA residence on arrival for employment, account re-designation, the income
tax day count, remote work for a foreign employer and OCI cardholders.
Demand: sweep ac221 (28 Nov 2026), all 7 markets: 'can nri work in india' - only an FAQ on the site (PR #884). User steer
26 Nov 2026: more call bookings / WhatsApp enquiries.
Facts: Indian citizens need no permit to work in India; OCI cardholders may take up employment, with special permission needed
only for specified activities (research, journalism, missionary work, mountaineering, protected and restricted areas, and
work with foreign diplomatic missions); under FEMA a person who comes to India to take up employment is resident from arrival,
so NRE / NRO accounts are re-designated as resident accounts and foreign-currency balances can move to an RFC account; for
income tax, residential status follows the day count (182 days in the year, or 60 days plus 365 days in the four preceding
years, with the 120-day variation for visitors with Indian income above INR 15 lakh), and salary for work done in India is
income earned in India and taxable here whatever the status; a long stay working remotely for a foreign employer can make the
person resident; returning residents may be RNOR for one or more years; treaty tie-breaker and foreign tax credit (Form 67)
where both countries tax. No fees, no portal menu paths, no office claims. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "can-nri-work-in-india-fema-resident-on-arrival-tax-day-count-remote-work-oci-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your citizenship or OCI status, the country you "
     "live in now, when you plan to start working in India and for whom (Indian employer or remotely for a foreign one), and your "
     "bank accounts and investments. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Can an NRI Work in India? (2026) FEMA Residence on Arrival for a Job, NRE / NRO Re-Designation, Tax Day Count, Remote Work and OCI Cardholders",
    em="yes - but your status changes.",
    kicker="/ NRIs and OCI cardholders taking up work in India &middot; Indian or foreign employer &middot; Updated 2026-11-28",
    lead=("<strong>An Indian citizen living abroad needs no permit to work in India, and OCI cardholders can also take up employment. "
          "The catch is status: under FEMA you become resident from the day you arrive to take up a job, and for income tax the day count decides - while salary for work done in India is taxed here whatever your status.</strong> "
          "Plan the bank accounts, investments and the year of the move before the first payslip."),
    sections=[
        ("/ Two laws, two tests", "FEMA and income tax work differently.",
         table(["Question", "FEMA", "Income tax"], [
             ["When do you become resident?", "From arrival, if you come to India to take up employment", "By day count for the financial year (182 days, or 60 days plus 365 days in the previous four years)"],
             ["What changes?", "NRE / NRO accounts re-designated; resident rules for new investments", "Indian salary always taxable; foreign income taxable once resident and ordinarily resident"],
             ["Transition", "RFC account can hold foreign currency brought back", "RNOR years can keep foreign income outside Indian tax"]])
         + ul("<strong>OCI cardholders:</strong> can work in India; special permission is needed only for specified activities such as research, journalism, missionary work and mountaineering, and for protected areas.",
              "<strong>Salary for work in India:</strong> taxable in India from day one, even while you are still non-resident for the year.",
              "<strong>Both countries taxing:</strong> the tax treaty's tie-breaker decides residence, and foreign tax credit is claimed with Form 67.")),
        ("/ Remote work and the move", "Common situations.",
         ul("<strong>Working remotely from India for a foreign employer:</strong> a long stay can make you resident for tax, and the salary for days worked in India is taxable here - the employer may also face payroll and permanent establishment questions.",
            "<strong>Joining an Indian employer:</strong> the employer deducts TDS from salary; tell your banks so accounts are re-designated.",
            "<strong>Investments made as an NRI:</strong> NRE deposits can run to maturity or move to RFC; shares and funds bought as an NRI need the broker and depository records updated.",
            "<strong>Foreign pensions and accounts:</strong> report them in Schedule FA once you are resident and ordinarily resident.",
            "<strong>Timing:</strong> the date of arrival and the days in India in the year of the move decide whether that year counts as resident.")
         + call_box("an NRI or OCI cardholder starting work in India", ["Residential status for the year of the move and RNOR",
                                                                        "NRE / NRO re-designation and RFC",
                                                                        "Tax on Indian and foreign salary; treaty relief",
                                                                        "Remote work for a foreign employer",
                                                                        "Schedule FA and foreign assets"],
                    "Citizenship or OCI status, current country, start date and employer, accounts and investments.")
         + sources("Foreign Exchange Management Act, 1999 (definition of person resident in India) and the FEMA (Deposit) Regulations; Income-tax Act, 2025 on residential status, RNOR and income earned in India; MHA notification on OCI cardholder rights; site residential status, returning NRI and NRE / NRO pages.")),
    ],
    faqs=[("Can an NRI work in India?", "Yes. An Indian citizen living abroad needs no permit to work in India. Under FEMA, coming to India to take up employment makes you resident from arrival, so NRE and NRO accounts must be re-designated, and for income tax the day count decides your status for the year."),
          ("Can an OCI cardholder work in India?", "Yes. OCI cardholders can take up employment in India; special permission is needed only for specified activities such as research, journalism, missionary work and mountaineering, and for visits to protected or restricted areas."),
          ("Is my salary taxable in India if I am still an NRI?", "Salary for work done in India is income earned in India and taxable here whatever your residential status. Your status decides whether your foreign income is also taxed in India."),
          ("Can I work remotely from India for a foreign company?", "You can, but a long stay can make you resident for tax, and the salary for the days you work in India is taxable here. The foreign employer may also need to look at Indian payroll and permanent establishment risk. Plan the stay and the contract first."),
          ("What happens to my NRE account when I start working in India?", "It must be re-designated as a resident account once you become resident under FEMA. Foreign-currency money can move to a Resident Foreign Currency (RFC) account, and FCNR deposits can run to maturity."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your citizenship or OCI status, current country, when and for whom you will work in India, and your bank accounts and investments. Or book a call directly.")],
    related=[("nri-residential-status-rnor-india.html", "NRI residential status and RNOR"),
             ("nri-returning-india-tax-rnor-transition.html", "Returning NRI: tax and RNOR transition"),
             ("nre-nro-fcnr-account-tax-rules.html", "NRE, NRO and FCNR tax rules"),
             ("can-foreigner-open-bank-account-in-india-resident-nro-nre-snrr-oci-tourist-company-2026.html", "Bank accounts for foreign nationals")],
    cta_h="Moving back to work in India?", cta_b=C,
    keywords="can nri work in india, nri working in india tax, oci card work in india, remote work from india for foreign company tax, nri becomes resident fema, nre account after returning for job",
    desc="Can an NRI work in India? Yes - no permit for Indian citizens; OCI cardholders can work too. FEMA residence from arrival for a job, NRE / NRO re-designation and RFC, income tax day count, Indian salary always taxable, remote work for a foreign employer, RNOR.",
    howto={"name": "How an NRI prepares to work in India", "description": "Status, accounts, tax.", "steps": [
        {"name": "Check status for the year", "text": "Arrival date and day count; RNOR possibility."},
        {"name": "Re-designate accounts", "text": "NRE / NRO to resident; foreign currency to RFC."},
        {"name": "Plan salary tax", "text": "Indian salary taxed from day one; treaty relief and Form 67 if taxed abroad."},
        {"name": "Update investments and reporting", "text": "Broker and depository records; Schedule FA once resident."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch KT complete")
