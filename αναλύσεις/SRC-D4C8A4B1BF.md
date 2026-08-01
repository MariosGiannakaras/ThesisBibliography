---
κωδικός: SRC-D4C8A4B1BF
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "Algorithms 2023, 16(3), 165"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Resilience and Resilient Systems of Artificial Intelligence: Taxonomy, Models and Methods

## Βιβλιογραφική ταυτότητα
Viacheslav Moskalenko, Vyacheslav Kharchenko, Alona Moskalenko, Borys Kuzikov. *Algorithms* 16(3), 165, 2023. DOI: 10.3390/a16030165.

## Σκοπός
Systematic review/taxonomy για resilience σε AI systems. Η εργασία προσπαθεί να ενοποιήσει κατακερματισμένες χρήσεις των όρων robustness, fault tolerance, graceful degradation, recovery, adaptation, concept drift και adversarial/fault disturbances.

## Κεντρική διάκριση robustness–resilience
Η εργασία επισημαίνει ότι σε μεγάλο μέρος της βιβλιογραφίας το `resilience` χρησιμοποιείται σαν συνώνυμο μίας μόνο ιδιότητας, συχνά robustness ή fault tolerance. Αντίθετα, ένα resilient AI system πρέπει να καλύπτει ευρύτερο κύκλο από:

1. προετοιμασία/ανίχνευση,
2. absorption/withstanding της διαταραχής,
3. graceful degradation όταν η πλήρης λειτουργία δεν μπορεί να διατηρηθεί,
4. recovery της χαμένης performance/functionality,
5. adaptation ώστε να αντιμετωπίζει καλύτερα μελλοντικές διαταραχές.

Αυτό ευθυγραμμίζεται άμεσα με τη βασική thesis distinction ότι **robustness δεν είναι resilience** και ότι final worst-case performance μόνο του δεν περιγράφει recovery/adaptation.

## Resilience stages
Η εργασία χρησιμοποιεί τετραφασικό system-resilience framing:
- planning/preparation,
- absorption,
- recovery,
- adaptation.

Για RL agents αυτό μπορεί να χαρτογραφηθεί προσεκτικά ως:
- detector/preparation mechanisms,
- immediate performance degradation/robustness,
- post-change recovery curve,
- continued learning/context update.

Η χαρτογράφηση είναι thesis-specific και δεν πρέπει να παρουσιαστεί σαν να προτείνεται αυτούσια από τους συγγραφείς για tabular RL.

## Affordable resilience
Ιδιαίτερα χρήσιμη για τη διπλωματική είναι η έννοια **affordable resilience**: η ανθεκτικότητα πρέπει να αξιολογείται μαζί με life-cycle/resource cost και όχι ως δωρεάν ιδιότητα.

Η εργασία συζητά trade-off μεταξύ nominal performance και resilience indicator υπό resource constraints. Αυτό παρέχει cross-domain rationale για την ήδη επιλεγμένη resource-aware αξιολόγηση:
- memory overhead,
- compute/update overhead,
- prior-data/training cost,
- adaptation interactions,
- performance benefit.

## Resilience indicators
Η review τονίζει ότι πολλές εργασίες μετρούν μόνο ένα μέρος του resilience profile, π.χ. ability to absorb perturbation χωρίς recovery rate ή recovery rate χωρίς degradation/absorption. Αυτό υποστηρίζει πολυδιάστατο scorecard αντί ενός scalar resilience score.

## Συνάφεια με τη διπλωματική
Η πηγή χρησιμοποιείται ως **εννοιολογικό/ορολογικό foundation**, όχι ως algorithmic evidence.

Κλειδώνει ότι η πειραματική αξιολόγηση πρέπει να διαχωρίζει:
- robustness / immediate retained performance,
- degradation magnitude,
- recovery speed,
- final adapted performance,
- adaptation/learning after recovery,
- resource cost.

## Περιορισμοί
- Broad AI/system review, όχι RL-specific experimental paper.
- Περιλαμβάνει cybersecurity, fault tolerance, adversarial attacks και system-engineering threats εκτός του core non-adversarial GridWorld scope.
- Η taxonomy είναι synthesis και όχι proof ότι κάθε listed mechanism βελτιώνει RL resilience.
- Δεν παρέχει matched agent comparison ή changepoint benchmark.

## Χρήση στη διπλωματική
**Υποστηρικτική πηγή για definitions και evaluation architecture.**

Δεν χρησιμοποιείται για να δικαιολογήσει συγκεκριμένο RL agent. Χρησιμοποιείται για:
1. robustness ≠ resilience,
2. absorption/recovery/adaptation ως διαφορετικές phases,
3. graceful degradation ως μετρήσιμη intermediate behavior,
4. affordable/resource-aware resilience,
5. ανάγκη πολυδιάστατων metrics.

## Νέες protocol απαιτήσεις
- Report immediate degradation magnitude χωριστά από recovery time.
- Report resource overhead δίπλα στο resilience benefit.
- Αν χρησιμοποιηθεί aggregate resilience score, να παραμένουν διαθέσιμες οι constituent metrics ώστε να μην κρύβονται trade-offs.
- `Graceful degradation` operationalized ως controlled/limited performance loss ή constraint-preserving fallback, όχι ως generic wording.

## Κατάσταση επαλήθευσης
Ελέγχθηκε το πλήρες journal PDF. **Επιλέγεται ως supporting conceptual source.**