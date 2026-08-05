---
κωδικός: SRC-AC30CEB175
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "MDPI Sustainability 16(12):4959, JATS XML, DOI 10.3390/su16124959"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-05"
---

# AI Applications to Enhance Resilience in Power Systems and Microgrids—A Review

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Younes Zahraoui, Tarmo Korõtko, Argo Rosin, Saad Mekhilef, Mehdi Seyedmahmoudian, Alex Stojcevski, Ibrahim Alhamrouni
- **Έτος:** 2024
- **Τύπος πηγής:** peer-reviewed review article για εφαρμογές AI στη resilience ηλεκτρικών συστημάτων και microgrids
- **Περιοδικό:** Sustainability, 16(12), 4959
- **DOI:** https://doi.org/10.3390/su16124959
- **Πρωτότυπο που ελέγχθηκε:** `structured-originals/ORIGINAL-5EA5EC73C37B1331.xml`, SHA-256 `5ea5ec73c37b1331d5bd0baa4d867575dd1555ec6916383ae60eda278abc6d83`
- **Canonical πλήρες κείμενο:** `sources/SRC-AC30CEB175.md`, deterministic conversion από JATS χωρίς μετάφραση

## Σκοπός και ερευνητικό ερώτημα

Η εργασία εξετάζει πώς τεχνικές AI μπορούν να ενισχύσουν τη resilience power systems και microgrids πριν, κατά και μετά από disruptive events. Ο στόχος της δεν είναι να μελετήσει τη resilience ενός AI agent ως learning system, αλλά να ανασκοπήσει AI-based τεχνικές που χρησιμοποιούνται για prediction, control, reconfiguration, service restoration και συναφείς λειτουργίες ενός resilience-critical φυσικού συστήματος.

Για τη διπλωματική η αξία της είναι κυρίως **εννοιολογική και μεθοδολογική**. Η διάκριση pre-event / during-event / post-event, η έμφαση στη γρήγορη αποκατάσταση μετά από disruption και η ανάγκη πρακτικής validation προσφέρουν domain-independent αρχές που μπορούν να χρησιμοποιηθούν ως υποστηρικτική τεκμηρίωση για το πώς θα οριστούν phases και measurements του GridWorld experiment. Δεν αποτελεί άμεσο evidence ότι κάποιος συγκεκριμένος RL agent υπερέχει στο δικό μας benchmark.

## Σύνοψη

Οι συγγραφείς παρουσιάζουν τη resilience ως ικανότητα προετοιμασίας και προσαρμογής σε μεταβαλλόμενες συνθήκες, αντίστασης/reconfiguration και ταχείας αποκατάστασης μετά από disruptive events. Η ανασκόπηση οργανώνει εφαρμογές AI σε power systems και microgrids και εξετάζει τη χρήση τους σε διαφορετικές χρονικές φάσεις ενός event.

Η εργασία καλύπτει machine learning, deep learning, probabilistic/statistical approaches, optimization και decision-making methods. Στο resilience-oriented τμήμα εξετάζονται, μεταξύ άλλων, service restoration, fault management, islanding/reconfiguration και operational support. Η service restoration αντιμετωπίζεται ρητά ως post-disruption πρόβλημα στο οποίο ζητείται γρήγορη ανάκτηση παροχής/λειτουργικότητας υπό περιορισμούς.

Το review δεν περιορίζεται στα θετικά αποτελέσματα. Καταγράφει δυσκολίες πραγματικής υιοθέτησης, εξάρτηση από data quantity/quality, τεχνολογική readiness, protection, regulation και ανάγκη πραγματικού experimental validation. Στις future directions προτείνει πλουσιότερα simulation models και synthetic data, αλλά ταυτόχρονα ζητά real-time experimental validation των προτεινόμενων AI techniques.

## Μεθοδολογία

Η review methodology περιγράφεται ρητά στη Section 1.4:

1. **Keyword search:** Google Scholar με όρους γύρω από resilience, power systems, AI models, microgrids, machine learning και deep learning.
2. **Paper screening:** διαχωρισμός review/research papers και ταξινόμηση AI models ανά model/application.
3. **Backward/forward citation search:** πρόσθετα papers από references και papers που cited τις επιλεγμένες εργασίες.
4. **Review:** εξέταση objective, method, event phase, data source/type, performance και compared approaches.
5. **Analysis:** σύγκριση για restoration/reconfiguration approaches, research gaps και future opportunities.

Η χρονική κάλυψη δηλώνεται ως studies από 2016 έως τον χρόνο της ανασκόπησης. Η μεθοδολογία είναι σαφέστερη από ένα narrative review χωρίς documented search process, αλλά δεν παρουσιάζεται ως πλήρες systematic review με PRISMA flow, πλήρη search strings ανά database, explicit exclusion counts ή formal risk-of-bias/quality appraisal.

## Κύρια ευρήματα

