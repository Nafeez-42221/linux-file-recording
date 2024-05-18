import pygame
pygame.mixer.init()
pygame.mixer.music.load('\\wsl.localhost\\Ubuntu-22.04\\home\\nafeez \\output3.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
