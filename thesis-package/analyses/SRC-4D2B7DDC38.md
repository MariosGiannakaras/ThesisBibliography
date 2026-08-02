# SRC-4D2B7DDC38 — Distributionally Robust Reinforcement Learning with Interactive Data Collection

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Miao Lu, Han Zhong, Tong Zhang, Jose Blanchet
- **Έκδοση:** 2024, αναθεώρηση 13 Ιουλίου 2026
- **Τύπος:** θεωρητική εργασία distributionally robust RL
- **Ρόλος στη διπλωματική:** υποστηρικτική

## Ερευνητικό ερώτημα

Η εργασία εξετάζει αν μπορεί να μαθευτεί sample-efficient robust policy όταν ο πράκτορας συλλέγει δεδομένα μόνο με κανονική αλληλεπίδραση στο training environment. Δεν διαθέτει generative model που επιτρέπει queries σε οποιοδήποτε state-action pair και δεν υποθέτει offline dataset με κάλυψη των deployment dynamics.

## Κεντρικό αποτέλεσμα: curse of support shift

Η εργασία αποδεικνύει ότι γενικά η sample-efficient μάθηση μπορεί να είναι αδύνατη όταν states που είναι σημαντικά στα testing environments είναι απρόσιτα ή εξαιρετικά σπάνια στο training environment. Το πρόβλημα δεν λύνεται απλώς με περισσότερο exploration όταν οι supports είναι ουσιαστικά ασύνδετες.

Αυτό είναι ιδιαίτερα σημαντικό για τη διπλωματική: ένας agent που εκπαιδεύεται μόνο σε ένα fixed layout δεν μπορεί να θεωρηθεί robust σε structural shifts που δημιουργούν νέα reachable regions ή transition patterns που δεν εμφανίστηκαν ποτέ στην training distribution.

## Tractable subclass και algorithm

Για total-variation robust sets, οι συγγραφείς εισάγουν πρόσθετη assumption που αποκλείει τις support-shift παθολογίες και προτείνουν optimistic robust planning algorithm με near-optimal sample complexity. Επεκτείνουν επίσης το πλαίσιο σε άλλο robust-set formulation και Markov games.

## Συνάφεια

Η εργασία λειτουργεί κυρίως ως limitation theorem και protocol-design source:

- απαιτεί coverage diagnostics,
- αποτρέπει υπερβολικούς ισχυρισμούς sim-to-real/generalization,
- αιτιολογεί train distributions με ποικιλία layouts και transitions,
- διαχωρίζει ordinary sampling uncertainty από structural support mismatch.

Δεν αποτελεί άμεσο practical baseline για τη βασική GridWorld υλοποίηση.

## Πειραματικές απαιτήσεις

- Καταγραφή state/transition coverage ανά training regime.
- Αναφορά unseen states ή unseen transition tuples μετά την αλλαγή.
- Χωριστά tests για in-support parameter shift και out-of-support structural shift.
- Training distributions που δεν χρησιμοποιούν πληροφορίες από το final test schedule.
- Αποφυγή ισχυρισμού robustness όταν η test support δεν καλύπτεται από το training interaction.
- Προαιρετικό coverage-overlap metric ανά scenario.

## Περιορισμοί

- Η εργασία είναι κυρίως θεωρητική και δεν συγκρίνει τους πρακτικούς baselines της διπλωματικής.
- Το tractable result βασίζεται σε ειδική assumption και συγκεκριμένη robust-set δομή.
- Distributional robustness δεν συνεπάγεται rapid recovery μετά από changepoint.
- Η inventory-control εφαρμογή δεν αποτελεί GridWorld evidence.
- Η έκδοση του 2026 πρέπει να αναφέρεται με ακρίβεια και όχι ως παλαιότερο αμετάβλητο preprint.

## Απόφαση

**Επιλογή ως υποστηρικτική πηγή.** Κεντρική χρήση: support-shift limitation, coverage-aware benchmark design και οριοθέτηση των claims robust/generalization.