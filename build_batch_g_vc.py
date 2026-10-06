# -*- coding: utf-8 -*-
"""Batch G: VC funding deep-dive pages for Indian founders (5 pages)."""
from build_lib import page, write_page

# 1. How to raise seed funding India
write_page("how-to-raise-seed-funding-india-startup", page(
    slug="how-to-raise-seed-funding-india-startup",
    title="How to Raise Seed Funding for Indian Startup 2026 | Complete Playbook - BQP",
    description="How to raise seed funding for Indian startup 2026: timing, deck, metrics bar, India vs US VC targeting, SAFE / CCD / equity, term-sheet negotiation, cap-table math, FEMA. Working CA + fund-raising guide.",
    keywords="how to raise seed funding India, seed round India startup, Indian seed VC list, pre seed vs seed India, seed round term sheet India, how much to raise seed India, India seed valuation",
    hero_kicker="/ Fundraising &middot; Seed round",
    hero_title_html="How to raise seed funding, <em>Indian startup playbook.</em>",
    hero_lead="Seed round in India in 2026 means raising USD 250K to USD 3M at valuations of USD 5M to USD 25M post-money, from a mix of Indian angel syndicates, Indian seed VCs, and US seed VCs with India mandates. The round takes 3-6 months end-to-end. This is the sequence that actually works.",
    sections=[
        ("/ When to raise seed", "The timing question.",
         "<p>Raise seed when you have one of:</p>"
         "<ul>"
         "<li><strong>Clear product-market signal:</strong> paying customers (even if small), strong retention, waitlist with intent-to-pay evidence.</li>"
         "<li><strong>Hard-to-replicate team / IP:</strong> technical founders with 10+ years of relevant expertise, published research, previous exits.</li>"
         "<li><strong>Market-timing urgency:</strong> a window that is opening or closing (regulatory change, platform shift, new buyer behaviour).</li>"
         "</ul>"
         "<p>Do NOT raise seed when:</p>"
         "<ul>"
         "<li>You have no customers, no team differentiation, no urgency &mdash; investors will pass regardless of pitch quality.</li>"
         "<li>You could instead reach INR 1 crore ARR via bootstrapped-to-cashflow &mdash; cheaper equity.</li>"
         "<li>You are not yet full-time on the business.</li>"
         "</ul>"
         "<p>Typical founder journey: ideation (3-6 months) &rarr; MVP + first customers (3-9 months) &rarr; pre-seed from angels or accelerator (3-6 months) &rarr; seed with institutional VCs. Jumping to seed too early is the single most common timing mistake.</p>"),
        ("/ What to raise", "Round-sizing math.",
         "<p>Seed round size is driven by: 18-24 month runway to the next round + hiring plan + marketing / acquisition cost + buffer. Dilution: 15-25% at seed is typical.</p>"
         "<p><strong>Example:</strong> target monthly burn INR 20 lakh / month post-raise (team of 8-10 + servers + minimal marketing). 24-month runway = INR 4.8 crore &asymp; USD 575K. Round USD 1-1.5M to allow buffer and growth hiring.</p>"
         "<p><strong>Pre-money vs post-money:</strong> seed term sheets typically specify post-money SAFE cap or equity-round post-money valuation. For USD 1.5M raise at USD 10M post-money &rarr; 15% dilution. For same raise at USD 7M post-money &rarr; 21% dilution.</p>"
         "<p><strong>Valuation reference points (India seed, 2026):</strong></p>"
         "<ul>"
         "<li>Pre-revenue + strong team / idea: USD 3-6M pre-money.</li>"
         "<li>Early revenue (INR 1-5 lakh MRR): USD 5-10M pre-money.</li>"
         "<li>Growing revenue (INR 10-25 lakh MRR): USD 10-20M pre-money.</li>"
         "<li>Strong growth + clear retention (INR 25-75 lakh MRR): USD 15-30M pre-money &mdash; borderline Series A.</li>"
         "</ul>"
         "<p>These are India-focused ranges. For AI / deeptech / US-oriented SaaS, valuations run 1.5-2x these.</p>"),
        ("/ Who to raise from", "India seed VCs vs US VCs vs angels.",
         "<p><strong>Indian seed VCs (sector-generalist):</strong></p>"
         "<ul>"
         "<li>Blume Ventures, Prime Venture Partners, 3one4 Capital, India Quotient, Fundamentum, Peak XV Surge, Elevation Capital.</li>"
         "<li>Cheque size USD 250K-2M at seed; valuations USD 5-20M pre.</li>"
         "<li>Lead investor expectation + board seat typically.</li>"
         "</ul>"
         "<p><strong>Indian seed VCs (sector-specialist):</strong></p>"
         "<ul>"
         "<li>Fintech: Beenext, Jupiter, Omnivore (agri).</li>"
         "<li>D2C: DSG Consumer Partners, Fireside, Sixth Sense.</li>"
         "<li>AI: Together Fund, Z21 Ventures.</li>"
         "<li>Climate: Climate Angels, Infuse Ventures.</li>"
         "</ul>"
         "<p><strong>Micro VCs / angel syndicates:</strong></p>"
         "<ul>"
         "<li>100X.VC, Antler India, PedalStart, All In Capital, Ex-Founder-syndicates (First Cheque, Volt, Angel List India).</li>"
         "<li>Cheque USD 25K-250K; fill out the round after lead.</li>"
         "</ul>"
         "<p><strong>US seed VCs with India mandate:</strong></p>"
         "<ul>"
         "<li>Accel US (via India), Lightspeed US-via-India, Sequoia (now Peak XV), Matrix Partners, General Catalyst India angle.</li>"
         "<li>Cheque USD 1-3M at seed; require Delaware C-Corp structure.</li>"
         "<li>Higher valuations, higher metrics bar, longer process.</li>"
         "</ul>"
         "<p><strong>Angel investors:</strong></p>"
         "<ul>"
         "<li>Named Indian angels: Kunal Shah, Nithin Kamath, Varun Alagh, Deep Kalra, Sanjay Mehta, Nikhil Kamath.</li>"
         "<li>LetsVenture / AngelList India syndicates: pooled smaller cheques.</li>"
         "<li>Alumni networks (IIT, IIM, Harvard, Stanford).</li>"
         "</ul>"),
        ("/ Instruments", "SAFE, CCD, CCPS, equity round.",
         "<p><strong>SAFE (if Delaware C-Corp):</strong> YC post-money SAFE, standard valuation cap. Fast close (1-2 weeks), low legal cost. Converts at next priced round. Not FEMA-compliant for Indian company.</p>"
         "<p><strong>CCD / CCPS (if Indian Pvt Ltd):</strong> Compulsorily Convertible Debentures or Compulsorily Convertible Preference Shares &mdash; the Indian analogues to SAFE. FEMA-compliant for foreign and domestic investors. Conversion mechanics specified in agreement.</p>"
         "<p><strong>Equity round:</strong> priced round with full Shareholder Agreement, Investor Rights Agreement, Articles of Association amendments. Longer close (6-12 weeks) but clean cap table.</p>"
         "<p><strong>Hybrid:</strong> many Indian seed rounds now use CCPS (preference shares) as the priced instrument &mdash; combines SAFE-speed of convertibility with FEMA-compliance and preference-stack economics.</p>"),
    ],
    faqs=[
        ("How long does a seed round take to close in India?",
         "3-6 months from first outreach to money in bank. First month: outreach + first meetings. Second month: product demo + metrics review. Third month: term sheet from lead. Fourth-sixth months: due diligence + legal + closing. Fast rounds (3 months) happen when metrics are exceptional or founder is known. Slow rounds (9+ months) usually mean the round is actually failing."),
        ("What valuation should I target for a seed round in India?",
         "USD 5-20M pre-money is the typical seed range. Pre-revenue + strong team: USD 3-6M. Early revenue (INR 1-5 lakh MRR): USD 5-10M. Growing revenue (INR 10-25 lakh MRR): USD 10-20M. AI / deeptech / US-oriented SaaS commands 1.5-2x these. Do not optimise for highest valuation &mdash; optimise for right lead investor and right round size for 18-24 month runway."),
        ("Should I raise in INR or USD?",
         "For Indian company: typically a mix. Indian VCs raise rupee cheques directly into the Indian company bank account via FDI route. US VCs raise USD into Delaware C-Corp (if flipped) or into Indian company via FDI. Round size is typically quoted in USD for consistency. Average seed round USD 1-2M = INR 8-16 crore."),
        ("Do I need to flip to Delaware before raising seed?",
         "If raising from US VCs: yes, flip first. US VCs almost always require Delaware C-Corp. If raising from Indian VCs: no, Indian company structure is fine &mdash; use CCPS for the round. Hybrid: some founders raise seed from Indian VCs into Indian company, then flip + raise Series A from US VCs. Depends on your funding path for the next 24 months."),
        ("What is a typical dilution at seed?",
         "15-25% is standard. 15% for strong team + strong metrics (small round at high valuation). 20-22% is typical. 25%+ is a sign of either weak metrics or needing a lot of capital or weak negotiation. Over 30% dilution at seed is a red flag for Series A investors who want enough founder equity preserved for future rounds."),
        ("Does BQP help with seed-round structuring?",
         "Yes. We handle: round structuring (SAFE vs CCPS vs equity vs hybrid), valuation certificate for pricing-guideline compliance, FEMA FC-GPR filings, Delaware-side if flipped, SAFE / term-sheet legal co-ordination, cap-table modelling across multiple scenarios, 83(b) + QSBS setup where applicable. Standard engagement from scoping to close. Request via get-a-quote.html."),
    ],
    related=[
        ("safe-vs-convertible-note-india-founder.html", "Guide", "SAFE vs Note"),
        ("india-to-delaware-flip-structure.html", "Guide", "Flip to Delaware"),
        ("vc-term-sheet-india-key-terms.html", "Guide", "VC Term Sheet Terms"),
    ],
    cta_headline="First seed round? Structure matters as much as pitch.",
    cta_body="Over the past 3 years, we have co-ordinated 40+ seed and Series A rounds for Indian founders &mdash; valuation certificates, FEMA FC-GPR, term-sheet review, cap-table modelling, flip-coordinated-with-raise. We know what common clauses to accept vs push back on. Scoping call is free.",
))

