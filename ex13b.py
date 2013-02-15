# LCTHW - Exercise 13: Parameters, Unpacking, Variables
# Extra Credit Question 3
# by: Brett A Phillips
# date: February 7, 2013

from sys import argv

script, codeWord = argv

print ""

firstName = raw_input("What is your first name? ")

print ""
if codeWord == "BatCave2" :
	print "%s, you have been cleared for access using codeword %s." % (firstName, codeWord)
else :
	print "%s, permission denied." % (firstName)
	
print ""

