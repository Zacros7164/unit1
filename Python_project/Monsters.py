import pygame
from pygame.sprite import Sprite
from SETTINGS import *
import random


class Monster(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # self.game = game
        randY = random.randint(185,400)
        self.y = randY
        self.x = 0
        self.speed = 15
        self.power = 5


class Wolf(Monster):
    def __init__(self):
        Monster.__init__(self)
        # self.image = pygame.Surface((46,45))
        self.img = wolf_image
        self.rect = pygame.Rect(0,0,46,45)
        # self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        # self.image.fill(red)
        # self.power = 5
        self.cur_img = 0
        self.tick = 0
    
    def draw_me(self):
        if self.x < 850:
            self.x += self.speed
            self.rect.x = self.x

    def attack(self):
        if self.cur_img == (len(wolf_images) - 1):
            self.cur_img = 0
        if self.tick % 5 == 0:
            self.img = wolf_images[self.cur_img]
            self.cur_img += 1
        # print self.cur_img
        self.tick += 1
        # if self.cur_img == (len(wolf_images) - 1):
        #     self.cur_img == 0

