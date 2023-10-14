'''
Given the root node of a binary search tree and two integers low and high, return the sum of values
of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__( self, val=0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST( self,
                     root: Optional[TreeNode],
                     low: int,
                     high: int ) -> int:

        total_sum = 0

        def dfs( node ):
            nonlocal total_sum

            if node:

                if low <= node.val <= high:
                    total_sum += node.val

                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)

        dfs(root)
        return total_sum
