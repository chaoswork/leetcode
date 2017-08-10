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
        Solution: Greedy
        """
# this is my first submition.
# in fact, wi stores some consecutive numbers
#         res = 0
#         wi = {} # store the index
#         last = ""
#         for i in range(0, len(s)):
#             if s[i] == last:
#                 wi.clear()
#                 wi[s[i]] = i
#             else:
#                 if s[i] in wi:
#                     idx = wi[s[i]]
#                     wi.clear()
#                     for k in range(idx + 1, i + 1):
#                         wi[s[k]] = k
#                 else:
#                     wi[s[i]] = i
#                     
#             if res < len(wi):
#                 res = len(wi)
#             last = s[i]
#         return res

        res = 0
        wl = 0 # left index
        wr = 0 # right index
        wi = {}
        last = ""
        for i in range(0, len(s)):
            if s[i] == last:
                wl = i
            else:
                if s[i] in wi and wi[s[i]] <= wr and wi[s[i]] >= wl:
                    wl = wi[s[i]] + 1
                  
            wi[s[i]] = i
            wr = i
                    
            if res < wr - wl + 1:
                res = wr - wl + 1
            last = s[i]
        return res
                
                
                
            
