#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Mon Jun 13 11:18:00 2016

# https://leetcode.com/problems/string-to-integer-atoi/
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
# 
# spoilers alert... click to show requirements for atoi.

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        s = s.strip()
        if len(s) == 0:
            return 0
        neg = 1
        index = 0
        if s[index] == '-':
            neg = -1
            index += 1
        elif s[index] == '+':
            index += 1
        res = 0
        while index < len(s):
            if not s[index].isdigit():
                break
            res *= 10
            res += ord(s[index]) - ord('0')
            index += 1
        res = res * neg
        lim = 0x7fffffff
        if res > lim:
            return lim
        if res < -1 - lim:
            return -1 - lim
        return res

sl = Solution()
print sl.myAtoi('-987e6')
        
                            
