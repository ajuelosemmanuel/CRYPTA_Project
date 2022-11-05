Remarques :
+ Seed avec 127 "1" -> toujours des 0
+ Seed avec 127 "0" -> toujours des 0
+ Il est sûrement plus judicieux de regarder les nombres avec un pas de deux : regarder pourquoi mathématiquement.
+  cas particulier : `5488425272918362311545171852291803201` étant l'inverse de `(2**61-1)`, les Y sont les 8 derniers bits des puissances de `(2**61-1)`.
+  Attaque sur le challenge : suivre les étapes du cours