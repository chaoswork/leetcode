#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Thu Jun 16 11:44:19 2016

# https://leetcode.com/problems/3sum/

# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:

#    [
#      [-1, 0, 1],
#      [-1, -1, 2]
#    ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while(left < right and nums[right] == nums[right + 1]):
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res
                    

sl = Solution()
print sl.threeSum([-1, 0, 1, 2, -1, -4])
                        
