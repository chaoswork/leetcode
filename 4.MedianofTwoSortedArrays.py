#!/usr/bin/env python
# coding: utf-8

# Author:	Chao Huang
# Date:		Sat May 28 15:00:54 2016

# https://leetcode.com/problems/median-of-two-sorted-arrays/
# There are two sorted arrays nums1 and nums2 of size m and n
# respectively. Find the median of the two sorted arrays. The overall run
# time complexity should be O(log (m+n)).


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        Also solve the problem of find the kth number from two sorted array
        """
        lnm = len(nums1) + len(nums2)
        if lnm % 2:
            # the array index should be lnm/2, but the count index is (lnm/2 + 1)
            return self.findkth(nums1, nums2, lnm / 2 + 1)
        else:
            small = self.findkth(nums1, nums2, lnm / 2 + 1)
            large = self.findkth(nums1, nums2, lnm / 2)
            return (small + large) / 2.0

    def findkth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        Ak = None
        if len(A) >= k / 2:
            Ak = A[k / 2 - 1]
        Bk = None
        if len(B) >= k / 2:
            Bk = B[k / 2 - 1]

        # if Ak == None, drop B[:k/2]
        # if Bk == None, drop A[:k/2]
        # if Ak < Bk, drop A[:k/2]
        # if Ak == Bk, drop A[:k/2] or B[:k/2]
        # if Ak > Bk, drop B[:k/2]
        if Bk == None or (Ak != None and Ak < Bk):
            # drop A[:k/2]
            return self.findkth(A[k / 2:], B, k - k / 2)
        return self.findkth(A, B[k / 2:], k - k / 2)


sl = Solution()
print sl.findkth([1, 3, 4, 5, 7, 9, 10], [2, 4, 6, 8, 9], 6)

print sl.findMedianSortedArrays(
    [1, 2, 6, 9, 10, 13, 17, 18, 19, 27, 28, 47, 56, 78, 90], [3, 5, 8])
