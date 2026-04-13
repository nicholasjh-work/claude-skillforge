# Rationale and References

This repository contains AI operating standards used to guide code generation, troubleshooting, data work, and technical documentation in Claude sessions.

These standards are split into two categories.

---

## 1. Standards-backed rules

These rules are grounded in published engineering guidance and vendor documentation.

### Coding and comments

**Rule:** Sparse, non-obvious comments only. Self-documenting code through clear naming and small functions.

**Source:** PEP 8 Style Guide for Python Code. PEP 8 states that inline comments should be used sparingly and that comments contradicting the code are worse than no comments. It advises against stating the obvious.

**URL:** https://peps.python.org/pep-0008/#comments

---

### Configuration and secrets

**Rule:** Never hardcode secrets. Use environment variables as the application interface for configuration. Keep real secret values out of source control and, for persistent or production systems, prefer managed secret storage and rotation.

**Sources:**
- Twelve-Factor App, Factor III (Config). Recommends strict separation of config from code and storing config in environment variables.
- OWASP Secrets Management Cheat Sheet. Recommends centralized secret management, auditing, rotation, and controlled access for production secrets.

**URLs:**
- https://12factor.net/config
- https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

---

### Python data models

**Rule:** Use dataclasses for lightweight internal models. Use Pydantic for external contracts, validation, API schemas, and settings.

**Sources:**
- Python standard library dataclasses documentation.
- Pydantic V2 documentation for validation models and typed contracts.

**URLs:**
- https://docs.python.org/3/library/dataclasses.html
- https://docs.pydantic.dev/latest/

---

### dbt structure and testing

**Rule:** Separate raw, staging, intermediate, and mart layers. Define tests (unique, not_null, accepted_values, relationships) in YAML.

**Sources:**
- dbt best practices: How we structure our dbt projects.
- dbt documentation: Data tests.

**URLs:**
- https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview
- https://docs.getdbt.com/docs/build/data-tests

---

### BI semantic modeling

**Rule:** Use star schema design. Govern fact tables, dimensions, join types, filter propagation, and semantic layer concerns. Prioritize correctness of business definitions.

**Source:** Microsoft Power BI documentation on star schema design and model relationships.

**URLs:**
- https://learn.microsoft.com/en-us/power-bi/guidance/star-schema
- https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand

---

### SQL parameterization

**Rule:** Parameterize all SQL values. Never build value-bearing queries through string concatenation. If dynamic identifiers are unavoidable, validate against an allowlist.

**Source:** OWASP SQL Injection Prevention Cheat Sheet.

**URL:** https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

---

### Python tooling

**Rule:** Use ruff for linting, formatting, and import sorting. Use mypy in strict mode.

**Sources:**
- Ruff documentation (Astral). Ruff is a fast Python linter and formatter that replaces flake8, isort, and black in a single tool.
- mypy documentation for static type checking.

**URLs:**
- https://docs.astral.sh/ruff/
- https://mypy.readthedocs.io/en/stable/

---

## 2. House operating conventions

These are intentional working preferences for AI-assisted engineering in this repository. They are not claimed as universal industry standards. They are repository-specific operating decisions intended to improve consistency, clarity, and maintainability.

- Lead with the answer before providing context or explanation
- Prefer narrow fixes over refactors during troubleshooting
- Avoid AI-style comment patterns: banner sections, decorative separators, narrative inline comments
- No file headers in repo code (dbt models, app modules, components)
- Use purpose headers only for standalone artifacts where context helps
- Use fixed output structures for code delivery (Answer, Code, Tests, Run, Notes) and troubleshooting (Answer, Cause, Fix, Code, Validation, Expected result, Caveats)
- Ask at most one clarifying question per response
- No em dashes in output
- Prefer SQL for set-based data work, Python for orchestration and integration
- Treat metric definitions as governed assets
- Flag grain mismatches explicitly

---

## Maintenance

This document is updated when skill rules change or new standards are adopted. Last updated: April 2026.
