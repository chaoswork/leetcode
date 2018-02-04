#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:	Chao Huang (huangchao.cpp@gmail.com)
Date: Sat Feb  3 22:38:32 2018
Brief: https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
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


def buildList(ls):
    head = None
    for x in ls:
        cur = head
        head = ListNode(x)
        head.next = cur
    return head



from heapq import heappush, heappop


class PriorityQueue:
    def __init__(self):
        self._queue = []

    def put(self, item):
        heappush(self._queue, item)

    def get(self):
        return heappop(self._queue)

    def empty(self):
        return len(self._queue) == 0


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        pq = PriorityQueue()
        for i in range(0, len(lists)):
            if lists[i]:
                pq.put((lists[i].val, i))
        while not pq.empty():
            min_indx = pq.get()[1]

            temp = lists[min_indx]
            lists[min_indx] = lists[min_indx].next
            temp.next = None
            cur.next = temp
            cur = cur.next
            if lists[min_indx]:
                pq.put((lists[min_indx].val, min_indx))

        return head.next


l1 = buildList([4, 2, 1])
l1.display()
l2 = buildList([4, 3, 1])
l2.display()
l3 = buildList([5, 4, 2])
l3.display()

sol = Solution()
import sys
sol.mergeKLists([l1, l2, l3]).display()
print sol.mergeKLists([])
print sol.mergeKLists([[]])
