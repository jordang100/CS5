# coding: utf-8
#
# hw0pr2b.py
#

""" 
Title for your adventure:   To Study or to not Study... for the SAT

Notes on how to "win" or "lose" this adventure:
  To win, choose prep over and over again (more than 1 times).
  To tie (up to your interpretation), choose prep exactly 1 times.
  To lose, don't choose prep (AKA less than 1 times).

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        inputs: no inputs    (prompted text doesn't count as input)
        outputs: no outputs  (printing doesn't count as output)
    """
    delay = 10.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
    score = 0            # if score is >= 3, then user aces the sat/act

    yesOrNo = input("Do you wish to proceed with this adventure? (y/n)")

    if yesOrNo == 'y':
        username = input("What do they call you, worthy adventurer? ")

        print()
        print("Welcome,", username, " to the SAT study simulator")
        print("where your actions determine your fate")
        print()

        print("Your quest: To ace the SAT / ACT")
        print()
        test = input("What test shall you overcome? (SAT/ACT) ")
        if test == "ACT":
            print("Aha, the kind that does well under time constraints!")
        elif test == "SAT":
            print("Hm... the kind that enjoys texts which boggle the mind...")
        else:
            print("Each to their own, then.")
        print()

        print("On to the quest!\n\n")
        print("You've just gotten back home from school. You have two options: To complete")
        print("your homework or to study for the " , test, ". Keep in mind, you have the")
        print("test in 2 days.")
        time.sleep(5)
        print()

        choice1 = input("Do you choose the homework or the prep? [homework/prep] ")
        print()

        if choice1 == "homework":
            print("Being the good little student you are, you plop down to your seat and")
            print("finish the homework due tomorrow. After you finish, you are surprised that")
            print("six hours have passed. It is now 12:00 AM! Will you sleep or do some prep?")

        else:  
            print("Being the ambitious person you are, you plop down to your seat and")
            print("prep furiously. After you finish, you are surprised that")
            print("six hours have passed. It is now 12:00 AM! Will you continue studying or sleep?")
            score = score + 1

        choice2 = input("What will you do at this late hour? [sleep/prep]")
        print () 

        if choice2 == 'sleep':
            print("You sleep 7 hours! (Better than what I get...) and wake up refreshed\n\n")
        elif choice2 == 'prep':
            print("Quite the studious one ey? Well then... You sleep 5 hours!... and wake up souless \n\n")
            score = score + 1
        
        time.sleep(delay)

        print ("A month has passed. You have taken the", test, "and now here are the results...")
        time.sleep(delay)

        if test == 'SAT' and score > 1:
            print ("You got a 1600!!!!!! Off to college baby!")
        elif test == 'SAT' and score == 1:
            print ("You got a 1370! Not bad!")
        elif test == 'ACT' and score >1:
            print ("You got a 36!!!!! Off to college baby!")
        elif test == 'ACT' and score == 1:
            print ("You got a 30! Not bad!")
        else:
            print ("You forgot there even was a test and never took it... What a shame, you looked so ambitious.")

        return