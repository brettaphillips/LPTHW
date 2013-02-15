# LCTHW - Exercise 11: Asking Questions
# by: Brett A Phillips
# date: February 6, 2013

print "How old are you?",
age = raw_input()
print "How tall are you? (in inches)",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

#NOTE: raw_input reads input as a string.  If you try and do a numeric format character would toss exception.
print "So, you're %r old, %r inches tall, and weigh %r pounds." % (age,height,weight)
#NOTE: could fromat the end to do the convert and then can display as a number.
#print "So, you're %d old, %d inches tall, and weigh %d pounds." % (int(age),int(height),int(weight))

# NOTES:
# - if the input is something like 5'6" then the raw_input will automatically
#   go through and escape one of the text deliminators.  The reason why is because
#   the raw_input reads the value as a string.  so 5'6"  would actually be '5\'6"'
