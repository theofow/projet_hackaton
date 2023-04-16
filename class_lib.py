import random
import pygame

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xy = (self.x, self.y)
        self.width = 1080
        self.height = 720

    def coo(self):
        return self.x, self.y

    def deplace(self, ax, ay):
        if 0 <= self.x + ax <= self.width - 50:  # Vérifie si le robot ne sort pas de la largeur de l'écran
            self.x = self.x + ax
        if 0 <= self.y + ay <= self.height - 45:  # Vérifie si le robot ne sort pas de la hauteur de l'écran
            self.y = self.y + ay
        self.xy = (self.x, self.y)

class Battery:
    def __init__(self):
        self.percent = 100
        self.max_percent = 100

class Stock:
    def __init__(self):
        self.max = 10
        self.content = []

class Robot:
    def __init__(self):
        self.position = Position()
        self.battery = Battery()
        self.stock = Stock()
        self.image = pygame.transform.scale(pygame.image.load("robot_sprite.png"), (50, 45))

class Bank:
    def __init__(self):
        self.balance = 0

class Ressource:
    def __init__(self):
        self.id = random.randint(1,4)
        self.position = Position()

def random_move(robot):
    # la méthode prend un objet robot en paramètre et déplace ce robot
    # d'une case dans une direction aléatoire
    directions = ["up", "down", "left", "right"]
    direction = random.choice(directions)
    if direction == "up":
        if robot.position.y > 0:
            robot.position.deplace(0, -1)
    elif direction == "down":
        if robot.position.y < 720:
            robot.position.deplace(0, 1)
    elif direction == "left":
        if robot.position.x > 0:
            robot.position.deplace(-1, 0)
    elif direction == "right":
        if robot.position.x < 1080:
            robot.position.deplace(1, 0)
