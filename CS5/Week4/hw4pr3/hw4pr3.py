
# hw4pr3.py
# Name: Lawrence 

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
    
def changeGrey(p):
    """ 
    helper for greyscale; makes grey
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    return [ red, red, red ]

def greyscale():
    """ 
    modifies an image to make it greyscale
    """
    Im_pix = getRGB( 'spam.png' )  # read in the in.png image
    print( "The first two pixels of the first row are", )
    print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ [ changeGrey(p) for p in row ] for row in Im_pix ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, 'out.png' )

def binarizePic(p, thresh):
    """ 
    helper for binarize; as name implies, binerizes the picture
    """
    red = p[0]
    green = p[1]
    blue = p[2]
    if (red + green + blue)/3 >= thresh:
        return [ 255, 255, 255 ]
    else:
        return [ 0, 0, 0 ]

def binarize( thresh ):
    """ 
    binarizes an image (makes it black and white) with a threshold of thresh 
    given by the user. This threshold is a brightness value between 0 and 
    255 - if a pixel is greater than the threshold value, then it should turn 
    white, and if its less than the threshold value, then it should turn black
    """
    Im_pix = getRGB( 'spam.png' )  # read in the in.png image
    print( "The first two pixels of the first row are", )
    print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ [ binarizePic(p, thresh) for p in row ] for row in Im_pix ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, 'out.png' )

def flipVert ():
    """
    flips the image on its horizontal axis (the bottom is on the top and the top is on the bottom)
    """
    Im_pix = getRGB( 'spam.png' )  # read in the in.png image
    print( "The first two pixels of the first row are", )
    print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ row for row in Im_pix[::-1] ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, 'out.png' )

def flipHoriz ():
    """
    Flip the image on its vertical axis
    """
    Im_pix = getRGB( 'spam.png' )  # read in the in.png image
    print( "The first two pixels of the first row are", )
    print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of lists (each pixel is [R,G,B])
    New_pix = [ row[::-1] for row in Im_pix ]
    # now, save to the file 'out.png'
    saveRGB( New_pix, 'out.png' )

def mirrorVert():
    """
    Mirror the photo across its horizontal axis (i.e., so that the top part is mirrored upside down on 
    the bottom of the image)
    """

"""
def mirrorVert(picture):
  width = getWidth(picture)
  height = getHeight(picture)
  newPicture = makeEmptyPicture(width, height)
  for yvalue in range(1,  height + 1): 
    for xvalue in range(1, width + 1):
      oldPixel = getPixel(picture, xvalue, yvalue)
      oldColor = getColor(oldPixel)
      newPixel = getPixel(newPicture, xvalue, height-yvalue+1)
      setColor(newPixel, oldColor)
  return newPicture
"""

def mirrorHoriz():
    """
    Same as above, but across the vertical axis. Instead of replacing the bottom rows with the reversed 
    top rows (as you did in mirrorVert), you'll replace the last half of the pixels in every row with 
    the reversed first half of the pixels
    """

def scale():
    """
    Scale the image to half of each of its original dimensions (this will be a quarter of its original area)
    """
    
"""
In addition, if you'd like to create your own effects, we'd love to see them!! Please be sure to include a comment 
or note to the graders explaining what you did. Be creative! Also, feel free to include one or two images of your 
own choosing that you've transformed algorithmically... .
"""