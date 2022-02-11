'''
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        a = 0
        c = 0

        for i in nums:
            a += i
            if k == a:
                c += 1
            if a - k in d:
                c += d[a - k]
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        print(d)
        return c
