# -*- coding: utf-8 -*-
"""Batch AT: Round 31 - old vs new section numbers (Income-tax Act, 2025) for NRIs, founders and foreign companies, with a lookup box."""
from build_lib import page, write_page

CONTACT = "Email durgesh@bharatquantumprospera.com or WhatsApp +91 78018 87130. Fixed-scope quote within 48 hours."
SLUG = "income-tax-act-2025-section-mapping-old-vs-new-54-is-82-80c-is-123-nri"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# (old, new, topic) - only rows where at least two practitioner mappings agree, or verified earlier
SECTIONS = [
    ("6", "6", "Residential status (resident, RNOR, non-resident)"),
    ("9", "9 (read with Schedule I)", "Income deemed to accrue or arise in India"),
    ("44AB", "63", "Tax audit"),
    ("44ADA", "58", "Presumptive taxation for professionals"),
    ("54", "82", "Capital gains exemption on a residential house"),
    ("54EC", "85", "Capital gains exemption on specified bonds"),
    ("54F", "86", "Capital gains exemption on sale of other assets, reinvested in a house"),
    ("80C", "123 (read with Schedule XV)", "Deduction for PF, life insurance, ELSS, tuition, home-loan principal"),
    ("80D", "126", "Health insurance deduction"),
    ("87A", "156", "Rebate (no tax up to INR 12 lakh in the new regime)"),
    ("90", "159", "Relief under a tax treaty (DTAA)"),
    ("111A", "196", "Short-term capital gains on listed equity"),
    ("112", "197", "Long-term capital gains (other assets)"),
    ("112A", "198", "Long-term capital gains on listed equity"),
    ("115BAC", "202", "New tax regime (default)"),
    ("139(1)", "263(1)", "Filing the income tax return"),
    ("139(8A) / 140B", "267", "Updated return (ITR-U)"),
    ("195", "393(2)", "TDS on payments to non-residents"),
    ("206C", "394", "TCS, including on foreign remittances under LRS"),
    ("234B", "424", "Interest for default in advance tax"),
    ("234C", "425", "Interest for deferment of advance tax"),
]

rows = "".join(f'<tr data-k="{o.lower()} {n.lower()} {t.lower()}"><td>Section {o}</td><td><strong>Section {n}</strong></td><td>{t}</td></tr>' for o, n, t in SECTIONS)
LOOKUP = ('<p><label for="sq"><strong>Search a section</strong> (old number, new number or topic):</label><br>'
          '<input id="sq" type="search" placeholder="e.g. 54, 80C, capital gains, treaty" style="width:100%;max-width:420px;padding:10px 12px;border:1px solid #ccc;border-radius:6px;font:inherit;margin-top:6px" /></p>'
          f'<table id="st"><thead><tr><th>Income-tax Act, 1961</th><th>Income-tax Act, 2025</th><th>Topic</th></tr></thead><tbody>{rows}</tbody></table>'
          '<p id="snone" style="display:none">No match. Try another word.</p>'
          '<script>(function(){var q=document.getElementById("sq"),rs=[].slice.call(document.querySelectorAll("#st tbody tr")),n=document.getElementById("snone");'
          'q.addEventListener("input",function(){var t=q.value.toLowerCase().replace(/^(section|sec\\.?|s\\.)\\s*/,"").trim(),c=0;rs.forEach(function(r){var k=r.getAttribute("data-k"),s=!t||(" "+k).indexOf(" "+t)>-1||(t.length>2&&k.indexOf(t)>-1);r.style.display=s?"":"none";if(s)c++;});n.style.display=c?"none":"";});})();</script>')

