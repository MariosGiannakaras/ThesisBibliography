# SRC-CE71F210EE — Simple and Principled Uncertainty Estimation with Deterministic Deep Learning via Distance Awareness

## Απόφαση

**Απόρριψη από το core export λόγω supervised/neural scope και redundancy.**

Η εργασία προτείνει SNGP για distance-aware predictive uncertainty σε vision/NLP classification. Είναι υψηλής ποιότητας primary source, αλλά δεν μελετά sequential RL, environmental changepoints ή post-change recovery.

Οι χρήσιμες έννοιες neural epistemic uncertainty, OOD awareness και calibration καλύπτονται ήδη από `SRC-7C18826BEE`, `SRC-A6616BE773` και `SRC-70AEC665B2`. Η εισαγωγή SNGP θα πρόσθετε νέο neural architecture χωρίς άμεση ανάγκη στο tabular core.

Διατηρείται ως πιθανή μελλοντική neural-detector reference, χωρίς εξαγωγή.