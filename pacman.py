import pygame, math
from pygame.locals import *
from pygame.sprite import Sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


def collision(rectA, rectB):
    if rectB.right < rectA.left:
        return False
    if rectB.bottom < rectA.top:
        return False
    if rectB.left > rectA.right:
        return False
    if rectB.top > rectA.bottom:
        return False
    if rectA.center > rectB.center:
        return False
    return True


def collisionBackground(joueur, collision):
    if math.sqrt((collision.x - joueur.x) ** 2 + (collision.y - joueur.y) ** 2) <= 28:
        return True
    else:
        return False


pygame.init()

fenetre = pygame.display.set_mode((600, 600))
background = pygame.image.load("map.jpg")
fenetre.blit(background, (0, 0))
pygame.display.set_caption("PacMan")

perso = Player((20, 20), pygame.image.load("perso.png"))
player_group = pygame.sprite.Group()
player_group.add(perso)

perso1 = Sprite()
perso1.image = pygame.image.load("fantome.png")
perso1.rect = perso1.image.get_rect()
perso1.rect.topleft = (50, 50)
pygame.display.flip()
pygame.key.set_repeat(10)

ghosts = pygame.sprite.Group()
ghosts.add(perso1)

continuer = 1
while continuer:
    fenetre.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                new_rect = perso.rect.move(0, -2)
                if not collisionBackground(new_rect, perso1.rect):
                    perso.rect = new_rect
            if event.key == K_DOWN:
                new_rect = perso.rect.move(0, 2)
                if not collisionBackground(new_rect, perso1.rect):
                    perso.rect = new_rect
            if event.key == K_LEFT:
                new_rect = perso.rect.move(-2, 0)
                if not collisionBackground(new_rect, perso1.rect):
                    perso.rect = new_rect
            if event.key == K_RIGHT:
                new_rect = perso.rect.move(2, 0)
                if not collisionBackground(new_rect, perso1.rect):
                    perso.rect = new_rect
        if event.type == QUIT:
            continuer = 0
    player_group.draw(fenetre)
    ghosts.draw(fenetre)
    pygame.display.update()
