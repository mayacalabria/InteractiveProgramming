import pygame

class View(object):
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, size):
        """ Initialize the view with a reference to the model and the
            specified screen dimensions (represented as a tuple
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
        """ Display a an Infobutton object on the map screen """
        self.drawing = pygame.draw.rect(info.surf,info.color,info.rect,info.rect.width)
        self.screen.blit(info.surf, self.drawing)
        pygame.display.update()



class State(object):
    """ Creates red square at the specified location to represent a click zone for
    each state.

    state: string with name of state
    left: leftmost coordinate
    top: topmost coordinate
    width: distance from left
    height: distance from top
    """
    def __init__(self, state, left, top, width = 20, height = 20):
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



class Infocard(object):
    def __init__(self,msg,color=(200,200,200)):
        self.msg = msg
        self.left = 850
        self.top = 400
        self.width = 200
        self.height = 280
        self.surf = pygame.Surface((self.width,self.height))
        self.color = color
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,image):
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        info = pygame.image.load(image)
        view.screen.blit(info,self.card)
        pygame.display.update()




def text_objects(text,font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


def find_state(pos,states):
    for state in states:
        left = state.left
        top = state.top
        if (left < pos[0] < left + 20) and (top < pos[1] < top + 20):
            return state.state
    return 'White'





if __name__ == "__main__":

    # creating the map screen
    pygame.init()
    size = (1100, 700)
    view = View(size)
    view.draw()

    # instantiating the State classes
    washington = State('Washington', 130, 55)
    wyoming = State('Wyoming', 360, 155)
    texas = State('Texas',515,410)
    cali = State('California',150,300)
    mass = State('Massachusetts',985,178,10,10)
    arizona = State('Arizona',285,350)
    florida = State('Florida',810,480)
    penn = State('Pennsylvania',880,205)
    scarolina = State('SouthCarolina',825,355)
    alabama = State('Alabama',775,375)
    states = [washington,wyoming,texas,cali,mass,arizona,florida,penn,scarolina,alabama]
    for state in states:
        view.display_info(state)


    smallText = pygame.font.SysFont("comicsansms",30)


    while True:
        # print(washington.button())


        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                state = find_state(mouse,states)
                info_card = Infocard(state)
                info_card.draw(state+'.png')
