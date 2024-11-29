#!/usr/bin/env python3

# Change the functions below to determine the powerset of a given set.
def powerset(nums):
    m=[]
    nums = set(nums)
    nums = list(nums)
    if not nums:
        m.append(nums)
    else:
        A = nums[0]
        B = nums[1:]
        for z in powerset(B):
            m.append(z)
            r = [A] + z
            m.append(r)
    return m





# The following lines call the function and print the return
# value to the Console. This way you can check what they do.
test_set = [1, 2, 3]
result = powerset(test_set)
# Example output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# Note that the order of the powerset could differ depending on the implementation.
# Make sure to look at the predefined test and adjust it if so.
print(result)
