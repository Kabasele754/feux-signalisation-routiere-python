import pygame
from pygame.locals import *

# Paramètres de la fenêtre et de la route
size = width, height = (800, 800)
road_w = int(width / 1.6)
roadmark_w = int(width / 50)

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

    # Dessin des poteaux
    pole_color = (100, 100, 100)  # Couleur du poteau
    pole_width = 4  # Largeur du poteau

    # Position des poteaux
    pole1_x, pole1_y = width // 4, height // 4
    pole2_x, pole2_y = width // 4 * 3, height // 4
    pole3_x, pole3_y = width // 4, height // 4 * 3
    pole4_x, pole4_y = width // 4 * 3, height // 4 * 3

    # Dessin des poteaux
    pygame.draw.rect(screen, pole_color, (pole1_x - pole_width // 2, pole1_y - road_w / 2, pole_width, road_w))
    pygame.draw.rect(screen, pole_color, (pole2_x - pole_width // 2, pole2_y - road_w / 2, pole_width, road_w))
    pygame.draw.rect(screen, pole_color, (pole3_x - pole_width // 2, pole3_y - road_w / 2, pole_width, road_w))
    pygame.draw.rect(screen, pole_color, (pole4_x - pole_width // 2, pole4_y - road_w / 2, pole_width, road_w))

    # Dessin des feux de signalisation
    traffic_light_size = 15  # Taille des feux de signalisation

    # Dessin des feux de signalisation pour chaque poteau
    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (pole1_x, pole1_y - 30), traffic_light_size)  # Feu du haut
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (pole1_x, pole1_y), traffic_light_size)  # Feu du milieu
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (pole1_x, pole1_y + 30), traffic_light_size)  # Feu du bas

    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (pole2_x, pole2_y - 30), traffic_light_size)  # Feu du haut
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (pole2_x, pole2_y), traffic_light_size)  # Feu du milieu
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (pole2_x, pole2_y + 30), traffic_light_size)  # Feu du bas

    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (pole3_x, pole3_y - 30), traffic_light_size)  # Feu du haut
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (pole3_x, pole3_y), traffic_light_size)  # Feu du milieu
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (pole3_x, pole3_y + 30), traffic_light_size)  # Feu du bas

    pygame.draw.circle(screen, (255, 0, 0) if traffic_light_state == "red" else (0, 0, 0), (pole4_x, pole4_y - 30), traffic_light_size)  # Feu du haut
    pygame.draw.circle(screen, (255, 255, 0) if traffic_light_state == "yellow" else (0, 0, 0), (pole4_x, pole4_y), traffic_light_size)  # Feu du milieu
    pygame.draw.circle(screen, (0, 255, 0) if traffic_light_state == "green" else (0, 0, 0), (pole4_x, pole4_y + 30), traffic_light_size)  # Feu du bas

    # Affichage des véhicules
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    pygame.display.update()

# Fermeture de la fenêtre
pygame.quit()
