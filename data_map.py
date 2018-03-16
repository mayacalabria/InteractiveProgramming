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



class Infobutton(object):
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



def find_state(x,y):
    if 130 < x < 130+20 and 55 < y < 55+20:
        return 'Washington'
    elif 360 < x < 360+20 and 155 < y < 155+20:
        return 'Wyoming'
    elif 515 < x < 515+20 and 410 < y < 410+20:
        return 'Texas'
    elif 150 < x < 150+20 and 300 < y < 300+20:
        return 'Cali'
    elif 985 < x < 985+10 and 178 < y < 178+10:
        return 'Mass'
    elif 285 < x < 285+20 and 350 < y < 350+20:
        return 'Arizona'
    elif 810 < x < 810+20 and 480 < y < 480+20:
        return 'Florida'
    elif 880 < x < 880+20 and 205 < y < 205+20:
        return 'Penn'
    elif 825 < x < 825+20 and 355 < y < 355+20:
        return 'Scarolina'
    elif 775 < x < 775+20 and 375 < y < 375+20:
        return 'Alabama'
    else:
        return 'Not Found'



if __name__ == "__main__":
    #alabama

    pygame.init()
    size = (1100, 700)
    view = View(size)
    view.draw()
    washington = Infobutton('Washington', 130, 55)
    view.display_info(washington)
    wyoming = Infobutton('Wyoming', 360, 155)
    view.display_info(wyoming)
    texas = Infobutton('Texas',515,410)
    view.display_info(texas)
    cali = Infobutton('California',150,300)
    view.display_info(cali)
    mass = Infobutton('Massachusetts',985,178,10,10)
    view.display_info(mass)
    arizona = Infobutton('Arizona',285,350)
    view.display_info(arizona)
    florida = Infobutton('Florida',810,480)
    view.display_info(florida)
    penn = Infobutton('Pennsylvania',880,205)
    view.display_info(penn)
    scarolina = Infobutton('South Carolina',825,355)
    view.display_info(scarolina)
    alabama = Infobutton('Alabama',775,375)
    view.display_info(alabama)


    smallText = pygame.font.SysFont("comicsansms",30)


    while True:
        # print(washington.button())


        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                state = find_state(mouse[0], mouse[1])
                if state == 'Washington':
                    wa_card = Infocard('Washington')
                    wa_card.draw('Washington.png')
                if state == 'Wyoming':
                    wy_card = Infocard('Wyoming')
                    wy_card.draw('Wyoming.png')
                if state == 'Texas':
                    tx_card = Infocard('Texas')
                    tx_card.draw(view)
                if state == 'Cali':
                    ca_card = Infocard('California')
                    ca_card.draw(view)
                if state == 'Mass':
                    ma_card = Infocard('Massachusetts')
                    ma_card.draw(view)
                if state == 'Arizona':
                    az_card = Infocard('Arizona')
                    az_card.draw(view)
                if state == 'Florida':
                    fl_card = Infocard('Florida')
                    fl_card.draw(view)
                if state == 'Penn':
                    pa_card = Infocard('Pennsylvania')
                    pa_card.draw(view)
                if state == 'Scarolina':
                    sc_card = Infocard('South Carolina')
                    sc_card.draw(view)
                if state == 'Alabama':
                    al_card = Infocard('Alabama')
                    al_card.draw(view)
                if state == 'Not Found':
                    clear_card = Infocard('',color=(255,255,255))
                    clear_card.draw(view)
