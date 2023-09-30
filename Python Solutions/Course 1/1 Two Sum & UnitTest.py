'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order!!!
'''


import unittest
from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp not in num_map.keys():
                num_map[n] = i
            else:
                return [i, num_map[comp]]


class TestSolution(unittest.TestCase):

    def test_twoSum(self):
        solution = Solution()
        # Test case 1
        nums1 = [2, 7, 11, 15]
        target1 = 9
        result1 = solution.twoSum(nums1, target1)
        self.assertEqual(set(result1), {0, 1})     #---> use set for comparison!!!

        # Test case 2
        nums2 = [3, 2, 4]
        target2 = 6
        result2 = solution.twoSum(nums2, target2)
        self.assertEqual(set(result2), {1, 2})

        # Test case 3
        nums3 = [3, 3]
        target3 = 6
        result3 = solution.twoSum(nums3, target3)
        self.assertEqual(set(result3), {0, 1})


if __name__ == '__main__':
    unittest.main()
