#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-28 下午2:32
# @Author  : yinwb
# @File    : leetcode023.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        mergedList = lists[0]

        for i in range(1, len(lists)):
            cntList = lists[i]
            tmpList = ListNode(0)
            node1 = mergedList
            node2 = cntList
            node3 = tmpList
            while node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    node3.next = node1
                    node1 = node1.next
                else:
                    node3.next = node2
                    node2 = node2.next
                node3 = node3.next
            else:
                node3.next = node2 if node1 is None else node2
                mergedList = tmpList.next
        return mergedList


if __name__ == "__main__":
    arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = []
    for array in arrays:
        tmpList = ListNode(0)
        node = tmpList
        for elem in array:
            node.next = ListNode(elem)
            node = node.next
        lists.append(tmpList.next)
    solution = Solution()
    solution.mergeKLists(lists)
