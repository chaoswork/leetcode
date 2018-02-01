#!/usr/bin/env python
# coding: utf-8

"""
Author: Chao Huang
Date:   Thu Feb  1 15:22:34 2018
Breif: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.


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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        target = length - n
        if target == 0:
            return head.next
        cur = ListNode(0)
        cur.next = head
        while target > 0:
            target -= 1
            cur = cur.next
        cur.next = cur.next.next
        return head


head = None
for x in [5, 4, 3, 2, 1]:
    cur = head
    head = ListNode(x)
    head.next = cur

head.display()
sol = Solution()
import sys
sol.removeNthFromEnd(head, int(sys.argv[1])).display()
