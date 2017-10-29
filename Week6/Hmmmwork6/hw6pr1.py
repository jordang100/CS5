# Starter file for Hmmmwork6, updated for python3
# hw6pr1.py - Hmmm!
#
# problem number: Lab!
#
# name: Lawrence Mao
# date: 10-14-17
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# you'll write unique (or uniq) later in the lab...
def unique(L):
    """
    will take a list as its only input and should return True if that list has only unique elements 
    (no elements repeated) and False otherwise
    """
    s = set()
    for x in L:
        if x in s: 
            return False
        s.add(x)
    return True

# You'll paste your numbers in this triple-quoted string:
NUMBERS = """
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
"""

def test( S ):
    """ test takes in a triple-quoted string, S,
        containing one number per line. Then, test
        returns True if those numbers are all unique
        (or if S is empty); otherwise it returns False
    """
    S = S.strip()    # remove spaces in front  + back of S
    ListOfStrings = S.split()   # split S at each space/newline
    # print("ListOfStrings is", ListOfStrings)
    ListOfIntegers = [ int(s) for s in ListOfStrings ]  # convert each from str to int
    # print("ListOfIntegers is", ListOfIntegers)
    return unique( ListOfIntegers )

# Example1 is an example program that
#   1) asks the user for two inputs
#   2) computes the product of the inputs
#   3) prints out the result (with write)
#   4) stops

Example1 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
"""


# Problem1 is an example program that
#   1) asks the user for an input
#   2) counts up from that input
#   3) keeps going and going...

"""
First, it should ask the user for an input. Hmmm only allows integers between -32768 and 32767. For this problem, you may assume that the input will be positive and less than 30.
Next, your Hmmm program should compute the cube of that input. It should print the result. You'll need multiple multiplications to compute the cube! This will require multiple instructions. In general, it takes a lot more Hmmm instructions to do something than, say, Python lines of code!
Next, your Problem1 should count downward from that resulting value (the cube of the input) one integer at a time. It should print each one until it gets to 0.
When this countdown is at zero, the program should stop. The last value printed should be either 0 or 1. Either is completely OK as the final value.
"""

Problem1 = """
00 read r1          # get # from user to r1
01 write r1         # print the value of r1
02 mul r2 r1 r1     # square r1 and store in r2
03 mul r2 r2 r1     # multiply r2 with r1 to get cube of r1
04 write r2         # print value of r2
05 addn r2 -1       # subtract 1 from r2
06 jgtzn r2 04      # if greater than zero, go to line 04
07 halt             # never halts! [use ctrl-c]
"""


# Lab task #1: Change Problem1 to "the cubic countdown"

# Lab task #2: Write a random-number generator, named Random, here:
#   (Note: this is starter code for the inputs...)

Random = """
00 read r1        # input a
01 read r2        # input c
02 read r3        # input m
03 read r4        # input X_0
04 read r5        # input N
05 jltzn r5 13    # if N less than 0, jump to line 13
06 jeqzn r5 13    # if N equal to 0, jump to line 13
07 addn r5 -1     # countdown for N
08 mul r4 r4 r1   # multiply X_n by multiplier a
09 add r4 r4 r2   # adds X_n to increment c
10 mod r4 r4 r3   # mod r4 by modulus m
11 write r4       # prints value of X_n
12 jnezn r5 06    # if N not equal to 0, jump to line 6
13 halt           # halt
"""

# The values for a and c that I am using to produce 100 distinct output values are 1 and 1.

# This function runs the Hmmm program specified
#
def Hmmm(prog):
    """ This funtion, named Hmmm, takes in a triple-quoted Python string,
        named prog. That string, prog, should be a Hmmm program.

        Note that this file has three already-started Hmmm programs, named
        Example1, Problem1, and Random. See below for how to run them.

        This function will then load the libraries it needs, 
        assemble the Hmmm program into machine language (bits), and
        then run it... . User input will come from the command-line.

        So, to use this function, for example, in ipython:

        In[]: run hw6pr1.py

        In[]: Hmmm( Example1 )
            ... the Hmmm program should be assembled into machine code ...
            ... and then run. (Usually you'll say n (no) to the debugging mode.)
    """
    importlib.reload(hmmmAssembler)  # make sure we're using the latest version
    importlib.reload(hmmmSimulator)  # for both assembler and simulator
    fail = hmmmAssembler.main(prog)  # assemble input into machine code
    if fail is None:
        hmmmSimulator.main(['-n'])   # run that code, don't ask for debugging...