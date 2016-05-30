#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Thu May 26 01:01:52 2016

# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

# Python中尽量少赋值，不然容易超时

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Solution 1: Bruce Force, O(n^2)
        """
        res = [-1, -1]
        for i in range(0, len(s)):
            # odd length palindromic
            tres = self.palindromic(s, i, 0)
            tres_even = self.palindromic(s, i, 1)
            if res[1] - res[0] < tres[1] - tres[0]:
                res = tres
            if res[1] - res[0] < tres_even[1] - tres_even[0]:
                res = tres_even
        return s[res[0] : res[1]]

    def palindromic(self, s, i, is_even):
        j = 0
        res = ""
        while i + j < len(s) and i - j - is_even >= 0:
            if s[i - j - is_even] != s[i + j]:
                break
            j += 1
        j = j - 1
        res = [i - j - is_even , i + j + 1]
        return res
"""
class Solution(object):
    def longestPalindrome(self, s):

#        :type s: str
#        :rtype: str
#        Solution 1: Bruce Force, O(n^2)


        res = ""
        for i in range(0, len(s)):
            # odd length palindromic
            tres = self.palindromic(s, i, 0)
            tres_even = self.palindromic(s, i, 1)
            if len(res) < len(tres):
                res = tres
            if len(res) < len(tres_even):
                res = tres_even
        return res
            
    def palindromic(self, s, i, is_even):
        j = 0
        res = ""
        while i + j < len(s) and i - j - is_even >= 0:
            sb = s[i - j - is_even]
            sf = s[i + j]
            # print 'sb=%s,s[i]=%s,sf=%s' % (sb, s[i], sf)
            # print 'j=%d' % j
            if sb != sf:
                break
            j += 1
        j = j - 1
        res = s[i - j - is_even : i + j + 1]
        return res
"""            
sl = Solution()

print sl.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print sl.palindromic("123abcba", 5, 0)
            
