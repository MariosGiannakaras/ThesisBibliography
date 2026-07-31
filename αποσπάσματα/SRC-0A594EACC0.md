---
κωδικός: SRC-0A594EACC0
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Αποσπάσματα — Cooperative Resilience in Artificial Intelligence Multiagent Systems

## Τεκμήριο E1

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 2–3, Definition 1 και επεξήγηση του ορισμού
- **Ισχυρισμός:** Η resilience πρέπει να ορίζεται ως χρονική ικανότητα που περιλαμβάνει αντίσταση, ανάκαμψη και μετασχηματισμό απέναντι σε συγκεκριμένο disruptive event, όχι απλώς ως υψηλή τελική επίδοση.
- **Κεφάλαιο:** Θεωρητικό υπόβαθρο — ορισμός resilience
- **Θέματα:** resilience, resistance, recovery, transformation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Οι συγγραφείς ορίζουν την cooperative resilience ως την ικανότητα ενός συστήματος συλλογικής δράσης να προβλέπει και να προετοιμάζεται, να αντιστέκεται, να ανακάμπτει και να μετασχηματίζεται όταν disruptive events απειλούν την κοινή του ευημερία. Με αυτόν τον ορισμό, η resilience καλύπτει διαφορετικές φάσεις πριν, κατά και μετά τη διαταραχή και περιλαμβάνει τη δυνατότητα μάθησης από προηγούμενα events.

### Συμφραζόμενα

Ο ορισμός αφορά cooperative systems. Στη διπλωματική μπορεί να χρησιμοποιηθεί σε single-agent μορφή μόνο αφού αντικατασταθεί το joint welfare από σαφώς ορισμένες task και safety performance variables.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να ταυτιστεί η resilience με zero-shot robustness ή με adaptation μόνο. Ένας πράκτορας μπορεί να είναι robust χωρίς να μαθαίνει, ή adaptive αλλά με πολύ μεγάλη αρχική κατάρρευση.

### Προτεινόμενη χρήση

Να στηρίξει τον κεντρικό λειτουργικό ορισμό και τον διαχωρισμό robustness, adaptation και resilience.

### Παραπομπή

Chacon-Chamorro et al. (2024), σελ. 2–3, Definition 1.

## Τεκμήριο E2

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 3–6, Sections 3.1–3.2 και Equation 1
- **Ισχυρισμός:** Η ποσοτική μέτρηση resilience μπορεί να βασιστεί στη σύγκριση performance και reference curves μέσα σε event windows που διαχωρίζουν failure και recovery profiles.
- **Κεφάλαιο:** Μετρικές και πειραματικό πρωτόκολλο
- **Θέματα:** reference curve, degradation, failure profile, recovery profile
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Για κάθε relevant variable κατασκευάζεται reference curve χωρίς disruption και performance curve υπό disruption. Σε παράθυρο που περιέχει incident time, failure time και recovery time, το failure profile και το recovery profile υπολογίζονται ως λόγοι του εμβαδού κάτω από την performance curve προς το αντίστοιχο εμβαδό κάτω από τη reference curve. Ο summary δείκτης συνδυάζει τα δύο profiles με τη διάρκειά τους, ώστε να λαμβάνονται υπόψη τόσο η έκταση όσο και η χρονική εξέλιξη της υποβάθμισης και της ανάκαμψης.

### Συμφραζόμενα

Η reference curve δεν χρειάζεται να είναι ιδανική· είναι η αναμενόμενη συμπεριφορά του ίδιου συστήματος χωρίς το disruptive event. Αυτό είναι κατάλληλο για matched-seed nominal/perturbed runs στο GridWorld.

### Περιορισμοί και κίνδυνος παρερμηνείας

Η μέθοδος απαιτεί θετικά προσανατολισμένες variables και συνεπή επιλογή incident, failure και recovery times. Αυθαίρετα windows μπορούν να αλλάξουν το score. Οι raw curves και οι επιμέρους metrics πρέπει να δημοσιεύονται μαζί με το composite.

### Προτεινόμενη χρήση

Να αιτιολογήσει normalized performance deficit, area-under-reference loss και recovery-time metrics.

### Παραπομπή

Chacon-Chamorro et al. (2024), σελ. 3–6, Sections 3.1–3.2, Equation 1.

## Τεκμήριο E3

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδα 6, Sections 3.3–3.4
- **Ισχυρισμός:** Η αξιολόγηση διαδοχικών disruptions πρέπει να εξετάζει αν η απόκριση βελτιώνεται ή χειροτερεύει από event σε event και όχι μόνο να υπολογίζει ανεξάρτητο μέσο όρο.
- **Κεφάλαιο:** Μετρικές — repeated changes
- **Θέματα:** repeated disruptions, transformation, continual adaptation
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Η τρίτη φάση της μεθόδου συνδυάζει τα resilience scores διαδοχικών events με κανόνα που επιβραβεύει θετική μεταβολή και τιμωρεί αρνητική. Έτσι επιχειρεί να αποτυπώσει transformation: ένα σύστημα που μαθαίνει από προηγούμενη διαταραχή μπορεί να αντιμετωπίσει καλύτερα την επόμενη. Στην τέταρτη φάση οι διαφορετικές welfare variables συνδυάζονται με harmonic mean, ώστε μία πολύ αδύναμη διάσταση να επηρεάζει έντονα το τελικό score.

