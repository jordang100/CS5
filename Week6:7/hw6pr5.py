#
# hw6pr5.py - Intro to loops!
#
# Name: Lawrence Mao
#

import random

def countGuesses( hidden ):
    """ 
        uses a while loop to guess hidden, from 0 to 99
        input: hidden, a "hidden" integer from 0 to 99
        output: the number of guesses needed to guess hidden
    """
    guess = random.choice( range(0,100) )  # 0 to 99, inclusive 
    numguesses = 1        # we just made one guess, above
    while guess != hidden:
        guess = random.choice( range(0,100) )   # guess again!
        numguesses += 1   # add one to our number of guesses
    return numguesses

def fac(n):
    """ 
        loop-based factorial function 
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

def power(b,p):
    """
    Returns the value of b**p using a for loop
    b is base and p is nongegative power
    """
    result = 1
    for x in range(p):
        result *= b
    return result

def summed( L ):
    """ 
        loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for e in L:
        result = result + e    # or result += e
    return result

# tests!(summed)
print("summed( [4,5,6] ): should be 15 ==", summed( [4,5,6] ))
print("summed( range(3,10) ): should be 42 ==", summed( range(3,10) ))

def summedOdds(L):
    """
    takes in any list of integers L and returns the sum of all odd elements in L using a loop!
    """
    result = 0
    for x in range(len(L)):
        result += L[x] if L[x] % 2 == 1 else 0
    return result

def unique( L ):
  """ 
      returns whether all elements in L are unique
      input: L, a list of any elements
      output: True, if all elements in L are unique,
      or False, if there is any repeated element
  """
  if len(L) == 0:
    return True
  elif L[0] in L[1:]:
    return False
  else:
    return unique( L[1:] )  # recursion is OK, too!

def untilARepeat (high):
    """
        keeps a list L of all of the integers guessed. Start with L = [ ] !
        keeps looping as long as all of the elements in L are unique (no repeats).
        use a while loop!
        use the unique(L) function that's provided below - it returns a boolean
        within the while loop:
        make a guess in the range(0,high)
        count the number of guesses (add one each time to some kind of counting variable)
        add the guess on to the end of the list L (see below for a hint on this...)
        when the while loop finishes, the function should return the number of guesses needed until it gets a repeat
    """
    L = []
    cnt = 0
    while unique(L):
        L.append(random.choice(range(0, high)))
        cnt += 1
    return cnt

#
# tests for looping factorial
#

print("fac(0): should be 1 ==", fac(0))
print("fac(5): should be 120 ==", fac(5))

#
# tests for power
#

print("power(2,5): should be 32 ==", power(2,5))
print("power(5,2): should be 25 ==", power(5,2))
print("power(42,0): should be 1 ==", power(42,0))
print("power(0,42): should be 0 ==", power(0,42))
print("power(0,0): should be 1 ==", power(0,0))

#
# tests for summedOdds
#
print("summedOdds( [4,5,6] ): should be 5 ==", summedOdds( [4,5,6] ))
print("summedOdds( range(3,10) ): should be 24 ==", summedOdds( list(range(3,10)) ))