import pygame
from game_class import *

pygame.init()


#génération de la fenêtre
pygame.display.set_caption("Pojet : ROBOT")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("map.jpg")
background = pygame.transform.scale(background, (1080, 720))





game = Game()

running = True

while running :
    

    screen.blit(background, (0, 0))


    screen.blit(game.robot.image, (0, 0))

    

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu...")
