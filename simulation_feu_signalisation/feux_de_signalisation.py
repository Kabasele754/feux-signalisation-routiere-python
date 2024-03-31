import time

# Durées pour chaque état des feux (en secondes)
DUREE_VERTE = 5
DUREE_ORANGE = 2
DUREE_ROUGE = 5

def afficher_feu(etat_feux):
    """Affiche l'état actuel des feux."""
    if etat_feux == "vert":
        print("Feu vert - Passage autorisé")
    elif etat_feux == "orange":
        print("Feu orange - Attention, le feu va passer au rouge")
    elif etat_feux == "rouge":
        print("Feu rouge - Arrêt obligatoire")

def changer_etat_feux(etat_feux):
    """Change l'état des feux."""
    if etat_feux == "vert":
        return "orange"
    elif etat_feux == "orange":
        return "rouge"
    elif etat_feux == "rouge":
        return "vert"

# Initialisation de l'état initial des feux
etat_feux = "vert"

try:
    while True:
        afficher_feu(etat_feux)
        if etat_feux == "vert":
            time.sleep(DUREE_VERTE)
        elif etat_feux == "orange":
            time.sleep(DUREE_ORANGE)
        elif etat_feux == "rouge":
            time.sleep(DUREE_ROUGE)
        etat_feux = changer_etat_feux(etat_feux)
except KeyboardInterrupt:
    print("\nArrêt du programme.")

