import pygame
from Archer import Archer
from Monsters import *
from SETTINGS import *
from Arrow import Arrow
from pygame.sprite import Group, groupcollide
from Wall import Wall

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
tick = 0 
gameOn = True
while gameOn:
    tick += 1
    if tick % 120 == 0:
        monsters.add(Wolf())
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
                player.attack()
                new_arrow = Arrow(player)
                arrows.add(new_arrow)

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
    bg_music = pygame.mixer.Sound('music.wav')
    bg_music.play()
    for wolf in monsters:
        wolf.draw_me()
        pygame_screen.blit(wolf.image, [wolf.x,wolf.y])
    for arrow in arrows:
        arrow.update_me()
        pygame_screen.blit(arrow.image, [arrow.x, arrow.y])
    arrow_hit= groupcollide(arrows,monsters,True,True)
    if arrow_hit:
        monsters.add(Wolf())
    monster_hit = groupcollide(monsters, walls, False, False)
    # print monster_hit
    if monster_hit:
        # for wolf in monsters:
        for attack_wolf in monster_hit:
            attack_wolf.attack()
            if wolf.image == wolf_images[0]:
                print "hello"
                wall.take_damage(wolf.power)
                print wall.health

    if not wall.is_alive():
        gameOn = False
    # pygame_screen.blit(wall.img, [wall.x, wall.y])
    pygame.display.flip()