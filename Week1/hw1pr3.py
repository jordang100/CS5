# CS5 Gold, hw1pr3
# Filename: hw1pr3.py
# Name: Lawrence Mao
# Problem description: Function Frenzy!

#
# leng example from class
#

def leng( s ):
    """ leng outputs the length of s
            input: s, which can be a string or list

    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng( s[1:] )

def mult (n,m):
    """
    Using recursion to multiply two integers n and m
    """
    if m < 0:
        m=m*-1
        n=n*-1
    if m == 0:
        return 0
    else:
        return n + mult(n,m-1)

def dot (L,K):
    """
    Find dot product of two matrices L and K
    """
    if leng(L) == 0 or leng(K) == 0 or leng(K) != leng(L):
        return 0
    else:
        return L[0] * K[0] + dot(L[1:],K[1:])

def ind(e, L):
    """
    Find location of e in sequence L. If e not in L, return length of L
    """
    if e not in L:
        return len(L)
    elif L[0]==e:
        return 0
    else:
        return 1+ind(e,L[1:])

def letterScore(let):
    """
    Turns character let into a number value. If not a valid letter, result is 0.
    """
    if let in 'aeilnorstu':
        return 1
    elif let in 'dg':
        return 2
    elif let in 'bcmp':
        return 3
    elif let in 'fhvwy':
        return 4
    elif let in 'k':
        return 5
    elif let in 'jx':
        return 8
    elif let in 'qz':
        return 10
    else:
        return 0

def scrabbleScore(S):
    """
    Take in string S and computes score using previous function
    """
    if S == "":
        return 0
    else: 
        return letterScore(S[0])+scrabbleScore(S[1:])

def converter (S):
    """
    Converts from DNA to RNA
    """
    if S=='A':
        return 'U'
    if S=='C':
        return 'G'
    if S ==  'G':
       return 'C'
    if S=='T':
        return 'A'
    else:
        return ''

def transcribe(S):
    """
    Using converter, transcribes everything
    """
    if S == '':
        return''
    else:
         return converter(S[0])+transcribe(S[1:])

#
# I finished all of the CodingBat STRING problems.
#

#
# I finished all of the CodingBat LIST problems.
#