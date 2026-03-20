# tests/shared/conftest.py
"""
Add repo root to sys.path so shared.* and ai_pattern_scrubber are importable.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
