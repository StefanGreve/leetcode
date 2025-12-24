from typing import List

# PROBLEM STATEMENT
# https://leetcode.com/problems/self-dividing-numbers/?envType=problem-list-v2&envId=maths-m2-divisibility-modular-arithmetic
#
# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
# and 128 % 8 == 0. A self-dividing number is not allowed to contain the digit zero.
#
# CONSTRAINTS
# 1 <= left <= right <= 10^4
#
# EXAMPLES
# Input     left = 1, right = 22
# Output    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
# Input     left = 47, right = 85
# Output    [48, 55, 66, 77]

def getDigits(x: int) -> List[int]:
    digits: List[int] = []

    while (x != 0):
        x, d = divmod(x, 10)
        digits.append(d)

    return digits[::-1]

def selfDividingNumbers(left: int, right: int) -> List[int]:
    result: List[int] = []

    for n in range(left, right+1):
        digits = getDigits(n)

        if (0 in digits): continue

        self_dividing = all(n % x == 0 for x in digits)

        if (not self_dividing): continue

        result.append(n)

    return result

if __name__ == '__main__':
    # examples
    assert selfDividingNumbers(1, 22) ==  [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert selfDividingNumbers(47, 85) == [48, 55, 66, 77]

