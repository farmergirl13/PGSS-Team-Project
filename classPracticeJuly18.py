def thirdSide(side1, side2):
    return ((side1)**2+(side2**2))**0.5
    
def testThirdSide():
    print('Testing thirdSide()... ', end='')
    assert(thirdSide(3, 4) == 5)
    assert(thirdSide(6, 8) == 10)
    print('Passed.')
    
testThirdSide()

a = [1, 2, 3, 4]
#print(a[1])


perm1 = [2, 1, 3]
perm2 = [3, 2, 1]

    
def rearrangePerm(perm1, perm2):
    finalPerm = []
    for i in range(len(perm1)):
        finalPerm.append(0)
        
    for i in range(len(perm1)):
        pos = perm2.index(perm1[i])
        finalPerm[pos] = i+1
        
    return finalPerm
        
print(rearrangePerm(perm1, perm2))