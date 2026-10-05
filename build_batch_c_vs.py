# -*- coding: utf-8 -*-
"""Batch C: 5 vs-comparison pages."""
from build_lib import page, write_page

# 1. Delaware C-Corp vs Wyoming LLC
write_page("delaware-c-corp-vs-wyoming-llc", page(
    slug="delaware-c-corp-vs-wyoming-llc",
    title="Delaware C-Corp vs Wyoming LLC 2026 | Which to Choose - BQP",
    description="Delaware C-Corp vs Wyoming LLC for Indian founders. Franchise tax, privacy, VC-fundability, 83(b) elections, QSBS, annual compliance. CA-led comparison for 2026 incorporations.",
    keywords="Delaware C-Corp vs Wyoming LLC, Wyoming LLC Indian founder, Delaware vs Wyoming startup, VC fundable LLC vs C-Corp, Wyoming privacy LLC, Delaware franchise tax vs Wyoming",
    hero_kicker="/ US entity choice &middot; Delaware vs Wyoming",
    hero_title_html="Delaware C-Corp vs Wyoming LLC, <em>for an Indian founder.</em>",
    hero_lead="Two states dominate US entity formation for international founders: Delaware (the legal default for VC-backed C-Corps) and Wyoming (lower-cost, higher-privacy LLC default). The right choice depends almost entirely on whether US venture capital is in your plan.",
    sections=[
        ("/ The quick answer", "Delaware if VC-funded; Wyoming if not.",
         "<p>Short decision rule:</p>"
         "<ul>"
         "<li><strong>Raising from US venture capital in the next 12 months?</strong> Delaware C-Corp. Not optional &mdash; US VCs invest in Delaware C-Corps.</li>"
         "<li><strong>Bootstrapping, cash-flow business, no US VC on the horizon?</strong> Wyoming LLC. Lower franchise fees, better privacy, pass-through tax.</li>"
         "<li><strong>Unsure?</strong> Start with Wyoming LLC. The F-reorg to a Delaware C-Corp is a routine 30-60 day conversion if the VC path materialises.</li>"
         "</ul>"),
        ("/ Franchise tax &amp; annual cost", "Wyoming is materially cheaper.",
         "<p><strong>Delaware C-Corp annual costs:</strong></p>"
         "<ul>"
         "<li>Franchise tax: minimum USD 400 (assumed par value method), typical USD 400-1,000 for early-stage, can run USD 5,000+ for growth-stage with high authorised shares.</li>"
         "<li>Annual report: USD 50 filing fee.</li>"
         "<li>Registered agent: USD 100-300.</li>"
         "<li>Total year 1 steady state: typically USD 600-1,500.</li>"
         "</ul>"
         "<p><strong>Wyoming LLC annual costs:</strong></p>"
         "<ul>"
         "<li>Annual report: USD 60 (plus USD 0.0002 per asset dollar, capped low).</li>"
         "<li>Registered agent: USD 50-150.</li>"
         "<li>Total year 1 steady state: typically USD 150-250.</li>"
         "</ul>"
         "<p>Delta over 5 years: roughly USD 3,000-7,000 saved in Wyoming &mdash; meaningful for bootstrapped founders, immaterial for VC-track companies.</p>"),
        ("/ Privacy", "Wyoming hides owner names; Delaware does not for LLCs either, but C-Corps vary.",
         "<p>Wyoming LLCs do not require public disclosure of members or managers on the annual report. Owner names are kept private at the state registry level. The registered agent sees them, and KYC/AML processes at banks will see them, but public searches do not.</p>"
         "<p>Delaware LLCs similarly do not require public member disclosure. Delaware C-Corps also do not require public shareholder disclosure. State-level privacy is similar between the two.</p>"
         "<p>The privacy advantage of Wyoming over Delaware is marginal for LLC/LLC comparison. For C-Corp/LLC comparison, both are private at state level.</p>"
         "<p>BOIR / CTA (federal beneficial ownership reporting) status: currently exempt for domestic entities under the March 2025 FinCEN interim rule &mdash; same treatment for Delaware and Wyoming.</p>"),
        ("/ VC-fundability", "Delaware wins decisively.",
         "<p>US VCs invest in Delaware C-Corps. Reasons:</p>"
         "<ul>"
         "<li>Delaware corporate law is familiar, well-litigated, VC-friendly on preferred stock terms.</li>"
         "<li>Standard VC term sheets, voting agreements, drag-along, protective provisions, information rights all assume Delaware.</li>"
         "<li>Delaware Court of Chancery is the specialist corporate court &mdash; disputes resolve predictably.</li>"
         "<li>Delaware General Corporation Law supports common VC mechanics (board classes, preferred share series, protective provisions).</li>"
         "</ul>"
         "<p>Wyoming LLCs are not VC-fundable. US VCs will not invest into a Wyoming LLC &mdash; the LLC operating agreement is non-standard, member units do not translate to preferred stock, Section 1202 QSBS does not apply (LLC is not a C-Corp), 83(b) elections do not fit LLC profits-interests cleanly.</p>"
         "<p>If VC is a possibility, start with Delaware C-Corp or plan the Wyoming-to-Delaware conversion before the term sheet.</p>"),
        ("/ Decision framework", "Three scenarios.",
         "<p><strong>Scenario 1: Bootstrapped SaaS, two Indian founders, Indian team, US customers via Stripe.</strong> No US VC planned. Choose Wyoming LLC. Pass-through to the Indian founders means no US entity-level tax. Form 5472 obligation attaches (annual filing). Lowest ongoing cost.</p>"
         "<p><strong>Scenario 2: AI startup planning to raise USD 2M seed from a US VC in 6 months.</strong> Choose Delaware C-Corp from day one. 83(b) elections for founders on day of incorporation. QSBS 5-year clock starts immediately. VC term sheet drops into standard Delaware structure.</p>"
         "<p><strong>Scenario 3: Not sure &mdash; maybe VC, maybe not.</strong> Start Wyoming LLC. If VC term sheet materialises, convert to Delaware C-Corp via F-reorg (30-60 days, tax-free). Lose: the time between Wyoming formation and C-Corp conversion does not count for QSBS 5-year holding. For most founders this is acceptable.</p>"),
    ],
    faqs=[
        ("Which state has lower incorporation cost: Delaware or Wyoming?",
         "Wyoming. Formation fee: Wyoming USD 100, Delaware USD 90-200 depending on entity type. Annual compliance: Wyoming USD 150-250, Delaware USD 600-1,500. Over 5 years, Wyoming saves USD 3,000-7,000 for a standard early-stage entity."),
        ("Can I convert from Wyoming LLC to Delaware C-Corp later?",
         "Yes. Delaware allows direct statutory conversion of an out-of-state LLC into a Delaware C-Corp. Done as an F-reorg (IRC Section 368(a)(1)(F)) the conversion is tax-free in the standard founder scenario. Timing: 30-60 days. If VC raise is likely, convert before the term sheet."),
        ("Does Form 5472 apply to Wyoming LLCs?",
         "Yes. Form 5472 applies to any 25%+ foreign-owned US entity with reportable transactions &mdash; Delaware, Wyoming, or any US state. For a Wyoming single-member LLC owned by an Indian individual, the annual pro forma 1120 + Form 5472 filing applies the same as a Delaware LLC."),
        ("Can an Indian founder be a Wyoming LLC member without a US SSN?",
         "Yes. Wyoming does not require US SSN for LLC members or managers. The LLC obtains an EIN via Form SS-4 (fax or international phone, 4-8 weeks). The Indian individual files their own US obligations via ITIN or passport-based identification. Same mechanics as Delaware."),
        ("Does QSBS (Section 1202) apply to a Wyoming LLC?",
         "No. QSBS applies to C-Corporation stock only. A Wyoming LLC member interest is not C-Corp stock, so QSBS does not apply. If QSBS eligibility matters, incorporate as a Delaware C-Corp from day one &mdash; the 5-year holding period starts from the C-Corp formation date. An LLC-to-C-Corp conversion resets the QSBS clock to the conversion date, not the LLC formation date."),
        ("Does BQP incorporate in both Delaware and Wyoming?",
         "Yes. We handle both. Scoping typically starts with your 12-month funding plan &mdash; if US VC is on the horizon, Delaware C-Corp from day one. If not, Wyoming LLC with built-in conversion documentation if the plan changes. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("convert-llc-to-c-corp-f-reorganization.html", "Guide", "LLC to C-Corp conversion"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Delaware or Wyoming &mdash; we scope it right the first time.",
    cta_body="The right entity for your situation depends on your 12-month funding plan, your US revenue profile, and whether you plan to live in the US eventually. We scope all three, recommend, and incorporate. Standard setup includes EIN, bank account introduction, Form 5472 planning, and 83(b) elections where applicable.",
))

# 2. C-Corp vs S-Corp
write_page("us-c-corp-vs-s-corp-indian-founder", page(
    slug="us-c-corp-vs-s-corp-indian-founder",
    title="C-Corp vs S-Corp for Indian Founder 2026 | Why S-Corp Won't Work - BQP",
    description="C-Corp vs S-Corp election analysis for Indian founders. Why S-Corp is unavailable for non-US-citizen owners, S-Corp vs C-Corp tax comparison, pass-through LLC as the S-Corp alternative for Indians.",
    keywords="C-Corp vs S-Corp India, S-Corp Indian founder, S-Corp non-US citizen, S-Corp election ineligible, C-Corp double taxation India, pass-through LLC vs S-Corp",
    hero_kicker="/ US entity choice &middot; C-Corp vs S-Corp",
    hero_title_html="C-Corp vs S-Corp, <em>for an Indian founder.</em>",
    hero_lead="S-Corp election is a US small-business tax regime that eliminates C-Corp double taxation by taxing profits at the shareholder level only. For American founders it is often the first-choice structure. For Indian founders it is unavailable &mdash; non-US-citizen owners disqualify the election. Here is the detail and the LLC-as-alternative that most Indian founders end up using.",
    sections=[
        ("/ What S-Corp election is", "A pass-through tax regime for small US corporations.",
         "<p>A US corporation (formed as a C-Corp under state law) can elect S-Corporation status under IRC Subchapter S by filing Form 2553. The election flips the entity's federal tax treatment from double taxation (corporate 21% + shareholder dividend tax) to pass-through taxation (profits flow to shareholders and are taxed once at their rates).</p>"
         "<p>Eligibility requirements:</p>"
         "<ul>"
         "<li>Domestic US corporation.</li>"
         "<li>No more than 100 shareholders.</li>"
         "<li>All shareholders must be individuals, certain trusts, or certain estates &mdash; no corporations, no partnerships.</li>"
         "<li><strong>All shareholders must be US citizens or US tax residents.</strong></li>"
         "<li>Only one class of stock (voting differences allowed; economic differences not).</li>"
         "</ul>"
         "<p>Election mechanics: Form 2553 filed within 2 months and 15 days of the start of the tax year in which the election is to take effect, signed by all shareholders.</p>"),
        ("/ Why Indian founders cannot elect S-Corp", "The non-US-citizen rule.",
         "<p>An Indian individual who is not a US tax resident (not a green-card holder, not meeting the 183-day substantial-presence test) cannot be an S-Corp shareholder. The election is simply unavailable where any shareholder fails the US-citizen-or-resident test.</p>"
         "<p>Practical implications for Indian founders:</p>"
         "<ul>"
         "<li>You cannot elect S-Corp status for a Delaware C-Corp if you (the Indian individual founder) are a shareholder and not a US tax resident.</li>"
         "<li>Your Delaware C-Corp defaults to C-Corp tax treatment: 21% federal corporate tax on profits + 30% US withholding (reduced to 15% / 25% under India-US DTAA) on dividends paid to you.</li>"
         "<li>If you later become a US tax resident (H-1B, L-1, green card for 183+ days in a tax year), S-Corp election becomes available &mdash; but only prospectively, with Form 2553 filed in that year.</li>"
         "</ul>"),
        ("/ Pass-through LLC: the Indian founder alternative", "What S-Corp would have done, delivered via LLC.",
         "<p>For an Indian founder wanting pass-through tax treatment on their US entity, the LLC structure delivers what S-Corp would have delivered:</p>"
         "<ul>"
         "<li>A single-member LLC is a disregarded entity for US federal tax by default &mdash; profits flow through to the single member (the Indian individual) with no entity-level US tax, unless the profits are US-source Effectively Connected Income (ECI).</li>"
         "<li>A multi-member LLC is a partnership for US federal tax by default &mdash; profits are reported to each member on a Schedule K-1 and taxed at the member level.</li>"
         "<li>No shareholder-eligibility restrictions &mdash; Indian citizens, Indian companies, trusts, and other non-US persons can be LLC members.</li>"
         "<li>No one-class-of-stock restriction &mdash; LLC operating agreements can allocate profits, losses, and distributions in any economically-reasonable manner.</li>"
         "</ul>"
         "<p>Trade-off: LLCs are not VC-fundable. If you need US venture capital, the LLC must convert to a C-Corp (F-reorg) first.</p>"),
        ("/ Tax comparison illustration", "A worked example.",
         "<p>Scenario: Indian founder owns 100% of a US entity with USD 500,000 of pre-tax profit. All operations in India, but entity classified as C-Corp with the profit coming from US customers.</p>"
         "<p><strong>Case 1: Delaware C-Corp (default).</strong></p>"
         "<ul>"
         "<li>US federal corporate tax: USD 500,000 &times; 21% = USD 105,000.</li>"
         "<li>Delaware franchise tax: USD 400 (assume minimum).</li>"
         "<li>After-tax at entity: USD 394,600.</li>"
         "<li>Dividend to Indian founder: USD 394,600 &times; (1 - 25% treaty withholding) = USD 295,950 net to India.</li>"
         "<li>Indian founder reports dividend income in India; claims foreign tax credit; net Indian tax varies.</li>"
         "</ul>"
         "<p><strong>Case 2: Wyoming or Delaware single-member LLC (pass-through disregarded).</strong></p>"
         "<ul>"
         "<li>US federal tax on US-source ECI, if any (varies by activity).</li>"
         "<li>No entity-level tax if no US-source ECI.</li>"
         "<li>Profits flow to the Indian founder and are taxed in India at Indian rates.</li>"
         "<li>No US dividend withholding (not a dividend; LLC distribution to member).</li>"
         "</ul>"
         "<p>The LLC path is materially better if the activity does not generate US-source ECI. The C-Corp path is often required for operational reasons (VC-fundability, US employee hiring, US customer contracts). Model both before deciding.</p>"),
    ],
    faqs=[
        ("Can I elect S-Corp status for my Delaware C-Corp as an Indian founder?",
         "No. S-Corp election under IRC Subchapter S requires all shareholders to be US citizens or US tax residents. An Indian individual who is not a US tax resident is an ineligible shareholder, and the presence of even one ineligible shareholder disqualifies the entire election."),
        ("What is the Indian equivalent of S-Corp tax treatment?",
         "A US LLC (single-member or multi-member) delivers pass-through tax treatment similar to what S-Corp provides &mdash; without the shareholder-eligibility restrictions. For a non-US-resident Indian individual, the LLC's single-member disregarded-entity status is the standard choice if VC-fundability is not required."),
        ("If I become a US tax resident later, can I elect S-Corp then?",
         "Yes, prospectively. If the Indian founder becomes a US tax resident (H-1B, L-1, green card, or substantial presence 183+ days) in a given year, S-Corp election can be filed on Form 2553 within 2 months and 15 days of the start of that year. The election applies from the year of filing forward; it does not retroactively treat prior years."),
        ("Does an Indian company owning a US C-Corp disqualify S-Corp?",
         "Yes, independently of the citizenship issue. S-Corp shareholders must be individuals (or certain trusts); corporations and partnerships are ineligible. An Indian company holding US C-Corp shares disqualifies S-Corp election even if the ultimate human owner is a US citizen."),
        ("What is the double-taxation cost of C-Corp vs pass-through?",
         "C-Corp: 21% federal corporate tax at entity + 15% / 25% treaty withholding on dividend to Indian shareholder = ~33-40% total US tax burden on distributed profits. Pass-through LLC: 0% US entity tax if no US-source ECI, plus the Indian founder's Indian tax on profits in India. The LLC saves materially where the activity does not generate US-source ECI."),
        ("Does BQP structure Indian-founder US entities?",
         "Yes. Scoping covers: VC-fundability requirement, US-source ECI analysis (US employees, US customers, US property), expected profit profile, and founder's own tax residence. We recommend LLC or C-Corp accordingly and handle incorporation + ongoing compliance. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("delaware-c-corp-vs-wyoming-llc.html", "Guide", "Delaware vs Wyoming"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="C-Corp vs LLC choice is the first big tax decision.",
    cta_body="For an Indian founder, S-Corp is off the table. The real choice is C-Corp (VC-fundable, double-taxed) vs LLC (pass-through, no US VC). We scope both against your 12-month plan and set up the right structure.",
))

# 3. Mercury vs Brex
write_page("mercury-vs-brex-indian-founder", page(
    slug="mercury-vs-brex-indian-founder",
    title="Mercury vs Brex for Indian Founder 2026 | Which US Bank Account - BQP",
    description="Mercury vs Brex account opening for Indian-founder Delaware entities. KYC acceptance, FDIC coverage, international wires, fees, treasury yield. Working comparison for 2026 incorporations.",
    keywords="Mercury vs Brex India, Mercury Indian founder, Brex Indian founder, US business bank account India, Mercury Delaware LLC, Brex Delaware C-Corp, Mercury Treasury yield",
    hero_kicker="/ US banking &middot; Mercury vs Brex",
    hero_title_html="Mercury vs Brex, <em>for an Indian-founder US entity.</em>",
    hero_lead="Two fintech banking platforms dominate account opening for Indian-founder Delaware entities: Mercury (full business banking, Treasury yield) and Brex (business banking plus corporate cards and spend management). Both accept Indian-founder entities without US SSN. The right choice depends on your spending profile and whether you need corporate cards from day one.",
    sections=[
        ("/ What both get right", "The baseline for an Indian founder.",
         "<p>Both Mercury and Brex solve the hardest problem for an Indian founder: opening a US business bank account without a US SSN, without physically visiting the US, and without a credit history. Both accept:</p>"
         "<ul>"
         "<li>Delaware or Wyoming LLC / C-Corp.</li>"
         "<li>Non-US-resident foreign founder as a 100% owner.</li>"
         "<li>Passport (plus national ID in some cases) as primary identification.</li>"
         "<li>Fully-remote onboarding.</li>"
         "<li>EIN-based tax identification for the entity.</li>"
         "</ul>"
         "<p>Both route deposits through FDIC-insured partner banks (not themselves direct banks). Both offer wire transfers, ACH, international wires. Both have modern APIs and web dashboards built for software-founder workflow.</p>"),
        ("/ Where they differ", "Spend management vs treasury yield.",
         "<p><strong>Mercury strengths:</strong></p>"
         "<ul>"
         "<li>Mercury Treasury: idle balance over USD 500K earns Treasury-fund yield (4-5% range depending on Fed rate).</li>"
         "<li>IO (deposits insured sweep) extends FDIC coverage to USD 5M+ through sweep partners.</li>"
         "<li>Simple multi-currency setup for incoming payments.</li>"
         "<li>Open to earlier-stage, smaller-balance entities &mdash; low minimums.</li>"
         "<li>Developer-friendly API if you want to automate payouts or reconciliation.</li>"
         "</ul>"
         "<p><strong>Brex strengths:</strong></p>"
         "<ul>"
         "<li>Corporate cards from day one &mdash; underwritten against entity cash balance, no personal guarantee.</li>"
         "<li>Spend management: receipt capture, policy enforcement, auto-categorisation, expense reporting.</li>"
         "<li>Travel booking and reimbursement integrated.</li>"
         "<li>Better fit for a team of 5+ with recurring expenses.</li>"
         "<li>Historically has had higher balance thresholds to maintain full feature access; this has eased recently.</li>"
         "</ul>"
         "<p><strong>Where Brex is weaker:</strong> Brex has periodically closed accounts of very-small-balance or earliest-stage founders to focus on larger customers. Mercury is more consistently open to pre-revenue founders.</p>"),
        ("/ Decision framework", "Match to your situation.",
         "<p><strong>Scenario 1: Pre-revenue founder, LLC just incorporated, USD 10K seed capital.</strong> Mercury. Easier approval, no card-approval friction (which Brex can gate), banking-only is sufficient at this stage.</p>"
         "<p><strong>Scenario 2: Seed-funded company, USD 1-5M in bank, hiring 5+ US contractors.</strong> Either works. Mercury for Treasury yield on idle balance; Brex for spend management across the team. Many founders use both &mdash; Mercury as primary deposit account, Brex for cards + spend management.</p>"
         "<p><strong>Scenario 3: Series A+, USD 5M+ balance, 20+ team members, international travel.</strong> Brex becomes the natural fit for spend management. Keep Mercury or Mercury Treasury as the deposit/yield account.</p>"),
        ("/ Common pitfalls", "What to avoid.",
         "<ul>"
         "<li><strong>Opening with incomplete entity documentation.</strong> Both platforms require Certificate of Incorporation / Formation + EIN + Operating Agreement / Bylaws + proof of address for the founder (utility bill, bank statement). Missing any element delays or blocks approval.</li>"
         "<li><strong>Mismatched addresses.</strong> Delaware registered address + Indian founder residential address + any US virtual mailbox address must be consistent across the application. Discrepancies trigger KYC review.</li>"
         "<li><strong>Early-stage founders applying to Brex before raising.</strong> Brex has intermittently declined pre-funded applicants. Start with Mercury; add Brex after first institutional round.</li>"
         "<li><strong>Wire limits.</strong> Both platforms have outgoing international wire limits that scale with account history. For a USD 500K-plus outbound wire in month 1, pre-coordinate with the bank or expect a review.</li>"
         "</ul>"),
    ],
    faqs=[
        ("Can an Indian founder open a Mercury account without visiting the US?",
         "Yes. Mercury supports fully-remote onboarding for non-US-resident founders of Delaware and Wyoming entities. Required documents: Certificate of Incorporation / Formation, EIN, Operating Agreement, founder passport, proof of founder address (utility bill or bank statement, 3 months old). Approval typically 2-5 business days."),
        ("Does Brex require revenue to open an account?",
         "Not strictly, but Brex has historically preferred funded or revenue-generating entities. Pre-revenue, pre-funded founders have been declined. If you are pre-funded, start with Mercury; add Brex after your first institutional round."),
        ("Is Mercury or Brex FDIC-insured?",
         "Both route deposits through FDIC-insured partner banks (Mercury: Choice Financial Group, Evolve Bank, and others; Brex: JPMorgan via Brex Treasury). Standard FDIC coverage is USD 250K per depositor per insured bank; both platforms extend coverage via sweep arrangements to multiple partner banks."),
        ("Can I earn yield on my Mercury balance?",
         "Yes, via Mercury Treasury (balances over USD 500K). Treasury yield tracks short-term US Treasury rates. Current yield is in the 4-5% range depending on Fed rate. Mercury Vault (smaller balances) has a separate yield product with lower minimum."),
        ("Do I need an ITIN to open Mercury or Brex?",
         "No. Both accept the entity's EIN as the primary tax identifier. The individual founder uses their passport for KYC; no ITIN is required at account opening. ITIN may be needed later for individual US tax filings (if the founder has US-source income) but is not a banking prerequisite."),
        ("Does BQP help with Mercury / Brex account opening?",
         "Yes, as part of the US incorporation package. Standard package includes entity formation + EIN + bank account introduction (Mercury or Brex as applicable). Not a bank intermediary &mdash; we prepare the application pack and coach the founder through the process. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("stripe-atlas-alternative-india.html", "Guide", "Stripe Atlas alternative"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="US bank account from India in 2 weeks.",
    cta_body="Mercury or Brex, matched to your stage. We prepare the application pack (entity docs + EIN + founder KYC + address proof), introduce you to the right platform, and coach you through approval. Standard timeline: 10-14 days from entity formation to funded bank account.",
))

# 4. SAFE vs Convertible Note
write_page("safe-vs-convertible-note-india-founder", page(
    slug="safe-vs-convertible-note-india-founder",
    title="SAFE vs Convertible Note 2026 | Which for Indian Founder - BQP",
    description="SAFE vs convertible note analysis for Indian founders raising from US angels and seed VCs. Valuation cap, discount, interest, maturity, Indian tax treatment on conversion. CA-led comparison.",
    keywords="SAFE vs convertible note, SAFE Indian founder, SAFE India tax, YC SAFE, convertible note India, SAFE conversion tax India, SAFE valuation cap, SAFE post-money",
    hero_kicker="/ Funding instruments &middot; SAFE vs Note",
    hero_title_html="SAFE vs convertible note, <em>for an India-origin founder.</em>",
    hero_lead="Both SAFEs and convertible notes are early-stage funding instruments that delay valuation negotiation to the next priced round. For Indian founders raising from US angels or seed VCs the choice shapes dilution math, Indian tax exposure at conversion, and compliance workload. Here is the comparison.",
    sections=[
        ("/ Baseline", "What each instrument is.",
         "<p><strong>Convertible note:</strong> A debt instrument. Investor lends money to the company; the note bears interest (typically 2-8%); on a qualified future financing round, the note converts to preferred stock at a discount or at a capped valuation. Maturity date typically 18-24 months &mdash; if no qualifying round happens by maturity, the note either repays or converts at a specified fallback.</p>"
         "<p><strong>SAFE (Simple Agreement for Future Equity):</strong> Not debt. Not equity until conversion. Developed by Y Combinator in 2013 as a founder-friendly alternative to notes. No interest, no maturity date. Converts to preferred stock on a qualified financing event (and sometimes on a dissolution or liquidity event) at a discount or capped valuation.</p>"),
        ("/ Head-to-head mechanics", "Where they differ.",
         "<p><strong>Interest:</strong> Note has it (compounding typically 5-8% annually; the compounded principal converts). SAFE has none. For a 24-month note at 6% compounding, the investor's principal converts at ~113% of original investment. SAFE converts at 100%.</p>"
         "<p><strong>Maturity:</strong> Note has one &mdash; if no priced round by maturity, repayment or forced conversion at a default price. SAFE has none &mdash; it can sit indefinitely. In practice almost all SAFEs convert in a priced round within 12-24 months regardless.</p>"
         "<p><strong>Debt character:</strong> Note is debt until conversion, which has downstream implications: it sits on the balance sheet as a liability, it can trigger insolvency tests, and in bankruptcy it ranks ahead of equity. SAFE is neither debt nor equity &mdash; sits in a 'future equity' line item.</p>"
         "<p><strong>Dilution math on conversion:</strong> Pre-money vs post-money SAFEs matter. The 2018 YC post-money SAFE converts <em>after</em> the new money is included in the base, which allocates more dilution to the founder than a pre-money SAFE at the same cap would. Model carefully.</p>"
         "<p><strong>Legal cost:</strong> SAFE is a 5-page standardised form (YC free). Convertible note is 10-15 pages, often with investor-specific redlines. SAFE closes faster and cheaper.</p>"),
        ("/ Indian tax treatment on conversion", "The founder-side consideration.",
         "<p>For an Indian-resident founder of a Delaware C-Corp (post-flip) raising via SAFE or note from US investors, the instrument's conversion to preferred stock is a transaction between the Delaware company and the US investor &mdash; the Indian founder is not a party and has no personal Indian tax trigger at that point.</p>"
         "<p>However, dilution effects on the founder's share count matter:</p>"
         "<ul>"
         "<li>At the next priced round, the SAFE / note converts into preferred stock, diluting the founder's percentage. This is a dilution event, not a taxable event for the founder.</li>"
         "<li>If the founder is also receiving fresh founder-equity grants or exercising stock options alongside the conversion, those grants/exercises are their own tax events.</li>"
         "</ul>"
         "<p>Where Indian tax actually attaches:</p>"
         "<ul>"
         "<li>If the SAFE / note is being issued by an Indian company (not Delaware), compulsorily convertible debentures (CCDs) are the Indian equivalent &mdash; FDI route, FEMA pricing guidelines apply, Form FC-GPR on issue, Form FC-TRS if transferred.</li>"
         "<li>SAFEs in Indian company structure are regulatorily problematic &mdash; FEMA has not clearly recognised the SAFE as a permitted instrument. CCDs or convertible preference shares are the standard Indian alternatives.</li>"
         "</ul>"),
        ("/ Decision framework", "Which for which situation.",
         "<p><strong>US angel or seed VC into Delaware C-Corp:</strong> SAFE is the standard default in 2026. YC post-money SAFE form, standard valuation cap, standard discount. Closes in days.</p>"
         "<p><strong>Non-institutional investor who insists on debt-flavored instrument:</strong> Convertible note. Interest 4-6%, maturity 18-24 months, discount 15-20%, cap at a defensible number.</p>"
         "<p><strong>Indian angel into Indian company:</strong> CCD (compulsorily convertible debenture) under FEMA. Not SAFE. If you need SAFE-style simplicity, flip to Delaware first.</p>"
         "<p><strong>Series A term-sheet imminent:</strong> If a priced Series A is 60-90 days away, raise the gap money as a SAFE &mdash; it converts cleanly into the Series A preferred. Avoid issuing new SAFEs at a cap close to the expected Series A valuation (minimal discount means minimal upside for the SAFE investor; investor may push for note instead).</p>"),
    ],
    faqs=[
        ("Is SAFE legal in India?",
         "SAFE is a US instrument; its direct use in Indian-company funding is not clearly recognised under FEMA. The Indian equivalents are CCDs (compulsorily convertible debentures) or compulsorily convertible preference shares, which have clear FEMA pricing and FDI treatment. For a Delaware C-Corp subsidiary (post-flip), SAFEs are freely usable."),
        ("Does SAFE have interest?",
         "No. SAFE has no interest, no maturity date. The investor converts the original principal into preferred stock at the discount or cap. Convertible notes have interest, typically 4-8% compounding."),
        ("What is pre-money vs post-money SAFE?",
         "Pre-money SAFE (YC original 2013): converts at a cap based on the pre-money valuation of the next priced round. Post-money SAFE (YC 2018 update): converts at a cap based on the post-money valuation including the new money. Post-money SAFEs allocate more dilution to the founder for the same cap. The YC 2018 post-money SAFE is the most-used form today."),
        ("Do SAFEs ever convert if there's no priced round?",
         "SAFEs typically convert on a qualified financing (next priced round), a liquidity event (acquisition or IPO), or a dissolution event. Without any of these, a SAFE can sit indefinitely. In practice almost all SAFEs convert within 24 months, usually at the Series A priced round."),
        ("What is a 'qualified financing' for SAFE conversion?",
         "Typically defined in the SAFE as a priced equity round above a specified threshold (commonly USD 1M+). The threshold prevents a tiny subsequent raise from triggering conversion at an unexpectedly low valuation. The YC standard SAFE form has specific language."),
        ("Does BQP structure SAFE / convertible note rounds for Indian founders?",
         "Yes, from both sides: for Indian-founder Delaware C-Corps issuing SAFEs to US angels (US-side legal co-ordination + cap table modelling + 83(b) considerations), and for Indian companies raising via CCD or CCPS under FEMA (Form FC-GPR, valuation certificate, pricing guidelines). Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("india-to-delaware-flip-structure.html", "Guide", "India to Delaware flip"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Closing a SAFE round and need the cap-table math?",
    cta_body="We model dilution across the SAFE conversion plus the Series A, co-ordinate with the US investor's lawyer on form, and handle the Indian-side FEMA filings if any component is Indian-issued. Standard SAFE close: 1-2 weeks from term sheet.",
))

# 5. ESOP vs RSU vs Phantom Stock
write_page("esop-vs-rsu-vs-phantom-stock-india-us", page(
    slug="esop-vs-rsu-vs-phantom-stock-india-us",
    title="ESOP vs RSU vs Phantom Stock 2026 | India-US Startup Guide - BQP",
    description="ESOP vs RSU vs phantom stock for Indian startups with US entities. Tax treatment under India Section 17(2), US Section 83(b), 409A valuations, vesting mechanics. Working CA guide.",
    keywords="ESOP vs RSU India, phantom stock India, 409A valuation startup, ESOP tax India, RSU tax India, 83(b) election ESOP, employee equity India US",
    hero_kicker="/ Employee equity &middot; ESOP vs RSU vs Phantom",
    hero_title_html="ESOP vs RSU vs phantom stock, <em>for India-US startups.</em>",
    hero_lead="Three ways to give employees equity-like upside: ESOPs (stock options), RSUs (restricted stock units), and phantom stock (cash-settled rights that track share value). For India-US startups the choice shapes employee tax at vesting / exercise / sale, employer accounting, and regulatory load. Here is the comparison.",
    sections=[
        ("/ The three instruments", "What each actually is.",
         "<p><strong>ESOP (stock option):</strong> A contractual right to buy a specified number of shares at a specified strike price, after a vesting period. Employee pays the strike price on exercise and becomes a shareholder. Upside is share-price-above-strike.</p>"
         "<p><strong>RSU (restricted stock unit):</strong> A contractual right to receive a specified number of shares (or their cash value) on vesting, with no strike price. Employee becomes a shareholder on vesting (or on a later settlement date). Upside is full share value at settlement.</p>"
         "<p><strong>Phantom stock:</strong> A contractual right to receive a cash payment equal to the share value (or appreciation above a reference price) on a vesting or liquidity event. Employee never actually holds shares; cash is paid at settlement. Upside is share-value-at-settlement, delivered as cash.</p>"),
        ("/ Indian tax at each stage", "Section 17(2) and Section 56.",
         "<p><strong>ESOP taxation in India (Section 17(2)(vi)):</strong></p>"
         "<ul>"
         "<li><strong>At grant:</strong> no tax.</li>"
         "<li><strong>At vesting:</strong> no tax.</li>"
         "<li><strong>At exercise:</strong> perquisite tax on the (FMV at exercise &minus; strike price). Taxed at slab rates in the employee's hands. Employer deducts TDS.</li>"
         "<li><strong>At sale of exercised shares:</strong> capital gains on (sale price &minus; FMV at exercise). LTCG if held 24+ months (unlisted) or 12+ months (listed); STCG otherwise.</li>"
         "</ul>"
         "<p><strong>RSU taxation in India:</strong> treated as ESOP with zero strike price for tax purposes. At vesting / settlement, perquisite tax on full FMV (equivalent of exercise event for RSU is vesting / settlement). At sale, capital gains on (sale price &minus; FMV at vesting).</p>"
         "<p><strong>Phantom stock taxation in India:</strong> no shares, no capital gains treatment. The cash payment at settlement is salary / bonus income, taxed at slab rates with TDS. No preferential capital-gains rate applies.</p>"),
        ("/ US tax at each stage", "ISOs, NSOs, 83(b), and 409A.",
         "<p>Different categories in the US:</p>"
         "<ul>"
         "<li><strong>ISO (Incentive Stock Option):</strong> US-citizen or US-resident employees only. Favourable tax treatment &mdash; no regular tax at exercise (AMT only), long-term capital gains on sale if held 2 years from grant + 1 year from exercise.</li>"
         "<li><strong>NSO (Non-qualified Stock Option):</strong> Any employee including non-US. Ordinary income tax on (FMV at exercise &minus; strike) at exercise. Capital gains on subsequent sale from FMV at exercise basis.</li>"
         "<li><strong>RSU:</strong> Ordinary income on FMV at vesting. Capital gains on sale from FMV at vesting basis.</li>"
         "<li><strong>83(b) election</strong> on founder restricted stock purchased at nominal price: lock in FMV at grant as the taxable amount (typically near-zero for day-one founders). Must file within 30 days.</li>"
         "<li><strong>409A valuation</strong>: required for US entities issuing options with strike price = FMV. Independent third-party valuation good for 12 months (or until a material event). Protects the company and employees from IRC 409A penalty for below-FMV options.</li>"
         "</ul>"),
        ("/ Which to use for which scenario", "Decision framework.",
         "<p><strong>Indian startup with Indian employees, no US entity:</strong> ESOP under India's standard ESOP regulations. 24-month minimum vesting cliff for Section 17(2) treatment; typical pattern is 4-year vest with 1-year cliff. Trust structure (ESOP Trust) often used for parking unvested options.</p>"
         "<p><strong>Delaware C-Corp with Indian employees (post-flip or Delaware-first):</strong> NSOs for Indian employees (ISOs are US-citizen/resident only). 409A valuation required. Standard 4-year vest / 1-year cliff. Indian employees pay perquisite tax on exercise under Section 17(2); the Delaware entity has no India tax deduction obligation (the Indian subsidiary that employs the employee does, via re-charge).</p>"
         "<p><strong>Delaware C-Corp with US employees:</strong> ISOs for US-citizen/resident employees up to the USD 100K annual vesting limit; NSOs beyond that. 83(b) for founder restricted stock. 409A valuation annual.</p>"
         "<p><strong>Phantom stock scenario:</strong> useful where the company does not want to actually issue shares (regulatory restriction, cap-table hygiene, or private-held preference). Also used for key employees of an Indian subsidiary where issuing shares in the parent is impractical. Tax is salary-rate at settlement &mdash; worse than ESOP for employees in high-growth exits, so typically reserved for exceptional cases.</p>"),
    ],
    faqs=[
        ("Is ESOP tax-free at grant in India?",
         "Yes. ESOPs are not taxable at grant or vesting in India. The taxable event is exercise &mdash; the FMV at exercise minus strike price is treated as salary perquisite under Section 17(2)(vi) and taxed at slab rates. A second tax event occurs at sale of the exercised shares, as capital gains."),
        ("Can an Indian employee hold ISOs?",
         "No. US ISOs (Incentive Stock Options) are available only to US-citizen or US-resident employees under IRC 422. Indian-resident employees of a Delaware C-Corp receive NSOs (Non-qualified Stock Options), which are ordinary-income at exercise for US tax purposes (though Indian tax rules govern their India-side treatment)."),
        ("What is 409A valuation and when do I need it?",
         "409A is a US tax rule requiring that stock options be granted at a strike price equal to the fair market value of the underlying stock on the grant date. For a private company, FMV is determined by an independent 409A valuation. The valuation is good for 12 months or until a material event (funding round, acquisition offer, significant business change). Required for every US option grant to avoid IRC 409A penalties."),
        ("How does phantom stock avoid cap-table dilution?",
         "Phantom stock is a contractual cash obligation, not actual equity. The company owes the employee a cash payment equal to the share value at settlement, but no shares are ever issued. Cap table is unchanged. The accounting treatment reflects the obligation as a liability on the balance sheet, with mark-to-market adjustments as share value changes."),
        ("What is the vesting cliff requirement in India for ESOP tax treatment?",
         "Section 17(2)(vi) requires a minimum vesting period for ESOPs to receive the standard perquisite tax treatment. The typical pattern is 1-year cliff + 3 years of monthly vesting (total 4 years), which satisfies the requirement. Shorter vesting can trigger immediate perquisite tax at grant rather than at exercise."),
        ("Does BQP structure ESOP / RSU plans for India-US startups?",
         "Yes. For Indian companies: Section 17 ESOP plan drafting, trust structure, vesting documentation. For Delaware C-Corps with Indian employees: NSO plan with 409A valuation co-ordination, India-side perquisite tax calculation, cross-border grant mechanics. Scoping depends on team size and cross-border composition. Request via get-a-quote.html."),
    ],
    related=[
        ("us-incorporation.html", "Guide", "US LLC &amp; C-Corp incorporation"),
        ("india-to-delaware-flip-structure.html", "Guide", "India to Delaware flip"),
        ("get-a-quote.html", "Mandate", "Get a firm quote"),
    ],
    cta_headline="Granting equity to your first 10 team members?",
    cta_body="The right instrument depends on where the employee lives, their tax residency, and your entity structure. We scope ESOP vs RSU vs phantom per employee, draft the plan documents, co-ordinate 409A valuation (if US entity), and handle the India-side perquisite tax at exercise.",
))

print("Batch C complete: 5 vs-comparison pages written")
