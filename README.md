# Projet de CRYPTA

Schéma :

![imagesujet](media/sujet.png)

Objectifs :
+ Implanter le schéma
  + Voir `/lib`
+ Discuter de son efficacité
  + Statistiques dans le rapport
+ Casser le challenge
  + `challenge_attack.py`
  + Seed  = `160132562724753331766255120961262537267`
+ Trouver une attaque / une manière de l'empêcher
  + Attaque : trouvée - manière de l'empêcher : utiliser un P pair (on ne peut plus inverser 2**8, et donc l'attaque n'est plus possible !)
+ Si aucune attaque est trouvée, expliquer les tentatives
  + rapport
+ Comment la sécurité serait-elle affectée si certains paramètres étaient agrandis/rétrécis ?
  + rapport
+ Rapport

Date de rendu : 24/11

## To-do list
+ Faire le rapport "propre"
+ Bien décrire comment marche l'attaque

## Edit : 13/11 - Le sujet change un peu

![imagesujet](media/vrai_sujet.png)

Il faut donc implanter une version générale du PRNG - ce qui n'est pas un problème. On garde quand même le travail déjà fait, puisqu'on ne va pas jeter ça.

