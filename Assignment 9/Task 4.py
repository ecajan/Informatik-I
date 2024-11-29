#!/usr/bin/env python3
import re

# Change the functions below to determine if the given input is a palindrome.

def is_palindrome(s):
    sedit = (re.sub(r'\W+', '', s)).lower()
    if len(sedit) <= 1:
        return True
    elif len(sedit) == 2 and sedit[0] == sedit[-1]:
        return True
    else:
        return sedit[0] == sedit[-1] and is_palindrome(sedit[1:-1])


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
