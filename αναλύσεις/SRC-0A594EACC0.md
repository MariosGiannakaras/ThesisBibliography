---
κωδικός: SRC-0A594EACC0
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "arXiv:2409.13187v2 και IEEE TAI metadata"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-07-31"
---

# Cooperative Resilience in Artificial Intelligence Multiagent Systems

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Manuela Chacon-Chamorro, Luis Felipe Giraldo, Nicanor Quijano, Vicente Vargas-Panesso, César González, Juan Sebastián Pinzón, Rubén Manrique, Manuel Ríos, Yesid Fonseca, Daniel Gómez-Barrera, Mónica Perdomo-Pérez
- **Έτος:** 2024 preprint· μεταγενέστερη δημοσίευση IEEE TAI 2025
- **Τύπος πηγής:** θεωρητική πρόταση ορισμού και εμπειρική μεθοδολογία μέτρησης
- **DOI / arXiv / URL:** arXiv:2409.13187· DOI:10.1109/TAI.2025.3567371
- **Πρωτότυπο που ελέγχθηκε:** `πρωτότυπα/SRC-0A594EACC0.pdf`

## Σκοπός και ερευνητικό ερώτημα

Η εργασία επιχειρεί να ορίσει και να μετρήσει την «cooperative resilience» σε multi-agent AI systems. Ρωτά ποια οντότητα θεωρείται resilient, απέναντι σε ποιο disruptive event και ποιες χρονικές ικανότητες συνθέτουν resilience: anticipation, preparation, resistance, recovery και transformation.

Η παρούσα διπλωματική είναι κατά βάση σύγκριση decision-making agents και όχι μελέτη collective welfare. Επομένως, η πηγή δεν αποτελεί άμεση απόδειξη για single-agent algorithm superiority. Είναι όμως πολύ χρήσιμη για τη λειτουργικοποίηση της resilience: απαιτεί reference behavior χωρίς disruption, performance curve με disruption, σαφή incidence/failure/recovery times και χωριστή αποτίμηση της πτώσης και της ανάκαμψης. Αυτά ευθυγραμμίζονται άμεσα με την επίσημη απαίτηση αξιολόγησης «ανθεκτικότητας και ταχύτητας ανάκαμψης».

## Σύνοψη

Οι συγγραφείς συνθέτουν ορισμούς resilience από engineering, ecology, psychology, economics, network science και dynamical systems. Προτείνουν ότι cooperative resilience είναι η ικανότητα ενός collective system να anticipates, prepares for, resists, recovers from και transforms under disruptive events που απειλούν το joint welfare.

Η μέτρηση οργανώνεται σε τέσσερα στάδια. Πρώτα επιλέγονται time-dependent well-being variables και δημιουργούνται performance και reference curves με και χωρίς disruption. Έπειτα, για κάθε event και variable, υπολογίζεται summary metric που συνδυάζει failure profile και recovery profile στο αντίστοιχο time window. Στο τρίτο στάδιο συναρμολογούνται successive disruptions, με reward για βελτίωση και penalty για χειροτέρευση. Τέλος, οι variables συνδυάζονται σε συνολικό resilience score με harmonic mean, ώστε πολύ χαμηλή επίδοση σε μία κρίσιμη διάσταση να μην κρύβεται από υψηλές τιμές στις υπόλοιπες.

Η μεθοδολογία εφαρμόζεται στο Melting Pot 2.0 Commons Harvest Open με RL και LLM-augmented agents. Δύο disruption families εξετάζονται: stochastic apple removal με διαφορετικό αριθμό και severity events, και προσωρινή εισαγωγή unsustainable bots. Τα αποτελέσματα δείχνουν ότι η resilience map μπορεί να αναδείξει non-monotonic ή history-dependent συμπεριφορά που δεν φαίνεται από ένα απλό cumulative resource metric.

## Μεθοδολογία

