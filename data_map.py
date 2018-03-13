import pygame

class View(object):
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
        bg = pygame.image.load("heatmap.png")
        bg = pygame.transform.scale(bg,self.size)
        self.screen.blit(bg, [0,0])
        # bg.blit()
        pygame.display.update()

    def display_info(self,info):
        self.drawing = pygame.draw.rect(info.surf,info.color,info.rect,info.rect.width)
        self.screen.blit(info.surf, self.drawing)
        pygame.display.update()

class Infobutton(object):
    def __init__(self, state, left, top, width, height):
        self.state = state
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width,self.height))
        self.color = 255,0,0
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)
        self.rect.width = 0

    #def __str__(self):
        #return "State=%s, size=%f by %f, position=(%f,%f)" % (self.state,
                                                             # self.dim,
                                                              #self.dim,
                                                              #self.x,
                                                              #self.y)






if __name__ == "__main__":

    pygame.init()
    size = (1100, 700)
    view = View(size)
    while True:
        view.draw()
        washington = Infobutton('Washington', 130, 55, 25, 20)
        view.display_info(washington)
