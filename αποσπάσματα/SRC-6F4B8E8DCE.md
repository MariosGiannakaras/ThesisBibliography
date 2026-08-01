---
κωδικός: SRC-6F4B8E8DCE
κατάσταση: επαληθευμένο
ελεγχθέν-πρωτότυπο: ναι
ημερομηνία-ελέγχου: "2026-08-01"
---

# Τεκμήρια

## 1. Safety formulation πρέπει να δηλώνεται
- Τύπος: πιστή παράφραση
- Θέση: Sections 2–3
- Ισχυρισμός: Cumulative, state και instantaneous safety constraints εκφράζουν διαφορετικές απαιτήσεις και η generalized formulation καλύπτει συγκεκριμένες αυστηρές περιπτώσεις.
- Κεφάλαιο: Safe RL / Experimental protocol
- Θέματα: CMDP; instantaneous safety; constraint semantics
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η εργασία διαχωρίζει expected cumulative safety από almost-sure/high-probability formulations και δείχνει ότι το guarantee type αποτελεί μέρος του problem definition.

### Συμφραζόμενα
Η διπλωματική δεν πρέπει να συγκρίνει safety methods χωρίς κοινό definition του constraint.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν καλύπτει όλες τις risk/CVaR formulations με την ίδια ισοδυναμία.

### Προτεινόμενη χρήση
Για explicit field `safety_guarantee_type`.

### Παραπομπή
Wachi et al., NeurIPS 2023.

## 2. Emergency stop ως prior capability
- Τύπος: πιστή παράφραση
- Θέση: Assumptions 3.2–3.4, Section 4
- Ισχυρισμός: Το MASE χρησιμοποιεί emergency-stop action όταν δεν υπάρχει action που πιστοποιείται ως ασφαλής με το απαιτούμενο confidence.
- Κεφάλαιο: Safety mechanisms
- Θέματα: emergency stop; reset; uncertainty quantifier; intervention
- Κατάσταση: επαληθευμένο

### Κείμενο ή πιστή παράφραση
Η safety guarantee εξαρτάται από δυνατότητα ασφαλούς διακοπής/reset και από confidence bound που καλύπτει το πραγματικό safety cost.

### Συμφραζόμενα
Η δυνατότητα αυτή είναι εξωτερική prior capability, όχι προϊόν του RL agent.

### Περιορισμοί και κίνδυνος παρερμηνείας
Δεν πρέπει να πιστωθεί ως learned recovery.

### Προτεινόμενη χρήση
Report intervention/reset count και utility cost χωριστά από adaptation performance.

### Παραπομπή
Wachi et al., Sections 3–4.