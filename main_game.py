import pygame
import time
import random 

bif = 'background_3.png'
mif = 'arrow-small-right.png'

class model(object):
    """This is he model that stores the game state """
    def __init__ (self, ball, pacman): 
        self.ball = ball
        self.pacman = pacman
        self.point = point 

    def update(self):
        # self.ball = ball #sets the ball equal to the equation that defines it 
        # self.pacman = pacman #Defines the pacman by its equation. 
        self.ball.update(self.pacman) #Updates each character each round (?)
        # self.point = point


class pacman(object):
    """ This is our pacman who dies from ghosts and eats balls!"""
    def __init__(self, x, y, radius):
        self.x = x #center coordinates/dimensions defining the pacman shape
        self.y = y
        self.radius = radius 
        #Liv: Is pacman currently a ball? Should we make him into a sprite?


class ball (object):
    """this is the ball that pacman eats and scores points by eating!"""

    def __init__ (self, x, y, radius): #Another circle defining the 
        self.x = x
        self.y = y
        self.radius = radius 

    def update (self, pacman):

        if self.x == pacman.x and self.y == pacman.y:
           self.radius = 0 #todo: when pacman eats me, disappear 
           #More specifically, when the Pacman is the same 

class point(object):
    """ this is what you earn when you collect the point rectangle :)"""
    def __init__ (self,number):
        self.number = number # Making an initial number.
    def add_point(self):
        self.number = self.number + 1 #Adding to this 
        #(and making a function out of it so we can use it later independently of the class.)
        return self.number # do I need to return this

class game_controller (object):
    def __init__(self,model):
        self.model = model #Creating a model. (What's that? Just an overarching structure?)
    def handle_event (self, event):
        """ This is the controlled where user input (arrow keys or openCV) changes the model"""
        # code in this section HEAVILY modified and extended from http://www.nerdparadise.com/tech/python/pygame/basics/part6/
        # also documentation here: http://www.pygame.org/docs/ref/key.html
        #while True:

        #for event in pygame.event.get():

        # determine if X was clicked, or Ctrl+W or Alt+F4 was used
        if event.type == pygame.QUIT:
            return
        #If the game quits, none of the below happen. 
        if event.type == pygame.KEYDOWN:
        #If ___ key is pressed something is added or subtracted to one of the axis. 
            if event.key == pygame.K_UP:
                #print 'up'
                model.pacman.y = model.pacman.y - 10 #For example, going up is going in a positive direction in the y axis (by 1 for 1 press of the key.)
            if event.key == pygame.K_DOWN:
                #print 'down'
                model.pacman.y = model.pacman.y + 10
            if event.key == pygame.K_LEFT:
                #print 'left'
                model.pacman.x = model.pacman.x - 10
            if event.key == pygame.K_RIGHT:
                #print 'right'
                model.pacman.x = model.pacman.x + 10


class pygameview (object):
    """ Provides a view of the pacman model in a pygame window """
    def __init__(self, model, screen): 
        """ Initialize with the specified model """
        self.model = model # The model is a model. 
        self.screen = screen #The display is equal to the function that define's it's results

    def draw(self):
        """ Draw the game to the pygame window """
        # draw all the bricks to the screen
        self.screen.fill(pygame.Color('white'))

        #This sequence draws pacman onto the screen with the dimensions we gave earlier.

        pygame.draw.circle(self.screen,
                           (255, 0, 0),
                           (self.model.pacman.x, self.model.pacman.y),
                           self.model.pacman.radius)

        #This draws a dot (we want several, though, right?)

        pygame.draw.circle(self.screen, 
                        (0, 0, 255),
                        (self.model.ball.x,
                        self.model.ball.y), 
                        self.model.ball.radius) 

        pygame.display.update()

if __name__ == '__main__':
    """ Provides a view of the pacman model in a pygame window """
    # This part starts the display and loads the background. 
    pygame.init()
    # pygame.display.init()
    screen = pygame.display.set_mode([1000,1000]) #Starting the display using bif and mif
    # background = pygame.image.load(bif).convert()
    # mouse_c= pygame.image.load(mif).convert_alpha()
   
    model = model(ball(50,50,50), pacman(60, 70, 50))
    view = pygameview(model, screen)
    controller = game_controller(model)

    # This part runs the code until it's closed. (QUIT is built in.)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                controller.handle_event(event)
        model.update()
        view.draw() 
        time.sleep(.001) #todo: initialize all locations of pacman, ball AND make something appropriate happen when pacman eats a ball

    # def __init__(self, model, size):
    #     """ Initialize with the specified model """
    #     self.model = model
    #     self.screen = pygame.display.set_mode(size)



