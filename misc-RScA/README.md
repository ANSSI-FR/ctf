# Challenge RScA

*Fichiers fournis :* `sniff_0` et `sniff_1`.

À la suite d'une intervention, nos équipes ont récupéré un téléphone sécurisé utilisé par un agent appartenant à une organisation criminelle. Depuis sa récupération, nous avons pris soin de laisser le téléphone en permanence sous tension.

Habituellement, ce téléphone est notamment utilisé pour recevoir des instructions signées par un individu plus haut dans la chaîne hiérarchique. Le téléphone est chargé de *vérifier* les signatures de ces messages. Une phase de rétroconception nous a permis d'identifier que l'algorithme utilisé pour cette opération est un **RSA**.

La particularité forte de notre contexte est l'**absence totale d'information sur les paramètres publics utilisés par l'algorithme**. De plus, la vérification est implémentée de manière sécurisée, de façon à empêcher la récupération de ces paramètres.

L'objectif final de notre mission est de parvenir à signer des messages à la place du supérieur hiérarchique, afin de tendre un piège aux membres de l'organisation. Pour cela, nous vous demandons de retrouver tous les paramètres utilisés.

La rétroconception nous a appris plusieurs points importants.

Premièrement, nous avons pu retrouver l'implémentation du RSA. Voici le pseudo-code que nous avons pu reconstruire, où on note phi(N) l'indicatrice d'Euler de N :

```
Function RSA(m, e, phi(N), N):
    r  <- random(0, 2**32)
    e' <- e + r * phi(N)
    accumulator = 1
    dummy = 1
    for i from len(e') - 1 to 0:
        accumulator <- (accumulator * accumulator) mod N
        tmp <- (accumulator * m) mod N
        if (i-th lsb of e') == 1:
            accumulator <- tmp
        else:
            dummy <- tmp
    return accumulator
```

Deuxièmement, il s'avère que les deux opérations de multiplications modulaires

```
accumulator <- (accumulator * accumulator) mod N
```
et

```
tmp <- (accumulator * m) mod N
```

sont effectuées en faisant appel à un accélérateur matériel.

Au démarrage du téléphone, le bloc responsable de la signature va chercher dans une carte SIM les paramètres e et N. Le paramètre N est fourni à l'accélérateur et stocké dans un SRAM non lisible. Tout redémarrage du téléphone impliquerait le verrouillage de la carte SIM, que nous ne pouvons pas débloquer (son propriétaire étant plutôt muet quant au code PIN nécessaire).

Du côté des bonnes nouvelles, nous sommes parvenus lors de notre intervention à récupérer un morceau de la documentation de cet accélérateur, dont nous vous fournissons un mémo ci-dessous. De plus, nous sommes parvenus à sniffer le bus de communication entre cet accélérateur et le bloc responsable de la vérification de signature.

Depuis l'intervention, nous avons reçu deux messages différents de l'extérieur. Le *sniffing* du bus lors de la vérification des signatures de chacun de ses messages vous est donné. Le contenu des messages en lui-même est anecdotique.

Votre objectif est de retrouver les paramètres (N, p, q, e, d) du RSA, avec :

* N : le module "public" du RSA ;
* p, q : les facteurs premiers de N (p * q = N, et p < q) ;
* e : l'exposant "public" stocké sur le téléphone (0 < e < phi(N)) ;
* d : l'exposant "privé" utilisé pour signer les messages (0 < d < phi(N)).

Le flag à retrouver est de la forme ECSC{N+p+q+e+d} avec N+p+q+e+d écrit en hexadécimal.


# Protocole de communication

Les trames envoyées par le bloc RSA à l'accélérateur modulaire suivent la forme suivante :

```
| senderId | receiverId | opcode | operand1(opt) | operand2(opt) |
```

Les trames envoyées par l'accélérateur au bloc RSA suivent la forme suivante :

```
| senderId | receiverId | operand1 |
```

avec :

* senderId : 1 octet codant l'Id du bloc expéditeur
* receiverId : 1 octet codant l'Id du bloc destinataire
* opcode (optionnel) : 1 octet codant l'opération (voir ci-après)
* operand1 : un certain nombre d'octets représentant le premier opérande
* operand2 : un certain nombre d'octets représentant le second opérande

## Description des opérations

### Chargement du module N

Demande le chargement du module N dans l'accélérateur hardware.

* opcode : 0x11
* operand1 : 2 octets représentant la taille t de N en bits
* operand2 : t octets représentant la valeur de N

### Addition modulaire

Demande l'addition modulaire de deux opérandes de taille t.
La taille t est inférée par l'accélérateur grâce à sa connaissance de N.

* opcode : 0x22
* operand1 : t octets représentant la valeur du premier opérande
* operand2 : t octets représentant la valeur du second opérande

### Soustraction modulaire
Demande la soustraction modulaire de deux opérandes de taille t.
La taille t est inférée par l'accélérateur grâce à sa connaissance de N.

* opcode : 0x33
* operand1 : t octets représentant la valeur du premier opérande
* operand2 : t octets représentant la valeur du second opérande

### Inversion modulaire
Demande l'inversion modulaire d'un opérande de taille t. Si l'élément n'a pas d'inverse, retourne 0.
La taille t est inférée par l'accélérateur grâce à sa connaissance de N.

* opcode : 0x44
* operand1 : t octets représentant la valeur à inverser
* operand2 : non présent

### Multiplication modulaire
Demande la multiplication modulaire de deux opérandes de taille t.
La taille t est inférée par l'accélérateur grâce à sa connaissance de N.

* opcode : 0x55
* operand1 : t octets représentant la valeur du premier opérande
* operand2 : t octets représentant la valeur du second opérande

### Mise au carré modulaire
Demande la mise au carré modulaire d'un opérande de taille t.
La taille t est inférée par l'accélérateur grâce à sa connaissance de N.

* opcode : 0x66
* operand1 : t octets représentant la valeur à mettre au carré
* operand2 : non présent

### Demande de réponse
Demande de la réponse suite à une demande d'opération.

* opcode : 0x77
* operand1 : non présent
* operand2 : non présent

La réponse de taille t suit le format de trames décrit au début de ce document.
