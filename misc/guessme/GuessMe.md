# Description :

## Objectif:

le programme source est fourni au format python et donné dans le dossier enoncé.

Il consiste à deviner un nombre entier en **16 coups au maximum** et cette action est faite 64 fois.

Il n'est pas possible de réaliser l'opération manuellement avec la commande "nc" (netcat) indiquée car la session dure environ une minute.

La saisie manuelle est complètement hors délai avec la contrainte. Il est proposé ici de créer un script en python automatisant la recherche.

## Solution

le programme proposé est **GuessMe.py**. Il établit une connexion au serveur via une socket.

Il recherche le nombre aléatoire généré par le programme source en utilisant une simple dichotomie.

Il prend le milieu de l'intervalle de récherche et dit si le nombre proposé est plus grand ou plus petit que celui généré et recoupe l'intervalle en deux.
L'idée est d'obtenir la réponse en 16 coups ou moins. Comme c'est un nombre de 8 bits aléatoires, il doit pouvoir être trouvé en 16 étapes. 

Le plus grand entier entier possible déduit d'une taille de 8 octets est converti en décimal. Il permet de connaître le plus grand entier de cet intervalle.