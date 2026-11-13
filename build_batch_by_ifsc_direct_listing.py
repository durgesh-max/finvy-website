# -*- coding: utf-8 -*-
"""Batch BY (13 Nov 2026): direct listing of Indian companies on GIFT IFSC exchanges - the 3 November 2026 amendment.
Facts: Companies (Listing of Equity Instruments in Permissible Jurisdictions) Amendment Rules, 2026, G.S.R. 968(E) dated
3 November 2026 under section 23(3) read with section 469 of the Companies Act, 2013: "equity shares" widened to "equity
instruments" (including convertible debentures and preference shares); rules extended to unlisted public companies in
IFSCs; companies with negative net worth may list if at least 75% of the net offer is allotted to qualified institutional
buyers; conditions on existing holders, specified defaults and the look-back period revised; LEAP-1 form replaced; offers
for sale by existing holders allowed where the securities are eligible under the NDI Rules. Base rules: Companies (Listing
of equity shares in permissible jurisdictions) Rules, 2024; permissible exchanges in GIFT IFSC (India INX, NSE IX); only
unlisted public companies (a private company must convert first); FEMA direct listing framework under the NDI Rules."""
from urllib.parse import quote
from build_lib import page, write_page

UPDATED = "Last updated: 13 November 2026."


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


CONTACT = ("WhatsApp +91 78018 87130 or email durgesh@bharatquantumprospera.com with the company's status (private or public), cap table and funding history. "
           "We reply the same working day with the readiness steps and a fixed-scope quote; merchant bankers and counsel handle the offer itself.")
SLUG = "direct-listing-gift-ifsc-indian-company-equity-instruments-amendment-november-2026"
BOX = (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:16px 18px;margin:18px 0;background:var(--bg-soft)">'
       f'<p style="margin:0 0 8px;font-weight:600">Weighing an IFSC listing against a flip or a domestic IPO?</p>'
       f'<p style="margin:0">We prepare the company side: conversion to a public company, cap table and FEMA history clean-up, valuation and the tax position for founders and foreign investors. '
       f'<a href="{wa("Hi Durgesh, we are considering a direct listing on a GIFT IFSC exchange. Can you check our readiness?")}" target="_blank" rel="noopener"><strong>WhatsApp CA Durgesh Chavda</strong></a>.</p></div>')

