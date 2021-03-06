'''
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = start + (end - start) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                start = mid + 1
            else:
                end = mid - 1

        return end
        