# Hvítur Kassi (1) et (2)

| Phase          | Catégorie  |    Difficulté  | Nombre de résolutions |
|:--------------:|:----------:|:--------------:|:---------------------:|
| Pré-sélections | crypto     |     Moyen      |             36 / 1241 |
| Pré-sélections | crypto     |   Difficile    |              0 / 1241 |

### Description (1)

Saurez-vous trouver l'entrée ``m`` qui affiche le flag ?

Le flag est de la forme ECSC{``m``}.

SHA-256(`wb.py`) : `636e1d5ceca1cf99ce9b4eeddfca0f1e09a0d769cf226c5221209c40771cf2a8`

### Description (2)

Saurez-vous désormais extraire la clé secrète ``k`` utilisée par cet algorithme de chiffrement ?

Le flag est de la forme ECSC{``k`` au format hexadécimal}.

Note : `wb.py` est le même que pour ``Hvítur Kassi (1)``

--
*Indice :* Le fichier `wb.py` implémente la fonction de chiffrement de l'algorithme `SKINNY-64-128` avec une clé secrète `k` qu'il faut retrouver.

Les spécifications de `SKINNY-64-128` sont disponibles ici : [https://sites.google.com/site/skinnycipher/design](https://sites.google.com/site/skinnycipher/design)


