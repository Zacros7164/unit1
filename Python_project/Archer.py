import pygame
from pygame.sprite import Sprite

class Archer(Sprite):
    def __init__(self):
        super(Archer, self).__init__
        self.health = 10
        self.x = 920
        self.y = 200
        self.yspeed = 10
        self.xspeed = 8
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_left = False
        self.should_move_right = False

    def should_move(self,direction,start = True):
        if direction == 'right':
            self.should_move_right = start
        if direction == 'left':
            self.should_move_left = start
        if direction == 'down':
            self.should_move_down = start
        if direction == 'up':
            self.should_move_up = start

    def draw_me(self):
        if self.should_move_right:
            if self.x < 925:
                self.x += self.xspeed
        elif self.should_move_left:
            if self.x > 915:
                self.x -= self.xspeed
        if self.should_move_down:
            if self.y < 400:
                self.y += self.yspeed
        elif self.should_move_up:
            if self.y > 185:
                self.y -= self.yspeed