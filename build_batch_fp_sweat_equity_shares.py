# -*- coding: utf-8 -*-
"""Batch FP (23 Nov 2026): Sweat equity shares in India - rules, limits, valuation and tax (perquisite, startup deferral,
capital gains), and non-resident recipients. Call-first page for founders.
Demand: sweep 23 Nov 2026 (ac45, founders), all 7 markets, coverage 0.25-0.50: "sweat equity shares taxation", "taxation
of sweat equity shares in india", "income tax on sweat equity shares", "tax deferred on sweat equity shares", "tax
treatment of sweat equity shares", "what are sweat equity share", "sweat equity shares income tax act".
Facts (checked 23 Nov 2026):
- Companies Act, 2013, section 2(88) and section 54 with rule 8 of the Companies (Share Capital and Debentures) Rules,
  2014 (TaxGuru, Treelife, Mondaq, IncorpX summaries): issued to directors or employees at a discount or for
  consideration other than cash, for know-how, intellectual property or value additions; special resolution; valuation
  by a registered valuer; in a year up to 15% of paid-up capital or shares worth INR 5 crore, whichever is higher;
  total up to 25% of paid-up capital at any time, or 50% for a DPIIT-recognised startup up to 10 years from
  incorporation; lock-in of three years from allotment; allotment within 12 months of the resolution.
- Income tax: perquisite = fair market value on the date of allotment minus the amount paid (section 17(2)(vi) of the
  1961 Act, carried into the 2025 Act); employer deducts TDS; for an eligible startup (with the Inter-Ministerial Board
  certificate) tax on ESOPs and sweat equity can be deferred to within 14 days of the earliest of 48 months from the end
  of the relevant assessment year, sale, or leaving employment (site ESOP calculator page). On sale, cost = the fair
  market value taxed as perquisite.
- Non-resident recipients: reported to the RBI in Form ESOP (site LSF calculator lists Form ESOP among flow returns)."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "sweat-equity-shares-india-tax-rules-limits-valuation-startup-deferral-2026"

C = contact("the company's stage and DPIIT status, who would receive sweat equity (director, employee, adviser), what they contribute (work, know-how, IP), the number of shares, and whether the recipient lives in India")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Sweat Equity Shares in India (2026): Tax on Allotment, the Startup Deferral, Limits, Valuation and Lock-In",
    em="taxed when you get them, not only when you sell.",
    kicker="/ Startups &middot; Equity &middot; Tax &middot; Updated 2026-11-23",
    lead=("<strong>Sweat equity shares are shares a company gives its directors or employees at a discount, or for their know-how, intellectual property or work, instead of cash.</strong> "
          "They are <strong>taxed as salary when allotted</strong>: the fair market value on the allotment date, less anything the person paid, is a perquisite taxed at slab rates, and the company deducts tax. "
          "At an <strong>eligible startup</strong> holding the Inter-Ministerial Board certificate, that tax can be <strong>deferred</strong> until the earliest of 48 months after the end of the relevant assessment year, the sale of the shares, or leaving the company. "
          "Company law caps sweat equity at <strong>15% of paid-up capital (or INR 5 crore worth) a year</strong> and <strong>25% in total</strong>, or <strong>50% for a DPIIT startup</strong> in its first ten years, with a <strong>three-year lock-in</strong> and a registered valuer&rsquo;s report. "
          "When the shares are sold later, the value already taxed becomes the cost, so it is not taxed twice."),
    sections=[
        ("/ The rules", "Companies Act, section 54 and rule 8.",
         table(["Rule", "What applies"], [
             ["Who can receive", "Directors and employees of the company (and of its holding or subsidiary company), in India or outside"],
             ["What for", "Know-how, intellectual property rights or value additions, or simply at a discount"],
             ["Approval", "Special resolution of shareholders; allotment within 12 months of it"],
             ["Valuation", "Registered valuer&rsquo;s report on the shares and, where given for IP or know-how, on what is contributed"],
             ["Limit in a year", "15% of paid-up capital or shares worth INR 5 crore, whichever is higher"],
             ["Overall limit", "25% of paid-up capital at any time; 50% for a DPIIT-recognised startup up to 10 years from incorporation"],
             ["Lock-in", "Three years from allotment"]])
         + call_box("Planning sweat equity for a founder, director or key hire", ["Whether sweat equity or ESOPs suits the person and the company",
                                                                                 "Valuation, the special resolution and the allotment filings",
                                                                                 "Tax on allotment, and the startup deferral if you qualify",
                                                                                 "Sweat equity against IP: tax for the person contributing it",
                                                                                 "Recipients living abroad: RBI reporting and tax"],
                    "company stage and DPIIT status, the recipient and their role, what they contribute, the number of shares and where they live.")),
        ("/ How it is taxed", "Allotment, deferral, sale.",
         table(["Stage", "Tax"], [
             ["Allotment", "Fair market value on the allotment date minus the amount paid is a perquisite, taxed as salary at slab rates; the company deducts TDS"],
             ["Eligible startup", "Tax and TDS can be deferred until 14 days after the earliest of: 48 months from the end of the relevant assessment year, sale of the shares, or leaving the company"],
             ["Sale", "Capital gain = sale price minus the fair market value taxed at allotment; holding period runs from allotment"],
             ["Unlisted shares held over 24 months", "12.5% long-term capital gains plus surcharge and cess; shorter holding at slab rates"]])
         + ul("<strong>The cash problem:</strong> tax is due on shares that cannot be sold for three years. That is why the startup deferral matters; check that the company has the Inter-Ministerial Board certificate, not only DPIIT recognition. See " + L("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "the startup tax holiday and IMB certificate") + ".",
              "<strong>Sweat equity for IP:</strong> where a founder gives the company intellectual property in exchange for shares, the transfer of the IP can itself be taxable for the founder. Value and document it carefully.",
              "<strong>Fair market value:</strong> for unlisted shares, the value is set by a category I merchant banker under the income-tax rules, which can differ from the company-law valuation. Get both right.",
              "<strong>Non-resident recipients:</strong> issue to a person outside India is reported to the RBI in Form ESOP within 30 days; India taxes the perquisite to the extent it relates to work in India.")),
        ("/ Sweat equity or ESOPs?", "Which to use.",
         table(["", "Sweat equity", "ESOP"], [
             ["What the person gets", "Shares now", "An option to buy shares later"],
             ["Tax point", "On allotment", "On exercise"],
             ["Lock-in", "Three years by law", "Set by the scheme (vesting of at least one year)"],
             ["Founders and promoters", "Can receive it", "Promoters cannot receive ESOPs, except in startups within 10 years"],
             ["Best for", "A founder or director contributing IP or work before funding", "Employees, over time, with vesting"]])
         + '<p>Related: ' + L("how-to-issue-esops-india.html", "issuing ESOPs") + ' &middot; ' + L("esop-perquisite-tax-calculator.html", "ESOP tax calculator") + ' &middot; ' + L("esop-vs-rsu-vs-phantom-stock.html", "ESOP vs RSU vs phantom stock") + ' &middot; ' + L("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "founder salary vs dividend") + ' &middot; ' + L("fema-valuation-report-india-foreign-investment-fair-value-validity-90-days-2026.html", "valuation reports") + '.</p>'
         + sources("Companies Act, 2013, sections 2(88) and 54, and rule 8 of the Companies (Share Capital and Debentures) Rules, 2014, as summarised by TaxGuru, Treelife, Mondaq and IncorpX; Income-tax Act, 1961, section 17(2)(vi) and the startup deferral provisions, carried into the Income-tax Act, 2025; RBI reporting in Form ESOP. Checked 23 November 2026. Confirm the current rule 8 text and your company&rsquo;s DPIIT and IMB status before issuing.")),
    ],
    faqs=[("What are sweat equity shares?", "Shares a company issues to its directors or employees at a discount, or for consideration other than cash such as know-how, intellectual property or value additions, under section 54 of the Companies Act, 2013."),
          ("How are sweat equity shares taxed in India?", "On allotment, the fair market value of the shares on that date minus any amount paid is taxed as a salary perquisite at slab rates, with TDS by the company. On a later sale, the gain over that value is a capital gain."),
          ("Can tax on sweat equity be deferred?", "Yes, at an eligible startup holding the Inter-Ministerial Board certificate. Tax can be paid within 14 days of the earliest of 48 months from the end of the relevant assessment year, the sale of the shares, or leaving the company."),
          ("What is the limit on sweat equity shares?", "In a year, 15% of paid-up capital or shares worth INR 5 crore, whichever is higher. In total, 25% of paid-up capital, or 50% for a DPIIT-recognised startup in its first ten years."),
          ("Is there a lock-in on sweat equity shares?", "Yes, three years from the date of allotment."),
          ("Can a founder get sweat equity shares?", "Yes. Sweat equity can go to directors, including founder-directors, for their work, know-how or IP. ESOPs, by contrast, generally cannot be given to promoters except in startups within ten years of incorporation."),
          ("Can BQP structure sweat equity for our company?", "Yes. " + C)],
    related=[("how-to-issue-esops-india.html", "Issuing ESOPs"),
             ("esop-perquisite-tax-calculator.html", "ESOP tax calculator"),
             ("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "Startup tax holiday and IMB certificate")],
    cta_h="Giving sweat equity to a founder or key person?", cta_b=C,
    keywords="sweat equity shares taxation India, income tax on sweat equity shares, tax deferred sweat equity startup, what are sweat equity shares, sweat equity limit 15% 25% 50%, sweat equity lock in 3 years, sweat equity vs ESOP, sweat equity valuation registered valuer",
    desc="Sweat equity shares in India (2026): taxed as a perquisite on allotment (FMV minus amount paid), deferrable at eligible startups for up to 48 months; limits 15% or INR 5 crore a year, 25% total (50% for DPIIT startups), 3-year lock-in, registered valuer; capital gains on sale.",
    howto={"name": "How to issue sweat equity shares", "description": "Steps for a private company.", "steps": [
        {"name": "Check the limits", "text": "15% or INR 5 crore a year; 25% total, or 50% for a DPIIT startup."},
        {"name": "Get valuations", "text": "Registered valuer for company law; merchant banker FMV for income tax."},
        {"name": "Pass a special resolution", "text": "And allot within 12 months."},
        {"name": "Handle tax", "text": "TDS on the perquisite, or the startup deferral if eligible."},
        {"name": "File and report", "text": "Allotment filings; Form ESOP to the RBI for recipients outside India."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FP complete")
