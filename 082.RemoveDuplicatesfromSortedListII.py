#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Fri Mar  2 16:11:51 2018
Brief: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        fakehead = ListNode(head.val + 1)
        cur = head
        last = fakehead
        glast = fakehead
        isdup = False
        while cur:
            if last.val == cur.val:
                isdup = True
            else:
                if isdup:
                    glast.next = cur
                else:
                    glast.next = last
                    glast = last
                isdup = False
            last = cur
            cur = cur.next
        if isdup:
            glast.next = None
        else:
            glast.next = last
        return fakehead.next


lst = buildList([1, 1, 2, 3, 3, 4])
sol = Solution()
res = sol.deleteDuplicates(lst)
print res
