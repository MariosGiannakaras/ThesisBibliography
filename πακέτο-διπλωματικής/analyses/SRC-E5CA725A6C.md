---
κωδικός: SRC-E5CA725A6C
κατάσταση: επαληθευμένη
έκδοση-που-ελέγχθηκε: "PhD thesis, University of Technology Sydney, October 2024"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Deep Reinforcement Learning in Non-stationary Environments

## Βιβλιογραφική ταυτότητα
Zihe Liu. *Deep Reinforcement Learning in Non-stationary Environments*. Doctor of Philosophy in Computer Science, Australian Artificial Intelligence Institute, University of Technology Sydney, 2024. Supervisors: Jie Lu, Guangquan Zhang, Junyu Xuan.

Η διατριβή ενσωματώνει, μεταξύ άλλων, peer-reviewed αποτελέσματα των Liu et al. για DRL με unknown change points, συμπεριλαμβανομένου άρθρου στο IEEE Transactions on Cybernetics (DOI 10.1109/TCYB.2024.3356981) και εργασίας IJCAI 2024 για behavior-aware adaptation.

## Σκοπός και ερευνητικό ερώτημα
Η εργασία αντιμετωπίζει άμεσα το πρόβλημα που βρίσκεται στον πυρήνα της παρούσας διπλωματικής: ένας RL agent δρα σε ακολουθία περιβαλλόντων/MDPs που αλλάζουν σε άγνωστες χρονικές στιγμές και πρέπει όχι μόνο να συνεχίζει να μαθαίνει αλλά να **ανιχνεύει** την αλλαγή και να **προσαρμόζει** την πολιτική του με τρόπο που αξιοποιεί χρήσιμη προηγούμενη γνώση χωρίς να εγκλωβίζεται σε αρνητική μεταφορά.

Η διατριβή διατυπώνει χωριστά το ευκολότερο πρόβλημα γνωστών change points και το πρακτικότερο πρόβλημα άγνωστων change points. Στο δεύτερο, οι πραγματικές χρονικές στιγμές αλλαγής δεν δίνονται στον agent· ο agent παράγει δικά του detected change points που μπορεί να καθυστερούν, να λείπουν ή να είναι λανθασμένα.

## Μεθοδολογία
Η διατριβή αναπτύσσει τόσο model-free όσο και model-based detection/adaptation schemes. Δύο ιδιαίτερα χρήσιμες γραμμές για την παρούσα διπλωματική είναι οι DARL και FDA.

### 1. DARL — Detection-Adaptation Reinforcement Learning
Το DARL είναι model-free end-to-end πλαίσιο με δύο διακριτά υποσυστήματα:

1. **Environment change detection**
   - αντιμετωπίζει τα observed state-action pairs ως samples από την joint distribution `P(s,a)=P(s)P(a|s)`,
   - εξετάζει μεταβολή της state marginal `P(s)` με distributional test/MMD,
   - εξετάζει μεταβολή της conditional `P(a|s)`/policy μέσω distance των διαδοχικών policy networks,
   - αποφασίζει αλλαγή όταν οι ενδείξεις συμφωνούν σε μικρό χρονικό διάστημα.

2. **Policy adaptation**
   - χρησιμοποιεί gradient information από παλαιότερες policies,
   - δεν επιβάλλει ισότιμη διατήρηση όλων των προηγούμενων policies,
   - χαλαρώνει/σταθμίζει τη μεταφορά ανάλογα με την απόσταση από το νέο regime ώστε να περιορίζει negative transfer από «bad» ή άσχετες προηγούμενες policies.

Η διάκριση είναι ιδιαίτερα σημαντική: το detector αποφασίζει **αν/πότε** άλλαξε το περιβάλλον, ενώ ο adapter αποφασίζει **πώς** θα τροποποιηθεί η policy μετά την ένδειξη αλλαγής.

### 2. FDA — Functional Detection and Adaptation
Το FDA μεταφέρει το detection/adaptation reasoning σε functional/Bayesian representation:

- χρησιμοποιεί Wasserstein-type functional surprise μεταξύ διαδοχικών policy representations,
- εφαρμόζει Welch's t-test και significance level `α` για change decision,
- προσαρμόζει τη δύναμη preservation της προηγούμενης γνώσης ανάλογα με το estimated change magnitude,
- κρατά περιορισμένη representative memory αντί όλου του ιστορικού,
- επιλέγει representative trajectories με συνδυασμό proximity σε decision boundaries και cumulative reward,
- χρησιμοποιεί functional regularization ώστε παρόμοια regimes να διατηρούν περισσότερη προηγούμενη γνώση και μεγαλύτερες αλλαγές να επιτρέπουν μεγαλύτερη plasticity.

