def thirdSide(side1, side2):
    return ((side1)**2+(side2**2))**0.5
    
def testThirdSide():
    print('Testing thirdSide()... ', end='')
    assert(thirdSide(3, 4) == 5)
    assert(thirdSide(6, 8) == 10)
    print('Passed.')
    
testThirdSide()

a = [1, 2, 3, 4]
print(a[1])
