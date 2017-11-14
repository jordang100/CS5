#
# hw6 extra - Hmmm: Recursive Fibonacci
# Name: Lawrence Mao
# Date: 10-23-17
#

# Displays Fibonacci sequence up to n-th term using recursive functions
def helper(n):
    """
    helper for Problem6. There is recursion here...
    """
    if n<=1:
        return n
    else:
        return (helper(n-1) + helper(n-2))

def Problem6(n):
    if n <= 0:
        return n
    else:
        for i in range(n):
            print(helper(i))