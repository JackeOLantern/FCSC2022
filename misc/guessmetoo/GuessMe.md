# Description :

## Objectif:

le programme source est fourni au format python et donné dans le dossier enoncé.

Il doit faire deviner un nombre de 128 bits en 136 essais. La difficulté est que le programme va mentir une seule fois. Il répond invariablement l'inverse.
La demande est aléatoire. On peut considérer dans un premier temps qu'il ne ment pas durant 128 appels, qui servent à tester les bits positionnés de la solution.
En 128 appels, on aura évalué tous les bits de la solution un par un via une matrice. Il ne resre plus que 8 essais pour trouver lequel des 128 bits a été permuté.
De plus, la répétition n'est pas autorisée.

## Solution

le programme proposé est **GuessMetoo.py**. Il établit une connexion au serveur via une socket.

Il recherche le nombre aléatoire généré par le programme source en testant les bits un à un grâce à une matrice diagonale. Ce procédé s'apparente à un calcul de CRC.

Pour construire le CRC, on définit une matrice du type "Interleave matrix", dans laquelle les lignes et les colonnes sont inversées et pour lesquelles chaque colonnes
est différentes. Comme il est possible d'envoyer huit demandes de 128 bits, il y a une matrice de 128 colonnes et 8 lignes pour vérifier à quel intersection, 
la colonne a été modiféee. Dans ce cas-il in n'y a plus qu'à permuter les bits. Les demandes sont envoyées une par une pour contrôle. Les bonnes réponses sont attendues.

Comme il n'y a dans l'absolu qu'une réponse qui a été modifiée, il s'agit juste d'évaluer laquelle. On calcule la parité de la première demande puis la parité de la 2ème
demande etc.. jusqu'à la parite de la 128ème demande. Ensuite, est calculée la parité des 8 demandes supplémentaires. Si le programme n'avait pas menti, toutes les parités
des bits positionnés devraient correspondre : les 128 premières demandes devraient correspondre aux 8 dernières, sans la modification de là où l'énoncé a menti.

L'exécution du programme demande bit à bit si les 128 bits sont positionnés: donc  tous les bits sont du nombre sont testés donc le nombre en binaire est automatiquement obtenu.
Il s'avère qu'un des chiffres est volontairement faux d'après l'énoncé: il faut déterminer lequel avec les 8 appels restant car sur les 136 appels autorisés, on en a utilisé 128.

L'algorithme doit permettre de trouver le bit modifié dans les appels précédents au bout des huits tests suppléeet si la bonne réponse est trouvée, le programme a produit le "flag".
