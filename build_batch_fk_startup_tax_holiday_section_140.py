# -*- coding: utf-8 -*-
"""Batch FK (22 Nov 2026): Startup tax holiday - section 80-IAC of the 1961 Act, now section 140 of the Income-tax Act,
2025. Eligibility, the 2030 cut-off, IMB certificate, MAT, 115BAA, and the February 2026 DPIIT framework. Call-first.
Demand: sweep 22 Nov 2026 (ac44, founders), all 7 markets: "section 80iac eligibility", "section 80iac registration",
"eligible business under section 80iac", "startup india tax exemption for 3 years", "startup india tax exemption
certificate", "startup india tax exemption conditions", "startup india tax exemption limit", "startup taxation in india".
Site had one 'best CA' page with stale points and other pages saying '3 of 7 years'.
Facts (checked 22 Nov 2026):
- Income Tax Department, text of section 140, Income-tax Act, 2025 ("Special provision in respect of specified
  business"; page reviewed 26 Oct 2026): 100% of profits of eligible business for three consecutive tax years out of
  ten beginning with the year of incorporation; eligible start-up = company or LLP engaged in eligible business,
  incorporated on or after 1 April 2016 but before 1 April 2030, total turnover not above INR 100 crore in the tax year
  of the claim, holding a certificate of eligible business from the Inter-Ministerial Board; not formed by splitting up
  or reconstruction, or by transfer of previously used plant and machinery (with the imported-machinery exception).
- FY 2025-26 claims fall under section 80-IAC of the 1961 Act (same conditions; Finance Act 2025 extended the
  incorporation date to 31 March 2030). TaxUpdate, 12 June 2026.
- 115BAA bars most deductions, including this one; MAT applies under the normal regime and the MAT paid is creditable.
- DPIIT G.S.R. 108(E), 4 Feb 2026 (Treelife, Lexology, Nasscom summaries): recognition turnover limit INR 200 crore;
  deep tech startups 20 years and INR 300 crore; age limit 10 years retained; cooperative societies eligible.
- Some secondary reports say the Finance Act, 2026 raised the tax turnover test to INR 300 crore; the department's own
  section 140 text (reviewed 26 Oct 2026) still reads INR 100 crore. The page states INR 100 crore and flags this."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 22 November 2026."
SLUG = "startup-tax-holiday-section-80-iac-now-section-140-eligibility-imb-certificate-mat-115baa-2026"

C = contact("your incorporation date, entity type (company or LLP), DPIIT recognition number if any, turnover and expected profit for the next three years, and whether you have opted for the 22% regime")
PAGES = [dict(
    slug=SLUG,
    title="Startup Tax Holiday in India (2026): Section 80-IAC, Now Section 140 - Eligibility, the IMB Certificate, MAT, the 22% Regime and the 2030 Cut-Off",
    em="three tax-free years, if you plan them.",
    kicker="/ Startups &middot; Income tax &middot; Updated 2026-11-22",
    lead=("<strong>An eligible Indian startup pays no income tax on its business profits for any three consecutive years of its choice within its first ten years.</strong> "
          "The relief was section 80-IAC of the Income-tax Act, 1961 and is <strong>section 140 of the Income-tax Act, 2025</strong> from 1 April 2026, on the same conditions. "
          "To qualify, the startup must be a <strong>company or LLP incorporated between 1 April 2016 and 31 March 2030</strong>, have turnover of <strong>INR 100 crore or less</strong> in the year of the claim, and hold a <strong>certificate from the Inter-Ministerial Board</strong>. DPIIT recognition alone is not enough. "
          "Two traps cost founders money: a company that has opted for the <strong>22% tax regime cannot claim it</strong>, and <strong>minimum alternate tax</strong> can still be payable in the holiday years. "
          "Choose the three years for when profits are highest, and apply for the certificate well before you need it."),
    sections=[
        ("/ Eligibility", "All of these must be true.",
         table(["Condition", "What the law says"], [
             ["Entity", "Private limited company or LLP. Partnership firms and proprietorships cannot claim it"],
             ["Incorporation date", "On or after 1 April 2016 and before 1 April 2030"],
             ["Business", "Innovation, development or improvement of products, processes or services, or a scalable business model with high potential for jobs or wealth creation"],
             ["Turnover", "INR 100 crore or less in the year for which the deduction is claimed"],
             ["Certificate", "Certificate of eligible business from the Inter-Ministerial Board, in addition to DPIIT recognition"],
             ["Origin", "Not formed by splitting up or reconstructing an existing business, or by moving used plant and machinery into it (imported machinery not used in India is allowed)"],
             ["Years", "Any three consecutive tax years out of the first ten, counting from the year of incorporation"]])
         + '<p>For the year to 31 March 2026 the claim is made under section 80-IAC of the 1961 Act. From the year starting 1 April 2026 it is section 140 of the 2025 Act; a holiday already started continues.</p>'
         + call_box("Startup tax holiday: can we claim it, and when?", ["Whether your company or LLP meets each condition",
                                                                       "Applying for the Inter-Ministerial Board certificate",
                                                                       "Choosing the three years, with MAT and the 22% regime compared",
                                                                       "Turnover close to the INR 100 crore test",
                                                                       "What happens to the holiday on a merger, flip or change of business"],
                    "your incorporation date, entity type, DPIIT number, turnover and profit forecast, and current tax regime.")),
        ("/ The money traps", "MAT and the 22% regime.",
         ul("<strong>22% regime:</strong> a company that opts for the concessional regime (section 115BAA of the 1961 Act, carried into the 2025 Act) gives up most deductions, including this one, and the option cannot be withdrawn. Do not opt in before your holiday years are over if you plan to claim.",
            "<strong>Minimum alternate tax:</strong> in the normal regime a company pays MAT on book profit even when the holiday brings regular tax to nil. The MAT paid becomes a credit that can be used against regular tax in later years.",
            "<strong>Compare both paths:</strong> normal regime with the holiday and MAT, against the 22% regime with no holiday, over five or more years. See <a href=\"how-to-pick-section-115baa-vs-115bab-vs-standard-decision-tree.html\">choosing a tax regime</a> and <a href=\"form-29b-mat-applicability-certificate-india-2026.html\">the MAT certificate</a>.",
            "<strong>LLPs</strong> do not pay MAT but pay alternate minimum tax on the same idea; model it the same way.",
            "<strong>Return on time:</strong> deductions of this kind are claimed in a return filed by the due date; a late return can lose it.")),
        ("/ DPIIT recognition after February 2026", "Recognition is wider than the tax test.",
         ul("<strong>New framework:</strong> DPIIT notification G.S.R. 108(E) of 4 February 2026 replaced the 2019 rules.",
            "<strong>Turnover for recognition:</strong> up to INR 200 crore in any year (it was INR 100 crore).",
            "<strong>Deep tech startups:</strong> a new category recognised for up to 20 years with turnover up to INR 300 crore.",
            "<strong>Age:</strong> 10 years from incorporation for other startups.",
            "<strong>Cooperative societies</strong> can now be recognised.",
            "<strong>But the tax holiday has its own test:</strong> INR 100 crore in the claim year and incorporation before 1 April 2030, as written in section 140. Some reports say the Finance Act, 2026 raised the tax limit to INR 300 crore; the Income Tax Department&rsquo;s published text of section 140 still reads INR 100 crore, so plan on that until it changes.")
         + '<p>Related: <a href="how-to-register-startup-india-dpiit.html">registering with DPIIT</a> &middot; <a href="startup-india-complete-guide.html">Startup India guide</a> &middot; <a href="esop-perquisite-tax-calculator.html">ESOP tax calculator</a> &middot; <a href="which-is-better-llp-vs-private-limited-india.html">LLP or private limited</a>.</p>'
         + sources("Income-tax Act, 2025, section 140, as published by the Income Tax Department (page reviewed 26 October 2026); Income-tax Act, 1961, section 80-IAC as amended by the Finance Act, 2025 (incorporation up to 31 March 2030); DPIIT notification G.S.R. 108(E) dated 4 February 2026, as summarised by Treelife, Lexology and Nasscom; TaxUpdate, &ldquo;Section 80-IAC Startup Tax Holiday for FY 2025-26&rdquo; (12 June 2026). Checked 22 November 2026.")),
    ],
    faqs=[("What is the startup tax holiday in India?", "An eligible startup can deduct 100% of the profits of its eligible business for any three consecutive years out of its first ten years. It was section 80-IAC of the Income-tax Act, 1961 and is section 140 of the Income-tax Act, 2025 from 1 April 2026."),
          ("Who is eligible for section 80-IAC or section 140?", "A private limited company or LLP incorporated on or after 1 April 2016 and before 1 April 2030, engaged in an eligible business, with turnover of INR 100 crore or less in the claim year, holding a certificate from the Inter-Ministerial Board, and not formed by splitting up or reconstructing an existing business."),
          ("Is DPIIT recognition enough to get the tax exemption?", "No. DPIIT recognition is the first step. The tax holiday also needs a certificate of eligible business from the Inter-Ministerial Board."),
          ("Can a startup claim 80-IAC and the 22% tax rate together?", "No. A company that opts for the concessional 22% regime gives up this deduction, and the option cannot be withdrawn."),
          ("Does a startup pay MAT during the tax holiday?", "A company in the normal regime can still owe minimum alternate tax on book profit. The MAT paid is carried forward as a credit against regular tax in later years."),
          ("Is the tax holiday 3 years out of 7 or out of 10?", "Out of 10. The window was extended from seven to ten years from incorporation; the three years must be consecutive."),
        ("What is the difference between sections 80-IA, 80-IAB, 80-IAC and 80-IB?", "They are separate profit-linked deductions. 80-IA covered infrastructure and certain industrial undertakings (now section 138 of the Income-tax Act, 2025), 80-IAB covered developers of special economic zones (now section 139), and 80-IAC covers eligible startups (now section 140). 80-IA and 80-IAB now mainly continue for undertakings that met past start-date cut-offs, and 80-IB covered older categories of industrial undertakings that have largely run out. For a new business today, the startup deduction in section 140 is the one usually still open."),
        ("What is an eligible business for the startup tax holiday?", "A business carried on by a DPIIT-recognised company or LLP that works on innovation, development or improvement of products, processes or services, or a scalable business model with high potential for employment or wealth creation, and that holds a certificate of eligible business from the Inter-Ministerial Board."),
        ("How do I register or apply for the 80-IAC (section 140) tax holiday?", "First get DPIIT recognition on the Startup India portal. Then apply on the same portal for the Inter-Ministerial Board certificate of eligible business, with the incorporation documents, financials and a description of the innovation. Once the certificate is granted, claim the deduction in the return for the three consecutive years you choose within ten years of incorporation."),
          ("What changed for startups in February 2026?", "DPIIT notification G.S.R. 108(E) of 4 February 2026 raised the recognition turnover limit to INR 200 crore, created a deep tech category recognised for 20 years with a INR 300 crore limit, and allowed cooperative societies. The tax holiday keeps its own conditions."),
          ("Can BQP help us claim the startup tax holiday?", "Yes. " + C)],
    related=[("how-to-register-startup-india-dpiit.html", "Registering with DPIIT"),
             ("how-to-pick-section-115baa-vs-115bab-vs-standard-decision-tree.html", "Choosing a tax regime"),
             ("startup-india-complete-guide.html", "Startup India guide")],
    cta_h="Profitable soon, or already? Plan the three years now.", cta_b=C,
    keywords="section 80-IAC, section 140 Income-tax Act 2025, startup tax holiday India, section 80IAC eligibility, startup India tax exemption 3 years, Inter-Ministerial Board certificate, startup tax exemption conditions, 80-IAC MAT, 80-IAC 115BAA, DPIIT 2026 notification 200 crore deep tech",
    desc="Startup tax holiday India (2026): section 80-IAC, now section 140 - 100% of profits for 3 consecutive years out of 10 for a company or LLP incorporated 1 April 2016 to 31 March 2030, turnover up to INR 100 crore, with an IMB certificate. MAT, the 22% regime trap and DPIIT's 2026 rules.",
    howto={"name": "How to claim the startup tax holiday", "description": "Section 80-IAC / section 140.", "steps": [
        {"name": "Get DPIIT recognition", "text": "Online on the Startup India portal."},
        {"name": "Apply for the IMB certificate", "text": "Certificate of eligible business from the Inter-Ministerial Board."},
        {"name": "Stay in the normal regime", "text": "Do not opt for the 22% regime before the holiday years."},
        {"name": "Choose three consecutive years", "text": "Within ten years from incorporation, when profits are highest."},
        {"name": "Claim in an on-time return", "text": "With audited accounts; account for MAT and its credit."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch FK complete")
