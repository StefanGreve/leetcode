import math
from collections import namedtuple

# PROBLEM STATEMENT
# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning
#
# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all
# elements between x and n inclusively.
#
# CONSTRAINTS
# 1 <= n <= 1000
#
# EXAMPLE
# Input     n = 8
# Output    6
#
# Input     n = 1
# Output    1
#
# Input     n = 4
# Output    -1

ExampleData = namedtuple("ExampleData", ["input", "output"])

def pivotInteger(n: int) -> int:
    # The Gauss sum formula for 1..n is given by
    # s_n = n(n+1)/2
    #
    # Therefore, the sum x..n is given by the difference of s_n and the sum of 1..x-1:
    # s_{n-x} = s_n - (x-1)(x-1+1)/2
    #         = s_n - (x-1)x/2
    #
    # We are looking for an x that satisfies
    # s_x = s_{n-x}
    #
    # Hence, solving for x yields:
    #            x(x+1)/2 = n(n+1)/2 - (x-1)x/2
    # x(x+1)/2 + (x-1)x/2 = n(n+1)/2
    # [x(x+1) + x(x-1)]/2 = n(n+1)/2
    #      x[x+1 + x-1]/2 = n(n+1)/2
    #                 x^2 = n(n+1)/2
    #                   x = sqrt(n(n+1)/2)
    #
    # If x is an integer (pivot), return x, otherwise -1.
    x = math.sqrt(sum(range(1, n+1)))
    return int(x) if x.is_integer() else -1

if __name__ == '__main__':
    # examples
    assert pivotInteger(8) == 6
    assert pivotInteger(1) == 1
    assert pivotInteger(4) == -1

    # test cases
    results = (ExampleData(input = n, output = pivotInteger(n)) for n in range(1, 1001))
    print("\n".join(map(str, results)))


