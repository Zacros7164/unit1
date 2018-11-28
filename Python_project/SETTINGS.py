import pygame
import os

screen_size = (960,544)
pygame_screen = pygame.display.set_mode(screen_size)

TITLE = "Castle Defense"


# =====IMAGES=====
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
background_image = pygame.image.load(os.path.join(img_folder, 'castle_defense.png'))
archer_image = pygame.image.load(os.path.join(img_folder, 'archer_1.png'))
wolf_image = pygame.image.load(os.path.join(img_folder, 'wolf_1.png'))