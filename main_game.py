import pygame
import time
import random


WIDTH = 500
HEIGHT = 500
STEPSIZE = 10
END_TIME = 60


class Model(object):
    """This is the model that stores the game state. It includes the objects such as the balls (points to be "eaten"),
     and the pacman character that "eats" the balls. as attributes. This gets changed by the controller and drawn by the
       viewer. "
       Inputs: ball objects (3 of them), pacman object, and points
       Makes a model object with these things (ball objects, pacman object, points) as attributes of the object. """
    def __init__ (self, ball, ball2, ball3, pacman, point):
        """" Initialization for model attributes.
        Inputs: ball objects (3 of them), pacman object, and points; creates a model object with these things
        (ball objects, pacman object, points) as attributes of the object. """

        self.ball = ball
        self.ball2 = ball2
        self.ball3 = ball3
        self.pacman = pacman
        self.point = point
        self.clock = pygame.time.Clock
        self.running = True

    def run_time(self):
       game_time = pygame.time.get_ticks()/1000
       t = END_TIME - game_time
       if game_time > END_TIME:
           self.running = False
           t = 0
       return t

    def update(self):
        """  Updates each of the balls in relation to pacman each time the main game loop is run."""
        self.ball.update(self.pacman) #Updates each character each round (?)
        self.ball2.update(self.pacman)
        self.ball3.update(self.pacman)


class Pacman(object):
    """ This is our pacman who eats balls and scores points!"""
    def __init__(self, x, y, radius):
        """Initialization for the attributes of pacman. Inputs: x position, y position, radius of pacman (all in pixels).
        Creates a pacman!"""
        self.x = x #center coordinates/dimensions defining the pacman shape
        self.y = y
        self.radius = radius


class Ball (object):
    """this is the ball that pacman eats, and scores points by eating!"""


    def __init__ (self, x, y, radius,color, value): #Another circle defining the
        """Initialization for the attributes of the ball object. Inputs: x position, y position, radius (all in pixels),
        color, and value (points scored for being eaten)"""
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.value = value

    def update (self, pacman):
        """ Checks to see if pacman is centered under the point - if he is, moves the ball to a new random location
        """
        if self.x == pacman.x and self.y == pacman.y:
            self.x = random.choice(range(0, WIDTH, 10))
            self.y = random.choice(range(0, HEIGHT, 10))
            model.point = model.point + int(self.value)



class Game_Controller (object):
    """
    The controller takes pygame events and changes the model based on the nature of the event)
    """
    def __init__(self,model):
        """Adds the model object being used as a attribute of the controller so that things can actually be controlled"""
        self.model = model
    def handle_event (self, event):
        """ This is the controlled where user input (arrow keys) changes the model"""
        # code in this section HEAVILY modified and extended from http://www.nerdparadise.com/tech/python/pygame/basics/part6/
        # also documentation here: http://www.pygame.org/docs/ref/key.html


        # determine if X was clicked, or Ctrl+W or Alt+F4 was used
        if event.type == pygame.QUIT:
            return
        #If the game quits, none of the below happen.
        if event.type == pygame.KEYDOWN:


        #If ___ key is pressed something is added or subtracted to one of the axis.
            if event.key == pygame.K_UP:
                if model.pacman.y == 0:
                    model.pacman.y = model.pacman.y
                else:
                    model.pacman.y = model.pacman.y - STEPSIZE #For example, going up is going in a positive direction in the y axis (by 1 for 1 press of the key.)


            if event.key == pygame.K_DOWN:
                if model.pacman.y == HEIGHT:
                    model.pacman.y = model.pacman.y
                else:
                    model.pacman.y = model.pacman.y + STEPSIZE

            if event.key == pygame.K_LEFT:
                if model.pacman.x == 0:
                    model.pacman.x = model.pacman.x
                else:
                    model.pacman.x = model.pacman.x - STEPSIZE

            if event.key == pygame.K_RIGHT:
                   if model.pacman.x == WIDTH:
                        model.pacman.x = model.pacman.x
                   else:
                        model.pacman.x = model.pacman.x + STEPSIZE



