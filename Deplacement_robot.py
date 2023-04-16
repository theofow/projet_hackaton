import pygame
from class_lib import *
import time
from random import randint

def random_movement(robot):
    # Déplacement aléatoire du robot
    direction = randint(1, 4)

    if direction == 1:
        robot.position.deplace(5, 0)
    elif direction == 2:
        robot.position.deplace(-5, 0)
    elif direction == 3:
        robot.position.deplace(0, 5)
    elif direction == 4:
        robot.position.deplace(0, -5)