#
# hw9pr1.py
# Name: Lawrence Mao
# Date: 10-31-17
#

#
# Here is a function that will help start hw9pr1's lab:
#

import random

def createOneRow(width):
    """ 
    Returns one row of zeros of width "width"...
    You might use this in your createBoard(width, height) function 
    """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ 
    Returns a 2d array with "height" rows and "width" cols 
    """
    A = []
    for row in range(height):
        A += [[0]*width]        # use the above fun. so that SOMETHING is one row!!
    return A

def printBoard(A):
    """ 
    This function prints the 2d list-of-lists A
    """
    for row in A:               # row is the whole row
        for col in row:         # col is the individual element
            print(col,end='')   # print that element
        print() 

def diagonalize(width, height):
    """ 
    Creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    but, only in the * interior * of the 2d array
    """
    A = createBoard(width, height)

    for row in range(1,height-1):
        for col in range(1,width-1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    """
    Returns a 2d array that has all live cells—with the value of 1—except 
    for a one-cell-wide border of empty cells (with the value of 0) around 
    the edge of the 2d array
    """
    A = createBoard(w, h)

    for row in range(1,h-1):
        for col in range(1,w-1):
            if 0 < row < h-1 and 0 < col < w-1:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def randomCells(w, h):
    """
    Returns an array of randomly-assigned 1's and 0's except that the outer edge of the array is still completely empty (all 0's) as in the case of innerCells
    """
    A = createBoard(w, h)

    for row in range(1,h-1):
        for col in range(1,w-1):
            if 0 < row < h-1 and 0 < col < w-1:
                A[row][col] = random.choice([0, 1])
            else:
                A[row][col] = 0
    return A

def copy(A):
    """ 
    Returns a DEEP copy of the 2d array A 
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )

    for row in range(1,height-1):
        for col in range(1,width-1):
            newA[row][col] = A[row][col]
            # what single line should be here to copy each 
            # element of A into the corresponding element of newA?

    return newA

def innerReverse(A):
    """
    Takes an old 2d array A (an old "generation") and then creates a new 
    generation newA of the same shape and size, using createBoard or copy.
    The new generation should be the "opposite" of A's cells everywhere except 
    on the outer edge
    """

    height = len(A)
    width = len(A[0])
    newA = createBoard( width, height )

    for row in range(1,height-1):
        for col in range(1,width-1):
            if 0 < row < len(A)-1 and 0 < col < len(A[0])-1:
                newA[row][col] = (A[row][col] + 1) % 2
            else:
                newA[row][col] = 0
    return newA

def countNeighbors(row, col, A):
    """
    return the number of live neighbors for a cell in the board A at a particular row and col
    """
    cnt = 0
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            if abs(x) + abs(y) != 0:
                cnt += A[row+x][col+y]
    return cnt

def next_life_generation (A):
    """ 
    makes a copy of A and then advances one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays at 0.
    """
    w = len(A[0])
    h = len(A)
    B = createBoard(w, h)
    for i in range(h):
        for j in range(w):
            if 0 < i < h-1 and 0 < j < w-1:
                cnt = countNeighbors(i, j, A)
                if cnt < 2 or cnt > 3:
                    B[i][j] = 0
                elif cnt == 3:
                    B[i][j] = 1
                else:
                    B[i][j] = A[i][j]
            else:
                B[i][j] = 0
    return B