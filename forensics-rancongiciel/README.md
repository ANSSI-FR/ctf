# Rançongiciel

| Phase          | Catégorie  |    Difficulté  | Nombre de résolutions |
|:--------------:|:----------:|:--------------:|:---------------------:|
| Pré-sélections | forensics  |     Facile     |            148 / 1241 |
| Pré-sélections | forensics  |     Moyen      |             71 / 1241 |
| Pré-sélections | forensics  |     Moyen      |             58 / 1241 |

SHA256(`mem.dmp`) : `ce117720fa4126f57814b3a779a7eb4ba21570e3f5dfd44a6706771783a46f1b` 

SHA256(`data`) : `16e0f3c320da11e137e9aed80788e44c385f60a554ce034eb6ddfbbfbea31f71`  

## Description

### Q1

Une victime de plus tombée sous le coup d’un rançongiciel. Le paiement de la rançon n’est pas envisagé vu le montant demandé. Vous êtes appelé pour essayer de restaurer les fichiers chiffrés.

Une suite d’éléments est nécessaire pour avancer dans l’investigation et constituer le rapport d’incident.

Pour commencer, quel est le nom du fichier exécutable de ce rançongiciel, son identifiant de processus et quel est devenu le nom du fichier flag.docx une fois chiffré ? Donnez le SHA1 de ce nom avec son extension.

Note : l’image disque fait environ 440 Mo compressés et environ 1.4 Go décompressée. 

Réponse attendue au format ECSC{nom_du_rançongiciel.exe:PiD:sha1}.

### Q2

Retrouvez la clé de chiffrement de ce rançongiciel.

### Q3

Déchiffrez le fichier `data` ci-joint.
