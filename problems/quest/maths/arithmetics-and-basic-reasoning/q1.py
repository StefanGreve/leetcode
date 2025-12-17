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

ExampleData = namedtuple("Example", ["input", "output"])

example1 = ExampleData(input = [3,5,1], output = True)
example2 = ExampleData(input = [1,2,4], output = False)

def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    diffs = [abs(arr[i+1] - arr[i]) for i in range(len(arr) - 1)]
    output = len(set(diffs)) == 1
    return output

if __name__ == '__main__':
    result1 = canMakeArithmeticProgression(example1.input)
    print(result1 == example1.output)

    result2 = canMakeArithmeticProgression(example2.input)
    print(result2 == example2.output)

