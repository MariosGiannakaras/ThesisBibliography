---
κωδικός: SRC-95C9DAEE68
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Evidence — Deep Reinforcement Learning in Non-stationary Environments

## Evidence E1 — Change detection and post-change adaptation are separate problems
- **Type:** faithful paraphrase
- **Location:** Chapter 1, Section 1.2, research questions and objectives; dissertation abstract
- **Claim:** The dissertation treats unknown change-point detection and subsequent policy adaptation as linked but distinct parts of non-stationary reinforcement learning.
- **Thesis use:** mechanism taxonomy; metrics
- **Topics:** change detection; adaptation; non-stationarity
- **Status:** verified

### Faithful paraphrase
In a non-stationary environment, an agent can first need to recognize that the environment has changed and then decide how to update its policy for the new condition. The dissertation develops methods in which information from change detection is used to guide adaptation, rather than treating continued training alone as sufficient evidence that a change was identified.

### Limitation
This decomposition does not imply that every adaptive agent must contain a separate explicit detector. A continually adapting baseline without a discrete detection event remains a valid comparator.

## Evidence E2 — Adaptation strength can depend on estimated change magnitude
- **Type:** faithful paraphrase
- **Location:** Chapter 1, Section 1.2; methodology chapters on detection-informed adaptation
- **Claim:** The proposed methods use information about the extent of environmental change to balance preservation of prior knowledge against stronger policy modification.
- **Thesis use:** severity protocol; stability-plasticity analysis
- **Topics:** change magnitude; knowledge preservation; plasticity
- **Status:** verified

### Faithful paraphrase
The dissertation motivates stronger adaptation and exploration when the detected change is large, while smaller changes can justify retaining more of the previous policy or learned knowledge. This frames adaptation as a stability-plasticity trade-off rather than a binary choice between keeping and discarding the old solution.

### Limitation
Change magnitude must be defined independently of the eventual algorithm outcome. In the thesis benchmark it should be determined by predeclared environment parameters or a precomputed distance, not post hoc from recovery performance.

## Evidence E3 — Controlled experiments can perturb dynamics, geometry, and observations separately
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.1; Tables 3.1–3.2; Figure 3.4
- **Claim:** The experiments introduce controlled changes to physical parameters, environmental obstacles, and observation conditions while withholding the changed parameter from the agent.
- **Thesis use:** shift-family design
- **Topics:** dynamics shift; structural shift; observation shift
- **Status:** verified

### Faithful paraphrase
The evaluated non-stationary settings include changes to CartPole dynamics such as gravity, pole mass, and force magnitude; wind changes in LunarLander; obstacle changes in MiniGrid; and visual changes such as lighting and texture in ViZDoom. The agent is not directly given the hidden environment variable that changed.

### Limitation
Most changes are abrupt and preconfigured. This gives a clear ground-truth changepoint but does not by itself cover gradual drift or simultaneous interacting perturbations.

## Evidence E4 — Detector quality and post-change control quality require different metrics
- **Type:** faithful paraphrase
- **Location:** Chapter 3, Section 3.4.2 and corresponding results tables/figures
- **Claim:** The dissertation evaluates change detection with detection-oriented metrics and evaluates adaptation through performance trajectories after the change.
- **Thesis use:** metric separation
- **Topics:** F1; detection delay; performance dip; recovery
- **Status:** verified

### Faithful paraphrase
The experiments compare detected and true change points using detector metrics such as F1 and delay, while also examining policy performance around and after the change. A detector can therefore be accurate yet still lead to slow or poor adaptation, and an adapting policy can recover despite an imperfect detector.

### Thesis-safe implication
Report false alarms/missed changes and detection delay separately from maximum performance degradation, recovery time, and final post-change return.

## Evidence E5 — Unknown changepoints are a different assumption from oracle boundaries
- **Type:** faithful paraphrase
- **Location:** Abstract; Chapters 1, 3–6
- **Claim:** The dissertation explicitly studies non-stationary environments in which change points are not supplied to the learning algorithm.
- **Thesis use:** oracle/non-oracle labeling
- **Topics:** unknown change point; detector; prior information
- **Status:** verified

### Faithful paraphrase
The proposed frameworks are motivated by settings where the agent cannot rely on an external task-boundary signal. In an experimental comparison, a method that is told the true changepoint should therefore be labeled as an oracle-boundary condition and not compared as if it solved the same detection problem.

## Evidence E6 — The contribution spans deep model-free and model-based methods, not a required tabular implementation
- **Type:** faithful paraphrase
- **Location:** Abstract; Chapters 3–6
- **Claim:** The dissertation develops several deep-RL change-detection and adaptation methods, including model-free and latent/model-based approaches.
- **Thesis use:** feasibility/background boundary
- **Topics:** deep RL; model-free; model-based; latent dynamics
- **Status:** verified

### Faithful paraphrase
The dissertation demonstrates that detection-informed adaptation can be implemented through multiple deep-RL mechanisms, including behavior, gradient, uncertainty, and latent-dynamics signals. These approaches establish a broad design space but are substantially more complex than the resource-aware tabular baseline family of the thesis.

## Avoid overclaiming
This source supports the detection/adaptation decomposition and controlled-shift evaluation. It does not establish that every resilient agent requires an explicit detector or that the dissertation's deep architectures are necessary for the thesis GridWorld implementation.
