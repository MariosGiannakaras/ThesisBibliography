# Batch 45 — final no-analysis sweep

Date: 2026-08-01

## Scope
This batch closed the final 26 records that remained without a canonical scientific decision after Batch 44. Source texts were evaluated in their original language. No original file was deleted.

## Selected sources

### SRC-CA06A28C0B — Open-World Learning for Radically Autonomous Agents
**Role:** supporting.

Key contribution to the thesis protocol:
- sudden and unannounced environmental change,
- explicit separation of monitoring, diagnosis, and repair,
- detector ≠ adapter,
- novelty-response curves,
- detection delay reported separately from adaptation/recovery rate,
- randomized novelty timing to avoid anticipation leakage.

### SRC-EA5D0E318E — Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles
**Role:** background.

Key contribution:
- calibration ≠ predictive accuracy,
- deep ensembles as an optional predictive-uncertainty signal,
- static OOD uncertainty ≠ online changepoint detection,
- compute/memory cost must be reported if a neural ensemble is used.

### SRC-701E163AC8 — Reinforcement Learning: An Introduction, second edition
**Role:** background; canonical Sutton–Barto record.

Key contribution:
- tabular/online RL foundations,
- Q-learning as the continual baseline,
- constant-step-size recency for non-stationary tracking,
- recency ≠ reset and recency ≠ changepoint detection.

Verification note: the local Markdown conversion for this record remains empty at the time of analysis. Bibliographic identity and final-edition structure were checked against MIT Press, and section-level content was checked against the authors' complete March 2018 second-edition draft. The linked original is retained for conversion reconciliation.

## Rejected sources
The following 23 records were given final exclusion decisions:

- `SRC-CCFF246CA7` — broad DNN uncertainty survey; high quality but redundant with selected UQ sources.
- `SRC-9EED60003F` — NASA ML certification/evidence report; assurance scope, redundant for the thesis experiment.
- `SRC-59A04B97F6` — later NASA Simplex/RTA work; redundant with selected canonical RTA source.
- `SRC-3A95B5303C` — NASA milestone/presentation material; stronger primary sources already selected.
- `SRC-698B096865` — infrastructure-recovery MARL thesis; different resilience target and MARL confounds.
- `SRC-E2356C5721` — offline RL uncertainty/pessimism; offline dataset uncertainty ≠ online environmental change.
- `SRC-F99517DABE` — generic intelligent-agent background without unique experimental evidence.
- `SRC-CDCA1BACF3` — computer-vision robustness thesis; supervised perception robustness ≠ RL recovery.
- `SRC-2554BB8102` — LLM-agent survey; outside the current RL-agent scope.
- `SRC-02D2683D4F` — redundant LLM-agent survey.
- `SRC-0249AC29E8` — instructional RL lecture/video material.
- `SRC-01F23B6B1F` — POMDP example-domain resource rather than scientific claim evidence.
- `SRC-D546F0AACB` — practitioner agentic-governance article.
- `SRC-3BD2FDEADB` — NumPy/GridWorld tutorial.
- `SRC-EE33F366D6` — duplicate/derivative NumPy/GridWorld tutorial.
- `SRC-55005EF367` — superseded 2014–15 pre-publication Sutton–Barto second-edition draft; final 2018 record selected separately.
- `SRC-D0A02E4877` — incomplete IEEE landing-page capture and non-core application case.
- `SRC-3EEF180BD3` — LLM reward-hacking preprint; specification failure ≠ environmental resilience.
- `SRC-D6A6F6F96E` — reward-shaping tutorial; shaping is a benchmark-design confound, not a recovery mechanism.
- `SRC-AA093F6111` — adversarial reward-preserving robust-RL preprint; adversarial attacker model outside core scope.
- `SRC-EC8E7E4711` — agentic-AI industry report, non-primary.
- `SRC-F6E2AD5FA8` — CFD uncertainty-quantification thesis; different domain/problem.
- `SRC-82B9A220FE` — introductory RL-from-scratch tutorial.

## Scientific decisions locked by this batch
1. Open-world monitoring, diagnosis, and repair are separate functions.
2. Novelty-response curves should expose transient degradation and recovery, not only final return.
3. Detection delay and post-detection adaptation rate are separate metrics.
4. Static predictive uncertainty/OOD performance is not sufficient evidence of sequential change detection.
5. Constant-step-size recency is a continual adaptation baseline, not a detector or reset.
6. The canonical foundational textbook record is the final 2018 Sutton–Barto second edition; earlier draft records are preserved but not double-counted.

## Language/provenance note
New citation-ready evidence created in this batch preserves the language of the underlying source. No scientific source or evidence text is translated merely for repository convenience.
