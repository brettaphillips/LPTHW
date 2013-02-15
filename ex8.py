# LCTHW - Exercise 8: Printing, Printing
# By: Brett A Phillips
# Date: February 5, 2013

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one" , "two", "three", "four")
print formatter % (True, False, False, True)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)