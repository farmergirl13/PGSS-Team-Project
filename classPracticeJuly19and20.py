import random
def f(x):
    return 1/0
def g(x):
    return f(x)
def h(x):
    return g(x)
#h(1)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    
def swap2(a, i, j): #tuple assignment
    (a[i], a[j]) = (a[j], a[i])

a = [1, 2, 3, 4]
swap2(a, 1, 3)

assert(a==[1, 4, 3, 2])
print("passed!!")


#to make a copy without creating an alias (doesn't work)
coords = [(1, 2), (3, 4), (5, 6)]
coords2 = []
for coord in coords:
    coords2.append(coord)
print(coords)
print(coords2)



def countOdds(a):
    numberOfOdds = 0
    for i in a:
        if(ai%2!=0):
            numberOfOdds += 1
    return numberOfOdds
    
def countOdds2(a):
    numberOfOdds = 0
    for i in range(0, len(a)):
        if(a[i]%2!=0):
            numberOfOdds += 1
    return numberOfOdds
    
a = [4, 9, 2, 5, 843]
print(countOdds2(a))



#to make a tuple from a list
def makeEvenOddList(a):
    newList = []
    for i in a:
        if(i%2==0):
            newList.append((i, "even"))
        else:
            newList.append((i, "odd"))
            
    return newList
    
result = [(4, "even"), (9, "odd"), (2, "even"), (5, "odd"), (843, "odd")]
print(makeEvenOddList(a))
assert(makeEvenOddList(a) == result)
print("passed!!")

questions = [
        ("What color is the sky?", "Blue"), ("1+1", "2"), ("12+34", "46")]
        
def quizzer(questions):
    yourAnswer = ""
    for i in range(0, len(questions)):
        while(yourAnswer != questions[i][1]):
            print(questions[i][0])
            yourAnswer = input("> ")
        print("Correct!")
        
quizzer(questions)
        
def rps():
    choices = ["rock", "paper", "scissors"]
    
    choice = random.choice(choices)
    
    return choice
    
print(rps())


    

