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
score = 0
coins = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
background = pygame.image.load("AnimatedStreet.png")

screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption("RACE")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)


class Player(pygame.sprite.Sprite):
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


P = Player()
E = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E)
coins_group = pygame.sprite.Group()
coins_group.add(C)

all = pygame.sprite.Group()
all.add(P)
all.add(E)
all.add(C)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(score), True, black)

    coins_text = font_small.render("Coins: " + str(coins), True, black)
    screen.blit(scores, (10, 10))
    screen.blit(coins_text, (width - 100, 10))

    for entity in all:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P, coins_group):
        coins += 1
        coin_hit = pygame.sprite.spritecollide(P, coins_group, True)

    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FPS.tick(fps)