- **Resilient entity:** collective multi-agent system, ανθρώπινο ή τεχνητό.
- **Disruptions:** εξωτερική αφαίρεση πόρων και εσωτερική εισαγωγή agents με unsustainable policy.
- **Stage I:** construction performance curves P(t) και reference curves R(t) για επιλεγμένες variables.
- **Stage II:** event-specific summary metric J που συνδυάζει failure και recovery profile, incident time, failure time και recovery/stabilization time.
- **Stage III:** aggregation πολλαπλών events με penalty/reward για deterioration ή transformation across disruptions.
- **Stage IV:** harmonic mean across variables.
- **Environment:** Melting Pot 2.0 Commons Harvest Open.
- **Decision systems:** independent PPO agents και LLM-augmented generative agents.
- **Indicators:** apples alive per capita, trees alive per capita, cumulative Gini equality και collective hunger.
- **Scenario factors:** αριθμός disruptive events, event timing, depletion severity και duration unsustainable-bot exposure.

## Κύρια ευρήματα

1. **Resilience απαιτεί explicit entity, disruption και expected behavior.** Δεν έχει νόημα να δηλωθεί ότι ένας agent είναι «resilient» χωρίς να οριστεί απέναντι σε ποια αλλαγή και σε σχέση με ποια reference curve. Τεκμηρίωση: Sections 1–2.
2. **Η resilience είναι χρονική διαδικασία, όχι ένα τελικό score.** Resistance, failure depth, recovery speed και transformation ανήκουν σε διαφορετικές φάσεις πριν, κατά και μετά το disruption. Τεκμηρίωση: Definition 1 και Section 3.
3. **Reference και performance curves είναι απαραίτητες.** Η συμπεριφορά με disruption συγκρίνεται με αντίστοιχη no-disruption συμπεριφορά, όχι μόνο με αυθαίρετο absolute threshold. Τεκμηρίωση: Section 3.1 και Figure 2.
4. **Failure και recovery πρέπει να αποτυπώνονται χωριστά.** Το event-specific metric χρησιμοποιεί failure profile για magnitude/speed της πτώσης και recovery profile για speed/stabilization μετά το minimum. Η πλήρης επιστροφή στο reference δεν θεωρείται δεδομένη. Τεκμηρίωση: Section 3.2 και Equation 1.
5. **Η severity και η συχνότητα disruptions πρέπει να παραμετροποιούνται ανεξάρτητα.** Στα apple-removal experiments μεταβάλλονται αριθμός events και magnitude v_s, δημιουργώντας εννέα scenarios. Τεκμηρίωση: Section 4.3.1 και Table 2.
6. **Ένα aggregate resilience score μπορεί να κρύψει ή να αναδείξει history effects ανάλογα με τον ορισμό του.** Η proposed Stage III ανταμείβει βελτίωση σε successive disruptions, οπότε περισσότερα events δεν οδηγούν αναγκαστικά σε μικρότερο score. Αυτό είναι feature του metric αλλά και σημαντική ερμηνευτική προειδοποίηση. Τεκμηρίωση: Sections 3.3 και 4.3.1, Figures 4–5.
7. **Μία μόνο performance variable δεν επαρκεί σε multi-objective systems.** Η harmonic mean penalizes πολύ χαμηλή τιμή σε μία well-being dimension. Για single-agent GridWorld η ίδια αρχή υποδεικνύει ότι return, safety violations και recovery δεν πρέπει να συμπιεστούν άκριτα σε έναν αριθμό. Τεκμηρίωση: Section 3.4.

## Υποθέσεις και ορισμοί

Ο προτεινόμενος ορισμός αφορά συλλογικά συστήματα και joint welfare. Οι performance variables πρέπει να έχουν θετική ερμηνεία, δηλαδή μεγαλύτερη τιμή να σημαίνει καλύτερο αποτέλεσμα. Τα disruptive events θεωρούνται stochastic ως προς occurrence ή magnitude και αναλύονται μέσα σε time windows με incident, failure και recovery landmarks.

Για τη διπλωματική, μια ασφαλής μεταφορά είναι να υιοθετηθούν οι χρονικές έννοιες χωρίς να χρησιμοποιηθεί ο όρος «cooperative»:

