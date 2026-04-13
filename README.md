<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/nh-logo-dark.svg" width="120">
  <source media="(prefers-color-scheme: light)" srcset="assets/nh-logo-light.svg" width="120">
  <img alt="Hidalgo Systems Labs" src="assets/nh-logo-light.svg" width="120">
</picture>

<h1 align="center">Claude Skillforge</h1>
<p align="center"><b>Production-ready Claude Skills you can install and use. Not a list. A library.</b></p>

<p align="center">
  <a href="https://github.com/nicholasjh-work/claude-skillforge/actions/workflows/ci.yml"><img src="https://github.com/nicholasjh-work/claude-skillforge/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/nicholasjh-work/claude-skillforge/actions/workflows/skill-lint.yml"><img src="https://github.com/nicholasjh-work/claude-skillforge/actions/workflows/skill-lint.yml/badge.svg" alt="Skill Lint"></a>
  <a href="https://github.com/nicholasjh-work/claude-skillforge/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/nicholasjh-work/claude-skillforge/stargazers"><img src="https://img.shields.io/github/stars/nicholasjh-work/claude-skillforge?style=for-the-badge" alt="Stars"></a>
</p>

---

### What is this?

Claude Skillforge is a library of 30 battle-tested Claude Skills built for enterprise analytics, data engineering, professional writing, and career tools. Every skill in this repo has been used in production workflows, not written as a demo.

Skills are instruction files that teach Claude how to perform specific tasks in a repeatable, high-quality way. They load on demand and cost roughly 100 tokens until activated.

---

### What are Claude Skills?

Claude Skills are specialized instruction folders that Claude dynamically discovers and loads when relevant to a task. Each skill contains a `SKILL.md` file with YAML frontmatter (name and description for routing) and detailed execution instructions.

Skills use progressive disclosure: Claude scans metadata first (~100 tokens), loads full instructions only when the skill matches (~2-5K tokens), and accesses bundled resources only as needed. Multiple skills can be active simultaneously without overwhelming the context window.

---

### How to install

**Claude.ai (Web/Desktop)**
1. Go to Settings > Capabilities > Skills
2. Upload skill folders or point to this repository

**Claude Code (CLI)**
```bash
git clone https://github.com/nicholasjh-work/claude-skillforge.git
# Copy desired skill folders into your project's .claude/skills/ directory
```

**Manual**
Copy any skill folder into your Claude skills directory. Each folder is self-contained.

---

### Core

Foundational operating standards that govern how Claude behaves across all tasks.

<p>
  <a href="core/claude-operator-standard/"><img src="https://img.shields.io/badge/claude--operator--standard-0550ae?style=for-the-badge" alt="claude-operator-standard"></a>&nbsp;
  <a href="core/claude-code-standard/"><img src="https://img.shields.io/badge/claude--code--standard-0550ae?style=for-the-badge" alt="claude-code-standard"></a>&nbsp;
  <a href="core/claude-session-handoff/"><img src="https://img.shields.io/badge/claude--session--handoff-0550ae?style=for-the-badge" alt="claude-session-handoff"></a>
</p>

| Skill | What it does |
|---|---|
| **claude-operator-standard** | Universal operating standard for Claude sessions. Governs communication style, troubleshooting method, output format, session behavior, and handoff protocol. |
| **claude-code-standard** | Technical execution standard for coding, SQL, Python, dbt, and data engineering. Covers stack preferences, documentation rules, testing, and analytics engineering guidance. |
| **claude-session-handoff** | Generates a structured handoff block that captures full technical state so a conversation can continue in a new window with zero re-explanation. |

---

### Data Engineering

Tools for data quality, SQL, reporting, KPI governance, and analytics engineering.

<p>
  <a href="data-engineering/data-defect-investigator/"><img src="https://img.shields.io/badge/data--defect--investigator-0d6e3f?style=for-the-badge" alt="data-defect-investigator"></a>&nbsp;
  <a href="data-engineering/data-file-profiler/"><img src="https://img.shields.io/badge/data--file--profiler-0d6e3f?style=for-the-badge" alt="data-file-profiler"></a>&nbsp;
  <a href="data-engineering/dataset-reconciler/"><img src="https://img.shields.io/badge/dataset--reconciler-0d6e3f?style=for-the-badge" alt="dataset-reconciler"></a>&nbsp;
  <a href="data-engineering/report-output-validator/"><img src="https://img.shields.io/badge/report--output--validator-0d6e3f?style=for-the-badge" alt="report-output-validator"></a>&nbsp;
  <a href="data-engineering/sql-join-risk-reviewer/"><img src="https://img.shields.io/badge/sql--join--risk--reviewer-0d6e3f?style=for-the-badge" alt="sql-join-risk-reviewer"></a>&nbsp;
  <a href="data-engineering/sql-report-query-builder/"><img src="https://img.shields.io/badge/sql--report--query--builder-0d6e3f?style=for-the-badge" alt="sql-report-query-builder"></a>&nbsp;
  <a href="data-engineering/kpi-definition-standard/"><img src="https://img.shields.io/badge/kpi--definition--standard-0d6e3f?style=for-the-badge" alt="kpi-definition-standard"></a>&nbsp;
  <a href="data-engineering/report-requirements-translator/"><img src="https://img.shields.io/badge/report--requirements--translator-0d6e3f?style=for-the-badge" alt="report-requirements-translator"></a>
