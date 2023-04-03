#############################################################
#                         IMPORTS                           #
#############################################################

from random import randint


#############################################################
#                         CLASSES                           #
#############################################################



# Position définit la position d'un objet sur la map.
# Elle dispose de plusieurs méthodes permettant le déplacement par exemple.
# Tous les objets sont régis par cette classe.

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def coo(self):
        return self.x, self.y
    
    def deplace(self, ax, ay):
        self.x = self.x + ax
        self.y = self.y +ay
    
    def reset_pos(self):
        self.x = 0
        self.y = 0
        
    def random_pos(self):
        self.x = randint(0,20)
        self.y = randint(0,20)
    

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

# Robot représente un robot au départ

class Robot:
    def __init__(self, position=None):
        self.position = position if position else Position()
        self.battery = Battery()
        self.stock = Stock()

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
        self.id = randint(1,4)
        self.position = Position()
        #prix à ajouter



# création d'un agent (test)
agent_1 = Robot()