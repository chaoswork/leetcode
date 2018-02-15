#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Feb 15 16:03:21 2018
Brief: https://leetcode.com/problems/sqrtx/description/

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to
 return an integer, the decimal part will be truncated.
"""
import sys


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        left^2 <= x, right^2 > x, left < right
        """
        if x == 0:
            return x
        left = 1
        right = x
        while left + 1 < right:
            mid = (left + right) / 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
        return left


sol = Solution()
print sol.mySqrt(int(sys.argv[1]))
