---
κωδικός: SRC-9DCA1F02C1
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Αποσπάσματα — Leveraging Procedural Generation to Benchmark RL

## Τεκμήριο E1
- **Τύπος:** πιστή παράφραση
- **Θέση:** Abstract και §§1–2
- **Ισχυρισμός:** Procedural generation επιτρέπει χωριστά train/test level distributions.
- **Κατάσταση:** επαληθευμένο

Το Procgen δημιουργεί μεγάλο αριθμό randomized levels, ώστε η policy να μην αξιολογείται επανειλημμένα στις ίδιες σχεδόν καταστάσεις.

**Παραπομπή:** Cobbe et al., 2020, Abstract και §§1–2.

## Τεκμήριο E2
- **Τύπος:** πιστή παράφραση
- **Θέση:** §2.2
- **Ισχυρισμός:** Sample efficiency και generalization έχουν διαφορετικά protocols.
- **Κατάσταση:** επαληθευμένο

Για sample efficiency, training και testing γίνονται στην πλήρη level distribution. Για generalization, η training policy βλέπει finite level set και αξιολογείται σε unseen levels.

**Παραπομπή:** Cobbe et al., 2020, §2.2.

## Τεκμήριο E3
- **Τύπος:** πιστή παράφραση
- **Θέση:** §3.1
- **Ισχυρισμός:** Μικρά training sets προκαλούν ισχυρό overfitting.
- **Κατάσταση:** επαληθευμένο

Σε πολλά environments, η test performance παραμένει πολύ χαμηλότερη από την training performance και απαιτούνται χιλιάδες distinct levels για να περιοριστεί το gap.

**Παραπομπή:** Cobbe et al., 2020, §3.1.

## Τεκμήριο E4
- **Τύπος:** πιστή παράφραση
- **Θέση:** §3.2
- **Ισχυρισμός:** Fixed level sequence μπορεί να δίνει ψευδή εικόνα μάθησης.
- **Κατάσταση:** επαληθευμένο

Οι agents γίνονται ικανοί στα πρώτα deterministic training levels, αλλά όταν η test sequence τυχαιοποιείται η επίδοση δείχνει ότι έχει μαθευτεί ελάχιστη γενικεύσιμη structure.

**Παραπομπή:** Cobbe et al., 2020, §3.2.

## Τεκμήριο E5
- **Τύπος:** πιστή παράφραση
- **Θέση:** §3.3
- **Ισχυρισμός:** Το recommended generalization protocol χρησιμοποιεί held-out levels.
- **Κατάσταση:** επαληθευμένο

Η εργασία προτείνει training σε 500 hard-distribution levels και zero-shot αξιολόγηση στην unseen level distribution ως πρακτικό benchmark compromise.

**Περιορισμός:** ο αριθμός 500 δεν μεταφέρεται αυτούσιος στο μικρό GridWorld.

**Παραπομπή:** Cobbe et al., 2020, §3.3.

## Τεκμήριο E6
- **Τύπος:** πιστή παράφραση
- **Θέση:** §§4–5
- **Ισχυρισμός:** Model size και algorithm ordering εξαρτώνται από compute και environment.
- **Κατάσταση:** επαληθευμένο

Μεγαλύτερες architectures βελτιώνουν συχνά sample efficiency/generalization, ενώ PPO και Rainbow έχουν διαφορετική επίδοση ανά environment.

**Χρήση:** resource reporting και αποφυγή aggregate universal rankings.

**Παραπομπή:** Cobbe et al., 2020, §§4–5.
