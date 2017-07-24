import timeit

start = timeit.default_timer()

s1 = "ATTGCCTGC"
s2 = "TGCGCCATT"

start = timeit.default_timer()

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
    #returns substring and indexes in the first and second strings
    return s1[xl-l: xl], (xl-l), (yl-l)
    
def XinString(string, index):
    count2 = 0
    for i in range(index):
        if(string[i] == "X" or string[i] == "Y"):
            count2+=1
    return count2

def rearrangePerm(perm1, perm2):
    finalPerm = []
    for i in range(len(perm1)):
        finalPerm.append(0)
        
    for i in range(len(perm1)):
        pos = perm2.index(perm1[i])
        finalPerm[pos] = i+1
        
    return finalPerm
    
    
            

def substringRevision(s1, s2):
    count = 0
    perm1 = []
    perm2 = []
    while(len(s1) != count):
        #runs longest substring and returns substring and position in tuple
        substringTuple = longest_substring(s1, s2)
        print("SubstringTuple = ", substringTuple)
        #replaces string 1 with a variable for the common substring
        s1 = s1[0:substringTuple[1]] + "X" + s1[(substringTuple[1] + len(substringTuple[0])):len(s1)]
        
        print("s1 = ", s1)
        #replaces string 2 with a variable for the common substring
        s2 = s2[0:substringTuple[2]] + "Y" + s2[(substringTuple[2] + len(substringTuple[0])):len(s2)]
        print("s2 = ", s2)
        #build perm1
        perm1 = (perm1[0: XinString(s1, substringTuple[1])]) + [(count+1)] + (perm1[XinString(s1, substringTuple[1]): len(perm1)])
        print(perm1)
        #build perm2
        perm2 = (perm2[0: XinString(s2, substringTuple[2])]) + [(count+1)] + (perm2[XinString(s2, substringTuple[2]): len(perm2)])
        print(XinString(s2, substringTuple[2]))
        print(perm2)
        
        count+=1
    print(rearrangePerm(perm1, perm2))

        
substringRevision(s1, s2)

    
stop = timeit.default_timer()
print("Run time: ", stop - start)