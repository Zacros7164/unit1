import pygame
from Archer import Archer
from Monsters import *
from SETTINGS import *
from Arrow import Arrow
from pygame.sprite import Group, groupcollide
from Wall import Wall
from Button import Start_Button

player = Archer()
monsters = pygame.sprite.Group()
wolf = Wolf()
monsters.add(wolf)
# new_arrow = Arrow(player)
arrows =Group()
wall = Wall()
walls = Group()
walls.add(wall)
pygame.init()
pygame.mixer.init()
start_button = Start_Button(pygame_screen)
tick = 0 
gameOn = True
game_start = False
bg_music_sound = pygame.mixer.Sound('music.wav')
shoot_sound = pygame.mixer.Sound('shoot.wav')

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
            elif event.key == 32:
                new_arrow = Arrow(player)
                arrows.add(new_arrow)
                pygame.mixer.Channel(1).play(shoot_sound)
                

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # print mouse_x,mouse_y;
            if start_button.rect.collidepoint(mouse_x, mouse_y):
                game_start = True
                # pygame.mixer.Channel(0).play(bg_music_sound)
                bg_music_sound.set_volume(0.3)
                bg_music_sound.play()

    pygame_screen.blit(background_image, [0,0])
    if game_start == True:
        tick += 1
        if tick % 120 == 0:
            monsters.add(Wolf())
        player.draw_me()
        pygame_screen.blit(archer_image, [player.x,player.y])
        # pygame.mixer.Channel(0).play(bg_music_sound)
        bg_music_sound.set_volume(0.3)
        bg_music_sound.play()
        for wolf in monsters:
            wolf.draw_me()
            pygame_screen.blit(wolf.img, [wolf.x,wolf.y])
        for arrow in arrows:
            arrow.update_me()
            pygame_screen.blit(arrow.img, [arrow.x, arrow.y])
        arrow_hit= groupcollide(arrows,monsters,True,True)
        if arrow_hit:
            monsters.add(Wolf())
        monster_hit = groupcollide(monsters, walls, False, False)
        # print monster_hit
        if monster_hit:
            # for wolf in monsters:
            for attack_wolf in monster_hit:
                attack_wolf.attack()
                if wolf.img == wolf_images[0]:
                    print "hello"
                    wall.take_damage(wolf.power)
                    print wall.health
    if game_start == False:
        start_button.setup_message()
        start_button.draw_button()

    if not wall.is_alive():
        gameOn = False
    # pygame_screen.blit(wall.img, [wall.x, wall.y])
    pygame.display.flip()
