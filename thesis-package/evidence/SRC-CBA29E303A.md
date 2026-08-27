---
κωδικός: SRC-CBA29E303A
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-28"
---

# Evidence — Revisiting Fundamentals of Experience Replay

## Evidence E1 — Replay capacity is a consequential algorithm property
- **Type:** faithful paraphrase
- **Location:** official PMLR abstract
- **Claim:** Increasing replay capacity substantially improves some studied algorithms while leaving others relatively unaffected.
- **Thesis use:** DQN configuration identity
- **Status:** verified

### Thesis-safe implication
DQN replay capacity must be explicitly resolved and reported; it cannot be treated as an irrelevant hidden default.

## Evidence E2 — Replay ratio links optimizer work to environment experience
- **Type:** faithful paraphrase
- **Location:** official PMLR abstract
- **Claim:** The ratio of learning updates to collected experience is experimentally important across studied deep-RL algorithms.
- **Thesis use:** interaction/update accounting
- **Status:** verified

### Thesis-safe implication
The v2 runner records actual environment interactions separately from gradient/update counts and freezes DQN update cadence/replay ratio as part of its method configuration.

## Evidence E3 — Replay management is part of learning dynamics
- **Type:** methodological implication from E1–E2
- **Location:** study focus on replay capacity and replay ratio
- **Claim:** Replay configuration changes the off-policy learning process and therefore must be controlled in comparisons.
- **Thesis use:** scientific checkpoint and post-change intervention boundary
- **Status:** verified within study scope

### Thesis-safe implication
Clearing or reweighting DQN replay at a change boundary is a separate scientific intervention, not a transparent restore detail.

## Avoid overclaiming
This source does not specify the final thesis buffer size, replay ratio or post-change strategy, and it does not establish resilience superiority of replay-based methods.
