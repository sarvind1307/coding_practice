'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        carry = 0
        ans = ""
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            carry, remain = divmod(carry, 2)
            ans += str(remain)
        return ans[::-1]
