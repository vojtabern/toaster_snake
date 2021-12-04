import keyword

import pygame
import sys
import time
import random
from character import texture
from control import *
from food import *


def display():
    player = texture()
    color = [0, 0, 0]
    pygame.init()
    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    window = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Keyboard_Input")
    fps = 30
    fpsclock = pygame.time.Clock()
    x = window.get_height() / 2
    y = window.get_width() / 2
    step = 5
    player_texture = window.blit(player, (x, y, 50, 50))
    jidlo = 0
    while True:
        keys = pygame.key.get_pressed()
        window.fill(color)
        spawnfood(window, window.get_width(), window.get_height(), jidlo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

            elif keys:
                if keys[pygame.K_w]:
                    y -= step
                if keys[pygame.K_s]:
                    y += step
                if keys[pygame.K_d]:
                    x += step
                if keys[pygame.K_a]:
                    x -= step

            #pygame.draw.rect(window, rec_color, pygame.Rect(x, y, 50, 50))
            #spawnfood(window, window.get_width(), window.get_height(), jidlo)

            x = control_x(window, player_texture, x)
            y = control_y(window, player_texture, y)
            player_texture = window.blit(player,(x, y, 50, 50))

            pygame.display.flip()
            pygame.display.update()
            fpsclock.tick(fps)
        jidlo += 1

display()