# -*- coding: utf-8 -*-
"""Batch FL (22 Nov 2026): Doing Business in India 2026 - the facts a foreign company needs, in one place. Pillar page
written to be quoted (facts table with numbers and sources) and to route to the detailed guides. Call-first.
Demand: sweep 22 Nov 2026 (ac44, foreign), all 7 markets: "doing business in india guide", "doing business in india
2025", "doing business in india pdf", "how to open a business in india as a foreigner", "setting up wholly owned
subsidiary in india", "india fdi policy", "india fdi regulations", "why do companies outsource to india".
Every figure below is already stated, with its source, on a dedicated page of this site that was checked this month:
- Income-tax Act, 2025 in force from 1 April 2026 ("tax year"); section 195 -> 393; 80-IAC -> 140 (site pages).
- Domestic company 22% regime (25.17% effective); foreign company / branch 35% plus surcharge and cess (branch vs
  subsidiary calculator page). Dividend, royalty and technical-fee withholding 20% plus surcharge and cess, treaty
  rates usually 5% to 15% (TDS calculator page; Income Tax Department withholding table).
- FDI automatic route for most sectors; government route for entities of countries sharing a land border (Press Note 3)
  and capped sectors (FDI rules page). Contract manufacturing 100% automatic (TOLA page).
- Private company: at least two directors and two shareholders; one director resident in India for 182 days or more in
  the previous calendar year (Companies Act, 2013, section 149(3)) (company registration pages).
- FC-GPR within 30 days of allotment; FLA return by 15 July each year; late fee INR 7,500 + 0.025% a year (LSF page).
- Statutory audit for every company; income-tax return 31 October (30 November with transfer pricing); Form 3CEB 31 Oct;
  master file Part A for every constituent entity; AOC-4 within 30 days and MGT-7 within 60 days of the AGM.
- Liaison, branch and project offices need RBI approval through an authorised bank (Form FNC); liaison office annual
  activity certificate (site pages).
- GST: registration when supplies cross the threshold or for inter-state supply; exports of services zero-rated under
  LUT; most business services 18% (GST pages).
- Equalisation levy abolished (2% from 1 Aug 2024, 6% from 1 Apr 2025). DPDP Rules, 2025 notified 13 Nov 2025, main
  duties from about 13 May 2027. India has not enacted Pillar Two. India-UK CETA in force 15 July 2026.
- Foreign companies cannot buy property directly; a subsidiary can for its business; liaison office lease only."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "doing-business-in-india-2026-guide-for-foreign-companies-entity-tax-fdi-compliance-repatriation"

C = contact("your company, its country, what you want to do in India (sell, hire, manufacture, buy a company, set up a capability centre), your timeline and two or three time slots with your time zone")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Doing Business in India 2026: A Guide for Foreign Companies - Entity, FDI, Tax Rates, Compliance, Hiring, Banking and Getting Money Out",
    em="the facts in one place, and who to call.",
    kicker="/ Foreign companies &middot; India entry &middot; Updated 2026-11-22",
    lead=("<strong>Most foreign companies do business in India through a wholly owned Indian private limited company.</strong> "
          "Foreign ownership of 100% is allowed without approval in most sectors. Investors from countries that share a land border with India, and a few capped sectors, need government approval first; since Press Note 2 of 2026, land-border ownership within 10% and non-controlling no longer triggers it. "
          "The company pays <strong>about 25% tax</strong> under the 22% regime; a foreign company&rsquo;s branch pays <strong>35% plus surcharge and cess</strong>. "
          "Dividends, royalties and service fees paid abroad carry Indian withholding tax of 20% plus surcharge and cess, usually cut to <strong>5% to 15%</strong> by a tax treaty. "
          "Every company needs <strong>a director resident in India</strong>, a statutory audit, an annual tax return and RBI reporting of foreign investment. "
          "India has a new <strong>Income-tax Act, 2025</strong> from 1 April 2026, has <strong>abolished the equalisation levy</strong> and has <strong>not enacted Pillar Two</strong>. "
          "This page sets out the facts and links to the detailed guide for each step."),
    sections=[
        ("/ India at a glance for a foreign company", "Key facts, 2026.",
         table(["Topic", "The position in 2026", "Detail"], [
             ["Usual vehicle", "Wholly owned private limited company (subsidiary)", L("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "Entry structure chooser")],
             ["Foreign ownership", "100% under the automatic route in most sectors; government approval for capped sectors and for investors from countries sharing a land border (since Press Note 2 of 2026, not where that ownership is within 10% and non-controlling)", L("fdi-rules-india-2026-automatic-government-route-reporting-draft-foreign-investment-rules.html", "FDI rules 2026") + " &middot; " + L("press-note-2-2026-fdi-land-border-countries-china-10-percent-60-day-approval.html", "Press Note 2")],
             ["Directors", "At least two for a private company, one resident in India (182 days or more in the previous calendar year)", L("can-foreign-national-register-company-in-india-how-long-documents-resident-director-2026.html", "Registering as a foreigner")],
             ["Corporate tax", "22% regime: about 25.17% effective. Branch of a foreign company: 35% plus surcharge and cess", L("branch-vs-subsidiary-india-tax-calculator-foreign-company-35-percent-vs-25-percent-dividend-treaty-2026.html", "Branch vs subsidiary calculator")],
             ["Withholding on payments abroad", "20% plus surcharge and cess on royalty, technical fees, interest and dividends; treaty rate usually 5% to 15% with a tax residency certificate and Form 41", L("tds-on-payment-to-foreign-company-calculator-royalty-fts-interest-dividend-treaty-rates-2026.html", "TDS calculator")],
             ["Tax law", "Income-tax Act, 2025 from 1 April 2026 (new section and form numbers)", L("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Old and new form numbers")],
             ["Transfer pricing", "Arm&rsquo;s length pricing with group companies; accountant&rsquo;s report; master file Part A for every group entity", L("transfer-pricing-india-foreign-mnc.html", "Transfer pricing")],
             ["Foreign investment reporting", "Form FC-GPR within 30 days of issuing shares; FLA return by 15 July every year", L("fema-health-check-foreign-owned-indian-company-fc-gpr-fla-compounding-2026.html", "FEMA health check")],
             ["GST", "Registration on crossing the threshold or for inter-state supplies; exports of services zero-rated under a letter of undertaking; most business services 18%", L("gst-registration-non-resident-taxable-person-india-foreign-company-reg-09-gstr-5-2026.html", "GST for foreign businesses")],
             ["Digital businesses", "No equalisation levy since 1 April 2025; ordinary tax rules and GST apply", L("equalisation-levy-india-abolished-6-percent-2-percent-what-applies-now-foreign-digital-companies-2026.html", "Equalisation levy abolished")],
             ["Global minimum tax", "India has not enacted Pillar Two; any top-up is collected in the parent&rsquo;s country", L("beps-pillar-2-india-implementation-october-2026-update.html", "Pillar Two status")],
             ["Personal data", "DPDP Rules, 2025 notified on 13 November 2025; main duties from about 13 May 2027", L("dpdp-rules-january-2025-operational-status-october-2026.html", "DPDP timeline")],
             ["Property", "A foreign company cannot buy directly; a subsidiary can for its business; a liaison office can only lease", L("can-foreign-company-or-foreigner-buy-property-land-in-india-fema-rules-branch-subsidiary-lease-2026.html", "Property rules")],
             ["Getting money out", "Dividends, royalties and service fees, buy-back or capital reduction, each with its own tax and paperwork", L("repatriate-profits-india-foreign-parent.html", "Repatriating profits")]])
         + call_box("Planning India: a first call", ["Which structure suits what you want to do",
                                                     "Approvals, timeline and the documents your board will sign",
                                                     "Tax on the Indian entity and on money paid back to you",
                                                     "Hiring before you have an entity",
                                                     "The annual compliance you are signing up for"],
                    "your company, its country, the plan for India, your timeline and two or three time slots with your time zone.")),
        ("/ Ways to enter", "Choose by what you will do in India.",
         table(["Option", "Use it when", "Watch out for"], [
             ["Employer of record", "Testing the market with a few hires, no entity yet", "Permanent establishment risk if staff sell or sign for you; see " + L("permanent-establishment-risk-checker-india-foreign-company-2026.html", "PE risk checker")],
             ["Liaison office", "Representation and market research only, no income", "RBI approval, no billing, annual activity certificate"],
             ["Branch or project office", "Specific activities or a defined project", "RBI approval, 35% tax, parent directly exposed"],
             ["Wholly owned subsidiary", "Selling, hiring, building a team or a capability centre", "Directors, audit, transfer pricing, FEMA reporting"],
             ["Joint venture", "A local partner brings licences, customers or a capped sector", L("joint-venture-in-india-with-foreign-company-structure-fdi-shareholders-agreement-exit-2026.html", "JV structure and exit")],
             ["Acquisition", "Buying an existing Indian business", L("due-diligence-indian-company-foreign-buyer.html", "Due diligence") + " and " + L("tds-on-purchase-of-shares-from-non-resident-nri-foreign-company-unlisted-listed-rate-section-393-195-india-2026.html", "withholding on share purchases")]])),
        ("/ The first year", "What a new Indian subsidiary does.",
         ul("<strong>Before incorporation:</strong> name approval, a resident director, the registered office, and FDI route check.",
            "<strong>Incorporation and bank account:</strong> the parent remits share capital through banking channels; the bank issues the foreign inward remittance certificate and KYC.",
            "<strong>Within 30 days of issuing shares:</strong> Form FC-GPR to the RBI through the bank, with a valuation certificate. Late filing costs a fee; see the " + L("fema-late-submission-fee-calculator-fc-gpr-fc-trs-form-di-fla-apr-lsf-rbi-2026.html", "late fee calculator") + ".",
            "<strong>Registrations:</strong> PAN, TAN, GST where needed, payroll registrations (provident fund, state taxes) as staff join.",
            "<strong>Intercompany agreements:</strong> service, licence and cost-sharing agreements priced at arm&rsquo;s length.",
            "<strong>Year end, 31 March:</strong> audit, board and shareholder meetings, company law filings, the FLA return by 15 July, income-tax return and transfer-pricing report. See the " + L("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "annual compliance calendar") + ".")
         + '<p>Related: ' + L("india-market-entry-foreign-company-guide.html", "India market entry playbook") + ' &middot; ' + L("foreign-company-india-advisor-market-research-entity-due-diligence-m-and-a-joint-venture-2026.html", "advisor for foreign companies") + ' &middot; ' + L("gcc-global-capability-centre-india-setup-us-company-safe-harbour-2026.html", "capability centres") + ' &middot; ' + L("india-free-trade-agreements-2026-uk-eu-efta-uae-oman-australia-new-zealand-foreign-companies.html", "trade agreements") + ' &middot; ' + L("does-foreign-company-need-to-file-income-tax-return-in-india-royalty-fees-dividend-capital-gains-itr-6-2026.html", "does the parent file an Indian return?") + ' &middot; ' + L("close-company-in-india-strike-off-stk-2-procedure-restore-foreign-subsidiary-2026.html", "closing a subsidiary") + '.</p>'
         + sources("Companies Act, 2013 (section 149(3) on resident directors); Foreign Exchange Management (Non-debt Instruments) Rules, 2019 and the consolidated FDI policy including Press Note 3 (2020); RBI directions on reporting (FC-GPR, FLA) and on offices of foreign entities; Income-tax Act, 2025 and the Income Tax Department withholding-rate table; Finance Act, 2025 (equalisation levy); DPDP Rules, 2025; Taxation and Other Laws (Amendment) Act, 2026. Each figure is sourced in detail on the linked page. Checked 22 November 2026.")),
    ],
    faqs=[("Can a foreign company own 100% of an Indian company?", "Yes, in most sectors under the automatic route without prior approval. Investors from countries sharing a land border with India, and some capped or regulated sectors, need government approval first; under Press Note 2 of 2026, an investor whose land-border beneficial ownership is within 10% and non-controlling can use the automatic route."),
          ("What is the best way for a foreign company to start doing business in India?", "For selling, hiring or building a team, usually a wholly owned private limited company. An employer of record suits a few early hires, and a liaison office suits representation without income."),
        ("How long does it take for a foreign company to set up a company in India?", "Incorporation through the MCA's SPICe+ form usually takes a few weeks once documents are ready. The usual delays are apostilled or consularised parent documents, digital signatures and DINs for directors, the resident director, and the bank account; the FC-GPR filing with the RBI follows within 30 days of issuing shares to the parent."),
        ("Does a foreign company need a local partner in India?", "No, in most sectors. 100% foreign ownership is allowed under the automatic route without a local partner; a few sectors have caps or need government approval, and investors linked to countries sharing a land border with India need approval unless the stake is within 10% and non-controlling (Press Note 2 of 2026)."),
        ("Does a foreign company need GST registration to sell to Indian customers?", "It depends on what it sells and to whom. A foreign supplier of online services to Indian consumers must register for GST under the OIDAR rules; services sold to Indian businesses are usually taxed under reverse charge by the Indian buyer; goods are taxed at import. A subsidiary selling in India registers like any Indian company."),
          ("What is the corporate tax rate in India for a foreign company?", "An Indian subsidiary under the 22% regime pays about 25.17% including surcharge and cess. A branch of a foreign company pays 35% plus surcharge and cess."),
          ("Does an Indian subsidiary need an Indian director?", "It needs at least one director who stayed in India for 182 days or more in the previous calendar year. A private company needs at least two directors in total."),
          ("What filings does a foreign-owned Indian company make every year?", "Statutory audit, company law annual filings, an income-tax return, a transfer-pricing report and master file where applicable, GST returns if registered, and the FLA return to the RBI by 15 July."),
          ("How does a foreign parent take money out of India?", "Through dividends, royalties and service fees, or a share buy-back or capital reduction. Each carries Indian tax, usually reduced by a tax treaty, and needs Forms 145 and 146 for the bank."),
          ("Has India introduced the global minimum tax or a digital services tax?", "No. India has not enacted Pillar Two, and it abolished the equalisation levy: the 2% levy ended on 1 August 2024 and the 6% levy on 1 April 2025."),
          ("Can BQP help a foreign company set up and run in India?", "Yes. " + C)],
    related=[("india-entry-structure-chooser-subsidiary-llp-branch-liaison-eor-foreign-company-2026.html", "Entry structure chooser"),
             ("foreign-owned-indian-subsidiary-annual-compliance-calendar-fy-2026-27.html", "Annual compliance calendar"),
             ("india-market-entry-foreign-company-guide.html", "India market entry playbook")],
    cta_h="Planning India for your company?", cta_b=C,
    keywords="doing business in India 2026, doing business in India guide, how to start a business in India as a foreigner, setting up wholly owned subsidiary in India, India FDI policy 2026, corporate tax rate India foreign company, India subsidiary resident director, foreign company India compliance, repatriate profits India",
    desc="Doing business in India 2026 for foreign companies: wholly owned subsidiary as the usual vehicle, 100% FDI automatic in most sectors, about 25% tax (branch 35%), treaty withholding on dividends, resident director, FC-GPR and FLA, no equalisation levy or Pillar Two, and how to take money out.",
    howto={"name": "How a foreign company starts doing business in India", "description": "Main steps.", "steps": [
        {"name": "Choose the structure", "text": "Subsidiary, liaison or branch office, employer of record or joint venture."},
        {"name": "Check the FDI route", "text": "Automatic in most sectors; government approval for land-border countries and capped sectors."},
        {"name": "Incorporate and bank", "text": "Resident director, registered office, share capital through banking channels."},
        {"name": "Report the investment", "text": "Form FC-GPR within 30 days of issuing shares."},
        {"name": "Run the annual cycle", "text": "Audit, tax return, transfer pricing, company law filings and the FLA return by 15 July."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FL complete")
