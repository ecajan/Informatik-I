#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    if len(data) >= 1:
        keyt = tuple(sorted(data[0].keys()))
    else:
        keyt = ()

    changetotuple = []
    for tups in data:
        templ = []
        for key in keyt:
            templ.append(tups[key])
        changetotuple.append(tuple(templ))

    retrntpl = (keyt, changetotuple)

    return retrntpl

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))