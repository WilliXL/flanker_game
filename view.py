import pygame
from pygame.locals import *
import os
import random
import gif
import functions

readyImages = []
maps = []
pos = []
neg = []
def loadMaps(screen):
    maps = []
    (width,height) = screen.get_size()
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    for i in range(7):
        g = gif.GIFImage(path + 'map' + str(i) + '.gif')
        g.scale(screen.get_size())
        maps += [g]
        pygame.draw.rect(screen,Color("yellow"),(width/10,(height/10) * 8,(width/10) * i,height/9))
        pygame.display.flip()   
    pygame.draw.rect(screen,Color("blue"),(width/10,(height/10) * 8,(width/10) * 7,height/9))
    return maps
def loadFeedback(screen):
    pos = []
    neg = ([],[])
    (width,height) = screen.get_size()
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    for i in range(7):
        g = gif.GIFImage(path + 'Reward' + str(i + 1) + '---Pos.gif')
        g.scale(screen.get_size())
        pos += [g]
        pygame.draw.rect(screen,Color("blue"),(width/10,(height/10) * 8,(width/10) * i,height/9))
        pygame.display.flip()
    
    pygame.draw.rect(screen,Color("blue"),(width/10,(height/10) * 8,(width/10) * 7,height/9))
    return (pos,neg)
def loadReady():
    global readyImages
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    readyImages = [pygame.image.load(path + 'intro_1.png'),
                   pygame.image.load(path + 'intro_2.png'),
                   pygame.image.load(path + 'Directions1.png'),
                   pygame.image.load(path + 'Directions2.png'),
                   pygame.image.load(path + 'Directions3.png'),
                   pygame.image.load(path + 'Directions3.5.png'),
                   pygame.image.load(path + 'Directions4.png'),
                   pygame.image.load(path + 'Directions5.png')]
def menuLoop(screen):
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    pygame.mixer.init()
    pygame.mixer.music.load(path + "temp.mp3")
    pygame.mixer.music.set_volume(.5)
    (width,height) = screen.get_size()
    (midX,midY) = (width/2,height/2)
    quit = False
    fishY = [(clickLoop,410/1080),    (exerLoop,530/1080),
             (stepLoop,650/1080),(taskLoop,770/1080)]
    global maps
    maps = loadMaps(screen) 
    loadReady()
    global pos
    global neg
    (pos,neg) = loadFeedback(screen)
    while(not quit):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
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
                    quit = True
                    call = lambda f,arg : f(arg)
                    call(fishY[0][0],screen)
                elif event.key == pygame.K_RIGHT:
                    fishY = fishY[1:] + [fishY[0]]
                elif event.key == pygame.K_LEFT:
                    fishY = [fishY[-1]] + fishY[:-1]
                #for degug purpose
                elif event.key == pygame.K_ESCAPE: 
                    quit = True
                    pygame.quit()
                    break




