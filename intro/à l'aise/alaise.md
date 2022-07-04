# Description :

## Objectif:

A l'aise
Cette épreuve vous propose de déchiffrer un message chiffré avec la méthode inventée par Blaise de Vigénère.

La clé est `FCSC` et le message chiffré :

Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk
n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz
ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f
Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf.

Grâce à l'outil en ligne dcode, le message est restitué avec le chiffrage de Vigénère. Sans la clé indiquée 'CLE', 
le décodage par cet outil du message d'origine est réalisé par la brute force et fournit le résultat immédiatement.
Le flag est le nom de la ville mentionnée dans ce message.


## Solution

> **Attention, vous n'avez le droit qu'à 3 tentatives !**
On va de suite tenter de déchiffrer le texte via la méthode du chiffre de Vigenère et la clé fournie via le fabuleux CyberChef : 
Bonjour cher agent ! Votre prochaine mission, si vous
l'acceptez bien sur, sera d'infiltrer le reseau
souterrain ou se cache nos ennemis. Rendez-vous a
**Nantes** le 29 avril pour le debut de votre mission.

Le flag est donc FCSC{Nantes}