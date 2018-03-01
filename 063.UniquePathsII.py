#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Tue Feb 27 17:01:16 2018
Brief: https://leetcode.com/problems/unique-paths-ii/description/

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique
paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
import sys


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0:
            return 0
        m = len(obstacleGrid[0])
        if m == 0:
            return 0
        count = [[1 - obstacleGrid[i][j] for j in range(m)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    count[i][j] = 0
                else:
                    left = count[i - 1][j] if i > 0 else 0
                    top = count[i][j - 1] if j > 0 else 0
                    count[i][j] = left + top
        # for item in count:
        #    print item

        return count[n - 1][m - 1]


sol = Solution()
a = [
    [1]
]
print sol.uniquePathsWithObstacles(a)