1. **Η resilience είναι χρονική διαδικασία με pre-, during- και post-event φάσεις.** Η εργασία οργανώνει την ανάλυση και τις εφαρμογές με βάση τη θέση τους ως προς το event occurrence time. Αυτό υποστηρίζει phase-aware experimental design αντί ενός μόνο aggregate post-hoc score.
2. **Η restoration speed είναι ξεχωριστή διάσταση από τη nominal λειτουργία.** Στη service restoration, ο στόχος είναι ταχεία αποκατάσταση κρίσιμης λειτουργικότητας μετά από major disruption υπό operational constraints.
3. **AI χρησιμοποιείται επειδή τα resilience problems μπορεί να έχουν nonlinearity, uncertainty, coupling και πολλαπλές μεταβλητές.** Αυτό αποτελεί motivation για adaptive/learning-based methods, όχι απόδειξη ότι AI είναι πάντοτε καλύτερο από συμβατικές μεθόδους.
4. **Data quantity και quality είναι άμεσος περιορισμός της αξιοπιστίας των AI models.** Inconsistent/incomplete data μπορεί να υποβαθμίσει την απόδοση και άρα πρέπει να λαμβάνεται υπόψη όταν σχεδιάζεται disturbed observation/data regime.
5. **Simulation και synthetic data είναι χρήσιμα αλλά δεν υποκαθιστούν validation.** Οι συγγραφείς προτείνουν richer simulation models για παραγωγή synthetic data και ταυτόχρονα επισημαίνουν την ανάγκη real-time experimental investigation.
6. **Η υιοθέτηση AI σε resilience-critical συστήματα έχει operational και governance constraints.** Technology readiness, protection, infrastructure, regulation και accountability περιορίζουν το πώς γενικεύονται αποτελέσματα από controlled experiments.

## Υποθέσεις και ορισμοί

Η εργασία χρησιμοποιεί domain-specific power-system resilience. Η γενική ιδέα περιλαμβάνει preparation/adaptation, resistance/reconfiguration και rapid restoration, αλλά οι concrete objectives είναι power supply, critical loads, topology, voltage/current constraints και άλλα ηλεκτρικά μεγέθη.

Στη διπλωματική δεν θα μεταφερθούν αυτούσια αυτά τα domain-specific μεγέθη. Θα χρησιμοποιηθεί μόνο η γενική χρονική λογική: nominal phase → disruption → degradation → adaptation/recovery → stabilized post-change behavior.

## Περιορισμοί και απειλές εγκυρότητας

- **Domain specificity:** microgrids και electric power systems διαφέρουν ουσιαστικά από single-agent GridWorld RL. Η πηγή δεν αποδεικνύει μεταφορά συγκεκριμένων AI techniques στο thesis benchmark.
- **Review completeness:** η αναζήτηση βασίζεται κυρίως σε Google Scholar και citation chaining και δεν παρέχεται πλήρες reproducible systematic-review protocol.
- **Heterogeneous evidence:** οι reviewed studies έχουν διαφορετικά systems, objectives, datasets και performance measures. Δεν δικαιολογείται άμεσο cross-paper algorithm ranking.
- **Real-world gap:** μεγάλο μέρος του literature βασίζεται σε simulations/controlled studies, ενώ η ίδια η εργασία ζητά μεγαλύτερη practical/real-time validation.
- **Broad AI terminology:** ο όρος AI καλύπτει πολύ διαφορετικές τεχνικές, από optimization έως deep learning. Δεν πρέπει να χρησιμοποιηθεί η ανασκόπηση για να αιτιολογήσει από μόνη της συγκεκριμένο agent family.
- **Potential publication/search bias:** δεν περιγράφεται formal quality appraisal ή publication-bias analysis.

## Σχέση με τη διπλωματική

Η πηγή είναι χρήσιμη για:

- θεωρητικό υπόβαθρο της resilience ως process γύρω από disruptive events,
- διάκριση pre-event / during-event / post-event,
- αιτιολόγηση ξεχωριστής μέτρησης degradation και recovery,
- discussion της σχέσης uncertainty/data quality με adaptive AI behavior,
- αιτιολόγηση controlled simulation ως πειραματικού εργαλείου μαζί με ρητή αναγνώριση external-validity limits,
- threats-to-validity section σχετικά με real-world adoption και generalization.

Δεν πρέπει να χρησιμοποιηθεί ως direct evidence για:

- επιλογή συγκεκριμένου RL algorithm,
- υπεροχή deep RL έναντι tabular methods,
- ακριβές recovery metric ή threshold,
- direct transfer από microgrid restoration σε GridWorld adaptation.

## Απόφαση

- **Ρόλος:** υποστηρικτική
- **Απόφαση:** επιλογή και εξαγωγή.
- **Κεφάλαια:** Θεωρητικό υπόβαθρο; Σχετικές εργασίες; Μεθοδολογία; Μετρικές; Threats to validity
- **Θέματα:** resilience lifecycle; disruption phases; recovery; service restoration; uncertainty; simulation validation
- **Αιτιολόγηση:** peer-reviewed review με σαφή phase-aware framing και άμεσα χρήσιμες παρατηρήσεις για recovery και validation. Η εφαρμογή είναι domain-specific, επομένως χρησιμοποιείται υποστηρικτικά και όχι ως κύρια evidence πηγή για agent/algorithm selection.
