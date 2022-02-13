'''
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        x = len(s)
        arr = []
        for i in range(1 << x):
            arr.append([s[j] for j in range(x) if (i & (1 << j))])
        return arr