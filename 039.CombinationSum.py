#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb 17 21:29:27 2018
Brief: https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (C) (without duplicates) and a target number
(T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

import sys


class Solution(object):
    def dfs(self, cand, target, prev_result, debug):
        """
        dfs for dp
        """
        # print debug, cand, target, prev_result
        if target == 0:
            self.result.append(prev_result)
            return True
        if len(cand) == 0 or target < 0:
            return False
        self.dfs(cand, target - cand[0], prev_result + [cand[0]], debug + '-')
        self.dfs(cand[1:], target, prev_result, debug + '=')

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(list(set(candidates)), target, [], '')
        return self.result


sol = Solution()
cand = map(lambda x: int(x), sys.argv[1].split(','))
target = int(sys.argv[2])
print sol.combinationSum(cand, target)
