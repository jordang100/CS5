# Name: Lawrence Mao

def numToBaseB (N, B):
    """
    takes as input a non-negative integer N and a base B (between 2 and 10 inclusive); it should 
    return a string representing the number N in base B.
    """
    if N == 0:
        return ''
    else:
        return numToBaseB(N//B, B) + str(int(N)%B)

def baseBToNum(S, B):
    """
    converts a string S from base B to base 10
    """
    if (S == ""):
        return 0
    else:
        return baseBToNum(S[1:], B) + int(S[0]) * (B ** (len(S) - 1))

def baseToBase(B1, B2, s_in_B1):
    """
    takes three inputs: a base B1, a base B2 (both of which are between 2 and 10, inclusive) 
    and s_in_B1, which is a string representing a number in base B1
    """
    return numToBaseB(baseBToNum(s_in_B1, B1), B2)

def add (S, T):
    """
    takes two binary strings S and T as input and returns their sum, also in binary
    """
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB (S, T):
    """
    takes two strings as input. These strings are the representations of binary numbers. 
    Your addB function should return a new string representing the sum of the two input strings. 
    The sum needs to be computed using the "elementary-school" binary addition algorithm, shown above 
    and in class, and not using base conversions. That is - this is purely syntactic addition!
    """
    # base cases!
    if S == "":
        return T
    elif T == "":
        return S

    # There will be four recursive cases - here is the first one:
    if S[-1] == '0' and T[-1] == '0':
        return addB( S[:-1], T[:-1] ) + '0'   # 0 + 0 == 0
    elif S[-1] == "0" or T[-1] == "0":
        return addB(S[:-1],T[:-1]) + "1"

    # three more recursive cases still to specify...
    else:
        return addB(addB(S[:-1],"1"),T[:-1])+"0"

def compress (S):
    """
    takes a binary string S of length less than or equal to 64 as input and returns another 
    binary string as output. The output binary string should be a run-length encoding of the 
    input string
    """
    cnt = 1
    ans = ""
    for x in range(1, len(S)):
        if S[x] != S[x-1]:
            ans += S[x-1]
            pad = numToBaseB(cnt, 2)
            ans += "0"*(7-len(pad)) + pad
            cnt = 1
        else:
            cnt += 1
    pad = numToBaseB(cnt, 2)
    ans += S[len(S)-1] +  "0"*(7-len(pad)) + str(pad)
    return ans
    
def binaryToNum(string):
    """
    Helper for uncompress, as name implies, binary to num
    """
    dec=0
    count=0
    while string != '':
        if string[-1]=='1':
            dec =dec + (2**count)
        count = count +1
        string = string[:-1]
    return dec  

def uncompress(C):
    """
    "inverts" or "undoes" the compressing in your compress function. That is, 
    uncompress(compress(S)) should give back S
    """
    string = ''
    while C != '':
        count = binaryToNum(C[1:8])
        string = string + C[0]*count
        C =C[8:]
    return string