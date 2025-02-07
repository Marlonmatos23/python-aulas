#ler um arquivo mp3 e depois reproduzir
import pygame
pygame.init()
pygame.mixer.music.load('david.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
