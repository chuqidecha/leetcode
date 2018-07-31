#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-31 下午9:57
# @Author  : yinwb
# @File    : leetcode085.py
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        rows, cols = len(matrix), len(matrix[0])

        hists = [[0] * (cols + 1) for _ in range(rows)]
        hists[0][:cols] = [int(i) for i in matrix[0]]

        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    hists[i][j] = hists[i - 1][j] + 1

        maxRect = 0
        for i in range(rows):
            stack = []
            j = 0
            while j < cols + 1:
                if len(stack) == 0 or hists[i][j] >= hists[i][stack[len(stack) - 1]]:
                    stack.append(j)
                    j += 1
                else:
                    top = stack[len(stack) - 1]
                    stack.pop()
                    area = hists[i][top] * (j - (-1 if len(stack) == 0 else stack[len(stack) - 1]) - 1)
                    maxRect = maxRect if maxRect > area else area
        return maxRect
