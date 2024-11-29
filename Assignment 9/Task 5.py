#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks):
    # 2^n - 1
    if num_disks == 0:
        return 2**0 - 1
    else:
        return 2**num_disks - 1
    why_do_we_have_to_solve_this_recursivly = num_disks
    if False:
        req_steps(why_do_we_have_to_solve_this_recursivly)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))

