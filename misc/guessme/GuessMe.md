# Description :

## Objectif :

le programme source est fourni au format python et donné dans le dossier enoncé.

Il consiste à deviner un nombre entier en **16 coups au maximum** et cette action est faite 64 fois.

Il n'est pas possible de réaliser l'opération manuellement avec la commande "nc" (netcat) indiquée car la session dure environ une minute.

La saisie manuelle est complètement hors délai avec la contrainte. Il est proposé ici de créer un script en python automatisant la recherche.

## Solution :

le programme proposé est **GuessMe.py**. Il établit une connexion au serveur via une socket.

Il recherche le nombre aléatoire généré par le programme source en utilisant une simple dichotomie.

Il prend le milieu de l'intervalle de récherche et dit si le nombre proposé est plus grand ou plus petit que celui généré et recoupe l'intervalle en deux.
L'idée est d'obtenir la réponse en 16 coups ou moins. Comme c'est un nombre de 8 bits aléatoires, il doit pouvoir être trouvé en 16 étapes. 

Le plus grand entier entier possible déduit d'une taille de 8 octets est converti en décimal. Il permet de connaître le plus grand entier de cet intervalle.

## Déroulement :
Connexion au service sur le port défini.

Open socket.

01found,15moretogo

02found,14moretogo

03found,13moretogo

04found,12moretogo

05found,11moretogo

06found,10moretogo

07found,9moretogo

08found,8moretogo

09found,7moretogo

010found,6moretogo

011found,5moretogo

012found,4moretogo

013found,3moretogo

014found,2moretogo

015found,1moretogo

016found,0moretogo

Au bout de la quinzième itération, 15 fois consécutives du nombre trouvé en moins de deux minutes, par l'automatisation et pas décelable manuellement,
Le drapeau "flag" obtenu à l'issue de la séquence calculatoire s'affiche : 

**FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}**
