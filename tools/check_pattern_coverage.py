#!/usr/bin/env python3
"""
tools/check_pattern_coverage.py

Runs ai-pattern-scrubber against one or more fixture files and reports
pattern coverage. Exits non-zero if coverage is below --threshold.

Usage:
    python tools/check_pattern_coverage.py \\
        --fixture tests/fixtures/synthetic_ai_doc.txt \\
        --threshold 0.9

    python tools/check_pattern_coverage.py \\
        --fixture skills/email-writer/examples/short.json \\
        --fixture skills/email-writer/examples/medium.json \\
        --threshold 0.9
"""

import argparse
import json
import sys
from pathlib import Path

# Adjust sys.path so the package is importable from repo root
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from ai_pattern_scrubber import detect_patterns
except ImportError as e:
    print(f"ERROR: Could not import ai_pattern_scrubber: {e}", file=sys.stderr)
    print("If running in CI with a mock, set MOCK_SCRUBBER=1", file=sys.stderr)
    sys.exit(2)


TOTAL_PATTERNS = 24


def load_fixture(path: str) -> str:
    """Load text from a .txt or .json fixture file."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Fixture not found: {path}")

    if p.suffix == ".json":
        data = json.loads(p.read_text(encoding="utf-8"))
        # Support both {"text": "..."} and {"input": {"text": "..."}}
        if "text" in data:
            return data["text"]
        elif "input" in data and "text" in data["input"]:
            return data["input"]["text"]
        elif "before" in data:
            return data["before"]
        else:
            return json.dumps(data)  # fallback: use raw JSON as text
    else:
        return p.read_text(encoding="utf-8")


def check_coverage(fixtures: list[str], threshold: float) -> int:
    """
    Returns 0 if coverage >= threshold, 1 if below, 2 on error.
    """
    all_text = "\n\n".join(load_fixture(f) for f in fixtures)
    hits = detect_patterns(all_text)
    detected_ids = {h.id for h in hits}
    coverage = len(detected_ids) / TOTAL_PATTERNS

    print(f"\n{'='*60}")
    print(f"Pattern Coverage Report")
    print(f"{'='*60}")
    print(f"Fixtures:        {', '.join(fixtures)}")
    print(f"Total patterns:  {TOTAL_PATTERNS}")
    print(f"Detected:        {len(detected_ids)} — {sorted(detected_ids)}")
    missing = set(range(1, TOTAL_PATTERNS + 1)) - detected_ids
    if missing:
        print(f"Missing:         {sorted(missing)}")
    print(f"Coverage:        {coverage:.1%}  (threshold: {threshold:.1%})")
    print(f"Total hits:      {len(hits)}")

    sev_counter = {"low": 0, "med": 0, "high": 0}
    for h in hits:
        sev_counter[h.severity] += 1
    print(f"Severity dist:   high={sev_counter['high']}  med={sev_counter['med']}  low={sev_counter['low']}")
    print(f"{'='*60}")

    if coverage >= threshold:
        print(f"PASS — coverage {coverage:.1%} meets threshold {threshold:.1%}")
        return 0
    else:
        print(
            f"FAIL — coverage {coverage:.1%} is below threshold {threshold:.1%}. "
            f"Missing patterns: {sorted(missing)}",
            file=sys.stderr,
        )
        return 1


def main():
    parser = argparse.ArgumentParser(description="Check ai-pattern-scrubber coverage on fixtures.")
    parser.add_argument(
        "--fixture",
        action="append",
        required=True,
        metavar="PATH",
        help="Path to a .txt or .json fixture file. Can be specified multiple times.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.9,
        help="Minimum coverage fraction (default: 0.9)",
    )
    args = parser.parse_args()

    try:
        exit_code = check_coverage(args.fixture, args.threshold)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        exit_code = 2
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}", file=sys.stderr)
        exit_code = 2

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
