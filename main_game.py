
import pygame

background = pygame.image.load(bif).convert()
mouse_c=pygame.image.load(mif).convert_alpha()


class model(object):
    """This is he model that stores the game state """
    def update (self):
        self.ball.update()


class pacman(object):
        """ This is our pacman who dies from ghosts and eats balls!"""
    def __init__(self, x, y, radius):
        self.x = x #center coordinates
        self.y = y
        self.radius = radius


class point_rect(object):
    """this is the ball that pacman eats and scores points by eating!"""
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def update (self):

        if self.x = pacman.x and self.y = pacman.y:
           pass #todo: when pacman eats me, disappear

class point(object):
     """ this is what you earn when you collect the point rectangle :)"""
    def __init__ (self,number):
        self.number = number
    def add_point(self):
        self.number = self.number + 1
        return self.number # do I need to return this

class game_controller (object):
    def __init__(self,model ):
        self.model = model
    def handle_event (object):
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
                        #print 'up'
                        self.model.pacman.y = model.pacman.y + 1
                    if event.key == pygame.K_DOWN:
                        #print 'down'
                        self.model.pacman.y = model.pacman.y - 1
                    if event.key == pygame.K_LEFT:
                        #print 'left'
                        self.model.pacman.x = model.pacman.x - 1
                    if event.key == pygame.K_RIGHT:
                        #print 'right'
                        self.model.pacman.y = model.pacman.x + 1


class pygameview (object):
    """ Provides a view of the pacman model in a pygame window """
    def __init__(self, model, size):
        """ Initialize with the specified model """
        self.model = model
        self.screen = pygame.display.set_mode(size)


    def draw(self):
        """ Draw the game to the pygame window """
        # draw all the bricks to the screen
        self.screen.fill(pygame.Color('white'))

        pygame.draw.circle(self.screen,
                           pygame.Color('red'),
                           (self.model.pacman.x, self.model.pacman.y),
                           self.model.pacman.radius)

        r = pygame.Rect(self.model.point.left,
                        self.model.point.top,
                        self.model.point.width,
                        self.model.point.height)
        pygame.draw.rect(self.screen, pygame.Color('orange'), r)
        pygame.display.update()





#def drawGameFrame(boxx, boxy)
#    lef, top = boxCoordinates(boxx,boxy)
#    pygame.draw.rect(DISPLAY, RED, (left-5, top = 5, (60,60), (60,60)))

#def testing123 ():
#    pygame.init()
#    display = pygame.display.set_mode([640, 600])
#    red = (230,50,50)
#    while True:
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#    window.fill((40,50,180))
#    pygame.draw.rect(display, (red), Rect(100,300), (20,30))
#    pygame.display.update()


        # screen.blt(background, (0,0))


if __name__ == '__main__':
    pygame.init()
    size = (640, 480)
    model = model()
    view = pygameview(model, size)
    controller = game_controller(model)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            else:
                game_controller.handle_event(self,event)
        model.update()
        view.draw()
        time.sleep(.001) #todo: initialize all locations of pacman, ball AND make something appropriate happen when pacman eats a ball
