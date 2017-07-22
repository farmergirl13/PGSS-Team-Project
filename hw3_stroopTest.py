####################################################
# 2017 PGSS CS HW3
####################################################

# Instructions:
# https://docs.google.com/document/d/17fCC9mQ5j4UiGi-BQv4h8f1pQsZODcZr8lFZQOCwBrA

# More colors:
# https://wiki.tcl.tk/37701

####################################################
# 
# Fill in this section!
# Author: Elizabeth Farmer
# Collaborated with:
#   Sammi,
#   <GROUP MEMBER'S NAME>, 
#   <GROUP MEMBER'S NAME>
# (A reminder that there is a 4-person group limit.)
#
####################################################

from tkinter import *
import random
import copy

####################################################
# Helper functions
####################################################

# Utilize this function below to draw. (It is called for you already.)
# Hint: You will want to pass in other parameters than the default.
def getRootAndCanvas(width=300, height=300):
  root = Tk()
  canvas = Canvas(root, width=width, height=height)
  canvas.pack()
  return (root, canvas)

####################################################
# stroopTest
####################################################

def stroopTest(availableColors, rows, cols):
  winWidth = cols*100
  winHeight = rows*50
  (root, canvas) = getRootAndCanvas(winWidth, winHeight)
  
  randomWord = []
  randomColor = []
  randomWordTuple = []
  #create the words and colors
  for row in range(rows):
    for col in range(cols):
      x = col*100 + 50
      y = row*50 + 25
      word = random.choice(availableColors)
      color = random.choice(availableColors)
      while(word==color):
        word = random.choice(availableColors)
      canvas.create_text(x, y, text=word, fill=color)
      randomWord.append(word)
      randomColor.append(color)
      randomTupleAddition = (word, color)
      randomWordTuple.append(randomTupleAddition)
      
      
  
  print(randomColor)

  
  result = randomWordTuple
  # Keep this line at the end! It makes your drawing actually display.
  root.mainloop()
  # Keep the return at the very end!
  return result

####################################################
# Testing stroopTest (only what we can test...)
####################################################

def testTupleListResult(testResult, availableColors, rows, cols):
  # check dimensions
  correctLength = rows * cols
  assert(len(testResult) == correctLength)
  for (wordText, colorOfWord) in testResult:
    # check that we only used the available colors
    assert(wordText in availableColors)
    assert(colorOfWord in availableColors)
    # check that the wordText and colorOfWord don't match
    assert(wordText != colorOfWord)

def testStroopTest():
  # simple test
  print("Testing simple test...")
  availableColors = ["red", "green", "blue"]
  rows = 3
  cols = 4
  testResultSimple = stroopTest(availableColors, rows, cols)
  testTupleListResult(testResultSimple, availableColors, rows, cols)
  print("Simple test passed!")
  print("(Make sure to check visual and printed results as well.)")
  
  # hard test
  print("\nTesting hard test...")
  availableColors = ["red", "orange", "yellow", "green", "blue",
                     "purple", "gray", "black", "pink"]
  rows = 7
  cols = 5
  testResultHard = stroopTest(availableColors, rows, cols)
  testTupleListResult(testResultHard, availableColors, rows, cols)
  print("Hard test passed!")
  print("(Make sure to check visual and printed results as well.)")
  
  # silly test
  print("\nTesting silly test...")
  availableColors = ["cyan", "tomato", "khaki", "firebrick"]
  rows = 10
  cols = 10
  testResultSilly = stroopTest(availableColors, rows, cols)
  testTupleListResult(testResultSilly, availableColors, rows, cols)
  print("Silly test passed!")
  print("(Make sure to check visual and printed results as well.)")

testStroopTest()
