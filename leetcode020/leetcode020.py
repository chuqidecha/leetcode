#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-29 下午9:35
# @Author  : yinwb
# @File    : leetcode020.py

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if len(stack) == 0 or char in ('(','{','['):
                stack.append(char)
            else:
                if char == ')' and stack[-1] != '(':
                    return False
                elif char == '}' and stack[-1] != '{':
                    return False
                elif  char == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0