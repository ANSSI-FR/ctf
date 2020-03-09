# StegCryptoDIY - Final Boss

| Phase          | Catégorie  |   Difficulté   | Nombre de résolutions |
|:--------------:|:----------:|:--------------:|:---------------------:|
| Finale France  |   crypto   |    Difficile   |                0 / 50 |

### Description

Comme tout le monde s'en rappelle Dumb et Dumby ont échangé, il y a quelques semaines, en utilisant un nouveau cryptosystème basé sur les problèmes FACT et DLP : CryptoDIY.

Pour rappel, les paramètres `g1` et `g2` sont définis par

```
g1 = g ** (s1 * (p - 1)) mod N
g2 = g ** (s2 * (q - 1)) mod N
```

où `g` est un générateur inconnu `s1` et `s2` sont deux nonces et bien sûr `p` et `q` sont inconnus ;-)

Ils pensent avoir une version durcie, montrez leurs le contraire en retrouvant leur clé partagée à partir des informations issues des deux challenges précédents (`StegCryptoDIY - PNG` et `StegCryptoDIY - RNG`).

Note : le flag suit le format `lehack2019{xxx}` où `xxx` est une chaine de caractères.

SHA(`leHACK19_chall.png`) = `9bf1385ef8fc2638b90dfaa3d47d4a50ad52b67bf173b052621040f3ce48ca90`.

SHA(`leHACK19_ref.png`) = `9151821ba115ed4de102a79695dca76f4994550c6c37068804abe71778c9009e`.
