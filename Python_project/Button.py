import pygame.font
import pygame

class Start_Button(object):
    def __init__(self,screen):
        # print "Start Button"
        # get the screen and save it to this object
        self.screen = screen
        # how big is the screen? we ned a rect
        self.screen_rect = screen.get_rect()
        # set the width of the button imafge
        self.width = 350
        self.height = 100
        # set some colors
        # R,G,B 0-255
        # all 255 is white
        # all 0 is black
        self.button_color = 8,34,86
        self.text_color = 130,58,29
        self.font = pygame.font.Font(None,52)
        # set the rectangle of the button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        # set the location of the rectangle
        self.rect.center = self.screen_rect.center
        # setup the message
    def setup_message(self):
        self.image_message = self.font.render("Defend the Castle!",True,self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center
    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color,self.rect)
        # draw the button
        self.screen.blit(self.image_message,self.image_message_rect)