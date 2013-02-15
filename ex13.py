# LCTHW - Exercise 13: Parameters, Unpacking, Variables
# by: Brett A PHillips
# date: February 7, 2013

from sys import argv
#NOTE: 'sys' is a module (or library) that you import into your program

#NOTE: So what this is doing is pulling the arguments you append beyond 
#      the script name (example:  python py13.py arg arg arg).  If you don't
#      include the arguments in the command line, it will error out.

#Assigns data to the varaibles based on the input from the command line
script, first, second, third = argv

#Dipslays the text and data to the screen.
#NOTE: don't need a space between : and " - the , will include a space
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third


#Test the way that the argv is imported to determine if this is a string or int
#will call the program in BASH by:  python ex13.py one 2 three.  

# print "Argument 1 is a string: %r" % first
# print "Argument 2 is an int: %d" % second
# print "Argument 3 is a string: %r" % third

#Test failed.  Obviously this calls each argument as a string.