Αυτή η γραμμή παρέχει άμεσο θεωρητικό rationale για **recency/forgetting**, **selective memory** και **change-magnitude-aware adaptation** χωρίς να υποχρεώνει την παρούσα εργασία να υλοποιήσει βαριά Gaussian-process/deep functional machinery.

## Experimental design
### DARL
Η αξιολόγηση περιλαμβάνει CartPole, LunarLander, MiniGrid και VizDoom με πολλαπλές πραγματικές αλλαγές μέσα στην ίδια learning process. Ενδεικτικά schedules που δηλώνονται στη διατριβή:

- CartPole: αλλαγές στα episodes 500 και 1000,
- LunarLander: 500 και 1000,
- MiniGrid: 15,000 και 30,000,
- VizDoom: 2,500 και 5,000.

Ο agent δεν λαμβάνει το πραγματικό change point ως input στο unknown-change-point setting.

Comparators περιλαμβάνουν standard PPO/retraining, ODCP, CRL-Unsup, GEM και, σε adaptation ablations, PCGrad/CAGrad και άλλους gradient-transfer comparators.

### FDA
Η διατριβή δημιουργεί VizDoom shifts όπως:

- `simpler_basic → basic` και αλλαγή φωτισμού,
- `defend_the_line → defend_the_center` και έπειτα χαμηλότερος φωτισμός,
- `deadly_corridor` με μεταβολή αριθμού εχθρών 6→5→4.

Οι αλλαγές έχουν δύο change points ανά scenario και ούτε η χρονική στιγμή ούτε ο τύπος αλλαγής δίνονται στον agent.

## Κύρια ευρήματα
### Detection accuracy και detection delay είναι διαφορετικές μεταβλητές
Στο DARL, η διατριβή αναφέρει F1 για ODCP / CRL-Unsup / DARL αντίστοιχα:

- CartPole: 0.67 / 1.0 / 1.0,
- LunarLander: 0.5 / 0.67 / 0.8,
- MiniGrid: 0.4 / 1.0 / 1.0,
- VizDoom: 0.4 / 1.0 / 1.0.

Όμως, για πραγματικά change points `{500,1000}`, τα παραδείγματα detected points δείχνουν ότι υψηλότερο F1 δεν σημαίνει μικρότερο delay. Στο CartPole, CRL-Unsup αναφέρεται ότι ανίχνευσε `{502,1003}`, ενώ DARL `{508,1021}`· στο LunarLander `{504,1017}` έναντι `{515,1022}`. Άρα precision/recall/F1 και detection delay πρέπει να αναφέρονται **χωριστά**.

### Joint detector αντί ενός μόνο signal
Η ablation δείχνει ότι policy-change signal και episodic/state-distribution signal μεμονωμένα έχουν χαμηλότερη fidelity από τη συνδυαστική απόφαση. Αυτό υποστηρίζει το thesis protocol να μην θεωρεί ένα μόνο reward drop, TD error ή uncertainty spike επαρκές detector χωρίς calibration.

### Negative transfer
Η διατριβή εισάγει προηγούμενη «bad» policy και δείχνει ότι αυστηρά gradient-preservation schemes μπορούν να υποστούν αρνητική μεταφορά καθώς αυξάνονται τα regimes. Το DARL σχεδιάζεται ώστε να χαλαρώνει την επίδραση άσχετων προηγούμενων policies.

Αυτό ενισχύει την απαίτηση της παρούσας διπλωματικής για:
- no-transfer/scratch comparator,
- μέτρηση negative-transfer gap,
- διάκριση retention από χρήσιμη transfer.

### False alarms και missed changes έχουν διαφορετικό κόστος
Η διατριβή αναλύει ότι ένα false positive detection μπορεί να προκαλέσει μικρή προσωρινή πτώση reward λόγω περιττής adaptation και έπειτα recovery, ενώ ένα missed change μπορεί να επιβραδύνει adaptation επειδή λείπει σχετική constraint/knowledge-selection ενημέρωση.

Άρα δεν αρκεί binary detector accuracy· απαιτούνται:
- false-alarm rate,
- missed-change rate,
- delay,
- utility cost ανά false alarm,
- recovery cost μετά από missed/late detection.

