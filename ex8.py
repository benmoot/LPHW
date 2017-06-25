formatter = "%r %r %r %r"

# all these lines print what's in paranthesis in place of %r
# %r stands for "representation", it is a 'raw programmer' version of variable
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
