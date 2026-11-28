# -*- coding: utf-8 -*-
"""Batch LK (28 Nov 2026): Significant beneficial owner (SBO) under section 90 of the Companies Act - who is an SBO (10% tests and
significant influence or control), BEN-1 declaration by the individual, BEN-2 filing by the company, BEN-3 register, BEN-4 notice,
foreign-owned subsidiaries and consequences.
Demand: 'significant beneficial owner', 'ben-2 filing', 'ben-1 declaration', 'sbo foreign parent india subsidiary', 'section 90
companies act' - mentioned on the 100% foreign ownership and UK PSC pages but no dedicated page. Foreign-owned Indian subsidiaries
(the site's core foreign audience) must trace and report individuals at the top of the chain. User steer 26 Nov 2026 / 19 Nov
foreign-client steer: more call bookings.
Facts (Companies Act, 2013 section 90; Companies (Significant Beneficial Owners) Rules, 2018 as amended in 2019): an SBO is an
individual who, directly or indirectly (alone or together), holds at least 10% of the shares, or at least 10% of the voting rights,
or has the right to at least 10% of distributable dividend, or exercises significant influence or control; the individual files
BEN-1 with the company within 30 days of becoming an SBO or of any change; the company files BEN-2 with the Registrar within 30
days of receiving BEN-1; the company keeps a register of SBOs in BEN-3 and must take steps to identify SBOs, including sending
notice in BEN-4 to non-individual members holding 10% or more; for a foreign parent, the chain is traced to the individuals at the
top; certain holdings (government, specified regulated investment vehicles) are exempt; failure by the company, its officers or the
individual attracts penalties under section 90, and the company can apply to the tribunal to restrict rights on shares where the
SBO is not disclosed. No penalty amounts, no fees, no portal menu paths. advisory_lib.contact() is not used."""
import advisory_lib as A
from advisory_lib import ul, table, call_box, sources
from build_lib import page, write_page

A.UPDATED = "Last updated: 28 November 2026."
SLUG = "significant-beneficial-owner-sbo-india-section-90-ben-1-ben-2-ben-4-foreign-parent-subsidiary-2026"

C = ("WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the Indian company&rsquo;s shareholding pattern, the "
     "ownership chain up to the individuals at the top (for foreign parents, each holding layer), any shareholder agreements "
     "giving control rights, and the BEN forms filed so far. Or book a call directly.")
