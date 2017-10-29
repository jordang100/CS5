#
# hw2pr1.py
#
# Name:
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *

def tri( n ):
    """ draws n 100-pixel sides of an equilateral triangle
        note that s can be different than 3 (!)
    """
    shape( 'turtle' )
    width(10)
    color( 'darkgreen')
    if n == 0:
        return # stop drawing here
    else:
        forward(100)
        left(120)
        tri( n-1 )  # recurse to draw the rest of the sides!

def spiral( initialLength, angle, multiplier ):
    """ spiral-drawing function; Inputs:
        initialLength = the length of the first leg of the spiral
        angle = the angle, in degrees, turned after each spiral's leg
        multiplier = the fraction by which each leg of the spiral changes
    """
    if initialLength <= 1:          
        return     # stops this call to spiral
    else:
        forward(initialLength)
        left(angle)
        spiral(initialLength * multiplier, angle, multiplier)

def chai(size):
    """ our chai function! """
    if (size < 5): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)

        chai( size/2 )

        right(90)
        forward(size)
        left(90)

        chai( size/2 )

        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

def svtree( trunklength, levels ):
    """ svtree: draws a side-view tree
        trunklength = the length of the first line drawn ("the trunk")
        levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        # draw the original trunk (1 line)
        forward(trunklength)
        # turn a little bit to position the first subtree (1 line)
        left(30)
        # recurse! with both a smaller trunk and levels (1 line)
        svtree(trunklength/2, levels - 1)
        # turn the other way  to position the second subtree (1 line)
        right(60)
        # recurse again! (1 line)
        svtree(trunklength/2, levels - 1)
        # turn and go backwards (2 steps: 2 lines)
        left(30)
        backward(trunklength)

def snowflake(sidelength, levels):
    """ fractal snowflake function - complete.
          sidelength: pixels in the largest-scale triangle side
          levels: the number of recursive levels in each side
    """
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)
    flakeside( sidelength, levels )
    left(120)

def flakeside(sidelength, levels):
    if levels == 0:
        forward(sidelength)
    else: 
        nsl = sidelength/3
        flakeside(nsl, levels - 1)
        right(60)
        flakeside(nsl, levels - 1)
        left(120)
        flakeside(nsl, levels - 1)
        right(60)
        flakeside(nsl, levels - 1)
        right(120)
        
def fortytwo(number):
    if number == 0:
        return
    
    else:
        #Creating 4
        down()
        right(90)
        forward(10)
        left(90)
        forward(15)
        left(90)
        forward(10)
        backward(20)
        up()
        right(90)
        forward (3)

        #Creating 2
        left(90)
        forward(20)
        down()
        right(90)
        forward(15)
        right(90)
        forward(10)
        right(90)
        forward(15)
        left(90)
        forward(10)
        left(90)
        forward(15)
        up()
        forward(10)
        left(90)
        forward(20)
        right(90)

        fortytwo(number - 1)