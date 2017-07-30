# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import random
import copy

####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.rows = 15
    data.cols = 10
    data.margin = 20
    data.cellSize = 20
    data.emptyColor = "blue"    
    data.board = []
    data.timer = 0
    data.fallRate = 7
    data.score = 0
    data.gameOver = False
    for row in range(data.rows):
        rowList = []
        for col in range(data.cols):
            rowList += ["blue"]
        data.board.append(rowList)
    # Seven "standard" pieces (tetrominoes)
    iPiece = [
        [ True,  True,  True,  True]
    ]
    jPiece = [
        [ True, False, False ],
        [ True, True,  True]
    ]
    lPiece = [
        [ False, False, True],
        [ True,  True,  True]
    ]
    oPiece = [
        [ True, True],
        [ True, True]
    ]
    sPiece = [
        [ False, True, True],
        [ True,  True, False ]
    ]
    tPiece = [
        [ False, True, False ],
        [ True,  True, True]
    ]
    zPiece = [
        [ True,  True, False ],
        [ False, True, True]
    ]
    data.tetrisPieces = [ iPiece, jPiece, 
        lPiece, oPiece, sPiece, tPiece, zPiece ]
    data.tetrisPieceColors = [ "red", "yellow",
        "magenta", "pink", "cyan", "green", "orange" ]
    newFallingPiece(data)

def newFallingPiece(data):
    newPieceIndex = random.randint(0, len(data.tetrisPieces)-1)
    # set these values accordingly
    data.fallingPiece = data.tetrisPieces[newPieceIndex]
    data.fallingPieceColor = data.tetrisPieceColors[newPieceIndex]
    data.fallingPieceRow = 0
    fpCols = len(data.fallingPiece[0])
    boardCols = len(data.board[0])
    data.fallingPieceCol = boardCols//2 - fpCols//2

def mousePressed(event, data):
    # use event.x and event.y
    pass

def fallingPieceIsLegal(data):
    fpList = data.fallingPiece
    fpRow = data.fallingPieceRow
    fpCol = data.fallingPieceCol
    for i in range(len(fpList)):
        for j in range(len(fpList[0])):
            if fpList[i][j]:
                fpCellRow = fpRow + i
                fpCellCol = fpCol + j
                if fpCellRow < 0 or fpCellRow >= len(data.board):
                    return False
                elif fpCellCol < 0 or fpCellCol >= len(data.board[0]):
                    return False
                elif data.board[fpCellRow][fpCellCol] != data.emptyColor:
                    return False
    return True

def rotateFallingPiece(data):
    oldFP = copy.deepcopy(data.fallingPiece)
    newFP = []
    oldFPRows = len(oldFP)
    oldFPCols = len(oldFP[0])
    for col in range(oldFPCols-1, -1, -1):
        newFPRow = []
        for row in range(oldFPRows):
            newFPRow.append(oldFP[row][col])
        newFP.append(newFPRow)
    data.fallingPiece = newFP
    # find new center
    oldFPRow = data.fallingPieceRow
    oldFPCol = data.fallingPieceCol
    oldFPCenterRow = oldFPRow + oldFPRows//2
    oldFPCenterCol = oldFPCol + oldFPCols//2
    newFPRow = oldFPCenterRow - len(newFP)//2
    newFPCol = oldFPCenterCol - len(newFP[0])//2
    data.fallingPieceRow = newFPRow
    data.fallingPieceCol = newFPCol
    # if not legal, undo
    if not fallingPieceIsLegal(data):
        data.fallingPiece = oldFP
        data.fallingPieceRow = oldFPRow
        data.fallingPieceCol = oldFPCol

def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    if not fallingPieceIsLegal(data):
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        return False
    else:
        return True
        
def drawGameOver(data, canvas):
    canvas.create_text(data.width/2, data.height/2,
        text="Game Over",
        font="Consolas 36 bold",
        fill="white")
    canvas.create_text(data.width/2, data.height/2 + data.margin*2,
        text="Press 'r' to restart",
        font="Consolas 16 bold",
        fill="white")

