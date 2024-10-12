#!/usr/bin/env python3


# perform the transformation
def transform_string(s):
    l = len(s)
    i = s.find(":")
    low = s[0:i]
    upr = s[i+1:l]
    # Maybe you will want to use a temporary variable to hold the index
    # of the ":" character, so you can use it afterwards to slice the string?
    return((low).lower() + ":" + (upr).upper())

# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string("aB:cD"))

