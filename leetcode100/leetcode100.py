#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-28 下午5:01
# @Author  : yinwb
# @File    : leetcode100.py

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pQue = deque()
        qQue = deque()

        pQue.append(p)
        qQue.append(q)

        while len(pQue) > 0 and len(qQue) > 0:
            pNode = pQue.popleft()
            qNode = qQue.popleft()
            if pNode is None and qNode is None:
                continue
            elif pNode is not None and qNode is not None and pNode.val == qNode.val:
                pQue.extend([pNode.left, pNode.right])
                qQue.extend([qNode.left, qNode.right])
            else:
                return False
        else:
            if len(pQue) != len(qQue):
                return False

        return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    solution.isSameTree(root,root)