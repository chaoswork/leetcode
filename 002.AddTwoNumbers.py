#!/usr/bin/env python
# coding: utf-8

#Author:	Chao Huang
#Date:		Tue May 24 15:18:54 2016

# https://leetcode.com/problems/add-two-numbers/
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        res = ListNode(0)
        over = 0
        cur = res
        while True:
            cur.val = over
            if l1 != None:
                cur.val += l1.val
                l1 = l1.next
            if l2 != None:
                cur.val += l2.val
                l2 = l2.next
            # if res.val is greater then ten
            if cur.val >= 10:
                cur.val -= 10
                over = 1
            else:
                over = 0
                
            if not l1 and not l2 and over == 0:
                break

            next = ListNode(0)
            cur.next = next
            cur = cur.next
        return res
            
            
            
                
