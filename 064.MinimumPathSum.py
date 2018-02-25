#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb 25 12:01:27 2018
Brief: https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1
 minimizes the
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0
        for i in range(n):
            for j in range(m):
                if i - 1 < 0:
                    if j - 1 < 0:
                        continue
                    else:
                        grid[i][j] += grid[i][j - 1]
                else:
                    if j - 1 < 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        if grid[i - 1][j] < grid[i][j - 1]:
                            grid[i][j] += grid[i - 1][j]
                        else:
                            grid[i][j] += grid[i][j - 1]
        # print grid
        return grid[n - 1][m - 1]


sol = Solution()
mat = [[1, 3, 1],
       [1, 5, 1],
       [4, 2, 1]]
sol.minPathSum(mat)
