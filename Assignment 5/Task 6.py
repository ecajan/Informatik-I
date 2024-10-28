#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes(n):
    if n < 2:
        return['empty']
    grid = [ True for _ in range(n + 1) ]
    for yourmom in range(2, n + 1):
        if grid[yourmom]:
            for yourdad in range(yourmom * 2, n + 1, yourmom):
                grid[yourdad] = False

    primes_up_to_n = [ x for x in range(2, n + 1) if grid[x] ]

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes(1000))
