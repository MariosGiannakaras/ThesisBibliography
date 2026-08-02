# SRC-5E062C81BA — Robust Reinforcement Learning

## Βιβλιογραφική ταυτότητα

- **Συγγραφείς:** Jun Morimoto, Kenji Doya
- **Έκδοση:** NeurIPS 2000
- **Τύπος:** primary robust RL / control-theoretic method
- **Ρόλος στη διπλωματική:** υποστηρικτική ιστορική primary source

## Αντικείμενο

Η εργασία εισάγει robust RL που μεταφέρει ιδέες από H∞ control σε actor–disturber–critic learning. Ένας control agent προσπαθεί να επιλέξει την καλύτερη action ενώ ένας disturber αναπαριστά worst-case input/model disturbance.

Η robust objective διατυπώνεται ως min–max value problem ώστε η learned policy να είναι λιγότερο ευαίσθητη σε modeling errors και disturbances.

## Κύρια αποτελέσματα

- Παράγεται online learning formulation για value function, control και worst disturbance.
- Στο linear pendulum setting οι learned quantities συμφωνούν με analytic H∞ solution.
- Σε nonlinear swing-up, robust policy ανέχεται αλλαγές σε pendulum mass και friction καλύτερα από τον nominal model-based RL comparator της εργασίας.
- Το robustness αποκτάται κατά training μέσω worst-disturbance objective, όχι μέσω explicit post-change detector.

## Συνάφεια

Η εργασία είναι χρήσιμο historical primary evidence ότι “environmental change” μπορεί να αντιμετωπιστεί με **pre-trained worst-case robustness** αντί με **continued adaptation**.

Στο thesis protocol αυτό αποτελεί διαφορετικό agent class από continual/reset/context-recall agents. Η robust policy μπορεί να αντέξει αλλαγές χωρίς να ενημερώσει parameters μετά το change.

## Πρωτόκολλο που προκύπτει

Για robust-disturbance methods καταγράφονται:

- disturbance model/class,
- robustness parameter,
- whether disturbances were seen/generated during training,
- nominal training performance,
- zero-update performance μετά από parameter shift,
- performance με continued learning ενεργό/ανενεργό,
- clean-performance cost της robustness objective.

Κρίσιμη διάκριση:

- **zero-update robustness** = performance immediately after shift με frozen parameters,
- **adaptation** = improvement due to parameter updates after shift.

## Περιορισμοί

- Continuous-control/H∞ formulation, όχι tabular GridWorld.
- Worst-case disturber αντιστοιχεί σε συγκεκριμένη disturbance class.
- Το experiment με αλλαγή mass/friction δεν είναι repeated unknown-changepoint benchmark.
- Η καλύτερη disturbed performance δεν αποδεικνύει ταχύτερη relearning.

## Απόφαση

**Επιλογή ως υποστηρικτική ιστορική primary source.** Χρησιμοποιείται για το experimental requirement να αποσυντίθεται η άμεση zero-update robustness από τη μετέπειτα online adaptation.