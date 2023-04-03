#Ajout des lib
from random import randint


#############################################################
#                         CLASSES                           #
#############################################################



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
    
    
class Battery:
    def __init__(self):
        self.percent = 100
        self.level = 1

class Stock:
    def __init__(self):
        self.max = 10
        self.content = []

class Robot:
    def __init__(self, position=None):
        self.position = position if position else Position()
        self.battery = Battery()
        self.stock = Stock()


class Bank:
    def __init__(self):
        self.balance = 0
        
class Ressource:
    '''
    Guide pour le système de ressource
    ID: 
        001 : Pierre
        002 : Bois
        003 : Eau
    '''
    def __init__(self):
        self.id = randint(1,3)
        self.position = Position()
        #prix à ajouter

agent_1 = Robot()