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

    # def button(self,x,y,w,h,action=None):
    #     mouse = pygame.mouse.get_pos()
    #     click =
    #     return mouse
    #     #x,y,w,h,action=None

    #def __str__(self):
        #return "State=%s, size=%f by %f, position=(%f,%f)" % (self.state,
                                                             # self.dim,
                                                              #self.dim,
                                                              #self.x,
                                                              #self.y)

class Infocard(object):
    def __init__(self,msg):
        self.msg = msg
        self.left = 300
        self.top = 300
        self.width = 400
        self.height = 250
        self.surf = pygame.Surface((self.width,self.height))
        self.color = 255,255,255
        self.surf.fill(self.color)
        self.rect = pygame.Rect(self.left,self.top,self.width,self.height)

    def draw(self,view):
        self.card = pygame.draw.rect(self.surf,self.color,self.rect,self.rect.width)
        view.screen.blit(self.surf, self.card)
        pygame.display.update()

        textSurf, textRect = text_objects(self.msg, smallText)
        textRect.center = (self.left + (self.width/2),(self.top - (self.height/2)))
        view.screen.blit(textSurf, textRect)
        pygame.display.update()



def text_objects(text,font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()



def find_state(x,y):
    # if 130+20 > x > 130 and 55+20 > y > 55:
    if 130 < x < 130+20 and 55 < y < 55+20:
        return 'Washington'
    else:
        return 'Not Found'



if __name__ == "__main__":


    pygame.init()
    size = (1100, 700)
    view = View(size)
    view.draw()
    washington = Infobutton('Washington', 130, 55, 20, 20)
    view.display_info(washington)

    smallText = pygame.font.SysFont("comicsansms",20)


    while True:
        # print(washington.button())


        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                state = find_state(mouse[0], mouse[1])
                if state == 'Washington':
                    wa_card = Infocard('the facts')
                    wa_card.draw(view)
                #print (mouse[1])

                # print(find_state(mouse[0],mouse[1]))
