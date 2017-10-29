# Starter file for Hmmmwork6, updated for python3
# hw6 problem 4
#
# date: 
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

# For cs5green, you'll write a recursive power program
# For cs5black, it's the Ex. Cr. "Ackermann" program

#
# GOLD students:
#
# for cs5gold -- don't use these Hmmm starter lines at all!
#     instead, simply overwrite all of the contents of the 
#     triple-quoted string named Problem4 (below)
#     by copying the lines provided in hw6pr4's online description.
#

#
# for cs5green and cs5black:
#
# This is a placeholder by that name whose code you'll replace:
Problem4 = """
00 read r1          # get # from user to r1
01 read r2          # ditto, for r2
02 mul r3 r1 r2     # r3 = r1 * r2
03 write r3         # print what's in r3
04 halt             # stop.
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
