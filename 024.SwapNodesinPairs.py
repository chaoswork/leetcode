#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb  4 20:55:08 2018
Brief: https://leetcode.com/problems/swap-nodes-in-pairs/description/

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values
 in the list, only nodes itself can be changed.

"""

import sys
from utils.listnode import *


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fakehead = ListNode(0)
        fakehead.next = head

        cur = fakehead
        while True:
            if cur is None:
                break
            if cur.next is None:
                break
            if cur.next.next is None:
                break
            cur_next = cur.next
            cur.next = cur_next.next
            cur_next_next = cur_next.next
            cur_next.next = cur_next_next.next
            cur_next_next.next = cur_next
            cur = cur_next
        return fakehead.next


lists = sys.argv[1].split(',')
print lists
head = buildList(lists)
head.display()
sol = Solution()
result = sol.swapPairs(head)
result.display()
print sol.swapPairs(None)
