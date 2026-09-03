---
material_id: "MAT-7FE66E620F"
original_path: "originals/unidentified/7FE66E620F8C6A63__Reinforcement Learning and stochastic games.pdf"
original_sha256: "7fe66e620f8c6a63073fa965db83f86f1669a1d6fa91f84c3d45c505942c6457"
original_url: "https://github.com/MariosGiannakaras/ThesisBibliography/blob/ada0d1aec7511098fd12610ae9e5abe7aea875cd/originals/unidentified/7FE66E620F8C6A63__Reinforcement%20Learning%20and%20stochastic%20games.pdf"
linked_source_id: ""
citation_status: "not-citation-ready"
identification_status: "pending-review"
content_status: "full-text-extracted"
page_count: 2
text_characters: 3407
---
<!-- GENERATED_RESEARCH_MATERIAL: v1 -->

# Reinforcement Learning and stochastic games

> Research material retained for drafting and discovery. It may be useful even without complete citation metadata.
> The text below is an un-translated extraction. The original PDF and SHA-256 remain authoritative.

## Technical identity

- **Material ID:** `MAT-7FE66E620F`
- **Original file:** `originals/unidentified/7FE66E620F8C6A63__Reinforcement Learning and stochastic games.pdf`
- **SHA-256:** `7fe66e620f8c6a63073fa965db83f86f1669a1d6fa91f84c3d45c505942c6457`
- **Title candidate:** Reinforcement Learning and stochastic games
- **Author candidate:** kalou
- **Year candidate:** 2021
- **Candidate source:** first-page-or-filename
- **Citation status:** not citation-ready; content remains available for writing and later identification

## Full extracted text by page

<!-- PDF_PAGE: 1 -->
### Page 1

ΕΝΙΣΧΥΤΙΚΗ ΜΗΧΑΝΙΚΗ ΜΑΘΗΣΗ ΚΑΙ ΣΤΟΧΑΣΤΙΚΑ ΠΑΙΓΝΙΑ
(multi agent reinforcement learning)
Περιγραφή
Το μάθημα εξετάζει την ακόλουθη ερώτηση:
• Πως μπορεί μια μονάδα/πράκτορας (agent) να μάθει να ενεργεί για την επίτευξη κάποιου
σκοπού, σε ένα δυναμικό αβέβαιο και μερικώς παρατηρήσιμο περιβάλλον, παρουσία και
άλλων δρώντων μηχανισμών που επιδιώκουν τους δικούς τους σκοπούς?
Το ερώτημα και οι ειδικότερες εκδοχές του (ένας πράκτορας, κοινός σκοπός και συντονισμός ενεργειών
των μονάδων) έχει κεντρικό ενδιαφέρον σε μεγάλο φάσμα εφαρμογών:
 Υπολογιστική όραση, ρομποτική και αυτόνομη οδήγηση
 Επεξεργασία φυσικής γλώσσας
 Παιχνίδια (επιτραπέζια, παιχνίδια με τράπουλες, βιντεο)
 Κυβερνοφυσικά συστήματα
 Ανίχνευση σπάνιων γεγονότων (ανίχνευση και διάγνωση στην ιατρική φροντίδα)
 Επικοινωνίες και ασφάλεια (αντιμετώπιση απειλών και επιθέσεων σε αισθητήρες, κανάλια και
υπολογιστικούς κόμβους)
• Το μάθημα ασχολείται με εκείνες τις απαντήσεις στο παραπάνω ερώτημα οι οποίες στηρίζονται
στη θεωρία τις μεθόδους και τους αλγορίθμους της ενισχυτικής μηχανικής μάθησης
(reinforcement learning).  Ετσι, η αλληλεπίδραση  μεταξύ  των μονάδων και του περιβάλλοντος
στο οποίο ενεργούν ειναι συνεχής. Οι μονάδες παρατηρούν την κατάσταση του περιβάλλοντος
μέσω σχετικών μετρήσεων και έμμεσα αντλούν πληροφορίες για τις ενέργειες των άλλων
μονάδων. Κάποια πληροφοριακά στοιχεία είναι κοινά σε όλες τις μονάδες, άλλα συνιστούν
ιδιωτική πληροφόρηση. Με βάση  τις παρατηρήσεις που έχει στη διάθεση της,  κάθε μονάδα
επιλέγει μια ενέργεια και την εκτελεί. Η κατάσταση του περιβάλλοντος μεταβάλλεται χρονικά
και με αβέβαιο (πιθανοτικό) τρόπο, ανάλογα με την μέχρι τώρα εξέλιξη της και βασει των
ενεργειών των μονάδων. Οι αποφάσεις κάθε μονάδας λαμβάνονται ακολουθιακά (στό χρόνο ή
σε στάδια), στηρίζονται σε κανόνες, συνιστούν δηλαδή πολιτικές και κατά συνέπεια και η
μάθηση είναι ακολουθιακή. Ο κύκλος αυτός επαναλαμβάνεται συνεχώς επιτρέποντας στις
μονάδες να μαθαίνουν πως να ενεργούν ώστε να βελτιώνουν, οχι τη στιγμιαία ανταμειβή, αλλά
το συνολικό μακροπρόθεσμο όφελος/απόδοση.
Ειδικότερα, θα μελετήσουμε:
1. τις θεμελιώδεις μεθόδους της ενισχυτικής μάθησης:
 Μαρκοβιανές διαδικασίες απόφαση (MDPs), μερικώς παρατηρήσιμες MDPs (POMDPs) και
πίστη, Δυναμικός προγραμματισμός και εξίσωση Bellman, Q learning, στοχαστικά παίγνια,
κοινή και ιδιωτική πληροφόρηση, πολλαπλοί πράκτορες, ισορροπίες
 Εξομείωση και αλγόριθμοι στοχαστικής προσέγγισης
 Βασικές προσεγγιστικές δομές, βαθειά νευρωνικά δίκτυα με και χωρίς μνήμη.

<!-- PDF_PAGE: 2 -->
### Page 2

2. Αντιπρόσωπους αλγορίθμων ενισχυτικής μάθησης (vanilla policy gradient VPG, trust region policy
optimization TRPO, proximal policy optimization PPO, Deep deterministic policy gradient DPPG, Twin
delayed DDPG, TD3, Soft Actor Critic SAC, DQN, DDQN, και άλλους)
3. Βιβλιοθήκες αλγορίθμων ενισχυτικής μάθησης (Stable baselines3), βιβλιοθήκες με
προεγκατεστημένα περιβάλλοντα (OpenAI Gym) και υποκείμενες βιβλιοθήκες νευρωνικών δικτύων
(Pytorch).
Μαθησιακοί στόχοι
Απόκτηση γνώσεων και δεξιοτήτων σε μια σημαντική περιοχή της μηχανικής μάθησης που έχει
ισχυρούς δεσμούς με τον βέλτιστο έλεγχο (Optimal control), την επιχειρησιακή έρευνα (Operations
Research), τις προσεγγιστικές δομές (στοχαστική προσέγγιση, νευρωνικά δίκτυα), την εξομείωση, τη
θεωρία πληροφορίας και τη θεωρία παιγνίων, με εξαιρετικές επιτυχίες τα τελευταία χρόνια
Αξιολόγηση:
Συμμετοχή στο μάθημα, Εργασία
Πιστωτικές μονάδες: ECTS 6
