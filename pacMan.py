# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random

####################################
# customize these functions
####################################

def init(data):
    data.pacmanCX = 250
    data.pacmanCY = 150
    data.pacmanR = 20
    data.moveSize = 15
    data.ghostX = 100
    data.ghostY = 50
    data.ghostR = 10
    data.ghostMoveSize = 10
    moveSize = data.ghostMoveSize
    data.possibleGhostMoves = [
        (moveSize, 0), # right
        (-moveSize, 0), # left
        (0, moveSize), # down
        (0, -moveSize), # up
        (0, 0),
        (0, 0),
    ]
    data.timer = 0
    data.ghostdx = 0
    data.ghostdy = 0

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    print(event.keysym)
    if event.keysym == "Left":
        data.pacmanCX -= data.moveSize
    elif event.keysym == "Right":
        data.pacmanCX += data.moveSize
    elif event.keysym == "Up":
        data.pacmanCY -= data.moveSize
    elif event.keysym == "Down":
        data.pacmanCY += data.moveSize

def timerFired(data):
    data.timer += 1
    possibleMoves = data.possibleGhostMoves
    if data.timer % 5 == 0:
        (data.ghostdx, data.ghostdy) = random.choice(possibleMoves)
    data.ghostX += data.ghostdx
    data.ghostY += data.ghostdy

def redrawAll(canvas, data):
    cx = data.pacmanCX
    cy = data.pacmanCY
    r = data.pacmanR
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r,
        fill="yellow")
    cx = data.ghostX
    cy = data.ghostY
    r = data.ghostR
    canvas.create_rectangle(cx-r, cy-r, cx+r, cy+r,
        fill="gray")

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