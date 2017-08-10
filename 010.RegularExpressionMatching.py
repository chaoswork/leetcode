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
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = []
        for i in range(0, len(p)):
            if i + 1 < len(p) and p[i + 1] == '*':
                pattern.append(p[i: i + 2])
                continue
            if p[i] == '*':
                continue
            pattern.append(p[i])
        new_p = []
        for item in pattern:
            if len(item) == 2:
                if len(new_p) and len(new_p[-1]) == 2:
                    if new_p[-1] == item:
                        continue
            new_p.append(item)
        # print ''.join(new_p)
        return self.match_here(s, ''.join(new_p))

    def match_here(self, s, p):
        """
        从当前开始匹配
        """
        # print 'debug-here: s=%s,p=%s' % (s, p)
        if s == "" and p == "":
            return True

        if len(p) > 1 and p[1] == '*':
            return self.match_star(p[0], p[2:], s)

        if len(s) and len(p) and (s[0] == p[0] or p[0] == '.'):
            return self.match_here(s[1:], p[1:])

        return False

    def match_star(self, cur, rest_p, s):
        """
        匹配 x*
        """
        # print 'debug-star:[cur=%s,rest_p=%s,s=%s]' % (cur, rest_p, s)
        if rest_p == "" and s == "":
            return True
        if cur == '.':
            for i in range(0, len(s) + 1):
                if self.match_here(s[i:], rest_p):
                    return True
        else:
            # 找到第一个不是cur的坐标
            cur_index = 0
            while cur_index < len(s) and s[cur_index] == cur:
                # print 'debug,i=', i, cur, s[i]
                cur_index += 1
            # print 'debug, cur_index=%d' % cur_index
            for i in range(0, cur_index + 1):
                # print 'debug: s[i:]=%s,rest_p=%s' % (s[i:], rest_p)
                if self.match_here(s[i:], rest_p):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
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
