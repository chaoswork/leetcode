#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Mon Feb 26 20:19:07 2018
Brief: https://leetcode.com/problems/spiral-matrix-ii/description/

Given an integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
import sys


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        total = n * n
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        start = [0, 0]
        count = 1
        matrix = [[0 for i in range(n)] for j in range(n)]
        matrix[start[0]][start[1]] = count
        count += 1
        step = [n, n, n, n]
        while n > 0:
            right = -1
            for k in range(0, 3):
                for i in range(0, step[k] - 1):
                    start[0] += direction[k][0]
                    start[1] += direction[k][1]
                    if right < start[1]:
                        right = start[1]
                    # print 'debug, ]', start
                    matrix[start[0]][start[1]] = count
                    count += 1
            for i in range(0, step[3] - 2):
                start[0] += direction[3][0]
                start[1] += direction[3][1]
                # print 'debug, [', start
                matrix[start[0]][start[1]] = count
                count += 1
            if count > total:
                break
            else:
                start[0] += direction[0][0]
                start[1] += direction[0][1]
                matrix[start[0]][start[1]] = count
                count += 1
                # print 'debug->', start
            step = map(lambda x: x - 2, step)
        return matrix


sol = Solution()
mat = sol.generateMatrix(int(sys.argv[1]))
for item in mat:
    print item
