# Παρτίδα 29 — agentic/MARL/tutorial scope cleanup

Ημερομηνία: 2026-08-01

## Στόχος
Μαζικός καθαρισμός πηγών που χρησιμοποιούν όρους όπως agent, memory, resilience ή non-stationarity αλλά ανήκουν σε διαφορετικό experimental object από τη διπλωματική: LLM/agentic workflows, robotic foundation models, multi-agent communication/fault tolerance, HITL oversight, economics/finance applications ή derivative/tutorial material.

## Αποφάσεις
Όλες οι παρακάτω πηγές ελέγχθηκαν και χαρακτηρίστηκαν `απόρριψη` χωρίς διαγραφή πρωτοτύπων:

1. `SRC-3ADFA80991` — AAAI-25 robotic foundation-model tutorial transcript.
2. `SRC-A1D7E951DB` — alternate/duplicate conversion του ίδιου tutorial.
3. `SRC-897C38AAF8` — LLM-agent memory practitioner newsletter.
4. `SRC-44678B246F` — generative multi-agent fault-tolerance review.
5. `SRC-AABAFA12BF` — human-in-the-loop safety survey, διαφορετικό capability model.
6. `SRC-DFFF269D33` — communication-MARL survey· policy-induced multi-agent non-stationarity.
7. `SRC-60ECE049E6` — broad RL-for-economics survey, redundant/out-of-domain.
8. `SRC-798A4AFE7E` — finance-agent monograph/application scope.
9. `SRC-6806120384` — LLM-agent engineering workshop.
10. `SRC-6D968A501D` — alternate conversion του ίδιου workshop.
11. `SRC-084A1BFD64` — commercial executive agentic-AI guide.
12. `SRC-10236BC6DB` — generative-agent whitepaper, διαφορετικό agent paradigm.
13. `SRC-C7E22C59DE` — Cisco Live introductory AI-agent slides.
14. `SRC-B1BDB3A5A9` — introductory AI-agents YouTube/tutorial content.
15. `SRC-13CFB90F59` — practitioner LLM-agent implementation book.
16. `SRC-49195612A3` — data-integrity/security essay.
17. `SRC-83030D4158` — LLM-agent adversarial/security survey.
18. `SRC-70A0C89F93` — broad agentic-AI conceptual taxonomy; full conversion not required for current scope.
19. `SRC-50C47991CC` — broad AI-agent overview/essay.
20. `SRC-1F8839FDA8` — derivative Computerphile explanation of canonical `AI Safety Gridworlds` source.

## Επιστημονικές αποφάσεις που κλειδώνουν

- **LLM/agentic autonomy ≠ RL agent resilience.** Tool orchestration, prompt memory και multi-step LLM workflows δεν αποτελούν evidence για policy recovery σε MDP.
- **Policy-induced MARL non-stationarity ≠ exogenous environmental non-stationarity.** Αλλαγές επειδή μαθαίνουν άλλοι agents δεν θα χρησιμοποιούνται ως άμεση απόδειξη για reward/dynamics changepoints.
- **System fault tolerance ≠ policy adaptation.** Replication/checkpointing/network failover και cloud self-healing είναι διαφορετικό επίπεδο μηχανισμού.
- **Human safety oracle changes the information/capability budget.** HITL intervention δεν εισάγεται ως ισοδύναμο baseline χωρίς ξεχωριστή ερευνητική ερώτηση.
- **Derivative tutorials δεν μετρούν ως ανεξάρτητο evidence** όταν υπάρχει ήδη canonical primary paper.

## Αποτέλεσμα
- Νέες αποφάσεις: 20
- Νέες selected: 0
- Νέες exclusions: 20
- Νέα citation-ready excerpts: 0
- Αναμενόμενο canonical σύνολο μετά την παρτίδα: 182 αποφασισμένες πηγές = 91 selected + 91 exclusions.
- Αναμενόμενη υπόλοιπη ουρά: 304 από 486 ενεργές πηγές.
