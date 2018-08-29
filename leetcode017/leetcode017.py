#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-29 下午9:34
# @Author  : yinwb
# @File    : leetcode017.py
class Solution:
    NUM_CHAR_MAPPINF = ("abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        return self.helper(digits, 0, "")

    def helper(self, digits, cnt, item):
        if cnt == len(digits):
            return [item]

        cnt_str = self.NUM_CHAR_MAPPINF[int(digits[cnt]) - 2]
        res = []
        for index, char in enumerate(cnt_str):
            cnt_item = item + char
            res.extend(self.helper(digits, cnt + 1, cnt_item))
        return res
