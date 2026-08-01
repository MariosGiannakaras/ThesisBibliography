# Robust Reinforcement Learning

- **Source ID:** `SRC-71F2ECA651`
- **Authors:** Jun Morimoto; Kenji Doya
- **Venue:** Advances in Neural Information Processing Systems 13 (NIPS 2000)
- **Publication year:** 2000
- **Source language:** English
- **Canonical record:** official NeurIPS proceedings paper
- **Official abstract page:** https://proceedings.neurips.cc/paper_files/paper/2000/hash/e8dfff4676a47048d6f0c4ef899593dd-Abstract.html
- **Official PDF:** https://proceedings.neurips.cc/paper_files/paper/2000/file/e8dfff4676a47048d6f0c4ef899593dd-Paper.pdf
- **Primary-source verification:** completed against the 7-page official proceedings PDF on 2026-08-01

## Provenance repair

The previous Markdown conversion for this source resolved to an archival laboratory webpage rather than to the paper itself. That scrape was not a valid canonical paper conversion and must not be used as scientific evidence.

This record replaces the invalid webpage scrape with a canonical provenance/index record tied to the official NeurIPS primary source. The original paper remains the authoritative source for verification; the repository does not reproduce the full copyrighted proceedings text here.

## Paper structure used for verification

1. **Introduction** — motivation from model mismatch and input disturbance.
2. **H-infinity Control** — worst-disturbance / best-control differential-game formulation.
3. **Robust Reinforcement Learning** — minimax value formulation and actor–disturber–critic learning architecture.
4. **Simulation** — linear inverted-pendulum validation and nonlinear swing-up robustness experiments.
5. **Conclusions** — scope and results.

## Verified scientific anchors

- The paper explicitly treats model mismatch as a source of disturbance and motivates robust control against it.
- Robust RL is formulated as a minimax interaction between a control policy and a worst-case disturbance process.
- In the linear inverted-pendulum experiment, the learned robust value/policies converge toward the corresponding analytical robust-control solution.
- In the nonlinear swing-up experiment, the robust controller tolerates tested changes in pendulum weight and friction better than the standard RL comparator.
- The paper studies pre-emptive worst-case robustness to model/disturbance mismatch; it does **not** define unknown changepoint detection, context recall, or post-shift recovery metrics.

## Conversion status

- **Canonical primary source identified:** yes
- **Wrong archival scrape retired:** yes
- **Full-text evidence verified against original:** yes
- **Further OCR/full-text conversion required for citation use:** no; citation-ready evidence is maintained separately in `αποσπάσματα/SRC-71F2ECA651.md`.
