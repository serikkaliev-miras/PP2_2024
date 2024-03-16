import pygame
import sys

width = 400
height = 350
red = (255, 0, 0)
white = (255, 255, 255)
radius = 20
global x
global y
clock = pygame.time.Clock()


def game():
    x = width // 2
    y = height // 2
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > radius:
            x -= 20
        if keys[pygame.K_RIGHT] and x < width - radius:
            x += 20
        if keys[pygame.K_UP] and y - radius > 0:
            y -= 20
        if keys[pygame.K_DOWN] and y < height - radius:
            y += 20
        screen.fill(white)
        pygame.draw.circle(screen, red, (x, y), radius)
        pygame.display.flip()
        clock.tick(60)


pygame.quit()
game()
