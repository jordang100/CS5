#
# ASCII Art
# Name: Lawrence Mao
# Date: 10-29-17
#

def printRect(n, m, c):
    """
    takes three arguments, width, height, and symbol, and prints a width by height 
    rectangle of symbols on the screen
    """
    row=n*c
    for a in range(m):
        print (row)