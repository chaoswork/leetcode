#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Mon Jun 13 11:39:04 2016

# https://leetcode.com/problems/palindrome-number/
# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        xx = x
        while xx:
            t = xx % 10
            rev *= 10
            rev += t
            xx /= 10
        return rev == x

sl = Solution()
print sl.isPalindrome(1234321)
print sl.isPalindrome(123321)
print sl.isPalindrome(1234567)
print sl.isPalindrome(123456)
