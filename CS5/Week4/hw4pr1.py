# CS5 Gold/Black, hw4pr1
# Filename: hw4pr1.py
# Name: Lawrence Mao
# Problem description: Binary <-> decimal conversions

def isOdd( N ):
    """
    determines if N is odd or even
    """
    if N%2 == 0:
        return False
    else:
        return True

def numToBinary(N):
    """
    converting decimal numbers into binary form one bit at a time
    """
    if N == 0:
        return ''
    else: 
        return numToBinary(N//2) + str(N%2)

def binaryToNum(S):
    """
    converting from binary to number
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':  
        return 2*binaryToNum(S[:-1]) + 1

    else: # last digit must be '0'
        return 2*binaryToNum(S[:-1]) + 0

def increment(S):
    """
    accepts an 8-character string S of 0's and 1's and returns the next largest number in base 2
    """
    if S == '11111111':
        return '00000000'
    newS = numToBinary(binaryToNum(S) + 1)
    diff = len(S) - len(str(newS))
    newS = diff * '0' + newS
    return newS

def count(S, n):
    """
    accepts an 8-character binary input string and then begins counts n times upward from S, printing as it goes
    """
    print(S)
    if n == 0:
        return
    else:
        count(increment(S),n-1)

def numToTernary(N):
    """
    In a comment or triple-quoted string, explain what the ternary representation is for the value 59, and why it is so.
    59 is 2012 because 2*27 + 0*9 + 1*3 + 2*1 = 59
    returns a ternary string representing the value of the argument N
    """
    if N == 0:
        return ''
    else: 
        return numToTernary(N//3) + str(N%3)

def ternaryToNum(S):
    """
    return the value equivalent to the argument string S, when S is interpreted in ternary
    """
    if S == '':
        return 0

    # if the last digit is a '2'...
    elif S[-1] == '2':
        return 3*ternaryToNum(S[:-1]) + 2

    # if the last digit is a '1'...
    elif S[-1] ==  '1':  
        return 3*ternaryToNum(S[:-1]) + 1

    else: # last digit must be '0'
        return 3*ternaryToNum(S[:-1]) + 0

def balancedTernaryToNum(S):
    """
    return the decimal value equivalent to the balanced ternary string S
    """
    if S == '':
        return 0

    # if the last digit is a '-'...
    elif S[-1] == '-':
        return 3*balancedTernaryToNum(S[:-1]) - 1

    # if the last digit is a '+'...
    elif S[-1] ==  '+':  
        return 3*balancedTernaryToNum(S[:-1]) + 1

    else: # last digit must be '0'
        return 3*balancedTernaryToNum(S[:-1]) + 0

def numToBalancedTernary(N):
    """
    return a balanced ternary string representing the value of the argument N
    """
    if N == 0:
        return ''

    elif N%3 == 1:
        return numToBalancedTernary((N-1)/3) + '+'
    
    elif N%3 == 0:
        return numToBalancedTernary(N/3) + '0'

    elif N%3 == 2:
        return numToBalancedTernary((N+1)/3) + '-'