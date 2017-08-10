#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Thu Jun 16 11:13:03 2016

# https://leetcode.com/problems/roman-to-integer/

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        I = 1, X = 10, C = 100, M = 1000, V = 5, L = 50, D = 500
        """

        value = [("M", 1000), ("CM", 900), ("D", 500),
                 ("CD", 400), ("C", 100), ("XC", 90),
                 ("L", 50), ("XL", 40), ("X", 10),
                 ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
                 ]

        index = 0
        vi = 0
        res = 0
        while index < len(s):
            if s[index:].startswith(value[vi][0]):
                res += value[vi][1]
                index += len(value[vi][0])
            else:
                vi += 1
        return res


sl = Solution()
print sl.romanToInt("MMMLXXIX")
print sl.romanToInt("I")
                
