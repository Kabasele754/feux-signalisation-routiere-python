# Feux de signalisation routière

Ce projet est une simulation simple d'un système de feux de signalisation en utilisant le framework Kivy en Python.

## Fonctionnalités

- Simule le fonctionnement des feux de signalisation (vert, orange, rouge).
- Utilise la bibliothèque `time` pour contrôler la durée de chaque état des feux.
- Modularité améliorée avec des fonctions pour afficher l'état des feux et changer leur état.
- Gestion de l'arrêt du programme avec une interruption clavier (Ctrl+C).
- Simule le fonctionnement des feux de signalisation (vert, orange, rouge).
- Utilise le module `kivy.graphics` pour dessiner les feux de signalisation.
- Utilise la classe `Clock` de Kivy pour changer automatiquement la couleur des feux à intervalles réguliers.

## Utilisation

1. Assurez-vous d'avoir Python et Kivy installés sur votre système.
2. Clonez ce dépôt sur votre machine locale.
3. Exécutez le fichier `feux_de_signalisation.py` pour démarrer la simulation des feux de signalisation.

## Explication de `import time`

Dans ce projet, nous utilisons la bibliothèque standard `time` en important le module `time`. Cette bibliothèque fournit différentes fonctions liées au temps, notamment `time.sleep()`. Cette fonction est utilisée pour suspendre l'exécution du programme pendant un certain nombre de secondes, ce qui nous permet de contrôler la durée de chaque état des feux de signalisation.

## Code

Voici le code utilisé pour simuler les feux de signalisation :

```python
import time

# Définition des durées pour chaque état des feux
DUREE_VERTE = 5
DUREE_ORANGE = 2
DUREE_ROUGE = 5

# Initialisation de l'état initial des feux
etat_feux = "vert"

while True:
    if etat_feux == "vert":
        print("Feu vert - Passage autorisé")
        time.sleep(DUREE_VERTE)
        etat_feux = "orange"
    elif etat_feux == "orange":
        print("Feu orange - Attention, le feu va passer au rouge")
        time.sleep(DUREE_ORANGE)
        etat_feux = "rouge"
    elif etat_feux == "rouge":
        print("Feu rouge - Arrêt obligatoire")
        time.sleep(DUREE_ROUGE)
        etat_feux = "vert"
```

## interface  graphique  kivy

[feux de signalisation.mp4](feux%20de%20signalisation.mp4)
## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées d'amélioration ou si vous avez trouvé des bogues, n'hésitez pas à ouvrir une issue ou à proposer une demande d'extraction.

## Auteur

Ce projet a été réalisé par [Achille kabasele](https://github.com/Kabasele754/).





