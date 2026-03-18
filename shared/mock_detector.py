"""
Pattern detection module for AI prose scrubbing.

Conforms to SPEC.md Section 2 API contract.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class PatternHit:
    """Detected pattern occurrence in text."""
    pattern_id: int
    pattern_name: str
    matched_text: str
    start: int
    end: int
    severity: str  # 'low', 'med', 'high'
    confidence: float
    suggested_fix: str
    context: str


def detect_patterns(text: str) -> List[PatternHit]:
    """
    Detect AI writing patterns in prose.

    Args:
        text: Input text to analyze

    Returns:
        List of PatternHit objects for detected patterns
    """
    # Stub implementation: returns empty list to unblock CI
    # Full implementation pending SPEC.md Section 5 heuristics
    return []


def annotate_text(text: str, hits: List[PatternHit]) -> str:
    """
    Annotate text with detected pattern markers.

    Args:
        text: Original text
        hits: List of detected patterns

    Returns:
        Annotated text with pattern markers
    """
    # Stub implementation
    return text
