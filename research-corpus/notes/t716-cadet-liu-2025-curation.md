# T-716 source curation — Cadet and Liu 2025

**Date:** 2026-09-05  
**Scope:** post-intake scientific analysis, evidence verification, overlap comparison and export decision for `SRC-327CD7B903` and `SRC-0FD9BE81AC`.

## Decision summary

Both sources are retained as **supporting citation-ready sources**. Neither replaces the existing foundational/core sources for the corresponding thesis claims.

| Source | Final role | Main added value | Does not replace |
|---|---|---|---|
| `SRC-327CD7B903` — Cadet et al. 2025 | supporting | peer-reviewed RL-specific evidence for time-resolved resilience, time-granularity trade-offs, recovery-information loss from whole-horizon aggregation, normalization/aggregation across heterogeneous settings | `SRC-0A594EACC0` for general resilience process; `SRC-0F8A6588DC` for GridWorld novelty/recovery framing; project authority for exact RQ3 recovery semantics |
| `SRC-0FD9BE81AC` — Liu et al. 2025 | supporting | recent primary model-based continual RL using an incrementally learned world model plus MPC/CEM; explicit retention/forgetting evaluation; Continual Bench; method-specific regret analysis | `SRC-39696F490F` for continual-RL taxonomy/review; `SRC-8025C139CE` for broad dynamically varying RL framing; canonical Dyna sources for Dyna/Dyna-Q+; `SRC-D38364B32C` for closer-fit local learned-model adaptation/change evidence |

## Cadet et al. — overlap and ranking

### Strong overlap

- `SRC-0A594EACC0`: resilience as a temporal process rather than a static score.
- `SRC-0F8A6588DC`: post-change behavior should preserve separate degradation/recovery dimensions.
- `SRC-4000D2B40A`: broader resilience/evaluation methodology already used by the thesis claim tree.

### Unique increment

Cadet et al. adds a 2025 peer-reviewed RL-specific primary study that explicitly discusses **time granularity** and states that a whole-game interval can lose recovery information. It also demonstrates normalization and aggregation across many attack/topology settings and uses temporal-profile clustering when a mean summary is insufficient.

### Ranking decision

For the thesis claim that resilience is a temporal process, the broader/general and GridWorld-nearer sources remain primary. Cadet is ranked as supporting evidence because its resilience formula is tied to cyber assets, adversarial impacts and operational weights. Its formulas, smoothing and numerical window choice are not transferred to the thesis.

## Liu et al. — overlap and ranking

### Strong overlap

- `SRC-39696F490F`: CRL framing, catastrophic forgetting, stability/plasticity and multidimensional evaluation.
- `SRC-8025C139CE`: broad non-stationary/dynamically varying environment taxonomy.
- canonical Dyna/Dyna-Q+ sources: learned model plus planning mechanisms.
- `SRC-D38364B32C`: modern learned-model adaptation, replay/model freshness and non-stationary transition evidence.

### Unique increment

Liu et al. adds a 2025 ICML primary implementation of an Online Agent whose persistent shared component is a sparse FTL world model and whose action selection is performed by MPC/CEM. Continual Bench tests sequential tasks under unified dynamics and reward-defined task changes, explicitly evaluating retention of earlier tasks. The paper also provides a method-specific regret bound and explicit limitations.

### Ranking decision

Khetarpal remains the core continual-RL taxonomy source because it is broader and better aligned with conceptual classification. The canonical Dyna sources remain authoritative for Dyna mechanisms. Alver et al. remains closer to the thesis question when discussing learned-model adaptation after environmental change. Liu is selected as supporting related-work evidence for a modern alternative model-based continual architecture and for clarifying that `model-based RL` is not synonymous with `Dyna-Q+`.

## Thesis claim placement after synchronization

Recommended additions to the claim/evidence tree after the bibliography package is regenerated and synchronized:

- `LIT-013` resilience as temporal process: add `SRC-327CD7B903` as **supporting**, especially for granularity/aggregation discussion.
- `PROJ-008` RQ3 recovery rationale: `SRC-327CD7B903` may be cited only for the general need to preserve temporal recovery information; exact 32-interaction/tolerance/two-window/right-censoring semantics remain project authority.
- `LIT-008` non-stationarity/continual regimes: add `SRC-0FD9BE81AC` as **supporting example** of sequential reward-defined tasks under unified dynamics, not as a description of thesis disturbances.
- `LIT-007` / model-based related work: add `SRC-0FD9BE81AC` only as a modern contrast to Dyna-style planning, not as foundational Dyna evidence.
- Discussion/Future Work: use Liu for repeated task sequences, retention/forgetting metrics and richer world-model comparators.

## Formal export status

- `SRC-327CD7B903`: analysis verified; original checked; evidence verified; role supporting; export yes.
- `SRC-0FD9BE81AC`: analysis verified; original checked; evidence verified; role supporting; export yes.

The next governed step is generated selection/package regeneration and validation. No thesis prose should cite these IDs until the regenerated citation-ready package is merged and synchronized into `resilient-ai-agents-thesis`.
