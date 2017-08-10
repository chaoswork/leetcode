#!/usr/bin/env python
# coding: utf-8

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution.
# 
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_index = {}
        for i in range(0, len(nums)):
            nums_index[nums[i]] = i
        for i in range(0, len(nums)):
            rest = target - nums[i]
            if rest in nums_index and nums_index[rest] != i:
                return [i, nums_index[rest]]
            
