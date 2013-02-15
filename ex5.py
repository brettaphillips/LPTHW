# LCTHW - Exercise 5: more Variables and Printing
# by: Brett A Phillips
# date:  February 4, 2013

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tal." %height

print "He's %.2f centimeters tall." % (height * 2.54)
print "\n"

print "He's %d pounds heavy." % weight

print "He's %.2f kilograms heavy!" % (weight / 2.2)
print "\n"

print "Actually that's not too heavy!"
print "He's got %s eyes and %s hair." % (eyes, hair)

print "His teeth are usually %s depending on the coffee." % teeth

print "\n"
#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d... I get %d" % (
	age, height, weight, age + height + weight)