PAGES = [dict(
    slug=SLUG,
    title="Direct Listing of Indian Companies on GIFT City (IFSC) Exchanges: What the 3 November 2026 Amendment Changes",
    em="more instruments, more companies, one QIB condition.",
    kicker="/ Founders, foreign investors &middot; GIFT IFSC listing &middot; Updated 2026-11-13",
    lead=("On 3 November 2026 the Ministry of Corporate Affairs amended the rules that let Indian public companies list directly on exchanges in GIFT City's International Financial Services Centre (G.S.R. 968(E)). "
          "The rules now cover <strong>equity instruments</strong>, including convertible debentures and preference shares, not just equity shares; they extend to unlisted public companies in the IFSC; and companies with negative net worth may list if at least 75% of the net offer goes to qualified institutional buyers. "
          "Offers for sale by existing holders are also allowed where the securities are eligible under the FEMA non-debt rules. For founders with foreign investors, it is one more route to compare with a reverse flip or a domestic IPO."),
    sections=[
        ("/ What changed on 3 November 2026", "Against the 2024 rules.",
         table(["Point", "2024 rules", "After the 2026 amendment"], [
             ["What can be listed", "Equity shares", "Equity instruments, including convertible debentures and preference shares"],
             ["Who can list", "Unlisted public companies incorporated in India", "Also unlisted public companies in the IFSC, under the IFSCA framework"],
             ["Loss-making companies", "Barred by eligibility conditions", "Negative net worth allowed if at least 75% of the net offer goes to QIBs"],
             ["Offers for sale", "Limited", "Existing holders can offer securities that are eligible under the NDI Rules"],
             ["Other conditions", "-", "Revised tests on existing holders, specified defaults and the look-back period; LEAP-1 form replaced"]])
         + BOX),
        ("/ Before you consider it", "Readiness points.",
         ul("<strong>Be a public company:</strong> the route is for unlisted public companies, so a private limited company converts first.",
            "<strong>Clean FEMA history:</strong> every past foreign investment reported (FC-GPR, FC-TRS) and priced correctly; gaps surface in diligence.",
            "<strong>Cap table:</strong> ESOPs, convertibles and SAFEs mapped into instruments that can be listed.",
            "<strong>Investor fit:</strong> the QIB condition for loss-making companies means institutional demand has to be there.",
            "<strong>Tax:</strong> model capital gains for founders, ESOP holders and foreign investors on the listed instruments, including treaty positions."))
        ,
        ("/ How it compares", "Three routes for founders with foreign investors.",
         ul("<strong>Reverse flip to India:</strong> bring a foreign parent home first; see <a href=\"reverse-flip-india-fast-track-inbound-merger-section-233-rbi-tax-2026.html\">fast-track merger route</a> and <a href=\"us-india-reverse-flip-structure.html\">share-swap route</a>.",
            "<strong>Domestic IPO:</strong> SEBI eligibility and listing on Indian exchanges.",
            "<strong>IFSC direct listing:</strong> dollar-denominated listing in GIFT City under the amended rules.")
         + '<p>Related: <a href="gift-city.html">GIFT City overview</a> &middot; <a href="foreign-individuals-invest-indian-listed-shares-fema-schedule-iii-2026.html">foreign individuals investing in listed Indian shares (FEMA 2026)</a> &middot; <a href="ca-for-india-us-flip.html">India-US flips</a>.</p>'
         f'<p><strong>Sources:</strong> Companies (Listing of Equity Instruments in Permissible Jurisdictions) Amendment Rules, 2026, G.S.R. 968(E) dated 3 November 2026; Companies (Listing of equity shares in permissible jurisdictions) Rules, 2024; Companies Act, 2013, section 23(3); FEMA (Non-debt Instruments) Rules, 2019. <em>{UPDATED}</em> General information. The offer document, exchange approvals and IFSCA filings need merchant bankers and counsel.</p>'),
    ],
    faqs=[("What did the 3 November 2026 amendment change for listing in GIFT City?", "It widened the rules from equity shares to equity instruments (including convertible debentures and preference shares), extended them to unlisted public companies in the IFSC, allowed companies with negative net worth to list if at least 75% of the net offer goes to QIBs, and allowed offers for sale by existing holders where eligible under the NDI Rules."),
          ("Can a private limited company list directly in GIFT IFSC?", "Not as a private company. The route is for unlisted public companies, so a private limited company has to convert to a public company first."),
          ("Can a loss-making startup list in GIFT City now?", "Yes, if at least 75% of the net offer is allotted to qualified institutional buyers and the other eligibility conditions are met."),
          ("Which notification is it?", "G.S.R. 968(E) dated 3 November 2026, the Companies (Listing of Equity Instruments in Permissible Jurisdictions) Amendment Rules, 2026, issued under section 23(3) read with section 469 of the Companies Act, 2013."),
          ("Is an IFSC listing an alternative to a reverse flip?", "For some founders with foreign investors, yes: it gives a dollar listing while staying an Indian company. Compare it with a reverse flip and a domestic IPO on tax, investor demand and cost."),
          ("Can BQP prepare our company?", "Yes. " + CONTACT)],
    related=[("reverse-flip-india-fast-track-inbound-merger-section-233-rbi-tax-2026.html", "Reverse flip by fast-track merger"),
             ("gift-city.html", "GIFT City overview"),
             ("ca-for-india-us-flip.html", "CA for India-US flips")],
    cta_h="Considering a GIFT City listing?", cta_b=CONTACT,
    keywords="direct listing GIFT IFSC, Indian company listing GIFT City 2026, equity instruments permissible jurisdictions amendment, GSR 968(E), loss making company listing IFSC QIB 75%, India INX NSE IX direct listing, overseas listing Indian startups November 2026",
    desc="The 3 November 2026 amendment (G.S.R. 968(E)) lets Indian public companies list equity instruments, including convertible debentures and preference shares, on GIFT IFSC exchanges, extends to IFSC companies, and allows loss-making companies with 75% QIB allotment. What changed and how founders should prepare.",
    howto={"name": "How to prepare for an IFSC direct listing", "description": "Readiness steps for an Indian company.", "steps": [
        {"name": "Convert to a public company", "text": "The route is for unlisted public companies."},
        {"name": "Clean up FEMA and the cap table", "text": "Complete past FDI reporting and map ESOPs and convertibles."},
        {"name": "Check eligibility", "text": "Test the revised conditions, including the 75% QIB rule for loss-making companies."},
        {"name": "Model tax and compare routes", "text": "Compare with a reverse flip and a domestic IPO before appointing bankers."}]})]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'{p["title"]}, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"], howto=p["howto"])
    write_page(p["slug"], html)
print("Batch BY complete")
