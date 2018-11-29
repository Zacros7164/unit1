import pygame
from pygame.sprite import Sprite
from SETTINGS import *
import random
import time
class Wall(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.x = wallx
        self.y = wally
        # self.img = pygame.Surface((50,250))
        self.rect = pygame.Rect(0,0,50,250)
        # self.rect = self.img.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        # self.img.fill(white)
        self.health = 3500
    def take_damage(self,monster_power):
        self.health -= monster_power
        # time.sleep(1)
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    # def draw_me(self):