# 2. VC term sheet India key terms
write_page("vc-term-sheet-india-key-terms", page(
    slug="vc-term-sheet-india-key-terms",
    title="VC Term Sheet India 2026 | 15 Key Terms Explained - BQP",
    description="India VC term sheet decoded: liquidation preference, anti-dilution, pro-rata, drag-along, tag-along, protective provisions, board seats, information rights, founder vesting, ESOP pool. Working CA guide.",
    keywords="VC term sheet India, liquidation preference India, anti dilution India, pro rata rights VC, drag along tag along India, protective provisions India startup, founder vesting India",
    hero_kicker="/ Fundraising &middot; Term sheet",
    hero_title_html="VC term sheet, <em>15 terms that actually matter.</em>",
    hero_lead="A standard India VC term sheet is 6-10 pages but only ~15 terms genuinely affect your outcome at exit. The rest is boilerplate. Here is a working-founder's guide to each term, what the market standard is in 2026, and where to push back.",
    sections=[
        ("/ Economic terms", "Valuation, preference, dilution.",
         "<p><strong>1. Pre-money valuation.</strong> The valuation of the company before the investment. Pre-money + new money = post-money. Post-money also = (new money / investor ownership %). Fiercely negotiated. Market in 2026 India: seed USD 5-20M pre, Series A USD 20-50M pre, Series B USD 50-150M pre, Series C USD 150-400M pre.</p>"
         "<p><strong>2. Liquidation preference.</strong> At exit (sale or dissolution), the holder of preferred stock gets back their investment amount first (1x non-participating is the market standard in 2026). Participating preferences (2x, participating) are founder-hostile and rare at top rounds; expect them from strategic or distressed-round investors.</p>"
         "<p><strong>3. Anti-dilution.</strong> If a future round prices below the current round, existing preferred holders get additional shares to compensate. Three types: full-ratchet (very investor-friendly, rare), broad-based weighted average (market standard), narrow-based weighted average (friendlier to the investor). Default to broad-based WA.</p>"
         "<p><strong>4. ESOP pool.</strong> New ESOP pool created at the round, typically expanding the pool before the pricing. The pool is funded from the founders' pre-money equity (not post-money) &mdash; this is dilution the founders bear specifically. Standard: 10% ESOP at seed, additional 5-10% at Series A, 2-5% at later rounds. Push to size the pool realistically to your 18-24 month hiring plan, not over-size it.</p>"),
        ("/ Governance terms", "Board, information, protective.",
         "<p><strong>5. Board composition.</strong> Standard at seed: 3 seats (founder + lead investor + independent) or 2 seats (founder + lead). At Series A: 5 seats (founder + co-founder + Series A lead + Series Seed lead + independent). Founders should hold majority of board at least through Series A if possible.</p>"
         "<p><strong>6. Protective provisions / consent rights.</strong> List of actions requiring preferred-holder consent (change in articles, additional preferred classes, debt above a threshold, change in business, sale of substantially all assets, dividends). The list is long by default; negotiate thresholds carefully. Minimum (founder-friendly) and maximum (investor-friendly) wording differ materially.</p>"
         "<p><strong>7. Information rights.</strong> Monthly / quarterly reports, annual audited financials, board materials, access to books. Market standard: monthly P&amp;L, quarterly board report, annual audit, access to books on 2-week notice.</p>"
         "<p><strong>8. Pro-rata rights.</strong> Right of existing investor to participate in future rounds to maintain their ownership %. Usually attached to major investors (holding above threshold). Pro-rata rights at seed matter &mdash; this is how early investors double down in Series A and B.</p>"),
        ("/ Transfer terms", "Drag, tag, ROFR, ROFO.",
         "<p><strong>9. Right of First Refusal (ROFR).</strong> If a founder or major shareholder wants to sell their shares, the company and/or other preferred holders have the first right to buy. Standard.</p>"
         "<p><strong>10. Right of First Offer (ROFO).</strong> Softer version of ROFR &mdash; existing holders have the first offer, but the seller is free to seek higher prices externally.</p>"
         "<p><strong>11. Tag-along right.</strong> If a founder sells, other investors can 'tag along' and sell their proportionate share at the same price. Protects minority investors.</p>"
         "<p><strong>12. Drag-along right.</strong> If a defined threshold of shareholders (typically 50-75% of preferred + founder) approves a sale, all other shareholders can be forced to sell on the same terms. Essential for enabling clean exits. Negotiate the threshold.</p>"),
        ("/ Founder-specific terms", "Vesting, non-compete, employment.",
         "<p><strong>13. Founder vesting.</strong> Reset of founder equity to a 4-year vesting schedule with 1-year cliff. Even if founders previously held fully-vested shares, Series A often resets. Push for credit for time already served; push for single-trigger acceleration on involuntary termination.</p>"
         "<p><strong>14. Non-compete / non-solicit.</strong> 2-year non-compete and non-solicit post-termination. Reasonable but check scope (geographic, industry).</p>"
         "<p><strong>15. Founder employment agreement.</strong> New employment agreement signed with the Indian / Delaware entity &mdash; salary (initially modest, usually INR 20-40 lakh for Indian seed founder), benefits, equity vesting mechanics, IP assignment, termination clauses.</p>"),
    ],
    faqs=[
        ("What is 1x non-participating liquidation preference?",
         "The preferred-stock holder gets back 1x their investment amount before common shareholders get anything (that is the 'preference'). 'Non-participating' means after getting their 1x back, they stop participating in further distributions &mdash; they do not also get a pro-rata share of the remaining proceeds. For a founder, 1x non-participating is the market-friendly standard; 2x or participating preferences shift significant value to the investor at exit."),
        ("What is broad-based weighted average anti-dilution?",
         "The formula for issuing additional shares to existing preferred holders if a future round prices below the current round, using a broad-based 'fully diluted' share count as denominator (which dilutes the anti-dilution formula's effect on common shareholders). Market standard in India 2026. Full-ratchet anti-dilution (which fully adjusts preferred holders to the new lower price) is punitive for founders and other common holders."),
        ("Should founders accept pre-money ESOP pool funding?",
         "Reality: in competitive rounds, founders can push to post-money pool funding (where new investors also share the ESOP pool dilution). But in most India seed and Series A rounds, pre-money pool funding is market standard. The real negotiation is pool SIZE &mdash; if the investor insists on 15% ESOP pool but your 24-month hiring plan only needs 10%, push to size the pool realistically."),
        ("What are protective provisions I should push back on?",
         "Push back on: unanimous consent (vs supermajority); low revenue / debt thresholds (require consent even for small operational moves); any-investor consent (vs majority of preferred); forever duration (vs step-down post-IPO). Accept: consent for major-stakeholder-affecting actions (change in articles, new preferred class, M&A, dissolution). Market-reasonable protective provisions do not inhibit day-to-day operations."),
        ("What is founder vesting and should I accept it?",
         "4-year vesting with 1-year cliff on founder equity, usually reset at Series A even if founders previously held fully-vested shares. Yes, accept &mdash; it protects the business if a founder leaves. Push for: credit for time already served (so your clock starts earlier than Series A), single-trigger acceleration on involuntary termination (so you are not stripped of unvested shares if fired without cause), double-trigger acceleration on change of control (so M&A accelerates vesting)."),
        ("Does BQP review VC term sheets?",
         "Yes. Term-sheet review covers each of the 15+ terms, market-standard comparison for current round stage, specific-clause risk flags, prioritised negotiation ask list, and co-ordinated Indian + Delaware legal co-ordination if applicable. Standard engagement one-time per term sheet. Request via get-a-quote.html."),
    ],
    related=[
        ("how-to-raise-seed-funding-india-startup.html", "Guide", "Raising Seed"),
        ("safe-vs-convertible-note-india-founder.html", "Guide", "SAFE vs Note"),
        ("us-c-corp-vs-s-corp-indian-founder.html", "Guide", "C-Corp vs S-Corp"),
    ],
    cta_headline="Got a term sheet? Review before signing.",
    cta_body="A standard India VC term sheet has ~15 clauses that materially affect outcome. We review each, compare against market-standard for current round stage, and give you a prioritised push-back list. Faster + cheaper than a lawyer review for the business issues; still coordinate with legal for the drafting-side issues.",
))

