import pygame

background = pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()

class model(object):
    """This is he model that stores the game state """
    class wall(object):
        """ This is the wall object (that pacman can't go through) in the game """
    class pacman(object):
        """ This is our pacman who dies from ghosts and eats balls!"""
    class ghost(object):
        """ this is a ghost that kills (and maybe chases) pacman"""

    class ball(object):
        """this is the ball that pacman eats and scores points by eating!"""

import pygame
class model(object):
    """This is he model that stores the game state """
    class wall(object):
        """ This is the wall object (that pacman can't go through) in the game """
        def __init__(self, left, top, width, length):
            self.left = left
            self.top = top
            self.width = width
            self.length = length

    class pacman(object):
        """ This is our pacman who dies from ghosts and eats balls!"""
        def __init__(self, x, y, lives):
            self.x = x
            self.y = y
            self.lives = lives

    class ghost(object):
        """ this is a ghost that kills (and maybe chases) pacman"""
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class ball(object):
        """this is the ball that pacman eats and scores points by eating!"""
        def __init__ (self, x, y):
            self.x = x
            self.y = y

    class point(object):
        """ this is what you earn when you collect balls :)"""
        def __init__ (self,number):
            self.number = number
        def add_point(self):
            self.number = self.number + 1
            return self.number # do I need to return this

class controller (object):
    def main_controller (object):
        """ This is the controlled where user input (arrow keys or openCV) changes the model"""
        # code in this section HEAVILY modified and extended from http://www.nerdparadise.com/tech/python/pygame/basics/part6/
        # also documentation here: http://www.pygame.org/docs/ref/key.html
        while True:

            for event in pygame.event.get():

                # determin if X was clicked, or Ctrl+W or Alt+F4 was used
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:# if a key has been pressed
                    if event.key == pygame.K_UP:
                        print 'up'
                        #model.pacman.y = model.pacman.y + 1
                    if event.key == pygame.K_DOWN:
                        print 'down'
                        #model.pacman.y = model.pacman.y - 1
                    if event.key == pygame.K_LEFT:
                        print 'left'
                        #model.pacman.x = model.pacman.x - 1
                    if event.key == pygame.K_RIGHT:
                        print 'right'
                        #model.pacman.y = model.pacman.x + 1

                # determine if a letter key was pressed
                #if event.key == pygame.K_r:
                #    mode = 'red'
                #elif event.key == pygame.K_g:
                #    mode = 'green'
                #elif event.key == pygame.K_b:
                #    mode = 'blue'

class pygameview (object):
   """ This is the game window drawing all of the things that the user seems in response to the changes in the model"""

#def drawGameFrame(boxx, boxy)
#    lef, top = boxCoordinates(boxx,boxy)
#    pygame.draw.rect(DISPLAY, RED, (left-5, top = 5, (60,60), (60,60)))

def testing123 ():
    pygame.init()
    display = pygame.display.set_mode([640, 600])
    red = (230,50,50)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
    window.fill((40,50,180))
    pygame.draw.rect(display, (red), Rect(100,300), (20,30))
    pygame.display.update()


        # screen.blt(background, (0,0))


controller.main_controller()
#testing123()
