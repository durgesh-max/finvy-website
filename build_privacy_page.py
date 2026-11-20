# -*- coding: utf-8 -*-
"""Privacy and cookie notice (20 Nov 2026). Describes what the website actually does, checked against the code:
- Enquiries: WhatsApp / email / phone links open the visitor's own app; the quote and contact forms build a message in the
  visitor's WhatsApp or email app; the US incorporation intake form posts to FormSubmit (formsubmit.co), which emails the firm.
- Microsoft Clarity (project zgq0b04kz1) loaded by bqp-track.js; cookies per Microsoft's cookie list (_clck, _clsk
  first-party; CLID, ANONCHK, MR, MUID, SM third-party); consent via Clarity Consent API v2 with ad storage denied.
- bqp-track.js localStorage keys: bqp_consent (choice), bqp_attr (source and landing page, 30 days).
- Consent model: visitors in UK / EEA / Switzerland time zones are asked first; elsewhere Clarity runs with a notice and
  a Decline button.
- Fonts from Google Fonts; hosting on GitHub Pages; client portal is a demo that keeps data in the browser only.
Statements about how the firm handles enquiries are deliberately general; the firm should review them."""
from build_lib import page, write_page

UPDATED = "Last updated: 20 November 2026."
SLUG = "privacy"


def table(head, rows):
    return ('<div style="overflow-x:auto"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


CONTACT = ("Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with any question about your information, "
           "or to ask for a copy, a correction or deletion.")
BTN = ('<p><button type="button" onclick="if(window.bqpConsent){window.bqpConsent.open();}" '
       'style="padding:10px 18px;border-radius:6px;border:1px solid #0E1116;background:#0E1116;color:#fff;font:600 14px/1 Inter,system-ui,sans-serif;cursor:pointer">'
       'Change my cookie choice</button></p>')

PAGES = [dict(
    slug=SLUG,
    title="Privacy and Cookie Notice | Bharat Quantum Prospera",
    em="what this website collects, why, and your choices.",
    kicker="/ Privacy &middot; Cookies &middot; Updated 2026-11-20",
    lead=("This website is run by <strong>Bharat Quantum Prospera</strong>, the chartered accountancy practice of CA Durgesh Chavda, Ahmedabad, India. "
          "The site has <strong>no advertising</strong> and we do not sell personal information. "
          "We receive personal information only when <strong>you contact us</strong> by WhatsApp, email, phone or a form. "
          "We also use <strong>Microsoft Clarity</strong> to see how visitors use the site. Clarity sets cookies and records visits. "
          "If you are in the <strong>UK, the EEA or Switzerland</strong>, Clarity is loaded only after you accept. Elsewhere it runs unless you decline. "
          "You can change your choice at any time with the button on this page."),
    sections=[
        ("/ What we collect", "And where it goes.",
         table(["What", "When", "Who receives it"], [
             ["Your enquiry: name, contact details and what you tell us", "When you message us on WhatsApp, email us, call, or use the quote or contact form. These forms open your own WhatsApp or email app with the message filled in; nothing is sent until you send it.", "Bharat Quantum Prospera, through WhatsApp (Meta) or your email provider"],
             ["US incorporation intake form answers", "When you submit that form", "Sent to our email through FormSubmit (formsubmit.co), a form-to-email service"],
             ["A reference line such as &ldquo;Ref: page | via google&rdquo;", "Added to the pre-filled WhatsApp or email text so we know which page you were on and how you reached the site. You can see and delete it before sending.", "Us, as part of your message"],
             ["How the site is used: pages viewed, clicks, scrolling, device and browser type, approximate location from your IP address", "On each visit where Microsoft Clarity is active", "Microsoft Clarity, on our behalf. Text typed into forms is masked by Clarity by default."],
             ["Server logs, including your IP address", "On every visit", "GitHub Pages (GitHub, Inc.), which hosts the site"],
             ["A request for fonts, including your IP address", "On every visit", "Google Fonts (Google LLC)"],
             ["Client portal demo data", "Only if you try the client portal demo", "Stays in your own browser; it is not sent to us"]])
         + f"<p><em>{UPDATED}</em></p>"),
        ("/ Cookies and similar storage", "What is stored on your device.",
         table(["Name", "Set by", "Purpose"], [
             ["_clck, _clsk", "Microsoft Clarity (first-party cookies)", "Recognise a returning browser and join page views into one visit"],
             ["CLID, ANONCHK, MR, MUID, SM", "Microsoft (third-party cookies on Microsoft domains)", "Clarity and Microsoft browser identification; see Microsoft&rsquo;s cookie list"],
             ["bqp_consent", "This site (local storage)", "Remembers whether you accepted or declined"],
             ["bqp_attr", "This site (local storage, 30 days)", "Remembers the page you first landed on and how you arrived (for example a search engine). Stored only where Clarity is allowed."],
             ["bqp_accounts, bqp_files, bqp_session", "This site (local and session storage)", "Used only by the client portal demo, on your device"]])
         + "<p>We tell Clarity not to use advertising storage. Microsoft&rsquo;s own description of these cookies is in the "
           "<a href=\"https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-cookies\" rel=\"noopener\" target=\"_blank\">Clarity cookie list</a>, "
           "and its handling of data is described in the <a href=\"https://www.microsoft.com/en-us/privacy/privacystatement\" rel=\"noopener\" target=\"_blank\">Microsoft Privacy Statement</a>.</p>"),
        ("/ Your choice", "Accept, decline or change your mind.",
         ul("<strong>UK, EEA and Switzerland:</strong> we ask first. Until you accept, Clarity is not loaded and nothing is stored on your device for analytics.",
            "<strong>Other countries:</strong> Clarity runs when you arrive and a notice lets you decline.",
            "<strong>If you decline:</strong> Clarity&rsquo;s cookies are deleted, our own record of how you arrived is deleted, and Clarity is not loaded on the pages you visit afterwards.",
            "<strong>Changing your mind:</strong> use the button below, or clear this site&rsquo;s cookies and site data in your browser.",
            "We decide which rule applies from your browser&rsquo;s time zone, so no location lookup is made for this.")
         + BTN),
        ("/ How we use what you send us", "Enquiries and client information.",
         ul("<strong>Purpose:</strong> to reply to your enquiry and, if you engage us, to provide the professional services you ask for and meet our legal and professional obligations.",
            "<strong>Sharing:</strong> we do not sell your information. It is shared only where needed to do the work you ask for or where the law requires.",
            "<strong>Retention:</strong> enquiries are kept for as long as needed to deal with them; client records are kept for the periods that law and professional rules require.",
            "<strong>Where it is processed:</strong> we are based in India. WhatsApp, email, Microsoft, GitHub, Google and FormSubmit may process information in other countries, including the United States.",
            "<strong>Please do not send</strong> passwords, full card numbers or documents you would not want kept in a WhatsApp or email thread until we have agreed how to share them.")),
        ("/ Your rights and contact", "Access, correction, deletion and complaints.",
         ul("You can ask us what information we hold about you, and ask us to correct or delete it, subject to records we must keep by law.",
            "Depending on where you live, you may have further rights under laws such as India&rsquo;s Digital Personal Data Protection Act, 2023, the UK GDPR or the EU GDPR, including the right to object, to withdraw consent and to complain to your data protection authority.",
            "To use any of these rights, " + CONTACT[0].lower() + CONTACT[1:],
            "We will update this page when the website changes and show the date at the top.")),
    ],
    faqs=[("Does this website use cookies?", "Yes, only for Microsoft Clarity, which shows us how visitors use the site. Visitors in the UK, EEA and Switzerland are asked first; elsewhere Clarity runs unless you decline. There are no advertising cookies."),
          ("Can I decline cookies and still use the site?", "Yes. Everything on the site works if you decline. Clarity's cookies are deleted and Clarity is not loaded on later pages."),
          ("Does the website store what I type into its forms?", "No. The quote and contact forms open your own WhatsApp or email app with the message filled in. The US incorporation intake form is sent to our email through FormSubmit. Clarity masks text typed into forms by default."),
          ("How do I ask for my information to be deleted?", CONTACT)],
    related=[("contact.html", "Contact"), ("about.html", "About the firm"), ("book-a-call.html", "Book a call")],
    cta_h="A question about your information?", cta_b=CONTACT,
    keywords="Bharat Quantum Prospera privacy notice, cookie notice, Microsoft Clarity cookies, data protection",
    desc="Privacy and cookie notice for bharatquantumprospera.com: what the website collects when you contact us, how Microsoft Clarity is used, the cookies set, how to accept or decline, and how to ask for access, correction or deletion.")]

for p in PAGES:
    html = page(slug=p["slug"], title=p["title"], description=p["desc"], keywords=p["keywords"], hero_kicker=p["kicker"],
                hero_title_html=f'Privacy and Cookie Notice, <em>{p["em"]}</em>', hero_lead=p["lead"], sections=p["sections"], faqs=p["faqs"],
                related=[(h, "Related", t) for h, t in p["related"]], cta_headline=p["cta_h"], cta_body=p["cta_b"])
    write_page(p["slug"], html)
print("Privacy page built")
