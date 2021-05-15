"""
https://projecteuler.net/problem=6

...
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(n:int)->int:
    ''' return sum of squares of all numbers from 1...n'''
    return sum([i**2 for i in range(1,n+1)])

def square_of_sum(n:int)->int:
    ''' return square of the sum of all numbers from 1...n'''
    return sum(range(1,n+1))**2

def result(n): 
    return square_of_sum(n) - sum_of_squares(n)

assert result(10) == 2640

print(result(100))