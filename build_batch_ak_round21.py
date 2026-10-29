# -*- coding: utf-8 -*-
"""Batch AK: Round 21 - DIR-3 KYC now once every three years (G.S.R. 943(E), effective 31 March 2026): rewrite two pages, redirect one."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SRC = ('<p><strong>Sources:</strong> <a href="https://blog.instafinancials.com/2026/04/06/new-mca-rules-for-directors-kyc/" rel="nofollow noopener" target="_blank">InstaFinancials</a>; '
       '<a href="https://www.taxaj.com/learn/?p=372" rel="nofollow noopener" target="_blank">TaxAJ</a>; '
       '<a href="https://ebizfiling.com/blog/mca-revises-dir-3-kyc-norms/" rel="nofollow noopener" target="_blank">Ebizfiling</a>.</p>'
       '<p><em>Last updated: 29 October 2026. Sources differ on how the three-year cycle is counted for each DIN; confirm your next due year on the MCA portal.</em></p>')


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


PAGES = [
    dict(
        slug="dir-3-kyc-director-annual-compliance-india",
        title="DIR-3 KYC 2026: Now Once Every Three Years, Due 30 June",
        em="the annual filing is gone.",
        kicker="/ MCA &middot; Director KYC &middot; Updated 2026-10-29",
        lead="Director KYC is no longer annual. Under G.S.R. 943(E), dated 31 December 2025 and effective 31 March 2026, every DIN holder files DIR-3 KYC once every three consecutive financial years, by 30 June of the due year, instead of every year by 30 September. Changes to your mobile number, email or residential address must be reported within 30 days. There is no 30 September 2026 deadline.",
        sections=[
            ("/ What changed", "Old rule vs new rule.",
             "<table><thead><tr><th></th><th>Until FY 2025-26</th><th>From 31 March 2026</th></tr></thead><tbody>"
             "<tr><td>Frequency</td><td>Every financial year</td><td>Once every three consecutive financial years</td></tr>"
             "<tr><td>Due date</td><td>30 September</td><td>30 June of the due year</td></tr>"
             "<tr><td>Change in mobile, email or address</td><td>Reported in the next annual KYC</td><td>Reported within 30 days; does not reset the three-year cycle</td></tr>"
             "<tr><td>Form</td><td>DIR-3 KYC eForm or Web</td><td>Primarily DIR-3 KYC Web on the MCA portal</td></tr>"
             "<tr><td>Missed filing</td><td>DIN deactivated; INR 5,000 to reactivate</td><td>Same</td></tr></tbody></table>"
             "<p>Forms left in draft or pending payment on the MCA portal before 31 March 2026 were cancelled and must be filed again.</p>"),
            ("/ What you need to do", "By situation.",
             ul("<strong>Filed KYC for FY 2025-26</strong>: nothing more is needed for FY 2026-27 or FY 2027-28 unless your contact details change. Check your next due year on the MCA portal.",
                "<strong>Changed mobile number, email or address</strong>: update within 30 days of the change.",
                "<strong>New DIN</strong>: your first KYC falls due in the year your three-year cycle ends; diarise it when the DIN is allotted.",
                "<strong>DIN already deactivated for an earlier missed filing</strong>: file the pending KYC with the INR 5,000 fee to reactivate before signing any MCA form.",
                "<strong>Foreign directors</strong>: the same rule applies; keep the registered mobile and email reachable from abroad, because the Web filing uses OTPs.")),
            ("/ Why it matters", "DIN status blocks company filings.",
             ul("A deactivated DIN cannot sign AOC-4, MGT-7, DIR-12 or other MCA forms, and the director cannot be appointed elsewhere.",
                "Investors and lenders check DIN status in due diligence.",
                "Directors of companies that stop filing accounts for three years face disqualification under Section 164(2), which is a separate issue from KYC.") + SRC),
        ],
        faqs=[
            ("Is DIR-3 KYC still annual?", "No. From 31 March 2026, under G.S.R. 943(E), DIR-3 KYC is filed once every three consecutive financial years, by 30 June of the due year."),
            ("Is there a DIR-3 KYC deadline on 30 September 2026?", "No. The 30 September annual deadline no longer applies. Directors who filed for FY 2025-26 need not file for FY 2026-27 or FY 2027-28 unless their details change."),
            ("What if my mobile number or email changes?", "Update your KYC within 30 days of the change on the MCA portal. This does not reset your three-year cycle."),
            ("What happens if I miss my DIR-3 KYC?", "Your DIN is deactivated and you cannot sign MCA filings. Reactivation needs the pending KYC and a fee of INR 5,000."),
            ("Can BQP track DIR-3 KYC for our directors?", "Yes, including foreign directors: due-year tracking, change updates and reactivation. " + CONTACT),
        ],
        related=[("dir-3-kyc-deactivated-mca-filings-blocked-urgent-india.html", "DIN deactivated? Reactivation"), ("aoc-4-filing-deadline-30-october-2026-late-fee-india.html", "AOC-4 deadline")],
        cta_h="Director KYC or DIN status questions?", cta_b=CONTACT,
        keywords="DIR-3 KYC 2026, DIR-3 KYC every 3 years, DIR-3 KYC due date 30 June, GSR 943(E) DIR-3 KYC, DIR-3 KYC new rules 2026, is DIR-3 KYC annual",
        desc="DIR-3 KYC is now filed once every three financial years by 30 June (G.S.R. 943(E), effective 31 March 2026), not annually by 30 September. Contact-detail changes within 30 days; INR 5,000 to reactivate a deactivated DIN.",
    ),
    dict(
        slug="dir-3-kyc-deactivated-mca-filings-blocked-urgent-india",
        title="DIN Deactivated for DIR-3 KYC? How to Reactivate It in 2026",
        em="and unblock your company's MCA filings.",
        kicker="/ MCA &middot; DIN Reactivation &middot; Updated 2026-10-29",
        lead="A DIN marked 'Deactivated due to non-filing of DIR-3 KYC' cannot sign any MCA form, so AOC-4, MGT-7 and other filings stop. Many DINs were deactivated for missing the annual KYC under the old rules. Reactivation means filing the pending KYC with the INR 5,000 fee. Under the 2026 rules, KYC is then due only once every three years, plus within 30 days of any change in contact details.",
        sections=[
            ("/ What is blocked", "While the DIN is deactivated.",
             ul("The director cannot sign MCA forms: AOC-4, MGT-7/7A, DIR-12, PAS-3, PAS-6, MSME Form I, DPT-3, CHG-1 and others.",
                "The director cannot be appointed to another company.",
                "The company's own deadlines keep running, so late fees on AOC-4 and MGT-7 build up at INR 100 per day each.")),
            ("/ How to reactivate", "Steps.",
             "<ol><li>Log in to the MCA portal and check the DIN status and the KYC period shown as pending.</li>"
             "<li>Make sure the registered mobile number and email are working, since filing uses OTPs; if they changed, update them as part of the KYC.</li>"
             "<li>File the pending DIR-3 KYC and pay the INR 5,000 fee.</li>"
             "<li>Once the DIN shows as active, file the company's pending forms, starting with AOC-4 and MGT-7.</li>"
             "<li>Note your next KYC due year under the three-year cycle and set a reminder before 30 June of that year.</li></ol>"),
            ("/ Under the 2026 rules", "What changes after reactivation.",
             ul("KYC is due once every three consecutive financial years, by 30 June of the due year (G.S.R. 943(E), effective 31 March 2026).",
                "Mobile, email or address changes must be reported within 30 days.",
                f'Full explanation: <a href="dir-3-kyc-director-annual-compliance-india.html">DIR-3 KYC now once every three years</a>.') + SRC),
        ],
        faqs=[
            ("How do I reactivate a deactivated DIN?", "File the pending DIR-3 KYC on the MCA portal and pay the INR 5,000 fee. The DIN becomes active once the filing is processed."),
            ("Can a director with a deactivated DIN sign AOC-4 or MGT-7?", "No. The DIN must be active before the director can sign any MCA form."),
            ("Do I have to file DIR-3 KYC every year after reactivation?", "No. From 31 March 2026 KYC is due once every three financial years, by 30 June, plus within 30 days of any change in contact details."),
            ("Can BQP reactivate a foreign director's DIN?", "Yes, working remotely with the director on OTP verification and then filing the company's pending forms. " + CONTACT),
        ],
        related=[("dir-3-kyc-director-annual-compliance-india.html", "DIR-3 KYC 2026 rules"), ("mgt-7-mgt-7a-annual-return-29-november-2026-india.html", "MGT-7 due 29 November")],
        cta_h="DIN deactivated and filings stuck?", cta_b=CONTACT,
        keywords="DIN deactivated reactivate 2026, DIR-3 KYC deactivated DIN, reactivate DIN INR 5000, DIN deactivated due to non-filing of DIR-3 KYC, director KYC late fee",
        desc="How to reactivate a DIN deactivated for non-filing of DIR-3 KYC: file the pending KYC with the INR 5,000 fee, then file blocked AOC-4/MGT-7. From 31 March 2026, KYC is due once every three years by 30 June.",
    ),
]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"],
                hero_kicker=p["kicker"], hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>',
                hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]],
                cta_headline=p["cta_h"], cta_body=p["cta_b"])
    write_page(p["slug"], html)

REDIRECT_FROM = "dir-3-kyc-catch-up-november-december-2026"
REDIRECT_TO = "dir-3-kyc-director-annual-compliance-india.html"
with open(REDIRECT_FROM + ".html", "w", encoding="utf-8", newline="") as fh:
    fh.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DIR-3 KYC 2026: Now Once Every Three Years - BQP</title>
<link rel="canonical" href="https://bharatquantumprospera.com/{REDIRECT_TO}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={REDIRECT_TO}">
</head><body><p>DIR-3 KYC is no longer annual. This page has moved to <a href="{REDIRECT_TO}">DIR-3 KYC 2026: now once every three years</a>.</p></body></html>
""")

print(f"Batch AK complete: {len(PAGES)} pages rewritten, 1 redirect")
