
import pygame
from class_lib import *
from Deplacement_robot import random_move

pygame.init()

#génération de la fenêtre
pygame.display.set_caption("Projet : ROBOT")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("map.jpg")
background = pygame.transform.scale(background, (1080, 720))

robot1 = Robot()

print(robot1.position)
running = True

while running :

    # gestion des évènements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du programme...")

    # déplacement aléatoire du robot
    random_move(robot1)

    # affichage du robot et de la map
    screen.blit(background, (0, 0))
    screen.blit(robot1.image, robot1.position.xy)
    pygame.display.flip()