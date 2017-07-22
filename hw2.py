####################################################
# 2017 PGSS CS HW2
####################################################

####################################################
# 
# Fill in this section!
# Author: Elizabeth Farmer
# Collaborated with:
#   Sammi,
#   Michaela, 
#   <GROUP MEMBER'S NAME>
# (A reminder that there is a 4-person group limit.)
#
####################################################

from tkinter import *
import math

####################################################
# Helper functions
####################################################
# Utilize this function below to draw. (It is called for you already.)
# Hint: You will want to pass in other parameters than the default...
def getRootAndCanvas(width=300, height=300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    return (root, canvas)

####################################################
# drawTiledFlags
####################################################

def drawEUFlag(canvas, canvasWidth, canvasHeight, flagWidth, flagHeight, xPosition, yPosition, margin):
    canvas.create_rectangle(xPosition, yPosition, xPosition+flagWidth, yPosition+flagHeight, fill="blue")
    cx = flagWidth/2 + xPosition
    cy = flagHeight/2 + yPosition
    r = flagHeight/2
    r*=0.7
    for circle in range(12):
        circleRadius = flagHeight/12
        circleAngle = math.pi/2 - (2*math.pi)*(circle/12)
        circleX1 = cx + r*math.cos(circleAngle)-(1/2)*circleRadius
        circleY1 = cy - r*math.sin(circleAngle)-(1/2)*circleRadius
        circleX2 = circleX1 + circleRadius
        circleY2 = circleY1 + circleRadius
        canvas.create_oval(circleX1, circleY1, circleX2, circleY2, fill="yellow")
        
  
def drawBahamasFlag(canvas, flagWidth, flagHeight, xPosition, yPosition):
    x1 = xPosition
    y1 = yPosition
    x2 = x1 + flagWidth
    y2 = y1 + flagHeight  
    canvas.create_rectangle(x1, y1, x1+flagWidth, flagHeight/3 + y1, fill="cyan")
    canvas.create_rectangle(x1, flagHeight/3 + y1, x2, 2*flagHeight/3 + y1, fill="yellow")
    canvas.create_rectangle(x1, 2*flagHeight/3 + y1, x2, flagHeight + y1, fill="cyan")
    canvas.create_polygon(x1, y1, x1+flagWidth/2, y2-(flagHeight/2), x1, y2, fill="black")
    
  
  
def drawTiledFlags(margin, rows, cols, flagWidth, flagHeight):
    # This code is a gift to you.
    winWidth = margin*2 + cols*flagWidth
    winHeight = margin*2 + rows*flagHeight
    (root, canvas) = getRootAndCanvas(winWidth, winHeight)
    
    startX = margin
    startY = margin
   
    for row in range(0, rows):
        for col in range(0, cols):
            x1 = startX + col*(flagWidth)
            y1 = startY + row*flagHeight
            if((col+row)%2):
                drawBahamasFlag(canvas, flagWidth, flagHeight, x1, y1) 
            else:
                drawEUFlag(canvas, winWidth, winHeight, flagWidth, flagHeight, x1, y1, margin)
               
           
      
  # Hint: Helper functions for each flag type are recommended!
  # ...
  # Keep this line at the end! It makes your drawing actually display.
    root.mainloop()
  
  
def testDrawTiledFlags():
    print("Testing drawTiledFlags...")
    drawTiledFlags(margin=10, rows=3, cols=5, flagWidth=100, flagHeight=60)
    print("Bye!")

testDrawTiledFlags()

####################################################
# drawBlankSheetMusic (optional, but recommended)
####################################################

def drawBlankSheetMusic(title, winWidth, winHeight, lineHeight, lineMargin,
                        measuresPerLine):
    (root, canvas) = getRootAndCanvas(winWidth, winHeight)
  # Insert your drawing code here
  # ...
  # Keep this line at the end! It makes your drawing actually display.
    root.mainloop()
  
def testDrawBlankSheetMusic():
    print("Testing drawBlankSheetMusic...")
    drawBlankSheetMusic(title="Blank sheet music", winWidth=800, winHeight=200,
        lineHeight=50, lineMargin=20, measuresPerLine=5)
    print("Bye!")

#testDrawBlankSheetMusic()
