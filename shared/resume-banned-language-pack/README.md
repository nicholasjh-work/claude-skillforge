# resume-banned-language-pack

**Version:** 1.0.0 | [banned.json](./banned.json)

A hard-reject phrase list for resumes, cover letters, and LinkedIn. Every banned phrase includes a replacement template that forces concrete metrics or outcomes.

---

## Function Spec

```python
from resume_banned import flag_banned_phrases

flags = flag_banned_phrases(text)
# Returns: list[dict]
```

### Return Fields

| Field | Type | Description |
|---|---|---|
| `phrase` | str | Matched text from input |
| `start` | int | Char offset (inclusive) |
| `end` | int | Char offset (exclusive) |
| `suggestion` | str | Replacement template with `{N}`, `{%}`, `{VERB}`, `{OUTCOME}` placeholders |
| `requires_metric` | bool | True = replacement must include a number or measurable result |
| `severity` | `"error"` \| `"warning"` | error = always remove |

---

## 20 Before/After Replacements

| # | Rule | Before | After |
|---|---|---|---|
| 1 | RBL-001 | Results-driven project manager with a proven track record. | Shipped 6 features in Q2 2024, cutting customer support tickets by 40%. |
| 2 | RBL-002 | Strong team player with excellent collaboration skills. | Collaborated with 5-person cross-functional team to deliver API redesign 2 weeks early. |
| 3 | RBL-003 | Passionate about building scalable systems. | Built a Kafka-based event pipeline that processes 2M events/day, replacing a polling approach that failed at 100K. |
| 4 | RBL-004 | Detail-oriented engineer with strong communication skills. | Caught 12 production-level bugs in code review during a 3-month period; wrote the team's incident postmortem template. |
| 5 | RBL-005 | Proven track record of delivering results. | Delivered 8 production features in 6 months with a 0% rollback rate. |
| 6 | RBL-006 | Go-getter who takes initiative. | Identified a 3-second page-load regression, root-caused it without being assigned, and shipped the fix in 24 hours. |
| 7 | RBL-007 | Self-starter comfortable in ambiguous environments. | Scoped and shipped a new alerting system in 3 weeks with no spec, reducing on-call pages by 60%. |
| 8 | RBL-008 | Leveraged cloud technologies to drive efficiency. | Used AWS Lambda and SQS to replace a cron-based workflow, cutting infrastructure cost by $12K/year. |
| 9 | RBL-009 | Spearheaded company-wide digital transformation initiative. | Led 4-team migration from on-prem to AWS over 8 months; zero production downtime during cutover. |
| 10 | RBL-010 | Streamlined internal processes to improve productivity. | Automated weekly reporting, saving 3 hours/week per analyst across 8 analysts (24 hours/week total). |
| 11 | RBL-011 | Thought leader in the machine learning space. | Published 4 ML engineering posts averaging 8K monthly readers; invited to speak at MLOps World 2024. |
| 12 | RBL-012 | Added value to the organization through innovative solutions. | Redesigned the recommendation model, increasing click-through rate from 2.1% to 3.8%. |
| 13 | RBL-013 | Responsible for backend development. | Built and owned the GraphQL API layer serving 1.2M daily active users. |
| 14 | RBL-014 | Assisted with product roadmap planning. | Wrote the Q3 roadmap doc (adopted by PM); 4 of 5 proposals shipped in the quarter. |
| 15 | RBL-015 | Helped the team achieve their objectives. | Wrote the test framework that gave the team confidence to ship with a 2-day cycle instead of 2-week QA sprints. |
| 16 | RBL-016 | Dynamic and innovative communicator. | Created the engineering all-hands slide deck used by the VP for 6 quarters. |
| 17 | RBL-017 | Synergized cross-functional teams. | Resolved a 6-month product-engineering standoff by facilitating 3 structured working sessions; agreement shipped in Q4. |
| 18 | RBL-018 | Responsible for ensuring data quality. | Wrote the data validation pipeline that caught 1,400 bad records/month before they hit production. |
| 19 | RBL-019 | Value-added contributor to multiple high-impact projects. | Contributed critical path code to 3 projects generating $2M combined ARR in 2023. |
| 20 | RBL-020 | Extensive experience with cloud infrastructure. | 6 years of AWS experience; AWS Solutions Architect Professional cert; managed infra for platforms serving up to 50M monthly users. |

---

## Unit Tests