### Συμφραζόμενα

Η λογική repeated-event evaluation ταιριάζει με non-stationary GridWorld, όπου η ίδια ή διαφορετική αλλαγή εμφανίζεται περισσότερες φορές και μετράται learning-to-recover.

### Περιορισμοί και κίνδυνος παρερμηνείας

Ο συγκεκριμένος nonlinear aggregation rule μπορεί να δημιουργεί μη μονοτονικά αποτελέσματα και απαιτεί sensitivity analysis. Η διπλωματική δεν πρέπει να υιοθετήσει αυτούσιο το τελικό score χωρίς να παρουσιάσει και event-level αποτελέσματα.

### Προτεινόμενη χρήση

Να στηρίξει τη δημιουργία repeated-shift scenarios και metric “change in recovery performance across events”.

### Παραπομπή

Chacon-Chamorro et al. (2024), σελ. 6, Sections 3.3–3.4.

## Τεκμήριο E4

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 8–10, Section 4.3.1, Figures 4–5
- **Ισχυρισμός:** Πολλαπλές performance variables μπορούν να αποκαλύψουν καθυστερημένες ή έμμεσες συνέπειες μιας perturbation που δεν εμφανίζονται στο άμεσο task score.
- **Κεφάλαιο:** Μετρικές και αποτελέσματα
- **Θέματα:** multidimensional evaluation, delayed degradation, adaptive response
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Μετά την αφαίρεση μήλων, η άμεση πτώση φαίνεται στην resource availability, ενώ η απώλεια δέντρων, η ανισότητα και το collective hunger μπορούν να επιδεινωθούν αργότερα. Οι reference/performance curves δείχνουν ότι μία disruption έχει διαφορετική χρονική υπογραφή ανά indicator. Το τελικό resilience map εμφανίζει γενική πτώση με μεγαλύτερη ένταση και περισσότερα events, αλλά και μη αναμενόμενες εξαιρέσεις που αποδίδονται σε transformation ή σε complex scenario dynamics.

### Συμφραζόμενα

Οι συγκεκριμένες welfare variables είναι domain-specific. Η γενική αρχή είναι ότι return, safety violations, success rate και recovery quality πρέπει να αναλύονται χωριστά.

### Περιορισμοί και κίνδυνος παρερμηνείας

Τα plots βασίζονται σε πέντε episodes και τα μη μονοτονικά patterns δεν αποτελούν ισχυρή απόδειξη learning without additional statistical analysis.

### Προτεινόμενη χρήση

Να αιτιολογήσει πολλαπλές μετρικές και time-resolved curves αντί ενός συνολικού reward score.

### Παραπομπή

Chacon-Chamorro et al. (2024), σελ. 8–10, Section 4.3.1, Figures 4–5.

## Τεκμήριο E5

- **Τύπος:** πιστή παράφραση
- **Θέση:** σελίδες 10–12, Section 4.3.2, Figures 6–7, Discussion και Conclusion
- **Ισχυρισμός:** Η recovery behavior μπορεί να διαφοροποιεί συστήματα ακόμη και όταν η ίδια disturbance προκαλεί παρόμοια αρχική υποβάθμιση.
- **Κεφάλαιο:** Αποτελέσματα και threats to validity
- **Θέματα:** recovery slope, disruption duration, preliminary evidence
- **Κατάσταση:** επαληθευμένο

### Κείμενο ή πιστή παράφραση

Στο scenario με unsustainable bots, μεγαλύτερη διάρκεια παρουσίας οδηγεί σε χαμηλότερα resilience scores. Μετά την αποχώρηση των bots, οι RL agents συνεχίζουν περίπου την προηγούμενη resource-consumption pattern, ενώ οι LLM agents εμφανίζουν αλλαγή κλίσης προς την reference behavior. Η metric καταγράφει αυτή τη διαφορά ως recovery/adaptation profile. Οι συγγραφείς χαρακτηρίζουν τα αποτελέσματα preliminary και ζητούν περισσότερα scenarios και experiments.

### Συμφραζόμενα

Η σύγκριση PPO και GPT-4 δεν είναι ισοδύναμη ως προς training, action timing ή computational budget. Το χρήσιμο τεκμήριο αφορά τη μέτρηση της τροχιάς ανάκαμψης, όχι την ανωτερότητα ενός model family.

### Περιορισμοί και κίνδυνος παρερμηνείας

Δεν πρέπει να γενικευτεί ότι LLM agents είναι περισσότερο resilient. Το αποτέλεσμα αφορά έναν συγκεκριμένο social-dilemma disruption και λίγες επαναλήψεις.

### Προτεινόμενη χρήση

Να στηρίξει recovery slope, time-to-threshold και post-recovery steady-state metrics, μαζί με ρητή προειδοποίηση για περιορισμένη εξωτερική εγκυρότητα.

### Παραπομπή

Chacon-Chamorro et al. (2024), σελ. 10–12, Sections 4.3.2–5.