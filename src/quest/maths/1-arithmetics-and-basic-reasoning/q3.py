import random
from collections import namedtuple

# PROBLEM STATEMENT
# https://leetcode.com/problems/palindrome-number/?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# CONSTRAINTS
# -2^{31} <= x <= 2^{31}-1
#
# EXAMPLE
# Input     x = 121
# Output    true
#
# Input     x = -121
# Output    false
#
# Input     x = 10
# Output    false

ExampleData = namedtuple("ExampleData", ["input", "output"])

def isPalindrome(x: int) -> bool:
    # Negative numbers are never a palindrome
    if (x < 0): return False

    # Single-digit numbers are palindromes
    if (x < 10): return True

    rev: int = 0
    tmp: int = x

    while (tmp != 0):
        # Shift left once (REV * 10),
        # then add the last number (TMP % 10).
        rev = (rev * 10) + (tmp % 10)
        # Pop the last digit from TMP
        tmp //= 10

    return rev == x

if __name__ == '__main__':
    # examples
    assert isPalindrome(121) == True
    assert isPalindrome(-121) == False
    assert isPalindrome(10) == False

    # test cases
    results = [
        ExampleData(input=x, output=isPalindrome(x)) for x in (
            random.randint(-2**31, 2**31) for _ in range(100_000)
        )
    ]

    print("\n".join(map(str, results)))



