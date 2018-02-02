#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Feb  2 15:33:11 2018
Brief: https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are
all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = '({['
        right = {')': '(',
                 '}': '{',
                 ']': '['}
        stack = []
        for i in range(0, len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif s[i] in right:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != right[s[i]]:
                    return False
        if len(stack):
            return False
        return True


import sys
sol = Solution()
print sol.isValid(sys.argv[1])
