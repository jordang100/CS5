#
# hw9pr2.py
# Name: Lawrence Mao
# Date: 10-31-17
#

# here is a function for printing 2D arrays
#  (lists-of-lists) of data

def print2d( A ):
    """ print2d prints a 2D array, A
        as rows and columns
        input: A, a 2D list of lists
        output: None (no return value)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR): # NR = =numrows
        for c in range(NC):  # NC == numcols
            print(A[r][c], end = ' ')
        print()

    return None  # this is implied anyway,
    # when no return statement is present

# some tests for print2d
A = [ ['X',' ','O'], ['O','X','O'] ]
print("2-row, 3-col A is")
print2d(A)

A = [ ['X','O'], [' ','X'], ['O','O'], ['O','X'] ]
print("4-row, 2-col A is")
print2d(A)


# create a 2D array from a 1D string
def createA( NR, NC, s ):
    """ returns a 2D array with
        NR rows (numrows) and
        NC cols (numcols)
        using the data from s: across the
        first row, then the second, etc.
        We'll only test it with enough data!
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [ s[0] ] # add that char
            s = s[1:]   # get rid of that first char
        A += [newrow]
    return A

# a couple of tests for createA:
A = [ ['X',' ','O'], ['O','X','O'] ]
newA = createA( 2, 3, 'X OOXO')
print("Is newA == A? Should be True:", newA == A)

A = [ ['X','O'], [' ','X'], ['O','O'], ['O','X'] ]
newA = createA( 4, 2, 'XO XOOOX')
print("Is newA == A? Should be True:", newA == A)

# Homework Starts Here: inarrow_3
def inarow_3east( ch, r_start, c_start, A ):
    """
    this should start from r_start and c_start and check for three-in-a-row eastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start][c_start+i] != ch:
            return False
    return True

def inarow_3south( ch, r_start, c_start, A ):
    """
    this should start from r_start and c_start and check for three-in-a-row southward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+2 >= h or c_start < 0 or c_start >= w:
        return False
    for i in range(3):
        if A[r_start+i][c_start] != ch:
            return False
    return True

def inarow_3southeast( ch, r_start, c_start, A ):
    """
    this should start from r_start and c_start and check for three-in-a-row southeastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+2 >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True

def inarow_3northeast( ch, r_start, c_start, A ):
    """
    this should start from r_start and c_start and check for three-in-a-row northeastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start-1 < 0 or r_start >= h or c_start < 0 or c_start+2 >= w:
        return False
    for i in range(3):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True

# tests of inarow_3east
A = createA( 3, 4, 'XXOXXXOOOOOO')
#print2d(A)
print("inarow_3east('X',0,0,A): False ==", inarow_3east('X',0,0,A))
print("inarow_3east('O',2,1,A):  True ==", inarow_3east('O',2,1,A))
print("inarow_3east('X',2,1,A): False ==", inarow_3east('X',2,1,A))
print("inarow_3east('O',2,2,A): False ==", inarow_3east('O',2,2,A))

# tests of inarow_3south
A = createA( 4, 4, 'XXOXXXOXXOO OOOX')
#print2d(A)
print("inarow_3south('X',0,0,A):    True ==", inarow_3south('X',0,0,A))
print("inarow_3south('O',2,2,A):   False ==", inarow_3south('O',2,2,A))
print("inarow_3south('X',1,3,A):   False ==", inarow_3south('X',1,3,A))
print("inarow_3south('O',42,42,A): False ==", inarow_3south('O',42,42,A))

# tests of inarow_3southeast
A = createA( 4, 4, 'XOOXXXOXX XOOOOX')
#print2d(A)
print("inarow_3southeast('X',1,1,A):  True ==", inarow_3southeast('X',1,1,A))
print("inarow_3southeast('X',1,0,A): False ==", inarow_3southeast('X',1,0,A))
print("inarow_3southeast('O',0,1,A):  True ==", inarow_3southeast('O',0,1,A))
print("inarow_3southeast('X',2,2,A): False ==", inarow_3southeast('X',2,2,A))

