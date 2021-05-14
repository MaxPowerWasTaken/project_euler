import numpy as np
from loguru import logger
"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all 
of the numbers from 1 to 20?
"""

def prob5(upper_bound=int(1e7), factors=(1,10)):
    # everything is divisible by 1, and we are only checking
    # even numbers so don't need to check divisibility by 2
    if factors[0]<=2:
        factors = (3, factors[1])

    step = 2 * (factors[1]-1)
    for i in range(step, upper_bound, step):
        divisible_by_all = True
        for factor in range(factors[1], factors[0]-1, -1):
            if i % factor != 0:
                divisible_by_all = False
                logger.debug(f"{i} is not divisible by {factor}")
                break
        logger.debug(f"{i} is divisible by all factors, returning {i} as answer")
        if divisible_by_all:
            return i
    return None

UPPER_BOUND = int(5e9)
FACTORS = (1,20)
answer = prob5(upper_bound=UPPER_BOUND, factors=FACTORS)
print(f"Answer for factors {FACTORS} is {answer:,}")

"""NOTE:
An additional optimization to make: 
why check factors in numeric order (e.g. 3, 4, 5...19,20)?
Should check them in least-common order so can rule out i's faster
e.g. resort factors to e.g. 17,14,... per least common...

...Actually... this should work by just reversing order of factors...

"""