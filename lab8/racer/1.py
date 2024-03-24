import pygame
from pygame.locals import *
import random
import math

pygame.init()
screen = pygame.display.set_mode((400, 600))

pygame.display.set_caption("Racer")
gameon = True

FPS = pygame.time.Clock()

street = pygame.image.load("AnimatedStreet.png")

yourcar = pygame.image.load("Player.png")
ycrect = yourcar.get_rect()

enemycar = pygame.image.load("Enemy.png")
ecrect = enemycar.get_rect()

coin = pygame.image.load("coin.png")
coinrect = coin.get_rect()


xyour = 185
yyour = 500
xenemy = random.randint(10, 350)
yenemy = 0
speed = 3

xcoin = random.randint(25, 375)
ycoin = 0
counter = 0

font = pygame.font.SysFont("Score", 30)


pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

while gameon:
    FPS.tick(60)
    ycrect.x = xyour
    ycrect.y = yyour
    ecrect.x = xenemy
    ecrect.y = yenemy
    coinrect.x = xcoin
    coinrect.y = ycoin
    yenemy += speed
    ycoin += speed

    screen.blit(street, (0, 0))
    screen.blit(yourcar, (xyour, yyour))
    screen.blit(enemycar, (xenemy, yenemy))
    screen.blit(coin, (xcoin, ycoin))

    score = font.render(str(counter), True, (0, 0, 0))
    screen.blit(score, (25, 25))

    if ycoin > 600:
        ycoin = 0
        xcoin = random.randint(10, 350)

    if yenemy > 600:
        yenemy = 0
        xenemy = random.randint(10, 350)
        speed += 0.5

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if xyour > 7:
            xyour -= 5
    if keys[pygame.K_RIGHT]:
        if xyour < 352:
            xyour += 5

    if ycrect.colliderect(ecrect):
        pygame.mixer.music.load("crash.wav")
        pygame.mixer.music.play(-1)
        screen.fill((255, 0, 0))
        score = font.render("YOU LOSED!", True, (0, 0, 0))
        screen.blit(score, (150, 210))
        gameon = False

    if ycrect.colliderect(coinrect):
        ycoin = 0
        xcoin = random.randint(10, 350)
        counter += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            gameon = False
    pygame.display.flip()

    """
    i have commented my code
    """
