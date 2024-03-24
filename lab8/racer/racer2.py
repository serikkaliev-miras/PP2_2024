import pygame
import sys
import random
import time
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
speed = 5

screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("RACE")


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    # def draw(self, surf):
    #     surf.blit(self.image, self.rect)


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        p_k = pygame.key.get_pressed()
        if self.rect.left > 0:
            if p_k[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if p_k[K_RIGHT]:
                self.rect.move_ip(5, 0)

    # def draw(self, surf):
    #     surf.blit(self.image, self.rect)


P = player()
E = enemy()

enemies = pygame.sprite.Group()
enemies.add(E)
all = pygame.sprite.Group()
all.add(P)
all.add(E)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(white)

    for entity in all:
        screen.blit(entity.image, entity.rect)
        entity.move()
    # P.move2()
    # E.move1()
    # P.draw(screen)
    # E.draw(screen)

    if pygame.sprite.spritecollideany(P, enemies):
        screen.fill(red)
        pygame.display.update()
        for entity in all:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FPS.tick(fps)
