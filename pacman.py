import math
import pygame
from pygame.locals import *
from pygame.sprite import Sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


def collisionRadius(joueur, collision):
    if math.sqrt((collision.x - joueur.x) ** 2 + (collision.y - joueur.y) ** 2) <= 28:
        return True
    else:
        return False


pygame.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.queue("music.mp3")
pygame.mixer.music.play()

fenetre = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PacMan")

ch = Sprite()
ch.image = pygame.image.load("contour_haut.png")
ch.rect = ch.image.get_rect()
ch.mask = pygame.mask.from_surface(ch.image)

cb = Sprite()
cb.image = pygame.image.load("contour_bas.png")
cb.rect = cb.image.get_rect()
cb.mask = pygame.mask.from_surface(cb.image)

start = Sprite()
start.image = pygame.image.load("start.png")
start.rect = start.image.get_rect()
start.rect.topleft = (234, 242)
start.mask = pygame.mask.from_surface(start.image)

piece2 = Sprite()
piece2.image = pygame.image.load("piece2.png")
piece2.rect = piece2.image.get_rect()
piece2.rect.topleft = (388, 304)
piece2.mask = pygame.mask.from_surface(piece2.image)

piece6 = Sprite()
piece6.image = pygame.image.load("piece6.png")
piece6.rect = piece6.image.get_rect()
piece6.rect.topleft = (216, 126)
piece6.mask = pygame.mask.from_surface(piece6.image)

piece6b = Sprite()
piece6b.image = pygame.image.load("piece6.png")
piece6b.rect = piece6b.image.get_rect()
piece6b.rect.topleft = (46, 68)
piece6b.mask = pygame.mask.from_surface(piece6b.image)

piece7 = Sprite()
piece7.image = pygame.image.load("piece7.png")
piece7.rect = piece7.image.get_rect()
piece7.rect.topleft = (196, 46)
piece7.mask = pygame.mask.from_surface(piece7.image)

piece8 = Sprite()
piece8.image = pygame.image.load("piece8.png")
piece8.rect = piece8.image.get_rect()
piece8.rect.topleft = (426, 182)
piece8.mask = pygame.mask.from_surface(piece8.image)

piece9 = Sprite()
piece9.image = pygame.image.load("piece9.png")
piece9.rect = piece9.image.get_rect()
piece9.rect.topleft = (252, 46)
piece9.mask = pygame.mask.from_surface(piece9.image)

piece11 = Sprite()
piece11.image = pygame.image.load("piece11.png")
piece11.rect = piece11.image.get_rect()
piece11.rect.topleft = (350, 48)
piece11.mask = pygame.mask.from_surface(piece11.image)

piece12 = Sprite()
piece12.image = pygame.image.load("piece12.png")
piece12.rect = piece12.image.get_rect()
piece12.rect.topleft = (48, 48)
piece12.mask = pygame.mask.from_surface(piece12.image)

piece13 = Sprite()
piece13.image = pygame.image.load("piece13.png")
piece13.rect = piece13.image.get_rect()
piece13.rect.topleft = (154, 192)
piece13.mask = pygame.mask.from_surface(piece13.image)

piece14 = Sprite()
piece14.image = pygame.image.load("piece14.png")
piece14.rect = piece14.image.get_rect()
piece14.rect.topleft = (154, 320)
piece14.mask = pygame.mask.from_surface(piece14.image)

piece15 = Sprite()
piece15.image = pygame.image.load("piece15.png")
piece15.rect = piece15.image.get_rect()
piece15.rect.topleft = (464, 126)
piece15.mask = pygame.mask.from_surface(piece15.image)

piece16 = Sprite()
piece16.image = pygame.image.load("piece16.png")
piece16.rect = piece16.image.get_rect()
piece16.rect.topleft = (446, 48)
piece16.mask = pygame.mask.from_surface(piece16.image)

piece18 = Sprite()
piece18.image = pygame.image.load("piece18.png")
piece18.rect = piece18.image.get_rect()
piece18.rect.topleft = (370, 126)
piece18.mask = pygame.mask.from_surface(piece18.image)

obstacles_group = pygame.sprite.Group()
obstacles_group.add(ch, cb, start, piece2, piece6, piece6b, piece7,
                    piece8, piece9, piece11, piece12, piece13, piece14, piece15, piece16, piece18)


def collideObstacles(sprite):
    bool = False
    for sprites in obstacles_group.sprites():
        if pygame.sprite.collide_mask(sprite, sprites):
            bool = True
    return bool


perso = Player((288, 270), pygame.image.load("perso.png"))
perso.mask = pygame.mask.from_surface(perso.image)
player_group = pygame.sprite.Group()
player_group.add(perso)

ghost = Sprite()
ghost.image = pygame.image.load("fantome.png")
ghost.rect = ghost.image.get_rect()
ghost.rect.topleft = (15, 150)
ghost.mask = pygame.mask.from_surface(ghost.image)
ghosts = pygame.sprite.Group()
ghosts.add(ghost)

pygame.display.flip()
pygame.key.set_repeat(10)

background_accueil = pygame.image.load("background_accueil.jpg")

menu_accueil = 1
menu_jeu = 1

while menu_accueil:
    fenetre.blit(background_accueil, (0, 0))
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                menu_accueil = 0

    pygame.display.flip()

pygame.mixer.music.stop()

while menu_jeu:
    fenetre.fill([0, 0, 0])

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("playing.mp3")
        pygame.mixer.music.play(-1)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                perso.rect = perso.rect.move(0, -2)
                if collisionRadius(perso.rect, ghost.rect) or collideObstacles(perso):
                    perso.rect = perso.rect.move(0, 2)
            elif event.key == K_DOWN:
                perso.rect = perso.rect.move(0, 2)
                if collisionRadius(perso.rect, ghost.rect) or collideObstacles(perso):
                    perso.rect = perso.rect.move(0, -2)
            elif event.key == K_LEFT:
                perso.rect = perso.rect.move(-2, 0)
                if collisionRadius(perso.rect, ghost.rect) or collideObstacles(perso):
                    perso.rect = perso.rect.move(2, 0)
            elif event.key == K_RIGHT:
                perso.rect = perso.rect.move(2, 0)
                if collisionRadius(perso.rect, ghost.rect) or collideObstacles(perso):
                    perso.rect = perso.rect.move(-2, 0)
            elif event.key == K_ESCAPE:
                menu_accueil = 1
                menu_jeu = 0
        if event.type == QUIT:
            menu_accueil = 0
            menu_jeu = 0
    obstacles_group.draw(fenetre)
    player_group.draw(fenetre)
    ghosts.draw(fenetre)
    pygame.display.flip()

pygame.quit()
