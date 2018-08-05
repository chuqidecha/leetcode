#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-5 下午2:24
# @Author  : yinwb
# @File    : leetcode072.py

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[i] * (len(word2) + 1) for i in range(len(word1) + 1)]
        dp[0][:] = range(len(word2) + 1)


        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)

                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().minDistance(word1 = "horse", word2 = "ros"))
    print(Solution().minDistance(word1 = "intention", word2 = "execution"))