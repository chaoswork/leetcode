#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Tue May 31 11:53:20 2016

# https://leetcode.com/problems/reverse-integer/

# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        neg = 1
        if x < 0:
            neg = -1
            x = -x
        s = str(x)[::-1]
        x = int(s)
        if x > 0x7fffffff:
            x = 0
        
        return x * neg
        
                            
