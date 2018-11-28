import pygame
from pygame.sprite import Sprite
from SETTINGS import *

class Arrow(Sprite):
    def __init__(self, archer):
        Sprite.__init__(self)
        self.x = archer.x - 15
        self.y = archer.y
        self.speed = -10
        self.rect = pygame.Rect(0,0,23,14)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.arrows = []
        self.arrows.append(arrow_image)
        self.arrows.append(arrow_image)
        self.arrows.append(arrow_image)
        self.arrows.append(arrow_image)
        self.img = self.arrows[0]
        self.cur_arrow = 0
        self.power = 5

    def draw_me(self):
        self.x -= self.speed

    def update_me(self):
        self.cur_arrow += 1
        if self.cur_arrow == 4:
            self.cur_arrow = 0
        self.img = self.arrows[self.cur_arrow]
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y