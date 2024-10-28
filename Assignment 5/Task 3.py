#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a : list[int], b : list[int]) -> list[tuple[int, int]]:
        return [ (a[i if i < len(a) else -1], b[i if i < len(b) else -1]) for i in range(max(len(a), len(b))) if a and b]



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [1]))
