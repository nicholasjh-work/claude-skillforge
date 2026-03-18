# tests/shared/test_fact_preservation.py
"""
Fact preservation tests: named entities, numeric claims, and dates
present in the input must also be present in the rewritten output.

These tests verify the contract:
  "PRESERVE THESE FACTS: [list] — do not alter, omit, or fabricate"

Since these tests operate on pipeline outputs rather than the scrubber alone,
they use the humanizer_flow.pipeline module to generate a rewrite and then
check that each fact is still present.

Set MOCK_SCRUBBER=1 to run without a live LLM (scrubber will be mocked;
pipeline rewrite assertions are skipped in mock mode).
"""

import os
import re
import pytest


FACT_CASES = [
    {
        "id": "dates",
        "text": "The company was founded in 1994 and went public in 2001.",
        "preserve_facts": ["1994", "2001"],
    },
    {
        "id": "metrics",
        "text": "Latency dropped from 480ms to 120ms after the refactor.",
        "preserve_facts": ["480ms", "120ms"],
    },
    {
        "id": "proper_nouns",
        "text": "Priya Patel joined Stripe as a Staff Engineer in Q3 2023.",
        "preserve_facts": ["Priya Patel", "Stripe", "Q3 2023"],
    },
    {
        "id": "dollar_amounts",
        "text": "The migration saved $144,000 per year in provider fees.",
        "preserve_facts": ["$144,000"],
    },
]


def facts_present_in_text(facts: list[str], text: str) -> dict:
    """Returns {fact: found_bool} for each fact."""
    return {f: f in text for f in facts}


class TestFactPreservation:

    @pytest.mark.parametrize("case", FACT_CASES, ids=[c["id"] for c in FACT_CASES])
    def test_facts_present_in_input(self, case):
        """Sanity check: all facts must exist in the original text."""
        result = facts_present_in_text(case["preserve_facts"], case["text"])
        missing = [f for f, found in result.items() if not found]
        assert not missing, f"Test setup error — facts not in input: {missing}"

    @pytest.mark.skipif(
        os.environ.get("MOCK_SCRUBBER") == "1",
        reason="Pipeline rewrite not available in mock mode"
    )
    @pytest.mark.parametrize("case", FACT_CASES, ids=[c["id"] for c in FACT_CASES])
    def test_facts_preserved_after_rewrite(self, case):
        """After a full pipeline rewrite, all preserve_facts must still be present."""
        try:
            from humanizer_flow.pipeline import run_pipeline
        except ImportError:
            pytest.skip("humanizer_flow not installed")

        result = run_pipeline(
            text=case["text"],
            preserve_facts=case["preserve_facts"],
            tone="direct",
            profile="default",
        )
        final_text = result.get("final", result.get("draft", ""))
        check = facts_present_in_text(case["preserve_facts"], final_text)
        missing = [f for f, found in check.items() if not found]
        assert not missing, (
            f"Facts lost in rewrite for case '{case['id']}': {missing}\n"
            f"Final text: {final_text}"
        )
