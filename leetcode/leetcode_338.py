'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0, n+1):
            x = str(bin(i)[2:])
            # print(x)
            arr.append(x.count('1'))
        print(arr)
        return arr
