import pygame
from pygame.locals import *
import os
import random


def menuLoop(screen):
    (width,height) = screen.get_size()
    (midX,midY) = (width/2,height/2)
    quit = False
    fishY = [(compLoop,410/1080),    (exerLoop,530/1080),
             (exerciseLoop,650/1080),(taskLoop,770/1080)]
    while(not quit): 
        background = \
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                          os.sep + 'Menu Screen 3.0.png')
        background = pygame.transform.scale(background,screen.get_size())
        cursor = \
        pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +
                                          os.sep + 'cursor.png') 
        cursor = pygame.transform.scale(cursor,(width//15, height//20))
        screen.blit(background,(0,0))        
        screen.blit(cursor,((700/1920)*width-(width//30),fishY[0][1] * height))
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
    images = [pygame.image.load(path + 'CL_Brighter.png'),pygame.image.load(
              path + 'CR.png'), pygame.image.load(path + 'ICL.png'),
              pygame.image.load(path + 'ICR.png')]
    temp = []
    for image in images:
        temp += [pygame.transform.scale(image,screen.get_size())]
    images = temp
    trial = True
    time = pygame.time.get_ticks()
    trialTimer = 0
    maxTrialTime = 10000
    trialBlocks = [10000,5000]
    block = 0
    incorrectTrials = 0
    orient = random.randint(0,1)
    congr  = random.randint(0,1)
    maxTrials = 8
    trialNum = 0
    trialsPerBlock = 4
    def trialMistake():
        nonlocal trialNum
        trialNum += 1
        nonlocal incorrectTrials
        incorrectTrials += 1
        nonlocal trialTimer
        trialTimer  = 0
        nonlocal block
        nonlocal trialsPerBlock
        if trialNum > trialsPerBlock: block += 1
        nonlocal orient
        nonlocal congr 
        orient = random.randint(0,1)
        congr = random.randint(0,1)
        delta = 0
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(255,0,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    def trialSuccess():
        nonlocal trialNum
        trialNum += 1
        nonlocal block
        nonlocal trialsPerBlock
        if trialNum > trialsPerBlock: block += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr
        trialTimer = 0
        orient = random.randint(0,1)
        congr =  random.randint(0,1)
        delta = 0
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(255,255,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    ready = False
    while(not ready):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                ready = True
        pygame.draw.rect(screen,(0,0,255),((0,0),screen.get_size()))
        pygame.display.flip()
    while(trial):
        delta = pygame.time.get_ticks() - time
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        screen.blit(images[(congr * 2) + orient],(0,0))
        pygame.display.flip()
        trialTimer += delta
        if trialTimer > trialBlocks[block]:
            trialMistake()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
                if event.key == pygame.K_RIGHT:
                    if orient == 0:
                        trialMistake()
                        break
                    else:
                        trialSuccess()
                        break
                if event.key == pygame.K_LEFT:
                    if orient == 1:
                        trialMistake()
                        break
                    else:
                        trialSuccess()
                        break
        #if incorrectTrials > maxTrials:
            #if block > 0: block -= 1


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
