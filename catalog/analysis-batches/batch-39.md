# Παρτίδα 39 — agentic/vendor/community cleanup

Ημερομηνία: 2026-08-01

## Στόχος
Να αφαιρεθεί ακόμη ένα στρώμα records που χρησιμοποιούν όρους `agent`, `memory`, `learning`, `self-correction` ή `resilience` αλλά ανήκουν σε LLM/agentic, vendor, community, financial ή multi-agent robotics settings και όχι στο single-agent non-stationary RL experimental object.

## Reconciliation
Το `SRC-EC7D639B07` βρέθηκε ήδη canonical exclusion και δεν προσμετρήθηκε ξανά.

## Νέες exclusions — 17
1. `SRC-50F04B5AB0` — Google Cloud Vertex AI Agent Builder documentation.
2. `SRC-498A6D6324` — alternate/duplicate Vertex Agent Builder record.
3. `SRC-D4CDE277CE` — AWS introductory AI-agent explainer.
4. `SRC-68201B05FF` — IBM ReAct-agent explainer.
5. `SRC-2249D6DD6A` — IBM agentic-architecture explainer.
6. `SRC-27A285E652` — IBM AI-agent-learning explainer.
7. `SRC-E7E55DC611` — IBM AI-agent-memory explainer.
8. `SRC-7F7722EB5B` — LLM self-correction survey/secondary material.
9. `SRC-4A7380BA5C` — practitioner single-vs-multi-agent architecture guide.
10. `SRC-4EB5EB13CD` — Reddit LLM-agent failure discussion.
11. `SRC-DDD4D05B4E` — duplicate of the same Reddit thread.
12. `SRC-AC4429B655` — community discussion on one super-agent vs specialized agents.
13. `SRC-F494F45A40` — GenAI/GAN/VAE financial-market “resilience” application; not RL policy resilience.
14. `SRC-1A364A4551` — unusable OpenReview verification wrapper; underlying paper not reliably identifiable from available source.
15. `SRC-1C334CCF9D` — OpenReview wrapper for Robust Gymnasium; underlying ICLR 2025 paper already canonical elsewhere.
16. `SRC-4A5F7C9FC5` — Bellman-equation course material.
17. `SRC-CD78DD328C` — high-quality but out-of-scope multi-agent fuzzy-RL robotics PhD.

## Επιστημονικές αποφάσεις που κλειδώνουν
- **LLM memory ≠ RL context recall.** Context recall στη διπλωματική απαιτεί regime/context identification και measured reuse of policy/value knowledge.
- **LLM self-correction ≠ RL recovery.** Output revision after reasoning failure δεν είναι post-change policy adaptation.
- **Vendor architecture terminology δεν αποτελεί scientific evidence** για algorithmic resilience.
- **Community failure reports** μπορούν να χρησιμοποιούνται για discovery, όχι ως quantitative evidence.
- **Financial/system/infrastructure resilience** παραμένει διαφορετικό επίπεδο από learner-policy resilience.
- **Unusable source wrappers** δεν παράγουν claims· αν η underlying paper ταυτοποιηθεί αργότερα, αξιολογείται ως ξεχωριστή scientific identity.
- **Multi-agent component-failure robustness** δεν μεταφέρεται αυτόματα σε single-agent exogenous MDP changes.

## Totals μετά την παρτίδα
Starting point Παρτίδα 38: 349 αποφασισμένες = 97 selected + 252 exclusions.

- Νέες αποφάσεις: 17
- Νέες selected: 0
- Νέες exclusions: 17
- Canonical σύνολο: **366 αποφασισμένες = 97 selected + 269 exclusions**
- Υπόλοιπη ουρά: **120 / 486 ενεργές πηγές**

## Infrastructure note
Τα totals συνεχίζουν να βασίζονται αποκλειστικά στα canonical analyses/batch records. Generated status και curated export δεν θεωρούνται συγχρονισμένα.