"""Programa deve executar arquivo mp3 """

import pygame
pygame.init()
pygame.mixer.music.load('classic.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#programa que abre e reproduza o audio de arquivo MP3

