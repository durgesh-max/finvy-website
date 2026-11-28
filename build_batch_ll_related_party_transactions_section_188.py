# -*- coding: utf-8 -*-
"""Batch LL (28 Nov 2026): Related party transactions under section 188 of the Companies Act - who is a related party, which
transactions are covered, board and shareholder approval, the ordinary-course-and-arm's-length exemption, the wholly owned
subsidiary relief, AOC-2, the MBP-4 register, and the tax side (transfer pricing and section 40A(2)(b)).
Demand: 'related party transactions section 188', 'aoc-2 disclosure', 'related party transaction approval private company', 'arm's
length related party india' - mentioned on IPO / PE / secretarial pages but no dedicated page. Foreign-owned subsidiaries pay their
parents for services, royalties and goods - core audience. User steer 26 Nov / 19 Nov 2026: more call bookings.
Facts (Companies Act, 2013 sections 2(76), 177, 188 and 189; Companies (Meetings of Board and its Powers) Rules, 2014 rule 15;
Companies (Accounts) Rules rule 8(2)): related parties include directors, key managerial personnel and their relatives, firms and
private companies in which a director is a partner, member or director, and holding, subsidiary and associate companies and fellow
subsidiaries; section 188 covers sale, purchase or supply of goods or materials, buying or selling property, leasing, availing or
rendering services, appointing agents, appointment of a related party to an office or place of profit, and underwriting; such
contracts need the board's consent by resolution at a meeting, and prior shareholder approval by resolution where the rule 15
thresholds are crossed, with related parties not voting; transactions in the ordinary course of business and at arm's length are
outside section 188 approvals (companies with an audit committee still need its approval under section 177); shareholder approval is
not needed for transactions between a holding company and its wholly owned subsidiary whose accounts are consolidated and placed
before the shareholders; contracts are disclosed in the board's report in Form AOC-2 and entered in the MBP-4 register; a contract
entered without approval and not ratified within three months is voidable at the option of the board or shareholders. Tax: cross-
border related party transactions follow transfer pricing rules; payments to related domestic persons can be disallowed if
excessive (section 40A(2)(b)). No penalty amounts, no thresholds quoted, no fees. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "related-party-transactions-section-188-companies-act-approval-arms-length-aoc-2-wholly-owned-subsidiary-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the list of related parties, the contracts or "
     "planned transactions with them (goods, services, royalties, leases, loans, appointments), board and shareholder resolutions "
     "passed, and your last board report. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Related Party Transactions Under Section 188 (2026): Who Is a Related Party, Board and Shareholder Approval, the Arm's Length Exemption, AOC-2 and the Wholly Owned Subsidiary Relief",
    em="ordinary course and arm&rsquo;s length - or approvals.",
    kicker="/ Private companies, foreign-owned subsidiaries and promoters &middot; Companies Act section 188 &middot; Updated 2026-11-28",
    lead=("<strong>Contracts between a company and its directors, their relatives, group companies or the parent - for goods, services, property, leases, agents or appointments - fall under section 188 of the Companies Act. "
          "They need board approval, and shareholder approval above set limits, unless they are in the ordinary course of business and at arm&rsquo;s length. "
          "Every such contract is disclosed in Form AOC-2 in the board&rsquo;s report and entered in the MBP-4 register.</strong>"),
    sections=[
        ("/ The section 188 framework", "Who, what and which approval.",
         table(["Point", "Rule"], [
             ["Related parties", "Directors, KMP and their relatives; firms and private companies linked to a director; holding, subsidiary, associate and fellow subsidiary companies"],
             ["Transactions covered", "Goods or materials; buying or selling property; leasing; services; appointing agents; office or place of profit; underwriting"],
             ["Board approval", "Resolution at a board meeting; interested directors do not participate"],
             ["Shareholder approval", "Prior resolution where rule 15 limits are crossed; related parties do not vote"],
             ["Exemption", "Ordinary course of business and arm&rsquo;s length - no section 188 approvals (audit committee approval still applies where a company has one)"],
             ["Wholly owned subsidiary", "No shareholder approval for holding-WOS transactions where accounts are consolidated and placed before shareholders"],
             ["Disclosure", "Form AOC-2 in the board&rsquo;s report; MBP-4 register"],
             ["No approval", "Voidable at the board&rsquo;s or shareholders&rsquo; option if not ratified within three months; penalties on directors"]])
         + ul("<strong>Document arm&rsquo;s length:</strong> benchmarking, comparable quotes or pricing policies support the exemption - an assertion alone is weak.",
              "<strong>Loans and guarantees:</strong> loans to directors and group companies are governed by sections 185 and 186, not section 188.")),
        ("/ Foreign-owned subsidiaries and the tax side", "Where the parent is the counterparty.",
         ul("<strong>Typical contracts:</strong> service fees to the parent, royalties, cost allocations, purchase of goods, secondment of staff and IT charges.",
            "<strong>Approvals:</strong> board approval, or a documented ordinary-course and arm&rsquo;s-length basis; AOC-2 disclosure every year.",
            "<strong>Transfer pricing:</strong> cross-border related party transactions must be at arm&rsquo;s length under the Income-tax Act, with documentation and the accountant&rsquo;s report.",
            "<strong>Domestic related payments:</strong> excessive payments to related domestic persons can be disallowed under section 40A(2)(b).",
            "<strong>FEMA:</strong> remittances for royalty, fees and imports follow the current account and import rules.")
         + call_box("related party transactions", ["Mapping related parties",
                                                   "Arm&rsquo;s length and ordinary-course documentation",
                                                   "Board and shareholder resolutions",
                                                   "AOC-2 and MBP-4",
                                                   "Transfer pricing and 40A(2)(b) alignment"],
                    "Related parties, contracts, resolutions, last board report.")
         + sources("Companies Act, 2013 (sections 2(76), 177, 185, 186, 188 and 189); Companies (Meetings of Board and its Powers) Rules, 2014 (rule 15); Companies (Accounts) Rules, 2014 (rule 8(2), Form AOC-2); Income-tax Act transfer pricing provisions and section 40A(2)(b), with the corresponding provisions of the Income-tax Act, 2025; site transfer pricing and company secretarial pages.")),
    ],
    faqs=[("What is a related party transaction under section 188?", "A contract between a company and a related party - such as a director, key managerial person, their relative, a linked firm or private company, or a holding, subsidiary or associate company - for goods, property, leasing, services, agents, an office of profit or underwriting."),
          ("Does every related party transaction need shareholder approval?", "No. Board approval is needed, and prior shareholder approval only where the limits in rule 15 are crossed. Transactions in the ordinary course of business and at arm's length are outside section 188 approvals."),
          ("Is shareholder approval needed for transactions with a wholly owned subsidiary?", "No shareholder approval is required for transactions between a holding company and its wholly owned subsidiary whose accounts are consolidated and placed before the shareholders for approval."),
          ("What is Form AOC-2?", "The format for disclosing related party contracts in the board's report, covering contracts that are not at arm's length and material contracts at arm's length, with their terms and approvals."),
          ("What happens if section 188 approval is not taken?", "The contract is voidable at the option of the board or shareholders if not ratified within three months, and directors who authorised it face penalties."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your related parties, the contracts with them, resolutions passed and your last board report. Or book a call directly.")],
    related=[("best-ca-transfer-pricing-form-3ceb-india.html", "Transfer pricing and Form 3CEB"),
             ("company-secretarial-services-india-remote.html", "Company secretarial services"),
             ("significant-beneficial-owner-sbo-india-section-90-ben-1-ben-2-ben-4-foreign-parent-subsidiary-2026.html", "Significant beneficial owner (BEN-1 / BEN-2)"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar")],
    cta_h="Contracts with your parent, directors or group companies?", cta_b=C,
    keywords="related party transactions section 188, aoc-2 disclosure, related party transaction approval private company, arm's length related party india, section 188 wholly owned subsidiary exemption, mbp-4 register",
    desc="Related party transactions under section 188: who is a related party, covered contracts, board approval, shareholder approval above rule 15 limits, the ordinary-course and arm's-length exemption, wholly owned subsidiary relief, AOC-2, MBP-4, and transfer pricing and 40A(2)(b).",
    howto={"name": "How to handle related party transactions", "description": "Identify, document, approve, disclose.", "steps": [
        {"name": "Map related parties", "text": "Directors, KMP, relatives, linked entities and group companies."},
        {"name": "Test each contract", "text": "Ordinary course and arm's length, with documentation."},
        {"name": "Approve where needed", "text": "Board resolution; shareholder resolution above rule 15 limits."},
        {"name": "Disclose", "text": "AOC-2 in the board's report; MBP-4 register; align transfer pricing."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LL complete")
