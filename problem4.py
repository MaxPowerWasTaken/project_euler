"""
A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math 


def is_palindromic(n:int) -> bool:
    sn = str(n)
    for i in range(math.ceil(len(sn)/2)):
        if sn[i] != sn[-(i+1)]:
            return False
    return True

assert is_palindromic(9009) == True
assert is_palindromic(9008) == False

seq1 = range(999,1,-1)

if __name__ == "__main__":
    if is_palindromic(999*999):
        print(999*999)
    else:
        for i in range(999,1,-1):
            for j in range(998,1, -1):
                
            if is_palindromic(i*j):
                print(i*j)
                break
# BUG: this returns 289982, which is 538*539. But this method of 
# zipping through these pairs of numbers does not produce largest.
# For ex, if 999*997 were a palindrome, it would of course be larger.

# New approach...must need to calc many pair-mults, check palindrome,
# keep largest. But how many pairs do I need to mult and check?