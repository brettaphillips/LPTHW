# LCTHW - Exercise 15: Reading Files
# by: Brett A Phillips
# date: February 12, 2013

# import the argv module from the sys archive
from sys import argv

# gather variables from the command line
script, filename = argv

# create a variable 'txt' and assign the file referenced in the command line
txt = open(filename)

# Output text to screen and variable from command line
print "Here's your file %r:" % filename
# Use the read fucntion on variable 'txt' & output to screen
print txt.read()
# print a blank line to screen
print ""

# Output text to screen
print "Type the filename again:"
# Dipslay prompt,collect data (string), and assign to variable 'file_again'
file_again = raw_input("> ")
# Output two blank lines to screen
print "\n"

# Create variable 'txt_again' and assign file referenced in string variable 'file_again'
txt_again = open(file_again)

# Use the read fucntion on variable 'txt_again' & output to screen
print txt_again.read()
# Output two blank lines to screen
print "\n"
