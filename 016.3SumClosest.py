#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Mon Jun 27 17:48:38 2016

# https://leetcode.com/problems/3sum-closest/

# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = sys.maxint
        res = target
        for i in range(0, len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            tar = target - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == tar:
                    return target
                elif nums[left] + nums[right] > tar:

                    if nums[left] + nums[right] - tar < best:
                        best = nums[left] + nums[right] - tar
                        res = best + target
                    right -= 1
                else:

                    if tar - nums[left] - nums[right] < best:
                        best = tar - nums[left] - nums[right]
                        res = target - best
                    left += 1
        return res
                            
sl = Solution()
print sl.threeSumClosest([0,0,0], 1)
