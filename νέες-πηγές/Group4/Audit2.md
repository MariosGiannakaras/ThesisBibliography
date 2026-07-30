Θεματικός Άξονας 1: Θεμελιώδη Συγγράμματα & Επισκοπήσεις (Foundations & Surveys)
Αυτές οι αναφορές αποτελούν το απαραίτητο θεωρητικό υπόβαθρο για την κατανόηση της Ενισχυτικής Μάθησης (RL) και της μεταφοράς γνώσης (transfer learning).
1. Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (MIT Press)

    Πού αναφέρεται στις πηγές σας: Αποτελεί την κορυφαία αναφορά και αναφέρεται σχεδόν σε όλες τις πηγές σας.
    Γιατί είναι απαραίτητη: Είναι το βασικό εγχειρίδιο αναφοράς ("βίβλος") του RL. Ορίζει με μαθηματική ακρίβεια τις Μαρκοβιανές Διαδικασίες Απόφασης (MDPs), τις μεθόδους χρονικών διαφορών (Temporal Differences - TD) και τις θεμελιώδεις έννοιες της εξερεύνησης έναντι της εκμετάλλευσης (exploration-exploitation dilemma).

2. Taylor, M. E., & Stone, P. (2009). «Transfer learning for reinforcement learning domains: A survey» (Journal of Machine Learning Research)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch (2024).
    Γιατί είναι απαραίτητη: Παρέχει την πληρέστερη επισκόπηση του πώς ένας πράκτορας μπορεί να μεταφέρει τη γνώση από ένα περιβάλλον-πηγή (source domain) σε ένα περιβάλλον-στόχο (target domain). Αυτό είναι κρίσιμο για το GridWorld σας όταν αλλάζουν οι συνθήκες.

3. Zhu, Z., Lin, K., & Zhou, J. (2021). «Transfer learning in deep reinforcement learning: A survey» (IEEE Transactions on Pattern Analysis and Machine Intelligence)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του NovGrid και στη διατριβή του Balloch (καθώς και στην έκδοση του 2023).
    Γιατί είναι απαραίτητη: Εστιάζει στη μεταφορά γνώσης αποκλειστικά στο πλαίσιο της Βαθιάς Ενισχυτικής Μάθησης (Deep RL), αναλύοντας τεχνικές όπως η μεταφορά αναπαραστάσεων (representation transfer) και η προ-εκπαίδευση πολιτικής (policy pre-training).

4. Liang, J., He, R., & Tan, T. (2023). «A comprehensive survey on test-time adaptation under distribution shifts» (arXiv preprint)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch (2024).
    Γιατί είναι απαραίτητη: Εξετάζει τη δυναμική προσαρμογή κατά τον χρόνο δοκιμής (test-time adaptation) όταν υπάρχει μετατόπιση κατανομής (distribution shift). Σας βοηθά να στηρίξετε θεωρητικά το πώς ο πράκτοράς σας προσαρμόζεται online στο GridWorld χωρίς να ξαναεκπαιδευτεί από την αρχή.

5. Williams, R. J. (1992). «Simple statistical gradient-following algorithms for connectionist reinforcement learning» (Machine Learning)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch, στο άρθρο της SA-PPO, στη διατριβή του Χουτουρίδη και στη διατριβή του Zihe Liu.
    Γιατί είναι απαραίτητη: Είναι η ιστορική εργασία που εισήγαγε τον αλγόριθμο REINFORCE. Θεμελιώνει μαθηματικά τις μεθόδους κλίσης πολιτικής (policy gradient methods) πάνω στις οποίες βασίζεται ο PPO και ο A2C.

Θεματικός Άξονας 2: Ανθεκτικότητα, Αβεβαιότητα & Robust MDPs
Αυτές οι αναφορές επικεντρώνονται στο κεντρικό θέμα της διατριβής σας: την ανθεκτικότητα των πρακτόρων (robustness) απέναντι στην αβεβαιότητα των μεταβάσεων του περιβάλλοντος.
6. Bagnell, J. A., Ng, A. Y., & Schneider, J. G. (2001). «Solving uncertain markov decision processes» (Citeseer)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του PAIRED (Dennis et al., 2020) και στη διατριβή του Balloch (ως Bagnell et al., 2001).
    Γιατί είναι απαραίτητη: Από τις πρώτες ιστορικές εργασίες που εισάγουν την έννοια των Uncertain MDPs. Αναλύει πώς μπορούμε να εγγυηθούμε τη λήψη αποφάσεων όταν οι πιθανότητες μετάβασης του περιβάλλοντος δεν είναι πλήρως γνωστές.

