#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Feb  2 15:50:05 2018
Brief: https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list. The new list should
 be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        while l1 or l2:
            if l1 is None:
                cur.next = l2
                break
            if l2 is None:
                cur.next = l1
                break

            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
                tmp.next = None
                cur.next = tmp
            else:
                tmp = l2
                l2 = l2.next
                tmp.next = None
                cur.next = tmp
            cur = cur.next
        return head.next


def buildList(ls):
    head = None
    for x in ls:
        cur = head
        head = ListNode(x)
        head.next = cur
    return head


l1 = buildList([4, 2, 1])
l1.display()
l2 = buildList([4, 3, 1])
l2.display()

sol = Solution()
import sys
sol.mergeTwoLists(l1, l2).display()
