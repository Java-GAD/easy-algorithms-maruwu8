'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''
from typing import List


class Solution:
    def groupAnagrams( self,
                       strs: List[str] ) -> List[List[str]]:

        map_anagrams = {}
        result = []

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in map_anagrams.keys():
                map_anagrams[sorted_word] = [word]
            else:
                map_anagrams[sorted_word].append(word)

        for list in map_anagrams.values():
            result.append(list)

        # return list(anagram_dict.values())

        return result

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))