</p>

| Skill | What it does |
|---|---|
| **data-defect-investigator** | Investigates data defects, mismatches, duplicates, null issues, broken joins, and reconciliation failures. |
| **data-file-profiler** | Profiles CSV/Excel files: schema inspection, duplicate detection, null analysis, outliers, and data mismatches. |
| **dataset-reconciler** | Compares two datasets and explains count, amount, and field-level differences. Source vs target, old vs new, ERP vs DW. |
| **report-output-validator** | Validates report outputs, totals, grain, subtotals, and regression changes before release. |
| **sql-join-risk-reviewer** | Reviews schemas, joins, and SQL logic for grain violations, duplicate risk, orphan rows, and aggregation errors. |
| **sql-report-query-builder** | Builds production-grade SQL for reporting. Translates business requests into safe, auditable query logic. |
| **kpi-definition-standard** | Defines KPIs with precise formulas, grain, source logic, exclusions, and governance notes. |
| **report-requirements-translator** | Converts messy business requests into clean report or dashboard specifications. |

---

### Writing

Professional and editorial writing tools for business communication, technical documentation, and AI prose cleanup.

<p>
  <a href="writing/business-email-drafter/"><img src="https://img.shields.io/badge/business--email--drafter-b35900?style=for-the-badge" alt="business-email-drafter"></a>&nbsp;
  <a href="writing/correction-email-drafter/"><img src="https://img.shields.io/badge/correction--email--drafter-b35900?style=for-the-badge" alt="correction-email-drafter"></a>&nbsp;
  <a href="writing/cover-letter-drafter/"><img src="https://img.shields.io/badge/cover--letter--drafter-b35900?style=for-the-badge" alt="cover-letter-drafter"></a>&nbsp;
  <a href="writing/linkedin-message-drafter/"><img src="https://img.shields.io/badge/linkedin--message--drafter-b35900?style=for-the-badge" alt="linkedin-message-drafter"></a>&nbsp;
  <a href="writing/executive-brief-drafter/"><img src="https://img.shields.io/badge/executive--brief--drafter-b35900?style=for-the-badge" alt="executive-brief-drafter"></a>&nbsp;
  <a href="writing/technical--to--business--summarizer-b35900?style=for-the-badge" alt="technical-to-business-summarizer"></a>&nbsp;
  <a href="writing/stakeholder-status-update/"><img src="https://img.shields.io/badge/stakeholder--status--update-b35900?style=for-the-badge" alt="stakeholder-status-update"></a>&nbsp;
  <a href="writing/internal-technical-doc-writer/"><img src="https://img.shields.io/badge/internal--technical--doc--writer-b35900?style=for-the-badge" alt="internal-technical-doc-writer"></a>&nbsp;
  <a href="writing/incident-root-cause-writer/"><img src="https://img.shields.io/badge/incident--root--cause--writer-b35900?style=for-the-badge" alt="incident-root-cause-writer"></a>&nbsp;
  <a href="writing/requirements-doc-drafter/"><img src="https://img.shields.io/badge/requirements--doc--drafter-b35900?style=for-the-badge" alt="requirements-doc-drafter"></a>&nbsp;
  <a href="writing/meeting-to-decision-memo/"><img src="https://img.shields.io/badge/meeting--to--decision--memo-b35900?style=for-the-badge" alt="meeting-to-decision-memo"></a>&nbsp;
  <a href="writing/ai-writing-pattern-remover/"><img src="https://img.shields.io/badge/ai--writing--pattern--remover-b35900?style=for-the-badge" alt="ai-writing-pattern-remover"></a>&nbsp;
  <a href="writing/ai-prose-humanizer/"><img src="https://img.shields.io/badge/ai--prose--humanizer-b35900?style=for-the-badge" alt="ai-prose-humanizer"></a>
</p>

