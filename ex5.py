# a string is created by putting numbers or letters in double quotes (")
# anything in (") is a string and can be assigned as a variable
# this is important when dealing with numbers specifically
# variables MUST START WITH A LETTER
my_name = 'Paul B Mouton'
my_age = 26
my_height = 67 # inches
my_weight = 175 # pounds
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's pretty heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight
)

# %s prints strings, %d prints intergers, %r prints the string in 'quotes'
