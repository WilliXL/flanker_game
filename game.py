# started from barebones tkinter starter code from CMU's 15-112 by David Kosbie

# Global variables: canvas width and height, and buffer size
canvasWidth = 1660
canvasHeight = 980
buffer = 40

from tkinter import *
import pandas as pd

def init(data):
	data.mode = "enterInfo"
	data.prevMode = ""

########################
# mode dispatcher
########################

# modes:
'''
enterInfo
mainMenu
computerGame
	narrativeComputerGame
	tutorialComputerGame
	playGameComputerGame
exergame
	narrativeExergame
	tutorialExergame
	playGameExergame
exercise
	narrativeExercise
	tutorialExercise
	playGameExercise
task
	narrativeTask
	tutorialTask
	playGameTask
correct
incorrect
tooLong
gameOver
leaderboard
parseData
'''

def mousePressed(event, data):
    if (data.mode == "enterInfo"):               enterInfoMousePressed(event, data)

    elif (data.mode == "mainMenu"):              mainMenuMousePressed(event, data)

    elif (data.mode == "narrativeComputerGame"): narrativeComputerGameMousePressed(event, data)
    elif (data.mode == "tutorialComputerGame"):  tutorialComputerGameMousePressed(event, data)
    elif (data.mode == "playGameComputerGame"):  playGameComputerGameMousePressed(event, data)

    elif (data.mode == "narrativeExergame"):     narrativeExergameMousePressed(event, data)
    elif (data.mode == "tutorialExergame"):      tutorialExergameMousePressed(event, data)
    elif (data.mode == "playGameExergame"):      playGameExergameMousePressed(event, data)

    elif (data.mode == "narrativeExercise"):     narrativeExerciseMousePressed(event, data)
    elif (data.mode == "tutorialExercise"):      tutorialExerciseMousePressed(event, data)
    elif (data.mode == "playGameExercise"):      playGameExerciseMousePressed(event, data)

    elif (data.mode == "narrativeTask"):         narrativeTaskMousePressed(event, data)
    elif (data.mode == "tutorialTask"):          tutorialTaskMousePressed(event, data)
    elif (data.mode == "playGameTask"):          playGameTaskMousePressed(event, data)

    elif (data.mode == "correct"):               correctMousePressed(event, data)
    elif (data.mode == "incorrect"):             incorrectMousePressed(event, data)
    elif (data.mode == "tooLong"):               tooLongMousePressed(event, data)
    elif (data.mode == "gameOver"):              gameOverMousePressed(event, data)

    elif (data.mode == "leaderboard"):           leaderboardMousePressed(event, data)

    elif (data.mode == "parseData"):             parseDataMousePressed(event, data)
    

def keyPressed(event, data):
    if (data.mode == "enterInfo"):               enterInfoKeyPressed(event, data)
    
    elif (data.mode == "mainMenu"):              mainMenuKeyPressed(event, data)

    elif (data.mode == "narrativeComputerGame"): narrativeComputerGameKeyPressed(event, data)
    elif (data.mode == "tutorialComputerGame"):  tutorialComputerGameKeyPressed(event, data)
    elif (data.mode == "playGameComputerGame"):  playGameComputerGameKeyPressed(event, data)

    elif (data.mode == "narrativeExergame"):     narrativeExergameKeyPressed(event, data)
    elif (data.mode == "tutorialExergame"):      tutorialExergameKeyPressed(event, data)
    elif (data.mode == "playGameExergame"):      playGameExergameKeyPressed(event, data)

    elif (data.mode == "narrativeExercise"):     narrativeExerciseKeyPressed(event, data)
    elif (data.mode == "tutorialExercise"):      tutorialExerciseKeyPressed(event, data)
    elif (data.mode == "playGameExercise"):      playGameExerciseKeyPressed(event, data)

    elif (data.mode == "narrativeTask"):         narrativeTaskKeyPressed(event, data)
    elif (data.mode == "tutorialTask"):          tutorialTaskKeyPressed(event, data)
    elif (data.mode == "playGameTask"):          playGameTaskKeyPressed(event, data)

    elif (data.mode == "correct"):               correctKeyPressed(event, data)
    elif (data.mode == "incorrect"):             incorrectKeyPressed(event, data)
    elif (data.mode == "tooLong"):               tooLongKeyPressed(event, data)
    elif (data.mode == "gameOver"):              gameOverKeyPressed(event, data)

    elif (data.mode == "leaderboard"):           leaderboardKeyPressed(event, data)

    elif (data.mode == "parseData"):             parseDataKeyPressed(event, data)
    

