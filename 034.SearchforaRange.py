#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Feb 16 19:51:41 2018
Brief: https://leetcode.com/problems/search-for-a-range/description/

Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
import sys


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # a[left] < target, a[right] >= target, left < right
        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if right >= len(nums) or nums[right] != target:
            return [-1, -1]
        l1 = right
        # a[left] <=target, a[right] > target, left < right
        left = right
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if left <= -1 or nums[left] != target:
            return [-1, -1]
        l2 = left
        return [l1, l2]

sol = Solution()
print sol.searchRange(sys.argv[1].split(','), sys.argv[2])
