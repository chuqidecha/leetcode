#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-22 上午10:00
# @Author  : yinwb
# @File    : leetcode009.py

class Solution:
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tmp = x
        res = 0
        while tmp != 0:
            res = res * 10 + tmp % 10
            tmp = tmp // 10

        return res == x

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x %10 == 0 and x != 0):
            return False

        res = 0
        while res < x:
            res = res * 10 + x % 10
            x = x // 10

        return res == x or res // 10 == x


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(100))
