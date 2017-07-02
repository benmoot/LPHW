# this adds modules (libraries) to python. needed to be imported in order to keep programs as small as possible. also acts as documentation for future reading by other programmers.

# argv is the "argument variable"
# assigning variables to argv tells it to pring them in that order
from sys import argv

# the first variable, in this case "script" will ALWAYS print the name of the file.
script, first, second, third = argv

print "The script is called:", script

# the values that need to be filled
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
