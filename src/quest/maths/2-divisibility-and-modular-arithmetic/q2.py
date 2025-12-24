import random
import math
from collections import namedtuple

# PROBLEM STATEMENT
# https://leetcode.com/problems/smallest-integer-divisible-by-k/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic
#
# Given a positive integer k, you need to find the length of the smallest positive
# integer n such that n is divisible by k, and n only contains the digit 1.
#
# Return the length of n. If there is no such n, return -1.
#
# Note: n may not fit in a 64-bit signed integer.
#
# CONSTRAINTS
# 1 <= k <= 10^5
#
# EXAMPLES
# Input     k = 1
# Output    1
#
# Input     k = 2
# Output    -1
#
# Input     k = 3
# Output    3

ExampleData = namedtuple("ExampleData", ["input", "output"])

def smallestRepunitDivByK(k: int) -> int:
    # We are looking for the smallest
    #   R_n = 111..1 (n-ones)
    #
    # that is divisible by k without rest where
    #   r = R_n % k
    #
    # Because R_n is odd for all n and ends with 1, k should not share a factor
    # with 2 or 5.
    if (math.gcd(k, 10) != 1): return -1

    # This number can also be expressed using
    # positional notation:
    #   R_n = ∑(i=0..n-1) 10^i
    #       = 10 * R_{n-1} + 1
    #
    # What's important to realize is that we don't need to construct up R_n directly.
    # Doing so would severely affect the performance of the program. Instead,
    # we can track the remainder
    #   r = R_i % k
    #
    # at each step:
    #     1 % k
    #    11 % k
    #   111 % k
    #       ...
    #
    # The key identity to consider is
    #   R_{n+1} % k = (R_n * 10 + 1) % k
    #
    # which works out because multiplying by 10 shifts the digits left,
    # and taking the modulo keeps the remainder small. For example:
    #
    # R_1 =      1                                 | R_1 % 7 = 1
    # R_2 =     11 =     1 * 10 + 1 = R_1 * 10 + 1 | R_2 % 7 = 4
    # R_3 =    111 =    11 * 10 + 1 = R_2 * 10 + 1 | R_3 % 7 = 6
    # R_4 =   1111 =   111 * 10 + 1 = R_3 * 10 + 1 | R_4 % 7 = 5
    # R_5 =  11111 =  1111 * 10 + 1 = R_4 * 10 + 1 | R_5 % 7 = 2
    # R_6 = 111111 = 11111 * 10 + 1 = R_5 * 10 + 1 | R_6 % 7 = 0 => R_6 is divisible by 7
    i = 1
    r = 1 % k

    while r != 0:
        r = (r * 10 + 1) % k
        i += 1

        # For every modulo k, there are k possible remainders:
        #   {0, 1, 2, ..., k-1}.
        #
        # If the solution repeats without hitting 0, then there exists no R_n
        # that is divisible by k without remainder.
        if (i > k): return -1

    return i

if __name__ == '__main__':
    # examples
    assert smallestRepunitDivByK(1) == 1
    assert smallestRepunitDivByK(2) == -1
    assert smallestRepunitDivByK(3) == 3

    # test cases
    inputs = [random.randint(0, 10**5 + 1) for _ in range(100_000)]
    results = [ExampleData(input=k, output=smallestRepunitDivByK(k)) for k in inputs]

    print("\n".join(map(str, results)))
