#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-21 下午9:34
# @Author  : yinwb
# @File    : leetcode007.py

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        maxInt = (math.pow(2, 31) - 1) // 10

        res = 0

        sign, x = (-1, -x) if x < 0 else (1, x)

        while x != 0:
            remainder = x % 10
            if res > maxInt:
                return 0
            elif res == maxInt and (sign * remainder < -8 or sign * remainder > 7):
                return 0
            else:
                res = res * 10 + remainder
                x = x // 10
        return sign * res


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(123))
