#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Mon Feb 19 19:54:37 2018
Brief: https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input
 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
0,0 -> 0,3
0,1 -> 1,3
0,2 -> 2,3
0,3 -> 3,3
2,2 -> 2,1
1,3 -> 3,2
i,j -> j,n-1-i

beautiful solution: matrix[::] = zip(*matrix[::-1])
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        import copy
        m = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, n):
                ti = j
                tj = n - 1 - i
                matrix[ti][tj] = m[i][j]
