# 1. include pygame
# we needed pip to get this for us, because python doesn't ship with it
import pygame
from Hero import Hero
from bad_guy import BadGuy
from Arrow import Arrow
# get Group and group collide from the sprite module
from pygame.sprite import Group, groupcollide

# 2. initialize pygame
# Why do we need to do this? because they told us to
pygame.init()

# 3. Make a screen with a size, the size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption('Archer')

# ths is our hero object
theHero = Hero()
# this is our bad guy object
bad_guy = BadGuy()
bad_guys = Group()
bad_guys.add(bad_guy)
# this is a list to hold our arrows (quiver)
# arrows= []
# a group is a special pygame "list" for Sprites
arrows = Group()

# ===========VARIABLES FOR OUR GAME==========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
monster_image = pygame.image.load('monster.png')
goblin_image = pygame.image.load('goblin.png')
arrow_image = pygame.image.load('arrow.png')
# heroLoc = {
#     'x': 0,
#     'y': 0
# }

bg_music = pygame.mixer.Sound('faf.wav')
bg_music.play()

# ==============MAIN GAME LOOP==============
gameOn = True
# the loop will run as long as our bool is True
while gameOn:
    # we are in the game loop from here on out
    # 5. Listen for eventsamd quit if the user clicks the 'x'
    # ==========EVENT CHECKER==========
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # the user clicked the red dot
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            # the user pressed a key
            print event.key
            if event.key == 275:
                # the user pressed the right arrow, AND isn't off the screen! Move the guy right
                # theHero.x += 10
                theHero.should_move('right')
            elif event.key == 276:
                # the user pressed the left arrow , AND isn't off the screen! Move the guy left
                # theHero.x -= 10
                theHero.should_move('left')
            if event.key == 273:
                # the user pressed the up arrow, AND isn't off the screen! Move the guy up
                # theHero.y -= 10
                theHero.should_move('up')
            elif event.key == 274:
                # the user pressed the down arrow, AND isn't off the screen! Move the guy down
                # theHero.y += 10
                theHero.should_move('down')
            elif event.key == 32:
                # space bar = fire!!
                new_arrow = Arrow(theHero)
                arrows.add(new_arrow)

        elif event.type == pygame.KEYUP:
            # the user released a key
            print event.key
            if event.key == 275:
                theHero.should_move('right', False)
            elif event.key == 276:
                theHero.should_move('left', False)
            if event.key == 273:
                theHero.should_move('up', False)
            elif event.key == 274:
                theHero.should_move('down', False)
    # ==========DRAW STUFF==========
    # We use blit to draw on the screen
    # blit = block image transfer
    # blit is a method that takes 2 args:
    # 1. what to draw
    # 2. where to draw it
    # in the docs.... SURFACE(their name) = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    # Draw the hero
    theHero.draw_me()
    pygame_screen.blit(hero_image, [theHero.x, theHero.y])

    # Draw the arrows
    for arrow in arrows:
        arrow.update_me()
        pygame_screen.blit(arrow_image, [arrow.x, arrow.y])

    # inside ()
    # 1. group 1
    # 2. group 2
    # 3. if something in group 1 hits something in group 2, should i remove it from group 1? true = yes
    # 4. if something in group 2 hits something in group 1, should I remove it from group 2? false = no
    arrow_hit= groupcollide(arrows,bad_guys,True,True)
    if arrow_hit:
        bad_guys.add(BadGuy())
    # move the bad guys
    for bad_guy in bad_guys:
        bad_guy.update_me(theHero)
        pygame_screen.blit(monster_image, [bad_guy.x, bad_guy.y])
    pygame.display.flip()