7. Morimoto, J., & Doya, K. (2001). «Robust reinforcement learning» (Neural Computation / NeurIPS)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του PAIRED και στη διατριβή του Zihe Liu (ως Morimoto & Doya, 2000).
    Γιατί είναι απαραίτητη: Εισάγει επίσημα τον όρο Robust Reinforcement Learning. Χρησιμοποιεί τη θεωρία παιγνίων (game theory) και τη διατύπωση minimax (minimax formulation), όπου ο πράκτορας εκπαιδεύεται να αντιμετωπίζει έναν "αντίπαλο" (adversary) που εισάγει διαταραχές στο περιβάλλον, καθιστώντας τον πράκτορα εξαιρετικά ανθεκτικό.

8. Nilim, A., & El Ghaoui, L. (2005). «Robust control of markov decision processes with uncertain transition matrices» (Operations Research)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του PAIRED, της Action Robust RL και στη διατριβή του Balloch (ως Nilim & El Ghaoui, 2004).
    Γιατί είναι απαραίτητη: Θεμελιώνει μαθηματικά τη στιβαρή βελτιστοποίηση (robust dynamic programming) με τη χρήση συνόλων αβεβαιότητας (uncertainty sets) για τις μήτρες μετάβασης. Είναι η πιο κλασική αναφορά για Robust MDPs.

9. Lecarpentier, E., & Rachelson, E. (2019). «Non-stationary markov decision processes, a worst-case approach using model-based reinforcement learning» (NeurIPS)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch και στη διατριβή του Zihe Liu (ως Lecarpentier & Rachelson, 2019).
    Γιατί είναι απαραίτητη: Μελετά το πρόβλημα των μη-σταθερών MDPs υπό τη σκοπιά της χειρότερης περίπτωσης (worst-case approach). Σχετίζεται άμεσα με τον GridWorld σας όταν οι κανόνες του περιβάλλοντος αλλάζουν απρόβλεπτα.

10. Wang, Y., & Zou, S. (2021). «Online Robust Reinforcement Learning with Model Uncertainty» (NeurIPS)

    Πού αναφέρεται στις πηγές σας: Είναι η ίδια η πηγή 4 του Notebook σας και αναφέρεται στο Audit Report.
    Γιατί είναι απαραίτητη: Αναπτύσσει θεωρητικά και πειραματικά (σε tabular GridWorld περιβάλλοντα) robust Q-learning αλγορίθμους που διαχειρίζονται την αβεβαιότητα μοντέλου online και incremental.

Θεματικός Άξονας 3: Unsupervised Environment Design (UED) & GridWorld Benchmarks
Αυτές οι αναφορές είναι κρίσιμες για την υλοποίηση των πειραμάτων σας, καθώς το GridWorld αποτελεί το κατεξοχήν περιβάλλον δοκιμής αυτών των αλγορίθμων.
11. Chevalier-Boisvert, M., Willems, L., & Pal, S. (2018). «Minimalistic gridworld environment for openai gym» (GitHub - gym-minigrid)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch, στη διατριβή του Zihe Liu, στο PAIRED, στο NovGrid και στη διατριβή του CARL.
    Γιατί είναι απαραίτητη: Είναι η επίσημη βιβλιοθήκη του MiniGrid. Καθώς η εργασία σας θα υλοποιηθεί σε GridWorld, αυτή η αναφορά είναι η τεχνική βάση του περιβάλλοντος προσομοίωσής σας.

12. Dennis, M., et al. (2020). «Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design» (NeurIPS - PAIRED)

    Πού αναφέρεται στις πηγές σας: Είναι η πηγή 3 του Notebook σας και αναφέρεται εκτενώς στο Audit Report.
    Γιατί είναι απαραίτητη: Εισάγει το πλαίσιο του Unsupervised Environment Design (UED) και τον αλγόριθμο PAIRED. Εκπαιδεύει έναν adversarial GridWorld generator που δημιουργεί curricula (λαβυρίνθους) με στόχο τη μεγιστοποίηση του "regret" των πρακτόρων, παράγοντας εξαιρετικά ανθεκτικούς πράκτορες.

