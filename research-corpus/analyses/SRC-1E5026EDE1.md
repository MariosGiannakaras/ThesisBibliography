---
κωδικός: SRC-1E5026EDE1
κατάσταση: απόρριψη
έκδοση-που-ελέγχθηκε: "NeurIPS 2018, Learning safe policies with expert guidance"
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---
# Επιστημονική ανάλυση — SRC-1E5026EDE1

## Αντικείμενο
Primary NeurIPS εργασία για reward misspecification. Χρησιμοποιεί expert demonstrations για να ορίσει σύνολο reward functions συμβατών με την υπάρχουσα γνώση και βρίσκει max-min policy που είναι robust ως προς αυτό το reward set, ακόμη και όταν training/test MDPs διαφέρουν αλλά μοιράζονται feature space.

## Αξία
Η εργασία είναι υψηλής ποιότητας και ξεχωρίζει robust reward uncertainty από transition uncertainty. Ωστόσο απαιτεί expert demonstrations/known feature mapping και αντιμετωπίζει misspecified/unknown reward, όχι online external reward changepoints ή continued adaptation.

## Redundancy για τη διπλωματική
Τα boundaries reward hacking/misspecification έναντι external reward shift καλύπτονται ήδη από `SRC-8396F66954`, ενώ prior-guidance/capability accounting καλύπτεται από selected safe-transfer/shield sources. Η πλήρης max-min reward-learning μέθοδος δεν είναι feasible/core comparator.

## Απόφαση
**Απόρριψη ως υψηλής ποιότητας αλλά redundant/out-of-scope reward-misspecification source.** Δεν χρησιμοποιείται για να τεκμηριώσει recovery μετά από reward change.