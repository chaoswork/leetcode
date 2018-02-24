#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb 24 20:34:28 2018
Brief: https://leetcode.com/problems/search-in-rotated-sorted-array/description

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
import sys


class Solution(object):
    def bsearch(self, nums, target):
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        # find povit
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        if nums[left] < nums[right]:
            return self.bsearch(nums, target)
        else:
            if target < nums[0]:
                ret = self.bsearch(nums[right:], target)
                if ret < 0:
                    return -1
                return right + ret
            else:
                return self.bsearch(nums[:right], target)


sol = Solution()
print sol.search(sys.argv[1].split(' '), sys.argv[2])
