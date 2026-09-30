"""Evidence extractors — pull matchable strings from each SignalSource."""
from __future__ import annotations

import re
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import SignalSource


def extract_html(html: str) -> str:
    return html


def extract_headers(headers: dict[str, str], key: str) -> str:
    """Return a combined string of header_name: header_value for matching."""
    lines = []
    for k, v in headers.items():
        lines.append(f"{k.lower()}: {v}")
    return "\n".join(lines)


def extract_meta(html: str) -> str:
    """Extract all <meta> tag attribute strings."""
    return " ".join(re.findall(r"<meta[^>]+>", html, re.IGNORECASE))


def extract_cookies(cookies: dict[str, str]) -> str:
    return " ".join(f"{k}={v}" for k, v in cookies.items())


def extract_js_globals(js_globals: list[str]) -> str:
    return "\n".join(js_globals)


def extract_url(url: str) -> str:
    return url


def get_evidence(
    source: "SignalSource",
    *,
    html: str = "",
    headers: dict[str, str] | None = None,
    js_globals: list[str] | None = None,
    cookies: dict[str, str] | None = None,
    url: str = "",
) -> str:
    from .models import SignalSource as SS

    if source == SS.HTML:
        return html
    if source == SS.HEADER:
        return extract_headers(headers or {}, "")
    if source == SS.META:
        return extract_meta(html)
    if source == SS.COOKIE:
        return extract_cookies(cookies or {})
    if source == SS.JS_GLOBAL:
        return extract_js_globals(js_globals or [])
    if source == SS.URL:
        return url
    return ""