# 3. US VC vs India VC for Indian startup
write_page("us-vc-vs-india-vc-indian-startup", page(
    slug="us-vc-vs-india-vc-indian-startup",
    title="US VC vs India VC for Indian Startup 2026 | Which to Raise From - BQP",
    description="US VC vs India VC comparison for Indian startups: valuation benchmarks, process length, structure requirements, follow-on strategy, exit expectations, flip requirement. Working CA + fund-raising guide.",
    keywords="US VC vs India VC, raise from US investor India startup, Sequoia vs Accel India, Delaware flip for US VC, Y Combinator India founder, US seed investor India",
    hero_kicker="/ Fundraising &middot; US VC vs India VC",
    hero_title_html="US VC vs India VC, <em>for an Indian startup.</em>",
    hero_lead="Indian founders in 2026 have real choice: raise from Indian VCs with Mumbai / Bengaluru offices and INR cheques, or raise from US VCs with Delaware-C-Corp requirements and USD cheques at higher valuations. The right choice depends on your product, customer location, Series B+ plan, and tolerance for the flip process.",
    sections=[
        ("/ Economic comparison", "Valuations and cheque sizes.",
         "<p><strong>India seed round (2026 market):</strong></p>"
         "<ul>"
         "<li>Cheque size: USD 250K-2M.</li>"
         "<li>Pre-money valuation: USD 5-20M.</li>"
         "<li>Dilution: 10-20%.</li>"
         "<li>Round close time: 3-6 months.</li>"
         "</ul>"
         "<p><strong>US seed round into India startup (2026 market):</strong></p>"
         "<ul>"
         "<li>Cheque size: USD 1-3M (larger lead cheques than India).</li>"
         "<li>Pre-money valuation: USD 10-30M (meaningfully higher).</li>"
         "<li>Dilution: 10-18%.</li>"
         "<li>Round close time: 4-9 months (longer due diligence).</li>"
         "<li>Delaware C-Corp requirement: typically yes.</li>"
         "</ul>"
         "<p><strong>India Series A:</strong></p>"
         "<ul>"
         "<li>Cheque: USD 5-10M. Pre-money USD 20-50M. Round USD 7-15M.</li>"
         "</ul>"
         "<p><strong>US Series A into India startup:</strong></p>"
         "<ul>"
         "<li>Cheque: USD 7-15M. Pre-money USD 30-80M. Round USD 10-25M. Delaware required.</li>"
         "</ul>"
         "<p>Headline: US VCs pay higher valuations and write larger cheques, but demand Delaware structure and higher metrics bar.</p>"),
        ("/ Process comparison", "What each VC actually does.",
         "<p><strong>India VC process:</strong></p>"
         "<ul>"
         "<li>Partner meeting &rarr; associate / principal diligence &rarr; investment committee &rarr; term sheet.</li>"
         "<li>Diligence: product demo, metrics review, customer calls (3-5), basic legal / financial review.</li>"
         "<li>Decision style: more conviction-driven, less data-heavy.</li>"
         "<li>Communication: relatively direct, often informal WhatsApp follow-up.</li>"
         "</ul>"
         "<p><strong>US VC process (for India-based startup):</strong></p>"
         "<ul>"
         "<li>Partner meeting &rarr; team meeting &rarr; associate / principal diligence &rarr; investment committee &rarr; term sheet.</li>"
         "<li>Diligence: product demo, extensive metrics review (cohorts, retention, LTV / CAC), 10-20 customer calls, technical review, legal / financial / tax diligence.</li>"
         "<li>Decision style: more data-heavy, benchmark-oriented. 'Can this be a USD 100M+ ARR company?' is the gate.</li>"
         "<li>Communication: more formal; investment memos, follow-on meetings, email-centric.</li>"
         "</ul>"
         "<p>US VC process is more thorough but less certain &mdash; many startups get far along the US VC process without a term sheet. India VCs are more decision-ready after fewer meetings.</p>"),
        ("/ Series B+ follow-on", "What happens next.",
         "<p><strong>India seed from India VC:</strong></p>"
         "<ul>"
         "<li>India VC leads Series A if metrics support.</li>"
         "<li>Series B often brings in US / global growth funds (Lightspeed Growth, General Atlantic, Tiger).</li>"
         "<li>Clean path if staying India-focused.</li>"
         "</ul>"
         "<p><strong>India seed from US VC:</strong></p>"
         "<ul>"
         "<li>US VC leads Series A if metrics meet US bar (usually higher).</li>"
         "<li>Delaware structure already in place; Series B US growth funds comfortable.</li>"
         "<li>Clean path if staying US-funded.</li>"
         "</ul>"
         "<p><strong>India seed from India VC &rarr; need US Series A:</strong></p>"
         "<ul>"
         "<li>Need to flip to Delaware before Series A term sheet.</li>"
         "<li>Flip triggers Indian capital gains on shareholder level.</li>"
         "<li>Flipping at Series A valuation (USD 50M+) can trigger significant founder tax outlays.</li>"
         "<li>Early-flip strategy: flip before Series A even if seed was from India VC.</li>"
         "</ul>"),
        ("/ Decision framework", "Which VC for which startup.",
         "<p><strong>Choose India VCs if:</strong></p>"
         "<ul>"
         "<li>India-focused market (India customers, India team, India-centric growth path).</li>"
         "<li>Prefer faster round close (3-6 months).</li>"
         "<li>Want sector-specialist Indian investors with India network.</li>"
         "<li>Not comfortable with Delaware structure complexity.</li>"
         "<li>Series B+ plan accepts Tiger / Lightspeed Growth / General Atlantic as later leads.</li>"
         "</ul>"
         "<p><strong>Choose US VCs if:</strong></p>"
         "<ul>"
         "<li>US-first market or AI / SaaS targeting global English-speaking enterprise.</li>"
         "<li>Comfortable with Delaware structure + flip process + 83(b) + QSBS mechanics.</li>"
         "<li>Need higher valuation / larger cheque at seed.</li>"
         "<li>Series B+ plan is US-led all the way.</li>"
         "<li>Have the metrics (USD 25K+ MRR, strong retention) that US VCs expect.</li>"
         "</ul>"
         "<p><strong>Hybrid (common):</strong> India seed round with India VC lead + US VC syndicate participation. Allows later US-led Series A without starting from zero on US-side relationships.</p>"),
    ],
    faqs=[
        ("Can an Indian startup raise from US VCs without flipping to Delaware?",
         "Technically yes &mdash; US VCs can invest into Indian Pvt Ltd via FDI route using CCPS or equity. Practically no &mdash; most US VCs require Delaware C-Corp structure for their standard investment documents, 83(b) / QSBS mechanics, and preferred-share machinery. Exceptions exist for specific India-focused US VCs who comfortable with Indian company direct investment, but rare at seed-plus."),
        ("Do US VCs pay higher valuations than India VCs?",
         "Generally yes, by 30-80% for the same company. US VC seed USD 15M pre-money vs India VC seed USD 8-10M pre-money for the same India-based startup is common. The trade-off: higher metrics bar, longer process, Delaware structure overhead, higher expectation at Series B+."),
        ("What is the metrics bar for a US VC seed cheque?",
         "Typical: USD 25K+ MRR growing 20%+ month-over-month, strong retention (90%+ monthly for consumer, 95%+ for B2B SaaS), clear ICP, demonstrable PMF signal. India VC bar is similar but often more flexible on absolute MRR (growth and retention trajectory matter more than specific MRR number)."),
        ("Should I flip to Delaware before raising seed or after?",
         "Before, if US VCs are in the plan. Flipping at low valuation (pre-seed, pre-revenue USD 2-5M FMV) triggers manageable Indian capital gains. Flipping at Series A valuation (USD 50M+) triggers large and often unaffordable founder tax outlays. Early flip is a one-time cost; late flip is a multi-million-dollar cost."),
        ("Can I take a hybrid round &mdash; India VC + US VC together?",
         "Yes, common and often optimal. India VC leads with their standard investment process (faster, confident). US VC participates alongside for 25-40% of the round. Both get preferred stock in the same round. Delaware C-Corp structure needed (if raising US VC) or Indian structure with CCPS (if staying India). Hybrid rounds work well at seed and Series A."),
        ("Does BQP handle US VC rounds for Indian founders?",
         "Yes. Pre-raise flip execution (6 weeks before term sheet), Delaware incorporation + 83(b) + QSBS setup, US VC term sheet review (markets us-standard clauses), FEMA FC-GPR for any Indian-side investment, transfer-pricing documentation for post-round operations. Scoping call covers the full US VC path. Request via get-a-quote.html."),
    ],
    related=[
        ("how-to-raise-seed-funding-india-startup.html", "Guide", "Seed Round"),
        ("vc-term-sheet-india-key-terms.html", "Guide", "VC Term Sheet"),
        ("india-to-delaware-flip-structure.html", "Guide", "Flip"),
    ],
    cta_headline="US VC path or India VC path &mdash; both work; pick deliberately.",
    cta_body="For founders planning the Series A horizon, deciding US VC path (flip early, higher metrics bar) vs India VC path (keep Indian structure, India network) is the single most consequential capital-strategy decision. We scope the trade-off for your specific business and model both paths over 24 months.",
))

