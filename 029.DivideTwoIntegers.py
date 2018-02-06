#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb  6 23:56:08 2018
Brief: https://leetcode.com/problems/divide-two-integers/description/

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

import sys


class Solution(object):
    def left_one(self, x, y):
        """
        find left one of hex(x/y)
        """
        res = 1
        while x >= y:
            x = x >> 1
            res = res << 1
        return res >> 1

    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = 0
        if dividend < 0:
            dividend = -dividend
            neg += 1
        if divisor < 0:
            divisor = -divisor
            neg += 1
        if dividend < divisor:
            return 0
        res = 0
        while True:
            leftone = self.left_one(dividend, divisor)
            min_value = min(divisor, leftone)
            max_value = max(divisor, leftone)
            for i in range(0, min_value):
                dividend -= max_value

            res += leftone
            if leftone <= 1:
                break
        if neg == 1:
            res = 0 - res
        # handle the overflow, but this will not happen in python
        if res > 2147483647:
            res = 2147483647
        return res


sol = Solution()
a = sol.divide(int(sys.argv[1]), int(sys.argv[2]))
print a
print a == int(sys.argv[1]) / int(sys.argv[2])
