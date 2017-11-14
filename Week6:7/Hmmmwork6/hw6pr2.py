# Starter file for Hmmmwork6, updated for python3
# hw6 problem 2
#
# name(s): Lawrence Mao
# date: 10-22-17
#
#
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# For cs5gold, you'll write a power program
# For cs5black, it's a fibonacci program

# Either way, be sure to call it Problem2 !

# This is a placeholder by that name whose code you'll replace:
Problem2 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 setn r4 1        # set r4 to 1
03 addn r2 -1       # subtract 1 from r2
04 copy r3 r1       # set r3 = r1
05 jeqzn r2 10      # if r2 = 0, jump to line 10
06 jltzn r2 10      # if r2 < 0, jump to line 10
07 mul r3 r3 r1     # r3 = r3 * r1
08 addn r2 -1       # count down r2
09 jgtzn r2 07      # if counter r2 > 0, go to line 7
10 jltzn r2 12      # if r2 < 0, jump to line 12
11 copy r4 r3       # set r4 to r3
12 write r4         # prints r4
13 halt             # stop.
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