| Skill | What it does |
|---|---|
| **business-email-drafter** | Drafts natural business emails that are direct, specific, and free of canned language. |
| **correction-email-drafter** | Writes correction, clarification, and reset emails that are precise, calm, and not defensive. |
| **cover-letter-drafter** | Writes cover letters grounded in real experience and specific to the role. |
| **linkedin-message-drafter** | Writes concise LinkedIn messages for recruiters, hiring managers, and networking. |
| **executive-brief-drafter** | Writes short executive briefs: issue, impact, risk, and next step. |
| **technical-to-business-summarizer** | Translates technical findings into concise business-facing summaries for leadership. |
| **stakeholder-status-update** | Writes concise stakeholder updates on project status, issues, risks, and next steps. |
| **internal-technical-doc-writer** | Writes internal technical documents, SOPs, incident notes, and decision memos. |
| **incident-root-cause-writer** | Writes incident summaries separating facts, impact, root cause, and corrective action. |
| **requirements-doc-drafter** | Writes requirements documents with scope, logic, assumptions, dependencies, and acceptance criteria. |
| **meeting-to-decision-memo** | Converts meeting notes into decision memos with outcomes, owners, and next actions. |
| **ai-writing-pattern-remover** | Detects and removes AI writing patterns based on Wikipedia's "Signs of AI writing" guide. |
| **ai-prose-humanizer** | Removes AI patterns and adds human voice to prose. Two modes: CLEAN for professional docs, VOICE for creative writing. |

---

### Career

Resume optimization, salary negotiation, and job application tools.

<p>
  <a href="career/resume-bullet-rewriter/"><img src="https://img.shields.io/badge/resume--bullet--rewriter-6f42c1?style=for-the-badge" alt="resume-bullet-rewriter"></a>&nbsp;
  <a href="career/resume-bullet-editor/"><img src="https://img.shields.io/badge/resume--bullet--editor-6f42c1?style=for-the-badge" alt="resume-bullet-editor"></a>&nbsp;
  <a href="career/resume-section-writer/"><img src="https://img.shields.io/badge/resume--section--writer-6f42c1?style=for-the-badge" alt="resume-section-writer"></a>&nbsp;
  <a href="career/resume-one-page-optimizer/"><img src="https://img.shields.io/badge/resume--one--page--optimizer-6f42c1?style=for-the-badge" alt="resume-one-page-optimizer"></a>&nbsp;
  <a href="career/resume-two-page-optimizer/"><img src="https://img.shields.io/badge/resume--two--page--optimizer-6f42c1?style=for-the-badge" alt="resume-two-page-optimizer"></a>&nbsp;
  <a href="career/salary-negotiation-framework/"><img src="https://img.shields.io/badge/salary--negotiation--framework-6f42c1?style=for-the-badge" alt="salary-negotiation-framework"></a>
</p>

| Skill | What it does |
|---|---|
| **resume-bullet-rewriter** | Rewrites a single resume bullet to be metric-backed, action-verb-led, and free of banned phrases. |
| **resume-bullet-editor** | Edits existing resume bullets to remove banned language, add metrics, and strengthen impact. |
| **resume-section-writer** | Writes resume sections from raw notes, brain dumps, or bullet lists. |
| **resume-one-page-optimizer** | ATS-optimized one-page resume evaluator and rewriter. Scores, gaps, and full rewrite against a job description. |
| **resume-two-page-optimizer** | ATS-optimized two-page resume evaluator for senior/director/VP roles. |
| **salary-negotiation-framework** | Data-driven salary and total compensation negotiation framework. Covers tech, finance, PE/VC, healthcare, and B2B. |

---

### Design philosophy

These skills follow two layers of standards:

**Standards-backed rules** grounded in published engineering guidance (PEP 8, Twelve-Factor App, OWASP, dbt best practices, Microsoft Power BI documentation). See [docs/rationale-and-references.md](docs/rationale-and-references.md).

**House operating conventions** that are intentional working preferences for AI-assisted engineering: lead with the answer, sparse comments, no AI-style clutter, fixed output structures. These are not claimed as universal standards. See [docs/adr/0001-ai-session-operating-standard.md](docs/adr/0001-ai-session-operating-standard.md).

---

### Documentation

| Document | Purpose |
|---|---|
| [docs/rationale-and-references.md](docs/rationale-and-references.md) | Standards-backed justification for skill rules with source citations |
| [docs/adr/0001-ai-session-operating-standard.md](docs/adr/0001-ai-session-operating-standard.md) | Architecture Decision Record explaining why these standards exist |

---

### Contributing

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

### License

MIT License. See [LICENSE](LICENSE) for details.

---

<p align="center">
  <a href="https://www.linkedin.com/in/nicholashidalgo"><img src="https://img.shields.io/badge/LinkedIn-Nicholas_Hidalgo-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>&nbsp;
  <a href="https://nicholashidalgo.com"><img src="https://img.shields.io/badge/Website-nicholashidalgo.com-teal?style=for-the-badge" alt="Website"></a>&nbsp;
  <a href="mailto:analytics@nicholashidalgo.com"><img src="https://img.shields.io/badge/Email-analytics@nicholashidalgo.com-red?style=for-the-badge" alt="Email"></a>
</p>
