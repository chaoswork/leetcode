#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Mon Feb 26 19:57:12 2018
Brief: https://leetcode.com/problems/merge-intervals/description/

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '(%d, %d)' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        int_sort = sorted(intervals, key=lambda x: x.start)
        result = []
        begin = int_sort[0]
        for item in int_sort:
            if item.start <= begin.end:
                if item.end > begin.end:
                    begin.end = item.end
            else:
                result.append(begin)
                begin = item
        result.append(begin)
        return result
