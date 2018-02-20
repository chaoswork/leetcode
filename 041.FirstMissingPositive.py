#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb 20 22:47:51 2018
Brief: https://leetcode.com/problems/first-missing-positive/description/

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
import sys


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        lst = [0] * (len(nums) + 1)
        for item in nums:
            if item > 0 and item < len(lst):
                lst[item] = 1
        # print lst
        for i in range(1, len(lst)):
            if lst[i] == 0:
                return i
        return i + 1


sol = Solution()
lst = map(lambda x: int(x), sys.argv[1].split(','))
print sol.firstMissingPositive(lst)
print sol.firstMissingPositive([])
