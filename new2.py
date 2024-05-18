import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\Windows\\Downloads\\La La La Li La La La ! Bgm ! Arabic.mp3')
pygame.mixer.music.play()
pygame.event.wait()
