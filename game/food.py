import keyword

import pygame
import sys
import time
import random

def spawnfood (screen, width_x, height_y, jidlo):
    x = random_x(width_x)
    y = random_y(height_y)
    pygame.draw.rect(screen, [255, 0, 0], (x, y, 5, 5))

def random_x(width_x):
    x = random.randint(0 + 6, width_x - 6)
    return x

def random_y(height_y):
    y = random.randint(0 + 6, height_y - 6)
    return y