class PyGameView (object):
    """ Provides a view of the pacman model in a pygame window """
    def __init__(self, model, screen):#background
        """ Initialize with the specified model """
        self.model = model # The model is a model.
        self.screen = screen #The display is equal to the function that define's it's results

    def draw(self):
        """ Draw the game objects (balls, point counter, pacman) on the pygame window. """
 # draw all the bricks to the screen
        if not self.model.running:

            background = pygame.Surface(screen.get_size()) #this is just making a surface because we have to do this uncool thing called blitting to make the text show
            background = background.convert() #increases speed

           #End game (basic code structure from: http://www.pygame.org/docs/tut/tom/games2.html))

            background.fill((0, 0, 0)) #needs to match color
            font = pygame.font.Font(None, 36)
            text = font.render("END GAME! You earned " + str(model.point) + " Points", 1, (255,255,255)) #point.show(points_earned)
            textpos = text.get_rect()
            textpos.centerx = 250
            textpos.centery = 250
            background.blit(text, textpos)
            screen.blit(background, (0, 0))


        else:
            self.screen.fill(pygame.Color('white'))
            background = pygame.Surface(screen.get_size()) #this is just making a surface because we have to do this uncool thing called blitting to make the text show
            background = background.convert() #increases speed
            background.fill((255, 255, 255)) #needs to match color

           #This sequence draws pacman onto the screen with the dimensions we gave earlier.

            pygame.draw.circle(background,
                                (255, 255, 0),
                                (actual_pacman.x, actual_pacman.y),
                                actual_pacman.radius)

           #This draws a dot (we want several, though, right?)

            pygame.draw.circle(background,
                            first_ball.color,
                            (first_ball.x,
                            first_ball.y),
                            first_ball.radius)

            pygame.draw.circle(background, #kill screen use background
                            second_ball.color,
                            (second_ball.x,
                            second_ball.y),
                            second_ball.radius)

            pygame.draw.circle(background,
                            third_ball.color,
                            (third_ball.x,
                            third_ball.y),
                            third_ball.radius)

        # Display some text #http://www.pygame.org/docs/tut/tom/games2.html
        font = pygame.font.Font(None, 36)
        text = font.render('Points: '+str(model.point), 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = WIDTH - 200
        background.blit(text, textpos)
        screen.blit(background, (0, 0))

        font = pygame.font.Font(None, 36)
        text = font.render("POLKA DOTS!", 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = 100
        textpos.centery = HEIGHT - 50
        background.blit(text, textpos)
        screen.blit(background, (0,0))


        font = pygame.font.Font(None, 36)
        text = font.render("Timer: "+str(model.run_time()), 1, (0, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = WIDTH -80
        background.blit(text, textpos)
        screen.blit(background, (0,0))



        pygame.display.update() #update what the player is looking at)

if __name__ == '__main__':
    """ Provides a view of the pacman model in a pygame window """
    # This part starts the display and loads the background. mostly based on floobits brickbreaker
    pygame.init()
    pygame.time.Clock()
    pygame.time.get_ticks()
    pygame.key.set_repeat(50, 50) #https://sivasantosh.wordpress.com/2012/07/18/keyboard-event-handling-pygame/

    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    first_ball = Ball(50, 100,10, pygame.Color('blue'),5)
    second_ball = Ball(300, 200, 15,pygame.Color('green'),10)
    third_ball =  Ball(50, 200, 20,pygame.Color('red'),15)
    actual_pacman = Pacman(60, 70, 50)

    model = Model(first_ball,second_ball,third_ball,actual_pacman,0)
    view = PyGameView(model, screen)
    controller = Game_Controller(model)

    # This part runs the code until it's closed. (QUIT is built in.)
    # MAIN GAME LOOP
    running = True
    while running:
        for event in pygame.event.get(): #get events
            if event.type == pygame.QUIT: #find out if you're quitting, if not
                running = False
            else:
                controller.handle_event(event)  #handle the events (move objects in model from controller input)
        model.update() #update the points and positions of the balls
        view.draw()  #draw these changes
        time.sleep(.001) # wait a tiny bit of time