# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.gX = 10
    data.gY = 100
    data.gR = 20
    data.gMoveSize = 10
    moveSize = data.gMoveSize
    data.possibleGhostMoves = [(-moveSize, 0), (moveSize, 0), (0, -moveSize), (0, moveSize)]

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    (data.gostDx, data.ghostDy) = random.choice(data.possibleGhostMoves)
    data.gX += dx
    data.gY += dy
    

def redrawAll(canvas, data):
    # draw in canvas
    if(data.gX-data.gR>0 and data.gY+data.gR<width):
        canvas.create_rectangle(data.gX-data.gR, data.gY-data.gR, data.gX+data.gR, data.gY+data.gR, fill="gray")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
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

run(400, 400)