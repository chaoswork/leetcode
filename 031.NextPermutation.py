#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Wed Feb  7 15:19:02 2018
Brief: https://leetcode.com/problems/next-permutation/description/

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
import sys


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while nums[i] >= nums[i + 1]:
            i = i - 1
            if i < 0:
                break
        if i < 0:
            nums.sort()
            return
        swap_i = i + 1
        min_value = nums[i + 1]
        for j in range(i + 2, len(nums)):
            if nums[j] <= nums[i]:
                continue
            if nums[j] < min_value:
                swap_i = j
                min_value = nums[j]
        print id(nums)
        nums[i], nums[swap_i] = nums[swap_i], nums[i]

        nums_st = sorted(nums[i + 1:])
        for j in range(i + 1, len(nums)):
            nums[j] = nums_st[j - i - 1]


lists = sys.argv[1].split(',')

sol = Solution()
print sol.nextPermutation(lists)
