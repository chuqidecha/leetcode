#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-2 下午9:29
# @Author  : yinwb
# @File    : leetcode052.py

class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        return self.helper(n, [])

    def helper(self, n, items):
        if len(items) == n:
            return 1
        res = 0
        for i in range(n):
            # 如果该列已经有Queen，则跳过
            if i in items:
                continue
            nextRes = None
            able = True
            # 如果当前为第一个，则直接放置Queen
            if len(items) == 0:
                pass
            else:
                # 判断对角线上是否有Queen
                for index, item in enumerate(items):
                    if abs(index - len(items)) == abs(item - i):
                        able = False
                        break
            if able:
                next = items[:]
                next.append(i)
                res += self.helper(n, next)
        return res
