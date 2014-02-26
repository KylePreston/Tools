# Seattle Tip Calculator
# Kyle Preston 2013

bill = input ('\nWhat is the total before tax? ')

# Sales tax in Seattle, WA (2013)
tax = 0.095

bill = bill + bill*tax
print ("\nWith Seattle tax, that makes the total $%.2f." % bill)

tip = input('Enter the percentage of tip you want to leave: ')

if (tip > 40):
	print ("\nWow! Must have been excellent service!")

total = bill + bill*(tip/100.)
tip = bill * (tip/100.)

print ("\nYour total is: $%.2f." % total)
print ("and your tip amount is: $%.2f.\n" % tip)
