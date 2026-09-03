---
κωδικός: SRC-6F4F8BE003
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-09-03"
---

# Citation-ready evidence — Online Reinforcement Learning in Non-Stationary Context-Driven Environments

## E1 — Online non-stationarity and catastrophic forgetting
- **Τύπος:** faithful paraphrase
- **Θέση:** Abstract; Section 1, pp. 1–2
- **Ισχυρισμός:** Online RL in a changing environment can suffer catastrophic forgetting because sequential learning on new non-stationary experience can degrade behavior learned for earlier conditions.
- **Προτεινόμενη χρήση:** Background / Related Work; Discussion
- **Θέματα:** non-stationary RL; continual RL; catastrophic forgetting; stability-plasticity
- **Κατάσταση:** verified

**Faithful paraphrase:** The paper treats online RL as continual training and deployment in an environment whose characteristics change over time, and identifies catastrophic forgetting as a central difficulty: neural policies trained sequentially on new non-stationary data can lose behavior learned for earlier contexts.

**Context / limitation:** This supports a general motivation for studying adaptation and retention. It does not show that any one method in the thesis is more or less resilient under protocol-v2.1.

## E2 — The paper assumes observed exogenous context
- **Τύπος:** faithful paraphrase
- **Θέση:** Section 1, p. 1; Section 2, pp. 2–3
- **Ισχυρισμός:** Context-driven non-stationarity with an explicit context signal is a different information regime from a hidden environmental change.
- **Προτεινόμενη χρήση:** Background / Related Work; Methodology boundary; Threats to validity
- **Θέματα:** observed context; information boundary; contextual MDP; latent change
- **Κατάσταση:** verified

**Faithful paraphrase:** The formal setting supplies the current exogenous context to the policy together with the state, and lets that context alter rewards and transition dynamics. The paper explicitly distinguishes this from latent-context work that must infer an unobserved regime.

**Context / limitation:** This is the key transfer boundary for the thesis. The thesis's persistent action remap is not supplied to the learner as a context label, so the two settings must not be described as equivalent.

## E3 — Recurring-context GridWorld illustrates forgetting and relearning
- **Τύπος:** faithful paraphrase
- **Θέση:** Section 4.1, pp. 4–5, Figure 1
- **Ισχυρισμός:** When a policy is trained sequentially under changing regimes, behavior for an earlier regime may drift and require relearning when that regime returns.
- **Προτεινόμενη χρήση:** Related Work; Discussion of retention versus adaptation
- **Θέματα:** GridWorld; recurring contexts; forgetting; relearning
- **Κατάσταση:** verified

**Faithful paraphrase:** In the paper's two-mode GridWorld illustration, an A2C agent first learns the no-trap context, then trains only under a trap-active context and loses accuracy for the first context; when the first context returns, performance is initially suboptimal until the agent relearns it. The reverse forgetting pattern is also visible for the second context later in the sequence.

**Context / limitation:** The example exposes the active context to the policy and is pedagogical. It is not equivalent to the thesis testbed or evidence about the thesis's measured recovery times.

## E4 — LCPO constrains retention without training the on-policy objective on stale experience
- **Τύπος:** faithful paraphrase
- **Θέση:** Section 1, pp. 1–2; Section 4
- **Ισχυρισμός:** A continual-RL design can separate current-regime optimization from an explicit mechanism that limits destructive change to behavior associated with older regimes.
- **Προτεινόμενη χρήση:** Related Work
- **Θέματα:** LCPO; constrained policy optimization; retention; OOD context; replay buffer
- **Κατάσταση:** verified

**Faithful paraphrase:** LCPO stores past experience and identifies samples outside the current context distribution, but uses those samples to constrain policy changes on older contexts rather than to optimize the current on-policy objective directly from stale data.

**Context / limitation:** This describes LCPO's own mechanism. It must not be rephrased as a property of PPO generally or as an intervention implemented in this thesis.

## E5 — Capacity, exploration and buffer design remain limitations
- **Τύπος:** faithful paraphrase
- **Θέση:** Section 5.3 and Section 6, p. 10
- **Ισχυρισμός:** Continual adaptation mechanisms involve resource and stability-plasticity trade-offs; successful retention is not independent of representation capacity, exploration and memory design.
- **Προτεινόμενη χρήση:** Discussion; Limitations
- **Θέματα:** network capacity; exploration; buffer size; memory; continual adaptation
- **Κατάσταση:** verified

**Faithful paraphrase:** The authors report that very small retained buffers reduce performance and note that more complex or high-dimensional contexts may require more memory. They also identify finite network capacity, exploration after context changes, and buffer-management policy as unresolved or limiting factors.

**Context / limitation:** These are limitations of the LCPO setting and useful general cautions; they are not direct explanations for any specific protocol-v2.1 result unless independently supported by the thesis evidence.

## Citation note
Use the canonical bibliographic metadata from `SRC-6F4F8BE003`. Cite the ICLR 2025 paper itself, not this evidence file or the project freshness note.