import pygame, sys

background = pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()
class model(object):
    """This is he model that stores the game state """

    class wall(object):
        """ This is the wall object (that pacman can't go through) in the game """

    class pacman(object):
        """ This is our pacman who dies from ghosts and eats balls!"""
        def load_image(self, image_name)


    class ghost(object):
        """ this is a ghost that kills (and maybe chases) pacman"""

    class ball(object):
        """this is the ball that pacman eats and scores points by eating!"""
        
class controller (object):
    """ This is the controlled where user input (arrow keys or openCV) changes the model"""

class pygameview (object):
    """ This is the game window drawing all of the things that the user seems in response to the changes in the model"""

def drawGameFrame(boxx, boxy) 
    lef, top = boxCoordinates(boxx,boxy)
    pygame.draw.rect(DISPLAY, RED, (left-5, top = 5, (60,60), (60,60))) 

pygame.init() 
DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello Pygame!')
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit 
 

    #     screen.blt(background, (0,0))