def stepLoop(screen):
    print("!")
    difficulty = 0
    pygame.mixer.music.load(path + "temp.mp3")
    pygame.mixer.music.set_volume(.5)
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    pygame.mixer.music.play()
    images = [pygame.image.load(path + 'CLB.png'),pygame.image.load(
              path + 'CRB.png'), pygame.image.load(path + 'ILB.png'),
              pygame.image.load(path + 'IRB.png'),pygame.image.load(path +
              'MPBNGY.png'),pygame.image.load(path + 'MPBYGY.png')]
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
    randomOrder = False
    rightFirst = False
    incongrFirst = True 
    if randomOrder:
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,1) > 30 else 0
    else:
        orient = rightFirst
        congr  = incongrFirst
    maxTrials = 8
    trialNum = 0
    trialsPerBlock = 4
    blocksPerPractice = 2
    incorrectImage = pygame.image.load(path + 'incorrect.png')
    correctImage   = pygame.image.load(path + 'correct.png')
    incorrectImage = pygame.transform.scale(incorrectImage,screen.get_size())
    correctImage   = pygame.transform.scale(  correctImage,screen.get_size())
    def trialMistake():
        nonlocal trialNum
        trialNum += 1
        nonlocal incorrectTrials
        incorrectTrials += 1
        nonlocal trialTimer
        trialTimer  = 0
        nonlocal orient
        nonlocal congr 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        #screen.blit()
        screen.blit(incorrectImage,(0,0))
        #pygame.draw.rect(screen,(255,0,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    def trialSuccess():
        nonlocal trialNum
        trialNum += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr
        trialTimer = 0 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        screen.blit(correctImage,(0,0))
        #pygame.draw.rect(screen,(255,255,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    ready = False
    global readyImages 
    temp = []
    for image in readyImages:
        temp += [pygame.transform.scale(image,screen.get_size())]
    readyImages = temp
    g = gif.GIFImage("lc.gif")
    bubble = gif.GIFImage("bubbleanimation.gif")
    pygame.draw.rect(screen,Color("red"),(0,0,10,10))
    pygame.display.flip()
    bubble.scale(screen.get_size())
    pygame.draw.rect(screen,Color("green"),(0,0,10,10))
    (width,height) = screen.get_size()
    pressed = False
    done = False
    ls = gif.GIFImage("ls.gif")
    ls.scale(screen.get_size())
    rs = gif.GIFImage("rs.gif")
    rs.scale(screen.get_size())
    bs = gif.GIFImage("bs.gif")
    bs.scale(screen.get_size())
    for i in range(0,8):   
         while(not ready):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    done = True
                if event.type == pygame.KEYDOWN:
                    pressed = True
                    bubble.running = True
            screen.blit(readyImages[i],(0,0))
            if i == 3:
                if g.filename != "ls.gif": g = ls
                g.play()
                g.render(screen,(0,0))
            if i == 4:
                if g.filename != "rs.gif": g = rs
                g.play() 
                g.render(screen,(0,0))
            if i == 5:
                if g.filename != "bs.gif": g = bs
                g.play() 
                g.render(screen,(0,0))
            if pressed:
                    bubble.renderOnceAtSpeed(screen,(0,0),2)
            pygame.display.flip()
            ready = not bubble.running and pressed or done
         ready = False
         pressed = False
         bubble.rewind()
    pygame.event.get()
    while(trial):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
        if trialNum >= trialsPerBlock:
            block += 1
            trialNum = 0
        delta = pygame.time.get_ticks() - time
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        fontDef = pygame.font.Font("Corbert-Regular.otf",13)
        screen.blit(images[(congr * 2) + orient],(0,0))
        info = fontDef.render("trial: " + str(trialNum) + " "
                                       + "block: " + str(block),True,(0,0,0))
        screen.blit(info,(0,0))
        trialTimer += delta
        if block + 1 > blocksPerPractice:
            
            cont = False
            trial = False
            select = 1
            selections = [compLoop,stepLoop]
            while(not cont):
                screen.blit(images[4 + select],(0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            cont = True                            
                            call = lambda f,arg : f(arg)
                            call(selections[select],screen)
                        elif event.key == pygame.K_LEFT:
                            select = 1 - select
                        elif event.key == pygame.K_RIGHT:
                            select = 1 - select
        elif trialTimer > trialBlocks[block]:
            trialMistake() 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
                if event.key == pygame.K_RIGHT:
                    if orient == 0:
                        trialMistake()
                    else:
                        trialSuccess()
                if event.key == pygame.K_LEFT:
                    if orient == 1:
                        trialMistake()
                    else:
                        trialSuccess()
    return                    
    


def clickLoop(screen):
    print("!")
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    pygame.mixer.music.load(path + "temp.mp3")
    pygame.mixer.music.set_volume(.5)
    difficulty = 0
    pygame.mixer.music.play()
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    images = [pygame.image.load(path + 'CLB.png'),pygame.image.load(
              path + 'CRB.png'), pygame.image.load(path + 'ILB.png'),
              pygame.image.load(path + 'IRB.png'),pygame.image.load(path +
              'MPBNGY.png'),pygame.image.load(path + 'MPBYGY.png')]
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
    randomOrder = False
    rightFirst = False
    incongrFirst = True 
    if randomOrder:
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,1) > 30 else 0
    else:
        orient = rightFirst
        congr  = incongrFirst
    maxTrials = 8
    trialNum = 0
    trialsPerBlock = 4
    blocksPerPractice = 2
    incorrectImage = pygame.image.load(path + 'incorrect.png')
    correctImage   = pygame.image.load(path + 'correct.png')
    incorrectImage = pygame.transform.scale(incorrectImage,screen.get_size())
    correctImage   = pygame.transform.scale(  correctImage,screen.get_size())
    def trialMistake():
        nonlocal trialNum
        trialNum += 1
        nonlocal incorrectTrials
        incorrectTrials += 1
        nonlocal trialTimer
        trialTimer  = 0
        nonlocal orient
        nonlocal congr 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        #screen.blit()
        screen.blit(incorrectImage,(0,0))
        #pygame.draw.rect(screen,(255,0,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    def trialSuccess():
        nonlocal trialNum
        trialNum += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr
        trialTimer = 0 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        screen.blit(correctImage,(0,0))
        #pygame.draw.rect(screen,(255,255,0),((0,0),screen.get_size()))
        pygame.display.flip()
        pos[0].renderOnce(screen,(0,0))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    ready = False
    
    readyImages = [pygame.image.load(path + 'intro_1.png'),
                   pygame.image.load(path + 'intro_2.png'),
                   pygame.image.load(path + 'Directions1.png'),
                   pygame.image.load(path + 'Directions2.png'),
                   pygame.image.load(path + 'Directions3.png'),
                   pygame.image.load(path + 'Directions4.png'),
                   pygame.image.load(path + 'Directions5.png')]
    temp = []
    for image in readyImages:
        temp += [pygame.transform.scale(image,screen.get_size())]
    readyImages = temp
    g = gif.GIFImage("lc.gif")
    (width,height) = screen.get_size()
    for i in range(0,7):   
         while(not ready):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    ready = True
            screen.blit(readyImages[i],(0,0))
            if i == 3:
                if g.filename != "lc.gif": g = gif.GIFImage("lc.gif")
                g.play()
                g.render(screen,(0,height/4))
            if i == 4:
                if g.filename != "rc.gif": g = gif.GIFImage("rc.gif")
                g.play() 
                g.render(screen,(width/3,height/2))
            pygame.display.flip()
         ready = False
    pygame.event.get()
    while(trial):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
        if trialNum >= trialsPerBlock:
            block += 1
            trialNum = 0
        delta = pygame.time.get_ticks() - time
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        fontDef = pygame.font.Font("Corbert-Regular.otf",13)
        screen.blit(images[(congr * 2) + orient],(0,0))
        info = fontDef.render("trial: " + str(trialNum) + " "
                                       + "block: " + str(block),True,(0,0,0))
        screen.blit(info,(0,0))
        trialTimer += delta
        if block + 1 > blocksPerPractice:
            
            cont = False
            trial = False
            select = 1
            selections = [compLoop,clickLoop]
            while(not cont):
                screen.blit(images[4 + select],(0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            cont = True                            
                            call = lambda f,arg : f(arg)
                            call(selections[select],screen)
                        elif event.key == pygame.K_LEFT:
                            select = 1 - select
                        elif event.key == pygame.K_RIGHT:
                            select = 1 - select
        elif trialTimer > trialBlocks[block]:
            trialMistake() 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
                if event.key == pygame.K_RIGHT:
                    if orient == 0:
                        trialMistake()
                    else:
                        trialSuccess()
                if event.key == pygame.K_LEFT:
                    if orient == 1:
                        trialMistake()
                    else:
                        trialSuccess()
    return                    
    

        

def compLoop(screen):
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    effects  = pygame.mixer.Channel(1)
    SoundNeg = pygame.mixer.Sound(path + "Ratchet05.wav")
    SoundPos = pygame.mixer.Sound(path + "JarMus02.wav")
    SoundNeg.set_volume(.9)
    SoundPos.set_volume(.9)
    pygame.mixer.music.load(path + "temp.mp3")
    pygame.mixer.music.set_volume(.5)
    print("*")
    difficulty = 0
    temp = []
    images = [pygame.image.load(path + 'CLB.png'),pygame.image.load(
              path + 'CRB.png'), pygame.image.load(path + 'ILB.png'),
              pygame.image.load(path + 'IRB.png'),pygame.image.load(path +
              'MPBNGY.png'),pygame.image.load(path + 'MPBYGY.png')]
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
    randomOrder = False
    rightFirst = False
    incongrFirst = True 
    if randomOrder:
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,1) > 30 else 0
    else:
        orient = rightFirst
        congr  = incongrFirst
    maxTrials = 210
    trialNum = 0
    level = -1
    mistakes = 0
    trialsPerBlock = 7
    blocksPerGame = 24
    rewards = []
    for i in range(7):
        rewards += [pygame.image.load(path + 'Reward' + str(i) + '.png')]
    incorrectImage = pygame.image.load(path + 'incorrect.png')
    correctImage   = pygame.image.load(path + 'correct.png')
    incorrectImage = pygame.transform.scale(incorrectImage,screen.get_size())
    correctImage   = pygame.transform.scale(  correctImage,screen.get_size())
    data = functions.createDataDict()
    global maps
    def trialMistake():
        effects.play(SoundNeg)
        nonlocal trialNum
        trialNum += 1
        nonlocal mistakes
        mistakes += 1
        nonlocal incorrectTrials
        incorrectTrials += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr 
        functions.fill_trial(data,[
            ("" if congr else "in") + "conrguent",
            trialNum,block,"incorrect" if trialTimer != -1 else "toolong",
            trialTimer])           
        trialTimer  = 0
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,100) > 30 else 0
        delta = 0
        timeP = pygame.time.get_ticks()
        screen.blit(incorrectImage,(0,0))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - timeP
            timeP = pygame.time.get_ticks()
            pygame.event.get()
        nonlocal time
        time = pygame.time.get_ticks()
    def trialSuccess():
        effects.play(SoundPos)
        nonlocal trialNum
        trialNum += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr
        nonlocal level
        functions.fill_trial(data,[
            ("" if congr else "in") + "conrguent",
            trialNum,block,"correct",trialTimer])           
        trialTimer = 0 
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,100) > 30 else 0
        delta = 0
        timeP = pygame.time.get_ticks()
        screen.blit(rewards[level],(0,0))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - timeP
            timeP = pygame.time.get_ticks()
            pygame.event.get()
        nonlocal time
        time = pygame.time.get_ticks()
    ready = False
    dataDict = functions.createDataDict()
    readyImages = []
    for i in range(0,11):
        readyImages += [pygame.image.load(path + 'maps/map-' + str(i) + '.png')]
    temp = []
    for image in readyImages:
        temp += [pygame.transform.scale(image,screen.get_size())]
    readyImages = temp
