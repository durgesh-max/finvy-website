# -*- coding: utf-8 -*-
"""Shared helpers for foreign-company advisory pages: call-first CTA box, tables, sources, contact text."""
from urllib.parse import quote

UPDATED = "Last updated: 19 November 2026."  # builders may override advisory_lib.UPDATED before building


def wa(t):
    return "https://wa.me/917801887130?text=" + quote(t)


def ul(*x):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in x) + "</ul>"


def table(head, rows):
    return ("<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>")


def call_box(topic, agenda, bring):
    msg = f"Hi Durgesh, I would like to schedule a call about {topic} in India. Company: ... Country: ... What we want to do: ... Timeline: ..."
    mail = ("mailto:info@bharatquantumprospera.com?subject=" + quote("Call request: " + topic + " in India")
            + "&body=" + quote("Hi Durgesh,\n\nI would like to schedule a call about " + topic + " in India.\n\nCompany and country:\nWhat we want to do in India:\nTimeline:\nPreferred times (with time zone):\n\nThanks"))
    return (f'<div style="border:1px solid var(--line);border-left:4px solid #C2312A;border-radius:10px;padding:18px 20px;margin:20px 0;background:var(--bg-soft)">'
            f'<p style="margin:0 0 6px;font-weight:700">Schedule a call with CA Durgesh Chavda</p>'
            f'<p style="margin:0 0 10px">The right answer depends on your product, your home country and your Indian counterparty. A short call is the fastest way to get it right. On the call we cover:</p>'
            + ul(*agenda)
            + f'<p style="margin:10px 0 6px"><strong>Helpful to send before the call:</strong> {bring}</p>'
            f'<p style="margin:10px 0 0"><a href="https://topmate.io/cadurgesh_chavda/741484" target="_blank" rel="noopener"><strong>Book a call</strong></a> &middot; '
            f'<a href="{wa(msg)}" target="_blank" rel="noopener"><strong>WhatsApp +91 78018 87130</strong></a> &middot; '
            f'<a href="{mail}"><strong>Email info@bharatquantumprospera.com</strong></a>. Calls work across time zones. Everything you share is kept confidential.</p></div>')


def sources(text):
    return f'<p><strong>Sources:</strong> {text} <em>{globals()["UPDATED"]}</em> General information, not advice for a specific transaction.</p>'


def contact(what):
    return (f"Email info@bharatquantumprospera.com or WhatsApp +91 78018 87130 with {what}. "
            "We reply within one working day to set up a call, then send a written scope and fixed-fee quote.")


