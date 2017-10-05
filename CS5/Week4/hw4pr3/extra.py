
#
# hw4pr3.py
#

from cs5png import *


def testBinaryImage():
    """ run this function to create an 8x8 alien image
        named binary.png
    """
    ALIEN = "0"*8 + "11011011"*2 + "0"*8 + "00001000" + \
            "01000010" + "01111110" + "0"*8
    # this function is imported from cs5png.py
    NUM_ROWS = 8
    NUM_COLS = 8
    binaryIm( ALIEN, NUM_COLS, NUM_ROWS )
    # that should create a file, binary.png, in this
    # directory with the 8x8 image...


def change( p ):
    """ change takes in a pixel (an [R,G,B] list)
        and returns a new pixel to take its place!
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [ 255-red, 255-green, 255-blue ]


def invert():
    """ run this function to read in the in.png image,
        change it, and write out the result to out.png
    """
    Im_pix = getRGB( 'spam.png' )  # read in the in.png image
    print( "The first two pixels of the first row are", )
    print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ [ change(p) for p in row ] for row in Im_pix ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, 'out.png' )
    
# test it out!
invert()
    


