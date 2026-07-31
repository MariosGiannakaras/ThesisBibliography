# Επιστημονική ανάλυση — SRC-FFE02BA5EF

## Πηγή

**Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments**, Lowe et al., NeurIPS 2017.

## Αξιολόγηση

Η εργασία είναι θεμελιώδης primary source για MADDPG και centralized training with decentralized execution. Αναλύει non-stationarity που προκύπτει επειδή αλλάζουν οι policies άλλων agents και όχι επειδή μεταβάλλονται εξωγενώς reward/transition dynamics του περιβάλλοντος.

## Σχέση με το scope

Το τρέχον πειραματικό σχέδιο είναι single-agent GridWorld με environmental perturbations. Η multi-agent policy-induced non-stationarity είναι διαφορετικό causal mechanism, απαιτεί Markov games, joint actions και διαφορετικά baselines/metrics.

## Απόφαση

**Επαληθευμένη — εξαγωγή όχι λόγω multi-agent scope.** Η πηγή διατηρείται ως canonical MARL reference, αλλά δεν χρησιμοποιείται για claims περί single-agent resilience σε environmental shifts.