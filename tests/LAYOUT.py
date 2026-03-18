# tests/shared/ — Shared Component Tests
# tests/skills/ — Per-Skill Example Tests

# This file documents the tests/ directory layout.
# Each file is described with its purpose and location.

"""
tests/
├── conftest.py                          — shared fixtures, mock scrubber, patch env vars
├── fixtures/
│   ├── synthetic_ai_doc.txt             — 300-word doc with all 24 patterns (integration fixture)
│   ├── clean_human_doc.txt              — human-authored text (adversarial: should have 0 high-severity hits)
│   └── resume_bullets_before.json       — 20 raw bullets for resume test pipeline
│
├── shared/
│   ├── test_scrubber.py                 — 30 unit tests (patterns 1-24 + 6 adversarial) — FROM SPEC.md
│   ├── test_integration_pipeline.py     — coverage >= 0.9 integration test — FROM SPEC.md
│   ├── test_nick_mode.py                — 12 nick-mode rule tests — FROM nick-mode README.md
│   ├── test_resume_banned.py            — 20 resume banned phrase tests — FROM resume-banned README.md
│   ├── test_determinism.py              — same input -> same hit list at temp=0.0
│   └── test_fact_preservation.py        — entities/dates/metrics in -> entities/dates/metrics out
│
└── skills/
    ├── test_email_writer.py             — 3 stubs: short/medium/long, no high-severity
    ├── test_correction_email_writer.py
    ├── test_resume_writer.py
    ├── test_resume_editor.py
    ├── test_technical_writer.py
    ├── test_incident_summary_writer.py
    ├── test_stakeholder_update_writer.py
    ├── test_requirements_doc_writer.py
    ├── test_meeting_notes_to_decision_memo.py
    ├── test_linkedin_message_writer.py
    ├── test_cover_letter_writer.py
    ├── test_resume_bullet_rewriter.py
    ├── test_executive_brief_writer.py
    └── test_executive_summary_writer.py
"""
