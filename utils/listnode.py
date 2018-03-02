#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb  4 20:56:33 2018
Brief: ListNode of leetcode
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        cur = self
        while cur:
            print cur.val, '->',
            cur = cur.next
        print 'None'

    def __str__(self):
        cur = self
        result = ''
        while cur:
            result = ''.join([result, str(cur.val), '->'])
            cur = cur.next
        result += 'None'
        return result


def buildList(ls):
    """
    list to nodelist
    """
    head = None
    for x in reversed(ls):
        cur = head
        head = ListNode(x)
        head.next = cur
    return head
