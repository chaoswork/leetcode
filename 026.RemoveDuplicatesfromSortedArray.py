#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Mon Feb  5 23:23:05 2018
Brief: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
 the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
 being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

"""

import sys


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i + 1]
            else:
                i += 1
        return len(nums)


sol = Solution()
input_data = sys.argv[1].split(',')
print sol.removeDuplicates(input_data)
print input_data
