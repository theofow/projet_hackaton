#############################################################
#                         IMPORTS                           #
#############################################################

import pygame
from class_lib import *
from pygame.locals import *
from pygame import mixer
from Deplacement_robot import deplace

#############################################################
#               GENERATION DE LA FENETRE                    #
#############################################################

pygame.init()

pygame.display.set_caption("Projet : ROBOT")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("annexes/map.jpg")
background = pygame.transform.scale(background, (1080, 720))

mixer.init()
mixer.music.load('annexes/music.ogg')
mixer.music.play()

#############################################################
#               MISE EN PLACE DES ELEMENTS                  #
#############################################################

robot1 = Robot()
robot2 = Robot()
robot2.position.random_pos()
robot1.position.random_pos()

ressources = []
for i in range(5):
    ressources.append(Ressource())
    ressources[i].position.random_pos()


#############################################################
#                        LANCEMENT                          #
#############################################################

running = True

while running:
    screen.blit(background, (0, 0))

    for ressource in ressources:
        screen.blit(ressource.image, ressource.position.xy)

        # si un robot est sur la ressource
        if robot1.position.coo() == ressource.position.coo():
            robot1.score += ressource.value
            ressource.position.random_pos()
        elif robot2.position.coo() == ressource.position.coo():
            robot2.score += ressource.value
            ressource.position.random_pos()

    # déplacement des robots
    deplace(robot1)
    deplace(robot2)

    screen.blit(robot1.image, robot1.position.xy)
    screen.blit(robot2.image, robot2.position.xy)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du programme...")
