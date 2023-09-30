'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
'''

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        char_freq = {}

        for n in nums:
            char_freq[n] = char_freq.get(n, 0) + 1
            if char_freq[n] > 1:
                return True

        return False


nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
solution = Solution()

print(solution.containsDuplicate(nums1))
print(solution.containsDuplicate(nums2))