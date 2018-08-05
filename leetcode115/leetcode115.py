#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-4 上午11:06
# @Author  : yinwb
# @File    : leetcode115.py

class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(len(s)):
            before = 1
            for j in range(min(i + 1, len(t))):
                tmp = dp[j + 1]
                if s[i] == t[j]:
                    dp[j + 1] = dp[j + 1] + before
                before = tmp
        return dp[-1]

    def numDistinct2(self, s, t):
        if len(t) == 0:
            return 1
        if len(s) < len(t):
            return 0
        total = 0
        for i, si in enumerate(s):
            if si == t[0]:
                total += self.numDistinct2(s[i + 1:], t[1:])
        return total


if __name__ == "__main__":
    print(Solution().numDistinct2("rabbbit","rabbit"))
    print(Solution().numDistinct2("babgbag","bag"))
    print(Solution().numDistinct("rabbbit","rabbit"))
    print(Solution().numDistinct("babgbag","bag"))