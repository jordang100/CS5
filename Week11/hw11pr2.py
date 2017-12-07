#
# Game AI: Connect Four
# Name: Lawrence Mao
# Date: 11-14-17
#

import random

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
        
    #################################
    ### AI SECTION STARTS HERE!!! ###
    #################################
    
    def colsToWin( self, ox ):
        """
        return the list of columns where ox can move in the next turn in order to win and finish the game
        """
        s = []
        for i in range(self.width):
            if ox == 'X':
                if self.allowsMove(i)==True:
                    self.addMove(i, 'X')
                    if self.winsFor('X'):
                        s.append(i)
                    self.delMove(i)
                    
            elif ox == 'O':
                if self.allowsMove(i) == True:
                    self.addMove(i, 'O')
                    if self.winsFor('O'):
                        s.append(i)
                    self.delMove(i)
        return s

    def aiMove( self, ox ):
        """
        return a single integer, which must be a legal column in which to make a move
        - If there is a way for ox to win, then aiMove MUST return that move (that column number)
        - If here IS a way for ox to block the opponent's four-in-a-row, then aiMove MUST return 
        a move that blocks its opponent's four-in-a-row
        - If there is NO way for ox to win NOR a way for ox to block the opponent from winning, then 
        aiMove should return a move of your (the programmer's) choice -- but it must be a legal move. 
        We won't call aiMove when the board is full
        """
        if ox == 'X':
            if self.colsToWin('X') != []: #if there is a possibility to win
                val = self.colsToWin('X')
                return random.choice(val) #return random option in colsToWin
            else: #if no winning chance
                if self.colsToWin('O') != []: #see if enemy can win
                    val = self.colsToWin('O')
                    return random.choice(val) #block random option in enemy's colsToWin
                else: #if enemy and you can't win
                    if self.allowsMove(3) == True:
                        return 3 #drop in column 3, it's a safe bet
                    elif self.allowsMove(2) == True:
                        return 2
                    elif self.allowsMove(4) == True:
                        return 4
                    elif self.allowsMove(5) == True:
                        return 5
                    elif self.allowsMove(1) == True:
                        return 1
                    elif self.allowsMove(0) == True:
                        return 0
                    elif self.allowsMove(6) == True:
                        return 6

        elif ox == 'O':
            if self.colsToWin('O') != []: #if there is a possibility to win
                val = self.colsToWin('O')
                return random.choice(val) #return random option in colsToWin
            else: #if no winning chance
                if self.colsToWin('X') != []: #see if enemy can win
                    val = self.colsToWin('X')
                    return random.choice(val) #block random option in enemy's colsToWin
                else: #if enemy and you can't win
                    if self.allowsMove(3) == True:
                        return 3 #drop in column 3, it's a safe bet
                    elif self.allowsMove(2) == True:
                        return 2
                    elif self.allowsMove(4) == True:
                        return 4
                    elif self.allowsMove(5) == True:
                        return 5
                    elif self.allowsMove(1) == True:
                        return 1
                    elif self.allowsMove(0) == True:
                        return 0
                    elif self.allowsMove(6) == True:
                        return 6

    def hostGame(self, choice):
        """
        if choice == 1 hosts a Connect 4 game in which the computer controls X by using the aiMove method
        if choice == 2 hosts a Connect 4 game in which the player controls both X and O
        if choice == 0 hosts a Connect 4 game in which the AI controlls both X and O
        """
        print("Welcome to Connect 4!")
        print(self)
        if choice == 1:
            while 1==1:
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = int(input("Your Choice (O): "))
                
                self.addMove(users_col, "O")
                print(self)

                if self.winsFor("O"):
                    print("Player O Wins!")
                    return
                if self.isFull():
                    print("tie")
                    return

                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = self.aiMove('X')

                self.addMove(users_col,"X")
                print(self)

                if self.winsFor("X"):
                    print("Player X Wins!")
                    return

                if self.isFull():
                    print("tie")
                    return

        if choice == 2:
            while 1==1:
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = int(input("Your Choice (O): "))
                
                self.addMove(users_col, "O")
                print(self)

                if self.winsFor("O"):
                    print("Player O Wins!")
                    return
                if self.isFull():
                    print("tie")
                    return

                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = int(input("Your Choice (X): "))

                self.addMove(users_col,"X")
                print(self)

                if self.winsFor("X"):
                    print("Player X Wins!")
                    return

                if self.isFull():
                    print("tie")
                    return

        if choice == 0:
            while 1==1:
                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = self.aiMove('O')
                
                self.addMove(users_col, "O")
                print(self)

                if self.winsFor("O"):
                    print("Player O Wins!")
                    return
                if self.isFull():
                    print("tie")
                    return

                users_col = -1
                while self.allowsMove( users_col ) == False:
                    users_col = self.aiMove('X')

                self.addMove(users_col,"X")
                print(self)

                if self.winsFor("X"):
                    print("Player X Wins!")
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