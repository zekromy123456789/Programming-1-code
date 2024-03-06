#******************************************************************************
# solar.py
#******************************************************************************
# Name: Daniel Yadgarov
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#NONE
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#code was relitively simple 
#i think there is a more efficient way to organize the prints using f string but i forgot
# need to look it up
#also not sure if the rounding and formatting was the correct way but it was what i could think of off the top of my head

#asks for width and length
width = float(input('Enter width (in ft): '))
length = float(input('Enter length (in ft): '))
#calcs and prints total and usable sqrft
totalsqrft = length * width
usablesqrft = (.5 * totalsqrft) * .75
print('You have ' + str(totalsqrft) + ' square feet of roof area and ' + str(usablesqrft) + ' square feet usable for panels.')
#calcs and prints total fittable solar panels
fit = int(usablesqrft/21.1)
print('You can fit ' + str(fit) + ' solar panels on your roof.')
#calcs and prints rating
rating = fit * 400
print('You can install a system rated for ' + str(rating) + ' watts.')
#calcs and prints total generation
totalgen = .978 * rating
print('You can generate about ' + str(totalgen) + ' kilowatt-hours in a year.')
#calcs and prints total cost
cost = round(.24 * totalgen, 2)
print("That's equivalent to about $%.2f of electricity." %(cost))