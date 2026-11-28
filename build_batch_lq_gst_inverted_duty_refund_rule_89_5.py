# -*- coding: utf-8 -*-
"""Batch LQ (28 Nov 2026): GST refund for an inverted duty structure - when input tax on goods is higher than output tax, the rule
89(5) formula, inputs only (not input services or capital goods), exclusions, the two-year time limit, RFD-01, the 90% provisional
refund, and interest on delay.
Demand: 'inverted duty structure refund', 'gst refund inverted duty formula', 'rule 89(5)', 'inverted duty refund time limit',
'provisional refund inverted duty' - mentioned on the 57th GST Council page, news roundups and the ITC page but no dedicated page.
Manufacturers with a lower output rate (for example after rate cuts) need refund filing help. User steer 26 Nov 2026: more calls.
Facts (CGST Act sections 54 and 56; CGST Rules rules 89(5), 90 and 91): refund of unutilised input tax credit where the tax rate on
inputs is higher than the tax rate on output supplies (section 54(3)(ii)); not where output supplies are nil-rated or fully exempt,
and not for certain notified goods and services; rule 89(5) formula - maximum refund = (turnover of inverted rated supply x net ITC
/ adjusted total turnover) minus (tax payable on the inverted rated supply x net ITC / ITC availed on inputs and input services), as
amended in July 2022; net ITC means credit on inputs only - input services and capital goods are excluded (upheld by the Supreme
Court in VKC Footsteps, 2021); application in RFD-01 within two years from the relevant date (due date of the return for the period);
refund order within 60 days of a complete application, with interest at 6% a year for delay; 90% provisional refund on a risk-based
basis for inverted duty claims - recommended by the 56th GST Council (September 2025), operated from late 2025 and placed in section
54(6) by the Finance Act, 2026, with rule changes effective 1 November 2026 (web search 28 Nov 2026: CAclubindia, Business Standard,
Taxguru; matched to the site's 57th GST Council page). No fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "gst-inverted-duty-structure-refund-rule-89-5-formula-inputs-only-2-years-rfd-01-90-percent-provisional-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the periods you want to claim, your input and output "
     "GST rates, GSTR-3B and GSTR-2B for those periods, a split of credit between inputs, input services and capital goods, and "
     "any earlier refund applications or deficiency memos. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="GST Inverted Duty Structure Refund (2026): Rule 89(5) Formula, Inputs Only, Exclusions, Two-Year Time Limit, RFD-01 and 90% Provisional Refund",
    em="credit stuck because inputs cost more tax than outputs.",
    kicker="/ Manufacturers and traders with a lower output rate &middot; GST refund under section 54(3) &middot; Updated 2026-11-28",
    lead=("<strong>If the GST rate on your inputs is higher than on what you sell, unused credit piles up in your ledger. Section 54(3) lets you claim it back as an inverted duty structure refund. "
          "The rule 89(5) formula counts credit on inputs only - not input services or capital goods. The claim is filed in RFD-01 within two years. "
          "Eligible claims can now get a 90% provisional refund on a risk-based basis.</strong>"),
    sections=[
        ("/ Eligibility and the formula", "Section 54(3)(ii) and rule 89(5).",
         table(["Point", "Rule"], [
             ["When", "Tax rate on inputs is higher than the tax rate on output supplies"],
             ["Not available", "Output supplies that are nil-rated or fully exempt; certain notified goods and services"],
             ["Formula", "(Inverted rated turnover x net ITC / adjusted total turnover) minus (tax on inverted rated supply x net ITC / ITC on inputs and input services)"],
             ["Net ITC", "Credit on inputs only - input services and capital goods are excluded"],
             ["Time limit", "Two years from the relevant date (due date of the return for the period)"],
             ["Form", "RFD-01, with statements of turnover and invoices"],
             ["Provisional refund", "90% on a risk-based basis for eligible inverted duty claims"],
             ["Order and interest", "Within 60 days of a complete application; interest at 6% a year for delay"]])
         + ul("<strong>Inputs only:</strong> the Supreme Court upheld excluding input services from net ITC (VKC Footsteps, 2021), so a business whose credit is mainly on services gets a smaller refund.",
              "<strong>Rate changes:</strong> when output rates are cut, an inverted structure can start overnight - check from the period of the change.")),
        ("/ Getting the refund paid", "Where claims are cut or rejected.",
         ul("<strong>Split your credit:</strong> tag credit as inputs, input services or capital goods in your books; the formula depends on it.",
            "<strong>Match GSTR-2B:</strong> only credit reflected in GSTR-2B and claimed in GSTR-3B counts.",
            "<strong>Period planning:</strong> claim period by period within the financial year, and track the two-year deadline for each period.",
            "<strong>Deficiency memos and show cause notices:</strong> reply with the working, invoices and rate evidence; a rejected claim can be appealed.",
            "<strong>Same rate, different items:</strong> refund is not allowed where input and output rates are the same and the accumulation arises from other reasons.")
         + call_box("an inverted duty refund", ["Eligibility and rate analysis",
                                                "Rule 89(5) computation with inputs-only net ITC",
                                                "RFD-01 and supporting statements",
                                                "Replies to deficiency memos and notices",
                                                "Appeals against rejection"],
                    "Periods, input and output rates, GSTR-3B and 2B, credit split, earlier claims.")
         + sources("CGST Act, 2017 (sections 54 and 56, as amended by the Finance Act, 2026); CGST Rules, 2017 (rules 89(5), 90 and 91); Supreme Court, Union of India v. VKC Footsteps India (2021); GST Council 56th meeting recommendations; site GST refund for exporters, 57th GST Council and input tax credit pages.")),
    ],
    faqs=[("What is an inverted duty structure refund under GST?", "A refund of unutilised input tax credit where the GST rate on inputs is higher than the rate on output supplies, allowed under section 54(3)(ii) of the CGST Act and computed with the rule 89(5) formula."),
          ("Is credit on input services included in an inverted duty refund?", "No. Net ITC for the formula means credit on inputs (goods) only. Input services and capital goods are excluded, and the Supreme Court upheld this in VKC Footsteps (2021)."),
          ("What is the time limit for an inverted duty refund?", "The application in RFD-01 must be filed within two years from the relevant date, which is the due date of the return for the period of the claim."),
          ("Is there a provisional refund for inverted duty claims?", "Yes. Eligible inverted duty claims can get a 90% provisional refund on a risk-based basis, a facility recommended by the 56th GST Council and later placed in section 54(6) by the Finance Act, 2026."),
          ("When is inverted duty refund not allowed?", "Where output supplies are nil-rated or fully exempt, for certain notified goods and services, and where the accumulation is not because of a higher input rate."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the periods, input and output rates, GSTR-3B and GSTR-2B, credit split between inputs, services and capital goods, and any earlier claims. Or book a call directly.")],
    related=[("gst-refund-for-exporters-igst-paid-or-lut-unused-itc-rfd-01-shipping-bill-time-limit-documents-2026.html", "GST refund for exporters"),
             ("gst-changes-from-1-november-2026-57th-gst-council-cbic-circulars.html", "GST changes from 1 November 2026"),
             ("what-is-input-tax-credit-and-how-to-claim-india-gst.html", "What is input tax credit"),
             ("gst-appeal-apl-01-section-107-time-limit-pre-deposit-format-appellate-authority-2026.html", "GST appeal (APL-01)")],
    cta_h="Credit piling up in your GST ledger?", cta_b=C,
    keywords="inverted duty structure refund, gst refund inverted duty formula, rule 89(5), inverted duty refund time limit 2 years, provisional refund inverted duty 90 percent, vkc footsteps input services, rfd-01 inverted duty",
    desc="GST inverted duty structure refund: unused ITC where input rate exceeds output rate, rule 89(5) formula with net ITC on inputs only (VKC Footsteps), exclusions, RFD-01 within two years, 90% risk-based provisional refund, order in 60 days with 6% interest for delay.",
    howto={"name": "How to claim an inverted duty refund", "description": "From analysis to order.", "steps": [
        {"name": "Confirm the inversion", "text": "Input rate higher than output rate; output not nil-rated or exempt."},
        {"name": "Split credit", "text": "Inputs vs input services vs capital goods; match with GSTR-2B."},
        {"name": "Compute and file", "text": "Rule 89(5) formula; RFD-01 within two years for each period."},
        {"name": "Follow through", "text": "Track provisional refund; reply to deficiency memos; appeal if rejected."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LQ complete")
