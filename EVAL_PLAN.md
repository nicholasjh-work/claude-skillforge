# Human Evaluation Plan — writing-skills

**Version:** 1.0.0
**Date:** 2026-03-18

---

## 1. Purpose

This plan defines how to measure human-perceived quality of outputs from each writing skill. Automated tests (pytest, CI) verify structural correctness and absence of AI-pattern flags. This plan measures what they can't: does the output actually sound human? Is it factually faithful? Is it usable as-is?

---

## 2. Raters

- **Count:** 3 independent raters per skill
- **Profile:** Domain-appropriate. For resume/cover-letter skills: hiring managers or career coaches. For technical skills: senior engineers. For executive skills: PMs or directors.
- **Blind:** Raters do not know whether the text is original, AI-generated, or skill-output.
- **Calibration:** All raters score 5 calibration examples before the real set. Inter-rater agreement (Fleiss' kappa) must be ≥ 0.6 before evaluation proceeds.

---

## 3. Sample Size

- **50 examples per skill** = 50 before/after pairs
- **14 skills** = 700 total evaluations per rater
- **3 raters** = 2,100 total scored examples
- **Sampling:** 20 short, 20 medium, 10 long inputs per skill, randomly drawn from fixture corpus

---

## 4. Evaluation Rubric

Each rater scores the **output** (after rewrite) on 4 axes. Each axis is 1–5.

### Axis 1 — Human-likeness

> "Does this sound like a real, specific person wrote it — or does it still read like a template?"

| Score | Description |
|---|---|
| 5 | Unambiguously human: specific, has voice, no AI tells detectable |
| 4 | Sounds human; minor genericness remains |
| 3 | Borderline; could be human or weak AI output |
| 2 | Clearly AI-flavored but not egregious |
| 1 | Obviously AI-generated |

### Axis 2 — Factual Faithfulness

> "Are all key facts from the input present and accurate in the output?"

| Score | Description |
|---|---|
| 5 | All facts preserved exactly |
| 4 | All facts present; minor paraphrasing that doesn't change meaning |
| 3 | 1 fact paraphrased in a way that could be misleading |
| 2 | 1 fact omitted or distorted |
| 1 | Multiple facts wrong, omitted, or fabricated |

### Axis 3 — Edit Effort Required

> "How much would you need to edit this before publishing it to a real audience?"

| Score | Description |
|---|---|
| 5 | Publish as-is |
| 4 | Minor polish only (1–2 word changes) |
| 3 | One paragraph needs rewriting |
| 2 | Significant rewrite needed |
| 1 | Start over |

### Axis 4 — Tone Match

> "Does the tone match the stated target context and audience?"

| Score | Description |
|---|---|
| 5 | Perfect match — would not be out of place in the target context |
| 4 | Close match; slightly over- or under-formal |
| 3 | Noticeable mismatch but not disqualifying |
| 2 | Wrong tone for the context |
| 1 | Completely wrong register |

---

## 5. Pass Thresholds

A skill **passes** human evaluation if:

| Condition | Threshold |
|---|---|
| Mean Human-likeness | ≥ 3.8 / 5.0 |
| Mean Factual Faithfulness | ≥ 4.5 / 5.0 |
| Mean Edit Effort | ≥ 3.5 / 5.0 |
| Mean Tone Match | ≥ 3.8 / 5.0 |
| Examples scoring 1 on Factual Faithfulness | ≤ 2% of sample |
| Examples scoring 1 on Human-likeness | ≤ 5% of sample |

**A skill that fails Factual Faithfulness threshold must be suspended from production use** until root cause is identified and mitigated.

---

## 6. Evaluation Workflow

```
1. Generate 50 outputs per skill using the production pipeline (temperature=0.0, canonical seed)
2. Pair each output with its input (raters see both)
3. Distribute to raters via evaluation form (Google Forms / Airtable)
4. Raters score each pair independently — no discussion until scoring complete
5. Calculate inter-rater agreement (Fleiss' kappa) per skill
6. Average scores across raters for each example
7. Compute skill-level mean per axis
8. Flag any example scoring 1 on Factual Faithfulness for manual review
9. Publish results to EVAL_RESULTS.md
```

---

## 7. Metrics Output Format

```json
{
  "skill": "email-writer",
  "eval_date": "2026-03-18",
  "sample_size": 50,
  "rater_count": 3,
  "fleiss_kappa": 0.71,
  "results": {
    "human_likeness": {"mean": 4.1, "p10": 3.0, "p90": 5.0, "pass": true},
    "factual_faithfulness": {"mean": 4.8, "p10": 4.0, "p90": 5.0, "pass": true},
    "edit_effort": {"mean": 3.9, "p10": 3.0, "p90": 5.0, "pass": true},
    "tone_match": {"mean": 4.2, "p10": 3.0, "p90": 5.0, "pass": true}
  },
  "critical_failures": {
    "factual_faithfulness_1_count": 0,
    "human_likeness_1_count": 1
  },
  "overall_pass": true
}
```

---

## 8. Cadence

- **Initial evaluation:** Before any skill goes to production
- **Re-evaluation:** After any prompt change that touches Pass 1, Pass 2 Audit, or Pass 2 Final
- **Spot checks:** Monthly, 10 random examples per active skill
