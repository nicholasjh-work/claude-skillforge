# ai_pattern_scrubber.py
# Shim at repo root: re-exports the detect_patterns API from shared/mock_detector.py
# so tests can import `from ai_pattern_scrubber import detect_patterns`.
from shared.mock_detector import detect_patterns, PatternHit, annotate_text

__all__ = ["detect_patterns", "PatternHit", "annotate_text"]
