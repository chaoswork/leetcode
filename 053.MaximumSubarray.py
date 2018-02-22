#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Feb 22 21:36:59 2018
Brief: https://leetcode.com/problems/maximum-subarray/description/

Find the contiguous subarray within an array (containing at least
one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = nums[0]
        cur = 0
        for i in range(0, len(nums)):
            cur += nums[i]
            if cur > best:
                best = cur
            if cur < 0:
                cur = 0
        return best


sol = Solution()
print sol.maxSubArray([-2, 1])
