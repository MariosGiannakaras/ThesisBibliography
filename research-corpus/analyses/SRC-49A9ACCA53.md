---
source_id: SRC-49A9ACCA53
status: reviewed
source_checked: transcript
review_date: "2026-08-02"
---

# Safe reinforcement learning in non-stationary environments — seminar transcript

## Material type

The source record is an automatic transcript of a technical seminar on safe reinforcement learning under non-stationarity. The talk discusses non-stationary constrained MDPs, restart/sliding-window/discounting mechanisms, risk-sensitive RL, adaptive non-stationarity detection, and meta-safe RL.

## Thesis-content value

This source is **useful theory material**, not merely a discovery aid. It contains relevant conceptual explanations and design distinctions that can directly improve the theoretical synthesis and experimental reasoning of the thesis, including:

- why outdated data must be forgotten in non-stationary RL;
- the role of variation budgets in selecting restart or forgetting frequency;
- the distinction between known-budget restart methods and adaptive detection when the variation budget is unknown;
- joint evaluation of reward optimality and safety-constraint violation;
- the difference between within-task non-stationarity and multi-task learning with explicit task boundaries;
- the role of safe policy initialization in meta-learning across related tasks;
- a time-varying GridWorld example combining changing goals/obstacles with safety constraints.

These ideas are directly relevant to the thesis even if the transcript is not used as a formal bibliographic citation.

## Citation-grade limitations

The transcript should not be treated as a precise source for theorem statements, equations, numerical claims, or exact experimental protocols because:

- it is an automatic transcript with substantial transcription errors;
- mathematical notation is often corrupted;
- stable timestamps/sections are not encoded in the stored text;
- the talk synthesizes several research projects and assumptions.

Whenever an exact theorem, regret bound, algorithmic guarantee, or empirical result is needed, the corresponding primary paper should be checked.

## Decision

**Keep for thesis theory synthesis.**

- **Thesis-content role:** supporting-theory
- **Citation grade:** unstable-transcript / informal-expert
- **Use:** conceptual synthesis, mechanism comparison, experimental design, terminology checks
- **Formal citation evidence:** optional; primary papers preferred for exact claims
- **Do not classify as rejected solely because it is a YouTube transcript.**

A separate theory-material note should preserve the useful content in the source's original language.
