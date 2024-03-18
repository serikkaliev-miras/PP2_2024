import pygame
from pygame.locals import *

pygame.init()
i = 0
songs = ["song1.mp3",
         "song2.mp3"]
pygame.mixer.music.load(songs[i])
# pygame.mixer.music.load("labs/tsis 7/music player/song2.mp3")
pygame.mixer.music.play(0)
# prevb = pygame.image.load("labs/tsis 7/music player/prev.png")
# nextb = pygame.image.load("labs/tsis 7/music player/next.png")
# pauseb = pygame.image.load("labs/tsis 7/music player/pause.png")
# playb = pygame.image.load("labs/tsis 7/music player/play.png")
# iface = pygame.image.load("labs/tsis 7/music player/interface.png")

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")
gameon = True
print(len(songs))
while gameon:
    screen.fill((255, 255, 255))
    # screen.blit(iface,(0,0))
    # screen.blit(prevb,(0,0))
    # screen.blit(nextb,(0,0))
    # screen.blit(pauseb,(0,0))
    # screen.blit(playb,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # pause on space
                pygame.mixer.music.pause()
            if event.key == pygame.K_u:  # unpause
                pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:  # next
                if i < len(songs)-1:
                    i += 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
            if event.key == pygame.K_LEFT:  # prev
                if i > 0:
                    i -= 1
                    pygame.mixer.music.load(songs[i])
                    pygame.mixer.music.play(0)
        if event.type == QUIT:
            gameon = False
    pygame.display.flip()