### FDA και calibration window
Στα FDA experiments, ένα detection θεωρείται σωστό εάν συμβεί εντός 5 epochs από το πραγματικό change point. Η tolerance window αυτή αλλάζει άμεσα precision/recall/F1 και πρέπει να δηλώνεται ως protocol parameter.

Η διατριβή αναφέρει μέσο F1 σε 10 seeds για FDA μεγαλύτερο από τους συγκεκριμένους comparators στα τρία VizDoom scenarios που εξετάζονται, αλλά οι αριθμοί δεν πρέπει να γενικευθούν πέρα από το συγκεκριμένο benchmark και tolerance definition.

## Κρίσιμες υποθέσεις
1. Στο βασικό DARL formulation θεωρείται ίδιο state/action dimensionality μεταξύ regimes.
2. Υποτίθεται ότι υπάρχει αρκετός χρόνος/αρκετά episodes σε κάθε regime ώστε η policy να συγκλίνει πριν από την επόμενη αλλαγή.
3. Η εργασία είναι κυρίως deep-RL και αρκετές adaptation τεχνικές είναι computationally βαρύτερες από το resource-aware tabular benchmark της παρούσας διπλωματικής.
4. Οι change schedules είναι controlled synthetic/non-stationary benchmarks· δεν αποδεικνύεται πλήρης real-world universality.
5. Οι detector thresholds/tests και η definition του allowable detection window επηρεάζουν τα reported detection metrics.

## Περιορισμοί και απειλές εγκυρότητας
- Η υπόθεση convergence-before-next-change μειώνει την εξωτερική εγκυρότητα για πολύ γρήγορο drift ή high-frequency switching.
- F1 εξαρτάται από το tolerance window γύρω από το πραγματικό change point.
- Το deep policy-network distance δεν μεταφέρεται αυτούσιο σε tabular Q-learning.
- FDA έχει μη αμελητέο compute/memory overhead από functional/GP operations.
- Η PhD συνθέτει πολλαπλές μεθόδους και papers· για claims που υπάρχουν ως χωριστές journal/conference publications πρέπει αργότερα να προτιμηθεί η αντίστοιχη primary publication εάν προστεθεί στο corpus.

## Σχέση με την παρούσα διπλωματική
Η πηγή είναι **άμεση κύρια τεκμηρίωση** για τον experimental protocol και όχι απλώς background.

### Protocol decisions που προκύπτουν
1. Detector και adapter αξιολογούνται χωριστά.
2. Για detector report:
   - precision,
   - recall,
   - F1,
   - detection delay,
   - false alarms,
   - misses,
   - tolerance window.
3. Για adapter report:
   - post-change return curve,
   - initial degradation,
   - time/interactions-to-recovery,
   - area-under-recovery curve,
   - final asymptotic return,
   - negative-transfer gap.
4. False alarms πρέπει να έχουν μετρήσιμο adaptation cost.
5. No-transfer/full-reset comparator είναι απαραίτητος.
6. Change magnitude πρέπει να καταγράφεται επειδή μπορεί να αλλάζει το σωστό retention/plasticity trade-off.
7. Repeated-change experiments πρέπει να αναφέρουν ανά occurrence metrics, όχι μόνο aggregate final return.
8. Για fast-switching regimes πρέπει να υπάρχει ξεχωριστό stress test που παραβιάζει την convergence-before-next-change assumption.

## Χρήση στη διπλωματική
**Κύρια πηγή.** Χρησιμοποιείται για:
- formal unknown-changepoint framing,
- detector/adapter architecture,
- detection metrics και delay,
- false-alarm/miss consequences,
- negative transfer από προηγούμενα regimes,
- adaptation-vs-retraining comparison,
- change-magnitude-aware knowledge retention,
- bounded representative memory,
- justification για repeated non-stationary GridWorld experiments.

Δεν απαιτείται να υλοποιηθεί DARL ή FDA πλήρως. Η βασική αξία τους είναι να τεκμηριώσουν τι πρέπει να μετρηθεί και ποιες πληροφοριακές/υπολογιστικές παραδοχές πρέπει να δηλώνονται.

## Κατάσταση επαλήθευσης
Ελέγχθηκε το πλήρες converted PhD thesis. Επιλέγεται ως **κύρια** πηγή και παράγονται citation-ready excerpts.