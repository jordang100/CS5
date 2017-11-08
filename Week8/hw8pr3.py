#
# Pi from Pie
# Name: Lawrence Mao
# Date: 10-28-17
#

import random
import math

def throwDart():
    """
    Helper that throws dart and returns true or false if in or out of circle
    """
    x = random.uniform( -1.0, 1.0 )
    y = random.uniform( -1.0, 1.0 )
    if x**2 + y**2 <= 1:
        return True
    return False

def forPi( n ):
    """
    It should "throw" n darts at the square. Each time a dart is thrown, the function should print:
    - the number of darts thrown so far
    - the number of darts thrown so far that have hit the circle
    - the resulting estimate of π
    """
    numhits = 0
    for i in range(n):
        if throwDart():
            numhits += 1
        print (numhits, " out of ", i+1, " throws, so pi is ", numhits/(i+1)*4)
    return numhits / n * 4

def whilePi( error ):
    """
    Takes as input a positive floating-point value, error.
    It should then proceed to throw darts at the dartboard (the square) until the absolute 
    difference between the function's estimate of π and the real value of π is less than error.
    whilePi should print:
    - the number of darts thrown so far
    - the number of darts thrown so far that have hit the circle
    - the resulting estimate of π
    """
    throws = 0
    hits = 0
    while throws == 0 or abs(hits/throws*4 - math.pi) > error:
        hits += 1 if throwDart() else 0
        throws += 1
        print (hits," out of ", throws, " throws, so pi is ", hits/(throws)*4)
    return throws