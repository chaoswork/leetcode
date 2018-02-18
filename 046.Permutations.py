#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb 18 20:24:58 2018
Brief: https://leetcode.com/problems/permutations/description/

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
import sys


class Solution(object):
    def dp(self, nums):
        if len(nums) <= 1:
            return [nums]
        result = []

        for i in range(0, len(nums)):
            cur = self.dp(nums[:i] + nums[i + 1:])
            for item in cur:
                result.append([nums[i]] + item)
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dp(nums)


sol = Solution()
print sol.permute(sys.argv[1].split(','))