- **reference curve:** expected performance του ίδιου agent/algorithm χωρίς disruption ή με oracle post-change baseline,
- **resistance/degradation:** μέγεθος και ταχύτητα πτώσης μετά το event,
- **recovery time:** steps/episodes μέχρι προκαθορισμένη σταθεροποίηση,
- **recovery quality:** post-change plateau σε σχέση με reference/oracle,
- **transformation/learning across events:** βελτίωση στη δεύτερη έκθεση ίδιου ή σχετικού disruption.

## Περιορισμοί και απειλές εγκυρότητας

Η θεωρία και τα indicators σχεδιάζονται για multi-agent joint welfare, social dilemmas και resource sustainability. Η μεταφορά σε single-agent GridWorld απαιτεί νέο ορισμό variables και δεν επιτρέπει αυτούσια χρήση του cooperative-resilience score. Η επιλογή incident/failure/recovery points μπορεί να είναι ευαίσθητη σε smoothing και noisy curves. Η harmonic mean απαιτεί comparable positive indicators και μπορεί να είναι ασταθής κοντά στο μηδέν.

Τα experiments έχουν διαφορετικές interaction semantics για PPO και LLM agents, περιορισμένο αριθμό episodes για ορισμένες curves και custom transformations. Το Stage III reward για improvement across events μπορεί να δημιουργήσει counterintuitive rankings. Η πηγή αναγνωρίζει ότι μεγαλύτερο disruption δεν οδηγεί πάντα σε monotonic lower score λόγω stochastic dynamics και interaction effects.

Στη διπλωματική πρέπει να διατηρηθούν οι primitive metrics και οι full curves ως primary results. Ένας composite resilience index, αν χρησιμοποιηθεί, πρέπει να θεωρείται secondary summary και να συνοδεύεται από sensitivity analysis.

## Σχέση με άλλες πηγές

Το `SRC-0A4AFAC8E9` παρέχει στατιστικά αξιόπιστο τρόπο aggregation πολλαπλών runs. Το `SRC-95C9DAEE68` ορίζει detection/adaptation metrics σε non-stationary RL. Το `SRC-D14764616F` προσφέρει repeated-context scenario για retention και transformation. Το `SRC-0AEF7EF16A` δείχνει empirically διαφορετική recovery trajectory μετά από changing dynamics.

## Χρήση στη διπλωματική

- **Προτεινόμενα κεφάλαια:** ορισμοί, ερευνητικά ερωτήματα, metrics, experimental protocol, discussion και threats to validity.
- **Ισχυρισμοί που μπορεί να υποστηρίξει:** resilience πρέπει να ορίζεται σε σχέση με disruption και reference behavior· degradation και recovery είναι χωριστές χρονικές διαστάσεις· multiple severity/frequency scenarios είναι απαραίτητα.
- **Πειραματική συνέπεια:** να αποθηκεύονται raw per-step/per-episode curves, incident time, minimum performance, time-to-threshold και post-change plateau. Να εξεταστεί recovery AUC ή normalized performance gap ως secondary summary.
- **Τι δεν πρέπει να ισχυριστούμε:** ότι το cooperative-resilience index είναι validated για single-agent GridWorld, ότι composite score αρκεί μόνο του, ή ότι τα αποτελέσματα PPO-versus-LLM μεταφέρονται στους agents της διπλωματικής.

## Κατάσταση επαλήθευσης

- **Κατάσταση:** επαληθευμένη.
- **Έλεγχος πρωτοτύπου:** ελέγχθηκε το arXiv PDF, με έμφαση σε Abstract, Sections 1–4, Definition 1, Equation 1, Figures 2, 4–7 και Tables 1–2.
- **Απόφαση:** υποστηρικτική αλλά υψηλής αξίας πηγή για τον λειτουργικό ορισμό resilience και τον σχεδιασμό degradation/recovery metrics, με ρητό περιορισμό της μεταφοράς από multi-agent σε single-agent setting.
