#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Mar  2 16:11:51 2018
Brief: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

from utils.listnode import *


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        last = None
        while cur:
            if last is None:
                last = cur
            else:
                if last.val == cur.val:
                    last.next = cur.next
                else:
                    last = cur

            cur = cur.next
        return head


lst = buildList([1, 1, 2, 3, 3])
sol = Solution()
res = sol.deleteDuplicates(lst)
print res
