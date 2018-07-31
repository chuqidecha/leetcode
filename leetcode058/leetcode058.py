#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-31 下午9:54
# @Author  : yinwb
# @File    : leetcode058.py
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i == -1:
            return 0
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
