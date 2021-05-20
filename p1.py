"""
If we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
RANGE = 1000
mult_factor1 = 3
mult_factor2 = 5

mults = []
for i in range(1000):
    if i % mult_factor1 == 0 or i % mult_factor2 == 0:
        mults.append(i)

print(f"Sum of mults of {mult_factor1} and {mult_factor2} up to {RANGE} is {sum(mults)}")

"""better way with list comprehensions
sum([x for x in range(1000) if x % 3== 0 or x % 5== 0])
"""