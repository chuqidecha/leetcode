#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-23 下午9:39
# @Author  : yinwb
# @File    : leetcode019.py


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head

        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        else:
            slow.next = slow.next.next
            return head