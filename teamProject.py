import timeit

start = timeit.default_timer()

import re
s1 = "ACTCTCATGCTACLAKDASDFLSJFLJELIZABETHADJFLAJDFLK"
s2 = "AECATGTCAAASJDFJSLDFJELIZABETHALKSDJFLJDFLJADS"

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
                    xl  = x
                    startPosition = x-l
            else:
                t[x][y] = 0
    addition = s1[xl-l: xl], (xl-l)
    positionAndLength.append(addition)
    return positionAndLength
   
print(longest_substring(s1, s2))

def removeLongestSubstring(string, substring, position):
    
    
stop = timeit.default_timer()
print("Run time: ", stop - start)