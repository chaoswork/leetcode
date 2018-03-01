#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Mar  1 12:50:09 2018
Brief: https://leetcode.com/problems/length-of-last-word/description/

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:

Input: "Hello World"
Output: 5

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        vlist = s.split()
        if len(vlist) > 0:
            return len(vlist[-1])
        return 0
