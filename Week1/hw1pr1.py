# CS5 Gold, hw1pr1
# Filename: hw1pr1.py
# Name: Lawrence
# Problem description: First Python lab!

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):  [2,7,5,9]
answer0 = e[0:2] + pi[-2:]  
print(answer0)

# Problem 1: creating [7,1]
answer1 = e[1:3]           # not the right answer, but a start...
print(answer1)

# Problem 2: creating [9,1,1]
answer2 = pi[5:0:-2]
print(answer2)

# Problem 3: creating [1,4,1,5,9]
answer3 = pi[1:6]
print(answer3)

# Problem 4: creating [1,2,3,4,5]
answer4 = e[2::-2] + pi[0:6:2]
print(answer4)

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# 5. Create hey and store this string in the variable answer5. (3 ops.)
answer5 = h[0] + h[4:6]
print(answer5)

# 6. Create collude and store this string in the variable answer6. (our best: 5 ops.)
answer6 = c[0:4] + m[1:3] + h[4]
print(answer6)

# 7. Create arveyudd and store this string in the variable answer7. (our best: 3 ops.)
answer7 = h[1:6] + m[1:4]
print(answer7)

# 8. Create hardeharharhar and store this string in the variable answer8. (our best: 8 ops.)
answer8 = h[0:3] + m[2] + c[4] + 3*h[0:3]
print(answer8)

# 9. Create legomyego and store this string in the variable answer9. (our best: 8 ops.)
answer9 = c[3:6] + c[1] + m[0] + h[5] + c[4:6] + c[1]
print(answer9)

# 10. Create clearcall and store this string in the variable answer10. (our best: 9 ops.)
answer10 = c[0:5:2] + h[1:3] + c[0] + h[1] + c[2:4]
print(answer10)