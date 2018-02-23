#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Thu Feb 22 21:01:26 2018
Brief: https://leetcode.com/problems/wildcard-matching/description/

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
import sys


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        slen = len(s)
        plen = len(p)
        si = 0
        pi = 0
        lastsi = None
        lastpi = None
        while si < slen:
            if pi < plen and (s[si] == p[pi] or p[pi] == '?'):
                si += 1
                pi += 1
            elif pi < plen and p[pi] == '*':
                lastsi = si + 1
                lastpi = pi
                pi += 1
            elif lastpi is not None:
                pi = lastpi
                si = lastsi
            else:
                return False

        return p[pi:].count('*') == (plen - pi)


sol = Solution()
print sol.isMatch("aaabbbbaaaabbabbbbaabbabaaababaababaaaaaaabaaababbaababbaababbbaaaaabaabbabbaabaababbaabababbbbbbbbabbaabbaaabaababaabaababababababbbbbbabbabbaabbaabaaaaaababaabbbaaabaaabbbbbbbbbaabaabaaabaaabbabbabb",
"****a*b*b**b*bbb*b**bba***b**b*b*b**ba***b*b*a*b*b*****a**aaa*baaa*ba*****a****ba*a****a**b*******a*a")
