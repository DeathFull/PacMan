import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((600, 600))
background = pygame.image.load("./map.jpg")
fenetre.blit(background, (0, 0))

perso = pygame.image.load("perso.png")
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

pygame.display.flip()
pygame.key.set_repeat(400, 30)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                position_perso = position_perso.move(0, -3)
            if event.key == K_DOWN:
                position_perso = position_perso.move(0, 3)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-3, 0)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(3, 0)
        if event.type == QUIT:
            continuer = 0
    fenetre.blit(background, (0, 0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()