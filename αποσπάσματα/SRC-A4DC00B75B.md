---
κωδικός: SRC-A4DC00B75B
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
source-language: en
---

# Evidence — Minigrid & Miniworld: Modular & Customizable Reinforcement Learning Environments for Goal-Oriented Tasks

## E1 — MiniGrid provides a small, programmatically configurable 2D GridWorld substrate
- **Type:** faithful paraphrase
- **Location:** Abstract; Sections 1–2.2
- **Claim:** MiniGrid is designed as a minimal, customizable 2D environment library whose tile layouts, objects, missions, observations, actions, and rewards can be configured for research-specific tasks.
- **Status:** verified

### Faithful paraphrase
Chevalier-Boisvert et al. describe MiniGrid as a suite of two-dimensional tile-based goal-oriented environments built for rapid creation of new research tasks. Individual tiles can contain objects such as walls, keys, and goals; the agent uses a discrete action space; observations are partially observable by default; and the standard reward is sparse but can be replaced by a custom reward function.

### Thesis use
Use MiniGrid as the implementation substrate for versioned controlled perturbation scenarios rather than as evidence that GridWorld results automatically generalize to real systems.

### Citation
Chevalier-Boisvert et al. (2023), Abstract and Sections 1–2.2.

## E2 — The environment API supports explicit structural and observation changes
- **Type:** faithful paraphrase
- **Location:** Sections 2.2–2.4
- **Claim:** Environment generation and wrappers can modify layouts, object placement, stochastic actions, observation spaces, and reward behavior without embedding those changes inside the learning agent.
- **Status:** verified

### Faithful paraphrase
The library exposes environment-generation functions for constructing grid layouts and placing agents or objects, and its wrapper/API layer can alter environment behavior such as action stochasticity and observation representation. These mechanisms make experimental variation part of the environment configuration rather than an undocumented agent-side transformation.

### Thesis use
Serialize and version every layout, wrapper, transition-noise setting, observation mode, and reward configuration used in an experiment.

### Citation
Chevalier-Boisvert et al. (2023), Sections 2.2–2.4.

## E3 — Reset seeds support reproducible environment initialization
- **Type:** faithful paraphrase
- **Location:** Section 2.1, Listing 1
- **Claim:** The Gymnasium-compatible API accepts a reset seed, enabling reproducible environment initialization under a fixed configuration.
- **Status:** verified

### Faithful paraphrase
The paper's example interaction code initializes a MiniGrid environment through Gymnasium and calls `reset(seed=42)`, illustrating that environment randomness can be controlled through the standard seeded reset interface.

### Context and limits
A seeded environment reset does not automatically control every independent source of randomness in the learning stack.

### Thesis use
Store environment/layout seeds separately from agent initialization, exploration, minibatch, and training seeds.

### Citation
Chevalier-Boisvert et al. (2023), Section 2.1, Listing 1.

## E4 — Easy environment generation does not remove the need for solvability checks
- **Type:** protocol inference grounded in the environment API
- **Location:** Sections 2.2–2.4
- **Claim:** The API makes custom layouts easy to construct, but the paper does not guarantee that every user-generated layout or perturbation remains solvable.
- **Status:** verified

### Thesis use
Run an independent reachability/solvability check after every structural perturbation and keep the action–observation contract identical across agents being compared.

### Citation
Chevalier-Boisvert et al. (2023), environment construction sections.

## E5 — Transfer effectiveness depends on which components are reused
- **Type:** faithful paraphrase
- **Location:** Section 3.1; Table 1
- **Claim:** In the MiniGrid-to-MiniWorld case study, transferring different policy components produced different outcomes, and transferring actor weights could be detrimental in the reported setup.
- **Status:** verified

### Faithful paraphrase
The transfer case study evaluates combinations of mission-embedding, actor, and critic weights. The reported results show that component choice matters: some critic/mission transfers improve learning, while configurations that also transfer the actor can reduce performance relative to learning without that transferred component.

### Context and limits
This is one PPO transfer case study between two observation spaces and is not a universal result about actor transfer.

### Thesis use
For policy/context reuse, use component-level reuse/reset ablations and an explicit no-transfer comparator to detect negative transfer.

### Citation
Chevalier-Boisvert et al. (2023), Section 3.1 and Table 1.