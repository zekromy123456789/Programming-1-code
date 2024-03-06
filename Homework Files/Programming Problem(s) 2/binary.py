#******************************************************************************
# binary.py
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
# pretty simple code but pretty sure i can do the fstring incorporation better
#also would be 100 times better would loops
# 
# 
#import random
import random
#find 8 random numbers between 0 and 1
num1 = random.randrange(0,2)
num2 = random.randrange(0,2)
num3 = random.randrange(0,2)
num4 = random.randrange(0,2)
num5 = random.randrange(0,2)
num6 = random.randrange(0,2)
num7 = random.randrange(0,2)
num8 = random.randrange(0,2)
#calc decimal based on binary number
decimal = num1*128+num2*64+num3*32+num4*16+num5*8+num6*4+num7*2+num8*1
#print results
print("Here's a random example of binary!")
print('The binary number %s %s %s %s %s %s %s %s is the same as the decimal number %s.' %(num1, num2, num3, num4, num5, num6, num7, num8, decimal))