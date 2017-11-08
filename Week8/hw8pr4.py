#
# TT Securities, Incorporated
# Name: Lawrence Mao
# Date: 10-28-17
#

import math
import time

def makeList(numString):
    """
    Helper for main()
    """
    numString = numString.replace('[', '')
    numString = numString.replace(']', '')
    numList = numString.split(',')
    L = []
    for x in numList:
        L.append(float(x.strip()))
    return L

def main():
    """
    This program should:
    - Offer the user choices 0-6 and 9. 
    - Print a warning message if the integer is not a valid menu option
    - Quit if the user inputs 9
    - Allow the user to input a new list of stock prices, if the user selects choice 0
    - Print a table of days and prices, with labels, if the user selects choice 1
    - Compute the appropriate statistics about the list for choices 2-6
    """
    isQuit = False
    L = []
    while isQuit == False:
        print ("(0) Input a new list")
        print ("(1) Print the current list")
        print ("(2) Find the average price")
        print ("(3) Find the standard deviation")
        print ("(4) Find the min and its day")
        print ("(5) Find the max and its day")
        print ("(6) Your TT investment plan")
        print ("(7) Go on a text-based adventure!")
        print ("(9) Quit")
        print 
        choice = int(input("Enter your choice: "))
        if choice == 9:
            isQuit = True
        elif choice == 0:
            numString = input("Enter a new list of prices: ")
            L = makeList(numString)
        elif choice == 1:
            printList(L)
        elif choice == 2:
            print ("The average price is", averagePrice(L))
        elif choice == 3:
            print ("The st. deviation is", standardDev(L))
        elif choice == 4:
            ans = minDay(L)
            print ("The min is", ans[0], "on day", ans[1])
        elif choice == 5:
            ans = maxDay(L)
            print ("The max is", ans[0], "on day", ans[1])
        elif choice == 6:
            ans = TTPlan(L)
            print ("Your TTS investment strategy is to")
            print 
            print (" Buy on day", ans[0], "at price", L[ans[0]])
            print (" Sell on day", ans[1], "at price", L[ans[1]])
            print (" For a total profit of", ans[2])
        elif choice == 7:
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

        else:
            print ("The choice", choice, "is not an option.")
            print ("Try again")
        print
    print ("See you yesterday!")
def TTPlan (L):
    maxV = -(1 << 30)
    ans = []
    for x in range(len(L)):
        for y in range(1, len(L)):
            if L[y] - L[x] > maxV:
                maxV = L[y] - L[x]
                ans = [x, y, maxV]
    return ans
def maxDay (L):
    maxV = -(1 << 30)
    index = 0
    for x in range(len(L)):
        if L[x] > maxV:
            maxV = L[x]
            index = x
    return [maxV, index]
def minDay (L):
    minV = 1 << 30
    index = 0
    for x in range(len(L)):
        if L[x] < minV:
            minV = L[x]
            index = x
    return [minV, index]
def standardDev (L):
    ave = averagePrice(L)
    s = 0.0
    for x in L:
        s += (x - ave)**2
    return math.sqrt(s / len(L))
def averagePrice (L):
    s = 0.0
    for x in L:
        s += x
    return s / len(L)
def printList (L):
    print
    print ("Day  Price")
    print ("---  -----")
    for x in range(len(L)):
        print ("%3d %5.2f" %(x, L[x]))
    print
    
main()