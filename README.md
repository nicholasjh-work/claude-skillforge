# writing-skills

A mono-repo of Claude Code writing skills powered by the [Humanizer](https://github.com/blader/humanizer) two-pass AI-pattern removal flow.

---

## What's in here

```
shared/
  ai-pattern-scrubber/    — 24-pattern heuristic detection library + SPEC.md
  nick-mode-writing-standard/ — Machine-readable style rules + validation API
  resume-banned-language-pack/ — 20 banned phrases with metric-required replacements
  humanizer-flow/         — Reusable two-pass prompt flow template

skills/
  email-writer/
  correction-email-writer/
  resume-writer/
  resume-editor/
  technical-writer/
  incident-summary-writer/
  stakeholder-update-writer/
  requirements-doc-writer/
  meeting-notes-to-decision-memo/
  linkedin-message-writer/
  cover-letter-writer/
  resume-bullet-rewriter/
  executive-brief-writer/
  executive-summary-writer/

tests/
  shared/                 — Unit + integration tests for shared components
  skills/                 — Per-skill example validation tests

tools/
  check_pattern_coverage.py — Coverage reporter (exit 1 if below threshold)

.github/workflows/ci.yml  — CI with per-skill matrix jobs
EVAL_PLAN.md              — Human evaluation protocol (3 raters x 50 examples)
```

---

## Quick start

### Install a skill into Claude Code

```bash
./install-skill.sh email-writer
# copies skills/email-writer/ to ~/.claude/skills/email-writer/
```

### Use in Claude Code

```
/email-writer [paste your draft or notes]
```

---

## Install instructions

### Prerequisites

- Claude Code (`claude` CLI installed and authenticated)
- Python 3.11+ (for local tests and coverage tool)

### 1. Clone the repo

```bash
git clone https://github.com/nickhidalgo/writing-skills.git
cd writing-skills
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install a skill

```bash
./install-skill.sh <skill-name>
```

### 4. Run all shared tests locally

```bash
pytest tests/shared/ -v
```

### 5. Run pattern coverage check

```bash
python tools/check_pattern_coverage.py \
    --fixture tests/fixtures/synthetic_ai_doc.txt \
    --threshold 0.9
```

---

## Running with a mock scrubber (no API key required)

```bash
MOCK_SCRUBBER=1 pytest tests/ -v
```

---

## Components

| Component | Humanizer Patterns | Purpose |
|---|---|---|
| `ai-pattern-scrubber` | 1-24 | Detect all 24 AI-writing patterns |
| `nick-mode-writing-standard` | 1,4,7,8,13,19,21,22,23,24 | Enforce profile-specific style rules |
| `resume-banned-language-pack` | 1,4,5,7,8,19,21,24 | Hard-reject resume cliches |
| `humanizer-flow` | 1-24 (all) | Two-pass rewrite orchestrator |

---

## License

MIT