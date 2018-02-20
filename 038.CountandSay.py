#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb 20 23:11:29 2018
Brief: https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is the sequence of integers with the first five
terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""
import sys


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'

        for i in range(2, n + 1):
            cur = start[0]
            cnt = 1
            result = ''
            for j in range(1, len(start)):
                if start[j] == cur:
                    cnt += 1
                else:
                    result = ''.join([result, str(cnt), cur])
                    cur = start[j]
                    cnt = 1
            result = ''.join([result, str(cnt), cur])
            start = result

        return start


sol = Solution()
print sol.countAndSay(int(sys.argv[1]))
