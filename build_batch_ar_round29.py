# -*- coding: utf-8 -*-
"""Batch AR: Round 29 - old vs new income tax form numbers (Income-tax Rules, 2026) with a lookup box."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# (old, new, purpose, who uses it)
FORMS = [
    ("15CA", "145", "Information on remittance to a non-resident", "Anyone paying a non-resident or sending money abroad"),
    ("15CB", "146", "Chartered accountant's certificate for a foreign remittance", "Remitters needing a CA certificate"),
    ("10F", "41", "Information for claiming tax treaty (DTAA) benefits", "Non-residents claiming treaty rates"),
    ("67", "44", "Foreign tax credit claim", "Residents with foreign income taxed abroad"),
    ("13", "128", "Application for lower or nil TDS certificate", "NRIs selling property, non-residents with Indian income"),
    ("27Q", "144", "Quarterly TDS return for payments to non-residents", "Buyers, companies and firms paying non-residents"),
    ("26QB / 26QC / 26QD / 26QE", "141", "TDS on property, rent and certain payments (PAN-based)", "Property buyers, tenants, individuals paying contractors"),
    ("24Q", "138", "Quarterly TDS return for salary", "Employers"),
    ("26Q", "140", "Quarterly TDS return for other resident payments", "Businesses deducting TDS"),
    ("27EQ", "143", "Quarterly TCS return", "Collectors of TCS"),
    ("16", "130", "Salary TDS certificate", "Employees"),
    ("16A", "131", "Non-salary TDS certificate", "Payees of TDS"),
    ("26AS", "168", "Annual tax statement", "All taxpayers"),
    ("3CA / 3CB / 3CD", "26", "Tax audit report", "Businesses and professionals under audit"),
    ("3CEB", "48", "Transfer pricing accountant's report", "Companies with international or specified domestic transactions"),
    ("15G / 15H", "121", "Declaration for receiving income without TDS", "Residents with income below the taxable limit"),
    ("49A", "93 / 94", "PAN application: Indian individuals / Indian entities", "New PAN applicants"),
    ("49AA", "95 / 96", "PAN application: foreign individuals / foreign entities", "Foreign citizens, OCIs, foreign companies"),
    ("49B", "134", "TAN application", "Deductors"),
    ("35", "99", "Appeal to the Commissioner (Appeals)", "Taxpayers appealing an order"),
    ("36", "115", "Appeal to the ITAT", "Taxpayers appealing to the Tribunal"),
    ("61A", "165", "Statement of financial transactions (SFT)", "Reporting entities"),
]

rows = "".join(f'<tr data-k="{o.lower()} {n.lower()} {p.lower()}"><td>Form {o}</td><td><strong>Form {n}</strong></td><td>{p}</td><td>{w}</td></tr>' for o, n, p, w in FORMS)
LOOKUP = ('<p><label for="fq"><strong>Search a form</strong> (old number, new number or purpose):</label><br>'
          '<input id="fq" type="search" placeholder="e.g. 15CA, 10F, PAN, property" style="width:100%;max-width:420px;padding:10px 12px;border:1px solid #ccc;border-radius:6px;font:inherit;margin-top:6px" /></p>'
          f'<table id="ft"><thead><tr><th>Old form</th><th>New form</th><th>What it is</th><th>Who uses it</th></tr></thead><tbody>{rows}</tbody></table>'
          '<p id="fnone" style="display:none">No match. Try another word.</p>'
          '<script>(function(){var q=document.getElementById("fq"),rs=[].slice.call(document.querySelectorAll("#ft tbody tr")),n=document.getElementById("fnone");'
          'q.addEventListener("input",function(){var t=q.value.toLowerCase().replace(/^form\\s*/,"").trim(),c=0;rs.forEach(function(r){var s=!t||r.getAttribute("data-k").indexOf(t)>-1;r.style.display=s?"":"none";if(s)c++;});n.style.display=c?"none":"";});})();</script>')

sections = [
    ("/ Lookup", "Old form, new form.", LOOKUP),
    ("/ Which numbers apply when", "The rule of thumb.",
     ul("The Income-tax Act, 2025 and the Income-tax Rules, 2026 apply from 1 April 2026. Transactions and filings for tax year 2026-27 onwards use the new numbers.",
        "Returns, audits and transfer pricing reports for FY 2025-26 (AY 2026-27), due in 2026, are still under the 1961 Act and use the old forms, such as Form 3CEB and Form 3CD.",
        "Foreign remittances made from 1 April 2026 are reported in Form 145, with a CA certificate in Form 146 where required.",
        "Due dates and the basic purpose of most forms did not change; the numbers and section references did.",
        "Old forms remain relevant for corrections and proceedings for earlier years.")),
    ("/ For NRIs and foreign companies", "The forms you are most likely to meet.",
     ul("<strong>Sending or receiving money across borders</strong>: Form 145 (was 15CA) and Form 146 (was 15CB).",
        "<strong>Claiming treaty rates</strong>: Form 41 (was 10F), plus a tax residency certificate.",
        "<strong>Selling property in India as an NRI</strong>: Form 128 (was 13) for a lower TDS certificate; the buyer deducts TDS using PAN in Form 141 from 1 October 2026.",
        "<strong>Paying a non-resident</strong>: TDS return in Form 144 (was 27Q).",
        "<strong>Foreign company or foreign individual needing a PAN</strong>: Form 96 or Form 95 (was 49AA).",
        "<strong>Indian subsidiary of a foreign group</strong>: transfer pricing report in Form 48 (was 3CEB) from tax year 2026-27.") +
     '<p><strong>Sources:</strong> <a href="https://taxguru.in/income-tax/old-vs-new-income-tax-forms-mapping-commonly-used-form.html" rel="nofollow noopener" target="_blank">TaxGuru: old vs new income tax forms</a>; '
     '<a href="https://tax2win.in/guide/income-tax-forms-2026-old-vs-new-list" rel="nofollow noopener" target="_blank">Tax2win: new form list</a>.</p>'
     "<p><em>Last updated: 30 October 2026. Check the form on the e-filing portal before filing.</em></p>"),
]

faqs = [
    ("What is the new number for Form 15CA and 15CB?", "From 1 April 2026, Form 15CA is Form 145 and Form 15CB is Form 146 under the Income-tax Rules, 2026."),
    ("What is the new number for Form 10F?", "Form 41. Non-residents use it to give the information needed to claim tax treaty (DTAA) benefits."),
    ("What replaced Form 27Q?", "Form 144, the quarterly TDS return for payments to non-residents."),
    ("What is Form 128?", "The application for a lower or nil TDS certificate, which replaced Form 13. NRIs selling property commonly use it."),
    ("Is Form 3CEB still used?", "Yes, for FY 2025-26 (AY 2026-27). From tax year 2026-27 the transfer pricing report is Form 48."),
    ("What is the new number for Form 26AS?", "Form 168, the annual tax statement."),
    ("Can BQP file these forms?", "Yes: Forms 145/146, 41, 128, 144 and 48, for NRIs and foreign companies. " + CONTACT),
]

html = page(slug=SLUG,
            title="Old vs New Income Tax Form Numbers 2026: 15CA is 145, 15CB is 146, 10F is 41",
            description="Income-tax Rules, 2026 renumbered the forms from 1 April 2026: 15CA is Form 145, 15CB Form 146, 10F Form 41, 13 Form 128, 27Q Form 144, 26AS Form 168, 3CEB Form 48, 49AA Forms 95/96. Searchable table and what applies when.",
            keywords="Form 145 income tax, Form 146 income tax, Form 15CA new number, Form 15CB new form number, Form 41 DTAA, Form 10F new number, Form 128 lower TDS, Form 144 TDS non-resident, Form 168 annual statement, old vs new income tax forms 2026",
            hero_kicker="/ Income-tax Act 2025 &middot; Forms &middot; Updated 2026-10-30",
            hero_title_html="Old vs New Income Tax Form Numbers, <em>15CA is now 145.</em>",
            hero_lead="From 1 April 2026, the Income-tax Rules, 2026 renumbered almost every income tax form. Form 15CA is now Form 145, Form 15CB is Form 146, Form 10F is Form 41, Form 13 is Form 128, Form 27Q is Form 144 and Form 26AS is Form 168. Search the table below for any form.",
            sections=sections, faqs=faqs,
            related=[("form-15ca-15cb-foreign-remittance-india.html", "Related", "Foreign remittance forms (145/146)"),
                     ("income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", "Related", "Section 195 is now 393")],
            cta_headline="Not sure which form applies?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AR complete")