# tests of inarow_3northeast
A = createA( 4, 4, 'XOXXXXOXXOXOOOOX')
#print2d(A)
print("inarow_3northeast('X',2,0,A):  True ==", inarow_3northeast('X',2,0,A))
print("inarow_3northeast('O',3,0,A):  True ==", inarow_3northeast('O',3,0,A))
print("inarow_3northeast('O',3,1,A): False ==", inarow_3northeast('O',3,1,A))
print("inarow_3northeast('X',3,3,A): False ==", inarow_3northeast('X',3,3,A))

def inarow_Neast( ch, r_start, c_start, A, N ):
    """
    this should start from r_start and c_start and check for N-in-a-row eastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start][c_start+i] != ch:
            return False
    return True

def inarow_Nsouth( ch, r_start, c_start, A, N ):
    """
    this should start from r_start and c_start and check for N-in-a-row southward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start >= w:
        return False
    for i in range(N):
        if A[r_start+i][c_start] != ch:
            return False
    return True

def inarow_Nsoutheast( ch, r_start, c_start, A, N ):
    """
    this should start from r_start and c_start and check for N-in-a-row southeastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start < 0 or r_start+N-1 >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start+i][c_start+i] != ch:
            return False
    return True

def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    """
    this should start from r_start and c_start and check for N-in-a-row northeastward of element ch, returning True or False, as appropriate
    """
    h = len(A)
    w = len(A[0])
    if r_start-N+1 < 0 or r_start >= h or c_start < 0 or c_start+N-1 >= w:
        return False
    for i in range(N):
        if A[r_start-i][c_start+i] != ch:
            return False
    return True
    
# tests of inarow_Neast
A = createA( 5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
# print2d(A)
print("inarow_Neast('O',1,1,A,4):  True ==", inarow_Neast('O',1,1,A,4))
print("inarow_Neast('O',1,3,A,2):  True ==", inarow_Neast('O',1,3,A,2))
print("inarow_Neast('X',3,2,A,4): False ==", inarow_Neast('X',3,2,A,4))
print("inarow_Neast('O',4,0,A,5):  True ==", inarow_Neast('O',4,0,A,5))

# tests of inarow_Nsouth
A = createA( 5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
# print2d(A)
print("inarow_Nsouth('X',0,0,A,5): False ==", inarow_Nsouth('X',0,0,A,5))
print("inarow_Nsouth('O',1,1,A,4):  True ==", inarow_Nsouth('O',1,1,A,4))
print("inarow_Nsouth('O',0,1,A,6): False ==", inarow_Nsouth('O',0,1,A,6))
print("inarow_Nsouth('X',4,3,A,1):  True ==", inarow_Nsouth('X',4,3,A,1))

# tests of inarow_Nsoutheast
A = createA( 5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX' )
# print2d(A)
print("inarow_Nsoutheast('X',1,1,A,4):  True ==", inarow_Nsoutheast('X',1,1,A,4))
print("inarow_Nsoutheast('O',0,1,A,3): False ==", inarow_Nsoutheast('O',0,1,A,3))
print("inarow_Nsoutheast('O',0,1,A,2):  True ==", inarow_Nsoutheast('O',0,1,A,2))
print("inarow_Nsoutheast('X',3,0,A,2): False ==", inarow_Nsoutheast('X',3,0,A,2))

# tests of inarow_Nnortheast
A = createA( 5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX' )
# print2d(A)
print("inarow_Nnortheast('X',4,0,A,5):  True ==", inarow_Nnortheast('X',4,0,A,5))
print("inarow_Nnortheast('O',4,1,A,4):  True ==", inarow_Nnortheast('O',4,1,A,4))
print("inarow_Nnortheast('O',2,0,A,2): False ==", inarow_Nnortheast('O',2,0,A,2))
print("inarow_Nnortheast('X',0,3,A,1): False ==", inarow_Nnortheast('X',0,3,A,1))