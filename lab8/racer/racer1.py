import pygame
import sys
import random
from pygame.locals import *
pygame.init()
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

fps = 60
FPS = pygame.time.Clock()

width = 400
height = 600
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("RACE")


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move1(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move2(self):
        p_k = pygame.key.get_pressed()
        if self.rect.left > 0:
            if p_k[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if p_k[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


P = player()
E = enemy()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P.move2()
    E.move1()

    screen.fill(white)
    P.draw(screen)
    E.draw(screen)

    pygame.display.update()
    FPS.tick(fps)
