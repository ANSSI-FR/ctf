# Magasin à Secrets

| Phase          | Catégorie         |  Difficulté  | Nombre de résolutions |
|:--------------:|:-----------------:|:------------:|:---------------------:|
| Finale France  | reverse           |    Moyen     |                3 / 50 |

### Description

Lors d'une réponse à incident, nous avons pu récupérer un gestionnaire de mot de passe maison laissé par l'attaquant sur une machine de la victime.

Nous avons également pu récupérer une conversation entre deux attaquants :

```
z3r0: ta vu je t'est envoyé un mail avec le mdp netflix
LBigBossDu15: A merci je vais maté fast and furious ce soir alors
LBigBossDu15: Je lai mis dans le magasin de mdp
z3r0: t est bete, je lavais deja mis, et on a tous le meme mdp
LBigBossDu15: A oui, cest vrai mdr
```

Peut-être est-il possible de récupérer leurs secrets ?

SHA256(`MagasinSecret`): `3d2157e0a7e1a2ca4b031011880189e9f17032db22a3614f9e3905889b1b605e`.
