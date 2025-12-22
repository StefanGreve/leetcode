import math
import random
from collections import namedtuple
from typing import List

# PROBLEM STATEMENT
# https://leetcode.com/problems/ugly-number/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic
#
# An ugly number is a positive integer which does not have a prime factor
# other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
#
# CONSTRAINTS
# -2^{31} <= x <= 2^{31}-1
#
# EXAMPLE
# Input     x = 6
# Output    True
#
# Input     x = 1
# Output    True
#
# Input     x = 14
# Output    False

ExampleData = namedtuple("ExampleData", ["input", "output"])

# Sieve of Eratosthenes
def primeGenerator(n: int) -> List[int]:
    A: List[bool] = [True] * max(4, n+1)
    A[0], A[1] = False, False

    for i in range(2, math.isqrt(n)+1):
        if A[i] is True:
            for j in range(i**2, n+1, i):
                A[j] = False

    return [i for i in range(len(A)) if A[i] is True]

# Trial Division
def primeFactorization(n: int) -> List[int]:
    F: List[int] = []
    primes = primeGenerator(math.isqrt(n))

    for p in primes:
        while (n % p == 0):
            F.append(p)
            n //= p

    # if true, what remains must be prime
    if (n > 1):
        F.append(n)

    return F

def isUgly(n: int) -> bool:
    if (n <= 0): return False
    if (n == 1): return True

    allowed_prime_factors = [2, 3, 5]
    prime_factors = primeFactorization(n)

    return all(x in allowed_prime_factors for x in prime_factors)

if __name__ == '__main__':
    # examples
    assert isUgly(6) == True
    assert isUgly(1) == True
    assert isUgly(14) == False

    # test cases
    results = [
        ExampleData(input=random.randint(-2**31, 2**31), output=isUgly(x))
            for x in range(100_000)
    ]

    print("\n".join(map(str, results)))
