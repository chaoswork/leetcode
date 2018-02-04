#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sun Feb  4 21:24:51 2018
Brief: https://leetcode.com/problems/reverse-nodes-in-k-group/description/
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of k then
 left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""

import sys
from utils.listnode import *


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        fakehead = ListNode(0)
        fakehead.next = head

        cur = fakehead
        forward = fakehead
        count = 0
        stack = []
        while forward:
            count += 1
            forward = forward.next
            if forward is None:
                break
            stack.append(forward)
            if count % k == 0:
                cur.next = forward
                stage_next = forward.next
                for i in range(k - 1, 0, -1):
                    stack[i].next = stack[i - 1]
                stack[0].next = stage_next
                cur = stack[0]
                forward = stack[0]
                stack = []
        return fakehead.next


lists = sys.argv[1].split(',')
k = int(sys.argv[2])

head = buildList(lists)
head.display()
sol = Solution()
result = sol.reverseKGroup(head, k)
result.display()
print sol.reverseKGroup(None, k)