def drawScore(data, canvas):
    scoreString = "Score: " + str(data.score)
    canvas.create_text(data.width/2, data.margin/2,
        text=scoreString,
        font="Consolas 16 bold",
        fill="black")

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym == "Down":
        #data.fallingPieceRow += 1
        moveFallingPiece(data, 1, 0)
    elif event.keysym == "Left":
        #data.fallingPieceCol -= 1
        moveFallingPiece(data, 0, -1)
    elif event.keysym == "Right":
        #data.fallingPieceCol += 1
        moveFallingPiece(data, 0, 1)
    elif event.keysym == "Up":
        rotateFallingPiece(data)
    elif event.keysym == "r":
        init(data)
    else:
        newFallingPiece(data)

def timerFired(data):
    data.timer+=1
    if(data.timer%data.fallRate == 0):
        wasLegal = moveFallingPiece(data, 1, 0)
        if not wasLegal:
            placeFallingPiece(data)
            removeFullRows(data)
            newFallingPiece(data)
            if not fallingPieceIsLegal:
                data.gameOver = True
            
        

def drawCell(data, canvas, row, col, fillColor):
    x1 = data.margin + col*data.cellSize
    y1 = data.margin + row*data.cellSize
    x2 = x1 + data.cellSize
    y2 = y1 + data.cellSize
    canvas.create_rectangle(x1, y1, x2, y2,
        fill=fillColor, width=2)

def drawBoard(data, canvas):
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(data, canvas, row, col,
                data.board[row][col])

def drawFallingPiece(data, canvas):
    fpList = data.fallingPiece
    fpRows = len(fpList)
    fpCols = len(fpList[0])
    for pieceRow in range(fpRows):
        for pieceCol in range(fpCols):
            shouldDraw = fpList[pieceRow][pieceCol]
            if (shouldDraw):
                boardRow = data.fallingPieceRow + pieceRow
                boardCol = data.fallingPieceCol + pieceCol
                drawCell(data, canvas, boardRow, boardCol,
                    data.fallingPieceColor)
                    
def placeFallingPiece(data):
    fpList = data.fallingPiece
    fpRows = len(fpList)
    fpCols = len(fpList[0])
    for pieceRow in range(fpRows):
        for pieceCol in range(fpCols):
            shouldDraw = fpList[pieceRow][pieceCol]
            if (shouldDraw):
                boardRow = data.fallingPieceRow + pieceRow
                boardCol = data.fallingPieceCol + pieceCol
                data.board[boardRow][boardCol] = data.fallingPieceColor
                
def removeFullRows(data):
    boardRows = len(data.board)
    boardCols = len(data.board[0])
    newRow = boardRows-1
    roundScore = 0
    for oldRow in range(boardRows-1, -1, -1):
        rowIsFull = True
        for boardCol in range(boardCols):
            if data.board[oldRow][boardCol] == data.emptyColor:
                rowIsFull = False
        if rowIsFull:
            roundScore += 1
        else:
            data.board[newRow] = copy.copy(data.board[oldRow])
            newRow -= 1
    while newRow >= 0:
        data.board[newRow] = [data.emptyColor] * boardCols
        newRow -= 1
    data.score += roundScore**2

            

def drawGame(data, canvas):
    canvas.create_rectangle(0, 0,
        data.width, data.height,
        fill="orange")
    drawBoard(data, canvas)
    drawFallingPiece(data, canvas)
    drawScore(data, canvas)
    if(data.gameOver):
        drawGameOver(data, canvas)

def redrawAll(canvas, data):
    drawGame(data, canvas)

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

def playTetris():
    rows = 15
    cols = 10
    margin = 20
    cellSize = 20
    canvasWidth = 2*margin + cols*cellSize
    canvasHeight = 2*margin + rows*cellSize
    run(canvasWidth, canvasHeight)

playTetris()
