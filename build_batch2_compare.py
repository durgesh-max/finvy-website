# -*- coding: utf-8 -*-
"""Batch 2: 7 vs-comparison pages."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_seo import build_page, write_page

# -------- 6. Stripe Atlas vs Firstbase --------
write_page("stripe-atlas-vs-firstbase", build_page(
    slug="stripe-atlas-vs-firstbase",
    title="Stripe Atlas vs Firstbase | Delaware Formation Compared - BQP",
    description="Stripe Atlas vs Firstbase for Indian founders: pricing, EIN handling, US bank account setup, ongoing compliance and the FEMA gap neither covers. CA-led comparison.",
    keywords="Stripe Atlas vs Firstbase, Firstbase alternative India, Delaware C-Corp formation Indian founders, US incorporation SaaS, Stripe Atlas review, Firstbase review India, EIN service India, US company formation cost",
    hero_kicker="COMPARISON · US INCORPORATION",
    hero_title_html="Stripe Atlas vs Firstbase, <em>compared honestly.</em>",
    hero_lead="Two of the most-used incorporation platforms for founders forming a Delaware C-Corp from India. Pricing, timelines, what's included, what's missing, and the compliance gap both platforms leave open on the Indian side.",
    sections=[
        ("Overview", "Both are SaaS-first incorporation platforms",
         "<p>Stripe Atlas and Firstbase are software products that automate US company formation. Both file the Delaware Certificate of Incorporation, apply for the EIN, appoint a registered agent, and open a Mercury/Brex bank account through their integrations. The founder never speaks to a Chartered Accountant, lawyer or IRS employee during formation — the entire process is a series of web forms and PDFs. This works well for the US side. It does not address the Indian side of the cross-border structure, where FEMA, ODI reporting, transfer pricing and the eventual fundraise diligence pack live.</p>"),
        ("Pricing and inclusions", "What each fee actually covers",
         "<p>Both platforms use a headline one-time fee plus annual recurring charges.</p>"
         "<table><thead><tr><th>Component</th><th>Stripe Atlas</th><th>Firstbase</th></tr></thead><tbody>"
         "<tr><td>Formation fee (one-time)</td><td>USD 500</td><td>USD 399</td></tr>"
         "<tr><td>Delaware state filing (pass-through)</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>Registered agent (year 1)</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>Registered agent (yr 2+)</td><td>USD 100/yr</td><td>USD 199/yr</td></tr>"
         "<tr><td>EIN application</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>Bank account (Mercury)</td><td>Facilitated</td><td>Facilitated</td></tr>"
         "<tr><td>Post-incorporation compliance</td><td>Not included</td><td>Add-on packages</td></tr>"
         "<tr><td>Indian FEMA/ODI compliance</td><td>Not covered</td><td>Not covered</td></tr>"
         "</tbody></table>"
         "<p>Pricing changes; verify current fees on both sites before deciding.</p>"),
        ("What each does well", "Where the platforms shine",
         "<p><strong>Stripe Atlas</strong> is the closest to a one-click experience. Founder stock issuance, 83(b) mailing template, and integration into Stripe payment processing are seamless. Post-incorporation, the Atlas dashboard is a clean handoff to the founder for ongoing compliance calendaring. Good default choice for a founder who has already decided the US structure and just wants the paperwork done.</p>"
         "<p><strong>Firstbase</strong> emphasises ongoing compliance. Firstbase Loop and their tax filing add-ons cover Form 1120 preparation, Delaware franchise tax filing, and California/other state registrations as add-ons. Pricier over the multi-year horizon but reduces the number of vendors the founder juggles.</p>"),
        ("What both miss for Indian founders", "The Indian-side compliance gap",
         "<p>Neither platform touches the Indian regulatory obligations that arise when an Indian resident invests into a US entity. Specifically:</p>"
         "<ul>"
         "<li><strong>FEMA ODI compliance:</strong> Form ODI must be filed through your Indian AD bank within 30 days of remittance to the US entity.</li>"
         "<li><strong>Annual Performance Report (APR):</strong> Filed with RBI every year for as long as the ODI is held.</li>"
         "<li><strong>Transfer pricing (India):</strong> Form 3CEB is required if there are intercompany transactions between the Indian parent and US subsidiary (or vice versa).</li>"
         "<li><strong>ROC filings (India):</strong> Board resolutions, ODI declarations, and audit disclosures in the Indian company's books.</li>"
         "<li><strong>Fundraise diligence pack:</strong> Investors will demand a clean cross-border compliance file at diligence. Fixing it retroactively is 5-10x the cost of doing it right up front.</li>"
         "</ul>"
         "<p>This is the gap where a CA-led mandate pays for itself. BQP handles both sides in one engagement.</p>"),
    ],
    faqs=[
        ("Which is cheaper — Stripe Atlas or Firstbase?",
         "Firstbase is slightly cheaper on the initial formation fee. Stripe Atlas is cheaper on registered agent renewals (USD 100/yr vs USD 199/yr). Over 3 years, they land close. Neither includes Indian-side compliance, which is the real cost."),
        ("Do either help with EIN if I have no SSN?",
         "Yes. Both file Form SS-4 with the IRS on your behalf for the EIN. Timing varies from 1 to 6 weeks depending on IRS backlog. Neither requires you to have an SSN or ITIN."),
        ("Can I open a Mercury bank account through both?",
         "Yes. Both are integrated with Mercury. Approval is a Mercury underwriting decision, not the platform's — expect 1 to 3 weeks after entity is formed and EIN is issued. Mercury approval rates for Indian founders have been high since 2022."),
        ("Which handles the 83(b) election?",
         "Stripe Atlas provides a filled-out Form 83(b) mailing pack and instructs the founder to mail it within 30 days of stock issuance. Firstbase offers a similar template. The founder is responsible for actually mailing it and keeping the USPS certified-mail receipt. Missing the 30-day deadline is common and expensive."),
        ("Do either file Delaware franchise tax?",
         "Firstbase offers this as an add-on. Stripe Atlas reminds the founder but does not file it. Delaware franchise tax is due 1 March each year, with a minimum around USD 175 for a Wyoming LLC and around USD 400 for a Delaware C-Corp on the assumed par value method (materially higher on authorised shares method if not calculated correctly)."),
        ("Why would I pick a CA-led mandate over these?",
         "A CA-led mandate covers both jurisdictions in one fee. The US-side formation is roughly the same. The Indian-side FEMA/ODI/APR/3CEB/ROC compliance is included instead of missing. At fundraise, your diligence pack is clean. The total cost is comparable over 12 months and materially lower over the multi-year holding horizon."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="Comparing platforms and unsure?",
    cta_body="If you're on the fence between Atlas, Firstbase, Doola or a CA-led mandate, the right answer depends on your fundraise timeline, Indian corporate structure, and whether you have Indian-side transactions with the US entity. 20 minutes on WhatsApp saves months of retrospective clean-up.",
))

# -------- 7. Stripe Atlas vs Doola --------
write_page("stripe-atlas-vs-doola", build_page(
    slug="stripe-atlas-vs-doola",
    title="Stripe Atlas vs Doola | US Incorporation Compared - BQP",
    description="Stripe Atlas vs Doola for Indian founders: pricing, LLC vs C-Corp options, EIN handling, banking, tax filing add-ons and where each fits. CA-led comparison.",
    keywords="Stripe Atlas vs Doola, Doola alternative India, Delaware LLC formation, Wyoming LLC vs Delaware C-Corp, Doola review India, US incorporation Indian founder, tax filing Doola, LLC formation India",
    hero_kicker="COMPARISON · US INCORPORATION",
    hero_title_html="Stripe Atlas vs Doola, <em>compared honestly.</em>",
    hero_lead="Doola is the cheaper LLC-focused challenger to Stripe Atlas. When does the price gap matter, when doesn't it, and which fits which kind of founder — from a CA who has cleaned up after both.",
    sections=[
        ("Overview", "Different positioning, overlapping product",
         "<p>Stripe Atlas is positioned around Delaware C-Corp formation for founders raising US venture capital. Doola is positioned around Wyoming and Delaware LLC formation for solo founders, e-commerce operators, freelancers, and international entrepreneurs who need a US entity for banking, payment gateways, or e-commerce marketplaces (Amazon, Etsy). Both platforms will form either entity type; the marketing emphasis differs. For an Indian founder, the deciding question is what the US entity is <em>for</em>: raising VC (C-Corp), running an e-commerce/SaaS/consulting business (LLC often better), or holding US assets (LLC).</p>"),
        ("Pricing and inclusions", "The headline gap and what closes it",
         "<p>Doola is materially cheaper on the surface — starter LLC plans have historically been in the USD 197 range against Atlas's USD 500. The gap narrows once you add EIN expediting, registered agent renewals, tax filing add-ons, and any compliance modules. Verify current pricing on both sites before deciding.</p>"
         "<table><thead><tr><th>Component</th><th>Stripe Atlas</th><th>Doola (Starter)</th></tr></thead><tbody>"
         "<tr><td>Formation fee</td><td>USD 500</td><td>USD 197-297</td></tr>"
         "<tr><td>Entity type default</td><td>Delaware C-Corp</td><td>Wyoming or Delaware LLC</td></tr>"
         "<tr><td>Registered agent yr 1</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>EIN (standard)</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>EIN (expedited)</td><td>Not offered</td><td>Add-on</td></tr>"
         "<tr><td>Operating agreement</td><td>Included</td><td>Included</td></tr>"
         "<tr><td>Bookkeeping/tax</td><td>Not included</td><td>Add-on packages</td></tr>"
         "<tr><td>Indian FEMA/ODI</td><td>Not covered</td><td>Not covered</td></tr>"
         "</tbody></table>"),
        ("What each does well", "Where the platforms shine",
         "<p><strong>Stripe Atlas</strong> is stronger for founders on a clear US-VC path: Delaware C-Corp defaults, seamless founder-stock issuance, 83(b) mailing kit, integrated Stripe payments. Good defaults for a fundraise-bound business.</p>"
         "<p><strong>Doola</strong> is stronger for solo founders, e-commerce operators, and freelancers: cheaper starter tier, LLC-focused, bookkeeping and tax-filing add-ons designed for single-member operations, and a simpler dashboard aimed at non-VC use cases. If your US entity exists to accept Stripe payouts, run Amazon/Etsy sales, or hold IP, Doola LLC is often the right fit.</p>"),
        ("When each is wrong for you", "Failure modes",
         "<p><strong>Atlas is wrong when:</strong> you're bootstrapping a consulting practice with no VC in the picture — the C-Corp franchise tax and complexity are pure overhead. Wyoming LLC via Doola is materially cheaper to run.</p>"
         "<p><strong>Doola is wrong when:</strong> you're a startup raising a priced round from US VCs — they will require a Delaware C-Corp with founder stock, 83(b) filings, and clean cap table. Starting as an LLC and converting later is doable but adds cost and diligence friction.</p>"
         "<p><strong>Both are wrong when:</strong> the Indian entity is investing into the US entity and there's meaningful intercompany activity — FEMA ODI, transfer pricing, and the fundraise diligence pack need CA-led handling. Neither platform touches this.</p>"),
    ],
    faqs=[
        ("Which is cheaper — Stripe Atlas or Doola?",
         "Doola's starter plan is materially cheaper on formation. Over 12 months, if you add tax filing and bookkeeping add-ons on Doola, the gap shrinks. Atlas has no included ongoing compliance module."),
        ("Should I pick LLC (Doola) or C-Corp (Atlas)?",
         "LLC if you are solo, bootstrapping, running e-commerce/SaaS/consulting, or need a holding vehicle. C-Corp if you plan to raise a priced round from US VCs. LLC-to-C-Corp conversion later is possible via an F-reorganisation but adds cost and complexity."),
        ("Does Doola handle the EIN?",
         "Yes. Doola files Form SS-4 for the EIN. Timing follows the IRS International EIN backlog — usually 1 to 4 weeks. Both platforms handle this. Neither requires SSN."),
        ("Can I open a Mercury account with a Doola LLC?",
         "Yes. Mercury opens accounts for Wyoming and Delaware LLCs formed via Doola, subject to their own underwriting. Approval is common but not guaranteed. Timing typically 1-3 weeks after EIN is issued."),
        ("Does Doola handle California registration if I have California customers?",
         "California requires foreign LLC registration if you are 'doing business' in the state. Doola offers this as an add-on. Whether you actually need it depends on nexus — a Wyoming LLC selling SaaS to California customers without a California office or employee usually does not, but always confirm."),
        ("What about Form 5472 filing?",
         "A US LLC owned by a foreign person is a reportable disregarded entity requiring Form 5472 + pro-forma Form 1120 each year. Missing this is a USD 25,000 penalty. Doola offers this as a tax add-on. Atlas C-Corp files Form 1120 instead."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="LLC or C-Corp for your actual business?",
    cta_body="The right entity depends on your fundraise plans, US customer base, and whether the Indian entity will be involved. 20 minutes and we tell you honestly which of Atlas, Doola, Firstbase or a CA-led mandate fits your case.",
))

# -------- 8. C-Corp vs S-Corp --------
write_page("c-corp-vs-s-corp", build_page(
    slug="c-corp-vs-s-corp",
    title="C-Corp vs S-Corp | Eligibility, Tax, Which to Pick - BQP",
    description="C-Corp vs S-Corp explained: shareholder eligibility (why Indian founders cannot use S-Corp), federal tax treatment, when each entity fits and the practical decision matrix. CA-led guide.",
    keywords="C-Corp vs S-Corp, S-Corp eligibility, S-Corp Indian founder, C-Corp taxation, pass through taxation US, S-Corp shareholder limits, C-Corp double taxation, when to pick S-Corp, corp election Form 2553",
    hero_kicker="COMPARISON · US ENTITY STRUCTURES",
    hero_title_html="C-Corp vs S-Corp, <em>the honest answer.</em>",
    hero_lead="A common question that has a very short answer for most Indian founders (you cannot use S-Corp). The longer answer explains why, and covers the C-Corp vs LLC vs other options that actually apply.",
    sections=[
        ("Overview", "Two US federal tax classifications for the same corporate shell",
         "<p>Both C-Corp and S-Corp are the same state-law entity — a corporation formed under Delaware or another state's General Corporation Law. The difference is federal tax classification. A C-Corp is the default: it pays corporate income tax on its profits (21% federal + state), and its shareholders pay tax again on dividends. An S-Corp elects (via IRS Form 2553) to be a pass-through: no corporate-level tax, and profits/losses flow directly to shareholders' personal returns. The election has strict eligibility requirements that eliminate most cross-border founders, including all non-resident aliens.</p>"),
        ("Eligibility", "Why S-Corp is off the table for Indian founders",
         "<p>To make and maintain an S-Corp election, the corporation must satisfy all of the following (IRC Section 1361):</p>"
         "<ul>"
         "<li><strong>All shareholders must be US citizens or US resident aliens.</strong> Non-resident aliens are disqualified. Indian residents living in India, holding Indian passports, and not meeting the US substantial presence test are non-resident aliens.</li>"
         "<li>Maximum 100 shareholders.</li>"
         "<li>Only one class of stock (no preferred, no convertible with different rights).</li>"
         "<li>Only certain trusts and estates may be shareholders — no corporate shareholders, no partnerships as shareholders.</li>"
         "</ul>"
         "<p>The non-resident-alien disqualification is absolute. If a single share is transferred to an ineligible shareholder, the S election terminates automatically. This is why S-Corp is essentially unavailable to Indian founders operating from India.</p>"),
        ("Federal tax treatment", "How the numbers work when you can use S-Corp",
         "<p><strong>C-Corp tax:</strong> 21% federal corporate rate on taxable income + state corporate rate (Delaware franchise-only, California 8.84%, Texas nil corporate). Dividends to shareholders taxed again at their individual rate (up to 20% qualified dividend + 3.8% NIIT). For a US resident C-Corp shareholder with an operating business paying out dividends, effective rate is around 39-45% combined.</p>"
         "<p><strong>S-Corp tax:</strong> No corporate-level federal income tax. Profits and losses pass through to shareholders on Schedule K-1 and are taxed at individual rates. Shareholders receiving reasonable salary + distributions can avoid self-employment tax on the distribution portion — the main planning attraction for US resident owners of profitable service businesses.</p>"
         "<p>For a US-resident single-owner services business making USD 300-500k profit, S-Corp is typically the tax-optimal structure. For a VC-backed startup, C-Corp is required regardless.</p>"),
        ("Decision matrix", "What actually applies to you",
         "<p><strong>You are an Indian founder in India:</strong> S-Corp is not available. Choose between Delaware C-Corp (if raising US VC) or Wyoming/Delaware LLC (if bootstrapped or e-commerce/SaaS). We recommend LLC for the majority of cases where VC funding is not imminent, and C-Corp only when a priced round from US investors is on the near-term horizon.</p>"
         "<p><strong>You are a US-resident founder with a bootstrapped services business:</strong> S-Corp usually beats C-Corp on tax. Requires reasonable salary + payroll setup. Form 2553 election within 2 months and 15 days of the tax year start.</p>"
         "<p><strong>You are a US-resident founder raising VC:</strong> C-Corp, no exception. VCs will not invest in an S-Corp (pass-through kills their fund tax structure).</p>"
         "<p><strong>You are an Indian company with US operations:</strong> Delaware C-Corp subsidiary. Consider LLC only if the US operations are minimal and simple.</p>"),
    ],
    faqs=[
        ("Can an Indian founder living in India own an S-Corp?",
         "No. Non-resident aliens (which Indian residents living in India are) cannot be S-Corp shareholders. Owning even one share of an S-Corp as a non-resident alien terminates the election on the day the share transfers, and the corporation reverts to C-Corp tax treatment retroactively."),
        ("What if I become a US resident later — can I convert to S-Corp?",
         "Once you meet the US resident alien or citizen test, S-Corp eligibility opens. You can file Form 2553 to elect S status effective for the current tax year (within 2 months 15 days of year start) or effective for the following year. All other eligibility conditions (100 shareholders, one class of stock, no ineligible entity shareholders) must also be met."),
        ("How do C-Corp dividends actually get taxed?",
         "The C-Corp pays 21% federal + state tax on profits. When it distributes a dividend, the shareholder pays tax again: 0/15/20% qualified dividend rate + 3.8% Net Investment Income Tax for high earners. Effective combined rate is 36-45%. For non-resident alien shareholders receiving US-source dividends, US withholding is 30% (reduced to 15-25% by treaty)."),
        ("Is an LLC better than S-Corp for a US-resident founder?",
         "Depends. A single-member LLC is a disregarded entity (schedule C) with self-employment tax on all profits. An LLC electing S-Corp taxation (via Form 2553) can achieve the salary-plus-distribution tax savings without the S-Corp state-law inflexibility. Common structure for US-resident consultants making USD 200k+."),
        ("Can an S-Corp become a C-Corp later?",
         "Yes. Revoke the S election (majority shareholder consent, filed with IRS). Effective the date specified in the revocation or the following tax year. Once revoked, you must wait 5 years to re-elect S status. VCs may require this before investing."),
        ("Does S-Corp affect state tax?",
         "Most states honour the federal S-election (California, Delaware, others). New York and some states impose their own S-Corp filings and franchise taxes. State treatment can differ materially from federal — verify for the state of operation."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("esop-compensation.html", "Service", "ESOP &amp; 409A"),
    ],
    cta_headline="Picking the right US entity is the first fork in the road.",
    cta_body="C-Corp, LLC, S-Corp, disregarded entity — the wrong choice up front creates 5-figure retrofit costs later. 20 minutes with a CA who has structured hundreds of these gets you the right answer for your specific fact pattern.",
))

# -------- 9. Mercury vs Brex --------
write_page("mercury-vs-brex", build_page(
    slug="mercury-vs-brex",
    title="Mercury vs Brex | US Business Banking for Foreign Founders - BQP",
    description="Mercury vs Brex for Indian and foreign founders: account opening, minimum balances, wire fees, treasury yield, Ramp comparison, and which fits which stage.",
    keywords="Mercury vs Brex, Mercury bank India, Brex India founder, US business banking foreign founder, Mercury Treasury, Brex Cash, business bank account foreign, Mercury Ramp Brex",
    hero_kicker="COMPARISON · US BUSINESS BANKING",
    hero_title_html="Mercury vs Brex, <em>compared for foreign founders.</em>",
    hero_lead="Two of the most-used US business banking options for Indian and foreign founders. Account opening, minimums, wires, treasury, and where each stops making sense. Ramp mentioned where relevant.",
    sections=[
        ("Overview", "Both are fintech, not banks",
         "<p>Mercury and Brex are financial-technology platforms, not FDIC-chartered banks themselves. Both partner with FDIC-member banks (Choice Financial Group, Column, Evolve for Mercury; JPMorgan and others for Brex) to hold customer deposits under sweep programmes that extend FDIC coverage across multiple partner banks. The user experience is a modern web/mobile app; the underlying account is at the partner bank. Both open accounts for US-incorporated entities owned by foreign founders (subject to their own underwriting).</p>"),
        ("Opening an account as an Indian founder", "What each requires",
         "<p>Both platforms open accounts remotely for US-incorporated entities. The required documents are broadly similar: certificate of incorporation, EIN letter (IRS CP 575), operating agreement or bylaws, passport of authorised signatory, and business description. Both underwrite before opening — approval is not automatic. Approval rates for Indian founders with clean documentation have been high at Mercury since 2022 and moderate at Brex.</p>"
         "<p><strong>Mercury:</strong> Historically the more open door for foreign founders and early-stage startups. Underwriting focused on business legitimacy, no minimum balance, no monthly fee. Free domestic wires, USD 5 international outbound wire fees.</p>"
         "<p><strong>Brex:</strong> Historically stricter underwriting, favouring VC-backed startups with visible funding, more product depth (Brex Cash, Brex Corporate Card, expense management). Free wires domestic and international. In 2022 Brex began deprioritising bootstrapped and small startups, refocusing on VC-backed and enterprise.</p>"),
        ("Yield, wires, and fees", "The commercial terms that matter monthly",
         "<table><thead><tr><th>Feature</th><th>Mercury</th><th>Brex</th></tr></thead><tbody>"
         "<tr><td>Monthly fee</td><td>Nil (Standard)</td><td>Nil</td></tr>"
         "<tr><td>Minimum balance</td><td>Nil</td><td>Nil (mostly)</td></tr>"
         "<tr><td>Domestic wire (out)</td><td>Nil</td><td>Nil</td></tr>"
         "<tr><td>International wire (out)</td><td>USD 5</td><td>Nil</td></tr>"
         "<tr><td>Treasury yield (as of recent)</td><td>Mercury Treasury: money-market fund yields</td><td>Brex Cash: money-market fund yields</td></tr>"
         "<tr><td>Corporate card</td><td>Mercury IO (limited)</td><td>Brex Card (deep)</td></tr>"
         "<tr><td>Expense management</td><td>Basic</td><td>Deep (native)</td></tr>"
         "<tr><td>FDIC coverage (sweep)</td><td>Up to USD 5M</td><td>Up to USD 6M</td></tr>"
         "</tbody></table>"
         "<p>Rates and terms change; verify current terms on both platforms before deciding.</p>"),
        ("Which fits when", "The decision framework",
         "<p><strong>Pick Mercury when:</strong> you are an early-stage or bootstrapped founder, need reliable US banking with straightforward wires, want treasury sweep on idle cash, and don't need heavy expense management. Mercury is the most-common default for Indian founders forming a Delaware C-Corp or Wyoming LLC.</p>"
         "<p><strong>Pick Brex when:</strong> you are VC-backed, have visible traction and funding, want deep expense management and corporate card infrastructure, and international wires are frequent (free at Brex vs USD 5 at Mercury). Brex Card issuance is a genuine advantage over Mercury for companies with 10+ employees expensing frequently.</p>"
         "<p><strong>Consider Ramp when:</strong> the primary need is corporate card + expense management, not banking. Ramp is card-first with banking added later; the reverse of Mercury.</p>"
         "<p><strong>Consider both:</strong> Some founders keep Mercury for the operating account and Brex for the corporate card and expense stack. Legal and operational simplicity favours one platform.</p>"),
    ],
    faqs=[
        ("Do Mercury and Brex both accept Indian-founder-owned entities?",
         "Yes, both approve US-incorporated entities owned by Indian founders, subject to their own underwriting. Mercury's approval rate for Indian founders has been consistently high since 2022. Brex has become more selective since 2022, favouring VC-backed startups over bootstrapped ones."),
        ("Do I need a US SSN to open a Mercury or Brex account?",
         "No. Both accept passport of the authorised signatory. You do need a US-incorporated entity (Delaware, Wyoming, or another state) with a valid EIN issued by the IRS. Mercury and Brex will not open accounts for foreign-incorporated entities."),
        ("What is Mercury Treasury and how does it work?",
         "Mercury Treasury sweeps idle cash into money-market mutual funds (Vanguard Federal Money Market, Morgan Stanley Government Institutional). Not FDIC-insured (it's an SEC-registered investment fund) but generally regarded as very-low-risk. Yield varies with prevailing rates. Withdrawals settle T+1."),
        ("Is there a minimum balance at Brex?",
         "Brex removed most minimum balance requirements in 2023 but continues to be more selective on underwriting. Cash balances that fall to zero can trigger review. Verify current terms before opening."),
        ("What about Ramp — is it better than Mercury or Brex?",
         "Ramp is a corporate card + expense management platform with a Business Banking product. Positioning is closer to Brex than Mercury. For expense-heavy operations with strong card control needs, Ramp is competitive. For pure banking, Mercury is simpler."),
        ("If Mercury freezes my account, what happens?",
         "Fintech account freezes happen and recovery timelines vary. Mercury has been faster than average at unfreezes when documentation is provided. Best defence: keep customer records, invoices, and vendor documentation organised; respond to compliance requests within 48 hours; do not use the account for personal transactions."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="Setting up US banking for an Indian-owned entity?",
    cta_body="Account opening is the visible step; the invisible steps are getting the entity structure, EIN, authorised signatory documentation and initial funding routing right so that Mercury/Brex approve on the first pass. BQP does end-to-end.",
))

# -------- 10. SAFE vs Convertible Note --------
write_page("safe-vs-convertible-note", build_page(
    slug="safe-vs-convertible-note",
    title="SAFE vs Convertible Note | Early-Stage Instruments Compared - BQP",
    description="SAFE vs Convertible Note for early-stage rounds: valuation cap, discount, MFN, post-money vs pre-money SAFE, tax implications for Indian founders, when each fits.",
    keywords="SAFE vs convertible note, post money SAFE, pre money SAFE, valuation cap SAFE, convertible note interest, MFN clause SAFE, Y Combinator SAFE, seed round instrument, SAFE India founder tax",
    hero_kicker="COMPARISON · EARLY-STAGE FUNDING",
    hero_title_html="SAFE vs Convertible Note, <em>which and when.</em>",
    hero_lead="Two of the most-used instruments for pre-priced seed rounds. Mechanics, dilution, tax outcome, and how the choice looks different for an Indian founder building through a US parent versus staying India-only.",
    sections=[
        ("Overview", "Both defer valuation, in different ways",
         "<p>A SAFE (Simple Agreement for Future Equity) and a convertible note are both instruments that let a startup raise money now and issue equity later — at the next priced round. Neither requires setting a valuation at the time of investment. Both convert into shares at the priced round based on a valuation cap, a discount, or the lower of the two. The key differences are (i) SAFEs are equity, not debt; convertible notes are debt with interest and a maturity date; (ii) SAFEs are simpler; notes give investors downside protection via the maturity clause; (iii) tax treatment for founders and investors differs.</p>"),
        ("Mechanics", "Cap, discount, interest, maturity",
         "<p><strong>SAFE (Y Combinator, 2013; updated to post-money in 2018):</strong> Converts at the next priced round. Standard economic terms: valuation cap (converts at the lower of cap or round price), discount (converts at a discount to round price, e.g. 20%), or both. MFN (most-favoured nation) clause allows the SAFE holder to inherit better terms from a subsequent SAFE. Post-money SAFE (2018 version) fixes the dilution to the SAFE holders regardless of subsequent SAFEs; pre-money SAFE (original 2013) does not.</p>"
         "<p><strong>Convertible Note:</strong> Debt with an interest rate (typically 4-8% simple interest, accrued not paid) and a maturity date (typically 18-24 months). Converts at the priced round like a SAFE but with the accrued interest added to the principal at conversion. If no priced round happens before maturity, the note is technically due — in practice usually extended or converted to equity by mutual consent.</p>"
         "<p><strong>Dilution:</strong> Both dilute existing shareholders at conversion. Post-money SAFEs create a clearer picture of end-state cap table earlier; pre-money SAFEs and convertible notes create more uncertainty because the dilution depends on how much more is raised via similar instruments before the priced round.</p>"),
        ("Tax and regulatory implications", "For Indian founders and Indian-resident investors",
         "<p><strong>US side:</strong> SAFEs are generally treated as equity for US tax purposes (post-money SAFE is more clearly equity than pre-money). Convertible notes are debt until conversion, with interest income to the noteholder. Both instruments trigger 83(b) considerations if issued to founders as compensation (though usually not — usually issued for cash investment).</p>"
         "<p><strong>Indian side:</strong> If an Indian resident invests into a US startup via SAFE or note, the investment must be routed through the Liberalised Remittance Scheme (LRS, USD 250,000/year/person) or ODI (for Indian entity investors). SAFEs are typically permitted; convertible notes into US-incorporated startups also permitted subject to Indian reporting. Indian resident holding these instruments faces Indian tax on eventual capital gains at exit (LTCG 12.5% above INR 1.25 lakh, STCG at slab). Convertible note interest income is taxable in India on accrual (even if not paid in cash) — a genuine trap.</p>"),
        ("When each fits", "Practical picks",
         "<p><strong>Pick SAFE when:</strong> you are raising a friends-and-family or angel round from sophisticated investors, want minimal legal cost (Y Combinator SAFE forms are free), and expect a priced round within 12-18 months. Post-money SAFE is the current default in the US venture ecosystem.</p>"
         "<p><strong>Pick Convertible Note when:</strong> your investors want debt-like downside protection (interest accrual + maturity), you are raising in a jurisdiction where SAFEs are less common, or the round is a bridge to a specific event where the maturity date creates useful discipline. Also historically preferred by non-US investors who understand debt instruments better than SAFEs.</p>"
         "<p><strong>Consider a priced round instead when:</strong> the amount is large (typically USD 1M+ from institutional investors), you can defend a valuation, and the fully-diluted cap table clarity is worth the extra legal cost. Institutional VCs at Series Seed and above typically want a priced round.</p>"),
    ],
    faqs=[
        ("Is a post-money SAFE better than a pre-money SAFE?",
         "For the investor, post-money SAFE is more predictable — dilution is fixed at issue regardless of subsequent SAFEs. For the founder, post-money SAFE can be more dilutive if multiple SAFE rounds are stacked. Post-money is the current market standard for US SAFEs (Y Combinator switched in 2018)."),
        ("Does a convertible note accrue interest that founders have to pay?",
         "Interest accrues but is not paid in cash — it adds to the principal at conversion. So the founder never writes an interest check. At conversion into equity, the noteholder gets slightly more shares than they would have without interest accrual. Rate is typically 4-8%."),
        ("Can Indian founders issue SAFEs from a Delaware C-Corp?",
         "Yes. Delaware C-Corps routinely issue SAFEs for pre-priced rounds. The instrument is US-law-governed. Indian founders should ensure the SAFE is properly executed, board resolutions passed, and the incoming cash routed correctly to comply with US and Indian regulations."),
        ("What is the MFN clause in a SAFE?",
         "Most-Favoured Nation. If the company later issues a SAFE or note with better terms (lower cap, higher discount, other pro-investor terms), the MFN-holding investor can elect to swap their SAFE for the newer terms. Standard in Y Combinator SAFE templates."),
        ("How is SAFE conversion taxed for an Indian resident investor?",
         "At conversion, no US or Indian tax is triggered — it is an equity exchange, not a realisation event. At eventual sale of the converted shares, Indian LTCG applies (12.5% above INR 1.25 lakh) or STCG at slab rate for holdings under 24 months. US may withhold at 30% on the gain unless treaty benefits are claimed via Form W-8BEN and the shares qualify as not-US-real-estate under FIRPTA (usually the case for operating startups)."),
        ("What happens if the priced round never happens before note maturity?",
         "Technically the note is due at maturity. In practice, investors and founders extend the maturity or convert the note into equity at a mutually agreed valuation (often the last SAFE cap). Written amendments to the note are required. Failure to extend and failure to pay triggers a default event, giving the noteholder rights the company usually cannot honour."),
    ],
    related=[
        ("fund-raising.html", "Service", "Fund Raising"),
        ("capital-advisory.html", "Service", "Capital Advisory"),
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
    ],
    cta_headline="Structuring your first outside round?",
    cta_body="SAFE, note, priced round, side-letter terms, MFN, pro-rata, information rights — every one of these has an Indian-tax and FEMA implication if you are running a cross-border cap table. BQP structures early-stage rounds for founders raising from US, India and RoW investors.",
))

# -------- 11. ESOP vs RSU vs Phantom Stock --------
write_page("esop-vs-rsu-vs-phantom-stock", build_page(
    slug="esop-vs-rsu-vs-phantom-stock",
    title="ESOP vs RSU vs Phantom Stock | Employee Equity Compared - BQP",
    description="ESOP vs RSU vs Phantom Stock: mechanics, tax treatment at grant/vest/exercise/sale, Indian regulatory treatment, and which fits which stage of company.",
    keywords="ESOP vs RSU, phantom stock India, ESOP tax India, RSU tax India, employee stock option plan, SAR stock appreciation right, ESOP vesting India, 409A valuation, Rule 11UA valuation ESOP",
    hero_kicker="COMPARISON · EMPLOYEE EQUITY",
    hero_title_html="ESOP vs RSU vs Phantom, <em>tax outcomes compared.</em>",
    hero_lead="Three of the most-used employee equity instruments. How each works mechanically, where and when the employee gets taxed, and which is the right fit for an Indian startup at seed, growth or mature stage.",
    sections=[
        ("Overview", "Three instruments, three tax profiles",
         "<p>ESOPs (Employee Stock Option Plans), RSUs (Restricted Stock Units), and Phantom Stock / SARs (Stock Appreciation Rights) are three different ways to give employees economic upside tied to company equity. They differ on (i) whether the employee ever owns actual shares, (ii) when tax is triggered, and (iii) how the accounting and cash-flow implications hit the company. For Indian startups, ESOPs are the dominant instrument because they are well-understood by employees, RSUs are more common at listed and pre-IPO companies where actual share issuance is cleaner, and Phantom/SARs are used when the company wants to avoid actual cap table dilution.</p>"),
        ("How each works", "Mechanics side by side",
         "<p><strong>ESOP:</strong> Company grants employee an option to buy shares at a fixed strike price (usually FMV at grant). Option vests over 4 years typically (1-year cliff, then monthly). Employee exercises after vesting by paying the strike price. Between exercise and sale, the employee holds actual shares.</p>"
         "<p><strong>RSU:</strong> Company grants a right to receive shares (or cash equivalent) on vesting. No strike price. On vesting, shares are automatically issued to the employee (no exercise decision). Employee holds actual shares from vest date.</p>"
         "<p><strong>Phantom Stock / SAR:</strong> Company grants a right to receive a cash payment equal to the appreciation in the underlying share value between grant and payout date. Employee never receives actual shares. Payout is a cash bonus at a defined trigger event (vesting date, exit, IPO). Cap table is unchanged.</p>"),
        ("Tax treatment for Indian employees", "The critical column",
         "<p><strong>ESOP (Indian company):</strong> Under Section 17(2)(vi), tax is triggered at exercise on the difference between FMV at exercise and strike price — as salary income at slab rate. Second tax at sale on gain over FMV-at-exercise as capital gains (LTCG 12.5% if held 24+ months for unlisted shares, STCG at slab). Startups meeting DPIIT and Section 80-IAC conditions can defer the exercise-date tax under Section 191(2)(c) to the earlier of 48 months from exercise, exit, or sale.</p>"
         "<p><strong>RSU (Indian company):</strong> Tax at vest on the full FMV of the shares as salary income at slab rate. Second tax at sale on gain over FMV-at-vest as capital gains (LTCG 12.5% or STCG). RSUs from listed Indian companies are relatively common; unlisted RSUs are less used because the vest-date tax is a real cash outflow when the employee has no liquidity.</p>"
         "<p><strong>Phantom / SAR:</strong> Tax at payout on the full cash received as salary income at slab rate. No capital gains treatment — it is compensation. Simpler for the employee (single tax event) but no LTCG treatment available.</p>"),
        ("Which fits when", "Practical picks by stage",
         "<p><strong>Seed to Series B startup:</strong> ESOPs are the default. Standard 4-year vesting, 1-year cliff, strike at FMV per 409A/Rule 11UA valuation. Communicate the tax defer option (48-month deferral under Section 191(2)(c) if the startup is DPIIT-recognised and Section 80-IAC eligible). ESOP pool typically 10-15% at seed, expanded to 15-20% by Series B.</p>"
         "<p><strong>Growth stage / pre-IPO:</strong> Mix of ESOPs (for new hires) and RSUs (for senior hires at valuations where the strike price is large). RSUs eliminate the exercise decision for the employee and align cleanly with a near-term IPO timeline.</p>"
         "<p><strong>Mature private company / holding structure / family business:</strong> Phantom Stock or SARs can be preferable — no dilution, no cap table complexity, employee gets economic upside as a cash bonus. Common in professional services firms, family businesses, and companies that don't want employees on the register.</p>"),
    ],
    faqs=[
        ("What is a 409A valuation and do Indian startups need one?",
         "409A is a US IRS-mandated fair-market-value assessment for US C-Corp employee equity. An Indian company issuing ESOPs to Indian employees does not need a 409A — it needs a Rule 11UA valuation report from a registered valuer to set the strike price defensibly. If the Indian company has a US subsidiary issuing US employee equity, then 409A applies for that US-issued equity."),
        ("Can Indian startup ESOPs be tax-deferred?",
         "Yes, for startups recognised under DPIIT and eligible under Section 80-IAC (Section 191(2)(c), inserted by Finance Act 2020). Tax at exercise can be deferred to the earlier of 48 months from exercise, cessation of employment, or sale of shares. Not all startups qualify — check DPIIT and 80-IAC status."),
        ("Are RSUs from US parent to Indian employees taxable in India?",
         "Yes. If an Indian employee of the Indian subsidiary receives RSUs from the US parent, the vest-date FMV is taxable as salary in India at slab rate. The Indian employer must deduct TDS on this perquisite value. Later sale of the shares triggers Indian capital gains (with foreign asset reporting under Schedule FA if held on 31 March)."),
        ("What is the difference between a SAR and Phantom Stock?",
         "SAR (Stock Appreciation Right) pays only the appreciation between grant and payout — the strike-price analogue. Phantom Stock pays the full share value at payout (like receiving a share and cashing it). Both are cash instruments with no actual share issuance. SARs are more common; phantom stock less so."),
        ("Do ESOP schemes need SEBI or ROC approval?",
         "Indian ESOP schemes need approval by the company's shareholders via special resolution (Section 62(1)(b) of the Companies Act, Rule 12 of Companies (Share Capital and Debentures) Rules). Listed company ESOPs additionally need SEBI (Share Based Employee Benefits and Sweat Equity) Regulations 2021 compliance. Filed with ROC via MGT-14."),
        ("Can Phantom Stock be issued instead of ESOP to avoid dilution?",
         "Yes. Phantom stock creates no actual equity — cap table is unchanged. Ideal when founders want to avoid dilution, keep the register clean, or grant economic upside to consultants and non-employees where actual share issuance is regulatorily awkward. Tax is fully at slab rate on payout — no LTCG benefit."),
    ],
    related=[
        ("esop-compensation.html", "Service", "ESOP &amp; 409A / Rule 11UA Valuation"),
        ("fund-raising.html", "Service", "Fund Raising"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="Designing an employee equity scheme?",
    cta_body="Whether ESOP, RSU, phantom or a hybrid, the design decisions (strike, vesting, tax defer, valuation methodology, exit mechanics) compound. BQP designs schemes, produces the Rule 11UA / 409A valuation, files with ROC and defends the numbers at fundraise or audit.",
))

# -------- 12. Delaware C-Corp vs LLC --------
write_page("delaware-c-corp-vs-llc", build_page(
    slug="delaware-c-corp-vs-llc",
    title="Delaware C-Corp vs LLC | For Indian Founders - BQP",
    description="Delaware C-Corp vs LLC for Indian founders: taxation, Form 5472, VC-readiness, cost, when to pick each, and how to convert LLC to C-Corp later.",
    keywords="Delaware C-Corp vs LLC, LLC vs C-Corp Indian founder, Wyoming LLC vs Delaware C-Corp, Form 5472 LLC, F-reorganization LLC C-Corp, when to pick LLC, VC ready C-Corp, US entity Indian founder",
    hero_kicker="COMPARISON · US ENTITY STRUCTURE",
    hero_title_html="Delaware C-Corp vs LLC, <em>which fits you.</em>",
    hero_lead="The most-asked question for Indian founders setting up a US entity. Tax profiles, VC readiness, ongoing cost, the Form 5472 trap for foreign-owned LLCs, and the conversion path if you start with LLC and later need C-Corp.",
    sections=[
        ("Overview", "Two very different animals",
         "<p>A Delaware C-Corp is a corporation taxed at the entity level (21% federal + state). A LLC (Delaware or Wyoming) is by default a pass-through — a single-member LLC is a disregarded entity for US tax purposes, a multi-member LLC is a partnership. Both are US-incorporated entities that can hold US bank accounts, hire US employees, accept payments from US customers, and sign US contracts. The difference is what they do to your tax return, your fundraise readiness, and your annual compliance burden.</p>"),
        ("Tax treatment", "Where they diverge sharply",
         "<p><strong>C-Corp:</strong> Pays 21% federal corporate tax on taxable income. State corporate tax varies — Delaware has no state corporate tax on activity outside Delaware (franchise tax only, USD 400+ annually). Files Form 1120 annually. Dividends distributed to shareholders are taxed again at the shareholder's level. Losses stay trapped in the corporation.</p>"
         "<p><strong>LLC (single-member, foreign-owned):</strong> Disregarded entity for US tax — no separate corporate return. However, the foreign-owned single-member LLC must file <strong>Form 5472 with pro-forma Form 1120</strong> annually reporting related-party transactions. Missing this is a USD 25,000 penalty. If the LLC has US-source income (services rendered from the US, US real estate, etc.), the foreign owner has US tax exposure through the LLC.</p>"
         "<p><strong>LLC (multi-member):</strong> Partnership for US tax. Files Form 1065 and issues K-1 to each member. Each member pays US tax on their allocable share of income (foreign members via US withholding under Section 1446).</p>"),
        ("VC readiness and fundraise implications", "The reason most VC-bound startups pick C-Corp",
         "<p>US venture capital funds are structured as partnerships or LLCs themselves. When they invest in an LLC portfolio company, the pass-through nature creates unrelated business taxable income (UBTI) for their tax-exempt limited partners (endowments, pension funds), which forces awkward blocker structures. VCs almost universally require portfolio companies to be Delaware C-Corps for this reason.</p>"
         "<p>An LLC can be converted to a Delaware C-Corp via an F-reorganization (IRC Section 368(a)(1)(F)) before the priced round — this is standard practice for founders who started as LLC and later raise institutional capital. Legal cost typically USD 3-8k for the conversion, plus setup of new cap table.</p>"),
        ("Cost and ongoing compliance", "What you actually pay each year",
         "<table><thead><tr><th>Line item</th><th>Delaware C-Corp</th><th>Wyoming LLC</th><th>Delaware LLC</th></tr></thead><tbody>"
         "<tr><td>Formation state fee</td><td>USD 89-109</td><td>USD 100</td><td>USD 90</td></tr>"
         "<tr><td>Annual franchise/state tax</td><td>USD 400+ (assumed par value method, higher on authorised shares)</td><td>USD 60</td><td>USD 300</td></tr>"
         "<tr><td>Registered agent (annual)</td><td>USD 100-200</td><td>USD 50-150</td><td>USD 100-200</td></tr>"
         "<tr><td>Federal tax return</td><td>Form 1120 (paid preparer USD 1,500-3,000)</td><td>Form 5472 + pro-forma 1120 (USD 500-1,000)</td><td>Form 5472 + pro-forma 1120 (USD 500-1,000)</td></tr>"
         "<tr><td>Total year 1 (approx)</td><td>USD 2,000-4,000</td><td>USD 700-1,300</td><td>USD 900-1,500</td></tr>"
         "</tbody></table>"
         "<p>Wyoming LLC is materially cheaper. Delaware C-Corp costs more but delivers VC readiness. Verify current fees before deciding.</p>"),
    ],
    faqs=[
        ("If I don't plan to raise US VC, do I still need Delaware C-Corp?",
         "Usually no. Wyoming LLC is cheaper, simpler, and works for bootstrapped SaaS, e-commerce, consulting, holding US assets, and running an operating business without US employees. Convert to C-Corp only when a priced round is on the near-term horizon."),
        ("What is Form 5472 and why does it matter?",
         "Form 5472 reports transactions between a US corporation (or foreign-owned single-member LLC) and its foreign related parties. Filing is annual with the tax return (or as a pro-forma 1120 for disregarded LLCs). Penalty for failure to file is USD 25,000 per year. Most Indian-founder-owned single-member LLCs need this."),
        ("Can I convert an LLC to a C-Corp later?",
         "Yes, via an F-reorganization under IRC Section 368(a)(1)(F) — a statutory conversion filed with the state, treated as tax-free for US federal purposes. Legal cost typically USD 3-8k. Standard practice before a Delaware C-Corp priced round. Timing: allow 4-6 weeks."),
        ("Are LLC members personally liable for LLC debts?",
         "No — LLC provides limited liability shield similar to a corporation. Members are not personally liable for LLC debts and contracts (with narrow piercing-the-veil exceptions for fraud, undercapitalisation, personal guarantees). Same principle as a corporation."),
        ("Does an LLC or C-Corp need US employees?",
         "No. Both can operate without any US employees. Founders in India can run the entity remotely. US employees are needed only if you have physical operations in the US (retail, warehousing) or are hiring US-based staff (engineering, sales) intentionally."),
        ("What about franchise tax — how much does Delaware really cost?",
         "Delaware C-Corp franchise tax has two methods: (i) Authorised Shares Method — default, can be USD 175 to hundreds of thousands based on shares authorised, (ii) Assumed Par Value Capital Method — usually USD 400-450 for a small startup. Always calculate on both methods and pay the lower. Missing this is common and expensive."),
    ],
    related=[
        ("us-incorporation.html", "Service", "US Incorporation for Indian Founders"),
        ("global-taxation.html", "Service", "Global Taxation Advisory"),
        ("corporate-legal.html", "Service", "Corporate Legal &amp; FEMA"),
    ],
    cta_headline="Picking your US entity type?",
    cta_body="The C-Corp vs LLC decision compounds over years. Getting it right up front costs the same as getting it wrong; getting it wrong costs an F-reorganization later plus tax friction in the interim. BQP structures both, and converts LLCs to C-Corps when your fundraise timeline shifts.",
))

print("Batch 2 complete: 7 comparison pages written")
