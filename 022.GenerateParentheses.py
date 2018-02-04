#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb  3 21:57:15 2018
Brief: https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = {}
        result[1] = ['()']
        if n == 1:
            return result[n]
        for i in range(2, n + 1):
            result[i] = set()
            for j in range(1, i):
                for item1 in result[j]:
                    for item2 in result[i - j]:
                        result[i].add(''.join([item1, item2]))
                        if j == 1:
                            result[i].add(''.join(['(', item2, ')']))
        return list(result[n])


import sys
sol = Solution()
result = sol.generateParenthesis(int(sys.argv[1]))
print len(result), result
