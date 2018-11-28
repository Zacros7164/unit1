import pygame
from Archer import Archer
# from Monsters import *
from SETTINGS import *

player = Archer()


gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            print event.key
            if event.key == 275:
                player.should_move('right')
            elif event.key == 276:
                player.should_move('left')
            if event.key == 273:
                player.should_move('up')
            elif event.key == 274:
                player.should_move('down')
            # elif event.key == 32:
            #     new_arrow = Arrow(player)
            #     arrows.add(new_arrow)

        elif event.type == pygame.KEYUP:
            print event.key
            if event.key == 275:
                player.should_move('right', False)
            elif event.key == 276:
                player.should_move('left', False)
            if event.key == 273:
                player.should_move('up', False)
            elif event.key == 274:
                player.should_move('down', False)
    pygame_screen.blit(background_image, [0,0])
    player.draw_me()
    pygame_screen.blit(archer_image, [player.x,player.y])
    pygame_screen.blit(wolf_image, [250,250])
    pygame.display.flip()