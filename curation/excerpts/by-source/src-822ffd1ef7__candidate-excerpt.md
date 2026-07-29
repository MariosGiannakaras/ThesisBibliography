## SRC-822FFD1EF7 — BELIEF-ENRICHED PESSIMISTIC Q-LEARNING AGAINST ADVERSARIAL STATE PERTURBATIONS - ICLR Proceedings

- **Priority:** P1-core
- **Topics:** observation-uncertainty, partial-observability, tabular-rl, deep-rl
- **Source:** https://proceedings.iclr.cc/paper_files/paper/2024/file/64d67497ccd0afc0131e2fec8b18e2ab-Paper-Conference.pdf
- **Markdown:** `sources/markdown/SRC-822FFD1EF7__belief-enriched-pessimistic-q-learning-against-adversarial-state-perturb.md`
- **Review status:** machine-selected; full-text verification pending

> Algorithm 5: Belief-Enriched Pessimistic DQN (BP-DQN) Testing Data: Trained robust Q network Qr, PFRNN belief model Np 1 Initialize observation history Shis and action history Ahis; 2 for t = 0,1,...,T do 3 Observe the perturbed state s̃t; 4 if t = 0 then 5 M0 = Bϵ(s̃t); 6 end 7 Select an action based on belief Mt and Qr: at = argmaxa∈Aminm∈MtQr(m, a); 8 Append s̃t and at to Shis and Ahis and use belief model Np(Shis, Ahis) to generate Mt+1; 9 Execute action at in the environment; 10 end Algorithm 6: Diffusion-Assisted Pessimistic DQN (DP-DQN) Training. We highlight the difference between our algorithm and the vanilla DQN algorithm in brown. Data: Number of iterations T , trained vanilla Q network Qv , diffusion belief model Nd, target network update frequency Z, batch size D, belief size κd, exploration parameter ϵ′, noise level ϵϕ Result: Robust Q network Qr 1 Initialize replay buffer…
