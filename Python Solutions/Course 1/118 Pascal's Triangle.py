'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
from typing import List


class Solution:
    def generate( self,
                  numRows: int ) -> List[List[int]]:

        if numRows == 0:
            return []

        triangle = [[1]]  # ---> first row

        for i in range(1, numRows):

            prev_row = triangle[i - 1]
            new_row = [1]                    # ---> every row starts with 1

            for j in range(1, i):
                new_row.append(prev_row[j - 1] + prev_row[j])

            new_row.append(1)                # ---> every row ends with 1

            triangle.append(new_row)

        return triangle



numRows1 = 5
numRows2 = 1

solution = Solution()
output1 = solution.generate(numRows1)
output2 = solution.generate(numRows2)

print(output1)
print(output2)
