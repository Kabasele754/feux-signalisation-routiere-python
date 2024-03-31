import pygame
from pygame.locals import *
import random

# Définition des paramètres de la fenêtre et de la route
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4

# Paramètres d'animation
speed = 1

# Initialisation de Pygame
pygame.init()
running = True

# Création de la fenêtre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Simulation de feu de signalisation")
screen.fill((60, 220, 0))

# Chargement des images des véhicules
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

# Paramètres du feu de signalisation
traffic_light_x = width / 2 - road_w / 2 - 40
traffic_light_y = height / 2 + 50  # Décalage vers le bas pour que le feu soit au-dessus de la route
traffic_light_state = "red"  # État initial du feu
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

    # Animation du véhicule ennemi
    if traffic_light_state == "green":
        car2_loc[1] += speed
    if car2_loc[1] > height:
        car2_loc.center = left_lane, -200

    # Logique de fin de jeu
    if car_loc.colliderect(car2_loc):
        print("GAME OVER! YOU LOST!")
        break

    # Écoute des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])

    # Dessin de la route
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))

    # Dessin du feu de signalisation
    pygame.draw.rect(screen, (100, 100, 100), (traffic_light_x - 20, traffic_light_y - 70, 40, 220))  # Poteau
    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (traffic_light_x, traffic_light_y), 20)  # Feu rouge
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (traffic_light_x, traffic_light_y + 70), 20)  # Feu jaune
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (traffic_light_x, traffic_light_y + 140), 20)  # Feu vert

    # Déplacement de la voiture
    if traffic_light_state == "green":
        car_loc[1] -= speed

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()

# Fermeture de la fenêtre
pygame.quit()
