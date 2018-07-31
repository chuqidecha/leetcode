#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-31 下午9:52
# @Author  : yinwb
# @File    : leetcode055.py
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        i = 0
        while i <= far and i < len(nums):
            far = far if far > nums[i] + i else nums[i] + i
            i += 1

        return i == len(nums)