#    for i in range(0,len(readyImages)):         
#        while(not ready):
#            for event in pygame.event.get():
#                if event.type == pygame.KEYDOWN:
#                    ready = True
#            screen.blit(readyImages[i],(0,0))
#            pygame.display.flip()
#        ready = False
    pygame.event.get()
    reset = False
    
    while(trial): 
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
        if trialNum >= trialsPerBlock:
            block += 1
            trialNum = 0
            ready = False
            reset = False
        if trialNum == 0 and block % 3 == 0 and not reset: 
            level += 1
            reset = True
            print(trialNum)
            pygame.draw.rect(screen,Color("red"),(0,0,5,5))
            while(not ready):
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        ready = True
                #screen.blit(readyImages[level],(0,0))
                maps[level].renderOnce(screen,(0,0))
                pygame.display.flip()
            if mistakes >= 3 * trialsPerBlock // 2:
                block -= 3
            pygame.event.get()
            time = pygame.time.get_ticks()
        delta = pygame.time.get_ticks() - time
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        fontDef = pygame.font.Font("Corbert-Regular.otf",13)
        screen.blit(images[(congr * 2) + orient],(0,0))
        info = fontDef.render("round: " + str(trialNum) + " "
                                       + "block: " + str(block),True,(0,0,0))
        screen.blit(info,(0,0))
        trialTimer += delta
        if block + 1 > blocksPerGame:
          break
        if level > 7:
          break
        if pygame.time.get_ticks() > 15 * 60 * 1000:
          break
        if trialTimer > functions.trialTime(block):
            trialTimer = -1
            trialMistake() 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
                if event.key == pygame.K_RIGHT:
                    if orient == 0:
                        trialMistake()
                    else:
                        trialSuccess()
                if event.key == pygame.K_LEFT:
                    if orient == 1:
                        trialMistake()
                    else:
                        trialSuccess()
                if event.key == pygame.K_DOWN:
                    trialNum += 1
    functions.createCSV(data) 

