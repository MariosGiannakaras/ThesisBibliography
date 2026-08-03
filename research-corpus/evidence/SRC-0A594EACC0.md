---
κωδικός: SRC-0A594EACC0
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Cooperative Resilience in Artificial Intelligence Multiagent Systems

## E1 — Resilience spans resistance, recovery, and transformation across a disruptive event

- **Type:** faithful paraphrase
- **Location:** Section 2, Definition 1
- **Claim:** The paper defines resilience as a temporal capability that includes preparation, resistance, recovery, and transformation in response to a specified disruption.
- **Status:** verified

### Faithful paraphrase

Chacon-Chamorro et al. define cooperative resilience as the ability of a system involving collective action to anticipate and prepare for disruption, resist its effects, recover afterward, and transform in response to events that threaten joint welfare. The definition therefore treats resilience as a process spanning phases before, during, and after disruption, and it allows past disruptions to influence how the system handles later ones.

### Context and limits

The definition is written for cooperative multi-agent systems. A single-agent thesis can borrow the temporal structure only after replacing joint welfare with explicitly defined task and safety variables.

### Thesis use

Use resilience as a broader temporal concept than zero-shot robustness or adaptation alone. Preserve separate measurements for immediate degradation, recovery, and longer-term improvement.

### Citation

Chacon-Chamorro et al. (2024), Section 2, Definition 1.

## E2 — Reference and performance curves support event-window resilience measurement

- **Type:** faithful paraphrase
- **Location:** Sections 3.1–3.2
- **Claim:** The proposed measurement method compares time-dependent performance under disruption against a reference trajectory without the disruption.
- **Status:** verified

### Faithful paraphrase

The methodology first defines time-dependent variables of interest and records both a reference curve under normal conditions and a performance curve under disruptive conditions. Each disruptive event is then analyzed inside a time window containing the event and its subsequent failure and recovery behavior. The resilience calculation compares the performance and reference trajectories so that both the magnitude and temporal duration of degradation and recovery contribute to the result.

### Context and limits

The reference trajectory is not required to be ideal; it represents expected behavior without the disruptive event. Window placement and variable orientation must be defined consistently.

### Thesis use

Use matched-seed nominal and perturbed runs to construct normalized performance-deficit, area-loss, and recovery-time metrics while retaining the raw curves.

### Citation

Chacon-Chamorro et al. (2024), Sections 3.1–3.2.

## E3 — Repeated disruptions should be evaluated as a sequence, not only averaged independently

- **Type:** faithful paraphrase
- **Location:** Section 3, Stages III–IV
- **Claim:** The method explicitly aggregates event-level resilience over successive disruptions and rewards improvement while penalizing deterioration.
- **Status:** verified

### Faithful paraphrase

After computing resilience for individual disruptive events, the methodology combines those event-level measurements across time. The aggregation is designed to distinguish systems whose response improves after previous disruptions from systems whose resilience degrades over repeated events. A final stage also combines multiple welfare variables, so poor behavior on one important dimension can remain visible.

### Context and limits

The paper's exact nonlinear aggregation is one design choice and may be sensitive to event ordering and metric scaling.

### Thesis use

Report each occurrence separately and include a metric for change in recovery quality across repeated visits to the same or related regime, rather than relying only on a grand mean.

### Citation

Chacon-Chamorro et al. (2024), Section 3, Stages III–IV.

## E4 — Multiple variables can reveal delayed or indirect consequences of disruption

- **Type:** faithful paraphrase
- **Location:** Experimental results, Common Harvest Open case study
- **Claim:** Different performance variables can exhibit different temporal responses to the same disruption, so a single task score can miss delayed or indirect damage.
- **Status:** verified

### Faithful paraphrase

In the case study, environmental resource disruption affects indicators such as resource availability, sustainability, inequality, and collective hunger on different timescales. The resulting reference and performance curves show that one disruptive event can have an immediate effect on one indicator and delayed consequences on others.

### Context and limits

The particular welfare variables are domain-specific and come from a cooperative social-dilemma setting.

### Thesis use

Keep task return, success rate, safety violations, intervention cost, and recovery quality as separate reported quantities before any composite resilience score is constructed.

### Citation

Chacon-Chamorro et al. (2024), experimental case study and resilience analysis.

## E5 — The source is methodological support, not a direct single-agent algorithm baseline

- **Type:** scope inference grounded in the paper
- **Location:** Abstract; Sections 1–5
- **Claim:** The contribution is a definition and measurement methodology for cooperative resilience, validated in a multi-agent environment; it does not provide a directly comparable single-agent adaptation algorithm for the thesis benchmark.
- **Status:** verified

### Faithful paraphrase

The paper's central contribution is conceptual and metric-oriented. Its experiments use cooperative systems with RL- and LLM-based agents in Melting Pot 2.0, so its value for a single-agent GridWorld thesis lies primarily in the temporal decomposition and measurement principles rather than in algorithm ranking.

### Thesis use

Use the source for resilience definitions and repeated-event metric design, not as evidence that a particular multi-agent architecture should be implemented.

### Citation

Chacon-Chamorro et al. (2024), overall scope.
