Contexte du projet :

K17 est un agent infiltré qui a récupéré des informations capitales sur une organisation terroriste mais il est pris au piège dans une salle de conférence.
Son seul espoir est de transmettre toutes les données lors de la conférence qui a lieu le lendemain sans se faire repérer. Son seul moyen est de faire passer une message inaudible pour la salle, mais pas par son équipier.
L'agent X21 est en train de son côté d'analyser le flux audio de la salle de conférence pour peut être trouver un message caché.

Le premier programme "Programme K17.py" va récupérer les données d'un fichier passé en paramètre, les chiffrer puis générer un fichier audio inaudible pour l'oreille humaine.
Le deuxième programme "Programme X21.py" va prendre un fichier audio en paramètre, filtrer le signal pour ne garder que les hautes fréquences, démoduler le signal, le déchiffrer et restituer le contenu du message.

Les fichiers "ASK.py" et "LZW.py" sont deux bibliothèques externes utilisées dans les deux programmes principaux.