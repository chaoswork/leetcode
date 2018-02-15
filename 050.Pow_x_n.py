#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Feb 15 15:46:30 2018
Brief: https://leetcode.com/problems/powx-n/description/

Implement pow(x, n).


Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
"""


class Solution(object):
    def fastpow(self, x, n):
        """
        fast pow
        """
        if n == 0:
            return 1.0
        half = self.fastpow(x, n / 2)
        if n % 2 == 1:
            return half * half * x
        return half * half

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1 / x
        return self.fastpow(x, n)
