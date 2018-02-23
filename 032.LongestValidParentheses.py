#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Feb 23 20:54:42 2018
Brief: https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length
of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length=2

Another example is ")()())", where the longest valid parentheses substring is
"()()", which has length = 4.
"""
import sys


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
        stack.append(len(s))
        stack = [-1] + stack
        best = 0
        for i in range(0, len(stack) - 1):
            diff = stack[i + 1] - stack[i] - 1
            if diff > best:
                best = diff
        return best


sol = Solution()
print sol.longestValidParentheses(sys.argv[1])
