import pygame
from class_lib import *

pygame.init()


#génération de la fenêtre
pygame.display.set_caption("Pojet : ROBOT")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("map.jpg")
background = pygame.transform.scale(background, (1080, 720))





robot1 = Robot()

print(robot1.position)
running = True

while running :
    

    screen.blit(background, (0, 0))


    screen.blit(robot1.image, robot1.position.xy)

    

    pygame.display.flip()

    for event in pygame.event.get():
        # Cette boucle représente les évènements càd les éléments qui donnent 
        # vie au jeu et qui permette l'intéraction avec l'utilisateur


        # FERMETURE DU PROGRAMME

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du programme...")

        # DEPLACEMENT DU ROBOT

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                robot1.position.deplace(54,0)
            elif event.key == pygame.K_LEFT:
                robot1.position.deplace(-54,0)
            elif event.key == pygame.K_DOWN:
                robot1.position.deplace(0,48)
            elif event.key == pygame.K_UP:
                robot1.position.deplace(0,-48)

