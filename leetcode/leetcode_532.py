'''
532. K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
'''


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        s = set()
        t = set()
        for i in nums:
            if i - k in t:
                s.add(i-k)
            if i + k in t:
                s.add(i)
            t.add(i)
        return len(s)