def timerFired(data):
    if (data.mode == "enterInfo"):               enterInfoTimerFired(event, data)
    
    elif (data.mode == "mainMenu"):              mainMenuTimerFired(event, data)

    elif (data.mode == "narrativeComputerGame"): narrativeComputerTimerFired(event, data)
    elif (data.mode == "tutorialComputerGame"):  tutorialComputerTimerFired(event, data)
    elif (data.mode == "playGameComputerGame"):  playGameComputerTimerFired(event, data)

    elif (data.mode == "narrativeExergame"):     narrativeExergameTimerFired(event, data)
    elif (data.mode == "tutorialExergame"):      tutorialExergameTimerFired(event, data)
    elif (data.mode == "playGameExergame"):      playGameExergameTimerFired(event, data)

    elif (data.mode == "narrativeExercise"):     narrativeExerciseTimerFired(event, data)
    elif (data.mode == "tutorialExercise"):      tutorialExerciseTimerFired(event, data)
    elif (data.mode == "playGameExercise"):      playGameExerciseTimerFired(event, data)

    elif (data.mode == "narrativeTask"):         narrativeTaskTimerFired(event, data)
    elif (data.mode == "tutorialTask"):          tutorialTaskTimerFired(event, data)
    elif (data.mode == "playGameTask"):          playGameTaskTimerFired(event, data)

    elif (data.mode == "correct"):               correctTimerFired(event, data)
    elif (data.mode == "incorrect"):             incorrectTimerFired(event, data)
    elif (data.mode == "tooLong"):               tooLongTimerFired(event, data)
    elif (data.mode == "gameOver"):              gameOverTimerFired(event, data)

    elif (data.mode == "leaderboard"):           leaderboardTimerFired(event, data)

    elif (data.mode == "parseData"):             parseDataTimerFired(event, data)
    

def redrawAll(canvas, data):
    if (data.mode == "enterInfo"):               enterInfoRedrawAll(event, data)
    
    elif (data.mode == "mainMenu"):              mainMenuRedrawAll(event, data)

    elif (data.mode == "narrativeComputerGame"): narrativeComputerRedrawAll(event, data)
    elif (data.mode == "tutorialComputerGame"):  tutorialComputerRedrawAll(event, data)
    elif (data.mode == "playGameComputerGame"):  playGameComputerRedrawAll(event, data)

    elif (data.mode == "narrativeExergame"):     narrativeExergameRedrawAll(event, data)
    elif (data.mode == "tutorialExergame"):      tutorialExergameRedrawAll(event, data)
    elif (data.mode == "playGameExergame"):      playGameExergameRedrawAll(event, data)

    elif (data.mode == "narrativeExercise"):     narrativeExerciseRedrawAll(event, data)
    elif (data.mode == "tutorialExercise"):      tutorialExerciseRedrawAll(event, data)
    elif (data.mode == "playGameExercise"):      playGameExerciseRedrawAll(event, data)

    elif (data.mode == "narrativeTask"):         narrativeTaskRedrawAll(event, data)
    elif (data.mode == "tutorialTask"):          tutorialTaskRedrawAll(event, data)
    elif (data.mode == "playGameTask"):          playGameTaskRedrawAll(event, data)

    elif (data.mode == "correct"):               correctRedrawAll(event, data)
    elif (data.mode == "incorrect"):             incorrectRedrawAll(event, data)
    elif (data.mode == "tooLong"):               tooLongRedrawAll(event, data)
    elif (data.mode == "gameOver"):              gameOverRedrawAll(event, data)

    elif (data.mode == "leaderboard"):           leaderboardRedrawAll(event, data)

    elif (data.mode == "parseData"):             parseDataRedrawAll(event, data)
    



####################################
# use the run function as-is
####################################

def run(width=canvasWidth, height=canvasHeight):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1 # milliseconds
    data.e = None
    root = Tk()
    
    init(data)



    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed



    print("bye!")

run(canvasWidth, canvasHeight)