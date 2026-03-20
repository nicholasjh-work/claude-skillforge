# shared/ai_pattern_scrubber.py
# Shim: re-export the detect_patterns API from the canonical mock_detector
# so tests can import `from ai_pattern_scrubber import detect_patterns`.
from shared.mock_detector import detect_patterns, PatternHit, extract_facts, annotate_text

__all__ = ["detect_patterns", "PatternHit", "extract_facts", "annotate_text"]
