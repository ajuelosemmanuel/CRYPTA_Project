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

+ Poser les deux questions suivantes :
  + Peut-on mettre du code dans le rapport ? Si oui, quelle proportion ? Sinon, est-il possble de fournir un accès au repo GitHub ?
  + À quoi servent `a` et `p` dans le challenge ?
+ Tester l'efficacité du PRNG en faisant des statistiques
  + Idée : Générer 100.000 nombres aléatoires pour 1000 seeds différentes, puis faire un max de stats
+ Comparer les deux premières implantations (vitesse etc) en utilisant `timeit` et `cProfile`
+ Commenter chaque fichier Python et chaque fonction proprement