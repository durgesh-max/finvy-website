# -*- coding: utf-8 -*-
"""Batch BV (12 Nov 2026): reverse flip by fast-track inbound merger (foreign holding company into its wholly owned
Indian subsidiary under section 233 of the Companies Act, 2013).
Facts: Companies (Compromises, Arrangements and Amalgamations) Amendment Rules, 2024 (notified 9 September 2024, effective
17 September 2024) allowed a foreign holding company to merge into its wholly owned Indian subsidiary through the
section 233 fast track (Regional Director approval instead of NCLT), with prior RBI approval and compliance with the
FEMA (Cross Border Merger) Regulations, 2018; the rules were amended again in September 2025; a 2026 FEMA amendment
proposes a re-domiciliation framework. Tax: an amalgamation into an Indian company can be tax-neutral under section 47
of the 1961 Act (and its equivalent in the 2025 Act) only if the statutory definition of amalgamation is met; home-country
tax for foreign shareholders (for example US reorganisation rules) is often the larger issue. Timelines reported as months
on the fast track versus longer on the NCLT route."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 12 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def ol(*x):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in x) + "</ol>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the holding company's country, the cap table and the Indian subsidiary's details. "
           "We reply the same working day with the route options, the tax model and a fixed-scope quote; corporate counsel handles the scheme filings.")
SLUG = "reverse-flip-india-fast-track-inbound-merger-section-233-rbi-tax-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Model the tax before you pick the route</p>'
       f'<p style="margin:0">The legal route is now faster; the tax bill is where reverse flips succeed or stall. We model Indian and investor-side tax for the merger and the share-swap alternatives: '
       f'<a href="{wa("Hi Durgesh, we are planning a reverse flip to India. Can you model the fast-track merger route?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Reverse Flip to India by Fast-Track Merger: Section 233, RBI Approval and Tax (2026)",
    em="the Regional Director, not the NCLT.",
    kicker="/ Delaware, Singapore &amp; UK holding companies &middot; Reverse flip &middot; Updated 2026-11-12",
    lead=("Since 17 September 2024, a foreign holding company can merge into its wholly owned Indian subsidiary through the fast-track merger route under section 233 of the Companies Act, 2013, approved by the Regional Director instead of the NCLT, with prior RBI approval. "
          "That makes an inbound merger a practical way to bring a Delaware, Singapore or UK parent back to India, alongside the share-swap route. "
          "The legal steps are now shorter; the decisive question is usually tax, for the Indian entities and for the foreign shareholders in their home countries."),
    sections=[
        ("/ Two ways to flip back", "Compared.",
         table(["Route", "How it works", "Typical issues"], [
             ["Fast-track inbound merger (section 233)", "The foreign holding company merges into its wholly owned Indian subsidiary; shareholders receive shares of the Indian company", "Prior RBI approval, FEMA cross-border merger conditions, Indian tax neutrality conditions, investor-country tax"],
             ["Share swap", "Shareholders of the foreign parent swap their shares for shares of the Indian company, which becomes the parent", "FDI pricing and reporting, ODI for resident shareholders, capital gains for shareholders, then winding up or keeping the foreign entity"]])
         + '<p>The share-swap route in detail: <a href="us-india-reverse-flip-structure.html">US-India reverse flip structure</a>.</p>'
         + BOX),
        ("/ Fast-track merger steps", "In outline.",
         ol("<strong>Confirm eligibility:</strong> the foreign company is the holding company and the Indian company its wholly owned subsidiary; check the latest form of the rules (amended again in September 2025).",
            "<strong>RBI approval:</strong> obtain prior approval and meet the FEMA (Cross Border Merger) Regulations, 2018 for the assets, liabilities and shares that move.",
            "<strong>Scheme and approvals:</strong> board and shareholder approvals, creditor approvals and notices as section 233 requires, then the Regional Director's confirmation.",
            "<strong>Shares and filings:</strong> the Indian company issues shares to the foreign parent's shareholders, with FDI reporting for non-resident shareholders and ODI or other FEMA reporting where residents are involved.",
            "<strong>Close out abroad:</strong> deal with the foreign entity's dissolution, contracts, IP and bank accounts in its home jurisdiction."))
        ,
        ("/ Tax points", "Where the cost sits.",
         ul("<strong>Indian tax neutrality:</strong> an amalgamation into an Indian company can be exempt for the amalgamating company and its shareholders only if the statutory definition of amalgamation is met (including the shareholder-continuity condition).",
            "<strong>Foreign shareholders:</strong> their home country decides whether receiving Indian shares is taxable; US holders, for example, need a reorganisation analysis.",
            "<strong>ESOPs and SAFEs:</strong> map how options, warrants and convertibles in the foreign parent convert into the Indian company.",
            "<strong>Losses and stamp duty:</strong> check the carry-forward of losses, state stamp duty on the transfer and GST on any assets or services moving.")
         + '<p>Related: <a href="flip-tax-impact-calculator.html">flip tax impact calculator</a> &middot; <a href="how-to-structure-india-us-flip-f-reorganization-step-by-step.html">India-US flip step by step</a> &middot; <a href="ca-for-india-us-flip.html">CA for India-US flips</a>.</p>'
         f'<p><strong>Sources:</strong> Companies Act, 2013, section 233; Companies (Compromises, Arrangements and Amalgamations) Amendment Rules, 2024 (notified 9 September 2024, effective 17 September 2024) and the September 2025 amendment; FEMA (Cross Border Merger) Regulations, 2018; Income-tax provisions on amalgamation. <em>{UPDATED}</em> General information. BQP handles tax and FEMA; the scheme and Regional Director filings need corporate counsel.</p>'),
    ],
    faqs=[("Can a Delaware company merge into its Indian subsidiary?", "Yes. Since 17 September 2024, a foreign holding company can merge into its wholly owned Indian subsidiary through the section 233 fast-track route, with prior RBI approval and Regional Director confirmation instead of the NCLT."),
          ("Is the fast-track reverse flip tax-free?", "On the Indian side it can be tax-neutral if the statutory definition of amalgamation is met. Foreign shareholders' home-country tax is separate and often the bigger question."),
          ("Do we need RBI approval for an inbound merger?", "Yes. The rules require prior RBI approval, and the merger must meet the FEMA (Cross Border Merger) Regulations, 2018."),
          ("Merger or share swap: which is better?", "It depends on the shareholder base and tax. A merger avoids keeping a foreign parent; a share swap can be simpler where the merger conditions are not met. Model both."),
          ("How long does the fast track take?", "Reported timelines are a matter of months, shorter than the NCLT route, but RBI approval and foreign-law steps can extend it."),
          ("Can BQP model our reverse flip?", "Yes. " + CONTACT)],
    related=[("us-india-reverse-flip-structure.html", "US-India reverse flip structure"),
             ("flip-tax-impact-calculator.html", "Flip tax impact calculator"),
             ("ca-for-india-us-flip.html", "CA for India-US flips")],
    cta_h="Bringing your holding company back to India?", cta_b=CONTACT,
    keywords="reverse flip India fast track merger, section 233 inbound merger, foreign holding company merger Indian subsidiary, Rule 25A reverse flip, Delaware to India merger, reverse flip RBI approval, reverse flip tax India 2026",
    desc="Reverse flip to India by fast-track inbound merger: since 17 September 2024 a foreign holding company can merge into its wholly owned Indian subsidiary under section 233 with RBI approval and Regional Director confirmation. Steps, merger vs share swap, and the tax points for Indian entities and foreign shareholders.",
    howto={"name": "How to reverse flip by fast-track merger", "description": "Outline of the section 233 inbound merger route.", "steps": [
        {"name": "Confirm eligibility", "text": "Foreign holding company and wholly owned Indian subsidiary; check the current rules."},
        {"name": "Get RBI approval", "text": "Obtain prior approval and meet the FEMA cross-border merger regulations."},
        {"name": "Run the scheme", "text": "Board, shareholder and creditor approvals, then Regional Director confirmation."},
        {"name": "Issue shares and close out", "text": "Indian company issues shares; complete FEMA reporting and dissolve the foreign entity."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BV complete")
