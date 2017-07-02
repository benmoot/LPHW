# To produce "" accurately in text strings, you need to break them

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


# \t is for producing a tab within a string
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

# ESCAPE SEQUENCES
backslash = "This prints a backslash > \\"
single_quote = "Look, a single quote \'"
double_quote = "And a double! \""
BEL = "This prints an ASCI bell \a"
BS = "And this would be a backspace \b"
FF = "Formfeed is a weird word. \f"
LF = "Linefeed is kinda weird, too \n"
unicodename = "For unicode names, you use \N(name) and add the name."
carr_return = "Carriage return sounds like a typewriter \r"
tab = "\tWell we already know this one."
vtab = "\vBut this vertical tab."

print backslash
print single_quote
print double_quote
print BEL
print BS
print FF
print LF
print unicodename
print carr_return
print tab
print vtab

# # rotating loading bar
# while True:
#         for i in ["/","-","|","\\","|"]:
#             print "%s\r" % i,
