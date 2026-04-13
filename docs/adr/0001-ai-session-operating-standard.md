# ADR-0001: AI Session Operating Standard

**Status:** Accepted
**Date:** April 2026
**Author:** Nicholas Hidalgo

## Context

Working with Claude across enterprise analytics, data engineering, and professional writing tasks requires consistent behavior session to session. Without explicit operating standards, AI outputs drift toward generic patterns: verbose explanations, hedged recommendations, AI-style comment clutter, and inconsistent output structure.

This creates rework. Every session starts cold. Every output needs manual cleanup. The feedback loop is expensive.

## Decision

Define two complementary skill files that govern all Claude sessions:

1. **claude-operator-standard**: Universal rules for communication, troubleshooting, output format, session behavior, and handoff protocol. Loads in every conversation regardless of task type.

2. **claude-code-standard**: Technical execution rules for code generation, SQL, Python, dbt, analytics engineering, and BI work. Loads only when triggered by coding or data tasks. Assumes the operator standard is already active and does not duplicate its rules.

This separation keeps non-coding conversations lightweight (operator standard only, ~8K chars) while giving coding sessions full coverage (both skills, ~15K chars total).

## Consequences

**Benefits:**
- Consistent output quality across sessions without repeating instructions
- Reduced token cost compared to a single monolithic prompt
- Skills load independently and do not conflict
- New domain skills (writing, career) can layer on top without modifying the core pair
- Portable across Claude.ai, Claude Code, and API integrations

**Tradeoffs:**
- Two files to maintain instead of one
- Cross-reference dependency: the code standard assumes the operator standard exists
- Skill descriptions must be precise enough for Claude's routing to trigger correctly

**Risks mitigated:**
- Output drift over long sessions (operator standard enforces session behavior rules)
- Duplicate or conflicting instructions (deduplication is explicit in the code standard header)
- Token waste from loading irrelevant rules (progressive disclosure by design)

## Alternatives considered

**Single monolithic prompt:** Simpler to maintain, but forces every conversation to carry coding rules even for email drafting or planning tasks. Higher token cost, more noise.

**No explicit standards (rely on userPreferences only):** userPreferences ship in every message (~800+ tokens for detailed instructions). Skills load on demand and cost ~100 tokens until activated. Skills are also version-controlled and shareable.

## References

- [docs/rationale-and-references.md](../rationale-and-references.md) for standards-backed justification of individual rules
