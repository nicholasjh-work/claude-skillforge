# tests/conftest.py
"""
Shared pytest fixtures and mock scrubber setup.

Set MOCK_SCRUBBER=1 to run without the real ai_pattern_scrubber implementation.
The mock returns deterministic fixture-based hits for known test inputs.
"""

import sys
from pathlib import Path

# Add repo root to sys.path so shared.* and ai_pattern_scrubber are importable.
sys.path.insert(0, str(Path(__file__).parent.parent))

import os
import pytest
from unittest.mock import patch, MagicMock


# ─────────────────────────────────────────────
# Mock scrubber
# ─────────────────────────────────────────────

def make_mock_hit(id, label, severity, category, text, span_start=0):
    from dataclasses import dataclass
    from typing import Literal

    @dataclass
    class MockHit:
        id: int
        label: str
        span_start: int
        span_end: int
        severity: str
        confidence: float
        rationale: str
        matched_text: str
        category: str

    return MockHit(
        id=id,
        label=label,
        span_start=span_start,
        span_end=span_start + len(text),
        severity=severity,
        confidence=1.0,
        rationale=f"Mock hit for pattern {id}",
        matched_text=text,
        category=category,
    )


@pytest.fixture(autouse=True)
def maybe_mock_scrubber():
    """If MOCK_SCRUBBER=1 is set, patch detect_patterns with a simple stub."""
    if os.environ.get("MOCK_SCRUBBER") == "1":
        mock_hits = [
            make_mock_hit(7, "Overused AI Vocabulary", "high", "LANGUAGE", "delve"),
            make_mock_hit(13, "Em Dash Overuse", "high", "STYLE", "\u2014"),
            make_mock_hit(19, "Collaborative Communication Artifacts", "high", "COMMUNICATION", "I hope this helps"),
            make_mock_hit(21, "Sycophantic Tone", "high", "COMMUNICATION", "Great question"),
            make_mock_hit(24, "Generic Positive Conclusions", "high", "FILLER", "The future looks bright"),
        ]
        with patch("ai_pattern_scrubber.detect_patterns", return_value=mock_hits):
            yield
    else:
        yield


# ─────────────────────────────────────────────
# Shared fixtures
# ─────────────────────────────────────────────

SYNTHETIC_AI_DOC = """
Great question! Here is an overview of AI coding tools. I hope this helps!

AI-assisted coding serves as an enduring testament to the transformative potential of large language
models, marking a pivotal moment in the evolution of software development. In today's rapidly
evolving technological landscape, these groundbreaking tools\u2014nestled at the intersection of
research and practice\u2014are reshaping how engineers ideate, iterate, and deliver, underscoring
their vital role in modern workflows.

The value proposition is clear: streamlining processes, enhancing collaboration, and fostering
alignment. It's not just about autocomplete; it's about unlocking creativity at scale.
The tool serves as a catalyst. The assistant functions as a partner. The system stands as a
foundation for innovation.

Industry observers have noted that adoption has accelerated from hobbyist experiments to
enterprise-wide rollouts. The technology has been featured in The New York Times, Wired, and
The Verge. Additionally, the ability to generate documentation, tests, and refactors showcases
how AI can contribute to better outcomes, highlighting the intricate interplay between automation
and human judgment.

- \U0001F680 **Speed:** Code generation is significantly faster, reducing friction.
- \U0001F4A1 **Quality:** Output quality has been enhanced through improved training.
- \u2705 **Adoption:** Usage continues to grow, reflecting broader industry trends.

While specific details are limited based on available information, it could potentially possibly
be argued that these tools might have some positive effect. In order to fully realize this
potential, teams must align with best practices. He said \u201cresults speak for themselves.\u201d

In conclusion, the future looks bright. Exciting times lie ahead as we continue this journey
toward excellence. Let me know if you'd like me to expand on any section!
""".strip()

CLEAN_HUMAN_DOC = """
I've been using AI coding tools for about two years. The honest take: they're good at boilerplate
and bad at understanding intent. Autocomplete is useful. The "explain this code" feature is
occasionally useful. The "write this function from a description" feature works about 40% of the
time without needing significant editing.

The dangerous part is how natural the suggestions look. I've accepted code that compiled, passed
lint, and passed tests, only to catch later that it solved the wrong problem because I stopped
paying close attention.

If you treat it like a very fast junior engineer who needs code review on everything, it's useful.
If you treat it like a senior engineer you can trust, it will help you ship bugs faster.
""".strip()


@pytest.fixture
def synthetic_ai_doc():
    return SYNTHETIC_AI_DOC


@pytest.fixture
def clean_human_doc():
    return CLEAN_HUMAN_DOC
