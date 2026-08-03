---
κωδικός: SRC-F909CABDEB
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — A Survey of Continual Reinforcement Learning

## Evidence E1 — Continual RL balances stability, plasticity, and scalability
- **Type:** faithful paraphrase
- **Location:** Introduction; Section III-B
- **Claim:** Continual RL must preserve prior competence, acquire new behavior, and remain feasible as the task stream grows.
- **Thesis use:** evaluation dimensions
- **Topics:** stability; plasticity; scalability
- **Status:** verified

### Faithful paraphrase
The survey frames continual RL as a persistent-learning problem with three coupled demands: retaining previously acquired skills, adapting effectively to new tasks, and keeping memory and computation within reasonable bounds as more experience accumulates. Strong performance on only the most recent task is therefore insufficient evidence of a successful continual learner.

## Evidence E2 — Average performance and forgetting measure different properties
- **Type:** faithful paraphrase
- **Location:** Section III-C, metric definitions
- **Claim:** Aggregate performance over tasks and the loss of competence on earlier tasks are distinct continual-learning metrics.
- **Thesis use:** retention metrics
- **Topics:** average performance; forgetting; retention
- **Status:** verified

### Faithful paraphrase
An agent can obtain a strong average score while still losing substantial performance on an earlier task after learning later tasks. A recurring-regime experiment should therefore report retention or forgetting separately from aggregate reward.

### Limitation
Forgetting can only be measured if earlier regimes are revisited or otherwise reevaluated under a declared protocol.

## Evidence E3 — Forward transfer needs a from-scratch reference
- **Type:** faithful paraphrase
- **Location:** Section III-C, transfer metrics
- **Claim:** Forward transfer asks whether prior learning improves the learning trajectory on a new task relative to a comparable single-task or scratch baseline.
- **Thesis use:** transfer/context-recall evaluation
- **Topics:** forward transfer; negative transfer; learning curve
- **Status:** verified

### Faithful paraphrase
Prior experience is beneficial only if it improves learning on the new task relative to an appropriate reference that does not receive that transferred knowledge. If the transferred agent learns more slowly or reaches worse performance, the result is negative transfer rather than successful continual adaptation.

## Evidence E4 — Task-boundary visibility is a major experimental assumption
- **Type:** faithful paraphrase
- **Location:** Section III-E; scenario taxonomy
- **Claim:** Task-aware and task-agnostic continual-learning settings differ in whether the learner is given task identity or boundary information.
- **Thesis use:** oracle/non-oracle protocol
- **Topics:** task boundary; task identity; detector
- **Status:** verified

### Faithful paraphrase
In task-agnostic continual RL, the agent may receive neither a task label nor an explicit signal that the environment changed. This is fundamentally more demanding than a task-aware condition in which the switch is supplied externally. Both can be useful experimentally, but the supplied-boundary version should be labeled as an oracle or diagnostic condition.

## Evidence E5 — Scalability requires explicit resource reporting
- **Type:** faithful paraphrase
- **Location:** Sections III-B–III-D
- **Claim:** Continual-learning scalability is multidimensional and should be characterized through resource proxies rather than a single score.
- **Thesis use:** resource-aware evaluation
- **Topics:** memory; compute; sample efficiency; model growth
- **Status:** verified

### Faithful paraphrase
Methods can preserve performance by storing ever-growing policy sets, replay data, or auxiliary models, but that strategy may become impractical over a long task sequence. Meaningful comparisons should therefore report factors such as environment interactions, memory footprint, model size or growth, training/inference cost, and wall-clock overhead under the same hardware and implementation conditions.

## Evidence E6 — CRL encompasses more than simple source-to-target transfer
- **Type:** faithful paraphrase
- **Location:** Sections II–III-A
- **Claim:** Continual RL emphasizes sequential, persistent learning across changing tasks, including knowledge retention and transfer over time.
- **Thesis use:** terminology boundary
- **Topics:** continual RL; transfer RL; multi-task RL
- **Status:** verified

### Faithful paraphrase
Transfer RL can focus on improving a designated target task using source-task knowledge, while continual RL additionally requires a persistent learner to operate over a sequence of changing tasks and manage what to retain, reuse, or update. These paradigms should not be treated as interchangeable.

## Avoid overclaiming
The survey is a taxonomy and methodology source. It does not empirically establish that one context-memory or continual-learning method is optimal for the thesis GridWorld.
