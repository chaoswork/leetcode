#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Mon Jun 13 11:56:08 2016

# https://leetcode.com/problems/regular-expression-matching/

# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true


class Solution(object):
    def match(self, s, j, p, i):
        """
        dp
        """
        if i == len(p) and j == len(s):
            return 1
        if i == len(p) or j == len(s):
            return 0
        # print i, j, Solution.buff[i][j], s[j:], p[i:]

        if Solution.buff[i][j] != -1:
            return Solution.buff[i][j]
        if p[i] == '.' or s[j] == p[i]:
            # print 'debug-equal'
            if self.match(s, j + 1, p, i + 1) == 1:
                Solution.buff[i][j] = 1
                return 1

        if p[i] == '*':
            # match zero prev
            # print 'debug-match zero'
            if self.match(s, j, p, i + 1) == 1:
                Solution.buff[i][j] = 1
                return 1
            if i > 0:
                prev = p[i - 1]
                if prev == '.':
                    # print 'debug: prev = .'
                    for jj in range(j, len(s)):
                        if self.match(s, jj + 1, p, i + 1) == 1:
                            Solution.buff[i][j] = 1
                            return Solution.buff[i][j]
                else:
                    # print 'debug: prev = ', prev
                    for jj in range(j, len(s)):
                        if s[jj] == prev:
                            if self.match(s, jj + 1, p, i + 1) == 1:
                                Solution.buff[i][j] = 1
                                return Solution.buff[i][j]
                        else:
                            break
        if i < len(p) - 1 and p[i + 1] == '*':
            return self.match(s, j, p, i + 2)

        Solution.buff[i][j] = 0
        return 0

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        if a[i] == '.*' match(i + 2, j...)
        if a[i] == '.' match(i + 1, j + 1)
        if a[i] == other, if same, match(i + 1, j + 1)
        if a[i] == '*', match(i+1, prev...)
        """
        s = 'A' + s + 'B'
        p = 'A' + p + 'B'
        Solution.buff = [[-1 for j in range(len(s))] for i in range(len(p))]
        print '---', s, len(s), p, len(p)
        return self.match(s, 0, p, 0) == 1


if __name__ == '__main__':
    sol = Solution()
    print sol.isMatch("ab", ".*c") is False
    print sol.isMatch("aa", "a") is False
    print sol.isMatch("aa", "aa") is True
    print sol.isMatch("aaa", "aa") is False
    print sol.isMatch("aa", "a*") is True
    print sol.isMatch("aa", ".*") is True
    print sol.isMatch("ab", ".*") is True
    print sol.isMatch("aab", "c*a*b") is True
    print sol.isMatch("aaa", "a*a") is True
    print sol.isMatch("", "b*") is True
    print sol.isMatch("bbbba", ".*a*a") is True
    print sol.isMatch("a", "a*a") is True
    print sol.isMatch("aa", "b*a") is False
    print sol.isMatch("aaaaaaaaaaaaab",
                      "a*a*a*a*a*a*a*a*a*a*c") is False
