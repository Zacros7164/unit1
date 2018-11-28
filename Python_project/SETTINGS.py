import pygame
import os

screen_size = (960,544)
pygame_screen = pygame.display.set_mode(screen_size)

TITLE = "Castle Defense"

width = 46
height = 45
white = (255,255,255)
red = (255,0,0)
wallx = 897
wally = 185

# =====IMAGES=====
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
wolf_folder = os.path.join(img_folder, 'wolf man')
sounds_folder = os.path.join(game_folder, 'sounds')
# print wolf_folder
background_image = pygame.image.load(os.path.join(img_folder, 'castle_defense.png'))
archer_image = pygame.image.load(os.path.join(img_folder, 'archer_1.png'))
wolf_image = pygame.image.load(os.path.join(wolf_folder, 'wolf_1.png'))
arrow_image = pygame.image.load(os.path.join(img_folder, 'arrow1.png'))
wolf_images= [
    pygame.image.load(os.path.join(wolf_folder, 'wolf_1.png')),
    pygame.image.load(os.path.join(wolf_folder, 'wolf_2.png')),
    pygame.image.load(os.path.join(wolf_folder, 'wolf_3.png')),
    pygame.image.load(os.path.join(wolf_folder, 'wolf_4.png'))

]
