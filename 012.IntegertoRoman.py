#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Tue Jun 14 16:00:21 2016

# https://leetcode.com/problems/integer-to-roman/

# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        I = 1, X = 10, C = 100, M = 1000, V = 5, L = 50, D = 500
        """
        Roman = [("I", "V"), ("X", "L",), ("C", "D"), ("M","")]
        index = 0
        res = ""
        while num:
            n = num % 10
            if n >= 0 and n < 4:
                res = Roman[index][0] * n + res
            elif n == 4:
                res = Roman[index][0] + Roman[index][1] + res
            elif n == 5:
                res = Roman[index][1] + res
            elif n < 9:
                res = Roman[index][1] + Roman[index][0] * (n - 5) + res
            elif n == 9:
                res = Roman[index][0] + Roman[index + 1][0] + res

            index += 1
            num /= 10
        return res


sl = Solution()
print sl.intToRoman(10)
print sl.intToRoman(30)
print sl.intToRoman(40)
print sl.intToRoman(3079)
