#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Wed Feb 21 12:11:45 2018
Brief: https://leetcode.com/problems/valid-sudoku/description/
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled
with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
"""


class Solution(object):
    def check_list(self, lst):
        nums_set = set()
        for num in lst:
            if num == '.':
                continue
            if num in nums_set:
                return False
            nums_set.add(num)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        for i in range(n):
            if not self.check_list(board[i]):
                return False
            nums = []
            for j in range(n):
                nums.append(board[j][i])
            if not self.check_list(nums):
                return False
        for i in range(3):
            for j in range(3):
                nums = []
                for p in range(3):
                    for q in range(3):
                        nums.append(board[i * 3 + p][j * 3 + q])
                if not self.check_list(nums):
                    return False
        return True


sol = Solution()
a = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print sol.isValidSudoku(a)
print sol.check_list(['.', '.', '.', '5', '.', '.', '5', '.', '.'])
