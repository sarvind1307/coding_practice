'''
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
'''


class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            x, y = s[:i], s[i:]
            max_score = max(max_score, (x.count('0') + y.count('1')))
        print(max_score)
        return max_score