# LCTHW - Exercise 10: What was that?
# by: Brett A Phillips
# date: Feb 5, 2013

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a ine."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#print fat_cat in debugging mode (showing escape sequences)
print "%r" % fat_cat
#print fat_cat correctly (processing escape sequences)
print "%s" % fat_cat
