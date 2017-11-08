#
# The Read-it-and-Weep Sequence
# Name: Lawrence Mao
# Date: 11-5-17
#

def next( term ): 
    """
    term should be any integer
    the next function should return the next "read" term, which needs to be an int, based on the input term
    """
    if term == 0:
        return 0
    else:
        s_I = str(term)
        result_s = ''
        result_i = 0
        while True:

            if len(s_I) !=0:
                count = 1
                marker = s_I[0]
                for x in range(0,len(s_I)-1):
                    if s_I[x] == s_I[x+1] and s_I[x] == marker:
                        count = count + 1
                result_s = result_s + str(count) + marker

                s_I = s_I[count:]
                continue
            else:
                break

        result_i = int(result_s)
        return (result_i)

def readit(n):
    """
    prints the first n terms in the read-it-and-weep sequence: one per line, starting with a 1. 
    This readit function is unusual in that it does not need to return any value at all: it is 
    being used in order to print things
    """
    num = 1
    print (num)
    while n-1 > 0:
        print (next(num))
        num = next(num)
        n -= 1