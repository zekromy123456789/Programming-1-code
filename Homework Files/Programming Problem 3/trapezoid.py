#******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: Daniel Yadgarov
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# NONE
#
# 
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# overall code was not too bad
#tought i could have done the for loop more efficiently but still works 

import math
#DEFINE YOUR FUNCTION f HERE:
#deined function x
def f(x):
    value = math.sqrt(1+((math.sin(x))**2))
    return value
#CODE FOR GETTING THE INPUT:
#as explaied above
A = int(input('Enter the lower bound: '))
B = int(input('Enter the upper bound: '))
N = int(input('Enter the number of trapezoids: '))
################################################
#INSERT CODE FOR COMPUTING APPROXIMATION OF DEFINITE INTEGRAL USING TRAPEZOIDAL RULE BELOW:  
#set base variables 
deltax = (B-A)/N
x = A
loopvalue = 0
#forloop that calculates the sequence
for i in range(1,N):
    x += deltax
    print(x)
    value = 2*f(x)
    print(value)
    loopvalue += value
#adds the first value of sequence which is not included in the for loop because there 21 parts of loop only 20 included in code
sequence = loopvalue + f(A) + f(B)
#find approximation
approx = (deltax)/2 * sequence

################################################

#CODE FOR PRINTING THE APPROXIMATION TO 8 DECIMAL PLACES
print('The definite integral is approximiately: %.8f'%(approx))