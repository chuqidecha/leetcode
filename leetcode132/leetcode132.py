#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-10 下午4:34
# @Author  : yinwb
# @File    : leetcode132.py

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindrome = [[False] * len(s) for _ in range(len(s))]
        dp = list(range(len(s) - 1, -2, -1))

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                palindrome[i][j] = s[i] == s[j] and (i == j or i + 1 == j or palindrome[i + 1][j - 1])

                if palindrome[i][j]:
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0]


if __name__ == "__main__":
    print(Solution().minCut("ab"))
