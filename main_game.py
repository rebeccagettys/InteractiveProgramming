import pygame
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
class controller (object):
    """ This is the controlled where user input (arrow keys or openCV) changes the model"""

class pygameview (object):
    """ This is the game window drawing all of the things that the user seems in response to the changes in the model"""