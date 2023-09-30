'''
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
'''

from typing import List


class Solution:
    def fizzBuzz( self,
                  n: int ) -> List[str]:

        result = []
        for i in range(1,
                       n + 1):

            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")

            else:
                result.append(str(i))

        return result


n1 = 3
n2 = 5

solution = Solution()
output1 = solution.fizzBuzz(n1)
output2 = solution.fizzBuzz(n2)

print(output1)
print(output2)
