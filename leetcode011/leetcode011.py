#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-24 下午10:49
# @Author  : yinwb
# @File    : leetcode011.py

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            if height[r] < height[l]:
                cntArea = height[r] * (r - l)
                r -= 1
            else:
                cntArea = height[l] * (r - l)
                l += 1
            area = area if area > cntArea else cntArea
        return area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
