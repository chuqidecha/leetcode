#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-10 下午1:43
# @Author  : yinwb
# @File    : leetcode131.py

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                palindrome[i][j] = s[i] == s[j] and (i == j or i + 1 == j or palindrome[i + 1][j - 1])

        return self.helper(s,0,palindrome,[])

    def helper(self, s, start, palindrome, item):
        if len(s) == start:
            return [item]
        items = []
        for i in range(start, len(s)):
            if palindrome[start][i]:
                cntItem = item[:]
                cntItem.append(s[start:i+1])
                items.extend(self.helper(s,i+1,palindrome,cntItem))

        return items


if __name__ == "__main__":
    print(Solution().partition("aabaa"))