# 4. Convertible instruments India CCD CCPS
write_page("convertible-instruments-india-ccd-ccps", page(
    slug="convertible-instruments-india-ccd-ccps",
    title="CCD and CCPS India 2026 | Convertible Instruments Startup Funding - BQP",
    description="India CCD (Compulsorily Convertible Debenture) and CCPS (Compulsorily Convertible Preference Shares) for startup funding: FEMA, pricing, conversion mechanics, tax, SEBI AIF subscription. Working CA guide.",
    keywords="CCD CCPS India, convertible preference shares India, compulsorily convertible debenture startup, CCPS FDI India, CCD valuation India, pricing guidelines FEMA conversion",
    hero_kicker="/ Fundraising &middot; Indian instruments",
    hero_title_html="CCD and CCPS, <em>India's SAFE equivalents.</em>",
    hero_lead="For Indian companies raising from foreign or domestic investors without flipping to Delaware, the two primary instruments are Compulsorily Convertible Debentures (CCDs) and Compulsorily Convertible Preference Shares (CCPSs). Both are treated as equity under FEMA for FDI purposes, allowing clean inbound investment. The choice between them depends on timing of conversion and specific terms needed.",
    sections=[
        ("/ CCD basics", "Compulsorily Convertible Debentures.",
         "<p>Compulsorily Convertible Debenture (CCD) is a debt instrument that <strong>must</strong> convert to equity at a specified time or event. It is treated as equity under FEMA from the moment of issue, not as debt.</p>"
         "<ul>"
         "<li><strong>Nature:</strong> debenture (debt-like) that compulsorily converts to equity. Not optional.</li>"
         "<li><strong>Conversion trigger:</strong> specified event (next priced round, maturity date) or automatic at a predetermined date.</li>"
         "<li><strong>Interest / coupon:</strong> can carry interest during the pre-conversion period.</li>"
         "<li><strong>FEMA treatment:</strong> treated as equity under FDI framework. Automatic Route for most sectors.</li>"
         "<li><strong>Companies Act:</strong> issued under Section 71 as debentures; conversion terms specified in the trust deed.</li>"
         "</ul>"
         "<p>CCDs were historically the standard instrument for pre-2017 FDI into Indian startups. CCPS has largely overtaken for new deals.</p>"),
        ("/ CCPS basics", "Compulsorily Convertible Preference Shares.",
         "<p>Compulsorily Convertible Preference Shares (CCPS) are preference shares that <strong>must</strong> convert to equity at a specified time or event. Combine preference-stock economics (liquidation preference, cumulative dividend) with mandatory convertibility.</p>"
         "<ul>"
         "<li><strong>Nature:</strong> preference shares (equity-like) that compulsorily convert to equity. Not optional.</li>"
         "<li><strong>Conversion trigger:</strong> next priced round + 1x conversion, or specified event, or maturity (typically 20 years max under Indian Companies Act).</li>"
         "<li><strong>Liquidation preference:</strong> can specify 1x non-participating, 1x participating, or 2x variants.</li>"
         "<li><strong>Dividend:</strong> can specify cumulative or non-cumulative; practically rare for startup CCPS to pay dividend.</li>"
         "<li><strong>FEMA treatment:</strong> treated as equity under FDI framework.</li>"
         "<li><strong>Companies Act:</strong> issued under Section 55 as preference shares.</li>"
         "</ul>"
         "<p>CCPS is now the preferred Indian-side instrument for most seed and Series A rounds &mdash; combines preference-stock economics with FEMA-compliance.</p>"),
        ("/ Pricing and valuation", "FEMA pricing guidelines apply.",
         "<p>Both CCDs and CCPSs issued to foreign investors must comply with FEMA pricing guidelines:</p>"
         "<ul>"
         "<li><strong>Primary issuance to foreign investor:</strong> issue price must be at or above fair value determined by SEBI-registered Merchant Banker (DCF, NAV, or comparable-company method).</li>"
         "<li><strong>Secondary transfer:</strong> transfer price must be between fair value floor and fair value ceiling.</li>"
         "<li><strong>Fair-value certificate:</strong> required from SEBI-registered Merchant Banker before each FDI issuance.</li>"
         "<li><strong>No below-fair-value issuance:</strong> except in specified exceptions (ESOPs, bonus issue, rights issue).</li>"
         "</ul>"
         "<p>Conversion price: typically specified in the shareholder agreement as 'conversion at the next priced round' at either the pre-money valuation of that round (pre-money CCPS, less dilutive to new investors) or at the subscription-plus-discount price (less common).</p>"),
        ("/ Mechanics and timeline", "Issuance to conversion.",
         "<ol>"
         "<li><strong>Round structure finalised</strong> &mdash; CCD or CCPS, conversion terms, liquidation preference, pre-money.</li>"
         "<li><strong>Shareholder resolution</strong> amending Articles if needed; special resolution for preference share issuance.</li>"
         "<li><strong>Valuation certificate</strong> obtained from Merchant Banker.</li>"
         "<li><strong>Pricing guideline compliance confirmed.</strong></li>"
         "<li><strong>Investor remits capital</strong> to Indian company bank account.</li>"
         "<li><strong>Shares / debentures issued</strong> to the investor.</li>"
         "<li><strong>Form FC-GPR filed with RBI</strong> within 30 days of share issue.</li>"
         "<li><strong>Trust deed executed</strong> for CCDs (securing the debenture).</li>"
         "<li><strong>Conversion</strong> at the specified trigger &mdash; CCDs convert to equity; CCPS convert to equity. Fresh set of equity shares issued; FC-GPR filing on conversion is NOT required (conversion is intra-FDI).</li>"
         "</ol>"
         "<p>Common timing: CCD / CCPS issued at seed round; converts to equity at Series A priced round.</p>"),
    ],
    faqs=[
        ("What is the difference between CCD and CCPS?",
         "CCD (Compulsorily Convertible Debenture) is a debt instrument that must convert to equity. CCPS (Compulsorily Convertible Preference Shares) is a preference-share instrument that must convert to equity. CCDs are issued under Section 71 (Companies Act debenture rules); CCPSs under Section 55 (preference share rules). Both treated as equity under FEMA for FDI purposes. CCPS is the preferred structure today because it carries preference economics (liquidation preference, cumulative dividend if desired) built-in."),
        ("Is SAFE legal in India for Indian company funding?",
         "Direct SAFE issuance by an Indian company is not clearly covered under FEMA/Companies Act and faces regulatory uncertainty. The Indian equivalents are CCDs (debenture route) or CCPS (preference share route). Both deliver similar economics to SAFE (convertibility, no immediate equity dilution) within a FEMA-compliant framework. For Delaware C-Corp subsidiaries of Indian founders, SAFEs are freely usable."),
        ("Can domestic Indian investors subscribe to CCPS?",
         "Yes. Domestic Indian individuals, companies, and SEBI-registered AIFs can subscribe to CCPS of Indian companies. For AIF subscription, specific allocation and reporting rules apply. For individual investors, standard subscription under Companies Act."),
        ("Do CCPS carry dividend?",
         "They CAN carry dividend if specified, but startup CCPS typically do not. Standard startup CCPS: 1x non-participating liquidation preference + conversion to equity at next priced round + no dividend. If dividend is specified (cumulative or non-cumulative), the tax treatment follows dividend rules (shareholder-level taxable, 10% TDS under Section 194)."),
        ("When do CCPS convert to equity?",
         "At the specified trigger &mdash; typically the next priced round. Standard mechanic: CCPS 'converts at the pre-money valuation of the next priced round at 1x' (meaning the CCPS holder gets equity shares equivalent to their investment amount at the pre-money valuation of the next round). This is similar to how a SAFE converts in a US round."),
        ("Does BQP structure CCD / CCPS rounds for Indian startups?",
         "Yes. Full stack: round structuring (CCD vs CCPS vs equity), Merchant Banker valuation certificate (via SEBI-registered partner), FEMA pricing guideline compliance, shareholder resolutions, Articles amendments if needed, FC-GPR filing within 30 days, ongoing cap-table maintenance, conversion event execution at next round. Request via get-a-quote.html."),
    ],
    related=[
        ("safe-vs-convertible-note-india-founder.html", "Guide", "SAFE vs Note"),
        ("how-to-raise-seed-funding-india-startup.html", "Guide", "Raising Seed India"),
        ("fdi-vs-fpi-india-startup-investment.html", "Guide", "FDI vs FPI"),
    ],
    cta_headline="CCPS is the Indian SAFE &mdash; use it correctly.",
    cta_body="For Indian company seed and Series A rounds from foreign investors without a Delaware flip, CCPS is the standard. We handle valuation certificate, FEMA FC-GPR, Articles amendments, shareholder resolutions, and conversion mechanics at the next round. Per-round engagement from INR 1.5 lakh.",
))