sections = [
    ("/ Lookup", "Old section, new section.", LOOKUP),
    ("/ Which Act applies", "The rule of thumb.",
     ul("The Income-tax Act, 2025 applies from 1 April 2026, to tax year 2026-27 onwards. \"Previous year\" and \"assessment year\" are replaced by a single \"tax year\".",
        "Income of FY 2025-26 (AY 2026-27), including returns, audits and capital gains on sales up to 31 March 2026, stays under the 1961 Act and its section numbers.",
        "Most rules carried over with new numbers; check rates and thresholds separately, since Budgets change those.",
        "Several new numbers reuse old ones for a different topic: new section 92 is income from other sources (old 56), and new section 197 is long-term capital gains (old 112), not the lower TDS certificate.")),
    ("/ For NRIs and foreign companies", "The sections you will meet most.",
     ul("<strong>Selling property in India</strong>: exemptions in sections 82 (was 54), 85 (was 54EC) and 86 (was 54F); TDS on the sale by the buyer under section 393 (was 195).",
        "<strong>Residential status</strong>: still section 6.",
        "<strong>Treaty relief</strong>: section 159 (was 90), with Form 41 (was 10F).",
        "<strong>Payments to non-residents</strong>: TDS under section 393(2) (was 195), reported in Form 144 (was 27Q).",
        "<strong>Listed shares and mutual funds</strong>: sections 196 (was 111A) and 198 (was 112A).") +
     '<p>For forms, see <a href="old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html">old vs new income tax form numbers</a>.</p>'
     '<p><strong>Sources:</strong> <a href="https://cleartax.in/s/income-tax-act-2025-section-numbers-old-vs-new" rel="nofollow noopener" target="_blank">ClearTax</a>; '
     '<a href="https://taxgarden.in/blog/old-vs-new-income-tax-sections-2026-mapping-table" rel="nofollow noopener" target="_blank">TaxGarden (24 August 2026)</a>; '
     '<a href="https://bvaca.com/blog/income-tax-act-2025-old-vs-new-section-mapping" rel="nofollow noopener" target="_blank">BVACA (5 September 2026)</a>; '
     '<a href="https://blog.ebcwebstore.com/income-tax-act-2025-old-vs-new-sections-mapping-guide/" rel="nofollow noopener" target="_blank">EBC (8 July 2026)</a>.</p>'
     "<p><em>Last updated: 31 October 2026. Only mappings on which at least two practitioner tables agree are listed; check the Act text before citing a section in a filing.</em></p>"),
]

faqs = [
    ("What is the new section for Section 54 under the Income-tax Act, 2025?", "Section 82. Sections 54EC and 54F become sections 85 and 86."),
    ("What is Section 80C called in the new Income-tax Act?", "Section 123, read with Schedule XV."),
    ("What is the new section for 115BAC (new tax regime)?", "Section 202. The Section 87A rebate is now section 156."),
    ("What replaced Section 195 TDS?", "Section 393(2) of the Income-tax Act, 2025."),
    ("Is residential status still Section 6?", "Yes, residential status remains in section 6."),
    ("Which Act applies to FY 2025-26 income?", "The Income-tax Act, 1961. The 2025 Act applies from tax year 2026-27 (from 1 April 2026)."),
    ("Can BQP advise under both Acts?", "Yes, including transition issues for NRIs and foreign companies. " + CONTACT),
]

html = page(slug=SLUG,
            title="Income-tax Act 2025 Section Mapping: 54 Is Now 82, 80C Is 123, 115BAC Is 202, 195 Is 393",
            description="Old vs new section numbers under the Income-tax Act, 2025 (from 1 April 2026): 54 to 82, 54EC to 85, 54F to 86, 80C to 123, 87A to 156, 115BAC to 202, 112A to 198, 90 to 159, 195 to 393(2). Searchable table for NRIs, founders and foreign companies.",
            keywords="section 54 new section number, section 82 income tax act 2025, 80C new section 123, 115BAC section 202, 87A section 156, income tax act 2025 section mapping, old vs new income tax sections, section 195 now 393",
            hero_kicker="/ Income-tax Act 2025 &middot; Sections &middot; Updated 2026-10-31",
            hero_title_html="Income-tax Act 2025 Section Mapping, <em>54 is now 82.</em>",
            hero_lead="From 1 April 2026 the Income-tax Act, 2025 replaced the 1961 Act and renumbered its sections. Section 54 is now section 82, 54EC is 85, 54F is 86, 80C is 123, 87A is 156, 115BAC is 202, 112A is 198, 90 is 159 and 195 is 393(2). Residential status stays in section 6. Search the table below.",
            sections=sections, faqs=faqs,
            related=[("income-tax-act-2025-section-195-now-393-what-changed-nri-foreign.html", "Related", "Section 195 is now 393"),
                     ("old-vs-new-income-tax-form-numbers-2026-15ca-145-15cb-146-10f-41.html", "Related", "Old vs new form numbers")],
            cta_headline="Need a section checked?", cta_body=CONTACT)
write_page(SLUG, html)
print("Batch AT complete")
