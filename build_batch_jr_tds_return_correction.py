# -*- coding: utf-8 -*-
"""Batch JR (27 Nov 2026): TDS return correction - correction statements online on TRACES or with the consolidated
file (RPU / FVU), the two-year time limit under the Income-tax Act, 2025 and common errors.
Demand: sweep ac131 (27 Nov 2026), all 7 markets: "tds return correction", "tds return correction time limit / last date /
due date", "tds return correction utility", "tds return correction in new traces portal", "tds return correction online /
offline", "tds return correction fy 2026-27"; no page title targeted corrections.
User steer 26 Nov 2026: more call bookings / WhatsApp enquiries - deductors with errors need a correction filed.
Facts (verified 27 Nov 2026): Finance (No. 2) Act, 2024 set a six-year limit for correction statements from 1 April 2025;
under the Income-tax Act, 2025 (section 397(3)(f)), from 1 April 2026 a correction statement can be filed only within two
years from the end of the tax year in which the original statement was required to be delivered (CBDT advisory; older
quarters had transition cut-offs - exact dates not restated here); corrections are prepared from the consolidated file
downloaded from TRACES using the Return Preparation Utility and validated with the File Validation Utility, then uploaded
quoting the original token number; some fixes (challan re-tagging, PAN corrections) can be made online on TRACES; site
TDS default page for passwords / interest / late fee. No fees, no timings, no office claims."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources, contact
from build_lib import page, write_page

A.UPDATED = "Last updated: 27 November 2026."
SLUG = "tds-return-correction-statement-online-traces-conso-file-rpu-fvu-two-year-time-limit-common-errors-2026"

C = contact("your TAN, the form and quarter, the token number of the original statement, the default summary or justification report from TRACES, the challans, and the list of deductees with the correct PANs and amounts")
PAGES = [dict(
    slug=SLUG,
    title="TDS Return Correction (2026): How to File a Correction Statement Online on TRACES or With the Conso File (RPU / FVU), the Two-Year Time Limit and Common Errors",
    em="fix it while the window is open.",
    kicker="/ Companies, firms, tenants and property buyers &middot; TRACES &middot; Updated 2026-11-27",
    lead=("<strong>A TDS return correction (correction statement) fixes errors in a TDS or TCS statement already filed - a wrong PAN, an untagged challan, a missing deductee, a wrong amount or section, or a lower certificate not quoted.</strong> "
          "Until it is corrected, deductees may not see their tax credit in Form 168 (old 26AS) and the deductor may face a default notice. "
          "From 1 April 2026 the window is short: a correction can be filed only within two years from the end of the tax year in which the original statement was due."),
    sections=[
        ("/ When you need a correction", "The usual errors.",
         table(["Error", "Effect", "Fix"], [
             ["Wrong or invalid PAN", "Deductee does not get credit; higher-rate default", "PAN correction (online on TRACES or in the correction file)"],
             ["Challan not tagged or wrong challan", "Short payment default", "Re-tag or add the challan"],
             ["Deductee missing or wrong amount", "Credit missing or wrong in Form 168", "Add or edit the deductee row"],
             ["Wrong section or rate", "Short deduction default", "Correct the section / rate, or pay the difference"],
             ["Lower certificate not quoted", "Short deduction default", "Quote the Form 128 (old Form 13) certificate number"]])),
        ("/ How to file it", "Online on TRACES, or with the consolidated file.",
         ul("<strong>Online on TRACES:</strong> some fixes, such as re-tagging challans and correcting PANs, can be made online after logging in to TRACES with your TAN, without preparing a full file.",
            "<strong>Offline (most corrections):</strong> request the consolidated (conso) file for the form and quarter on TRACES, open it in the Return Preparation Utility (RPU), make the corrections, validate the file with the File Validation Utility (FVU), and upload the correction statement quoting the token number of the original statement.",
            "<strong>Pay what is due first:</strong> if the correction shows short payment, interest or late fee, pay it by challan and include the challan in the correction.",
            "<strong>Check after processing:</strong> download the new default summary from TRACES and confirm the deductees can see the credit in Form 168 (old 26AS).")),
        ("/ The time limit", "Two years under the 2025 Act.",
         ul("<strong>From 1 April 2026:</strong> under section 397(3)(f) of the Income-tax Act, 2025, a correction statement can be filed only within two years from the end of the tax year in which the original statement was required to be delivered.",
            "<strong>Before that:</strong> the Finance (No. 2) Act, 2024 had set a six-year limit from 1 April 2025, and the CBDT announced transition cut-offs for older quarters - if your correction relates to an old quarter, check whether the window has already closed.",
            "<strong>Why it matters:</strong> once the window closes, a deductee who lost credit has to rely on other remedies, and the deductor cannot clear the default by correcting the statement.")
         + call_box("TDS corrections", ["Reading the default summary and justification report",
                                        "Conso file, RPU and FVU corrections",
                                        "Online PAN and challan corrections on TRACES",
                                        "Paying short payment, interest and late fee",
                                        "Property buyer (Form 141) and NRI-payment (Form 144) corrections"],
                    "TAN, form, quarter and the original token number.")
         + sources("Income-tax Act, 2025 (section 397(3)(f)); Income-tax Act, 1961 (section 200(3) as amended by the Finance (No. 2) Act, 2024); CBDT advisory on the time limit for correction statements; TRACES and Protean RPU / FVU guidance; site TDS default and TDS return guides. Checked 27 November 2026.")),
    ],
    faqs=[("What is a TDS return correction?", "A correction statement filed to fix errors in a TDS or TCS statement already filed - wrong PANs, untagged challans, missing deductees, wrong amounts or sections, or a lower certificate not quoted - so that deductees get their credit and defaults are cleared."),
          ("What is the time limit for a TDS return correction?", "From 1 April 2026, under section 397(3)(f) of the Income-tax Act, 2025, a correction statement can be filed only within two years from the end of the tax year in which the original statement was due. Older quarters had transition cut-offs, so check whether the window for an old quarter has already closed."),
          ("How do I file a TDS correction statement?", "For most corrections, request the consolidated file on TRACES, make the changes in the Return Preparation Utility, validate with the File Validation Utility and upload the correction statement with the original token number. Some fixes, such as challan re-tagging and PAN corrections, can be made online on TRACES."),
          ("Can I correct a TDS return online on TRACES?", "Some corrections, such as re-tagging challans and correcting PANs, can be made online on TRACES with your TAN login. Other changes, such as adding deductees or changing amounts, are usually done through a correction file prepared from the consolidated file."),
          ("Does a correction remove the late filing fee?", "No. A correction fixes the content of the statement; a late original statement still carries the late fee, and a correction that reveals short payment or late payment brings interest that must be paid by challan."),
          ("What should I send to get a TDS return corrected?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with your TAN, the form and quarter, the original token number, the default summary or justification report from TRACES, the challans, and the correct PANs and amounts for each deductee. We check what can still be corrected, prepare the correction and file it."),
          ("Can BQP correct TDS returns for my company or property purchase?", "Yes. CA Durgesh Chavda works online with companies, foreign subsidiaries, tenants and property buyers. " + C)],
    related=[("tds-default-notice-traces-default-summary-password-how-to-clear-short-payment-interest-late-fee-2026.html", "TDS default notice"),
             ("tds-return-filing-fy-2026-27-due-dates-form-138-140-144-143-process-late-fee.html", "TDS return filing FY 2026-27"),
             ("form-16a-now-form-131-tds-certificate-2026-download-traces-due-dates-form-130-vs-131.html", "Form 131 (old 16A) certificates"),
             ("nil-lower-tds-certificate-form-128-formerly-form-13-section-395-how-to-apply-2026.html", "Form 128 lower TDS certificate"),
             ("buying-property-from-nri-no-tan-form-141-from-1-october-2026.html", "Buying property from an NRI: Form 141")],
    cta_h="TDS return needs correcting?", cta_b=C,
    keywords="tds return correction, tds correction statement, tds return correction time limit, tds return correction last date, tds return correction utility, tds return correction online traces, tds return correction offline rpu fvu, tds correction fy 2026-27",
    desc="TDS return correction: when you need a correction statement, how to file it online on TRACES or with the consolidated file (RPU / FVU), the two-year time limit under section 397(3)(f) of the Income-tax Act, 2025, and the common errors that cause defaults.",
    howto={"name": "How to file a TDS correction statement", "description": "From the conso file to a cleared default.", "steps": [
        {"name": "Find the errors", "text": "Download the default summary or justification report from TRACES."},
        {"name": "Get the conso file", "text": "Request the consolidated file for the form and quarter on TRACES."},
        {"name": "Correct and validate", "text": "Make the changes in the RPU and validate with the FVU."},
        {"name": "Upload and check", "text": "Upload with the original token number and check the new default summary."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch JR complete")
