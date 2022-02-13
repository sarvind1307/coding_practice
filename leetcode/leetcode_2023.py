'''
2023. Number of Pairs of Strings With Concatenation Equal to Target

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.
'''


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        x = 0
        l = len(nums)
        for i, c in enumerate(nums):
            for j, d in enumerate(nums):
                # print(c+d)
                if i != j and c+d == target:
                    print("lol", i,j)
                    x += 1
        return x