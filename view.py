import pygame
from pygame.locals import *
import os

def menuLoop(screen):
    quit = False
    background = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                   os.sep + 'CL_Brighter.png')
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
           #if event.key == pygame.K_RETURN:
           #   gameLoop(screen) 
           quit = True
    if not quit: menuLoop(screen)


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
