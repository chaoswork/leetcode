#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb 17 21:29:27 2018
Brief: https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

import sys


class Solution(object):
    def dfs(self, cand, start, target, prev_result):
        """
        dfs for dp
        """
        # print debug, cand, target, prev_result
        if target == 0:
            self.result.add(tuple(prev_result))
            return True
        for i in range(start, len(cand)):
            if cand[i] > target:
                return False

            self.dfs(cand, i + 1, target - cand[i],
                     prev_result + [cand[i]])
            # self.dfs(cand, i + 1, target, prev_result)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.result = set()
        self.dfs(candidates, 0, target, [])
        return map(lambda x: list(x), self.result)


sol = Solution()
cand = map(lambda x: int(x), sys.argv[1].split(','))
target = int(sys.argv[2])
print sol.combinationSum2(cand, target)
