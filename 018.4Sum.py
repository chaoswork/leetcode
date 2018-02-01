#!/usr/bin/env python
# coding: utf-8

"""
Author: Chao Huang
Date:   Thu Feb  1 14:42:28 2018
Breif: https://leetcode.com/problems/4sum/description/

Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array
which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pair_value = {}
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue

                key = nums[i] + nums[j]
                pair_value.setdefault(key, [])
                pair_value[key].append(set([i, j]))
        # find
        result = set()
        for key in pair_value:
            target_left = target - key
            if target_left not in pair_value:
                continue
            for left_set in pair_value[target_left]:
                for right_set in pair_value[key]:
                    merge = left_set | right_set
                    if len(merge) == 4:
                        cand = map(lambda x: nums[x], list(merge))
                        result.add(tuple(sorted(cand)))
        return map(lambda x: list(x), result)


sol = Solution()
print sol.fourSum([1, 0, -1, 0, -2, 2], 0)
