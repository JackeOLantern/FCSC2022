# Description :

## Objectif:

~$ nc challenges.france-cybersecurity-challenge.fr 2002
(nc : utilitaire pour ouvrir la connexion réseau sur l'URL et le port).
La logique classique de paiement tend à minimiser le nombre d'éléments de transactions et d'abord d'écouler les plus gros billets et pièces et on s'arrête quand le montant qui reste est inférieur au montant de la pièce ou que l'on n'a plus de pièces de ce type-là.
Avec le montant habituel (5, 10, 20), la transaction optimale est presque toujours celle-là: par exemple, si on doit payer 12 €, on donne 10€ + 2 € avec deux pièces.
Dans l'exercice, il s'agit de trouver un exemple qui fasse mieux en moins d'itérations (moins de grand nombre de pièces et un maximum de pièces différentes à utiliser).
La première ligne représente le montant à payer ; la deuxième ligne représente les pièces disponibles dans le porte-feuille; normalement, on a intérêt à prendre la plus grosse pièce. Or, ça ne fonctionne pas. Si on paye déjà avec 40€, il reste 15€ à payer. 
Comme toutes les autres pièces sont supérieures au montant restant, on devra utiliser 15 pièces de 1 €. Si on bypasse la pièce de 40 euros, il reste 30€, à compléter avec 24€ et 1€ : en trois pièces différentes, on obtient le résultat. On a utilisé plus
de pièces différentes mais moins de pièces au final. Evidemment, la solution est loin d'être unique puisque beaucoup d'autres solutions pourraient être proposées. On nous demande une seule solution pas toutes les solutions possibles.

## Solution

55
40 24 30 1
24 30 1
FCSC{bfa26d8861b987d439fe8d8f1004e8b8ea07a7b6f936b844e0f78f43c2dc33e9}