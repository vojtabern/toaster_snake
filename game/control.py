import pygame
import sys
import time
import random


def control_x(window, player, x):
    rec_color = [255, 0, 0]
    rect_x = pygame.draw.rect(window, rec_color, pygame.Rect(0, 0, 5, window.get_height()))
    rect_minusx = pygame.draw.rect(window, rec_color, pygame.Rect(window.get_width() - 5, 0, 5, window.get_height()))
    collide_x = player.colliderect(rect_x)
    collide_minusx = player.colliderect(rect_minusx)
    if collide_x:
        x += 5
        return x
    elif collide_minusx:
        x -= 5
        return x
    return x

def control_y(window, player, y):
    re_color = [0, 255, 0]
    rect_y = pygame.draw.rect(window, re_color, pygame.Rect(0, 0, window.get_width(), 5))
    rect_minusy = pygame.draw.rect(window, re_color, pygame.Rect(0, window.get_height() - 5, window.get_width(), 5))
    collide_y = player.colliderect(rect_y)
    collide_minusy = player.colliderect(rect_minusy)
    if collide_y:
        y += 5
        return y
    elif collide_minusy:
        y -= 5
        return y
    return y