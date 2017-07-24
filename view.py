import pygame
from pygame.locals import *
import os
import pygame.time


def menuLoop(screen):
    (width,height) = screen.get_size()
    (midX,midY) = (width/2,height/2)
    quit = False
    fishY = [(compLoop,440/1080),    (exerLoop,560/1080),
             (exerciseLoop,680/1080),(taskLoop,800/1080)]
    while(not quit): 
        background = \
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                          os.sep + 'Menu Screen 2.0.png')
        background = pygame.transform.scale(background,screen.get_size())
        cursor = \
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                          os.sep + 'cursor.png') 
        cursor = pygame.transform.scale(cursor,(width//15, height//20))
        screen.blit(background,(0,0))        
        screen.blit(cursor,(630-width//30,fishY[0][1] * height))
        pygame.display.flip()
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    call = lambda f,arg : f(arg)
                    call(fishY[0][0],screen)
                    quit = True
                elif event.key == pygame.K_RIGHT:
                    fishY = fishY[1:] + [fishY[0]]
                elif event.key == pygame.K_LEFT:
                    fishY = [fishY[-1]] + fishY[:-1]

        

def compLoop(screen):
    print("!")
    difficulty = 0
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    trialImages = [pygame.image.load(path + 'NR.png'),pygame.image.load(
                                     path + 'NL.png')]
    images = [pygame.image.load(path + 'CL_Brighter.png'),pygame.image.load(
              path + 'CR.png'), pygame.image.load(path + 'ICL.png'),
              pygame.image.load(path + 'ICR.png')]
    trial = True
    time = pygame.time.get_ticks()
    trialTimer = 0
    maxTrialTime = 10000
    incorrectTrials = 0
    currentImage = None
    while(trial):
        delta = pygame.time.get_ticks() - time
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        pygame.display.flip()
        trialTimer += delta
        if trialTimer > maxTrialTime:
            incorrectTrials += 1
            trialTimer = 0
            currentImage = None
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
def exerLoop(screen):
    print("?")
def exerciseLoop(screen):
    print(":")
def taskLoop(screen):
    print("*")

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