13. Wang, R., Lehman, J., Clune, J., & Stanley, K. O. (2019). «Paired open-ended trailblazer (POET): Endlessly generating increasingly complex and diverse learning environments and their solutions» (arXiv preprint)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του PAIRED και στο Audit Report.
    Γιατί είναι απαραίτητη: Εισάγει τον αλγόριθμο POET, ο οποίος πρωτοστάτησε στην αυτόματη παραγωγή περιβαλλόντων και curricula για την εκπαίδευση ανθεκτικών πολιτικών.

14. Wang, R., et al. (2020). «Enhanced POET: Open-ended reinforcement learning through unbounded invention of learning challenges and their solutions» (arXiv preprint)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του PAIRED και στο Audit Report.
    Γιατί είναι απαραίτητη: Η εξελιγμένη έκδοση του POET που εισάγει μεταφορές γνώσης σε περιβάλλοντα με αυξανόμενη πολυπλοκότητα.

Θεματικός Άξονας 4: Μη-Σταθερότητα & Ανίχνευση Αλλαγών (Non-Stationary RL & Change Detection)
Όταν ένας πράκτορας λειτουργεί υπό αβεβαιότητα, πρέπει να είναι σε θέση να ανιχνεύσει πότε το περιβάλλον αλλάζει (concept drift) και να προσαρμόσει την πολιτική του.
15. Adams, R. P., & MacKay, D. J. (2007). «Bayesian online changepoint detection» (arXiv preprint)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία της διατριβής του Zihe Liu (ως Adams & MacKay, 2007).
    Γιατί είναι απαραίτητη: Ο κλασικότερος αλγόριθμος για την online ανίχνευση σημείων αλλαγής (BOCPD). Στη διατριβή του Zihe Liu χρησιμοποιείται για να καταλάβει ο πράκτορας πότε άλλαξε το GridWorld.

16. Alegre, L. N., Bazzan, A. L., & da Silva, B. C. (2021). «Minimum-delay adaptation in non-stationary reinforcement learning via online high-confidence change-point detection» (AAMAS)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Zihe Liu και στη βιβλιογραφία του Alami (2023).
    Γιατί είναι απαραίτητη: Προτείνει έναν αλγόριθμο ανίχνευσης αλλαγών με εγγυήσεις υψηλής εμπιστοσύνης (high-confidence), επιτρέποντας στον πράκτορα να προσαρμόζεται με την ελάχιστη δυνατή καθυστέρηση (minimum delay).

17. Lopez-Paz, D., & Ranzato, M. (2017). «Gradient episodic memory for continual learning» (NeurIPS - GEM)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία της διατριβής του Zihe Liu (ως Lopez-Paz & Ranzato, 2017) και στην ανάλυση του DARL.
    Γιατί είναι απαραίτητη: Εισάγει τον αλγόριθμο Gradient Episodic Memory (GEM). Ο GEM χρησιμοποιεί ιστορικές κλίσεις (gradients) για να περιορίσει τις ενημερώσεις της τρέχουσας πολιτικής, εμποδίζοντας την καταστροφική λήθη (catastrophic forgetting) όταν ο πράκτορας αλλάζει περιβάλλον.

18. Kaplanis, C., Shanahan, M., and Clopath, C. (2019). «Policy consolidation for continual reinforcement learning» (arXiv preprint)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Zihe Liu (ως Kaplanis et al., 2019) και στις συγκρίσεις του DARL.
    Γιατί είναι απαραίτητη: Προτείνει τη μέθοδο Policy Consolidation (PC), η οποία σταθεροποιεί τις πολιτικές του πράκτορα σε πολλαπλά χρονικά επίπεδα, επιτρέποντας συνεχή μάθηση (continual learning) χωρίς απώλεια προηγούμενης γνώσης.

19. Da Silva, B. C., Basso, E. W., Bazzan, A. L., & Engel, P. M. (2006). «Dealing with non-stationary environments using context detection» (ICML)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη βιβλιογραφία του Alami και στη βιβλιογραφία του Zihe Liu.
    Γιατί είναι απαραίτητη: Θεμελιώδες άρθρο για τη διαχείριση μη-σταθερών περιβαλλόντων μέσω της μοντελοποίησης και ανίχνευσης "πλαισίων" (contexts).

