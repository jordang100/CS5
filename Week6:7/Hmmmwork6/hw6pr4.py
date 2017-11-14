# Starter file for Hmmmwork6, updated for python3
# hw6 problem 4
#
# date: 10-28-17
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
00 read r2         # read input r1.    
01 read r1         # read input r2.
02 setn r15 42     # 42 is the beginning of the stack, put that address in r15.
03 call r14 6      # begin function at line 6, but first put next address (03) into r14.
04 jumpn 22        # Let's defer final output to line 22
05 nop             # no operation—but useful for squeezing in an extra input
06 jnez r1 9       # BEGINNING OF FACTORIAL FUNCTION! Check if r1 is non-zero. If it is go to line 8 and do the real recursion!
07 setn r13 1      # otherwise, we are at the base case: load 1 into r13 and
08 jumpr r14       # return to where we were called from (address is in r14)
09 storer r1 r15   # place r1 onto the stack
10 addn r15 1      # increment stack pointer
11 storer r14 r15  # place r14 onto the stack
12 addn r15 1      # increment stack pointer
13 addn r1 -1      # change r1 to r1-1 in preparation for recursive call
14 call r14 6      # recursive call to factorial, which begins at line 5—but first store next memory address in r14
15 addn r15 -1     # we're back from the recursive call! Restore goods off the stack.
16 loadr r14 r15   # restoring r14 (return address) from stack
17 addn r15 -1     # decrement stack pointer
18 loadr r1 r15    # restoring r1 from stack
19 mul r13 r13 r2  # now for the multiplication 
20 jumpr r14       # and return!
21 nop             # nothing
22 write r13       # write the final output
23 halt            # halt
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
