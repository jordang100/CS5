# hw8pr1.py
# Lab 8
#
# Name:Lawrence Mao
#

# keep this import line...
from cs5png3 import *


#
# a test function...
#
def test_fun():
    """ algorithmic image-creation one pixel at a time...
        this is a test function: it should output
        an image named test.png in the same directory
    """
    im = PNGImage(300,200)  # creates an image of width=300, height = 200

    # Nested loops!
    for r in range(200):  # loops over the rows with runner-variable r
        for c in range(300):  # loops over the cols with c
            if  c == r:   
                im.plotPoint( c, r, (255,0,0))
            #else:
            #    im.plotPoint( c, r, (255,0,0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#

def mult(c, n):
    """ 
    mult uses only a loop and addition 
    to multiply c by the positive integer n
    returns the product c times n, but without multiplication. 
    Instead, it should start a value (named result) at 0 and 
    repeatedly add the value of c into that result. It should 
    use a for loop to make sure that it adds c the correct number 
    of times. After the loop finishes, it should return the result, 
    both conceptually and literally. 
    """
    result = 0
    for i in range(n):
        # update the value of result here in the loop
        result = result + c
    return result

def update(c, n):
    """ update starts with z=0 and runs z = z**2 + c
         for a total of n times. It returns the final z. 
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """ inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step
            Then, it returns
            False as soon as abs(z) gets larger than 2
            True if abs(z) never gets larger than 2 (for n iterations)
    """
    z = 0 + 0j
    for i in range(n):
        z = z**2 + c
        if abs(z)>2:
            return False
    return True

def weWantThisPixel(col, row):
    """ a function that returns True if we want
         the pixel at col, row and False otherwise
    """
    if col%10 == 0  and  row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
        to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """ 
        cale accepts
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
        scale returns the floating-point value that
        corresponds to pix
    """
    return float(pix)/pixMax * (floatMax - floatMin) + floatMin

def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    NUMITER = 25  # of updates, from above
    XMIN = -2.0   # the smallest real coordinate value
    XMAX =  1.0   # the largest real coordinate value
    YMIN = -1.0   # the smallest imag coordinate value
    YMAX =  1.0   # the largest imag coordinate value
    width = 1080
    height = 720
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            # Use scale twice:
            #   once to create the real part of c (x)
            scaledX = scale(col, width, XMIN, XMAX)
            #   once to create the imag. part of c (y)
            scaledY = scale(row, height, YMIN, YMAX)
            # THEN, test if it's in the M. Set:
            c = scaledX + scaledY * 1j

            if inMSet(c, NUMITER):
                image.plotPoint(col, row)

    # we looped through every image pixel; we now write the file
    image.saveFile()