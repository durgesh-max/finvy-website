# -*- coding: utf-8 -*-
"""Batch FO (23 Nov 2026): Converting an LLP into a private limited company - tax-free conditions, the 5-year 50% voting
test, losses, and the company-law route. Call-first page for founders raising equity.
Demand: sweep 22 Nov 2026 (ac44, founders), all 7 markets: "conversion of llp to private limited income tax",
"convert llp to private limited". Site had one 'best CA' page on LLP conversions.
Facts (checked 23 Nov 2026):
- 1961 Act: an LLP is a 'firm' (section 2(23)); section 47(xiii) treats the transfer of assets on succession of a firm
  by a company as not a transfer if (i) all assets and liabilities of the firm become the company's, (ii) all partners
  become shareholders in the proportion of their capital accounts on the date of succession, (iii) partners receive no
  consideration other than shares, and (iv) partners together hold at least 50% of voting power for five years;
  section 47A(3) taxes the company on breach; section 72A(6) carries forward the firm's losses and unabsorbed
  depreciation. Section 47(xiiib) is the reverse (company to LLP) route.
- 2025 Act (from 1 April 2026), per IncorpX analysis updated 29 Oct 2026 and TaxGuru / Treelife commentary:
  section 2(45) firm includes LLP; section 70(1)(zd) replaces 47(xiii); section 71(2) the clawback; section 116(8)-(9)
  losses. No clause names LLP-to-company expressly; the position rests on the definition of firm.
- Companies Act, 2013, section 366 and Part I of Chapter XXI with the Companies (Authorised to Register) Rules, 2014:
  partner consents, creditor consents, newspaper notice in Form URC-2 inviting objections within 21 days, SPICe+ with
  Form URC-1; LLP with fewer than seven partners registers as a private company."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 23 November 2026."
SLUG = "convert-llp-to-private-limited-company-india-tax-free-conditions-section-47-xiii-capital-gains-losses-2026"

C = contact("the LLP's partners and their capital account balances, main assets (property, investments, goodwill), any carried-forward losses, and why you want to convert (investor, ESOPs, foreign investment)")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Converting an LLP Into a Private Limited Company (2026): When It Is Tax-Free, the 5-Year 50% Voting Rule, Losses and the Process",
    em="usually done for investors; the tax test runs for five years.",
    kicker="/ Startups &middot; LLP &middot; Tax &middot; Updated 2026-11-23",
    lead=("<strong>An LLP can convert into a private limited company without capital gains tax if four conditions are met.</strong> "
          "All the LLP&rsquo;s assets and liabilities must pass to the company. Every partner must become a shareholder, in proportion to their <strong>capital account</strong> on the date of conversion. "
          "The partners must get <strong>nothing but shares</strong>. And the former partners must keep <strong>at least 50% of the voting power for five years</strong>. "
          "Break any of these, even in year three when an investor comes in, and the gain that was not taxed becomes the company&rsquo;s income. "
          "The relief was section 47(xiii) of the 1961 Act and is section 70(1)(zd) of the Income-tax Act, 2025. It works for LLPs because tax law treats an LLP as a firm, but no clause names LLPs expressly, so document the position. "
          "Most founders convert because investors and ESOPs need a company."),
    sections=[
        ("/ The four conditions", "All must hold.",
         table(["Condition", "What it means for an LLP", "When it is tested"], [
             ["All assets and liabilities move to the company", "No property, brand, loan or bank balance left behind with the LLP or a partner", "On conversion"],
             ["Every partner becomes a shareholder, in proportion to capital accounts", "Capital account balances on the conversion date set the ratio, not the profit-sharing ratio", "On conversion"],
             ["No consideration other than shares", "No cash payout of capital, current accounts or partner loans", "On conversion"],
             ["Former partners keep at least 50% of the votes", "Count every share issue, ESOP exercise and transfer that carries votes", "For five years"]])
         + '<p>If a condition fails later, the capital gain that was not taxed on conversion is taxed in the company&rsquo;s hands in the year of the breach, and losses already set off can be taxed back.</p>'
         + call_box("Converting our LLP before a funding round", ["Whether your LLP meets each condition today",
                                                                  "Realigning capital accounts before the conversion date",
                                                                  "Planning the round so the 50% voting test survives five years",
                                                                  "Carrying forward the LLP&rsquo;s losses",
                                                                  "Company law filings, GST and bank changes"],
                    "partners and capital balances, main assets, any losses, and the reason for converting.")),
        ("/ Why founders convert", "And what to watch.",
         ul("<strong>Investors:</strong> venture investors need shares, preference shares and convertible instruments that an LLP cannot issue.",
            "<strong>ESOPs:</strong> an LLP cannot grant employee stock options; a company can. See " + L("how-to-issue-esops-india.html", "issuing ESOPs") + ".",
            "<strong>Foreign investment:</strong> FDI in LLPs is allowed only in sectors open 100% under the automatic route without conditions; a company is simpler for most foreign investors.",
            "<strong>Startup tax holiday:</strong> LLPs can also qualify, but the holiday window runs from the original incorporation; see " + L("startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026.html", "startup tax holiday") + ".",
            "<strong>Investor dilution:</strong> if the round would take the former partners below 50% of the votes within five years, the tax-free treatment fails. Structure early rounds with that in mind.",
            "<strong>Tax rate after conversion:</strong> an LLP pays 30% plus surcharge and cess with no tax on profit share; a company pays about 25% under the 22% regime plus tax on dividends. Compare the two; see " + L("which-is-better-llp-vs-private-limited-india.html", "LLP or private limited") + ".")),
        ("/ The process", "Company law steps.",
         ul("<strong>1. Name:</strong> reserve the company name with the private limited suffix.",
            "<strong>2. Consents:</strong> a majority of partners and all secured creditors.",
            "<strong>3. Newspaper notice:</strong> Form URC-2 in an English and a local-language newspaper, inviting objections within 21 days.",
            "<strong>4. Accounts:</strong> a statement of assets and liabilities certified by the auditor, close to the filing date.",
            "<strong>5. Filing:</strong> the incorporation form with Form URC-1, the partner list with proposed shareholding, the LLP agreement and latest filings. An LLP with fewer than seven partners registers as a private company.",
            "<strong>6. After registration:</strong> the LLP&rsquo;s property vests in the company; update PAN, GST, bank, licences and contracts, and file the LLP&rsquo;s final return.")
         + '<p>Related: ' + L("best-ca-indian-llc-llp-conversion-india-2026.html", "LLP conversions") + ' &middot; ' + L("founder-salary-vs-dividend-india-private-limited-company-tax-director-remuneration-deemed-dividend-nri-founder-2026.html", "founder salary vs dividend after conversion") + ' &middot; ' + L("how-to-start-a-startup-in-india.html", "starting a startup in India") + '.</p>'
         + sources("Income-tax Act, 1961, sections 2(23), 47(xiii), 47A(3) and 72A(6); Income-tax Act, 2025, sections 2(45), 70(1)(zd), 71(2) and 116(8)-(9) as mapped in IncorpX&rsquo;s analysis (updated 29 October 2026) and commentary by TaxGuru and Treelife; Companies Act, 2013, section 366 and Part I of Chapter XXI; Companies (Authorised to Register) Rules, 2014. Checked 23 November 2026. Confirm the 2025 Act section numbers against the official text before filing.")),
    ],
    faqs=[("Is conversion of an LLP into a private limited company tax-free?", "Yes, if all assets and liabilities pass to the company, every partner becomes a shareholder in proportion to their capital account, partners receive only shares, and the former partners keep at least 50% of the voting power for five years. This was section 47(xiii) of the 1961 Act and is section 70(1)(zd) of the 2025 Act."),
          ("What happens if the 50% voting condition is broken after conversion?", "The capital gain not taxed on conversion is taxed as the company's income in the year of the breach, and losses already set off can be taxed back."),
          ("Can the LLP's losses be carried forward after conversion?", "Yes, if the conditions are met, the LLP's accumulated business loss and unabsorbed depreciation are treated as the company's, with the original carry-forward period continuing."),
          ("Does the share ratio follow the profit-sharing ratio?", "No. Shares must follow the partners' capital account balances on the conversion date. Realign capital accounts with proper entries before that date if needed."),
          ("How long does LLP to private limited conversion take?", "It includes a 21-day window for objections after the newspaper notice, then filing and registration, so plan for several weeks."),
          ("Why convert an LLP to a company before fundraising?", "Investors need shares and convertible instruments, employees need ESOPs, and foreign investment into LLPs is limited to certain sectors. A company handles all three."),
          ("Can BQP handle our LLP conversion?", "Yes. " + C)],
    related=[("which-is-better-llp-vs-private-limited-india.html", "LLP or private limited"),
             ("how-to-issue-esops-india.html", "Issuing ESOPs"),
             ("best-ca-indian-llc-llp-conversion-india-2026.html", "LLP conversions")],
    cta_h="Converting your LLP before a raise?", cta_b=C,
    keywords="convert LLP to private limited company, conversion of LLP to private limited income tax, LLP to company conversion tax free, section 47(xiii) LLP, section 70(1)(zd) Income-tax Act 2025, LLP to Pvt Ltd conversion process, URC-1 URC-2, LLP conversion 50% voting 5 years",
    desc="Converting an LLP into a private limited company (2026): tax-free if all assets move, partners get shares in proportion to capital accounts and nothing else, and keep 50% of votes for five years (section 47(xiii), now 70(1)(zd)). Clawback, losses and the URC-1/URC-2 process.",
    howto={"name": "How to convert an LLP into a private limited company", "description": "Tax-neutral route.", "steps": [
        {"name": "Check the four tax conditions", "text": "Assets, shareholding by capital accounts, shares only, 50% votes for five years."},
        {"name": "Realign capital accounts", "text": "With proper entries before the conversion date."},
        {"name": "Get consents and publish notice", "text": "Partners, secured creditors, Form URC-2 with 21 days for objections."},
        {"name": "File for registration", "text": "Incorporation form with Form URC-1 and certified accounts."},
        {"name": "Protect the five years", "text": "Plan funding and ESOPs so former partners keep 50% of votes."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FO complete")
