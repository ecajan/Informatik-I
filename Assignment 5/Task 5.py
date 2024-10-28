#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    n = set()
    for a, b in zip(top, bottom):
        if n:
            n = n.intersection(set([a, b]))
        else:
            n = set([a, b])
    print(n)
    minrot = -1
    for d in n:
        m = min(top.count(d), bottom.count(d)) - list(zip(top, bottom)).count((d, d))
        if minrot == -1 or m < minrot:
            minrot = m
    return minrot


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
