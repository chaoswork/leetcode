#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Mon May 30 02:03:20 2016

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s
        strlist = []
        
        n = numRows + numRows - 2
        rest = len(s) % n
        if rest:
            for i in range(0, n - rest):
                s += " "
        cur = 0
        while cur * n < len(s):
            period = cur * n
            strlist.append(s[period : period + numRows])
            if numRows > 2:
                strlist.append(" " + s[period + numRows: (cur + 1) * n][::-1] + " ")
            cur += 1
        print "^" + s + "$"
        print strlist
        res = ""
        for i in range(0, numRows):
            for j in range(0, len(strlist)):
                if strlist[j][i] != " ":
                    res += strlist[j][i]
        return res
            

sl = Solution()
print sl.convert("12345", 4)
