#
# Connect Four: The Board class
# Name: Lawrence Mao
# Date: 11-13-17
#

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """
    
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        W = self.width
        H = self.height
        self.data = [ [' ']*W for row in range(H) ]

        # we do not need to return inside a constructor!
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        H = self.height
        W = self.width
        s = ''   # the string to return
        for row in range(0,H):
            s += '|'   
            for col in range(0,W):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*W+1) * '-'    # bottom of the board
        
        # and the numbers underneath here
        s += '\n'
        for col in range(0, W) :
            s += " " + str(col)
        
        return s+"\n"       # the board is complete, return it
   
    def addMove(self, col, ox): 
        """adds a move"""
        for i in range(self.height):
            if self.data[i][col] != " ":
               self.data[i-1][col]=ox
               return
        self.data[self.height-1][col]=ox 

    def clear(self):
        """self explanitory"""
        self.data =[[" "]*self.width for row in range(self.height)]

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'
            
            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'


    def allowsMove(self, c):
        if c<0 or c>=self.width:
            return False
        if self.data[0][c]!=" ":
            return False
        return True


    def isFull(self):
        for x in range(self.width):
            if self.allowsMove(x)==True:
                return False
        return True

    def delMove(self, c): 
        for i in range(self.height):
            if self.data[i][c]!=" ":
                self.data[i][c]=" "
                return

    def winsFor(self, ox):
        for i in range(self.height):
            for j in range(self.width):
                if inarow_Neast(ox,i,j,self.data,4) or inarow_Nnortheast(ox,i,j,self.data,4) or inarow_Nsouth(ox,i,j,self.data,4) or inarow_Nsoutheast(ox,i,j,self.data,4):
                    return True

        return False

    def hostGame(self):
        print("Welcome to Connect 4!")
        print(self)
        while 1==1:
            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = int(input("X's Choice: "))
            
            
            
            self.addMove(users_col, "X")
            print(self)

            if self.winsFor("X"):
                print("Player X Wins!")
                return
            if self.isFull():
                print("tie")
                return

            users_col = -1
            while self.allowsMove( users_col ) == False:
                users_col = int(input("O's Choice: "))
            self.addMove(users_col,"O")

            print(self)
            if self.winsFor("O"):
                print("Player O Wins!")
                return

            if self.isFull():
                print("tie")
                return

















def inarow_Neast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start-(N-1) < 0 or r_start > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast( ch, r_start, c_start, A, N ):
    """ starting from (row,col) of (r_start,c_start)
        within 2d list-of-lists A (array)
        returns True if there are N ch's in a row and
        returns False otherwise
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start+(N-1) > H-1: return False # out of bounds row
    if c_start < 0 or c_start+(N-1) > W-1: return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True