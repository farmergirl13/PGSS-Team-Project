#===================================================================#
# Using Distances Between Genomes to Reconstruct Phylogenetic Trees #
#===================================================================#
# Created by:
#   Elizabeth Farmer
#   Bennett Andrews
#   Harshita Gupta
#===================================================================#

#-----------------------------
import timeit
start = timeit.default_timer()
#-----------------------------

strings = ["TAGCCGGCTGGAGCGGAGACGCCAGGGTTTAGCGCCGCGAATTGTAGGCTTATTCGGCAATTTCGGCTACATTGTCAACGCGGTATCTTTTCTTTAGGA",           
"CGGTTCTAGCAGTACAGAGGGTGCCGGCTGCTGGGCTGCCGTCACGCGTTAGCGCCGCGAATTTAATTTCTTGAACGCTGAGTAGCTTTTTAGGTAATA", "TAGCAGTAGAGGGTTTAGCGCGCGAATTACGCCGGGCAAGTAGTTCATTCCCTTACTGTGGTCAACGCCGGCTGTTCTTGACAGGAGTCTTGCTTATGG", 
"TAGCAAGGGTGCTCGCTGTAGGAGTAGCGAATCGGCTGCTCGCTGTTGGGCTGCAGCGCCGTCACGCTCTTTAATTTTCATGAATAGGCGGTTCTAATA", "TCTGAGCAGTAGAGGGTGCCGGAGGCTCTTTTAGCGCCGCTGAGTTGTTACACGTCGCGGTTGCCGCCATGAATTGTCTGGGCAATAGTTCATATAATC"]

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#        Step #1 Helper Functions                             #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Finds and returns the longest common subsets in two lists
def longest_substring(s1, s2):
    t = [[0]*(1+len(s2)) for i in range(1+len(s1))]
    positionAndLength = []
    l, xl = 0, 0
    for x in range(1,1+len(s1)):
        for y in range(1,1+len(s2)):
            if s1[x-1] == s2[y-1]:
                t[x][y] = t[x-1][y-1] + 1
                if t[x][y]>l:
                    l = t[x][y]
                    xl = x
                    yl = y
            else:
                t[x][y] = 0
    #Returns substring and indexes in the first and second strings
    return s1[xl-l: xl], (xl-l), (yl-l)

#Counts the number of placeholder values in the permutation modification process
def XinString(string, index):
    count2 = 0
    for i in range(index):
        if(string[i] == "X" or string[i] == "Y"):
            count2+=1
    return count2

#Orders the now useable base pair data into a single permutation
def rearrangePerm(perm1, perm2):
    finalPerm = []
    
    for i in range(len(perm1)):
        finalPerm.append(0)
        
    for i in range(len(perm1)):
        pos = perm2.index(perm1[i])
        finalPerm[pos] = i+1
        
    return finalPerm

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#        Step #2 Helper Functions                             #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Creates a new list from the final permutation by adding a 0 and n+1 position, and the 
#             number of times each number has been used in the cycle
def cycleCount(finalPerm):
    blockCount = [[0,1]]
    for i in range(len(finalPerm)):
        blockCount += [[finalPerm[i], 0]]
    blockCount += [[len(finalPerm)+1, 1]]
    return blockCount
    
#Figures out the position where each cycle should start
def startPosition(cycleList):
    for i in range(len(cycleList)):
        if(cycleList[i][1] < 2):
            return i
    return -42

#Finds the position of a number in the permutation and converts that distance in the cycle list
def findPosition(cycleList, finalPerm, number, max):
    if number == 0:
        return 0
    elif number == max:
        return max
    else:
        return (finalPerm.index(number) + 1)

#Increments the cycle counter for each number in the cycle
def incrementList(cycleList, number):
    cycleList[number][1] = cycleList[number][1] + 1
    
#Calculates the transposition distance from the number of cycles
def distance(finalPerm, cycles):
    lowerBound = ((len(finalPerm)+1) - cycles)/2
    upperBound = (len(finalPerm)+1) - cycles
    return upperBound #upperBound seems more correct than average

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#        Step #3 Helper Functions                             #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#Creates an array to store the distances between strings
def makeDistanceArray(strings):
    distanceArray = []
    for row in range(0, len(strings)):
        tempDistanceArray = []
        for col in range(0, len(strings)):
            tempDistanceArray += [0]
        distanceArray += [tempDistanceArray]
    return distanceArray
    
#Finds the smallest distance within the distance array
def findSmallestDistance(distanceArray):
    minimumDistance = 100000
    #print("Length of distance array", len(distanceArray))
    for row in range(0, len(distanceArray)):
        for col in range(0, len(distanceArray[0])):
            if(distanceArray[row][col]<minimumDistance and distanceArray[row][col]!=0):
                minimumDistance = distanceArray[row][col]
    return minimumDistance
    
def createNewList(oldList):
    add = []
    for row in range(len(oldList)-1):
        for col in range(len(oldList)-1):
            add += 0
    


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       #1) Base Pairs to Usable Data                         #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#The main function in step 1, two strings are compared and converted into a single permutation.
def substringRevision(s1, s2):
    count = 0
    perm1 = []
    perm2 = []
    while(len(s1) != count):
        #Runs longest substring and returns substring and position in tuple
        substringTuple = longest_substring(s1, s2)
        #print("SubstringTuple = ", substringTuple)
        
        #Replaces string 1 with a variable for the common substring
        s1 = s1[0:substringTuple[1]] + "X" + s1[(substringTuple[1] + len(substringTuple[0])):len(s1)]
        #print("s1 = ", s1)
        
        #Replaces string 2 with a variable for the common substring
        s2 = s2[0:substringTuple[2]] + "Y" + s2[(substringTuple[2] + len(substringTuple[0])):len(s2)]
       # print("s2 = ", s2)
        
        #Build unordered perm1
        perm1 = (perm1[0: XinString(s1, substringTuple[1])]) + [(count+1)] + (perm1[XinString(s1, substringTuple[1]): len(perm1)])
        #print(perm1)
        
        #Build unordered perm2
        perm2 = (perm2[0: XinString(s2, substringTuple[2])]) + [(count+1)] + (perm2[XinString(s2, substringTuple[2]): len(perm2)])
        #print(perm2)
        
       
        count+=1
    #print("finalPerm", rearrangePerm(perm1, perm2))
    return rearrangePerm(perm1, perm2)  
   


