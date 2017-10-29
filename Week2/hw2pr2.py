# CS5 Gold, hw2pr2
# Filename: hw2pr2.py
# Name: Lawrence Mao
# Problem description: Sleepwalking student

import random  
import sys
import time
sys.setrecursionlimit(50000)

def rs():
    """
        rs chooses a random step and returns it 
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])

def rwpos( start, nsteps ):
    """
        no loops, use recursion. number of nsteps taken from start position
    """
    nsteps -= 1
    start += rs()
    print("start is", start)
    if nsteps == 0:
        return start
    return rwpos(start, nsteps)

def rwsteps( start, low, hi ):
    """
        simulates a random walk. Int start = starting position, int low, smallest value sleepwalker
        will be allowed to wander to, and int hi, the highest value sleepwalker will be allowed to wander to.
    """
    if start == low or start == hi:
        
        return 1
    else:
        start = start + rs()
       
        x=hi-low
        l=start-low
        h=hi-start
        print('|'+'_'*l+'S'+'_'*h+'|')
        
        sys.stdout.flush()   # forces Python to print everything _now_
        time.sleep(0.1)      # and then sleep for 0.1 seconds

        rest_of_steps = rwsteps(start,low,hi)+1
        
        return rest_of_steps

def rwposPlain(start, nsteps):
    """
    does not print any debugging or explanatory information. Rather, it should simply return the final position
    """
    if nsteps==0:
        return start
    else:
        return rwposPlain(start+rs(),nsteps-1)

def ave_signed_displacement( numtrials ):
    """
    runs rwposPlain(0,100) for numtrials times and return the average of the result
    """
    LC = [ rwposPlain(0,100) for x in range(numtrials) ] 
    
    return sum(LC)/len(LC) #Averages Signed Displacement

def ave_squared_displacement( numtrials ):
    """
    run rwposPlain(0,100) for numtrials times and return the average of the squares of the results
    """
    LC = [ rwposPlain(0,100)**2 for x in range(numtrials) ]
    
    return sum(LC)/len(LC) #Averages Squared Displacement

"""
    In order to compute the average signed displacement for
    a random walker after 100 random steps, I ran random walker 100 steps 1000 times.
    This returned a list. I divided the sum of the list by its length, giving the average.
    I then did the average of 100,000 trials. Almost immediately, my computer's fans became twice as loud...

    In [86]: ave_signed_displacement(1000)

    Out[86]: -0.16

    In [87]: ave_signed_displacement(1000)

    Out[87]: 0.12

    In [88]: ave_signed_displacement(100000)

    Out[88]: 0.03492

    The average random signed displacement is around 0. 
"""
"""
     In order to compute the average squared displacement for
     a random walker after 100 random steps, I ran random walker and sqaured the result. Then I did this
     1000 times and averaged the results.

     In [90]: ave_squared_displacement(1000)
     Out[90]: 101.536

     In [91]: ave_squared_displacement(1000)
     Out[91]: 93.328

     Average squared displacement is around 100.
"""