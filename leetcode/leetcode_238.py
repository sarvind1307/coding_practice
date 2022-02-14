'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start, end, n = 1, 1, len(nums)
        out = [1]*n 
        for i in range(n):
            out[i] *= start
            start *= nums[i]
            out[~i] *= end
            end *= nums[~i]
        return out