#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       #2) Permutations and Mathematics                      #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#The main function in step two: the final permutation is ran through a cycle counter to figure out how many cycles it has
def transpositionDistance(s1, s2):
    finalPerm = substringRevision(s1, s2)
    #finalPerm = [2, 3, 1]
    cycleList = cycleCount(finalPerm)
    #print(cycleCount(finalPerm))
    cycle = 0
    
    #Assigns the initial start position and number
    startPos = startPosition(cycleList)
    startNum = cycleList[startPos][0]
    
    number = -1
    #cycle creator
    while(startPos != -42):
    #for i in range(0, 3):
        counter = 0
        
        while (startNum != number):
            
            if (counter == 0):#If it is the first time through the cycle, the number has to be the start number plus one
                #Increments the value of the start number
                number = startNum + 1 #value
                #Finds the position of that incremented amount
                number = findPosition(cycleList, finalPerm, number, len(cycleList)-1) #I added the -1 here to fix the code
                incrementList(cycleList, number)
                #Moves to the left one position
                number = number - 1 #position
                incrementList(cycleList, number)
                #Gets the value of that position
                number = cycleList[number][0] #value
                counter += 1
                
            else: #If it is not the first time through the cycle, the number has to be the number plus one
                #Increments the value of the start number
                number = number + 1 #value
                #Finds the position of that incremented amount
                number = findPosition(cycleList, finalPerm, number, len(cycleList)-1) #I added the -1 here to fix the code
                incrementList(cycleList, number)
                #Moves to the left one position
                number = number - 1 #position
                incrementList(cycleList, number)
                #Gets the value of that position
                number = cycleList[number][0] #value
                
        #Increments the cycle counter by one
        cycle += 1
        #Establishes the start position for the next cycle
        startPos = startPosition(cycleList)
        #If every number has been in two cycles, end the loop and stop counting cycles
        if(startPos != -42):
            startNum = cycleList[startPos][0]
     
    #print("Number of cycles is", cycle)
    #Calculates the transposition distance between the two permutations
    transDistance = distance(finalPerm, cycle)
    return transDistance

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       #3) Reconstructing the Phylogenetic Tree              #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def tree(strings):
    positionList = []
    for i in range(0, len(strings)):
        positionList += [i]
    print("PositionList", positionList)
    dict = {"string1":1, "string2":1, "string3":1, "string4":1, "string5":1}
    #Creates the distance array by identifying the minimum transposition distance between two strings
    distanceArray = makeDistanceArray(strings)
    for row in range(0, len(strings)):
        for col in range(0, len(strings)):
            distance = min(transpositionDistance(strings[row], strings[col]), transpositionDistance(strings[col], strings[row]))
            distanceArray[row][col] = distance
            distanceArray[col][row] = distance
    
    #Creates the tree array by finding the smallest distance within the distance array
    treeArray = []
    
    a = 0
    b = 0
    counter = 1
    print("Distance array", distanceArray)
    newNode = len(distanceArray)
    #Creates a new array by calculating the new distances
    while(len(distanceArray)>2):
        smallestDistance = findSmallestDistance(distanceArray)
        newRow = []
        remaining = []
        remaining2 = []
        newValue = []
        addition = []
        
        #Finds the smallest distance in the array
        for row in range(0, len(distanceArray[0])):
            for col in range(0, len(distanceArray[0])):
                if(distanceArray[row][col] == smallestDistance):
                    addition = [row, newNode, smallestDistance, col, newNode, smallestDistance]
            
                    a = row
                    b = col
        #Adds the nodes and distance to the final tree array
        treeArray += addition
        positionList.remove(positionList[a])
        positionList.remove(positionList[b])
        positionList += [newNode]
        print("positionList", positionList)
        
        #Keeps the old distances that do not change
        for row in range(0, len(distanceArray)):
            remaining = []
            for col in range(0, len(distanceArray[0])):
                if(a != row and b != row and a != col and b != col):
                    remaining += [distanceArray[row][col]]
                    
            remaining += [-1]
            if(remaining != [-1]):
                remaining2 += [remaining]
             
        #Calculates the new distances
        for i in range(0, len(distanceArray[0])):
            if(i != b and i != a):
                newValue += [((distanceArray[a][i] + distanceArray[b][i])*(1/2))]
        newValue += [0]
        newRow += [newValue]

        distanceArray = remaining2   
        distanceArray += newRow
        print("Mid distance array", distanceArray)
        for row in range(0, len(distanceArray)):
            for col in range(0, len(distanceArray)):
                print(distanceArray[row][col])
                if(distanceArray[row][col] == -1):
                    distanceArray[row][col] = distanceArray[col][row]
                
        print("***Tree array***", treeArray)
        print("Distance array after function", distanceArray)
        counter += 1
        newNode += 1
    
tree(strings)
    
#print(transpositionDistance("ATTGCCTGC", "TGCGCCATT"))
#print(transpositionDistance("TGCGCCATT", "ATTGCCTGC"))

#-----------------------------
stop = timeit.default_timer()
print("Run time: ", stop - start)
#-----------------------------