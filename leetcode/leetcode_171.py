'''
171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        # print(columnTitle)
        l = len(columnTitle)
        p = [26**i for i in range(l)]
        # print(p)
        s = 0
        for i in range(l):
            s += (ord(columnTitle[i]) - 64) * p[i]
        # print(s)
        return s