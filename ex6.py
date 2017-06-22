#  It's as if you were telling me to buy you a list of items from the store and you said, "I want milk, eggs, bread, and soup." Only as a programmer we say, "(milk, eggs, bread, soup)."
# ^ Great quote



# START EXPLANATION


# states there are 10 people. %d because it is not a string, it's an interger
x = "There are %d types of people." % 10

# this is for the following sentence, showing that %s takes place of strings, but neesd to be addressed in what order. (%s 1, %s 2, etc.)
binary = "binary"
do_not = "don't"

# variables assigned to strings
y = "Those who know %s and those who %s." % (binary, do_not)
# printing statement
print x
print y


# %r repeats the string from x in quotations.
# when printing y for %s the quotes are assigned by programmer
print "I said %r." % x
print "I also said: '%s'." % y

# this joke isn't funny. it prints the string followed by previous assigned variable
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious


# w + e adds the strings together into one sentence with no spaces
w = "This is the left side of..."
e = "a string with a right side."

print w + e


# %r displays raw data. good for debugging. %s and %d is used to display to users.
