from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class SignalSource(str, Enum):
    HTML = "html"        # rendered HTML body
    HEADER = "header"    # HTTP response headers
    JS_GLOBAL = "js"     # window.* globals (requires browser)
    META = "meta"        # <meta> tag attributes
    COOKIE = "cookie"    # cookie names/values
    URL = "url"          # final URL


@dataclass
class Signal:
    source: SignalSource
    pattern: str          # regex; matched case-insensitively
    confidence: int = 100 # how confident this single signal makes the detection (1–100)


@dataclass
class Rule:
    name: str
    category: str
    signals: list[Signal] = field(default_factory=list)
    implies: list[str] = field(default_factory=list)  # tech names auto-added when this rule matches
    website: str = ""


@dataclass
class Detection:
    name: str
    category: str
    confidence: int  # 1–100
    implied: bool = False
    website: str = ""


@dataclass
class DetectionResult:
    url: str
    detections: list[Detection]

    @property
    def categories(self) -> dict[str, list[Detection]]:
        result: dict[str, list[Detection]] = {}
        for d in self.detections:
            result.setdefault(d.category, []).append(d)
        return result

    def names(self) -> list[str]:
        return [d.name for d in self.detections]

    def has(self, name: str) -> bool:
        return any(d.name == name for d in self.detections)
