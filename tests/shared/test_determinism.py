# tests/shared/test_determinism.py
"""
Determinism tests: same input must produce identical output
on repeated calls to detect_patterns (temperature=0.0 contract).

These tests run detect_patterns twice on the same input and
assert the outputs are identical — same hits, same spans, same order.
"""

import pytest
from ai_pattern_scrubber import detect_patterns


DETERMINISM_CASES = [
    "Great question! Here is an overview. I hope this helps! The future looks bright.",
    "The system serves as a pivotal testament to the transformative potential of AI tools, underscoring their vital role.",
    "It could potentially possibly be argued this might have some effect on outcomes going forward.",
]


class TestDeterminism:

    @pytest.mark.parametrize("text", DETERMINISM_CASES)
    def test_same_input_same_hits(self, text):
        hits_a = detect_patterns(text)
        hits_b = detect_patterns(text)

        assert len(hits_a) == len(hits_b), (
            f"Hit count changed between runs: {len(hits_a)} vs {len(hits_b)}"
        )
        for a, b in zip(hits_a, hits_b):
            assert a.id == b.id
            assert a.span_start == b.span_start
            assert a.span_end == b.span_end
            assert a.severity == b.severity
            assert a.confidence == b.confidence

    def test_empty_input_deterministic(self):
        assert detect_patterns("") == detect_patterns("")

    def test_hit_order_deterministic(self, synthetic_ai_doc):
        hits_a = detect_patterns(synthetic_ai_doc)
        hits_b = detect_patterns(synthetic_ai_doc)
        assert [h.id for h in hits_a] == [h.id for h in hits_b]
        assert [h.span_start for h in hits_a] == [h.span_start for h in hits_b]
