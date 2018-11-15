# Include pygame
import pygame

# Init pygame
# In order to use pygame we have to run the init method
pygame.init()

# Create a screen with a size
# the screen size MUST be a tuple
screen_size = (512,480)
# Actually tell pygame to set the screen up and store it
# so pygame can uae it
pygame_screen = pygame.display.set_mode(screen_size)

# set the title of the window
pygame.display.set_caption('Goblin Chase')

# ==== VARIABLES FOR OUR GAME ====
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
monster_image = pygame.image.load('monster.png')


# Create the game loop (while 1)
# creat a boolean for whether the game should run or not
game_on= True
while game_on:
    # we are inside the main game loop
    # it will keep running as long as our boolean is True

    # Add a quit event (requires sys)
    # pygame comes with an event loop (like JS)
    for event in pygame.event.get():
        # we need to give pygame a way out.
        # if we dont.... Python is going to FREAK out
        # because it is inside an infinite loop
        if(event.type == pygame.QUIT):
            game_on = False

# Screen.fill (pass bg_color)
    # we want to draw on the screen
    # we are going to ue blit (block image transfer)
    # blit is a function and takes 2 arguments
    # 1. what do you want to draw?
    # 2. where do you want to draw it?
    pygame_screen.blit(background_image,[0,0])

    # Flip the screen and start over
    pygame.display.flip()