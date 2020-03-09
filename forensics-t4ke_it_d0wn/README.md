# T4ke it d0wn

| Phase          | Catégorie  |  Difficulté   | Nombre de résolutions |
|:--------------:|:----------:|:-------------:|:---------------------:|
| Finale France  | forensics  |  Moyen        |               10 / 50 |

### Description

Un botnet de plus vient d'être démantelé! Les communications avec le C2 sont détournées avec un Sinkhole depuis lequel des captures réseau sont faites.
L'analyste en charge de cette investigation n'a pas réussi à décoder ces communications... Il a tout de même mis en place un honeypot et a réussi à tromper ce botnet qui s'attaque principalement à des Raspberry exposés sur internet avec le service SSH activé et mot de passe par défaut. Cet honeypot a permis de récupérer le script client qui envoie les données au C2!

Votre mission, retrouver et décoder les données contenues dans cette capture pour identifier la victime à l'aide du script client!

SHA256(`client.py`) : `be984312cdfe18adf366ef0f90ed95c531b32d9fdb2bb242ac8d2227c9367620`.

SHA256(`sinkhole_capture.pcap`) : `8b02ee26c96e43d6c48fc4f7c5093b183b0a3d43581ce9e3b0a011d9597498dd`.
