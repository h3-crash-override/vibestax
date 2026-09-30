"""vibestax — Apache 2.0 web technology fingerprinting library."""
from __future__ import annotations

from .engine import run_detection
from .models import Detection, DetectionResult, Rule, Signal, SignalSource
from .rules import ALL_RULES

__version__ = "0.1.0"
__all__ = [
    "detect",
    "detect_from_page",
    "ALL_RULES",
    "Detection",
    "DetectionResult",
    "Rule",
    "Signal",
    "SignalSource",
]


def detect(
    url: str = "",
    html: str = "",
    headers: dict[str, str] | None = None,
    js_globals: list[str] | None = None,
    cookies: dict[str, str] | None = None,
    rules: list[Rule] | None = None,
) -> DetectionResult:
    """Detect web technologies from pre-fetched page content.

    Args:
        url: Final URL after redirects.
        html: Rendered HTML body.
        headers: HTTP response headers (case-insensitive keys OK).
        js_globals: List of global variable names visible on window (optional; requires browser).
        cookies: Cookie jar as name→value dict.
        rules: Override the built-in rule set (defaults to ALL_RULES).

    Returns:
        DetectionResult with .detections and .categories.
    """
    return run_detection(
        rules if rules is not None else ALL_RULES,
        url=url,
        html=html,
        headers={k.lower(): v for k, v in (headers or {}).items()},
        js_globals=js_globals,
        cookies=cookies,
    )


async def detect_from_page(page: object, rules: list[Rule] | None = None) -> DetectionResult:
    """Detect technologies from a live Playwright Page object.

    Requires the `playwright` optional dependency:
        pip install vibestax[playwright]

    Args:
        page: A Playwright `Page` object after navigation.
        rules: Override the built-in rule set.

    Returns:
        DetectionResult with .detections and .categories.
    """
    try:
        from playwright.async_api import Page as _Page  # noqa: F401
    except ImportError as exc:
        raise ImportError(
            "Playwright is required for detect_from_page. "
            "Install it with: pip install vibestax[playwright]"
        ) from exc

    html: str = await page.content()
    url: str = page.url

    # Capture response headers from the last main-frame navigation
    headers: dict[str, str] = {}
    try:
        response = await page.evaluate(
            "() => { "
            "  const e = performance.getEntriesByType('navigation')[0]; "
            "  return e ? e.responseStart : 0; "
            "}"
        )
    except Exception:
        pass  # header capture is best-effort

    # Enumerate window.* globals
    try:
        js_globals: list[str] = await page.evaluate(
            "() => Object.getOwnPropertyNames(window)"
        )
    except Exception:
        js_globals = []

    # Capture cookies
    try:
        raw_cookies = await page.context.cookies(urls=[url])
        cookies = {c["name"]: c["value"] for c in raw_cookies}
    except Exception:
        cookies = {}

    return detect(
        url=url,
        html=html,
        headers=headers,
        js_globals=js_globals,
        cookies=cookies,
        rules=rules,
    )
