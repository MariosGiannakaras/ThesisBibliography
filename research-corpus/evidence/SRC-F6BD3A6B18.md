---
κωδικός: SRC-F6BD3A6B18
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-27"
---

# Evidence — Sutton (1990), Dyna

## E1 — Dyna integrates real learning, model learning and planning

- **Type:** faithful paraphrase
- **Location:** Abstract and Section 1, pp. 471–472
- **Claim:** Dyna architectures alternate interaction with the real world and planning using a learned forward model.
- **Thesis use:** distinguish model-free continual agents from learned-model planning agents.
- **Status:** verified

### Faithful paraphrase
Dyna learns a world model online and uses model-generated experience for incremental planning while also learning directly from real interaction.

## E2 — Dyna-Q is Q-learning plus a learned-model planning mechanism

- **Type:** faithful paraphrase
- **Location:** Section 4, p. 475
- **Claim:** Dyna-Q combines Q-learning with a learned world model used to produce hypothetical experience for planning.
- **Thesis use:** mechanism definition of Dyna-Q.
- **Status:** verified

### Limitation
Do not describe Dyna-Q as receiving extra real environment samples when it performs extra planning backups.

## E3 — Planning steps are computation/model-generated updates

- **Type:** faithful paraphrase from experiment design
- **Location:** Sections 3–4, pp. 474–475
- **Claim:** The paper varies the number of hypothetical experiences generated with the model per real experience, demonstrating that planning intensity is a separate computational dimension.
- **Thesis use:** matched planning budgets for Dyna-Q versus Dyna-Q+.
- **Status:** verified

## E4 — Dyna-Q+ adds recency-driven exploration

- **Type:** faithful paraphrase
- **Location:** p. 476, immediately before Section 5
- **Claim:** The exploration-bonus variant tracks elapsed time since a state-action pair was tried in real experience and makes long-untried actions more attractive; it also permits hypothetical experience for previously untried actions.
- **Thesis use:** define the extra mechanism that distinguishes Dyna-Q+ from plain Dyna-Q.
- **Status:** verified

### Limitation
Do not reduce this mechanism to the statement “Dyna-Q+ = Dyna-Q with a positive scalar kappa”; treatment of untried actions is also part of the described exploration behavior.

## E5 — Changing-world experiment separates Dyna-Q and Dyna-Q+

- **Type:** faithful paraphrase
- **Location:** Section 5, pp. 476–477
- **Claim:** With matched k=10 planning, the shortcut experiment reports that the exploration-bonus Dyna-Q+ system discovers the newly opened shortcut while the non-bonus Dyna-Q system does not within the reported experiment.
- **Thesis use:** historical evidence that recency-driven re-exploration can matter when environmental improvement is not forced through current behavior.
- **Status:** verified

### Limitation
This is one historical maze result. It does not predict the ranking under the thesis's remap/failure/corruption conditions.

## E6 — Plain Dyna-Q is necessary for mechanism attribution

- **Type:** thesis-safe methodological inference
- **Location:** E2–E5 plus thesis design
- **Claim:** Comparing Dyna-Q and Dyna-Q+ at matched planning budgets isolates the incremental contribution of the recency/exploration mechanism more cleanly than comparing Dyna-Q+ only with model-free Q-learning.
- **Status:** verified as design inference

## Avoid overclaiming

The source does not show that:
- Dyna-Q+ is universally superior;
- more planning is always better;
- the historical k=10 setting is optimal for this thesis;
- model learning is robust to every hidden disturbance;
- Dyna-Q+'s exploration cost is free.