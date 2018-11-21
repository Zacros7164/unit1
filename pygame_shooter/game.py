# 1. include pygame
# we needed pip to get this for us, because python doesn't ship with it
import pygame

# 2. initialize pygame
# Why do we need to do this? because they told us to
pygame.init()

# 3. Make a screen with a size, the size MUST be a tuple
screen_size = (512,480)
pygame_screen = pygame.display.set_mode(screen_size)
# set the title of the window that opens...
pygame.display.set_caption('Archer')

# ===========VARIABLES FOR OUR GAME==========
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
monster_image = pygame.image.load('monster.png')
goblin_image = pygame.image.load('goblin.png')
arrow_image = pygame.image.load('arrow.png')
heroLoc = {
    'x': 0,
    'y': 0
}
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
            if event.key == 275 and heroLoc['x'] < 480:
                # the user pressed the right arrow, AND isn't off the screen! Move our dude right
                heroLoc['x'] += 10
            if event.key == 276 and heroLoc['x'] > 0:
                # the user pressed the left arrow , AND isn't off the screen! Move the guy left
                heroLoc['x'] -= 10
            if event.key == 273 and heroLoc['y'] > 0:
                # the user pressed the up arrow, AND isn't off the screen! Move the guy up
                heroLoc['y'] -= 10
            if event.key == 274 and heroLoc['y'] < 512:
                # the user pressed the down arrow, AND isn't off the screen! Move the guy down
                heroLoc['y'] += 10
    # ==========DRAW STUFF==========
    # We use blit to draw on the screen
    # blit = block image transfer
    # blit is a method that takes 2 args:
    # 1. what to draw
    # 2. where to draw it
    # in the docs.... SURFACE(their name) = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    pygame_screen.blit(hero_image, [heroLoc['x'], heroLoc['y']])
    pygame.display.flip()
