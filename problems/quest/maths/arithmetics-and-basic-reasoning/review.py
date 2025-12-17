import random
from collections import namedtuple

# PROBLEM STATEMENT
# https://leetcode.com/quest/maths-quest/quiz/reverse-integer/?envType=problem-list-v2&envId=maths-m1-assignment
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing
# x causes the value to go outside the signed 32-bit integer range [-2^{31}, 2^{31} - 1],
# then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# CONSTRAINTS
# -2^{31} <= x <= 2^{31}-1
#
# EXAMPLE
# Input     x = 123
# Output    321
#
# Input     x = -123
# Output    -321
#
# Input     x = 120
# Output    21

ExampleData = namedtuple("Example", ["input", "output"])

def reverse(x: int) -> int:
    rev = 0
    tmp = abs(x)

    while (tmp != 0):
        rev = (rev * 10) + (tmp % 10)
        tmp //= 10

    if (x < 0):
        rev *= -1

    if (rev < -2**31 or rev > (2**31)-1):
        rev = 0

    return rev

if __name__ == '__main__':
    results = [
        ExampleData(input=x, output=reverse(x)) for x in (
            random.randint(-2**31, 2**31) for _ in range(100_000)
        )
    ]

    print("\n".join(map(str, results)))