def exerLoop(screen):
    print("?")
def exerciseLoop(screen):
    print(":")
    difficulty = 0
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep

    images = [pygame.image.load(path + 'CLB.png'),pygame.image.load(
              path + 'CRB.png'), pygame.image.load(path + 'ILB.png'),
              pygame.image.load(path + 'IRB.png'),pygame.image.load(path +
              'MPBNGY.png'),pygame.image.load(path + 'MPBYGY.png')]
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
    randomOrder = False
    rightFirst = False
    incongrFirst = True 
    if randomOrder:
        orient = random.randint(0,1)
        congr = 1 if random.randint(0,1) > 30 else 0
    else:
        orient = rightFirst
        congr  = incongrFirst
    maxTrials = 8
    trialNum = 0
    trialsPerBlock = 4
    blocksPerPractice = 2
    incorrectImage = pygame.image.load(path + 'incorrect.png')
    correctImage   = pygame.image.load(path + 'correct.png')
    incorrectImage = pygame.transform.scale(incorrectImage,screen.get_size())
    correctImage   = pygame.transform.scale(  correctImage,screen.get_size())
    def trialMistake():
        pygame.mixer.music.load(path + "Ratchet05.mp3")
        pygame.mixer.music.play()
        nonlocal trialNum
        trialNum += 1
        nonlocal incorrectTrials
        incorrectTrials += 1
        nonlocal trialTimer
        trialTimer  = 0
        nonlocal orient
        nonlocal congr 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        screen.blit(incorrectImage,(0,0))
        #pygame.draw.rect(screen,(255,0,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    def trialSuccess():
        pygame.mixer.music.load(path + "JarMus02.mp3")
        pygame.mixer.music.play()
        nonlocal trialNum
        trialNum += 1
        nonlocal trialTimer
        nonlocal orient
        nonlocal congr
        trialTimer = 0 
        if trialNum > 3 or randomOrder:
            orient = random.randint(0,1)
            congr = 1 if random.randint(0,1) > 30 else 0
        else:
            orient = abs(rightFirst - (trialNum % 2))
            congr  = abs(incongrFirst - (trialNum // 2))
        delta = 0
        time = pygame.time.get_ticks()
        screen.blit(correctImage,(0,0))
        #pygame.draw.rect(screen,(255,255,0),((0,0),screen.get_size()))
        pygame.display.flip()
        while(delta < 1000):
            delta += pygame.time.get_ticks() - time
            time = pygame.time.get_ticks()
            pygame.event.get()
    ready = False
    
    readyImages = [pygame.image.load(path + 'Directions1.png'),
                   pygame.image.load(path + 'Directions2.png'),
                   pygame.image.load(path + 'Directions3.png'),
                   pygame.image.load(path + 'Directions4.png')]
    temp = []
    for image in readyImages:
        temp += [pygame.transform.scale(image,screen.get_size())]
    readyImages = temp
    for i in range(0,4):   
         while(not ready):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    ready = True
            screen.blit(readyImages[i],(0,0))
            pygame.display.flip()
         ready = False
    pygame.event.get()
    while(trial):
        if trialNum >= trialsPerBlock:
            block += 1
            trialNum = 0
        delta = pygame.time.get_ticks() - time
        time = pygame.time.get_ticks()
        pygame.draw.rect(screen,(0,0,0),((0,0),screen.get_size()))
        fontDef = pygame.font.Font("Corbert-Regular.otf",13)
        screen.blit(images[(congr * 2) + orient],(0,0))
        info = fontDef.render("trial: " + str(trialNum) + " "
                                       + "block: " + str(block),True,(0,0,0))
        screen.blit(info,(0,0))
        trialTimer += delta
        if block + 1 > blocksPerPractice:
            
            cont = False
            trial = False
            select = 1
            selections = [compLoop,practiceLoop]
            while(not cont):
                screen.blit(images[4 + select],(0,0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            cont = True                            
                            call = lambda f,arg : f(arg)
                            call(selections[select],screen)
                        elif event.key == pygame.K_LEFT:
                            select = 1 - select
                        elif event.key == pygame.K_RIGHT:
                            select = 1 - select
        elif trialTimer > trialBlocks[block]:
            trialMistake() 
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    trial = False
                if event.key == pygame.K_RIGHT:
                    if orient == 0:
                        trialMistake()
                    else:
                        trialSuccess()
                if event.key == pygame.K_LEFT:
                    if orient == 1:
                        trialMistake()
                    else:
                        trialSuccess()




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
    return
        
main()
