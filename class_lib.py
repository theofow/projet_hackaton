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
