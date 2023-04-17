

import random

def deplace(robot):
    deplacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # choix aléatoire d'un déplacement
    deplacement = random.choice(deplacements)
    robot.position.deplace(*deplacement)
