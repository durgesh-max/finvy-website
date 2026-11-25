# -*- coding: utf-8 -*-
"""Batch IW (25 Nov 2026): Startup India Seed Fund Scheme (SISFS) 2026 - status and alternatives. SISFS gives up to
Rs 20 lakh grant for proof of concept / prototype / trials and up to Rs 50 lakh as debt or convertible debentures for
market entry and scale-up, routed through selected incubators (about 217-219 incubators; corpus Rs 945 crore committed);
for DPIIT-recognised startups incorporated not more than about two years before applying; the 2026 call closed in May
2026 per guides (final extended deadline reported as 15 or 31 May 2026), with no new call announced as of October 2026;
the scheme was extended to complete disbursements. Alternatives: Fund of Funds for Startups 2.0 (Rs 10,000 crore,
notified April 2026, invests through SEBI-registered AIFs), Credit Guarantee Scheme for Startups, state seed funds,
section 80-IAC, angel and VC rounds.
Demand: sweep ac115 (25 Nov 2026), all 7 markets: "startup india seed fund scheme", "startup india scheme",
"startup india portal".
Facts (checked 25 Nov 2026): Startup India Schemes Playbook (June 2026), Startupflora and Startupgrantsindia (2026
deadline), Bajaj Finserv (April 2026), Taxtmi, News on AIR (Fund of Funds 2.0, April 2026); site DPIIT pages."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 25 November 2026."
SLUG = "startup-india-seed-fund-scheme-sisfs-2026-status-20-lakh-grant-50-lakh-debt-eligibility-alternatives"

C = contact("your incorporation date, DPIIT recognition number, stage (idea, prototype, revenue), funding raised so far and the amount you need")
L = lambda h, t: f'<a href="{h}">{t}</a>'
PAGES = [dict(
    slug=SLUG,
    title="Startup India Seed Fund Scheme (SISFS) 2026: Is It Still Open, Rs 20 Lakh Grant and Rs 50 Lakh Debt, Eligibility and Alternatives",
    em="check the call is open before you build the application.",
    kicker="/ Early-stage founders &middot; Startup funding &middot; Updated 2026-11-25",
    lead=("<strong>The Startup India Seed Fund Scheme offers DPIIT-recognised startups up to &#8377;20 lakh as a grant for proof of concept and up to &#8377;50 lakh as debt or convertible debentures for market entry, through selected incubators rather than directly from the government.</strong> "
          "The 2026 application window closed in May 2026 according to published guides, and no new call had been announced as of October 2026, although the scheme was extended to finish disbursements. "
          "Founders should check the Seed Fund portal for a new call and line up alternatives such as Fund of Funds 2.0 investors, state seed funds and angel rounds."),
    sections=[
        ("/ The scheme at a glance", "What SISFS offers.",
         table(["Point", "Detail"], [
             ["Grant", "Up to &#8377;20 lakh for proof of concept, prototype development or product trials"],
             ["Debt / convertible debentures", "Up to &#8377;50 lakh for market entry, commercialisation or scale-up"],
             ["Routed through", "Selected incubators (over 200 across India); you apply to incubators on the Seed Fund portal"],
             ["Who can apply", "DPIIT-recognised startups incorporated about two years or less before applying, with a scalable, technology-led business"],
             ["Each form of support", "Available once per startup"],
             ["2026 status", "Applications closed in May 2026 per published guides; no new call announced as of October 2026"]])
         + '<p>Get recognised first: see ' + L("how-to-register-startup-india-dpiit.html", "Startup India (DPIIT) registration") + ' and ' + L("what-is-dpiit-recognition.html", "what DPIIT recognition gives you") + '.</p>'),
        ("/ If the call is closed: alternatives", "Other routes to early capital.",
         ul("<strong>Fund of Funds for Startups 2.0:</strong> a &#8377;10,000 crore corpus notified in April 2026 that invests through SEBI-registered alternative investment funds, so startups raise from those funds rather than from the government.",
            "<strong>State startup policies:</strong> many states run their own seed grants, sustenance allowances and incubator programmes.",
            "<strong>Angel and seed rounds:</strong> priced equity, convertible notes or CCPS; see " + L("how-to-raise-seed-funding-india-startup.html", "how to raise seed funding") + ".",
            "<strong>Credit Guarantee Scheme for Startups:</strong> collateral-free debt from lenders backed by a government guarantee.",
            "<strong>Tax holiday:</strong> eligible DPIIT startups can apply for the section 80-IAC deduction; see " + L("best-ca-dpiit-startup-india-80-iac-application.html", "DPIIT and 80-IAC applications") + ".",
            "<strong>Full scheme list:</strong> see the " + L("startup-india-complete-guide.html", "Startup India complete guide") + ".")
         + call_box("Startup funding readiness", ["DPIIT recognition and 80-IAC",
                                                   "Seed fund and incubator applications",
                                                   "Investor-ready financials and cap table",
                                                   "FEMA filings for foreign investment",
                                                   "Valuation and share allotment"],
                    "your stage and funding plan.")
         + sources("Startup India Seed Fund Scheme guidelines and Seed Fund portal; Startup India Schemes Playbook (June 2026); Startupflora and Startupgrantsindia notes on the 2026 deadline; Bajaj Finserv (April 2026); Taxtmi; News on AIR on Fund of Funds 2.0 (April 2026); site DPIIT guides. Checked 25 November 2026.")),
    ],
    faqs=[("What is the Startup India Seed Fund Scheme?", "A government scheme that funds early-stage DPIIT-recognised startups through selected incubators: up to Rs 20 lakh as a grant for proof of concept and up to Rs 50 lakh as debt or convertible debentures for market entry and scale-up."),
          ("Is the Startup India Seed Fund Scheme still open in 2026?", "Published guides say the 2026 application window closed in May 2026 and no new call had been announced as of October 2026, although the scheme was extended to complete disbursements. Check the Seed Fund portal for any new call."),
          ("Who is eligible for SISFS?", "DPIIT-recognised startups incorporated about two years or less before applying, with a scalable business that uses technology in its product, service or delivery. Check the current guidelines for detailed conditions."),
          ("How do I apply for the Seed Fund?", "When a call is open, register on the Seed Fund portal with your DPIIT recognition details and apply to up to three incubators, who evaluate and disburse the funds."),
          ("What can I do if SISFS is closed?", "Look at funds backed by Fund of Funds 2.0, state seed grants, angel and seed rounds, the Credit Guarantee Scheme for Startups and the section 80-IAC tax holiday."),
          ("Can BQP help a startup become funding-ready?", "Yes. CA Durgesh Chavda can handle DPIIT recognition, 80-IAC, incubator and investor documentation, valuation and FEMA filings. " + C)],
    related=[("how-to-register-startup-india-dpiit.html", "Startup India (DPIIT) registration"),
             ("what-is-dpiit-recognition.html", "What is DPIIT recognition?"),
             ("how-to-raise-seed-funding-india-startup.html", "How to raise seed funding"),
             ("best-ca-dpiit-startup-india-80-iac-application.html", "DPIIT and 80-IAC applications"),
             ("startup-india-complete-guide.html", "Startup India complete guide")],
    cta_h="Raising your first money?", cta_b=C,
    keywords="startup india seed fund scheme, sisfs 2026, startup india seed fund last date, seed fund scheme eligibility, startup india seed fund 20 lakh 50 lakh, startup india scheme, fund of funds 2.0, startup india portal",
    desc="Startup India Seed Fund Scheme (SISFS) 2026: up to Rs 20 lakh grant and Rs 50 lakh debt through incubators for DPIIT startups, eligibility, whether the call is open (closed May 2026 per guides), and alternatives including Fund of Funds 2.0.",
    howto={"name": "How to approach Startup India seed funding", "description": "For early-stage founders.", "steps": [
        {"name": "Get DPIIT recognition", "text": "Free registration on the Startup India portal."},
        {"name": "Check the Seed Fund portal", "text": "Confirm whether a call is open."},
        {"name": "Shortlist incubators", "text": "Apply to up to three that fit your sector."},
        {"name": "Prepare the proposal", "text": "Proof of concept plan, milestones and use of funds."},
        {"name": "Line up alternatives", "text": "AIFs, state grants, angels and 80-IAC."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch IW complete")
