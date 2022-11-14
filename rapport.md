# Rapport

J'ai la flemme de rédiger donc liste :
+ On commence par implanter de manière naïve cf le fichier `scheme_naive.py` dans le dossier `lib`.
+ On crée une seconde version qui a des fonctions de logging, afin de voir l'historique des `X` et des `Y`.
+ On remarque qu'avec des clés petites (1,3 et 7 on été testées), il y a une sorte de pattern :
```
Pour X_0 = 3
X_0	:	0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011
X_1	:	0000000000000000000000000000000000000000000000000000000000000000101111111111111111111111111111111111111111111111111111111111101
X_2	:	0001011111111111111111111111111111111111111111111111111111111110100000000000000000000000000000000000000000000000000000000000011
X_3	:	1011100000000000000000000000000000000000000000000000000000000010010001011111111111111111111111111111111111111111111111111111100
X_4	:	1001000010111111111111111111111111111111111111111111111111111100111010000000000000000000000000000000000000000000000000000000011
X_5	:	0000110001000000000000000000000000000000000000000000000000000011111111000010111111111111111111111111111111111111111111111111100
X_6	:	0111001101000101111111111111111111111111111111111111111111111011000001101110000000000000000000000000000000000000000000000000100
X_7	:	1110110110010110000000000000000000000000000000000000000000000110000101011111000101111111111111111111111111111111111111111111010
X_8	:	1101010100101000001011111111111111111111111111111111111111111000101001010111010000000000000000000000000000000000000000000000101
```
+ Il faut donc regarder les mathématiques derrière ce PRNG de plus près. Après quelques observations, on trouve la formule générale : `X_n = X_0 * (2**61 - 1)**n mod (2**127 - 1)`
+ On fait alors une seconde implantation utilisant cette formule, qui n'a donc pas besoin de mémoire sur les `X_i` (mais qui nécessite néanmoins un compteur). De la même manière, on fait une version de l'implantation avec des fonctions de logging.

---

# Partie Challenge / Attaque

En lisant le cours (voir documents/lattice_cryptanalysis-3-5.pdf) on trouve une attaque sur ce schéma. On suit alors les étapes :
+ on doit récupérer un état interne qui fait log2(m) bits avec m = (2**127 - 1) soit 127 bits.
+ Ici, chaque sortie ne contient que 8 bits d'information (les 8 bits de poids faible). On a donc `log2(m/k) = 8 -> m/k = 2**8 -> k=2**119`
+ il faut donc examiner 16 sorties d'après la formule du cours : `log2(m)/(log2(m) - log2(k)) = 15.875`.

ce qui est écrit au dessus est totalement faux je crois lol

Première tentative : on essaie de faire ce qui est écrit dans le cours cf attempts/first_attempt.py - spoiler : ça n'a pas marché
le code n'est pas clean, mais je vais voir pour en faire un bien qui facilite les tests