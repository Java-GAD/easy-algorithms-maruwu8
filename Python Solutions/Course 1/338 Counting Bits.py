'''
Given an integer n, return an array ans of length n + 1 such
that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
'''
from typing import List


class Solution:
    def countBits( self,
                   n: int ) -> List[int]:
        ans = []

        for i in range(n + 1):
            count = 0
            num = i

            while num > 0:
                count += num % 2
                num //= 2

            ans.append(count)

        return ans

"""
BIT-WISE

ans = []
for i in range(n + 1):
    count = 0
    while i:
        count += i & 1   # --->  check the least significant bit
        i >>= 1          # ---> right-shift i by one bit (i >>= 1) to process the next bit until i becomes 0
    ans.append(count)
return ans
"""

n1 = 2
n2 = 25

solution = Solution()
output1 = solution.countBits(n1)
output2 = solution.countBits(n2)

print(output1)
print(output2)