# LCTHW - Exercise 6: Strings and Text
# by: Brett A Phillips
# date: February 4, 2013

#Assigns string & constant to x
x = "There are %d types of people." % 10
#Assigns value to variable
binary = "binary"
#Assigns value to variable
do_not = "don't"
#Assigns string and refrence tuple to varaiable y
y = "those who know %s and those who %s." % (binary, do_not)

#Display the variable to screen
print x
print y

#Display lines and variables to screen
print "I said: %r." % x
print "I also said: '%s'." % y

#Assign value to variable
hilarious = False
#Assigns value to variable => NOTE: can include the character format in the variable
joke_evaluation = "Isn't that joke so funny?! %r"

#Display the variable and passes reference
print joke_evaluation % hilarious

#Assign value to variables
w = "This is the left side of a..."
e = "a string with a right side."

#Displays contatenated strings
print w + e