# Projet de CRYPTA

Schéma :

![imagesujet](media/sujet.png)

Objectifs :
+ Implanter le schéma
+ Discuter de son efficacité
+ Casser le challenge
+ Trouver une attaque / une manière de l'empêcher
+ Si aucune attaque est trouvée, expliquer les tentatives
+ Comment la sécurité serait-elle affectée si certains paramètres étaient agrandis/rétrécis ?
+ Rapport

Date de rendu : 24/11

## To-do list

+ Tester l'efficacité du PRNG en faisant des statistiques
  + Analyser les stats du dossier `statistics`
+ Comparer les deux premières implantations (vitesse etc) en utilisant `timeit` et `cProfile`

## Edit : 13/11 - Le sujet change un peu

![imagesujet](media/vrai_sujet.png)

Il faut donc implanter une version générale du PRNG - ce qui n'est pas un problème. On garde quand même le travail déjà fait, puisqu'on ne va pas jeter ça.