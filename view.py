import pygame
from pygame.locals import *
import os



def menuLoop(screen):
    (width,height) = screen.get_size()
    (midX,midY) = (width/2,height/2)
    quit = False
    fishY = [(compLoop,597/2100),    (exerLoop,765/2100),
             (exerciseLoop,941/2100),(taskLoop,1125/2100)]
    while(not quit):
        background = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                       os.sep + 'Menu Screen 2.0.png')
        screen.blit(background,(0,0))   
        pygame.display.flip()
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   fishY[0][0](screen)
                   quit = True      
        

def compLoop(screen):
    pass
def exerLoop(screen):
    pass
def exerciseLoop(screen):
    pass
def taskLoop(screen):
    pass

def main():
    pygame.init()
    #class Struct(object): pass
    #data = Struct()
    #data.width = width
    #data.height = height
    modes = pygame.display.list_modes()
    screen = pygame.display.set_mode(modes[0],FULLSCREEN)
    info = pygame.display.Info()
    pygame.display.set_caption('dev')
    background = pygame.Surface(screen.get_size())
    screen.blit(background,(0,0))
    pygame.display.flip()
    menuLoop(screen)
        
main()
