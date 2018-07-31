#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-22 上午10:35
# @Author  : yinwb
# @File    : leetcode008.py

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import math
        maxInt = int(math.pow(2, 31) - 1)

        validChar = [repr(i) for i in range(10)]

        index = 0
        while index < len(str) and str[index] == ' ':
            index += 1

        sign = 1
        if index == len(str):
            return 0
        elif str[index] == '+':
            index += 1
        elif str[index] == '-':
            sign = -1
            index += 1
        elif str[index] == 0:
            return 0
        else:
            if str[index] not in validChar:
                return 0

        res = 0
        for next in range(index, len(str)):
            if str[next] in validChar:
                if res > maxInt // 10:
                    return maxInt * sign if sign == 1 else -maxInt - 1
                elif res == maxInt // 10 and sign == -1 and int(str[next]) > 8:
                    return -maxInt - 1
                elif res == maxInt // 10 and sign == 1 and int(str[next]) > 7:
                    return maxInt
                else:
                    res = res * 10 + int(str[next])
            else:
                break
        return res * sign


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("-2147483648"))
    print(solution.myAtoi('          '))
    print(solution.myAtoi('words and 987'))
    print(solution.myAtoi('4193 with words'))
    print(solution.myAtoi('   -42'))
