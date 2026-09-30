"""Rule matcher — applies a list of Rules against extracted evidence."""
from __future__ import annotations

import re
from typing import Iterable

from .models import Detection, DetectionResult, Rule, Signal
from .sources import get_evidence


def _match_signal(
    sig: Signal,
    *,
    html: str,
    headers: dict[str, str],
    js_globals: list[str],
    cookies: dict[str, str],
    url: str,
) -> bool:
    evidence = get_evidence(
        sig.source,
        html=html,
        headers=headers,
        js_globals=js_globals,
        cookies=cookies,
        url=url,
    )
    return bool(re.search(sig.pattern, evidence, re.IGNORECASE | re.DOTALL))


def _run_rules(
    rules: Iterable[Rule],
    *,
    html: str,
    headers: dict[str, str],
    js_globals: list[str],
    cookies: dict[str, str],
    url: str,
) -> dict[str, Detection]:
    """Returns map of name → Detection for matched rules."""
    matched: dict[str, Detection] = {}

    for rule in rules:
        if not rule.signals:
            continue
        signal_hits = [
            sig
            for sig in rule.signals
            if _match_signal(sig, html=html, headers=headers, js_globals=js_globals, cookies=cookies, url=url)
        ]
        if not signal_hits:
            continue
        # Confidence: max of any matching signal's confidence
        confidence = max(s.confidence for s in signal_hits)
        matched[rule.name] = Detection(
            name=rule.name,
            category=rule.category,
            confidence=confidence,
            website=rule.website,
        )
        for implied_name in rule.implies:
            if implied_name not in matched:
                matched[implied_name] = Detection(
                    name=implied_name,
                    category=rule.category,
                    confidence=confidence,
                    implied=True,
                )

    return matched


def run_detection(
    rules: list[Rule],
    *,
    url: str = "",
    html: str = "",
    headers: dict[str, str] | None = None,
    js_globals: list[str] | None = None,
    cookies: dict[str, str] | None = None,
) -> DetectionResult:
    matched = _run_rules(
        rules,
        html=html,
        headers=headers or {},
        js_globals=js_globals or [],
        cookies=cookies or {},
        url=url,
    )
    detections = sorted(matched.values(), key=lambda d: (-d.confidence, d.name))
    return DetectionResult(url=url, detections=detections)
