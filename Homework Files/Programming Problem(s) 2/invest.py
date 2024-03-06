#******************************************************************************
# invest.py
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
# Generally i thought this was a pretty interesting assignment the concept of e was interesting having to import it
# I used teh same rounding method as i did in the first assignment

#imports the number e
from math import e
#ask initial question:
choice = input("Enter C for continuous or N for noncontinuous: ")
#choose route depending on first choice
if choice == "C":
    #ask questions for C
    IA = float(input("Enter the initial amount: "))
    FTP = float(input("Enter the first time period in years: "))
    FGR = float(input("Enter the first growth rate as a percentage: "))
    STP = float(input("Enter the second time period in years: "))
    SGR = float(input("Enter the second growth rate as a percentage: "))
    #calculate ending value
    FT = IA * (e ** ((FGR/100)*FTP))
    ST = FT * (e ** ((SGR/100)*STP))
    #print ending value
    print("The ending value is %.2f" %(ST))
elif choice == "N":
    #ask questions for N
    IA = float(input("Enter the initial amount: "))
    FTP = float(input("Enter the first time period in years: "))
    FGR = float(input("Enter the first growth rate as a percentage: "))
    TCPY1 = float(input("Enter the number of times compounded per year: "))
    STP = float(input("Enter the second time period in years: "))
    SGR = float(input("Enter the second growth rate as a percentage: "))
    TCPY2 = float(input("Enter the number of times compounded per year: "))
    #calculate ending value
    FT = IA * ((1+((FGR/100)/TCPY1)) ** (TCPY1*FTP))
    ST = FT * ((1+((SGR/100)/TCPY2)) ** (TCPY2*STP))
    #print ending value
    print("The ending value is %.2f" %(ST))