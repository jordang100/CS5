# CS5 Gold, Lab1 part 2
# Filename: hw1pr2.py
# Name: Lawrence
# Problem description: First few functions!

from math import *

def dbl(x):
    """  
         output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x

def sq(x):
    """
        Write sq(x), which takes in a number named x as input. Then, sq should output the square of its input. 
        Note that this is the square, not the square root. (The square is x times itself... .)
    """
    return x*x

def interp(low, high, fraction):
    """
        interp(low,hi,fraction) takes in three numbers, low, high, and fraction, and should return the 
        Floating-point value that is fraction of the way between low and hi.
    """
    return (high-low)*fraction + low

def checkends(s):
    """
        Write a function checkends(s), which takes in a string s and returns True if the first character in s is the same as the last character in s. It returns False otherwise. The checkends function does not have to work on the empty string (the string '').
    """
    if s[0] == s[-1]:
        return True
     
    else:
        return False

def flipside(s):
    """
        Write a function flipside(s), which takes in a string s and returns a string whose first half is s's second
        half and whose second half is s's first half. If len(s) (the length of s) is odd, the first half of the 
        input string should have one fewer character than the second half. (Accordingly, the second half of the 
        output string will be one shorter than the first half in these cases.)
    """
    if len(s)%2 == 0:
        length2 = int(len(s)/2)
        return s[length2:len(s)+1] + s[0:length2]

    else:
        length2 = int((len(s)-1)/2)
        return s[length2:] + s[0:length2]

def convertFromSeconds(s):
    days = s // (24*60*60)  # # of days
    s = s % (24*60*60)     # the leftover
    hours = (s%86400)//3600
    minutes = (s%3600)//60
    seconds = (s%60)
    return [days, hours, minutes, seconds]