import pygame
from SETTINGS import *


class Game(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_capton(TITLE)

    def new(self):
        self.all_sprites = pygame.sprite.Group()

    def update(self):
        self.all_sprites.update()
