#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-31 下午10:04
# @Author  : yinwb
# @File    : leetcode084.py

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stackHeight = []
        maxArea = 0
        i = 0
        heights.append(0)
        while i < len(heights):
            top = len(stackHeight)
            if top == 0 or heights[stackHeight[top - 1]] <= heights[i]:
                stackHeight.append(i)
                i += 1
            else:
                tmp = stackHeight.pop()
                top = len(stackHeight)
                area = heights[tmp] * (i if top == 0 else i - stackHeight[top - 1] - 1)
                if area > maxArea:
                    maxArea = area

        return maxArea


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([1]))