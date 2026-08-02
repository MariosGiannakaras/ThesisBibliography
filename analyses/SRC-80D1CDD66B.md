# SRC-80D1CDD66B — Guiding Reinforcement Learning Using Uncertainty-Aware Large Language Models

## Απόφαση

**Απόρριψη από το core bibliography/export.**

Η εργασία χρησιμοποιεί LLM trainer, MC-dropout uncertainty και policy shaping σε MiniGrid. Είναι τεχνικά ενδιαφέρουσα, αλλά το κεντρικό ερευνητικό ερώτημα αφορά αξιοπιστία εξωτερικής LLM guidance και όχι προσαρμογή ενός RL agent σε exogenous environmental change.

## Αιτιολόγηση

- Εισάγει δεύτερο learned system, το LLM, με δικό του calibration problem.
- Η uncertainty αφορά reliability της advice, όχι transition/reward/context uncertainty του environment.
- Το policy-shaping mechanism θα άλλαζε ουσιωδώς το scope και το compute stack της διπλωματικής.
- Η χρήση MiniGrid από μόνη της δεν καθιστά τη μέθοδο evidence για resilience.
- Η σχετική ιδέα MC-dropout uncertainty καλύπτεται ήδη από το canonical `SRC-7C18826BEE`.

Η πηγή διατηρείται για πιθανή μελλοντική επέκταση human/LLM-in-the-loop, αλλά δεν εξάγεται.