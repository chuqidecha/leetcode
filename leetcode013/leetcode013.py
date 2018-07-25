#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-25 下午9:05
# @Author  : yinwb
# @File    : leetcode013.py

class Solution:
    def romanToInt(self, s):
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sLen = len(s)
        cnt = 0
        num = 0
        while cnt < sLen:
            if cnt + 1 < sLen and romanDict[s[cnt]] < romanDict[s[cnt + 1]]:
                num += (romanDict[s[cnt + 1]] - romanDict[s[cnt]])
                cnt += 2
            else:
                num += romanDict[s[cnt]]
                cnt += 1

        return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('III'))
    print(solution.romanToInt('IV'))
    print(solution.romanToInt('IX'))
    print(solution.romanToInt('LVIII'))
    print(solution.romanToInt('MCMXCIV'))
