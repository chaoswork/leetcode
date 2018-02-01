#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Tue May 24 15:46:26 2016

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string, find the length of the longest substring without repeating
# characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Solution:
        """
        if not s:
            return 0
        f = [0] * len(s)
        f[0] = 1
        last = {}
        last[s[0]] = 0
        # best = s[0]
        for i in range(1, len(s)):
            if s[i] not in last or last[s[i]] < i - f[i - 1]:
                f[i] = f[i - 1] + 1
            else:
                f[i] = i - last[s[i]]
            # if f[i] > len(best):
            #    best = s[i - f[i] + 1: i + 1]
            last[s[i]] = i

        return max(f)


if __name__ == '__main__':
    import sys
    sol = Solution()
    print sol.lengthOfLongestSubstring(sys.argv[1])