```python
# tests/test_resume_banned.py
"""
20 pytest cases: one per banned phrase. Verifies detection, span accuracy,
and that requires_metric is enforced.
"""
import pytest
from resume_banned import flag_banned_phrases


def find_flag(flags, rule_id):
    return next((f for f in flags if f["rule_id"] == rule_id), None)


class TestResumeBannedPhrases:

    def test_rbl001_results_driven_detected(self):
        text = "Results-driven project manager with experience."
        flags = flag_banned_phrases(text)
        f = find_flag(flags, "RBL-001")
        assert f is not None
        assert f["phrase"].lower() == "results-driven"
        assert f["requires_metric"] is True

    def test_rbl001_span_is_accurate(self):
        text = "I am a results-driven professional."
        flags = flag_banned_phrases(text)
        f = find_flag(flags, "RBL-001")
        assert f is not None
        assert text[f["start"]:f["end"]].lower() == "results-driven"

    def test_rbl002_team_player_detected(self):
        flags = flag_banned_phrases("Strong team player with collaboration skills.")
        assert find_flag(flags, "RBL-002") is not None

    def test_rbl003_passionate_about_detected(self):
        flags = flag_banned_phrases("Passionate about building AI products.")
        assert find_flag(flags, "RBL-003") is not None

    def test_rbl004_detail_oriented_detected(self):
        flags = flag_banned_phrases("Detail-oriented senior engineer.")
        f = find_flag(flags, "RBL-004")
        assert f is not None
        assert f["requires_metric"] is True

    def test_rbl005_proven_track_record_detected(self):
        flags = flag_banned_phrases("Proven track record of delivering results.")
        assert find_flag(flags, "RBL-005") is not None

    def test_rbl006_go_getter_detected(self):
        flags = flag_banned_phrases("Self-motivated go-getter who takes initiative.")
        assert find_flag(flags, "RBL-006") is not None

    def test_rbl007_self_starter_detected(self):
        flags = flag_banned_phrases("Self-starter comfortable in ambiguous environments.")
        assert find_flag(flags, "RBL-007") is not None

    def test_rbl008_leveraged_detected(self):
        flags = flag_banned_phrases("Leveraged cloud technologies to drive efficiency.")
        assert find_flag(flags, "RBL-008") is not None

    def test_rbl009_spearheaded_detected(self):
        flags = flag_banned_phrases("Spearheaded a company-wide digital transformation.")
        f = find_flag(flags, "RBL-009")
        assert f is not None
        assert f["requires_metric"] is True

    def test_rbl010_streamlined_requires_metric(self):
        flags = flag_banned_phrases("Streamlined internal processes.")
        f = find_flag(flags, "RBL-010")
        assert f is not None
        assert f["requires_metric"] is True

    def test_rbl011_thought_leader_detected(self):
        flags = flag_banned_phrases("Recognized thought leader in ML space.")
        assert find_flag(flags, "RBL-011") is not None

    def test_rbl012_value_add_detected(self):
        flags = flag_banned_phrases("Provided significant value-add to the org.")
        assert find_flag(flags, "RBL-012") is not None

    def test_rbl013_responsible_for_detected(self):
        flags = flag_banned_phrases("Responsible for backend development.")
        f = find_flag(flags, "RBL-013")
        assert f is not None
        assert "action verb" in f["suggestion"].lower() or "owned" in f["suggestion"].lower()

    def test_rbl014_assisted_with_detected(self):
        flags = flag_banned_phrases("Assisted with product roadmap planning.")
        assert find_flag(flags, "RBL-014") is not None

    def test_rbl015_helped_to_detected(self):
        flags = flag_banned_phrases("Helped to improve the CI/CD pipeline.")
        assert find_flag(flags, "RBL-015") is not None

    def test_rbl016_dynamic_detected(self):
        flags = flag_banned_phrases("Dynamic communicator and strategic thinker.")
        assert find_flag(flags, "RBL-016") is not None

    def test_rbl017_synergized_detected(self):
        flags = flag_banned_phrases("Synergized cross-functional teams to drive outcomes.")
        assert find_flag(flags, "RBL-017") is not None

    def test_rbl018_innovative_detected(self):
        flags = flag_banned_phrases("Innovative engineer with creative problem-solving skills.")
        assert find_flag(flags, "RBL-018") is not None

    def test_rbl020_extensive_experience_requires_metric(self):
        flags = flag_banned_phrases("Extensive experience with cloud infrastructure.")
        f = find_flag(flags, "RBL-020")
        assert f is not None
        assert f["requires_metric"] is True
        assert "{n}" in f["suggestion"].lower() or "number" in f["suggestion"].lower()

    def test_clean_text_returns_no_flags(self):
        text = (
            "Built and owned the GraphQL API layer serving 1.2M daily active users. "
            "Cut infrastructure cost by $12K/year by replacing cron jobs with AWS Lambda."
        )
        flags = flag_banned_phrases(text)
        assert flags == [], f"Unexpected flags on clean text: {flags}"
```
