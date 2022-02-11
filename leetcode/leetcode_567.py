'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''


from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x1 = [0] * 26
        x2 = [0] * 26
        l1 = len(s1)
        for i in s1:
            x1[ord(i) - 97] += 1
            
        for i in s2[:l1 - 1]:
            x2[ord(i) - 97] += 1
            
        for i, c in enumerate(s2[l1 - 1:]):
            x2[ord(c) - 97] += 1
            if x1 == x2:
                return True
            x2[ord(s2[i]) - 97] -= 1
        return False