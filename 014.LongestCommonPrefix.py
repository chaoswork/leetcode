#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Thu Jun 16 11:32:32 2016

# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        res = ""
        for i in range(0, len(strs[0])):
            same = True
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    same = False
                    break
            if same:
                res += strs[0][i]
            else:
                break
        return res

sl = Solution()
print sl.longestCommonPrefix(['12345', '123', '125'])
                    
