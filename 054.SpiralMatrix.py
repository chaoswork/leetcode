#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Mon Feb 26 20:19:07 2018
Brief: https://leetcode.com/problems/spiral-matrix/description/

Given a matrix of m x n elements (m rows, n columns), return all
elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
import sys


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []
        total = n * m
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        start = [0, 0]
        result = [matrix[start[0]][start[1]]]
        step = [m, n, m, n]
        while n > 0 and m > 0:
            right = -1
            for k in range(0, 3):
                for i in range(0, step[k] - 1):
                    start[0] += direction[k][0]
                    start[1] += direction[k][1]
                    if right < start[1]:
                        right = start[1]
                    # print 'debug, ]', start
                    result.append(matrix[start[0]][start[1]])
            for i in range(0, step[3] - 2):
                start[0] += direction[3][0]
                start[1] += direction[3][1]
                # print 'debug, [', start
                result.append(matrix[start[0]][start[1]])
            if len(result) >= total:
                result = result[:total]
                break
            else:
                start[0] += direction[0][0]
                start[1] += direction[0][1]
                result.append(matrix[start[0]][start[1]])
                # print 'debug->', start
            print result
            step = map(lambda x: x - 2, step)
        return result


sol = Solution()
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [
    [1, 4],
    [5, 8],
    [9, 12],
    [13, 16]]
print sol.spiralOrder(b)