PAGES = [dict(
    slug=SLUG,
    title="Significant Beneficial Owner (SBO) in India (2026): Section 90, the 10% Tests, BEN-1 Declaration, BEN-2 Filing, BEN-4 Notice and Foreign-Owned Subsidiaries",
    em="trace the chain to a real person.",
    kicker="/ Indian companies, foreign parents and their shareholders &middot; Companies Act section 90 &middot; Updated 2026-11-28",
    lead=("<strong>Every Indian company must identify its significant beneficial owners - the individuals who ultimately hold 10% or more of its shares, votes or dividend rights, or exercise significant influence or control - and report them to the Registrar. "
          "The individual declares in BEN-1 within 30 days, and the company files BEN-2 within 30 days of receiving it. "
          "For a subsidiary of a foreign group, that means tracing ownership up through every layer to the people at the top.</strong>"),
    sections=[
        ("/ Who is an SBO, and what is filed", "Section 90 and the SBO Rules.",
         table(["Point", "Rule"], [
             ["SBO tests (any one)", "At least 10% of shares; at least 10% of voting rights; right to at least 10% of distributable dividend; significant influence or control"],
             ["Holding", "Direct or indirect, alone or together with others"],
             ["BEN-1", "Declaration by the individual to the company within 30 days of becoming an SBO or of any change"],
             ["BEN-2", "Return by the company to the Registrar within 30 days of receiving BEN-1"],
             ["BEN-3", "Register of SBOs kept by the company"],
             ["BEN-4", "Notice by the company to non-individual members holding 10% or more, to identify SBOs"],
             ["Exemptions", "Certain government holdings and specified regulated investment vehicles"]])
         + ul("<strong>Not just shareholders:</strong> control through agreements, board rights or voting arrangements can make someone an SBO without 10% of the shares.",
              "<strong>Indirect holdings:</strong> where a company, trust, partnership or fund sits in the chain, look through it to the individuals behind it.")),
        ("/ Foreign-owned subsidiaries", "Where most errors happen.",
         ul("<strong>Trace every layer:</strong> for an Indian subsidiary of a foreign company, identify the individuals who control the foreign parent, layer by layer.",
            "<strong>Send BEN-4 early:</strong> the Indian company should formally ask its corporate shareholders for SBO details and record the replies.",
            "<strong>Keep it consistent:</strong> SBO details should match FEMA filings (FC-GPR / FLA), bank KYC and foreign registers such as the UK PSC register.",
            "<strong>Changes in the group:</strong> a restructuring, share transfer or new investor above the threshold restarts the 30-day clock.",
            "<strong>Consequences:</strong> the company, its officers and the individual face penalties under section 90, and the company can seek tribunal orders restricting rights on shares where the SBO is not disclosed.")
         + call_box("significant beneficial owner compliance", ["Mapping the ownership chain",
                                                                 "BEN-4 notices to corporate shareholders",
                                                                 "BEN-1 declarations and BEN-2 filing",
                                                                 "BEN-3 register",
                                                                 "Alignment with FEMA, bank KYC and foreign registers"],
                    "Shareholding pattern, ownership chain, control agreements, BEN forms filed.")
         + sources("Companies Act, 2013 (section 90); Companies (Significant Beneficial Owners) Rules, 2018, as amended in 2019 (Forms BEN-1 to BEN-4); site 100% foreign ownership, UK PSC and ROC compliance pages.")),
    ],
    faqs=[("Who is a significant beneficial owner in India?", "An individual who, directly or indirectly, holds at least 10% of a company's shares, voting rights or right to distributable dividend, or who exercises significant influence or control over the company."),
          ("What is the difference between BEN-1 and BEN-2?", "BEN-1 is the declaration the individual gives to the company within 30 days of becoming an SBO or of any change. BEN-2 is the return the company files with the Registrar within 30 days of receiving BEN-1."),
          ("Does a subsidiary of a foreign company need to file BEN-2?", "Yes, if any individual meets an SBO test through the foreign group. The Indian company must trace ownership through each layer of the foreign parent to the individuals at the top."),
          ("What is Form BEN-4?", "A notice the company sends to non-individual members holding 10% or more of its shares, asking for information needed to identify significant beneficial owners."),
          ("What happens if SBO details are not filed?", "The company, its officers in default and the individual face penalties under section 90, and the company can apply to the tribunal for orders restricting rights attached to the shares."),
          ("What should I send to start?", "WhatsApp +91 78018 87130 or email info@bharatquantumprospera.com with the shareholding pattern, the ownership chain to the top, any control agreements and the BEN forms filed so far. Or book a call directly.")],
    related=[("can-foreigner-own-100-percent-indian-company.html", "Can a foreigner own 100% of an Indian company?"),
             ("uk-ltd-indian-subsidiary-psc-filing-ca.html", "UK Ltd with an Indian subsidiary: PSC and SBO"),
             ("roc-compliance-private-limited-company-llp-2026-27-calendar-due-dates-forms-late-fees.html", "ROC compliance calendar"),
             ("director-resignation-removal-india-dir-11-dir-12-section-168-169-resident-director-2026.html", "Director resignation and removal")],
    cta_h="Need to map and report your significant beneficial owners?", cta_b=C,
    keywords="significant beneficial owner india, sbo section 90, ben-1 declaration, ben-2 filing, ben-4 notice, sbo foreign parent indian subsidiary, beneficial ownership 10 percent",
    desc="Significant beneficial owner (SBO) under section 90: individuals with 10% or more of shares, votes or dividend, or significant influence or control; BEN-1 within 30 days; BEN-2 within 30 days of receipt; BEN-3 register; BEN-4 notice; tracing foreign parent chains; penalties.",
    howto={"name": "How to comply with SBO rules", "description": "Identify, declare, file.", "steps": [
        {"name": "Map ownership", "text": "Trace every layer to the individuals at the top, including control rights."},
        {"name": "Send BEN-4", "text": "To corporate shareholders holding 10% or more."},
        {"name": "Collect BEN-1", "text": "From each SBO within 30 days of becoming one or of a change."},
        {"name": "File BEN-2", "text": "With the Registrar within 30 days; update the BEN-3 register."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch LK complete")
