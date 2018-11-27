# import pygame

class Hero(object):
    # classes always contain 2 parts
    # 1. __init__ = runs only once
    # 2. methods = run whnever you call them
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 10
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
            if self.x < 480:
                self.x += self.speed
        elif self.should_move_left:
            if self.x > 0:
                self.x -= self.speed
        if self.should_move_down:
            if self.y < 445:
                self.y += self.speed
        elif self.should_move_up:
            if self.y > 0:
                self.y -= self.speed