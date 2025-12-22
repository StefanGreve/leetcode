import random
from collections import namedtuple
from typing import List

# PROBLEM STATEMENT
# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
# CONSTRAINTS
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
# EXAMPLES
# Input     nums = [2, 7, 11, 15]
# Output    [0, 1]
#
# Input     nums = [3, 2, 4]
# Output    [1, 2]
#
# Input     nums = [3, 3]
# Output    [0, 1]

# Time Complexity: O(n^2), Space Complexity: O(1)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        try:
            # prevent using the same element twice
            nums[i] = None
            j = nums.index(target - n)
            return [i, j]
        except ValueError:
            nums[i] = n
            continue

if __name__ == '__main__':
    # examples
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
    assert twoSum([3, 3], 6) == [0, 1]

    # test cases
    inputs = [
        (
            nums := [random.randint(-10**9, 10**9+1) for _ in range(2, random.randint(2, 10**4) + 1)],
            sum(random.choices(nums, k=2))
        ) for _ in range(100)
    ]

    print("\n".join(f"nums={nums}, target={target} -> output={twoSum(nums, target)}" for nums, target in inputs)
)
