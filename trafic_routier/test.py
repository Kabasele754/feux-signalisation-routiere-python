import pygame
from pygame.locals import *

# Paramètres de la fenêtre et de la route
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)

# Paramètres de l'animation
speed = 1

# Initialisation de Pygame
pygame.init()
running = True

# Création de la fenêtre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulation de trafic routier")
screen.fill((60, 220, 0))

# Chargement des images des véhicules
car = pygame.image.load("trafic_routier/car.png")
car_loc = car.get_rect()
car_loc.center = width / 1.5, height * 0.5

car2 = pygame.image.load("trafic_routier/otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = width / 1.5 - road_w / 1.5, height * 0.5

# Paramètres du feu de signalisation
traffic_light_x = width / 2
traffic_light_y = height / 2
traffic_light_state = "green"
traffic_light_counter = 0
green_duration = 2000  # Durée en frames (60 frames par seconde)
red_duration = 800  # Durée en frames (60 frames par seconde)
yellow_duration = 300  # Durée en frames (60 frames par seconde)

# Boucle principale
while running:
    # Incrémentation du compteur de temps pour le feu de signalisation
    traffic_light_counter += 1

    # Mise à jour de l'état du feu de signalisation
    if traffic_light_state == "green" and traffic_light_counter > green_duration:
        traffic_light_state = "yellow"
        traffic_light_counter = 0
    elif traffic_light_state == "yellow" and traffic_light_counter > yellow_duration:
        traffic_light_state = "red"
        traffic_light_counter = 0
    elif traffic_light_state == "red" and traffic_light_counter > red_duration:
        traffic_light_state = "green"
        traffic_light_counter = 0

    # Animation des véhicules 1
    if traffic_light_state == "green":
        car2_loc[1] += speed
    if car2_loc[1] > height:
        car2_loc.center = width / 1.5 - road_w / 2, -200

    # Animation des véhicules 2
    if traffic_light_state == "green":
        car_loc[1] -= speed  # Ajustement de la position vers le haut
    if car_loc[1] < -200:  # Si la voiture sort de l'écran vers le haut
        car_loc.center = width / 1.5, height  # Réinitialisation de la position en bas de l'écran

    # Logique de fin de jeu
    if car_loc.colliderect(car2_loc):
        print("GAME OVER! YOU LOST!")
        break

    # Dessin de la route
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (50, 50, 50), (0, height / 2 - road_w / 2, width, road_w))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (0, height / 2 - roadmark_w / 2, width, roadmark_w))

    # Dessin du feu de signalisation
    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (traffic_light_x, traffic_light_y - 50), 20)
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (traffic_light_x, traffic_light_y), 20)
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (traffic_light_x, traffic_light_y + 50), 20)

    # Déplacement de la voiture
    if traffic_light_state == "green":
        car_loc[1] -= speed

    # Affichage des véhicules
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    pygame.display.update()

# Fermeture de la fenêtre
pygame.quit()
