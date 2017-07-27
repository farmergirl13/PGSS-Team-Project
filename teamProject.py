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

s1 = "ATTGCCTGC"
s2 = "TGCGCCATT"

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

def cycleCount(finalPerm):
    blockCount = [[0,1]]
    for i in range(len(finalPerm)):
        blockCount += [[finalPerm[i], 0]]
    blockCount += [[len(finalPerm)+1, 1]]
    return blockCount
    
def startPosition(cycleList):
    for i in range(len(cycleList)):
        if(cycleList[i][1] < 2):
            #return cycleList[i][0]
            print("cycleList", cycleList)
            print("i= ", i)
            return i
    return -42
            
def findPosition(cycleList, finalPerm, number, max):
    if number == 0:
        return 0
    elif number == max:
        return max
    else:
        return (finalPerm.index(number) + 1)

def incrementList(cycleList, number):
    cycleList[number][1] = cycleList[number][1] +1
    print(cycleList)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#        Step #3 Helper Functions                             #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#



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
        print("SubstringTuple = ", substringTuple)
        
        #Replaces string 1 with a variable for the common substring
        s1 = s1[0:substringTuple[1]] + "X" + s1[(substringTuple[1] + len(substringTuple[0])):len(s1)]
        print("s1 = ", s1)
        
        #Replaces string 2 with a variable for the common substring
        s2 = s2[0:substringTuple[2]] + "Y" + s2[(substringTuple[2] + len(substringTuple[0])):len(s2)]
        print("s2 = ", s2)
        
        #Build unordered perm1
        perm1 = (perm1[0: XinString(s1, substringTuple[1])]) + [(count+1)] + (perm1[XinString(s1, substringTuple[1]): len(perm1)])
        print(perm1)
        
        #Build unordered perm2
        perm2 = (perm2[0: XinString(s2, substringTuple[2])]) + [(count+1)] + (perm2[XinString(s2, substringTuple[2]): len(perm2)])
        print(perm2)
        
        count+=1
        
    return rearrangePerm(perm1, perm2)  
    print(rearrangePerm(perm1, perm2))




#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       #2) Permutations and Mathematics                      #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
def transpositionDistance():
    finalPerm = substringRevision(s1, s2)
    cycleList = cycleCount(finalPerm)
    print(cycleCount(finalPerm))
    cycle = 0
    
    
    #print(startPosition(cycleList))
    startPos = startPosition(cycleList)
    print(startPos)
    startNum = cycleList[startPos][0]
    print(startNum)
    
    #cycle creator
    while(startPos != -42):
        counter = 0
        number = -1
        while (startNum != number):
            if (counter == 0):
                number = startNum + 1
                print("number1", number)
                number = findPosition(cycleList, finalPerm, number, len(cycleList))
                print("number2", number)
                incrementList(cycleList, number)
                number = number - 1
                print("number3", number)
                incrementList(cycleList, number)
                number = cycleList[number][0]
                print("number4", number)
                counter += 1
            else: 
                number = number + 1
                print("number1", number)
                number = findPosition(cycleList, finalPerm, number, len(cycleList))
                print("number2", number)
                incrementList(cycleList, number)
                number = number - 1
                print("number3", number)
                incrementList(cycleList, number)
                number = cycleList[number][0]
                print("number4", number)
        cycle += 1
        print("cycle",cycle)
        startPos = startPosition(cycleList)
        
    print(cycle)
        
        
    

transpositionDistance()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#       #3) Reconstructing the Phylogenetic Tree              #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#



#-----------------------------
stop = timeit.default_timer()
print("Run time: ", stop - start)
#-----------------------------