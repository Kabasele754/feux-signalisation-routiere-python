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

