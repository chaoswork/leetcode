#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb 27 10:09:20 2018
Brief: https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it is able to trap after raining

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = [0] * n
        right = [0] * n
        for i in range(n):
            if i > 0:
                left[i] = max(left[i - 1], height[i - 1])

        for i in reversed(range(n)):
            if i < n - 1:
                right[i] = max(right[i + 1], height[i + 1])
        # print height
        # print left
        # print right
        lr = map(lambda x: min(x), zip(left, right))
        result = 0
        for i in range(n):
            if lr[i] > height[i]:
                result += lr[i] - height[i]
        return result


sol = Solution()
print sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 5, 1])
