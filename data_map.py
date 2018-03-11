import pygame

class PyGameWindowView(object):
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height """

        self.screen = pygame.display.set_mode(size)
        self.size = size

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pygame.Color(0,0,0))
        bg = pygame.image.load("us_map.jpg")
        bg = pygame.transform.scale(bg,self.size)
        self.screen.blit(bg, [0,0])
        pygame.display.update()


class Infobox(object):
    def __init__(self,state,dim,x,y):
        self.state = state
        self.dim = dim
        self.x = x
        self.y = y

    def __str__(self):
        return "State=%s, size=%f by %f, position=(%f,%f)" % (self.state,
                                                              self.dim,
                                                              self.dim,
                                                              self.x,
                                                              self.y)
    def draw(self,window):
        ### how can I draw onto an already existing screen
        






if __name__ == "__main__":

    pygame.init()
    size = (1100, 700)
    view = PyGameWindowView(size)
    while True:
        view.draw()
    washington = Infobox('Washington',20,50,50)
    print(washington)
