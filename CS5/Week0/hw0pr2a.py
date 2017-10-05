# coding: utf-8
#
# hw0pr2a.py
#

import random          # imports the library named random
import time            # includes a library named time

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game ...)
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    yesorno = "Y"

    while (yesorno=="y" or yesorno=="Y"): #determines if the program runs again
        user = input("Choose your weapon (rock, paper, or scissors): ")
        comp = random.choice( ['rock','paper','scissors'] )
        print()

        print('the user (you) chose', user) #output choices
        print('the comp (I)   chose', comp)
        print()

        if user == comp: #output results. Yes I know this is a very repetitive way of programming but it's 1 AM. Cut me some slack
            print ("Tie. Now let's see who can tip this scale...")
        elif (user == 'rock' and comp == 'scissors'):
            print ("Wow, you beat me. You're lucky that this game runs on RNG")
        elif (user == 'rock' and comp == 'paper'):
            print ("I win. Better luck next time.")
        elif (user == 'paper' and comp == 'rock'):
            print ("Damn you RNG")
        elif (user == 'paper' and comp == 'scissors'):
            print ("Bless you RNG")
        elif (user == 'scissors' and comp == 'paper'):
            print ("You must be proud of yourself. You beat me in a random chance game")
        elif (user == 'scissors' and comp == 'rock'):
            print ("Ha, my rock obliderates your puny pair of scissors.")
        else:
            print ("Nice try. Thinking you're clever by not entering rock, paper, or scissors")

        yesorno = input("Do you want to play me again? (y/n)")
    return