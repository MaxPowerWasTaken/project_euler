"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def get_factors(n:int) -> list:
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            factors.append(int(i))
            factors.append(int(n/i))

    # dedupe and re-sort to eliminate dupes for squares (9 -> [1,3,3,9])
    return sorted(set(factors))

def is_prime(n:int) -> bool:
    return True if len(get_factors(n)) == 2 else False

def get_prime_factors(n:int) -> list:
    return [i for i in get_factors(n) if is_prime(i)]

# TEST
assert set(get_factors(10)) == set([1,2,5,10])
assert set(get_factors(13)) == set([1,13])
assert is_prime(10) == False
assert is_prime(13) == True
assert is_prime(9) == False
assert set(get_prime_factors(13195)) == set([5, 7, 13, 29])

# result
if __name__ == "__main__":
    N = 600851475143
    print(max(get_prime_factors(N)))


"""
Should really only have to iterate up to sqrt(n)...
For Ex: Factors of 10
at i = 2...
    if 10%2 == 0:
        factors includes 2(i) and 10/2
"""
