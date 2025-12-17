import random
from collections import namedtuple
from typing import List

# PROBLEM STATEMENT
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence?envType=problem-list-v2&envId=maths-m1-arithmetic-basic-reasoning
#
# A sequence of numbers is called an arithmetic progression if the difference
# between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged
# to form an arithmetic progression. Otherwise, return false.
#
# CONSTRAINTS
# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6
#
# EXAMPLE
# Input     arr = [3,5,1]
# Output    True
#
# Input     arr = [1,2,4]
# Output    false

ExampleData = namedtuple("ExampleData", ["input", "output"])

def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    diffs = [abs(arr[i+1] - arr[i]) for i in range(len(arr) - 1)]
    output = len(set(diffs)) == 1
    return output

if __name__ == '__main__':
    # example1 = canMakeArithmeticProgression([3,5,1]) == True
    # example2 = canMakeArithmeticProgression([1,2,4]) == False
    results = [ExampleData(input=arr, output=canMakeArithmeticProgression(arr)) for arr in [
            [random.randint(-10**6, 10**6) for _ in range(random.randint(2, 1000))] for _ in range(100_000)
        ]
    ]

    print("\n".join(map(str, results)))