# 5. Founder vesting India US
write_page("founder-vesting-india-us-startup", page(
    slug="founder-vesting-india-us-startup",
    title="Founder Vesting India + US 2026 | Mechanics, 83(b), Reverse-Vesting - BQP",
    description="Founder vesting for India + US startup: Series A reverse-vesting, 4-year cliff schedules, 83(b) election for Delaware C-Corp, single and double-trigger acceleration, buy-back on departure. Working CA guide.",
    keywords="founder vesting India, founder vesting Delaware C-Corp, 83(b) election founder shares, reverse vesting Series A, founder acceleration vesting, India US founder vesting",
    hero_kicker="/ Equity &middot; Founder vesting",
    hero_title_html="Founder vesting, <em>India and US mechanics.</em>",
    hero_lead="Founder vesting is a term sheet standard: at Series A (sometimes earlier), founder equity resets to a 4-year vesting schedule with 1-year cliff. In India and US contexts the mechanics, tax implications and acceleration provisions differ. Here is the working-CA mapping of both sides.",
    sections=[
        ("/ What founder vesting is", "The reset at Series A.",
         "<p>Founder vesting means founder equity is subject to a schedule where it 'earns' over time. If the founder leaves before equity is fully vested, the unvested portion is forfeited or bought back by the company. Protects the business and remaining team from a founder leaving early.</p>"
         "<p><strong>Standard schedule:</strong> 4-year vesting with 1-year cliff. Mechanics:</p>"
         "<ul>"
         "<li>Nothing vests in the first 12 months (the 'cliff').</li>"
         "<li>At month 13, 25% (one year of vesting) vests all at once (cliff vest).</li>"
         "<li>From month 13 onwards, 1/48th of total equity vests each month (uniform vesting).</li>"
         "<li>At month 48, 100% vested.</li>"
         "</ul>"
         "<p><strong>When applied:</strong> most commonly at Series A &mdash; even if founders previously held 'fully vested' shares. The investor terms require a vesting reset. Negotiate to carve out time already served ('credit for time served').</p>"),
        ("/ Mechanics in Delaware C-Corp", "Restricted stock + 83(b).",
         "<p>In Delaware C-Corp structure, founder vesting is typically implemented via <strong>restricted stock</strong>:</p>"
         "<ul>"
         "<li>Founder is issued restricted stock subject to a Stock Restriction Agreement.</li>"
         "<li>Each tranche of stock vests on schedule.</li>"
         "<li>If founder departs before full vesting, the company has a repurchase right over unvested shares at the original purchase price (typically USD 0.001/share &mdash; i.e., buyback at a nominal amount).</li>"
         "</ul>"
         "<p><strong>83(b) election</strong> &mdash; critical:</p>"
         "<ul>"
         "<li>Within 30 days of restricted stock grant, founder files IRS Form 8832 (83(b) election).</li>"
         "<li>Election locks in the fair market value AT GRANT as the taxable amount, regardless of future vesting.</li>"
         "<li>For founder restricted stock purchased at nominal value when FMV is also nominal (day-one incorporation), 83(b) locks in near-zero taxable amount.</li>"
         "<li>Without 83(b): when each tranche of vested shares becomes substantially non-restricted, founder recognises taxable ordinary income on the then-FMV of that tranche. In a successful startup, this can be a massive tax bill at each vesting tranche &mdash; often prohibitive.</li>"
         "</ul>"
         "<p><strong>Missing the 30-day 83(b) window is unrecoverable.</strong> Set reminders, file via Certified Mail, retain acknowledgement.</p>"),
        ("/ Mechanics in Indian Pvt Ltd", "Founder equity + buyback agreement.",
         "<p>In Indian Pvt Ltd structure, founder vesting is typically implemented via a <strong>Share Purchase Agreement + Shareholder Agreement</strong> with vesting clauses:</p>"
         "<ul>"
         "<li>Founder holds equity shares outright.</li>"
         "<li>Shareholder Agreement specifies vesting schedule.</li>"
         "<li>If founder departs before full vesting, Indian investors have a call option to buy back the unvested shares at a predetermined price (often face value or nominal).</li>"
         "</ul>"
         "<p><strong>Tax at vesting:</strong></p>"
         "<ul>"
         "<li>Equity shares already held: no tax at vesting event (unlike US restricted stock without 83(b)).</li>"
         "<li>Buy-back by company at founder departure: tax under Section 115QA post-Oct 2024 (buyback distribution tax reinstated).</li>"
         "<li>Sale by founder at exit (fully vested shares): LTCG at 12.5% (post-July 2024) if held 24+ months.</li>"
         "</ul>"
         "<p>Indian structure is more tax-friendly than US without 83(b), but less flexible than US with 83(b) + QSBS.</p>"),
        ("/ Acceleration provisions", "Single and double trigger.",
         "<p>Acceleration shortens or eliminates the vesting schedule under specific circumstances. Two main types:</p>"
         "<p><strong>Single-trigger acceleration</strong> on involuntary termination (fired without cause):</p>"
         "<ul>"
         "<li>If the company fires the founder without cause, all remaining unvested shares immediately vest.</li>"
         "<li>Founder-protective; limits investor-side moves to oust founders.</li>"
         "<li>Market standard: push for 50-100% single-trigger acceleration on involuntary termination.</li>"
         "</ul>"
         "<p><strong>Double-trigger acceleration</strong> on change of control + termination:</p>"
         "<ul>"
         "<li>If the company is acquired AND the founder is terminated post-acquisition (or founder resigns for good reason), all unvested shares immediately vest.</li>"
         "<li>Protects founders from forced-departure post-sale.</li>"
         "<li>Market standard: 100% double-trigger acceleration is widely accepted.</li>"
         "</ul>"
         "<p><strong>Full single-trigger on change of control alone</strong> (acceleration on sale regardless of termination): investor-hostile and typically rejected. Not market-standard.</p>"),
    ],
    faqs=[
        ("Why do investors require founder vesting?",
         "To protect the business and the remaining team if a founder leaves early. If a 50/50 cofounder leaves 18 months after Series A with all shares vested, the remaining founder and investors are left with a cap table that still has the departing founder owning 50% &mdash; punitive. Vesting ensures that the equity flows to those actively building the business."),
        ("When should I file 83(b)?",
         "Within 30 days of receiving restricted stock. The 30-day window is strict and unrecoverable if missed. Typical scenarios: day of C-Corp incorporation (founders receive restricted stock); day of LLC-to-C-Corp conversion; day of F-reorg flip (founders receive C-Corp restricted stock). File by Certified Mail to the IRS Service Center listed in current Form 83(b) instructions. Retain acknowledgement."),
        ("What is the tax risk if I miss 83(b)?",
         "At each vesting tranche, the founder recognises ordinary-income tax on the then-FMV of the vested stock. In a successful startup, the FMV at each tranche can be USD hundreds of thousands or millions &mdash; and the founder owes ordinary income tax on that amount with no cash from the stock. Many founders have been bankrupted by missed 83(b) elections in high-growth companies. 83(b) is the single most critical founder-equity administrative task."),
        ("Can I get credit for time served before Series A reset?",
         "Push for it. Standard investor-friendly reset: 48 months from the Series A closing. Market-friendly compromise: founder gets credit for pre-reset time served (e.g., 'founder has already served 18 months, so 18 months vests immediately on reset, 30 months remain to vest'). This is the single most important vesting negotiation for existing founders."),
        ("Do I need separate vesting agreements for India + Delaware structures?",
         "If you have both (Indian subsidiary + Delaware parent post-flip), typically the founder equity sits at the Delaware level and vesting mechanics follow Delaware restricted stock + 83(b). Indian subsidiary employment is separate (salary paid in INR by Indian subsidiary). If the structure is Indian parent + Delaware subsidiary, founder equity at Indian level follows Indian Pvt Ltd mechanics."),
        ("Does BQP handle founder vesting setup?",
         "Yes. Delaware C-Corp restricted stock agreements + 83(b) election preparation + 30-day filing with Certified Mail + 83(b) acknowledgement retention. Indian Pvt Ltd founder vesting via Shareholder Agreement + buyback mechanics. India-Delaware co-ordination for post-flip founders. Standard engagement at incorporation or at Series A term-sheet stage. Request via get-a-quote.html."),
    ],
    related=[
        ("vc-term-sheet-india-key-terms.html", "Guide", "VC Term Sheet"),
        ("india-to-delaware-flip-structure.html", "Guide", "Flip to Delaware"),
        ("esop-vs-rsu-vs-phantom-stock-india-us.html", "Guide", "ESOP vs RSU"),
    ],
    cta_headline="Series A reset incoming? 83(b) is the first filing &mdash; 30-day window.",
    cta_body="Founder vesting reset at Series A is a term-sheet standard. The 83(b) election is the IRS filing that locks in near-zero taxable basis for the restricted stock &mdash; miss the 30-day window and it is unrecoverable. We co-ordinate the vesting mechanics (India and Delaware), prepare the 83(b), file by Certified Mail with acknowledgement.",
))

print("Batch G complete: 5 VC-funding pages written")
