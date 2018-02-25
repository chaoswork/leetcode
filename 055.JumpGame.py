#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb 25 11:40:24 2018
Brief: https://leetcode.com/problems/jump-game/description/

Given an array of non-negative integers, you are initially positioned at the
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        right = -1
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i + nums[i] <= right:
                break
            for j in range(nums[i]):
                if i + j >= len(nums):
                    break
                result[i + j] = 1
            if right < i + nums[i]:
                right = i + nums[i]
        return result[len(nums) - 1] == 1
