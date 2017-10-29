# Starter file for Hmmmwork6, updated for python3
# hw6 problem 3
#
# date: 10-22-17
#
# Hmmm...
#
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# For cs5gold, you'll write a fibonacci program
# For cs5black, it's a recursive Hanoi-solving program

# Either way, be sure to call it Problem3 !

# This is a placeholder by that name whose code you'll replace:
"""
takes a single input from the user, call it n, and prints the first n Fibonacci numbers.
"""
Problem3 = """
00 read r1          # getting n
01 setn r2 1        # set r2 to 1
02 setn r3 1        # set r3 to 1
03 neg r1 r1        # set r1 to -r1
04 jeqzn r1 12      # if r1 is 0, line 12
05 write r2         # print r2
06 copy r4 r3       # copy r4 from r3
07 add r4 r4 r2     # add r4 and r2
08 copy r2 r3       # copy r2 from r3
09 copy r3 r4       # copy r3 from r4
10 addn r1 1        # counter n up 1
11 jumpn 04         # back to line 4
12 halt             # stop
"""


# This function runs the Hmmm program specified by prog
#
def Hmmm(prog):
    """ This funtion, named Hmmm, takes in a triple-quoted Python string,
        named prog. That string, prog, should be a Hmmm program.

        See the docstring in hw6pr1.py for a full explanation!
    """
    importlib.reload(hmmmAssembler)  # make sure we're using the latest version
    importlib.reload(hmmmSimulator)  # for both assembler and simulator
    fail = hmmmAssembler.main(prog)  # assemble input into machine code
    if fail is None:
        hmmmSimulator.main(['-n'])   # run that code, don't ask for debugging...