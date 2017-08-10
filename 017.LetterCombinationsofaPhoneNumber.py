#!/usr/bin/env python
# coding: utf-8

"""
Author:	Chao Huang
Date:		Thu Apr 13 14:31:02 2017
Breif: Given a digit string, return all possible letter
combinations that the number could represent.

A mapping of digit to letters (just like on the
telephone buttons) is given below.

https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
"""


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = {'2': 'abc',
                      '3': 'def',
                      '4': 'ghi',
                      '5': 'jkl',
                      '6': 'mno',
                      '7': 'pqrs',
                      '8': 'tuv',
                      '9': 'wxyz'}
        result = [""]
        for d in digits:
            new_result = []
            for prefix in result:
                for c in letter_map[d]:
                    new_result.append(prefix + c)
            result = new_result
        return result


if __name__ == '__main__':
    sol = Solution()
    print sol.letterCombinations('23')
