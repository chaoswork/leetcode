#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb 24 21:02:46 2018
Brief: https://leetcode.com/problems/plus-one/description/

Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer.

You may assume the integer do not contain any leading zero,
except the number 0 itself.

The digits are stored such that the most significant digit is at
the head of the list.
"""
import sys


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        over = 1
        for i in range(n):
            k = n - 1 - i
            digits[k] += over
            if digits[k] == 10:
                over = 1
                digits[k] = 0
            else:
                over = 0

        if over > 0:
            digits = [over] + digits
        return digits


digits = map(lambda x: int(x), sys.argv[1].split(','))

sol = Solution()
print sol.plusOne(digits)
