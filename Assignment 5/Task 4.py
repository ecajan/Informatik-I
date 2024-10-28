#!/usr/bin/env python3
import re
# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = keywords
        self.keywords.sort(key = len, reverse = True)
        self.template = template
        self.replace_temp = []
        for sword in self.keywords:
            replace = (self.template * (len(sword) // len(self.template) + 1))[:len(sword)]
            self.replace_temp.append(replace)

    def filter(self, msg):
        for sword, replace in zip(self.keywords, self.replace_temp):
            msg = re.sub(re.escape(sword), replace, msg, flags = re.IGNORECASE)
        return (msg)


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard", "duckmastardio"], "?#$")
    offensive_msg = "abc defghi duckMastardio jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
