# Επιστημονική ανάλυση 10 — Benchmarks και ασφαλής συνεχής προσαρμογή

## Πεδίο

Η παρτίδα καλύπτει τρεις συμπληρωματικούς άξονες:

1. `SRC-0F8A6588DC` — NovGrid: sudden novelty injection και recovery metrics.
2. `SRC-3F84F52F97` — CARL: contextual MDPs, controlled train/test distributions και ID/OOD generalization.
3. `SRC-0406E13B97` — safe continual RL survey: performance και safety constraints κατά nonstationary adaptation.

## Γιατί επιλέχθηκαν μαζί

- Το NovGrid απαντά **πώς εισάγεται και μετριέται μία αιφνίδια αλλαγή**.
- Το CARL απαντά **πώς ορίζονται αναπαραγώγιμα context variables και train/test distributions**.
- Η safe-continual survey απαντά **ποιες πρόσθετες safety/cost διαστάσεις χρειάζονται όταν η προσαρμογή υπό αλλαγή έχει constraints**.

Η σύνθεση αποτρέπει τρεις συγχύσεις:

- static generalization ≠ online recovery,
- final return ≠ adaptation quality,
- performance recovery ≠ safety guarantee.

## Παραδοτέα

- Τρεις πλήρεις επαληθευμένες αναλύσεις.
- Τρία αρχεία evidence με ακριβείς sections/pages/figures.
- Τρεις νέες εγγραφές στην curated επιλογή διπλωματικής.
- Trigger ενημέρωσης μεταδεδομένων μετά από πραγματικές εισαγωγές πηγών, ώστε η λίστα «προς προσθήκη» να μην παραμένει παρωχημένη.

## Περιορισμός scope

Η παρτίδα δεν επιλέγει τελικό GridWorld implementation, models, metrics ή experimental protocol. Οι πηγές χρησιμοποιούνται για να ενημερώσουν τη μελλοντική απόφαση reuse/adapt/custom και το bounded approval pack της κύριας διπλωματικής.