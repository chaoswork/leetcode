#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Feb 22 20:02:06 2018
Brief: https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the
 first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from
index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""
import sys


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [0] * len(nums)
        last = [0] * len(nums)
        for i in range(len(nums)):
            if i + nums[i] <= last[i]:
                continue
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                if i + j <= last[i]:
                    continue
                if result[i + j] == 0 or result[i + j] > result[i] + 1:
                    result[i + j] = result[i] + 1
                    last[i + j] = i + nums[i]
        print result
        print last
        return result[-1]


sol = Solution()
sol.jump(map(lambda x: int(x), sys.argv[1].split(',')))
