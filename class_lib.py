#############################################################
#                         IMPORTS                           #
#############################################################

from random import randint
import pygame



#############################################################
#                         CLASSES                           #
#############################################################

# La classe grille correspond aux coordonnées d'un objet sur la grille
# Elle fonctionne en concert avec la classe Position qui elle permet
# de manipuler la position formelle de l'objet, c'est à dire sa position
# dans la fenêtre.

# Position définit la position d'un objet sur la map.
# Elle dispose de plusieurs méthodes permettant le déplacement par exemple.
# Tous les objets sont régis par cette classe.

class Position():
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.XY = (self.X,self.Y)
        self.x = 54*self.X
        self.y = 48*self.Y
        self.xy = (self.x,self.y)
    def coo(self):
        return self.X, self.Y
    
    def deplace(self, ax, ay):
        if (self.X+ax,self.Y+ay) not in ((0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),(13,0),(14,0),(15,0),(16,0),(17,0),(18,0),(19,0),(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(15,1),(16,1),(17,1),(18,1),(19,1),(0,2),(19,2),(0,3),(8,3),(10,3),(19,3),(0,4),(19,4),(0,5),(2,5),(3,5),(16,5),(17,5),(19,5),(0,6),(1,6),(2,6),(3,6),(4,6),(15,6),(16,6),(17,6),(18,6),(19,6),(0,7),(1,7),(2,7),(3,7),(4,7),(15,7),(16,7),(17,7),(18,7),(19,7),(0,8),(1,8),(2,8),(3,8),(4,8),(15,8),(16,8),(17,8),(18,8),(19,8),(0,9),(2,9),(3,9),(16,9),(17,9),(19,9),(0,10),(19,10),(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(19,11),(0,12),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(19,12),(0,13),(1,13),(2,13),(3,13),(4,13),(5,13),(6,13),(19,13),(0,14),(1,14),(2,14),(3,14),(4,14),(5,14),(6,14),(7,14),(11,14),(12,14),(13,14),(14,14),(15,14),(16,14),(17,14),(18,14),(19,14),(0,15),(1,15),(2,15),(3,15),(4,15),(5,15),(6,15),(7,15),(8,15),(9,15),(10,15),(11,15),(12,15),(13,15),(14,15),(15,15),(16,15),(17,15),(18,15),(19,15)):
            self.x = self.x + ax*54
            self.y = self.y + ay*48
            self.xy = (self.x,self.y)
            self.X = self.X+ax
            self.Y = self.Y+ay
            self.XY = (self.X,self.Y)
        
    def set_pos(self,bx,by):
        self.X = bx
        self.Y = by
        self.x = self.X*54
        self.y = self.Y*48
        
    def random_pos(self):
        #self.set_pos(randint(0,19),randint(0,14))
        self.set_pos(randint(7,8),randint(7,8))
# Battery définit la batterie des robots et diminue avec les déplacement.

class Battery:
    def __init__(self):
        self.percent = 100
        self.max_percent = 100


# Stock correspond au stockage des robots (leur max et leur contenu).

class Stock:
    def __init__(self):
        self.max = 10
        self.content = []


# La Team change le point d'apparition du robot


# Robot représente un robot au départ

class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.position = Position()
        self.battery = Battery()
        self.stock = Stock()
        self.image = pygame.transform.scale(pygame.image.load("robot_sprite/robot_right.png"), (52, 46))

    def switch_sprite(self, dir):
        if dir == "up":
            self.image = pygame.transform.scale(pygame.image.load("robot_sprite/robot_up.png"), (52, 46))
        elif dir == "down":
            self.image = pygame.transform.scale(pygame.image.load("robot_sprite/robot_down.png"), (52, 46))
        elif dir == "left":
            self.image = pygame.transform.scale(pygame.image.load("robot_sprite/robot_left.png"), (52, 46))
        elif dir == "right":
            self.image = pygame.transform.scale(pygame.image.load("robot_sprite/robot_right.png"), (52, 46))
        # self.rect = self.image.get_rect()


# Bank est la classe définissant le score obtenu par les robots

class Bank:
    def __init__(self):
        self.balance = 0


# Ressource est la classe qui définit chaque ressource. Certaines apparaissent
# aléatoirement tandis que d'autre sont fixe. Leur taux d'apparition est
# variable en fonction de leur valeur.

class Ressource:
    '''
    Guide pour le système de ressource
    ID: 
        001 : Pierre
        002 : Bois
        003 : Eau
        004 : Or
    '''

    def __init__(self):
        self.id = randint(1, 4)
        self.position = Position()
        if self.id == 1:
            self.image = pygame.transform.scale(pygame.image.load("ressources_sprite/pierre.png"), (52, 46))
        if self.id == 2:
            self.image = pygame.transform.scale(pygame.image.load("ressources_sprite/bois.png"), (52, 46))
        if self.id == 3:
            self.image = pygame.transform.scale(pygame.image.load("ressources_sprite/eau.png"), (52, 46))
        if self.id == 4:
            self.image = pygame.transform.scale(pygame.image.load("ressources_sprite/or.png"), (52, 46))
            
        # prix à ajouter


# création d'un agent (test)


class Game:
    def __init__(self):
        self.robot = Robot()
