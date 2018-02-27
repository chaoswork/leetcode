#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb 27 17:01:16 2018
Brief: https://leetcode.com/problems/unique-paths/description/

A robot is located at the top-left corner of a m x n grid (marked 'Start'
in the diagram below).

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid (marked 'Finish'
in the diagram below).

How many possible unique paths are there?
"""
import sys


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[1 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                count[i][j] = count[i - 1][j] + count[i][j - 1]
        for item in count:
            print item

        return count[n - 1][m - 1]


sol = Solution()
count = sol.uniquePaths(int(sys.argv[1]), int(sys.argv[2]))
