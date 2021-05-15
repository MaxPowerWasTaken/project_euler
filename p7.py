"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy as np
from problem3 import is_prime

def nth_prime(n):
    
    primes = [2]
    i = 3
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i = i + 2
    return primes[-1]

# test
assert nth_prime(6) == 13
if __name__ == "__main__":
    N = 6
    print(nth_prime(10_001))