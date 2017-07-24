import timeit

start = timeit.default_timer()

s1 = "ACTCCAGTCATC"
s2 = "AGCATGGGGTCA"

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
    

def substringRevision(s1, s2):
    count = 0
    while(len(s1) != count):
        #runs longest substring and returns substring and position in tuple
        substringTuple = longest_substring(s1, s2)
        print("SubstringTuple = ", substringTuple)
        #replaces string 1 with a variable for the common substring
        s1 = s1[0:substringTuple[1]] + str(count) + s1[(substringTuple[1] + len(substringTuple[0])):len(s1)]
        
        print("s1 = ", s1)
        #replaces string 2 with a variable for the common substring
        s2 = s2[0:substringTuple[2]] + str(count) + s2[(substringTuple[2] + len(substringTuple[0])):len(s2)]
        print("s2 = ", s2)
        count+=1
        
substringRevision(s1, s2)

    
stop = timeit.default_timer()
print("Run time: ", stop - start)