#################################################
# Lab1
#################################################

import cs112_s17_linter
import math
import decimal

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-101 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)
    
def roundHalfUp(d):
   # Round to nearest with ties going away from zero.
   rounding = decimal.ROUND_HALF_UP
   # See other rounding options here:
   # https://docs.python.org/3/library/decimal.html#rounding-modes
   return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Lab1 problems
#################################################

def isPerfectSquare(n):
    if(n==0): return True
    if(isinstance(n, int) and n>0):
       m = roundHalfUp(math.sqrt(n))
       x = m**2
       if(x==n):
        return True
        
    return False
       

def getKthDigit(n, k):
    if(k==0):
        return(abs(n)%10)
    else:
        return ((abs(n)//(10**k))%10)

def setKthDigit(n, k, d):
    x = getKthDigit(n, k)
    if(k==0):
        difference = (x - d)
    else:
        difference = (10**k)*(x-d)
    if(n<0):
        return n + difference
    return n - difference

        

#################################################
# Lab1 Test Functions
################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed.')

#################################################
# Lab1 Main
################################################

def testAll():
    testIsPerfectSquare()
    testGetKthDigit()
    testSetKthDigit()

def main():
    bannedTokens = (
        #'False,None,True,and,assert,def,elif,else,' +
        #'from,if,import,not,or,return,' +
        'as,break,class,continue,del,except,finally,for,' +
        'global,in,is,lambda,nonlocal,pass,raise,repr,' +
        'try,while,with,yield,' +
        #'abs,all,any,bool,chr,complex,divmod,float,' +
        #'int,isinstance,max,min,pow,print,round,sum,' +
        '__import__,ascii,bin,bytearray,bytes,callable,' +
        'classmethod,compile,delattr,dict,dir,enumerate,' +
        'eval,exec,filter,format,frozenset,getattr,globals,' +
        'hasattr,hash,help,hex,id,input,issubclass,iter,' +
        'len,list,locals,map,memoryview,next,object,oct,' +
        'open,ord,property,range,repr,reversed,set,' +
        'setattr,slice,sorted,staticmethod,str,super,tuple,' +
        'type,vars,zip,importlib,imp,string,[,],{,}')
    cs112_s17_linter.lint(bannedTokens=bannedTokens) # check style rules
    testAll()

if __name__ == '__main__':
    main()