Θεματικός Άξονας 5: Αλγόριθμοι Ενισχυτικής Μάθησης & Intrinsic Exploration
Αυτές οι πηγές καλύπτουν τους αλγορίθμους που θα συγκρίνετε (PPO, A2C) και τις μεθόδους εξερεύνησης που καθορίζουν την ανθεκτικότητά τους.
20. Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). «Proximal policy optimization algorithms» (arXiv preprint - PPO)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch, στη διατριβή του Zihe Liu, στη διατριβή του Χουτουρίδη και στη βιβλιογραφία του PAIRED.
    Γιατί είναι απαραίτητη: Εισάγει τον αλγόριθμο PPO, ο οποίος χρησιμοποιεί το clipped surrogate objective για να εξασφαλίσει εξαιρετική σταθερότητα εκπαίδευσης. Θα είναι ο βασικός αλγόριθμος σύγκρισής σας.

21. Schulman, J., Moritz, P., Levine, S., Jordan, M., & Abbeel, P. (2016). «High-dimensional continuous control using generalized advantage estimation» (ICLR - GAE)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Χουτουρίδη, στη διατριβή του Zihe Liu και στη διατριβή του Balloch (ως Schulman et al., 2015/2016).
    Γιατί είναι απαραίτητη: Εισάγει τον εκτιμητή GAE (Generalized Advantage Estimation). Είναι κρίσιμος για τη μείωση της διακύμανσης των δειγμάτων (variance reduction), σταθεροποιώντας την εκπαίδευση του PPO και του A2C.

22. Mnih, V., et al. (2016). «Asynchronous methods for deep reinforcement learning» (ICML - A3C/A2C)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch, στη διατριβή του Zihe Liu, στη διατριβή του Χουτουρίδη και στο άρθρο της SA-PPO.
    Γιατί είναι απαραίτητη: Παρουσιάζει την οικογένεια αλγορίθμων Actor-Critic (A3C και ο συγχρονισμένος A2C). Αποτελεί τον δεύτερο βασικό άξονα της σύγκρισης στην εργασία σας.

23. Burda, Y., Edwards, H., Storkey, A., & Klimov, O. (2018). «Exploration by random network distillation» (ICLR - RND)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch και στο Audit Report.
    Γιατί είναι απαραίτητη: Εισάγει τη μέθοδο εξερεύνησης RND. Χρησιμοποιεί την αποτυχία πρόβλεψης ενός δικτύου-στόχου (target network) ως εγγενή ανταμοιβή (intrinsic reward), επιτρέποντας στον πράκτορα να εξερευνά άγνωστες καταστάσεις.

24. Pathak, D., Agrawal, P., Efros, A. A., & Darrell, T. (2017). «Curiosity-driven exploration by self-supervised prediction» (ICML - ICM)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch (ως Pathak et al., 2017) και στο Audit Report.
    Γιατί είναι απαραίτητη: Εισάγει το Intrinsic Curiosity Module (ICM). Ορίζει την "περιέργεια" (curiosity) με βάση το σφάλμα πρόβλεψης των δυναμικών του περιβάλλοντος, βοηθώντας τον πράκτορα να ανιχνεύει αλλαγές.

25. Eysenbach, B., Gupta, A., Ibarz, J., & Levine, S. (2019). «Diversity is all you need: Learning skills without a reward function» (ICLR - DIAYN)

    Πού αναφέρεται στις πηγές σας: Αναφέρεται στη διατριβή του Balloch, στη διατριβή του Zihe Liu (ως Eysenbach et al., 2018) και στη βιβλιογραφία του PAIRED.
    Γιατί είναι απαραίτητη: Εισάγει τον αλγόριθμο DIAYN. Εκπαιδεύει τον πράκτορα να αναπτύσσει διαφορετικές δεξιότητες (skills) χωρίς εξωτερική ανταμοιβή, μεγιστοποιώντας την κάλυψη του χώρου καταστάσεων (state space coverage), γεγονός που αυξάνει δραματικά την ανθεκτικότητα.