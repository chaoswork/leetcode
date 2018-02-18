#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb 18 20:24:58 2018
Brief: https://leetcode.com/problems/permutations-ii/description/

Given a collection of numbers that might contain duplicates, return
all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
import sys


class Solution(object):
    def dp(self, nums):
        if len(nums) <= 1:
            return [nums]
        result = []
        res_idmap = set()

        for i in range(0, len(nums)):
            suffix = nums[:i] + nums[i + 1:]
            suffixid = tuple(sorted(suffix))
            if suffixid in Solution.buff:
                cur = Solution.buff[suffixid]
            else:
                cur = self.dp(suffix)
                Solution.buff[suffixid] = cur
            for item in cur:
                temp = [nums[i]] + item
                tempid = tuple(temp)
                if tempid not in res_idmap:
                    result.append(temp)
                    res_idmap.add(tempid)
        return result

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.buff = {}
        return map(lambda x: list(x), self.dp(nums))


sol = Solution()
print sol.permuteUnique(sys.argv[1].split(','))
