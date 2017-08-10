#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Tue Jun 14 15:22:51 2016

# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        li = 0
        ri = len(height) - 1
        while li < ri:
            area = (ri - li) * min(height[li], height[ri])
            if area > res:
                res = area
            if height[li] < height[ri]:
                li += 1
            elif height[li] > height[ri]:
                ri -= 1
            else:
                li += 1
                ri -= 1
        return res

sl = Solution()
print sl.maxArea([5,3,4])
                
