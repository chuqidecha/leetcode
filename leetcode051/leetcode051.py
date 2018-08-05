#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-2 下午9:27
# @Author  : yinwb
# @File    : leetcode051.py
def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    items = self.helper(n, [])
    res = []
    for item in items:
        tmp = [["."] * n for _ in range(n)]
        for row, col in enumerate(item):
            tmp[row][col] = "Q"
        res.append(["".join(row) for row in tmp])
    return res


def helper(self, n, items):
    if len(items) == n:
        return [items]
    resItems = []

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
            resItems.extend(self.helper(n, next))
    return resItems
